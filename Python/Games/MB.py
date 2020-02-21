from tkinter import *
from random import randint as ri
import time
##########################
root = Tk()
root.title("Морской бой")
GRID_SIZE=10
SQUARE_SIZE=25
c = Canvas(root, width=((1.75 + GRID_SIZE) * SQUARE_SIZE)*4, height=(2.5 + GRID_SIZE) * SQUARE_SIZE*2)
c.pack()
SSIZE=25
Padding=(GRID_SIZE*3.4)*SQUARE_SIZE
PaddingStart=3*SQUARE_SIZE
sPadding=8
my_coords,amy_coords,bot_coords,abot_coords,my_flot_coords,bot_flot_coords=[],[],[],[],[],[]
IN_GAME=False
STEP=True
SetType=0
SelectedFlot=0
ti=0
cWins=[0,0]
StepCounts=[0,0]
Difficulty=-1
ShipCount,BotShipCount=[4,3,2,1],[4,3,2,1]
MyLSC,BotLSC=[0,0,0,0],[0,0,0,0]
PrevAttack=[]
FlotOrient=0
DiffText=('Очень лёгкий','Лёгкий','Средний','Сложный','Очень сложный','Невозможный')
vectors = [(0,1),(0,-1),(-1,0),(1,0)]
points=0
fonts=0

Theme= {'Blue':
                {
                    'SimpleBtn':        '#2454f4',
                    'SimpleBtnShadow':  '#2962ff',
                    'Main':             '#2196f3',
                    'MainBtn':          '#0d47a1',
                    'ErrorBtn':         '#ff1744',
                    'Ship':             '#311b92',
                    'Damage':           '#f44336',
                    'MainText':         '#000000',
                    'BtnText':          '#ffffff',
                    'BG':               '#1a237e',
                    'Missing':          '#2196f3',
                    'Kill':             '#f50057',
                    'MainBtnShadow':    '#1565c0',
                    'ErrorBtnShadow':   '#d50000',
                    'Grid':             '#cccccc',
                    'Shadow':           '#283593',
                    'FG':               '#ffffff'
                },
         'Black':
                {
                    'SimpleBtn':        '#546e7a',
                    'SimpleBtnShadow':  '#455a64',
                    'Main':             '#333333',
                    'MainBtn':          '#37474f',
                    'ErrorBtn':         '#607e8b',
                    'Ship':             '#000000',
                    'Damage':           '#245a64',
                    'MainText':         '#111111',
                    'BtnText':          '#ffffff',
                    'BG':               '#262626',
                    'Missing':          '#90a6ae',
                    'Kill':             '#607d8b',
                    'MainBtnShadow':    '#263238',
                    'ErrorBtnShadow':   '#446f7a',
                    'Grid':             '#eeeeee',
                    'Shadow':           '#eeeeee',
                    'FG':               '#ffffff'
                },
         'Red':
                {
                    'SimpleBtn':        '#e53935',
                    'SimpleBtnShadow':  '#d32f2f',
                    'Main':             '#f44336',
                    'MainBtn':          '#c62828',
                    'ErrorBtn':         '#ff5252',
                    'Ship':             '#b71c1c',
                    'Damage':           '#d50000',
                    'MainText':         '#222222',
                    'BtnText':          '#ffffff',
                    'BG':               '#d50000',
                    'Missing':          '#ff5252',
                    'Kill':             '#b71c1c',
                    'MainBtnShadow':    '#b71c1c',
                    'ErrorBtnShadow':   '#ff1744',
                    'Grid':             '#ffcdd2',
                    'Shadow':           '#ff1744',
                    'FG':               '#ffffff'
                }
         }
