def build_diff(value1, value2):
    diff = {}
    keys_count = gen_keys_count(value1, value2)
    keys_sorted = sorted(keys_count)
    for key in keys_sorted:
        diff[key] = {}
        if key not in value1.keys():
            diff[key]['value'] = value2[key]
            diff[key]['change'] = 'add'
        elif key not in value2.keys():
            diff[key]['value'] = value1[key]
            diff[key]['change'] = 'remove'
        else:
            val1, val2 = value1[key], value2[key]
            if val1 == val2:
                diff[key]['value'] = val1
                diff[key]['change'] = 'nothing'
            else:
                diff[key]['value'] = (val1, val2)
                diff[key]['change'] = 'edit'
                if isinstance(val1, dict) and isinstance(val2, dict):
                    diff[key]['children'] = build_diff(val1, val2)
    return diff


def gen_keys_count(dict1, dict2):
    keys_count = {}
    for key in dict1.keys():
        keys_count[key] = 1
    for key in dict2.keys():
        keys_count[key] = keys_count.get(key, 0) + 2
    return keys_count
