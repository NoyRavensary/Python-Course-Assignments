def count_characters(content):
    return len(content)

def count_lines(content):
    # Split content into lines and count them
    lines = content.splitlines()
    return len(lines)

def count_words(content):
    return len(content.split())

def count_file_stats(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
        char_count = count_characters(content)
        line_count = count_lines(content)
        word_count = count_words(content)
        return char_count, line_count, word_count
    except FileNotFoundError:
        print("File not found.")
        return None
