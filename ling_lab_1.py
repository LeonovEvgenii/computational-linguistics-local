#!/usr/bin/python3
from bs4 import BeautifulSoup
from urllib.request import urlopen
import json

html_doc = urlopen('https://news.yandex.ru/science.html').read()

soup = BeautifulSoup(html_doc, 'lxml')
 
result_dic={}
list_temp = []

list_story = soup.select("div.story")#ссылки на новости
for story in list_story:
	
	list_temp.clear()	

	a = story.find('a', class_='link')	

	img = a.find('img', class_='image')
	list_temp.append(img.attrs["src"]) # Картинка

	div = story.find('div', class_='story__content')
	h2 = div.find('h2', class_='story__title')
	#a_title = h2.find('a', class_='link')
	#list_temp.append(a_title.get_text())# можно так, но и без него работает
	list_temp.append(h2.get_text()) # Заголовок

	div_text = div.find('div', class_='story__text')
	list_temp.append(div_text.get_text())

	result_dic["https://news.yandex.ru"+a.attrs["href"]] = list_temp # записали ссылку на новость
	
	#print("https://news.yandex.ru"+a.attrs["href"])
	#print(list_temp[0])
	#print(list_temp[1])
	#print(list_temp[2])	
	#print('\n')

	i = input('Продолжить?   1/0 в роли д/н  ')

	if i=='1':
		temp=json.dumps(result_dic)
		print('в jsone')
		print(temp)
		temp2=json.loads(temp)
		print('в pythone')
		print(temp2)
	else:
		break	


#print(result_dic)

temp=json.dumps(result_dic)
#print('в jsone')
#print(temp)
temp2=json.loads(temp)
#print('в pythone')
#print(temp2)