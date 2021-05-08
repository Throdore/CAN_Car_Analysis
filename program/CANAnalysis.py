# -*- codeing = utf-8 -*-
# @Time :2021/5/7 23:18
# @Author: Hepta_Nian
# @File:txt_test.py
# @Software:PyCharm


import re

number = 50
wj_name = "190.txt"


f = open(wj_name, encoding='UTF-8')
a = f.readlines()
c = [];
d = []
num = []
findxls = re.compile(r"...#")
print("开始")
for i in range(len(a)):
    b = re.findall(findxls, a[i])
    c.append(b)
print(len(c))
for i in range(0, len(c)):
    a = 0
    if c[i][0] in d:
        continue
    for j in range(len(c)):
        if c[i][0] in c[j]:
            a = a + 1
    for j in range(0, 3):
        print(c[i][0][j], end='')
        if j == 2:
            print(':', a)
    if a <= number:
        num.append(c[i][0])
    d.append(c[i][0])
for i in range(len(num)):
    print("yes", num[i])
