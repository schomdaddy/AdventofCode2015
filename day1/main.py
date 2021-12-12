f = open("input.txt")

x = f.readline().strip()
ans = 0
step = 0
base = True
for y in x:
    step += 1
    if y == '(':
        ans += 1
    else:
        ans -= 1
    if ans < 0 and base:
        print(step)
        base = False
print(ans)