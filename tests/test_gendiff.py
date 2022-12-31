from gendiff import generate_diff

def test_gendiff_empty():
    correct = open('tests/fixtures/results/result_empty.txt', 'r').read()
    assert generate_diff('tests/fixtures/json/empty.json', 'tests/fixtures/json/empty.json', 'stylish') == correct


def test_nested():
    correct = open('tests/fixtures/results/result_nested.txt', 'r').read()
    assert generate_diff('tests/fixtures/json/file3.json', 'tests/fixtures/json/file4.json', 'stylish') == correct


def test_gendiff_yaml():
    correct = open('tests/fixtures/results/result_common.txt', 'r').read()
    assert generate_diff('tests/fixtures/yaml/file1.yaml', 'tests/fixtures/yaml/file2.yaml', 'stylish') == correct


def test_gendiff_plain():
    correct = open('tests/fixtures/results/result_plain.txt', 'r').read()
    assert generate_diff('tests/fixtures/json/file3.json', 'tests/fixtures/json/file4.json', 'plain') == correct
