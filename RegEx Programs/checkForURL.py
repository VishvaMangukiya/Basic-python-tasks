import re

def valid_url(url):
    pattern = re.compile(
        r'^(https?://)?'
        r'([a-zA-Z0-9-]+\.)+'
        r'[a-zA-Z]{2,}'
        r'(:\d+)?'
        r'(/[w./?%&=-]*)?$'   
    )
    return bool(pattern.match(url))

url = input("Enter a URL: ")

if valid_url(url):
    print("Valid URL")
else:
    print("Invalid URL")