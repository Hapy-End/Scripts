rows,words,letters = 0,0,0
txt = ''
with open('txt') as file:
    txt = file.read()
print(txt)
rows = len(txt.split('\n'))-1
print("Кол-во строк:",rows)
words = len(txt.split(' '))
print("Кол-во слов:",words)
for i in txt.upper():
    if (ord("A")<=ord(i)<=ord("Z")) or (ord("А")<=ord(i)<=ord("Я")):
        letters+=1
print("Кол-во букв:",letters)