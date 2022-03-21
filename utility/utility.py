import re
import os
import shutil
import platform
import pickle
from datetime import datetime
from config import game_config
from config import level_config


DEFAULT_ARTICLE = game_config['ui']['articles']['default']
ARTICLE_MAP = game_config['ui']['articles']['mapped']


def get_os():
    """Returns base operating system name."""

    return platform.system().lower()


def is_empty_response(response):
    """Returns True if the response is valid, otherwise False."""

    if isinstance(response, str):
        return response is None or response.strip() == ''
    elif isinstance(response, int):
        return response == -1
    else:
        return False


def d4_inverse(d4_direction):
    """Returns the inverse of the d4 direction."""

    directions = [0, 1, 2, 3]
    return directions[(d4_direction + 2) % 4]


def d4_to_player_order(player_orientation):
    """Return the d4 index order relative to player orientation."""

    # order of d4 objects
    d4_order = [0, 1, 2, 3]
    # rotate order to match player orientation
    player_order = d4_order[player_orientation:] + d4_order[:player_orientation]
    # swap last two items to make order: front, right, left, behind
    report_order = player_order[:2] + [player_order[3]] + [player_order[2]]

    return report_order


def d4_to_player_list(player_orientation, d4_objects_list):
    """Return the objects list reordered to match player orientation."""

    player_object_list = [d4_objects_list[i]
                          for i in d4_to_player_order(player_orientation)]

    return player_object_list


def d4_duplicate_description(gameobject, d4_objects_list):
    """Returns True if there are any matching descriptions in the list of d4_objects, otherwise False."""

    d4_objects = []

    for obj_list in d4_objects_list:
        d4_objects += obj_list
        matching_object_descriptions = [obj.description.strip().lower()
                                        for obj in d4_objects
                                        if obj.description.strip().lower() == gameobject.description.strip().lower()]

    return len(matching_object_descriptions) > 1


def get_direction(x1, y1, x2, y2):
    """Return the d4 direction from location 1 (x1, y1) to location 2 (x2, y2) for adjacent locations."""

    dx = x2 - x1
    dy = y2 - y1

    if dx == dy or abs(dx) > 1 or abs(dy) > 1:
        raise ValueError("The locations must be adjacent and orthogonal to each other.")

    if dx == 0:
        return 2 if dy == 1 else 0
    else:
        return 1 if dx == 1 else 3


def get_relative_direction_text(orientation, direction):
    """Returns the text description of the direction based on orientation."""

    relative_directions = {
        0: 'in front of me',
        1: 'to my right',
        2: 'behind me',
        3: 'to my left'}

    dirkeys = sorted(relative_directions.keys())
    keyindex = direction - orientation

    return relative_directions[dirkeys[keyindex]]


def get_article(object_description):

    try:
        article = ARTICLE_MAP[object_description]
    except KeyError:
        article = DEFAULT_ARTICLE

    return article


def build_object_list_text(object_list):

    conjunction = 'and'
    delimiter = ','

    object_text = ''

    if len(object_list) == 1:
        obj = object_list[0]
        obj_repr = str(obj)
        object_text = ' '.join([get_article(obj_repr), obj_repr])

    elif len(object_list) == 2:
        obj_1 = object_list[0]
        obj_2 = object_list[1]
        obj_1_repr = str(obj_1)
        obj_2_repr = str(obj_2)
        object_text = ' '.join(
            [get_article(obj_1_repr), obj_1_repr,
             conjunction,
             get_article(obj_2_repr), obj_2_repr])

    elif len(object_list) > 2:
        working_text = (' ' + conjunction + ' ').join(
            [get_article(str(obj)) + ' ' + str(obj) for obj in object_list])
        replace_count = working_text.count(' ' + conjunction) - 1
        object_text = working_text.replace(' ' + conjunction, delimiter, replace_count)

    return object_text


def build_object_report_body(text_part_list):
    """Return string body for object report."""

    conjunction = 'and'
    delimiter = ','
    body_text = ''

    if len(text_part_list) == 1:
        body_text += text_part_list[0]

    elif len(text_part_list) == 2:
        body_text += ' '.join([text_part_list[0], conjunction, text_part_list[1]])

    elif len(text_part_list) > 2:
        initial_parts = text_part_list[:-1]
        final_part = text_part_list[-1]
        initial_text_string = (delimiter + ' ').join(initial_parts)
        body_text += (' ' + conjunction + ' ').join([initial_text_string, final_part])

    return body_text


