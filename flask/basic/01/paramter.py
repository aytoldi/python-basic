#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2019/12/13 0013 上午 1:51
#@Author: qaytix
#@File  : paramter.py

from flask import Flask
app=Flask(
    __name__,
    #http://127.0.0.1:5000/python/index.html
    static_url_path="/python",# تور كۆرگۈچ زىيارەت قىلدىغان تىنىچ  ھالەتتىكى مۇندەرىجە نامىنى ئۆزگەرتىش , نورمال قىىممەت static
    static_folder="staic", # تىنىچ ھالەتتىكى html بەت مۇندەرىجىسى ,  نورمال قىىممەت static
    template_folder="/templates", # setting templates, defultName templates
)