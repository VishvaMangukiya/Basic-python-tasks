import re

def parse_url(url):
    pattern = re.compile(
        r'^(?P<protocol>https?|ftp)://'        
        r'(?P<domain>[a-zA-Z0-9.-]+)'           
        r'(?::(?P<port>\d+))?'                    
        r'(?P<path>/[^\s?#]*)?'                  
        r'(?:\?(?P<query>[^#]*))?'                 
        r'(?:#(?P<fragment>.*))?$'                 
    )

    match = pattern.match(url)
    if match:
        return match.groupdict()
    else:
        return None

url = input("Enter a URL to parse: ")
result = parse_url(url)

if result:
    print("Parsed URL components:")
    for key, value in result.items():
        print(f"{key}: {value}")
else:
    print("Invalid URL format")
