import requests as rq
from lxml import html

Response = rq.get('http://www.pogodaiklimat.ru/history/34730.htm')
HTML = html.fromstring(Response.text)
Th = HTML.xpath('//tr/td/text()')
Td = HTML.xpath('//td/nobr/text()')
csvfile = "year,month,value,rank\n"
M = ['Jan','Feb','Dec']
mmin = 0

for i in range(0,len(Td),13):
	iTd = Td[i:i+13][0],Td[i:i+13][1],Td[i:i+13][11]
	for i in iTd:
		if mmin > float(i):
			mmin = float(i)
for i in range(0,len(Td),13):
	iTd = Td[i:i+13][0],Td[i:i+13][1],Td[i:i+13][11]
	iTds = sorted(list(map(float,iTd)))[::-1]
	rank = []
	for j in range(len(iTd)):
		rr = 1+iTds.index(float(iTd[j]))
		if len(rank)>0:
			try:
				rank.index(rr)
				rank.append(rr+1)
			except:
				rank.append(rr)
		else:
			rank.append(rr)
		csvfile += Th[i//13+1]+','+M[j]+','+(iTd[j] if float(iTd[j])<100 else 'NA')+','+str(rank[-1])+','+str(round(float(iTd[j])-mmin,1)) +'\n'
print(csvfile)
with open('data22.csv','w') as f:
	f.write(csvfile)
ttt = ""
with open('abs.txt','r') as f:
	ttt = f.read()
tt = ttt.split('\n')
mm = [0,0,"","",0,0]
year = tt[1].split(',')[0]
ss = 0
for i in tt[1:]:
	ii = i.split(',')
	if year != ii[0]:
		print(year,round(ss/3,1))
		year = ii[0]
		ss = 0
	ss += float(ii[2])
	for j in range(len(ii)):
		if j == 2 and mm[0]>float(ii[j]):
			mm[0]=float(ii[j])
			mm[2]=ii[1]
			mm[4]=ii[0]
		if j==2 and mm[1]<float(ii[j]):
			mm[1]=float(ii[j])
			mm[3]=ii[1]
			mm[5]=ii[0]
print(mm)