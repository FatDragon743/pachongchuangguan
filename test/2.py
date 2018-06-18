# -*- coding:utf-8 -*-  
'''
Created on 2017年12月13日

@author: Administrator
'''
import requests
from bs4 import BeautifulSoup
import re
from Get_html import *

url = 'http://www.acfun.cn/rank/list/#cid=63;range=1'
r = get_html(url,3)
soup = BeautifulSoup(r,'lxml')
# print (soup)
dad = soup.find('div',class_='mainer article')
mylist = dad.find_all('div',class_='item')
i =1
for item in mylist:
    print i
    i=i+1
    title = item.find('div',class_='l d').a.get_text()
    print 'title : '+(title)
    jianjie = item.find('div',class_='l d').p.get_text()
    print 'jianjie : '+(jianjie)
      
