from gendiff import file_parser
from gendiff import gendif_engine
from gendiff.formatters import stylish, plain


def generate_diff(file_path1, file_path2, formatter):
    file1 = file_parser.get_parsed_data(file_path1)
    file2 = file_parser.get_parsed_data(file_path2)
    diff = gendif_engine.build_diff(file1, file2)
    if formatter == 'stylish':
        return stylish.stylish(diff)
    if formatter == 'plain':
        return plain.plain(diff)
