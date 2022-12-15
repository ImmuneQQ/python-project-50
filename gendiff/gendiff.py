from gendiff import file_parser
import itertools


def generate_diff(file_path1, file_path2):
    file1 = file_parser.get_parsed_data(file_path1)
    file2 = file_parser.get_parsed_data(file_path2)
    return generate_string(file1, file2)


def generate_string(value1, value2):
    if value1 == {} and value2 == {}:
        return ''

    def walk(current_value1, current_value2, depth):
        keys_count = gen_keys_count(current_value1, current_value2)
        keys_sorted = sorted(keys_count)
        lines = []
        next_depth = depth + 1
        indent = depth * '    '
        next_indent = next_depth * '    '
        for key in keys_sorted:
            if keys_count[key] == 1:
                val = current_value1[key]
                if isinstance(val, dict):
                    val = walk(val, val, next_depth)
                else:
                    val = val_check_spec(val)
                lines.append(f"{indent}  - {key}: {val}")
            if keys_count[key] == 2:
                val = current_value2[key]
                if isinstance(val, dict):
                    val = walk(val, val, next_depth)
                else:
                    val = val_check_spec(val)
                lines.append(f"{indent}  + {key}: {val}")
            if keys_count[key] == 3:
                val1 = current_value1[key]
                val1 = val_check_spec(val1)
                val2 = current_value2[key]
                val2 = val_check_spec(val2)
                if not isinstance(val1, dict) or not isinstance(val2, dict):
                    if (isinstance(val1, dict)):
                        val1 = walk(val1, val1, next_depth)
                    if (isinstance(val2, dict)):
                        val2 = walk(val2, val2, next_depth)
                    if val1 == val2:
                        lines.append(f"{next_indent}{key}: {val1}")
                    else:
                        lines.append(f"{indent}  - {key}: {val1}")
                        lines.append(f"{indent}  + {key}: {val2}")
                else:
                    lines.append(
                        f"{next_indent}{key}: {walk(val1, val2, next_depth)}")
        result = itertools.chain('{', lines, [indent + '}'])
        return '\n'.join(result)
    return walk(value1, value2, 0)


def val_check_spec(val):
    if (val is True):
        return 'true'
    if (val is False):
        return 'false'
    if (val is None):
        return 'null'
    return val


def gen_keys_count(dict1, dict2):
    keys_count = {}
    for key in dict1.keys():
        keys_count[key] = 1
    for key in dict2.keys():
        keys_count[key] = keys_count.get(key, 0) + 2
    return keys_count
