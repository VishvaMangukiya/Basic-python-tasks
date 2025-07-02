text = input("Enter the string: ")

if "http://" in text or "https://" in text or "www." in text:
    print("URL found in the string.")
else:
    print("No URL found in the string.")

