with open("data_out_new1.txt", encoding="utf8") as f:
    content = f.read();

content = content.replace("http", "\nhttp");

with open("filename1.txt", mode="w", encoding="utf8") as f:
    content = f.write(content);