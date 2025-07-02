def append_file_content(source_file, target_file):
    with open(source_file, 'r') as src:
        content = src.read()
    
    with open(target_file, 'a') as tgt:
        tgt.write(content)
    
    print(f"Content of '{source_file}' appended to '{target_file}'.")

append_file_content('File Handling Programs/file2.txt', 'File Handling Programs/file1.txt')
