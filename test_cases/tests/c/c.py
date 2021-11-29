file = "01"
lines = []

with open("./" + file) as f:
    for line in f:
        lines.append(line)

print(lines)