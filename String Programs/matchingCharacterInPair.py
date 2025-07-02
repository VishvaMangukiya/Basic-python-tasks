def matching_character(str1, str2):
    set1 = set(str1)
    set2 = set(str2)
    matching = set1.intersection(set2)
    return len(matching)

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

count = matching_character(str1,str2)
print(f"Number of matching characters: {count}")