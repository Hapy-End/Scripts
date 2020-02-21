import pandas as pd
import requests as rq
import numpy as np
from lxml import html
import os

group = 25604
sem = 2
update = True
file_name = 'edu-site.html'

if update or file_name not in os.listdir('BD'):
    Response = rq.get('https://edu.donstu.ru/Rasp/Rasp.aspx',params='group='+str(group)+'&sem='+str(sem))
    with open('BD/'+file_name,'w') as f:
        f.write(Response.text)
Html = ''
with open('BD/'+file_name,'r') as f:
    Html = f.read()
Body = html.fromstring(Html)
Tb = Body.xpath('//td/text()')

WeekDay = 'Понедельник'
Header = ['Время начала','Время конца','Предмет','Преподаватель','Аудитория']

for i in range(len(Tb)):
    if WeekDay in Tb[i]:
        Tb = Tb[i+1:]
        break

nTb = []
ids = []

j = 2
for i in range(len(Tb)):
    if Tb[i].find('\xa0')!=-1:
        nTb.append(Tb[j:i])
        j = i+1
    if i==len(Tb)-1 and j!=len(Tb)-1:
        nTb.append(Tb[j:])

for i in range(len(nTb)):
    ids.append(WeekDay)
    for j in range(1,len(nTb[i])):
        if 'ауд.' in nTb[i][j-1]:
            WeekDay = nTb[i][j]
            nTb[i].remove(nTb[i][j])
            break
    if len(nTb[i])>=5:
        pass
    elif len(nTb[i])==3:
        for w in range(2):
            nTb[i].insert(w,nTb[i-1][w])

#for i in range(1,len(nTb)):
#    nTb[i].insert(0,ids[i])
#nTb[0] = ['День','Время начала','Время конца','Предмет','Преподаватель','Аудитория']
nTb = np.array(nTb[1:])

data = pd.DataFrame(nTb, index=ids[1:], columns=Header)
print(data)
print('Saving...')
data.to_csv('rasp.csv')
print('Saved in rasp.csv')