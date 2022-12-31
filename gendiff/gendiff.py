from gendiff import file_parser
from gendiff import gendif_engine
from gendiff.formatters import stylish


def generate_diff(file_path1, file_path2):
    file1 = file_parser.get_parsed_data(file_path1)
    file2 = file_parser.get_parsed_data(file_path2)
    diff = gendif_engine.build_diff(file1, file2)
    return stylish.stylish(diff)
