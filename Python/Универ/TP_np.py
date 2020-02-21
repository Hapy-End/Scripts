#Библиотеки
import random as rd
import numpy as np
import np.random as nrd

#Функции
#Создание матрицы
def mc(rows,cols,FROM,TO,nm):
  return(smc(rows,cols,FROM,TO,nm))
#Без numpy
def smc(rows,cols,FROM,TO,nm):
  if nm==1:
    return[rd.randint(FROM,TO) for i in range(rows)]
  else:
    return[[rd.randint(FROM,TO) for i in range(rows)] for j in range(cols)]
#С помощь numpy
def nmc(rows,cols,FROM,TO,nm):
  if nm==1:
    return(nrd.randint(FROM,TO,(rows,cols)))
  else:
    return(nrd.randint(FROM,TO,rows))

#Вывод матрицы
def mp(mList):
  try:
    for elem in mList:
      print(' '.join([str(elem[i]) for i in range(len(elem))]))
  except:
    for elem in mList:
      print(str(elem), end=' ')
    print()

#Отступ
def ots(cc):
  print('-'*cc)

#Вывод задания
def pEx(NUM):
  print('-'*16,'Задание',NUM,'-'*16)

#Вариант 9
print('-'*17+'Вариант 9'+'-'*17)
#Задание 1*
pEx(1)
arr=mc(10,10,1,2,2)
mp(arr)
count=0
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]==arr[j]:
            count+=1
print('Кол-во одинаковых строк',count)
ots(43)

#Задание 2*
pEx(2)
arr=mc(6,6,10,20,2)
mp(arr)
for i in range(len(arr)):
  sum=0
  count=0
  for j in range(len(arr[i])):
    count+=1
    sum+=arr[i][j]
  print('Среднее',i+1,'строки =',sum/count)
ots(43)

#Задание 3*
pEx(3)
arr=mc(10,1,10,40,1)
mp(arr)
for i in range(len(arr)):
  if arr[i]%2==0:
    arr[i]*=2
  else:
    arr[i]=0
mp(arr)
ots(43)

#Задание 4*
pEx(4)
arr=mc(5,5,-100,100,2)
mp(arr)
for i in range(len(arr)):
  sum=0
  for j in range(len(arr[i])):
    if arr[j][i]<0:
      sum+=arr[j][i]
  print('Сумма отр. элем.',i+1,'столбца = ',sum)
ots(43)

#Задание 5*
pEx(5)
arr_a=mc(10,1,-20,20,1)
arr_b=mc(10,1,-20,20,1)
mp(arr_a)
mp(arr_b)
for j in arr_b:
  if j>=0:
    arr_a.append(j)
mp(arr_a)
ots(43)

#Общий вариант
print('-'*15+'Общий вариант'+'-'*15)

#Задание 1*
pEx(1)
arr=mc(5,5,0,9,2)
mp(arr)
arr_rev=[i[:] for i in arr]
for i in range(len(arr)):
  arr_rev[i]=arr[i][::-1]
arr_rev=arr_rev[::-1]
for i in range(len(arr)):
  for j in range(len(arr[i])):
    if (i+j<len(arr)-1):
      arr[i][j]=arr_rev[i][j]
    if i+j>len(arr)-1:
      arr[i][j]=arr_rev[i][j]
ots(9)
mp(arr)
ots(43)

#Задание 2*
pEx(2)
arr=mc(10,1,0,20,1)
mp(arr)
count=0
for i in range(len(arr)):
  if (arr[i-1 if i>1 else i+1]<arr[i]>arr[i+1 if i<len(arr)-1 else i-1]):
    count+=1
print('Результат',count)
ots(43)

#Задание 3*
pEx(3)
arr=mc(15,1,0,50,1)
mp(arr)
for i in range(len(arr)):
  if (arr[i-1 if i>1 else i+1]>arr[i]<arr[i+1 if i<len(arr)-1 else i-1]):
    print('Результат',i)
    break
ots(43)

#Задание 4*
pEx(4)
arr=mc(15,1,0,50,1)
mp(arr)
arr_max=arr[0]
for i in range(len(arr)):
  if (arr[i-1 if i>1 else i+1]>arr[i]<arr[i+1 if i<len(arr)-1 else i-1]):
    continue
  elif (arr[i-1 if i>1 else i+1]<arr[i]>arr[i+1 if i<len(arr)-1 else i-1]):
    continue
  else:
    if arr[i]>arr_max:
      arr_max=arr[i]
print('Результат',arr_max)
ots(43)

#Задание 5*
pEx(5)
arr=mc(6,6,1,9,2)
mp(arr)
arr_min=arr[0][0]
for i in range(len(arr)):
  for j in range(len(arr[i])):
    if arr[i][j]<arr_min:
      arr_min=arr[i][j]
for i in range(len(arr)):
  for j in range(len(arr[i])):
    if i+j>len(arr)-1:
      arr[i][j]=0
    elif (i+j<len(arr)-1) and (i<j):
      arr[i][j]=arr_min
ots(11)
mp(arr)