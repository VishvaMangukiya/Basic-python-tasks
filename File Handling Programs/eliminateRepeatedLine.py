def remove_duplicate_lines(filename):
    seen = set()
    unique_lines = []

    with open(filename, 'r') as file:
        for line in file:
            if line not in seen:
                seen.add(line)
                unique_lines.append(line)

    with open(filename, 'w') as file:
        file.writelines(unique_lines)

    print(f"Duplicate lines removed from '{filename}'.")

filename = "File Handling Programs/new.txt"
remove_duplicate_lines(filename)
