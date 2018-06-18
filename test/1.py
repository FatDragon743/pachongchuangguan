# -*- coding:utf-8 -*-  
'''
Created on 2017年12月13日

@author: Administrator
'''
import requests
# r = requests.get(url='http://www.heibanke.com/lesson/crawler_ex00/')   #带参数的GET请求
# # print(r.status_code)  
# # print(r.url)#打印解码后的返回数据
from bs4 import BeautifulSoup
# soup = BeautifulSoup(r.text,'lxml')
# # print (soup)
# # print (soup.find('title').get_text())
# # print (soup.find('h1').get_text())
# text = soup.find('h3').get_text()
# # print (text)
import re
# num = re.search('\d+', text).group()
# print (num)
# new_url = 'http://www.heibanke.com/lesson/crawler_ex00/'+num
# print (new_url)
# r = requests.get(url=new_url)
# soup = BeautifulSoup(r.text,'lxml')
# # print (soup)
# # print (soup.find('title').get_text())
# # print (soup.find('h1').get_text())
# text = soup.find('h3').get_text()
# # print (text)
# import re
# num = re.search('\d+', text).group()
# print (num)
def get_new_url(url=''):
    r = requests.get(url=url)   #带参数的GET请求
    soup = BeautifulSoup(r.text,'lxml')
    text = soup.find('h3').get_text()
    num = re.search('\d+', text).group()
    new_url = 'http://www.heibanke.com/lesson/crawler_ex00/'+num
    return new_url
url = 'http://www.heibanke.com/lesson/crawler_ex00/'
while(True):
    url = get_new_url(url)
    print (url)
