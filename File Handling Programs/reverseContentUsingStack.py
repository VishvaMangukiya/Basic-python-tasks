def reverse_file_using_stack(source_file, target_file):
    stack = []

    with open(source_file, 'r') as src:
        content = src.read()
        for ch in content:
            stack.append(ch)

    with open(target_file, 'w') as tgt:
        while stack:
            tgt.write(stack.pop())

    print(f"Content of '{source_file}' reversed using stack and saved to '{target_file}'.")

reverse_file_using_stack('File Handling Programs/file1.txt', 'File Handling Programs/file2.txt')
