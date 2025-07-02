matrix = [
    ["a", "b"],
    ["c", "d"],
    ["e", "f"],
    ["g", "h"]
]

ans = [''.join(col) for col in zip(*matrix)]

print("Verticle concatenation: ",ans)