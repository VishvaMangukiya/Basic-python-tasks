import re

def extract_max_num(text):
    numbers = re.findall(r'\d+',text)

    if not numbers:
        return "No numbers found"
    
    numbers = list(map(int, numbers))

    return max(numbers)

text = input("Enter a string with numbers:" )
print("Maximum number: ",extract_max_num(text))