with open("new.txt", encoding="utf8") as f:
    content = f.read();

content = content.replace("alliptvlinks.com " , "");

with open("new1.txt", mode="w", encoding="utf8") as f:
    content = f.write(content);