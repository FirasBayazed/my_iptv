with open("osn.txt", encoding="utf8") as f:
    content = f.read();

content = content.replace("http", "\nhttp");

with open("filename.txt", mode="w", encoding="utf8") as f:
    content = f.write(content);