sTheme = Theme['Blue']
newTheme= Theme['Blue']
def FirstStart():
    LoadBD()
    for i in range(int(GRID_SIZE*2.5)):
            for j in range(int(GRID_SIZE*4.7)):
                c.create_rectangle(j * SQUARE_SIZE,i * SQUARE_SIZE,
                                 j * SQUARE_SIZE + SQUARE_SIZE,
                                 i * SQUARE_SIZE + SQUARE_SIZE, fill=Theme['Black']['BG'],outline=Theme['Black']['MainText'])
            c.update()
    c.create_text(SQUARE_SIZE*47//2,SQUARE_SIZE*25//2,text='Морской Бой',font=fonts['vvLargeBM'], fill=sTheme['BtnText'])
    c.create_text(SQUARE_SIZE*47//2,SQUARE_SIZE*30//2,text='@m.m.abdul',font=fonts['LargeBM'], fill=sTheme['BtnText'])
    c.update()
    time.sleep(1.5)
    c.delete(ALL)
    c.destroy()
    NewGame()
def LoadBD():
    global PaddingStart,Padding,sTheme,newTheme,PrevAttack,points,fonts,SetType,SSIZE,SQUARE_SIZE,c,IN_GAME,my_coords,amy_coords,bot_coords,abot_coords,my_flot_coords,bot_flot_coords,ShipCount,BotShipCount,MyLSC,BotLSC,Difficulty
    PrevAttack,amy_coords,bot_coords,abot_coords,my_flot_coords,bot_flot_coords=[],[],[],[],[],[]
    sTheme=newTheme
    SQUARE_SIZE=SSIZE
    IN_GAME,STEP=False,True
    Difficulty=-1
    SetType=0
    StepCounts=[0,0]
    ShipCount,BotShipCount=[4,3,2,1],[4,3,2,1]
    MyLSC,BotLSC=[0,0,0,0],[0,0,0,0]
    Padding=(GRID_SIZE*3.4)*SQUARE_SIZE
    PaddingStart=3*SQUARE_SIZE
    points =   [[22.5 *SQUARE_SIZE, 12*SQUARE_SIZE, 23.5*SQUARE_SIZE, 13*SQUARE_SIZE, 24.5*SQUARE_SIZE, 12*SQUARE_SIZE,
             24.5 *SQUARE_SIZE, 10.5*SQUARE_SIZE, 22.5*SQUARE_SIZE, 10.5*SQUARE_SIZE, 22.5*SQUARE_SIZE, 12*SQUARE_SIZE],
            [22.5 *SQUARE_SIZE,6*SQUARE_SIZE, 23.5*SQUARE_SIZE, 5*SQUARE_SIZE, 24.5*SQUARE_SIZE, 6*SQUARE_SIZE,
             24.5 *SQUARE_SIZE, 7.5*SQUARE_SIZE, 22.5*SQUARE_SIZE, 7.5*SQUARE_SIZE, 22.5*SQUARE_SIZE, 6*SQUARE_SIZE],
            [22   *SQUARE_SIZE, 8*SQUARE_SIZE, 20.5*SQUARE_SIZE, 8*SQUARE_SIZE, 19.5*SQUARE_SIZE, 9*SQUARE_SIZE,
             20.5 *SQUARE_SIZE, 10*SQUARE_SIZE, 22*SQUARE_SIZE, 10*SQUARE_SIZE, 22*SQUARE_SIZE, 8*SQUARE_SIZE],
            [25   *SQUARE_SIZE, 8*SQUARE_SIZE, 26.5*SQUARE_SIZE, 8*SQUARE_SIZE, 27.5*SQUARE_SIZE, 9*SQUARE_SIZE,
             26.5 *SQUARE_SIZE, 10*SQUARE_SIZE, 25*SQUARE_SIZE, 10*SQUARE_SIZE, 25*SQUARE_SIZE, 8*SQUARE_SIZE]]
    fonts= {'vSmall':'Ariel '+str(int(SQUARE_SIZE//2.3))+' bold',
        'Small':'monospaced '+str(SQUARE_SIZE//2),
        'SmallBM':'monospaced '+str(SQUARE_SIZE//2)+' bold',
        'Medium':'monospaced '+str(int(SQUARE_SIZE//1.5)),
        'MediumBM':'monospaced '+str(int(SQUARE_SIZE//1.5))+' bold',
        'LargeBM':'monospaced '+str(SQUARE_SIZE)+' bold',
        'vLargeBM':'monospaced '+str(int(SQUARE_SIZE*1.45))+' bold',
        'vvLargeBM':'monospaced '+str(SQUARE_SIZE*2)+' bold'}
def Restart(event):
    for i in range(int(GRID_SIZE*2.5)):
            for j in range(int(GRID_SIZE*4.7)):
                c.create_rectangle(j * SQUARE_SIZE,i * SQUARE_SIZE,
                                 j * SQUARE_SIZE + SQUARE_SIZE,
                                 i * SQUARE_SIZE + SQUARE_SIZE, fill=sTheme['FG'],outline=sTheme['Grid'])
            c.update()
    time.sleep(0.05)
    c.delete(ALL)
    c.destroy()
    LoadBD()
    NewGame()
def NewGame():
    global c
    c = Canvas(root, width=((1.75 + GRID_SIZE) * SQUARE_SIZE)*4, height=(2.5 + GRID_SIZE) * SQUARE_SIZE*2)
    c.pack()
    BackgroundGrid()
    MyGrid()
    EnemyGrid()
    TabloPMType()
    FlotBar()
    DiffBar()
    SettingBar()
def StepControl():
    global STEP
    STEP=True
def TheEnd():
    global IN_GAME,STEP
    if (sum(MyLSC)==0) or (sum(BotLSC)==0):
        if sum(MyLSC)==0:
            cWins[1]+=1
            c.itemconfig('gametitle',text='ВЫ ПРОИГРАЛИ',font=fonts['vLargeBM'])
        elif sum(BotLSC)==0:
            c.itemconfig('gametitle',text='ВЫ ВЫИГРАЛИ',font=fonts['vLargeBM'])
            cWins[0]+=1
        for i in bot_flot_coords:
            c.itemconfig('bf'+str(i[-1][0])+str(i[0][0])+str(i[0][-1]),outline=sTheme['Ship'],width=2)
        c.itemconfig('score', text=str(cWins[0])+'    '+str(cWins[1]))
        IN_GAME=False
        STEP=True
        c.create_rectangle(SQUARE_SIZE*37.5,22.5*SQUARE_SIZE,SQUARE_SIZE*46.5,24.5*SQUARE_SIZE,fill=sTheme['MainBtn'],outline=sTheme['MainBtnShadow'],tag='restart')
        c.create_text(SQUARE_SIZE*42,23.5*SQUARE_SIZE, text='ЕЩЁ РАЗОК',font=fonts['SmallBM'], fill=sTheme['BtnText'],tag='restart')
        c.tag_bind('restart','<Button-1>', lambda event: Restart(event))
def BotPM():
    global abot_coords,bot_flot_coords
    i=3
    while i>=0:
        if ShipCount[i]==0:
            i-=1
            continue
        FlotOrient=ri(0,1)
        rID=ri(0,len(amy_coords)-1)
        rID=amy_coords[rID]
        x1=Padding+rID[0]*SQUARE_SIZE
        y1=PaddingStart+rID[1]*SQUARE_SIZE
        if FlotOrient==0:
            x2=x1+SQUARE_SIZE * (i+1)
            y2=y1+SQUARE_SIZE
        else:
            x2=x1+SQUARE_SIZE
            y2=y1+SQUARE_SIZE * (i+1)
        Ship = FlotCheck([[int((x1-Padding)//SQUARE_SIZE),int((y1-PaddingStart)//SQUARE_SIZE)],
                          [int((x2-Padding)//SQUARE_SIZE-1),int((y2-PaddingStart)//SQUARE_SIZE-1)]],bot_flot_coords)
        ship = Ship[0:-1]
        pch=0
        for shippart in ship:
            if shippart not in abot_coords:
                bot_flot_coords.remove(Ship)
                pch=1
                break
        if pch==1:
            continue
        c.create_rectangle(x1,y1,x2,y2,outline=sTheme['Grid'],tag='bf'+str(i+1)+str(int((x1-Padding)//SQUARE_SIZE))+str(int((y1-PaddingStart)//SQUARE_SIZE)))
        x1=ship[0][0]-1
        x2=ship[-1][0]+1
        y1=ship[0][1]-1
        y2=ship[-1][1]+1
        while x1!=(x2+1):
            while y1!=(y2+1):
                if [x1,y1] in abot_coords:
                    abot_coords.remove([x1,y1])
                y1+=1
            x1+=1
            y1=ship[0][1]-1
        BotShipCount[i]-=1
        BotLSC[i]+=1
        if BotShipCount[i]==0:
            i-=1
def AutoPM(event):
        global amy_coords,my_flot_coords
        i=3
        while i>=0:
            if ShipCount[i]==0:
                i-=1
                continue
            FlotOrient=ri(0,1)
            rID=ri(0,len(amy_coords)-1)
            rID=amy_coords[rID]
            x1=PaddingStart+rID[0]*SQUARE_SIZE
            y1=PaddingStart+rID[1]*SQUARE_SIZE
            if FlotOrient==0:
                x2=x1+SQUARE_SIZE * (i+1)
                y2=y1+SQUARE_SIZE
            else:
                x2=x1+SQUARE_SIZE
                y2=y1+SQUARE_SIZE * (i+1)
            Ship = FlotCheck([[(x1-PaddingStart)//SQUARE_SIZE,(y1-PaddingStart)//SQUARE_SIZE],
                              [(x2-PaddingStart)//SQUARE_SIZE-1,(y2-PaddingStart)//SQUARE_SIZE-1]],my_flot_coords)
            ship = Ship[0:-1]
            pch=0
            for shippart in ship:
                if shippart not in amy_coords:
                    my_flot_coords.remove(Ship)
                    pch=1
                    break
            if pch==1:
                continue
            time.sleep(0.05)
            c.create_rectangle(x1,y1,x2,y2,width=2, outline=sTheme['Ship'],tag='ff'+str(i+1)+str(int((x1-PaddingStart)//SQUARE_SIZE))+str(int((y1-PaddingStart)//SQUARE_SIZE)))
            c.update()
            x1=ship[0][0]-1
            x2=ship[-1][0]+1
            y1=ship[0][1]-1
            y2=ship[-1][1]+1
            while x1!=(x2+1):
                while y1!=(y2+1):
                    if [x1,y1] in amy_coords:
                        amy_coords.remove([x1,y1])
                    y1+=1
                x1+=1
                y1=ship[0][1]-1
            ShipCount[i]-=1
            MyLSC[i]+=1
            if ShipCount[i]==0:
                i-=1
        c.create_rectangle(0,22*SQUARE_SIZE,47*SQUARE_SIZE,25*SQUARE_SIZE, fill=sTheme['BG'],outline=sTheme['Shadow'])
        PlacementProgress()

def BotAttack():
    global PrevAttack,bot_flot_coords
    if IN_GAME:
        if Difficulty==0:
            randcoords=my_coords[0]
        elif (Difficulty==5) or (Difficulty==4) and (len(bot_flot_coords)==1):
            while True:
                rJD=ri(0,len(my_flot_coords)-1)
                rID=ri(0,len(my_flot_coords[rJD])-2)
                randcoords=my_flot_coords[rJD][rID]
                if randcoords in my_coords:
                    break
        elif (len(PrevAttack)==0) or (Difficulty==1):
            rID=ri(0,len(my_coords)-1)
            randcoords=my_coords[rID]
        elif (len(PrevAttack)>1) and (Difficulty>=3):
            while True:
                for i in range(len(PrevAttack)):
                    if PrevAttack[0][1]==PrevAttack[1][1]:
                        rID=ri(2,3)
                    else:
                        rID=ri(0,1)
                    randcoords=[PrevAttack[i][0]+vectors[rID][0],PrevAttack[i][1]+vectors[rID][1]]
                    if randcoords in my_coords:
                        break
                if randcoords in my_coords:
                    break
        elif (len(PrevAttack)==1) or (Difficulty>=2):
            while True:
                VarAttack=[0,1,2,3]
                for i in range(len(PrevAttack)):
                    rID=ri(0,len(VarAttack)-1)
                    randcoords=[PrevAttack[i][0]+vectors[VarAttack[rID]][0],PrevAttack[i][1]+vectors[VarAttack[rID]][1]]
                    if randcoords in my_coords:
                        break
                    else:
                        VarAttack.remove(VarAttack[rID])
                if randcoords in my_coords:
                    break
        StepCounts[0]+=1
        my_coords.remove(randcoords)
        c.itemconfig('my'+str(randcoords[1])+str(randcoords[0]), fill=sTheme['Missing'])
        AM=0
        for j in range(len(my_flot_coords)):
            if (randcoords in my_flot_coords[j]):
                AM=1
                c.itemconfig('my'+str(randcoords[1])+str(randcoords[0]), fill=sTheme['Damage'])
                c.update()
                PrevAttack.append(randcoords)
                destroy=int(my_flot_coords[j][-1][-1])+1
                my_flot_coords[j][-1][-1]=str(destroy)
                if int(my_flot_coords[j][-1][-1])==my_flot_coords[j][-1][0]:
                    PrevAttack=[]
                    c.itemconfig('ff'+str(my_flot_coords[j][-1][0])+str(my_flot_coords[j][0][0])+str(my_flot_coords[j][0][1]),fill=sTheme['Kill'],outline=sTheme['Grid'],width=1)
                    MyLSC[my_flot_coords[j][-1][0]-1]-=1
                    ship=my_flot_coords[j][0:-1]
                    x1=ship[0][0]-1
                    x2=ship[-1][0]+1
                    y1=ship[0][1]-1
                    y2=ship[-1][1]+1
                    while x1!=(x2+1):
                        while y1!=(y2+1):
                            time.sleep(0.01)
                            c.itemconfig('my'+str(y1)+str(x1),fill=sTheme['Missing'])
                            if [x1,y1] in my_coords:
                                my_coords.remove([x1,y1])
                            y1+=1
                            c.update()
                        x1+=1
                        y1=ship[0][1]-1
                    my_flot_coords.remove(my_flot_coords[j])
                break
        if AM==1:
            if len(my_flot_coords)>0:
                BotAttack()
            else:
                TheEnd()
        elif (AM==0):
            StepControl()
def FlotCheck(ship,mlist):
    global my_flot_coords
    if ship[0][0]==ship[1][0]:
        if (ship[1][1]-ship[0][1]==0):
            ship=[ship[0]]
        elif (ship[1][1]-ship[0][1]==1):
            ship=ship
        elif (ship[1][1]-ship[0][1]==2):
            ship=[ship[0],[ship[0][0],ship[1][1]-1],ship[1]]
        elif (ship[1][1]-ship[0][1]==3):
            ship=[ship[0],[ship[0][0],ship[1][1]-2],[ship[0][0],ship[1][1]-1],ship[1]]
    elif ship[0][1]==ship[1][1]:
        if (ship[1][0]-ship[0][0]==0):
            ship=[ship[0]]
        elif (ship[1][0]-ship[0][0]==1):
            ship=ship
        elif (ship[1][0]-ship[0][0]==2):
            ship=[ship[0],[ship[1][0]-1,ship[0][1]],ship[1]]
        elif (ship[1][0]-ship[0][0]==3):
            ship=[ship[0],[ship[1][0]-2,ship[0][1]],[ship[1][0]-1,ship[0][1]],ship[1]]
    ship.append([len(ship),'0'])
    mlist.append(ship)
    return ship
def StartGame(event):
    PlacementProgress()
def PlacementProgress():
    global ShipCount,IN_GAME,Difficulty
    if (sum(ShipCount)==0) and (sum(MyLSC)!=0):
        if Difficulty<0:
            c.itemconfig('difftxt',text='ВЫБЕРИТЕ УРОВЕНЬ СЛОЖНОСТИ ЧТОБЫ ПРОДОЛЖИТЬ!',fill=sTheme['ErrorBtn'])
            c.create_rectangle(SQUARE_SIZE*37.5,22.5*SQUARE_SIZE,SQUARE_SIZE*46.5,24.5*SQUARE_SIZE,fill=sTheme['MainBtn'],outline=sTheme['MainBtnShadow'],tag='diffslc')
            c.create_text(SQUARE_SIZE*42,23.5*SQUARE_SIZE, text='НАЧАТЬ',font=fonts['SmallBM'], fill=sTheme['BtnText'],tag='diffslc')
            c.tag_bind('diffslc','<Button-1>',StartGame)
        else:
            for aaa in range(6):
                c.delete('diffbtn'+str(aaa),'difftxt'+str(aaa))
            c.delete('difftxt','diffslc','gametitle','score','tttt')
            IN_GAME=True
            TabloWiners()
    else:
        IN_GAME=False

def DiffControl(event):
    global Difficulty
    Diff = int((c.coords(c.find_withtag(CURRENT)[0])[0]//SQUARE_SIZE-3)//7)
    c.itemconfig('difftxt',text='ВЫБРАН '+DiffText[Diff].upper()+' УРОВЕНЬ')
    for i in range(6):
        if (i==Diff) and (i!=Difficulty):
            dfc = c.coords('diffbtn'+str(i))
            dfc[0]-=SQUARE_SIZE//4
            dfc[1]-=SQUARE_SIZE//4
            dfc[2]+=SQUARE_SIZE//4
            dfc[3]+=SQUARE_SIZE//4
            c.coords('diffbtn'+str(i),dfc)
        elif (i==Difficulty) and (i!=Diff):
            dfc = c.coords('diffbtn'+str(i))
            dfc[0]+=SQUARE_SIZE//4
            dfc[1]+=SQUARE_SIZE//4
            dfc[2]-=SQUARE_SIZE//4
            dfc[3]-=SQUARE_SIZE//4
            c.coords('diffbtn'+str(i),dfc)
    Difficulty=Diff

def DiffBar():
    x1=SQUARE_SIZE*3
    x2=x1
    for i in range(6):
        x2=x1+SQUARE_SIZE*6
        c.create_rectangle(x1,19.5*SQUARE_SIZE,x2,21*SQUARE_SIZE,fill=sTheme['SimpleBtn'],outline=sTheme['SimpleBtnShadow'],tag='diffbtn'+str(i))
        c.create_text(x2-SQUARE_SIZE*3,20.25*SQUARE_SIZE,text=DiffText[i],fill=sTheme['BtnText'],font=fonts['vSmall'],tag='difftxt'+str(i))
        c.tag_bind('diffbtn'+str(i),'<Button-1>', lambda event: DiffControl(event))
        c.tag_bind('difftxt'+str(i),'<Button-1>', lambda event: DiffControl(event))
        x1=x2+SQUARE_SIZE*1
    c.create_text(SQUARE_SIZE*47/2,17.5*SQUARE_SIZE, text='ВЫБЕРИТЕ УРОВЕНЬ СЛОЖНОСТИ',font=fonts['LargeBM'], fill=sTheme['MainText'],tag='difftxt')

#Нижняя панель с кораблями
def FlotBar():
    x1=SQUARE_SIZE
    x2=x1
    for i in range(4,0,-1):
        x2=x1+SQUARE_SIZE*i
        c.create_rectangle(x1,23*SQUARE_SIZE,x2,24*SQUARE_SIZE,fill=sTheme['SimpleBtn'],outline=sTheme['SimpleBtnShadow'],tag='f'+str(i))
        c.tag_bind('f'+str(i),'<Button-1>', lambda event: placement(event))
        x1=x2+SQUARE_SIZE*3
        c.create_text(x2+SQUARE_SIZE,23*SQUARE_SIZE+SQUARE_SIZE/2, text=('x',ShipCount[i-1]),font=fonts['SmallBM'], fill=sTheme['BtnText'],tag='fc'+str(i))
    c.create_rectangle(SQUARE_SIZE*37.5,22.5*SQUARE_SIZE,SQUARE_SIZE*46.5,24.5*SQUARE_SIZE,fill=sTheme['MainBtn'],outline=sTheme['MainBtnShadow'],tag='autopm')
    c.create_text(SQUARE_SIZE*42,23.5*SQUARE_SIZE, text='РАССТАВИТЬ',font=fonts['SmallBM'], fill=sTheme['BtnText'],tag='autopm')
    c.tag_bind('autopm','<Button-1>', lambda event: AutoPM(event))

#Вычисление номера корабля
def checkItem(current):
    global ti
    ids = c.find_withtag(current)[0]
    x1 = int(c.coords(ids)[0]//SQUARE_SIZE)
    if x1<5:
        ti=4
    elif x1<11:
        ti=3
    elif x1<16:
        ti=2
    elif x1<21:
        ti=1
    if ShipCount[ti-1]<=0:
        return(0)
    else:
        return(ti)

##########################
def placement(event):
    global ShipCount,SelectedFlot,FlotOrient
    if SelectedFlot==0:
        i=checkItem(CURRENT)
        PMState=0
        if i!=0:
            while PMState==0:
                FlotOrient=ri(0,1)
                rID=ri(0,len(amy_coords)-1)
                rID=amy_coords[rID]
                x1=PaddingStart+rID[0]*SQUARE_SIZE
                y1=PaddingStart+rID[1]*SQUARE_SIZE
                if FlotOrient==0:
                    x2=x1+SQUARE_SIZE * i
                    y2=y1+SQUARE_SIZE
                else:
                    x2=x1+SQUARE_SIZE
                    y2=y1+SQUARE_SIZE * i
                Ship = FlotCheck([[(x1-PaddingStart)//SQUARE_SIZE,(y1-PaddingStart)//SQUARE_SIZE],
                                  [(x2-PaddingStart)//SQUARE_SIZE-1,(y2-PaddingStart)//SQUARE_SIZE-1]],my_flot_coords)
                ship = Ship[0:-1]
                pch=0
                for shippart in ship:
                    if shippart not in amy_coords:
                        my_flot_coords.remove(Ship)
                        pch=1
                        break
                if pch==1:
                    continue
                PMState=1
                c.itemconfig(CURRENT, fill=sTheme['MainBtn'])
                c.create_rectangle(x1,y1,x2,y2,width=2, outline=sTheme['Ship'],tag='ff'+str(i)+str(ShipCount[i-1]))
                SelectedFlot='ff'+str(i)+str(ShipCount[i-1])
                my_flot_coords.remove(Ship)
                FlotPAD(i)
        else:
            c.itemconfig(CURRENT, fill=sTheme['ErrorBtn'], outline=sTheme['ErrorBtnShadow'])

###############################
def click(event):
    global IN_GAME,bot_coords,bot_flot_coords,STEP
    if IN_GAME and STEP:
        STEP=False
        ids = c.find_withtag(CURRENT)[0]
        x1, y1, x2, y2 = c.coords(ids)
        rID=[(x1-Padding)//SQUARE_SIZE,(y1-PaddingStart)//SQUARE_SIZE]
        if rID in bot_coords:
            StepCounts[1]+=1
            bot_coords.remove(rID)
            for j in range(len(bot_flot_coords)):
                if rID in bot_flot_coords[j]:
                    c.itemconfig(CURRENT, fill=sTheme['Damage'])
                    c.update()
                    destroy=int(bot_flot_coords[j][-1][-1])+1
                    bot_flot_coords[j][-1][-1]=str(destroy)
                    if int(bot_flot_coords[j][-1][-1])==bot_flot_coords[j][-1][0]:
                        c.itemconfig('bf'+str(bot_flot_coords[j][-1][0])+str(bot_flot_coords[j][0][0])+str(bot_flot_coords[j][0][1]),fill=sTheme['Kill'])
                        BotLSC[bot_flot_coords[j][-1][0]-1]-=1
                        ship=bot_flot_coords[j][0:-1]
                        x1=ship[0][0]-1
                        x2=ship[-1][0]+1
                        y1=ship[0][1]-1
                        y2=ship[-1][1]+1
                        while x1!=(x2+1):
                            while y1!=(y2+1):
                                time.sleep(0.01)
                                c.itemconfig('bot'+str(y1)+str(x1),fill=sTheme['Missing'])
                                c.update()
                                if [x1,y1] in bot_coords:
                                    bot_coords.remove([x1,y1])
                                y1+=1
                            x1+=1
                            y1=ship[0][1]-1
                        bot_flot_coords.remove(bot_flot_coords[j])
                    rID=0
                    STEP=True
                    break
        else:
            rID=0
            STEP=True
        if rID!=0:
            c.itemconfig(CURRENT, fill=sTheme['Missing'])
            c.update()
            BotAttack()
        else:
            TheEnd()

#Поле игрока
def MyGrid():
    c.create_rectangle(SQUARE_SIZE*3,SQUARE_SIZE*3,
                       SQUARE_SIZE*3 + GRID_SIZE * SQUARE_SIZE,
                       SQUARE_SIZE*3 + GRID_SIZE * SQUARE_SIZE,width=5, outline=sTheme['BG'],tag='my')
    c.create_text(SQUARE_SIZE*3 + GRID_SIZE * SQUARE_SIZE/2,SQUARE_SIZE*(GRID_SIZE+4),text='ВАШ ФЛОТ',font=fonts['MediumBM'],fill=sTheme['MainText'])
    for i in range(GRID_SIZE):
        c.create_text(SQUARE_SIZE*2+SQUARE_SIZE/2,(i+3.5) * SQUARE_SIZE, text=i+1, font=fonts['Small'], fill=sTheme['MainText'])
        c.create_text((i+3.5) * SQUARE_SIZE,SQUARE_SIZE*2+SQUARE_SIZE/2, text=chr(1040+(i if i!=GRID_SIZE-1 else i+1)),font=fonts['Small'], fill=sTheme['MainText'])
        for j in range(GRID_SIZE):
            c.create_rectangle(SQUARE_SIZE*3 + j * SQUARE_SIZE,SQUARE_SIZE*3 + i * SQUARE_SIZE,
                             SQUARE_SIZE*3 + j * SQUARE_SIZE + SQUARE_SIZE,
                             SQUARE_SIZE*3 + i * SQUARE_SIZE + SQUARE_SIZE, outline=sTheme['Grid'], fill=sTheme['FG'],tag='my'+str(i)+str(j))
            my_coords.append([i,j])
            amy_coords.append([i,j])
#Поле противника
def EnemyGrid():
    c.create_rectangle(Padding,PaddingStart,
                       Padding + GRID_SIZE * SQUARE_SIZE,
                       SQUARE_SIZE*3 + GRID_SIZE * SQUARE_SIZE,width=5, outline=sTheme['BG'],tag='bot')
    c.create_text(Padding + GRID_SIZE * SQUARE_SIZE/2,SQUARE_SIZE*(GRID_SIZE+4),text='ФЛОТ ПРОТИВНИКА',font=fonts['MediumBM'],fill=sTheme['MainText'])
    for i in range(GRID_SIZE):
        c.create_text(Padding + SQUARE_SIZE*11 - SQUARE_SIZE/2,(i+3.5) * SQUARE_SIZE, text=i+1, font=fonts['Small'], fill=sTheme['MainText'])
        c.create_text(Padding + (i+.5) * SQUARE_SIZE,2*SQUARE_SIZE+SQUARE_SIZE/2, text=chr(1040+(i if i!=GRID_SIZE-1 else i+1)),font=fonts['Small'], fill=sTheme['MainText'])
        for j in range(GRID_SIZE):
            c.create_rectangle(Padding + j * SQUARE_SIZE,(i+3) * SQUARE_SIZE,
                             Padding + j * SQUARE_SIZE + SQUARE_SIZE,
                             (i+3) * SQUARE_SIZE + SQUARE_SIZE,outline=sTheme['Grid'], fill=sTheme['FG'],tag='bot'+str(i)+str(j))
            c.tag_bind('bot'+str(i)+str(j),'<Button-1>', lambda event: click(event))
            bot_coords.append([i,j])
            abot_coords.append([i,j])
    BotPM()
#Фоновая сетка
def BackgroundGrid():
    for i in range(int(GRID_SIZE*2.5)):
            for j in range(int(GRID_SIZE*4.7)):
                c.create_rectangle(j * SQUARE_SIZE,i * SQUARE_SIZE,
                                 j * SQUARE_SIZE + SQUARE_SIZE,
                                 i * SQUARE_SIZE + SQUARE_SIZE, outline=sTheme['Grid'])
    c.create_rectangle(-SQUARE_SIZE,22*SQUARE_SIZE,47*SQUARE_SIZE+SQUARE_SIZE,25*SQUARE_SIZE+SQUARE_SIZE, fill=sTheme['BG'],outline=sTheme['Shadow'])
#Управление кораблями
def FlotMove(event, vector):
    global FlotOrient
    sf=c.coords(SelectedFlot)
    sfc=[]
    for i in range(len(sf)):
        sfc.append(int((sf[i]-PaddingStart)//SQUARE_SIZE) if i<2 else int((sf[i]-PaddingStart)//SQUARE_SIZE)-1)
    upl=PaddingStart
    downl=PaddingStart+GRID_SIZE*SQUARE_SIZE-SQUARE_SIZE
    xm=vector[0]*SQUARE_SIZE
    ym=vector[1]*SQUARE_SIZE
    Start=0
    if vectors.index(vector)==0:
        if ([sfc[2],sfc[3]+1] in amy_coords) and ([sfc[0],sfc[1]+1] in amy_coords):
            pass
        else:
            Start=1
            cccc=[]
            for iii in range(sfc[3]+1,GRID_SIZE):
                if ([sfc[2],sfc[3]+iii] in amy_coords) and (([sfc[0],sfc[1]+iii] in amy_coords) if FlotOrient==0 else 1==1):
                    cccc.append(iii)
                    print(cccc)
            if len(cccc)>=sfc[3]-sfc[1]+1:
                ym=SQUARE_SIZE*(cccc[sfc[3]-sfc[1]])
                Start=0
        if (Start==0):
            c.move(SelectedFlot, xm, ym)
    elif vectors.index(vector)==1:
        if ([sfc[2],sfc[3]-1] in amy_coords) and ([sfc[0],sfc[1]-1] in amy_coords):
            pass
        else:
            Start=1
            cccc=[]
            for iii in range(sfc[1],0,-1):
                if ([sfc[2],sfc[3]-iii] in amy_coords) and (([sfc[0],sfc[1]-iii] in amy_coords) if FlotOrient==0 else 1==1):
                    cccc.append(iii)
            if len(cccc)>=sfc[3]-sfc[1]+1:
                ym=-SQUARE_SIZE*(cccc[-(sfc[3]-sfc[1]+1)])
                Start=0
        if (Start==0):
            c.move(SelectedFlot, xm, ym)
    elif vectors.index(vector)==2:
        if ([sfc[2]-1,sfc[3]] in amy_coords) and ([sfc[0]-1,sfc[1]] in amy_coords):
            pass
        else:
            Start=1
            cccc=[]
            for iii in range(sfc[0],0,-1):
                if ([sfc[0]-iii,sfc[1]] in amy_coords) and (([sfc[2]-iii,sfc[3]] in amy_coords) if FlotOrient==1 else 1==1):
                    cccc.append(iii)
            if len(cccc)>=sfc[2]-sfc[0]+1:
                xm=-SQUARE_SIZE*(cccc[-(sfc[2]-sfc[0]+1)])
                Start=0
        if (Start==0):
            c.move(SelectedFlot, xm, ym)
    elif vectors.index(vector)==3:
        if ([sfc[2]+1,sfc[3]] in amy_coords) and ([sfc[0]+1,sfc[1]] in amy_coords):
            pass
        else:
            Start=1
            cccc=[]
            for iii in range(sfc[2]+1,GRID_SIZE):
                print([sfc[2]+iii,sfc[3]],[sfc[0]+iii,sfc[1]])
                if ([sfc[2]+iii,sfc[3]] in amy_coords) and (([sfc[0]+iii,sfc[1]] in amy_coords) if FlotOrient==1 else 1==1):
                    cccc.append(iii)
            if len(cccc)>=sfc[2]-sfc[0]+1:
                xm=SQUARE_SIZE*(cccc[(sfc[2]-sfc[0])])
                Start=0
        if (Start==0):
            c.move(SelectedFlot, xm, ym)
#Завершение управления
def FlotRotate(event,i):
    global FlotOrient
    i-=1
    sf=c.coords(SelectedFlot)
    if sf[1]>=PaddingStart+(GRID_SIZE*SQUARE_SIZE)-(i*SQUARE_SIZE):
        if ([(sf[0]-PaddingStart)//SQUARE_SIZE,(sf[1]-PaddingStart)//SQUARE_SIZE-(i-(GRID_SIZE-1-(sf[1]-PaddingStart)//SQUARE_SIZE))] in amy_coords):
            c.move(SelectedFlot,0,-SQUARE_SIZE*(i-(GRID_SIZE-1-(sf[1]-PaddingStart)//SQUARE_SIZE)))
    sf=c.coords(SelectedFlot)
    if (sf[0]>=PaddingStart+(GRID_SIZE*SQUARE_SIZE)-(i*SQUARE_SIZE)):
        if ([(sf[0]-PaddingStart)//SQUARE_SIZE-(i-(GRID_SIZE-1-(sf[0]-PaddingStart)//SQUARE_SIZE)),(sf[1]-PaddingStart)//SQUARE_SIZE] in amy_coords):
            c.move(SelectedFlot,-SQUARE_SIZE*(i-(GRID_SIZE-1-(sf[0]-PaddingStart)//SQUARE_SIZE)),0)
    sf=c.coords(SelectedFlot)
    if FlotOrient==0:
        if [int((sf[2]-PaddingStart)//SQUARE_SIZE)-i-1,int((sf[3]-PaddingStart)//SQUARE_SIZE)+i-1] in amy_coords:
            FlotOrient=1
            c.coords(SelectedFlot,sf[0],sf[1],sf[2]-i*SQUARE_SIZE,sf[3]+i*SQUARE_SIZE)
    else:
        if [int((sf[2]-PaddingStart)//SQUARE_SIZE)+i-1,int((sf[3]-PaddingStart)//SQUARE_SIZE)-i-1] in amy_coords:
            FlotOrient=0
            c.coords(SelectedFlot,sf[0],sf[1],sf[2]+i*SQUARE_SIZE,sf[3]-i*SQUARE_SIZE)
def FlotMoveDone(event,i):
    global SelectedFlot,FlotOrient
    sf=c.coords(SelectedFlot)
    c.delete(SelectedFlot)
    SelectedFlot='ff'+str(int((sf[2 if FlotOrient==0 else 3]-sf[0 if FlotOrient==0 else 1])//SQUARE_SIZE))+str(int(sf[0]//SQUARE_SIZE-3))+str(int(sf[1]//SQUARE_SIZE-3))
    c.create_rectangle(sf[0],sf[1],sf[2],sf[3],width=2, outline=sTheme['Ship'],tag=SelectedFlot)
    ship=FlotCheck([[int(SelectedFlot[-2]),int(SelectedFlot[-1])],
                    [int(SelectedFlot[-2])+(int(SelectedFlot[-3])-1 if FlotOrient==0 else 0),int(SelectedFlot[-1])+(int(SelectedFlot[-3])-1 if FlotOrient==1 else 0)]],my_flot_coords)[0:-1]
    x1=ship[0][0]-1
    x2=ship[-1][0]+1
    y1=ship[0][1]-1
    y2=ship[-1][1]+1
    while x1!=(x2+1):
        while y1!=(y2+1):
            if [x1,y1] in amy_coords:
                amy_coords.remove([x1,y1])
            y1+=1
        x1+=1
        y1=ship[0][1]-1
    ShipCount[i-1]-=1
    MyLSC[i-1]+=1
    c.itemconfig('fc'+str(i), text=('x',ShipCount[i-1]))
    c.delete('arrow0','arrow1','arrow2','arrow3','ok','arrowok','controltext','rotate','f'+str(i),'fc'+str(i))
    SelectedFlot=0
    PlacementProgress()
    if IN_GAME:
        TabloWiners()
    else:
        TabloPMType()
        FlotBar()
#Панель управления флотом
def FlotPAD(flot_id):
    c.delete('gametitle','score','tttt','autopm','autopmtxt')
    for i in range(1,5):
        if int(SelectedFlot[2])!=i:
            c.delete('f'+str(i),'fc'+str(i))
        else:
            xx1,yy1,xx2,yy2 = c.coords('f'+str(i))
            c.coords('f'+str(i),47/2*SQUARE_SIZE-(xx2-xx1)/2,yy1-SQUARE_SIZE/2,47/2*SQUARE_SIZE+(xx2-xx1)/2,yy2-SQUARE_SIZE/2)
            xx1,yy1 = c.coords('fc'+str(i))
            c.coords('fc'+str(i),47/2*SQUARE_SIZE,yy1+SQUARE_SIZE/1.5)
    c.create_polygon(points[0], fill=sTheme['MainBtn'], outline=sTheme['MainBtnShadow'],tag='arrow0')
    c.tag_bind('arrow0', '<Button-1>', lambda event: FlotMove(event,vectors[0]))

    c.create_polygon(points[1], fill=sTheme['MainBtn'], outline=sTheme['MainBtnShadow'],tag='arrow1')
    c.tag_bind('arrow1', '<Button-1>', lambda event: FlotMove(event,vectors[1]))

    c.create_polygon(points[2], fill=sTheme['MainBtn'], outline=sTheme['MainBtnShadow'],tag='arrow2')
    c.tag_bind('arrow2', '<Button-1>', lambda event: FlotMove(event,vectors[2]))

    c.create_polygon(points[3], fill=sTheme['MainBtn'], outline=sTheme['MainBtnShadow'],tag='arrow3')
    c.tag_bind('arrow3', '<Button-1>', lambda event: FlotMove(event,vectors[3]))

    c.create_rectangle(22.5*SQUARE_SIZE,8*SQUARE_SIZE,24.5*SQUARE_SIZE,10*SQUARE_SIZE, fill=sTheme['MainBtn'], outline=sTheme['MainBtnShadow'],tag='arrowok')
    c.create_rectangle(20*SQUARE_SIZE,14*SQUARE_SIZE,27*SQUARE_SIZE,15.5*SQUARE_SIZE, fill=sTheme['MainBtn'], outline=sTheme['MainBtnShadow'],tag='rotate')
    c.create_text(23.5 * SQUARE_SIZE,14.75 * SQUARE_SIZE, text='ПОВЕРНУТЬ', font=fonts['MediumBM'], fill=sTheme['BtnText'],tag='rotate')
    c.tag_bind('arrowok', '<Button-1>', lambda event: FlotMoveDone(event,flot_id))
    c.create_text(23.5 * SQUARE_SIZE,8 * SQUARE_SIZE/2, text='УПРАВЛЕНИЕ', font=fonts['LargeBM'], fill=sTheme['MainText'],tag='controltext')
    c.create_text(23.5 * SQUARE_SIZE,9 * SQUARE_SIZE, text='OK', font=fonts['Medium'], fill=sTheme['BtnText'],tag='ok')
    c.tag_bind('ok', '<Button-1>', lambda event: FlotMoveDone(event,flot_id))
    c.tag_bind('rotate', '<Button-1>', lambda event: FlotRotate(event,flot_id))
#Табло с информацией
def TabloWiners():
    c.delete('gametitle','score','tttt')
    c.create_text(47 * SQUARE_SIZE / 2,8 * SQUARE_SIZE/2, text='МОРСКОЙ БОЙ', font=fonts['vvLargeBM'], fill=sTheme['MainText'],tag='gametitle')
    c.create_text(47 * SQUARE_SIZE / 2,14 * SQUARE_SIZE/2, text=str(cWins[0])+'    '+str(cWins[1]), font=fonts['vvLargeBM'], fill=sTheme['MainText'],tag='score')
    c.create_text(47 * SQUARE_SIZE / 2,13.5 * SQUARE_SIZE/2, text=':', font=fonts['vLargeBM'], fill=sTheme['MainText'],tag='tttt')
def TabloPMType():
    c.delete('gametitle','score','tttt')
    c.create_text(47 * SQUARE_SIZE / 2,7.3 * SQUARE_SIZE/2, text='Расставьте корабли', font=fonts['vLargeBM'], fill=sTheme['MainText'],tag='gametitle')
    c.create_text(47 * SQUARE_SIZE / 2,18 * SQUARE_SIZE/2, text='  Для этого нажмите на любой корабль\n'
                                                        +' '*15+'(они на панели снизу).\n'
                                                        +'Затем с помощью появившихся стрелок\n'
                                                        +'        разместите корабль в лучшем,\n'
                                                        +'            на ваш взгляд, положении.\n\n'
                                                        +' Или выберите случайную расстановку.', font=fonts['Medium'], fill=sTheme['MainText'],tag='score')
def ChangeTheme(event):
    global newTheme,Theme
    t=[]
    ids = c.find_withtag(CURRENT)[0]
    x = int(c.coords(ids)[0]//SQUARE_SIZE-sPadding)
    for tt in Theme:
        t.append(tt)
    if Theme[t[x//2]]!=newTheme:
        for tt in t:
            if Theme[tt]==newTheme:
                c.coords('theme'+tt,c.coords('theme'+tt)[0]+3,c.coords('theme'+tt)[1]+3,c.coords('theme'+tt)[2]-3,c.coords('theme'+tt)[3]-3)
                break
        c.coords(ids,c.coords(ids)[0]-3,c.coords(ids)[1]-3,c.coords(ids)[2]+3,c.coords(ids)[3]+3)
        newTheme=Theme[t[x//2]]
def ChangeSize(event,op):
    global SSIZE
    if op=='minus':
        SSIZE-=1
    elif op=='plus':
        SSIZE+=1
    c.itemconfig('SizeTxt',text=SSIZE)
def SetExpand(event):
    global SetType
    SetType=1
    c.delete('setting')
    SettingDelete()
    SettingBar()
def SetClose(event):
    global SetType
    SetType=0
    c.delete('setting')
    SettingDelete()
    SettingBar()
def SettingBar():
    if SetType==0:
        x1=sPadding
        c.create_rectangle(0,SQUARE_SIZE//2,SQUARE_SIZE*x1,SQUARE_SIZE*1.5,fill=sTheme['MainBtn'],outline=sTheme['MainBtnShadow'],tag='setting')
        c.create_text(SQUARE_SIZE*(x1-4),SQUARE_SIZE,text='ПАРАМЕТРЫ',font=fonts['SmallBM'],fill=sTheme['BtnText'],tag='setting')
        c.tag_bind('setting','<Button-1>',SetExpand)
    else:
        x1=sPadding
        c.create_text(SQUARE_SIZE*(x1-4),SQUARE_SIZE,text='ВЫБЕРИТЕ ТЕМУ:',font=fonts['SmallBM'],fill=sTheme['MainText'],tag='chstheme')
        for t in Theme:
            c.create_rectangle(SQUARE_SIZE*x1-(3 if Theme[t]==newTheme else 0),SQUARE_SIZE//2-(3 if Theme[t]==newTheme else 0),SQUARE_SIZE*(x1+1)+(3 if Theme[t]==newTheme else 0),SQUARE_SIZE*1.5+(3 if Theme[t]==newTheme else 0),fill=Theme[t]['Main'],outline=Theme[t]['Shadow'],tag='theme'+t)
            c.tag_bind('theme'+t,'<Button-1>',lambda event: ChangeTheme(event))
            x1+=2
        x1+=3
        c.create_text(SQUARE_SIZE*(x1-1),SQUARE_SIZE,text='РАЗМЕР:',fill=sTheme['MainText'],font=fonts['SmallBM'],tag='Size')
        c.create_rectangle(SQUARE_SIZE*(x1+1),SQUARE_SIZE//2,SQUARE_SIZE*(x1+2),SQUARE_SIZE//2+SQUARE_SIZE,fill=sTheme['SimpleBtn'],tag='Sminus')
        c.create_text(SQUARE_SIZE*(x1+1)+SQUARE_SIZE//2,SQUARE_SIZE,text='-',font=fonts['MediumBM'],fill=sTheme['BtnText'],tag='Sminus')
        c.create_rectangle(SQUARE_SIZE*(x1+2),SQUARE_SIZE//4,SQUARE_SIZE*(x1+4),(SQUARE_SIZE//4)*3+SQUARE_SIZE,fill=sTheme['SimpleBtn'],tag='Size')
        c.create_text(SQUARE_SIZE*(x1+3),SQUARE_SIZE,text=SSIZE,font=fonts['MediumBM'],fill=sTheme['BtnText'],tag='SizeTxt')
        c.create_rectangle(SQUARE_SIZE*(x1+4),SQUARE_SIZE//2,SQUARE_SIZE*(x1+5),SQUARE_SIZE//2+SQUARE_SIZE,fill=sTheme['SimpleBtn'],tag='Splus')
        c.create_text(SQUARE_SIZE*(x1+4)+SQUARE_SIZE//2,SQUARE_SIZE,text='+',font=fonts['MediumBM'],fill=sTheme['BtnText'],tag='Splus')
        c.tag_bind('Sminus','<Button-1>',lambda event: ChangeSize(event,'minus'))
        c.tag_bind('Splus','<Button-1>',lambda event: ChangeSize(event,'plus'))
        x1+=1
        c.create_rectangle(SQUARE_SIZE*(x1+sPadding*0.55),SQUARE_SIZE//2,SQUARE_SIZE*(x1+sPadding*1.45),SQUARE_SIZE*1.5,fill=sTheme['MainBtn'],outline=sTheme['MainBtnShadow'],tag='setset')
        c.create_text(SQUARE_SIZE*(x1+sPadding),SQUARE_SIZE,text='ПЕРЕЗАПУСТИТЬ',fill=sTheme['BtnText'],font=fonts['SmallBM'],tag='setset')
        c.tag_bind('setset','<Button-1>',Restart)
        x1+=sPadding-2
        c.create_rectangle(SQUARE_SIZE*(x1+sPadding*0.75),SQUARE_SIZE//2,SQUARE_SIZE*(x1+sPadding*1.25),SQUARE_SIZE*1.5,fill=sTheme['MainBtn'],outline=sTheme['MainBtnShadow'],tag='setcloser')
        c.create_text(SQUARE_SIZE*(x1+sPadding),SQUARE_SIZE,text='СВЕРНУТЬ',fill=sTheme['BtnText'],font=fonts['SmallBM'],tag='setcloser')
        c.tag_bind('setcloser','<Button-1>',SetClose)
def SettingDelete():
    c.delete('chstheme','Sminus','Splus','Size','SizeTxt','setcloser','setset')
    for t in Theme:
        c.delete('theme'+t)
    c.update()
FirstStart()
root.mainloop()