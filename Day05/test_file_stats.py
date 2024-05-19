from file_stats import count_characters, count_lines, count_words

def test_count_characters():
    assert count_characters("Hello, World!") == 13
    assert count_characters("") == 0

def test_count_lines():
    assert count_lines("Hello\nWorld\n") == 2
    assert count_lines("Hello World") == 1

def test_count_words():
    assert count_words("Hello, World!") == 2
    assert count_words("Hello World\nPython") == 3
    assert count_words("") == 0
