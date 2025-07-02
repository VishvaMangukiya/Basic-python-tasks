data = {}

n = int(input("How many entries? "))

for _ in range(n):
    name = input("Enter name: ")
    subject = input("Enter subject: ")
    score = int(input("Enter score: "))
    data[(name, subject)] = score

print(data)