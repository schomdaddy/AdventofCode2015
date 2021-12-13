import hashlib
string = "yzbqklnj"

num = 0;
while True:
    input = string + str(num)
    m = hashlib.md5(input.encode())
    check = m.hexdigest()
    if check[0:6] == "000000":
        break
    num += 1
    print(num)
print(num)