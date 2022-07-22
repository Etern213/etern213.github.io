import os
import re

path = "D:\\lijiaqi\\source\\_posts"
md_list = os.listdir(path)

# 合并文件
contents = []
for md in md_list:
    if re.findall("(.*?).md", md) != []:
        mdfile = str(path) + '\\' + md
        with open(mdfile, 'r' ,encoding='utf-8') as f:
            contents.append(f.read() + "\n")
contents.append("所有文章索引" + "\n")

with open("D:\\lijiaqi\\source\\generate.md", "w" ,encoding='utf-8') as f:
    f.writelines(contents)
print("task done!")