def build_object_report_text(orientation, d4_objects):
    """Return string description of d4 objects relative to orientation."""

    report_order = d4_to_player_order(orientation)
    report_open = 'There\'s '
    report_body = ''
    report_close = '.'

    body_part_list = []

    for direction in report_order:
        component_list = d4_objects[direction]

        if len(component_list) > 0:
            this_text_part = build_object_list_text(component_list)
            this_text_part += ' ' + get_relative_direction_text(orientation, direction)
            body_part_list.append(this_text_part)

    if len(body_part_list) > 0:
        report_body += build_object_report_body(body_part_list)
    else:
        report_close = 'nothing around me.'

    report = report_open + report_body + report_close

    return report


def build_sensor_readout_text(sensors):
    """Return text to display in sensor console."""

    def value_bar(property):

        empty_char = '-'
        value_char = '|'
        bar_length = 40
        value_length = int(
            (property.value - property.min_value) /
            (property.max_value - property.min_value) *
            bar_length)
        empty_string = empty_char * bar_length
        value_string = value_char * value_length

        return merge_text(empty_string, value_string)

    def value_text(value):

        return merge_text('   ', str(value)[:3])

    properties = sorted([p for s in sensors for p in s.get_properties()], key=lambda x: x.description)

    readout_text = '\n\n'.join([
        '{0}: {1}\n{2} {3} {4} {5}'.format(
            p.description,
            str(p.value)[:3],
            value_text(p.min_value),
            value_bar(p),
            value_text(p.max_value),
            p.units)
        for p in properties])

    return readout_text


def build_weather_readout_text(weather_data):
    """Return text to display in weather station"""

    def display_text(value, units):

        if value is not None:
            return ' '.join((str(value), units)).strip()

        return 'NO DATA'

    weather_data['time'] = datetime.now().strftime('%H:%M:%S')

    sol = display_text(
        weather_data['sol'],
        '')
    time = display_text(
        weather_data['time'],
        '')
    temperature = display_text(
        weather_data['temperature']['value'],
        weather_data['temperature']['units'])
    wind_speed = display_text(
        weather_data['wind']['speed']['value'],
        weather_data['wind']['speed']['units'])
    wind_direction = display_text(
        weather_data['wind']['direction']['value'],
        weather_data['wind']['direction']['units'])
    pressure = display_text(
        weather_data['pressure']['value'],
        weather_data['pressure']['units'])

    readout_text = '\n'.join([
        'Sol/Time: {0} {1}'.format(sol, time),
        'Temperature: {0}'.format(temperature),
        'Wind speed: {0}'.format(wind_speed),
        'Wind direction: {0}'.format(wind_direction),
        'Pressure: {0}'.format(pressure)])

    return readout_text


def build_examination_report_text(gameobject, level):
    """Return text to display for examined game objects."""

    report_text = gameobject.report
    matches = re.findall(r"(\[.*?\])", report_text)

    for m in matches:
        clean = m.replace('[', '').replace(']', '')
        parts = clean.split('-')
        object_type = parts[0]
        config_id = int(parts[1])

        if object_type.lower() == 'device':
            device = level.system.get_device(config_id=config_id)
            device_description = ' '.join((
                device.msg_active_true if device.active else device.msg_active_false,
                device.description))
            device_text = ' '.join((
                get_article(device_description),
                device_description))
            report_text = report_text.replace(m, device_text)

        elif object_type.lower() == 'interface':
            interface = level.system.get_interface(config_id=config_id)
            interface_text = ' '.join((
                get_article(interface.description),
                interface.description))
            report_text = report_text.replace(m, interface_text)

    return report_text


def merge_dicts(a, b):
    """Merge two dictionaries."""

    return {**a, **b}


def merge_dicts_n(iterable):
    """Merge multiple dictionaries."""

    this_dict = iterable.pop(0)
    while len(iterable) > 0:
        this_dict = merge_dicts(this_dict, iterable.pop(0))

    return this_dict


def merge_lists(a, b):
    """Return items from list b substituted with items from a where b value is None."""

    if len(a) != len(b):
        raise ValueError("Lists must have same length.")
    c = []
    for i, j in zip(a, b):
        c.append(j if j is not None else i)
    return c


