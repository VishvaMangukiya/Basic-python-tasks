data = [(123, 'abc'), (45, '6d7'), (89, 'xyz0')]

digits = []

for tup in data:
    for item in tup:
        for ch in str(item):
            if ch.isdigit():
                digits.append(ch)

print(digits)
