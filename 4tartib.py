dict = {
    "t": 3,
    "p": 1,
    "y": 2,
    "o": 5,
    "h": 4,
    "n": 6,
}
v=sorted(dict.values())
for i in v:
    for key in dict:
        if dict[key]==i: 
            print(key)