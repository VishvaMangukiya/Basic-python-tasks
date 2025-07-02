import re

def add_space_to_camal_case(text):
    spaced_text = re.sub(r'(?<!^)(?=[A-Z])', ' ', text)
    return spaced_text

text = input("Enter a camalcase string: ")
result = add_space_to_camal_case(text)
print("Spaced string: ",result)