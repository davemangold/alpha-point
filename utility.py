def is_empty_response(response):
    """Returns True if the response is valid, otherwise False."""

    return response is None or response.strip() == ''


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


def build_component_list_text(component_list):

    article = 'a'
    conjunction = 'and'
    delimiter = ','

    component_text = ''

    if len(component_list) == 1:
        component_text = ' '.join([article, str(component_list[0])])

    elif len(component_list) == 2:
        component_text = ' '.join([article, str(component_list[0]), conjunction, article, str(component_list[1])])

    elif len(component_list) > 2:
        working_text = (' ' + conjunction + ' ').join([article + ' ' + str(component) for component in component_list])
        replace_count = working_text.count(' ' + conjunction) - 1
        component_text = working_text.replace(' ' + conjunction, delimiter, replace_count)

    return component_text


def build_component_report_body(text_part_list):

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


def build_component_report_text(orientation, d4_components):

    report_open = 'There\'s'
    report_body = ''
    report_close = '.'

    body_part_list = []

    for direction in range(len(d4_components)):
        component_list = d4_components[direction]

        if len(component_list) > 0:
            this_text_part = build_component_list_text(component_list)
            this_text_part += ' ' + get_relative_direction_text(orientation, direction)
            body_part_list.append(this_text_part)

    if len(body_part_list) > 0:
        report_body += build_component_report_body(body_part_list)
    else:
        report_close = ' nothing around me.'

    report = report_open + ' ' + report_body + report_close

    return report


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

    width = 60
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
    formatted_text = '\n'.join(keep_lines).strip()
    return formatted_text
