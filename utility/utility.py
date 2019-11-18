from config import game_config

# constants
DEFAULT_ARTICLE = game_config['ui']['articles']['default']
ARTICLE_MAP = game_config['ui']['articles']['mapped']


# functions
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
        object_text = ' '.join(
            [get_article(obj.description),
             str(obj)])

    elif len(object_list) == 2:
        obj_1 = object_list[0]
        obj_2 = object_list[1]
        object_text = ' '.join(
            [get_article(obj_1.description),
             str(obj_1),
             conjunction,
             get_article(obj_2.description),
             str(obj_2)])

    elif len(object_list) > 2:
        working_text = (' ' + conjunction + ' ').join(
            [get_article(obj.description) + ' ' + str(obj) for obj in object_list])
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

    # get natural order of d4 objects
    d4_order = list(range(len(d4_objects)))
    # rotate order to match player orientation
    player_order = d4_order[orientation:] + d4_order[:orientation]
    # swap last two items to make order: front, right, left, behind
    report_order = player_order[:2] + [player_order[3]] + [player_order[2]]

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


def format_ui_text(text):
    """Format text to fit within UI."""

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
    return formatted_text
