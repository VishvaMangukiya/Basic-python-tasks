def remove_duplicates(str):
    result = ""
    seen = set()
    for char in str:
        if char not in seen:
            seen.add(char)
            result += char
    return result

input_str = input("Enter a string: ")
output_str = remove_duplicates(input_str)
print("String after remove duplicates:", output_str)
