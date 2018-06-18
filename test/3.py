# -*- coding:utf-8 -*-  
'''
Created on 2017年12月13日

@author: Administrator
'''
import requests
from bs4 import BeautifulSoup
import re

text = 'sdfiushfjksadfjksadf】1231654'
num = re.search('\d+', text).group()
print num


r = requests.get('https://www.baidu.com/')
print r.text


html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
soup = BeautifulSoup(html_doc,'lxml')
print soup.find('title')