def plain(diff):
    def walk(diff, path):
        lines = []
        for key, value in diff.items():
            new_path = path_join(key, path)
            change = value['change']
            current_value = value['value']
            if change == 'add' or change == 'remove':
                lines.append(gen_line(new_path, current_value, change))

            if change == 'edit':
                if value.get('children', False):
                    lines.extend(walk(value['children'], new_path))
                else:
                    lines.append(gen_line(new_path, current_value, change))
        return lines
    result = "\n".join(walk(diff, ''))
    return result


def val_check_spec(val):
    if (val is True):
        return 'true'
    if (val is False):
        return 'false'
    if (val is None):
        return 'null'
    if (isinstance(val, str)):
        return f"'{val}'"
    if (isinstance(val, dict)):
        return "[complex value]"
    return val


def path_join(key, path):
    if path == '':
        return key
    return f"{path}.{key}"


def gen_line(key, value, change):
    common_part = f"Property '{key}' was "
    if change == 'add':
        norm_value = val_check_spec(value)
        return f"{common_part}added with value: {norm_value}"

    if change == 'remove':
        return f"{common_part}removed"

    if change == 'edit':
        norm_value1 = val_check_spec(value[0])
        norm_value2 = val_check_spec(value[1])
        return f"{common_part}updated. From {norm_value1} to {norm_value2}"
