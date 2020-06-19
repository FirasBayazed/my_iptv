# delete the line that contain "Rotana" and the line after it

file = open("in.txt", "r",encoding='UTF8')
lines = file.readlines()
file.close()

file = open("out.txt", "w",encoding='UTF8')
i = 0
while i < len(lines):
    line = lines[i]
    if "Rotana" not in line:
        file.write(line)
    else:
        i = i + 1
    i = i + 1
file.close()