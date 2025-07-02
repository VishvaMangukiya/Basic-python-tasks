import re
from collections import Counter

def most_occurring_number(text):
    numbers = re.findall(r'\d+', text)

    if not numbers:
        return "No numbers found."

    count = Counter(numbers)

    most_common = count.most_common(1)[0]  

    return f"Most occurring number: {most_common[0]} (Occurred {most_common[1]} times)"

text = input("Enter a string with numbers: ")
print(most_occurring_number(text))
