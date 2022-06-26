s = input()
i = 0
result = []
while i < len(s):
    if s[i] == "<":
        e = s.find(">", i+1) + 1
        result.append(s[i:e])
    elif s[i] == " ":
        e = i + 1
        result.append(" ")
    else:
        e1 = s.find(" ", i+1)
        e2 = s.find("<", i+1)
        if e1 == -1 and e2 == -1:
            e = len(s)
        elif e1 == -1:
            e = e2
        elif e2 == -1:
            e = e1
        else:
            e = min(e1, e2)
        result.append("".join(reversed(s[i:e])))
    i = e
print("".join(result))