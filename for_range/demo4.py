#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2019/12/8 0008 下午 16:22
#@Author: qaytix
#@File  : demo4.py
sum=0;
for i in range(1,11):
    if i==5:
        break;
    elif i==2 :
        continue;# ئاتلاپ ئۈتۈ كىتىش, i=2 نى sum بىلەن ھىسابلىمايدۇ ، يەنى sum+=i غا كىرمەيدۇ
    else:
      sum+=i;
print(sum)

