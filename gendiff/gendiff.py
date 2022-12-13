import json


def generate_diff(file_path1, file_path2):
    file1 = json.load(open(file_path1))
    file2 = json.load(open(file_path2))
    joint_dict = {}
    for key, value in file1.items():
        joint_dict.setdefault(key, [])
        joint_dict[key].append((1, value))
    for key, value in file2.items():
        joint_dict.setdefault(key, [])
        joint_dict[key].append((2, value))
    result_str = generate_string(dict(sorted(joint_dict.items())))
    return result_str


def generate_string(joint_dict):
    result_str = ''
    for key, value in joint_dict.items():
        first_item = value[0]
        first_value = first_item[1]
        if len(value) == 1:
            if first_item[0] == 1:
                result_str += f"  - {key}: {first_value}\n"
            else:
                result_str += f"  + {key}: {first_value}\n"
        if len(value) == 2:
            second_item = value[1]
            second_value = second_item[1]
            if first_value == second_value:
                result_str += f"    {key}: {first_value}\n"
            else:
                result_str += f"  - {key}: {first_value}\n"
                result_str += f"  + {key}: {second_value}\n"
    result_str = "{\n" + result_str + "}"
    return(result_str)
