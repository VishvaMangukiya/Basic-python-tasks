def find_n_char_words(filename, n):
    with open(filename, "r") as file:
        content = file.read()
        words = content.split()

        result = [word for word in words if len(word) == n]

        print(f"Words with {n} characters: ")
        for word in result:
            print(word)

filename = "File Handling Programs/new.txt"
n = 5
find_n_char_words(filename, n)