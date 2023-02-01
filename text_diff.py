import argparse
import difflib
import textwrap
import re

def remove_junk(text):
    text = re.sub(r'[\r\n]+', '', text)
    text = re.sub(r'\s+', ' ', text)
    return text

def compare_files(file1_path, file2_path):
    with open(file1_path) as file1, open(file2_path) as file2:
        content1 = textwrap.wrap(remove_junk(file1.read()))
        content2 = textwrap.wrap(remove_junk(file2.read()))

    diff = difflib.ndiff(content1, content2)
    differences = []
    i = j = 0
    for line in diff:
        differences.append(line)
    return differences

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Compare two text files and show all textual differences between them.")
    parser.add_argument("file1", help="Path to the first file")
    parser.add_argument("file2", help="Path to the second file")
    args = parser.parse_args()

    differences = compare_files(args.file1, args.file2)
    if differences:
        print("Textual Differences:")
        for line in differences:
            print(line)
    else:
        print("Files are identical.")
