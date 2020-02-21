rows,words,letters = 0,0,0
txt = ''
with open('str.xml') as file:
    txt = file.read()
print(txt)
rows = len(txt.split('\n'))-1
print("Кол-во строк:",rows)
words = len(txt.split(' '))
def wordsplit(text):
    symbols = [',','.','\n']
    NoSymbols = True
    for s in symbols:
        if s in text and NoSymbols:
            NoSymbols = False
            for text2 in text.split(s):
                if text2 != '':
                    yield list(wordsplit(text2))
    if NoSymbols:
        yield text
wordslist = []
for i in txt.split(' '):
    wordslist.extend(list(wordsplit(i)))
words = len(wordslist)-1
print("Кол-во слов:",words)
for i in txt.upper():
    if (ord("A")<=ord(i)<=ord("Z")) or (ord("А")<=ord(i)<=ord("Я")):
        letters+=1
print("Кол-во букв:",letters)