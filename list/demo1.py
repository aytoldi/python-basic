#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2019/12/7 0007 下午 17:25
#@Author: qaytix
#@File  : demo1.py

# ئې: tulpe بىلەن list نىڭ قانداق باغلىنشلىق ئوخشاشلىقى بار ، پەرقى نىمە ؟
#ئې: ئوخشاشلىقى ھەر ئىككسگە خالىغانچە قىممەت ساقلىغلى بولىدۇ ، tulpe غا ساقلانغا قىممەت مۇقىم ئۆزگەرتىشكە بولمايدۇ ، tulpe بولسا مەشغۇلاتقا چەكلمە قويدۇ
# ئې : ئەمما list قا ساقلانغان قىممەتلەرنى چەكلىمسىز ئۆزگەرتەلەيمىز
#ئې: list نى ئېنىقلىغاندا [] ئارقىلىق ئېنىقلايمىز
list1=["hello","world"];
list1[0]="_hello";#چەكلىمسىز ئۆزگەرتىش
first=list1[0];# ئې: list نىڭ ئىچىدىكى نۆلىنچى ئىندىكىستىكى قىممەتكە ئېرىشىش
print(first);
list2=["java","javascript","html5","python","css","jquery","vue","react"];
center=list2[0:4];# ئې: نۆلىنچى ئۇرۇندىن تۆتىنچى ئۇرۇنغىچە بولغان قىممەتكە ئېرىشىش ، تۆتىنچى ئۇرۇندىكى قىممەتنى ئالمايدۇ
print(center);
list3=["java","javascript"];
list3.append("html5");#ئې: list قا data قۇشۇش
list3.remove("html5");#ئې: يېڭى قوشقان قىممەتنى ئۆچۈرۈشتە قىممەتنىڭ ئۆزىنى يازىمىز
list3.remove(list3[0]);#ئې: list نىڭ ئىچدىكى نۆلىنچى ئۇرۇندىكى قىممەتنى ئۆچۈرۈش
help(list3.append);#ئې : list دىكى ئۇسۇلنىڭ ئىشلىتلىشنى دەپ بېرىدۇ
getLen=len(list3);
print(getLen);
#ئې: str بولسا (arr)序列 دەيمىز ، list نى 列表(select) دەيمىز ...

