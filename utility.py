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


def build_component_report_text(orientation, d4_components):

    article = 'a'
    conjunction = 'and'
    delimiter = ','

    report_open = 'There\'s'
    report_body = ''
    body_parts = []

    if any([len(component_list) > 0 for component_list in d4_components]):
        for direction in range(len(d4_components)):
            component_list = d4_components[direction]
            if len(component_list) > 0:
                this_part = delimiter.join([' ' + article + ' ' + str(interface) for interface in component_list]) + ' ' + get_relative_direction_text(orientation, direction)
                if this_part.count(delimiter) == 1:
                    this_part = this_part.replace(delimiter, ' ' + conjunction)
                elif this_part.count(delimiter) > 1:
                    this_part = this_part[::-1].replace(delimiter, (', ' + conjunction)[::-1])[::-1]
                body_parts.append(this_part)
        report_body += delimiter.join(body_parts)
        report_close = '.'
    else:
        report_close = ' nothing around me.'

    if len(body_parts) > 1:
        if any(part.count(conjunction) > 0 for part in body_parts):
            report_body = report_body[::-1].replace(delimiter, (', ' + conjunction)[::-1])[::-1]
        else:
            report_body = report_body.replace(delimiter, ' ' + conjunction)

    report = report_open + report_body + report_close
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
            lines.append(line)
            line = ''
            line += ' ' + w
    lines.append(line)
    keep_lines = [line for line in lines if len(line) > 0]
    formatted_text = '\n'.join(keep_lines)
    return formatted_text
