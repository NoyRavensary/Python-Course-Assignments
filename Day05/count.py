import sys
from file_stats import count_file_stats

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python count.py FILENAME")
    else:
        filename = sys.argv[1]
        result = count_file_stats(filename)
        if result:
            char_count, line_count, word_count = result
            print(f"Number of characters: {char_count}")
            print(f"Number of lines: {line_count}")
            print(f"Number of words: {word_count}")
