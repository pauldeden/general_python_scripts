import argparse
import codecs

def remove_non_ascii(file_name:str)->None:
    """Remove non-ASCII characters from a text file"""
    try:
        with codecs.open(file_name, 'r', encoding='utf-8', errors='ignore') as file:
            # Read the file contents
            contents = file.read()
            # Remove all non-ASCII characters
            cleaned_contents = ''.join(i for i in contents if ord(i) < 128)
    except IOError as e:
        print(f"Error opening/reading file: {e}")
        sys.exit()

    try:
        with codecs.open(file_name, 'w', encoding='utf-8') as file:
            # Write the cleaned contents to the file
            file.write(cleaned_contents)
    except IOError as e:
        print(f"Error writing to file: {e}")
        sys.exit()

    print(f"Successfully removed non-ASCII characters from {file_name}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Remove non-ASCII characters from a text file.')
    parser.add_argument('file', metavar='file', type=str, help='the file to be processed')
    args = parser.parse_args()
    remove_non_ascii(args.file)
