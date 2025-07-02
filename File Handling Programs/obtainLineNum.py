def find_word_line_num(filename, target_word):
    line_numbers = []

    with open(filename, 'r') as file:
        for i, line in enumerate(file, start = 1):
            if target_word in line:
                line_numbers.append(i)

    
    if line_numbers:
        print(f"The word '{target_word}' is found in line: {line_numbers}")
    else:
        print(f"The word '{target_word}' is not found in the file")

filename = "File Handling Programs/new.txt"
target_word = "Foram"
find_word_line_num(filename, target_word)