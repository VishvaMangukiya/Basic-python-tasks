def reverse_first_line(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    if lines:
        lines[0] = lines[0 ][::-1]  

        with open(filename, 'w') as file:
            file.writelines(lines)

        print(f"First line of '{filename}' has been reversed.")
    else:
        print("File is empty.")

reverse_first_line('File Handling Programs/new.txt')
