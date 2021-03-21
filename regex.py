import re

with open('new_channels.txt', 'r', encoding='UTF8') as f_in, open('data_out_new1.txt', 'w', encoding='UTF8') as f_out:
    txt = re.sub(r'(?<=^#EXTINF:-1)(.*,)', ',', f_in.read(), flags=re.M)
    print(txt, file=f_out, end='')