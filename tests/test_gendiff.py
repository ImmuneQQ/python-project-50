from gendiff import gendiff


def test_gendiff():
    correct = open('tests/fixtures/result1.txt', 'r').read()
    assert gendiff.generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json') == correct


def test_gendiff_empty():
    correct = open('tests/fixtures/result_empty.txt', 'r').read()
    assert gendiff.generate_diff('tests/fixtures/empty.json', 'tests/fixtures/empty.json') == correct


def test_gendiff_one_empty():
    correct = open('tests/fixtures/result_one_empty.txt', 'r').read()
    assert gendiff.generate_diff('tests/fixtures/file1.json', 'tests/fixtures/empty.json') == correct


def test_gendiff_similar():
    correct = open('tests/fixtures/result_similar.txt', 'r').read()
    assert gendiff.generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file1.json') == correct