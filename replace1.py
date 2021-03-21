with open("filename1.txt", encoding="utf8") as f:
    content = f.read();

content = content.replace("#EXTINF", "\n#EXTINF");

with open("filename2.txt", mode="w", encoding="utf8") as f:
    content = f.write(content);