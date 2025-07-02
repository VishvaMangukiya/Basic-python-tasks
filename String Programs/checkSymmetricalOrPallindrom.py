s = input("Enter a string: ")

if s == s[::-1]:
    print("The string is a Palindrome")
else:
    print("The string is not a Palindrome")
    
mid = len(s) // 2
if s[:mid] == s[-mid:]:
    print("The string is a Symmetrical")
else:
    print("The string is not Symmetrical")
