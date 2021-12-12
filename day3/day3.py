f = open("input.txt")
cord = []
x = 0
x2 = 0
y = 0
y2 = 0
robo = False
cord.append([x,y])
for a in f:
    string = a.strip()
    for b in string:
        if b == '^':
            if robo:
                y += 1
            else:
                y2 += 1
        elif b == '>':
            if robo:
                x += 1
            else:
                x2 += 1
        elif b == '<':
            if robo:
                x -= 1
            else:
                x2 -= 1
        else:
            if robo:
                y -= 1
            else:
                y2 -= 1
        if robo:
            if [x,y] not in cord:
                cord.append([x,y])
        else:
            if [x2,y2] not in cord:
                cord.append([x2,y2])
        if robo:
            robo = False
        else:
            robo = True
print(len(cord))