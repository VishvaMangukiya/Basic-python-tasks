import random
import string

target = input("Enter the string: ")
char = string.ascii_letters + string.digits + string.punctuation + ' '

attempt = ''
attempts = 0

while attempt != target:
    attemp = ''.join(random.choice(char) for i in range(len(target)))
    attempts +=1  

print(f"Target matched after {attempts} attempts: {attempts}")
