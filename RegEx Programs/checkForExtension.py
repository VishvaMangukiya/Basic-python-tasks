import re

file_list = [
    "report.pdf", "data.csv", "image.png", "doc1.docx",
    "notes.txt", "archive.zip", "photo.jpeg", "resume.docx"
]

extension = input("Enter file extension to search (e.g., pdf): ")

pattern = re.compile(rf'^.+\.{extension}$', re.IGNORECASE)

matched_files = [file for file in file_list if pattern.match(file)]

print("Files with extension .{}:".format(extension))
for file in matched_files:
    print(file)
