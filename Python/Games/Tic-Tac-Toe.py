from tkinter import *
from random import randint as r

GRID_SIZE = 3
SQUARE_SIZE = 150
PADDING = SQUARE_SIZE // 10
wins=[0,0]
WinP=[[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7],[-1,-2,-3]]
step=0
WinC=0
Winer='No winers'
alls = set()
crosses = set()
zeros = set()
IN_GAME=True

def TheEnd():
    if Winer.startswith('Крестики'):
        wins[0]+=1
    elif Winer.startswith('Нолики'):
        wins[1]+=1
    c.create_rectangle(0,0,GRID_SIZE * SQUARE_SIZE,GRID_SIZE * SQUARE_SIZE,fill='black')
    c.create_text(SQUARE_SIZE*GRID_SIZE/2, PADDING*1.5,
                  text=('Счёт:   X - '+str(wins[0])+'           O - '+str(wins[1])),
                  font="monospaced 20",
                  fill="white")
    TextWin = c.create_text(SQUARE_SIZE*GRID_SIZE/2, SQUARE_SIZE*GRID_SIZE/2,
                  text=Winer,
                  font="Arial 30",
                  fill="white")
    ExitBtn = c.create_rectangle(GRID_SIZE*SQUARE_SIZE/2, #x1
    GRID_SIZE * SQUARE_SIZE-SQUARE_SIZE/2, #y1
    GRID_SIZE * SQUARE_SIZE, #x2
    GRID_SIZE * SQUARE_SIZE, #y2
    fill='red')
    ExitText = c.create_text(GRID_SIZE*SQUARE_SIZE-SQUARE_SIZE*0.75, GRID_SIZE*SQUARE_SIZE-PADDING*2.4,
                      text="Выход",
                      font="Helvetica 25",
                      fill="white")
    RestartBtn = c.create_rectangle(0, #x1
    GRID_SIZE * SQUARE_SIZE-SQUARE_SIZE/2, #y1
    GRID_SIZE * SQUARE_SIZE/2, #x2
    GRID_SIZE * SQUARE_SIZE, #y2
    fill='green')
    RestartText = c.create_text(SQUARE_SIZE*0.75, GRID_SIZE*SQUARE_SIZE-PADDING*2.4,
                      text="Заново",
                      font="Helvetica 25",
                      fill="white")
    c.tag_bind(ExitBtn,"<Button-1>",EXIT)
    c.tag_bind(RestartBtn,"<Button-1>",RESTART)
    c.tag_bind(ExitText,"<Button-1>",EXIT)
    c.tag_bind(RestartText,"<Button-1>",RESTART)
    c.update()

def EXIT(event):
    root.destroy()

def RESTART(event):
    global IN_GAME,nWinP,c
    IN_GAME=True
    c.delete(ALL)
    c.destroy()
    c = Canvas(root, width=GRID_SIZE * SQUARE_SIZE, height=GRID_SIZE * SQUARE_SIZE)
    c.pack()
    crosses.clear()
    zeros.clear()
    qwerty=1
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            c.create_rectangle(j * SQUARE_SIZE, i * SQUARE_SIZE,
                         j * SQUARE_SIZE + SQUARE_SIZE,
                         i * SQUARE_SIZE + SQUARE_SIZE, fill='white',tag='bl'+str(i)+str(j))
            c.tag_bind('bl'+str(i)+str(j),'<Button-1>', lambda event: click(event))
            alls.add(qwerty)
            qwerty+=1
    c.update()
    GameProcess()

def GameProcess():
    global IN_GAME,WinC,Winer
    if IN_GAME:
        checker=crosses
        Winer='Крестики выиграли'
        while True:
            WinC=0
            for i in WinP:
                if WinC==3:
                    WinC=0
                    IN_GAME=False
                    TheEnd()
                else:
                    WinC=0
                for ii in i:
                    for j in checker:
                        if ii==j:
                            WinC+=1
            if checker is crosses:
                checker=zeros
                Winer='Нолики выиграли!!!'
            else:
                break
    if IN_GAME and (len(alls)==0):
            Winer='Ничья'
            IN_GAME=False
            TheEnd()
def add_elem(crt,x1,x2,y1,y2):
    if crt=='zero':
        shape = c.create_oval(x1+PADDING,y1+PADDING,
        x2-PADDING,y2-PADDING,
        outline='black',width=PADDING)
        elem = c.find_withtag(shape)[0]
        zeros.add(elem)
    else:
        shape = c.create_line(x1+PADDING*2,y1+PADDING*2,
        x1+PADDING,y1+PADDING,
        x2-PADDING,y2-PADDING,
        (x2+x1)/2,(y1+y2)/2,
        x1+PADDING,y2-PADDING,
        x2-PADDING,y1+PADDING,
        x2-PADDING*2,y1+PADDING*2,
        fill='black',width=PADDING)
        elem = c.find_withtag(shape)[0]
        crosses.add(elem)

def click(event):
    global IN_GAME,step
    if IN_GAME:
        try:
            ids = c.find_withtag(CURRENT)[0]
            x1, y1, x2, y2 = c.coords(ids)
            if ids not in crosses:
              if ids not in zeros:
                if step==0:
                    add_elem('cross',x1,x2,y1,y2)
                    crosses.add(ids)
                    alls.remove(ids)
                    step+=1
                    GameProcess()
                else:
                    add_elem('zero',x1,x2,y1,y2)
                    zeros.add(ids)
                    alls.remove(ids)
                    step-=1
                    GameProcess()
            c.update()
        except:
            print('Ошибка')

root = Tk()
root.title("Крестики-Нолики")
c = Canvas(root, width=GRID_SIZE * SQUARE_SIZE, height=GRID_SIZE * SQUARE_SIZE)
c.pack()
qwerty=1
for i in range(GRID_SIZE):
    for j in range(GRID_SIZE):
      c.create_rectangle(j * SQUARE_SIZE, i * SQUARE_SIZE,
                         j * SQUARE_SIZE + SQUARE_SIZE,
                         i * SQUARE_SIZE + SQUARE_SIZE, fill='white',tag='bl'+str(i)+str(j))
      c.tag_bind('bl'+str(i)+str(j),'<Button-1>', lambda event: click(event))
      alls.add(qwerty)
      qwerty+=1
root.mainloop()