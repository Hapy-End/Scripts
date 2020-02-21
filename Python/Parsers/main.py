import requests as rq
from lxml import html
import os

Response = rq.get('http://pogoda-service.ru/climate_table.php',params='country=RS&station=347300&day_begin=01&month_begin=01&day_end=31&month_end=12')
HTML = html.fromstring(Response.text)
#Th = HTML.xpath('//th[@class="th_res"]/text()')
Td = HTML.xpath('//td[@class="td_res"]/text()')
csvfile = "Дата,Максимальная температура,Минимальная температура,Средняя температура, Атмосферное давление,Скорость ветра,Осадки,Эффективная температура\n".replace(',',';')
M = 0
for i in range(0,len(Td),8):
	iTd = Td[i:i+8]
	for j in range(len(iTd)):
		jTd = iTd[j].replace('.',',')
		if j == 0:
			if int(jTd.split(' ')[0]) == 1:
				M += 1
			jTd = jTd[0:2] + "." + ("0"+str(M) if M<10 else str(M))
		csvfile += jTd + ";"
	csvfile = csvfile[:-1] + "\n"
with open('data.csv','w') as f:
	f.write(csvfile)