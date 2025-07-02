target_pair = "Name : Vishva"

count = 0

with open("File Handling Programs/new.txt","r") as file:
    for line in file:
        if line.strip() == target_pair:
            count += 1

print(f"The key-pair '{target_pair}' occurs {count} times.")