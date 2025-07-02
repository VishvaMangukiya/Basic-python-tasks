with open("File Handling Programs/new.txt", "r") as file:
    content = file.read()

    words = content.split()
      
    for word in words:
        print(word)