def merge_text(a, b):
    """Merge the two text blocks aligned to the top-left corner.

    Characters in a will be retained only where they intersect whitespace in b."""

    a_list = a.split('\n')
    b_list = b.split('\n')
    a_rows = len(a_list)
    b_rows = len(b_list)
    a_cols = max([len(row) for row in a_list])
    b_cols = max([len(row) for row in b_list])
    out_rows = max(a_rows, b_rows)
    out_cols = max(a_cols, b_cols)
    out_list = []

    for text_lines in (a_list, b_list):
        if len(text_lines) < out_rows:
            text_lines.extend([''] * (out_rows - len(text_lines)))
        for i in range(len(text_lines)):
            if len(text_lines[i]) < out_cols:
                text_lines[i] += ' ' * (out_cols - len(text_lines[i]))

    for i in range(out_rows):
        out_list.append('')
        for j in range(out_cols):
            a_char = a_list[i][j]
            b_char = b_list[i][j]
            out_list[i] += b_char if not b_char.isspace() else a_char

    out_text = '\n'.join(out_list)

    return out_text


def merge_nested_lists(a, b):
    """Return items from list b substituted with items from a where b value is None."""

    if len(a) != len(b):
        raise ValueError("Lists must have same length.")
    c = []
    for i, j in zip(a, b):
        c.append(merge_lists(i, j))
    return c


def text_map_to_nested_list(text_map):
    """Return a nested list from a text map."""

    return [[c for c in text_line[::2]] for text_line in text_map.split('\n')]


def nested_list_to_text_map(nested_list):
    """Return a text map from a nested list."""

    return '\n'.join([' '.join(i) for i in nested_list])


def explode_ui_text(text):
    """Split text into two lists containing continuous blocks of characters and newlines, respectively."""

    text_blocks = []
    newline_blocks = []

    clean = text.strip()
    last_char = ''

    for char in clean:

        if char == '\n':
            if len(newline_blocks) == 0 or last_char != '\n':
                newline_blocks.append(char)
            else:
                newline_blocks[-1] = newline_blocks[-1] + char
        else:
            if len(text_blocks) == 0 or last_char == '\n':
                text_blocks.append(char)
            else:
                text_blocks[-1] = text_blocks[-1] + char

        last_char = char

    return text_blocks, newline_blocks


def format_ui_text(text):
    """Format text to fit within UI."""

    final_text = ''
    formatted_blocks = []

    text_blocks, newline_blocks = explode_ui_text(text)
    newline_blocks.append('')  # add empty string to match size of text_blocks for zip

    for text in text_blocks:

        width = game_config['ui']['width']
        words = text.split()
        lines = []
        line = ''
        for w in words:
            if len(line + w) + 1 <= width:
                line += ' ' + w
            else:
                lines.append(line.strip())
                line = ''
                line += ' ' + w
        lines.append(line.strip())
        keep_lines = [line for line in lines if len(line) > 0]
        formatted_text = '\n'.join(keep_lines)
        formatted_blocks.append(formatted_text)

    for pair in zip(formatted_blocks, newline_blocks):
        final_text += (pair[0] + pair[1])

    return final_text


def level_exists(number):
    """Return True if the level exists in config, otherwise False."""

    return bool(level_config.get(number))


def save_exists(name):
    """Return true if save game file exists, otherwise False."""

    check_filepath = os.path.join('.save', name)

    return os.path.exists(check_filepath)


def save_object(obj, name):
    """Serialize game object and save to file."""

    save_file_path = os.path.join('.save', name)
    save_backup_path = save_file_path + '_bak'

    if hasattr(obj, 'player'):

        # reset player Actions (which include ad-hoc, local functions) so object can be serialized
        obj.player.actions = {}
        obj.player.last_action = None

    if os.path.isfile(save_file_path):
        shutil.copy(save_file_path, save_backup_path)

    try:

        with open(save_file_path, "wb") as save_file:
            pickle.dump(obj, save_file)

        if os.path.isfile(save_backup_path):
            os.remove(save_backup_path)

    except:

        os.remove(save_file_path)
        os.rename(save_backup_path, save_file_path)


def load_object(name):
    """De-serialize save file and return game object."""

    load_filepath = os.path.join('.save', name)

    with open(load_filepath, "rb") as save_file:
        obj = pickle.load(save_file)

        if hasattr(obj, 'player'):
            # update player actions that were reset on save
            obj.player.update_actions()  # update action functions

    return obj


def transfer_inventory(src_player, tgt_player):
    """Replace target player inventory with source player inventory."""

    tgt_player.inventory = src_player.inventory
    tgt_player.inventory.owner = tgt_player

    for item in tgt_player.inventory.items:
        item.game = tgt_player.game

    return
