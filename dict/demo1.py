#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2019/12/7 0007 下午 20:38
#@Author: qaytix
#@File  : demo1.py
#ئې: dict غا ساقلانغان ئۇچۇرلار object شەكلىدە بولىدۇ {key1:value1,key2:value2}

dict1={"firstName":"java","lastName":"script","version":6};
print(dict1["firstName"]);#قىممەتكە ئىرىشىش
dict1["firstName"]="_Java";
print(dict1["firstName"]);#قىممەت ئۆزگەرتىش
dict1.pop("firstName");#ئۆچۈرۈش
dict1.clear();#ئې : ھەممنى ئۈچۈرۈش {} , ئۆچكەندىن كىيىن قۇرۇق sobject قالىدۇ
dict2={"firstName":"java","lastName":"script","version":6};
getKey=dict2.keys();
print(getKey);# ['firstName', 'lastName', 'version']
getValue=dict2.values();
print(getValue);# ['java', 'script', 6]

