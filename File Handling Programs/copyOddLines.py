def copy_odd_lines(source_file, target_file):
    with open(source_file, 'r') as src, open(target_file, 'w') as tgt:
        for index, line in enumerate(src):
            if index % 2 == 0:  
                tgt.write(line)
    print(f"Odd lines copied from '{source_file}' to '{target_file}'.")

copy_odd_lines('File Handling Programs/new.txt', 'File Handling Programs/file2.txt')
