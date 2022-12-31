import itertools


def stylish(diff):
    if diff == {}:
        return ''

    def walk(node, depth):
        lines = []
        next_depth = depth + 1
        indent = depth * '    '
        for key, value in node.items():
            if not is_dict(value):
                form_value = val_check_spec(value)
                lines.append(gen_line(key, form_value, indent))
            elif 'change' not in value.keys():
                if is_dict(value):
                    form_value = walk(value, next_depth)
                    lines.append(gen_line(key, form_value, indent))
                else:
                    form_value = val_check_spec(value['value'])
                    lines.append(gen_line(key, form_value, indent))
            elif not is_dict(value['value']) and 'children' not in value:
                change = value['change']
                if change != 'edit':
                    form_value = val_check_spec(value['value'])
                    add_indent = get_add_indent(change)
                    lines.append(gen_line(key, form_value, indent, add_indent))
                else:
                    value1 = value['value'][0]
                    value2 = value['value'][1]
                    if is_dict(value1):
                        form_value1 = walk(value1, next_depth)
                    else:
                        form_value1 = val_check_spec(value1)
                    if is_dict(value2):
                        form_value2 = walk(value2, next_depth)
                    else:
                        form_value2 = val_check_spec(value2)
                    lines.append(gen_line(key, form_value1, indent, '  - '))
                    lines.append(gen_line(key, form_value2, indent, '  + '))
            else:
                change = value['change']
                if change != 'edit':
                    form_value = walk(value['value'], next_depth)
                    add_indent = get_add_indent(change)
                    lines.append(gen_line(key, form_value, indent, add_indent))
                else:
                    children = walk(value['children'], next_depth)
                    lines.append(gen_line(key, children, indent))
        result = itertools.chain('{', lines, [indent + '}'])
        return '\n'.join(result)
    return walk(diff, 0)


def val_check_spec(val):
    if (val is True):
        return 'true'
    if (val is False):
        return 'false'
    if (val is None):
        return 'null'
    return val


def gen_line(key, value, indent, add_indent='    '):
    return f"{indent}{add_indent}{key}: {value}"


def is_dict(value):
    return isinstance(value, dict)


def get_add_indent(change):
    if change == 'nothing':
        return '    '
    if change == 'add':
        return '  + '
    if change == 'remove':
        return '  - '
