import string

f = open("input.txt")
commands = []
wires = {}
for x in f:
    (operand, result) = x.strip().split("->")
    operand = operand.strip().split(" ")
    commands.append((operand, result))

for c1 in string.ascii_lowercase:
    wires[c1] = 0
    for c2 in string.ascii_lowercase:
        wires[c1 + c2] = 0
for z in range(100):
    for command in commands:
        op = command[0]
        res = command[1]
        if len(op) == 1:
            try:
                wires[res.strip()] = int(op[0])
            except ValueError:
                wires[res.strip()] = wires[op[0]]
        elif "NOT" in op:
            wires[res.strip()] = ~wires[op[1].strip()]
        elif "LSHIFT" in op:
            wires[res.strip()] = wires[op[0].strip()] << int(op[2])
        elif "RSHIFT" in op:
            wires[res.strip()] = wires[op[0].strip()] >> int(op[2])
        elif "AND" in op:
            try:
                wires[res.strip()] = wires[op[0].strip()] & wires[op[2].strip()]
            except KeyError:
                wires[res.strip()] = int(op[0]) & wires[op[2].strip()]
        elif "OR" in op:
            wires[res.strip()] = wires[op[0].strip()] | wires[op[2].strip()]
print(wires["a"])