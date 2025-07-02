def count_lines(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        print(f"Total number of lines: {len(lines)}")

filename = "File Handling Programs/new.txt"
count_lines(filename)
