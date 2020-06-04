import re

with open('f.txt', 'r', encoding='UTF8') as f_in, open('data_out.txt', 'w', encoding='UTF8') as f_out:
    txt = re.sub(r'(?<=^#EXTINF:-1)(.*,)', ',', f_in.read(), flags=re.M)
    print(txt, file=f_out, end='')