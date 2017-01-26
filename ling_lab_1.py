#!/usr/bin/python3
from bs4 import BeautifulSoup
from urllib.request import urlopen
import json

html_doc = urlopen('https://news.yandex.ru/science.html').read()

soup = BeautifulSoup(html_doc, 'lxml')
 
#print(soup)

#for meta in soup.find_all('meta'):
#    print(meta.get('content'))

#div_mas=soup.find_all("div", role="listitem")

#----------------------------------------
mas_src_img=[]
temp=soup.find_all('img', class_='image') #получил все ссылки на картинки
del temp[0]# первая картинка не новости
for i in temp:
	mas_src_img.append(i.get('src'))
#----------------------------------------

#-------------------------------------------
temp = soup.select("h2.story__title a") #ссылки на новости
mas_a_herf=[]
for i in temp:
	mas_a_herf.append("https://news.yandex.ru"+i.attrs["href"])
#--------------------------------------------

#-----------------------------------------
mas_text_h2=[]
temp = soup.select("h2.story__title") #заголовки новостей
for i in temp:
	mas_text_h2.append(i.get_text())
#-----------------------------------------

#-----------------------------------------
mas_text=[]
temp = soup.select("div.story__text") #краткое описание новостей
for i in temp:
	mas_text.append(i.get_text())
#-----------------------------------------

#print(mas_src_img[0])
#print(mas_a_herf[0])
#print(mas_text_h2[0])
#print(mas_text[0])

itog=[mas_src_img, mas_a_herf, mas_text_h2, mas_text]

#temp=json.dumps(itog)
temp=json.dumps(mas_src_img)
print('В виде json:')
print(temp)
temp2=json.loads(temp)
print('В виде python:')
print(temp2)