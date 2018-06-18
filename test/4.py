# -*- coding:utf-8 -*-  
'''
Created on 2017年12月13日

@author: Administrator
'''
import requests
from bs4 import BeautifulSoup
r = requests.get('https://www.qiushibaike.com/article/119816915')
# print r.text
soup = BeautifulSoup(r.text,'lxml')
print soup.find('div',class_='content').get_text(strip=True) 
print soup.find("h2").get_text(strip=True)
dad = soup.find('div',class_='author clearfix')
print 'https:'+dad.find("img")['src']
print soup.find("span ")