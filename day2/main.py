f = open("input.txt")
s = []
sa = []
ans = 0
for x in f:
    s.append(x.strip().split('x'))
for x in s:
    sa.append([int(x[0]) * int(x[1]) * 2, int(x[1]) * int(x[2]) * 2, int(x[0]) * int(x[2]) * 2])
for x in sa:
    min = 0
    if x[0] > x[1]:
        if x[1] > x[2]:
            min = x[2]
        else:
            min = x[1]
    elif x[2] > x[0]:
        min = x[0]
    else:
        min = x[2]
    ans += x[0] + x[1] + x[2] + min/2
print(ans)
ans2 = 0
for x in s:
    small1 = 0;
    small2 = 0;
    area = int(x[0]) * int(x[1]) * int(x[2])
    if int(x[0]) > int(x[1]):
        if int(x[0]) > int(x[2]):
            small1 = int(x[1])
            small2 = int(x[2])
        else:
            small1 = int(x[1])
            small2 = int(x[0])
    elif int(x[2]) > int(x[1]):
        small1 = int(x[0])
        small2 = int(x[1])
    else:
        small1 = int(x[0])
        small2 = int(x[2])
    ans2 += area + small1 * 2 + small2 * 2
print(ans2)