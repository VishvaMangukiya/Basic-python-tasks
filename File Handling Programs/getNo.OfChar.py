with open("File Handling Programs/new.txt","r") as file:
    content = file.read()

    file.seek(0)
    lines = file.readlines()

    char_count = len(content)

    word_count = len(content.split())

    space_count = content.count(' ')

    line_count = len(lines)

    print("Charachters: ", char_count)
    print("Words: ",word_count)
    print("Spaces: ",word_count)
    print("Lines: ",line_count)