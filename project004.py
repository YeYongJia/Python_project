# 读取一个英文文件，计算其中单词数量
# from collections import Counter

from typing import Text

text = open(r'E:\python_project\a_story.txt')
count = 0
for line in text:
    count += len(line.split())
#   print(line.split())
print('This text has ' +str(count)+ ' words.')
##  a=sum([len(line.split()) for line in open('E:\\python_project\\a_story.txt', 'r')])
##  print(a)
