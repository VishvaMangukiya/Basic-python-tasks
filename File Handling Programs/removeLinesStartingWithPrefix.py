def remove_lines_with_prefix(filename, prefixes):
    with open(filename, 'r') as file:
        lines = file.readlines()

    filtered_lines = [line for line in lines if not line.startswith(tuple(prefixes))]

    with open(filename, 'w') as file:
        file.writelines(filtered_lines)

    print(f"Lines starting with {prefixes} removed from '{filename}'.")

filename = "File Handling Programs/new.txt"
prefixes = ["#", "//", "note"] 
remove_lines_with_prefix(filename, prefixes)
