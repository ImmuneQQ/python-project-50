import yaml
import json


def get_parsed_data(file_path):
    extension = file_path.split('.')[-1]

    if extension in ('json', 'yaml', 'yml'):
        if extension == 'json':
            data = json.load(open(file_path))
        if extension in ('yaml', 'yml'):
            data = yaml.load(open(file_path), Loader=yaml.Loader)

    return data if data else {}
