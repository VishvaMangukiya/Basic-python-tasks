def merge_files(file1, file2, merged_file):
    with open(file1, 'r') as f1, open(file2, 'r') as f2, open(merged_file, 'w') as mf:
        mf.write(f1.read())
        mf.write('\n')  
        mf.write(f2.read())
    print(f"Files '{file1}' and '{file2}' merged into '{merged_file}'.")

merge_files('File Handling Programs/new.txt', 'File Handling Programs/file2.txt', 'File Handling Programs/file1.txt')
