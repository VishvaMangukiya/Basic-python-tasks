with open("File Handling Programs/new.txt","r") as file:
    while True:
        char = file.read(1)
        if not char:
            break
        print(char)