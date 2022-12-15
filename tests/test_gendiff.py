from gendiff import generate_diff


def test_gendiff():
    correct = open('tests/fixtures/results/result1.txt', 'r').read()
    assert generate_diff('tests/fixtures/json/file1.json', 'tests/fixtures/json/file2.json') == correct


def test_gendiff_empty():
    correct = open('tests/fixtures/results/result_empty.txt', 'r').read()
    assert generate_diff('tests/fixtures/json/empty.json', 'tests/fixtures/json/empty.json') == correct


def test_gendiff_one_empty():
    correct = open('tests/fixtures/results/result_one_empty.txt', 'r').read()
    assert generate_diff('tests/fixtures/json/file1.json', 'tests/fixtures/json/empty.json') == correct


def test_gendiff_similar():
    correct = open('tests/fixtures/results/result_similar.txt', 'r').read()
    assert generate_diff('tests/fixtures/json/file1.json', 'tests/fixtures/json/file1.json') == correct


def test_gendiff_yaml():
    correct = open('tests/fixtures/results/result1.txt', 'r').read()
    assert generate_diff('tests/fixtures/yaml/file1.yaml', 'tests/fixtures/yaml/file2.yaml') == correct


def test_gendiff_multi():
    correct = open('tests/fixtures/results/result1.txt', 'r').read()
    assert generate_diff('tests/fixtures/yaml/file1.yaml', 'tests/fixtures/json/file2.json') == correct


def test_bigus():
    correct = open('tests/fixtures/results/result_bigus.txt', 'r').read()
    assert generate_diff('tests/fixtures/json/file3.json', 'tests/fixtures/json/file4.json') == correct