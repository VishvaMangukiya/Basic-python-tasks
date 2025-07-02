import re

def is_valid_ip(ip):
    pattern = re.compile(
        r'^('
        r'(25[0-5]|'     
        r'2[0-4][0-9]|'    
        r'1[0-9]{2}|'       
        r'[1-9]?[0-9])\.){3}'  
        r'(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])$' 
    )
    return bool(pattern.match(ip))

ip_address = input("Enter an IP address: ")

if is_valid_ip(ip_address):
    print("Valid IP address")
else:
    print("Invalid IP address")
