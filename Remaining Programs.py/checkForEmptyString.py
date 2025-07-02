def become_empty(s, sub):
    while sub in s:
        s = s.replace(sub, "")
    return s == ""

s = "ababab"
sub = "ab"
print(become_empty(s, sub))  

s = "abcabcab"
sub = "abc"
print(become_empty(s, sub))  
