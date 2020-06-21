file = open("in.txt", "r",encoding='UTF8')
lines = file.readlines()
file.close()

file = open("out2.txt", "w",encoding='UTF8')
i = len(lines) - 1
while i >= 0:
    line = lines[i]
    if "rotana" not in line:
        file.write(line)
    else:
        i = i - 1
    i = i - 1
file.close()