f = open("input.txt")
doubles = []
ans = 0
v = 0
good = False
double = False
for x in f:
    for y in range(13):
        substring = x[y:y+2]
        if substring in x[y+2:]:
            good = True
    old = " "
    old2 = " "
    for y in x:
        if y == old2:
            double = True
        old2 = old
        old = y
    if double and good:
        ans += 1
    double = False
    good = False
print(ans)