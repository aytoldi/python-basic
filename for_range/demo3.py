#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2019/12/8 0008 下午 16:02
#@Author: qaytix
#@File  : demo3.py

list={"firstName":"java","lastNmae":"javascript","version":6};

for item in list:
    getKey=list[item];
    print(getKey);#java    javascript      6

#dict_items([('firstName', 'java'), ('lastNmae', 'javascript'), ('version', 6)])
print(list.items());# ئې: بارلىق key ۋە value قىممەتلەرگە ئېرىشىش

getAllKeyValue=list.items();
for key,value in getAllKeyValue:
    print("key:",key);
    print("value:",value);
    """
        key: firstName
        value: java
        key: lastNmae
        value: javascript
        key: version
        value: 6
    """