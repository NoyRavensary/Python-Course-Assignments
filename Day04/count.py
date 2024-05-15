import sys

def count_file_stats(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            char_count = len(content)
            line_count = content.count('\n') + 1  # Add 1 to count the last line
            word_count = len(content.split())
            
            print(f"Number of characters: {char_count}")
            print(f"Number of lines: {line_count}")
            print(f"Number of words: {word_count}")
    except FileNotFoundError:
        print("File not found.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python count.py FILENAME")
    else:
        filename = sys.argv[1]
        count_file_stats(filename)
