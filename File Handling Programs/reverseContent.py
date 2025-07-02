def reverse_file_content(source_file, target_file):
    with open(source_file, 'r') as src:
        content = src.read()

    reversed_content = content[::-1]  

    with open(target_file, 'w') as tgt:
        tgt.write(reversed_content)

    print(f"Reversed content of '{source_file}' saved to '{target_file}'.")

reverse_file_content('File Handling Programs/file1.txt', 'File Handling Programs/file2.txt')
