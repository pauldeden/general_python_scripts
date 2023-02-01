import argparse
import difflib
import re

def compare_files(file1_path, file2_path):
    with open(file1_path) as file1, open(file2_path) as file2:
        content1 = file1.read().splitlines()
        content2 = file2.read().splitlines()

    diff = difflib.ndiff(content1, content2, linejunk=difflib.IS_LINE_JUNK, charjunk=difflib.IS_CHARACTER_JUNK)
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
