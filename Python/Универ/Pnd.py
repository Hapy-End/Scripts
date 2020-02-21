import pandas as pd

dtf = pd.read_csv('train.csv',index_col='PassengerId')
print('1)',(dtf['Sex']=='female').sum(),(dtf['Sex']=='male').sum())
print('2)',round(dtf['Survived'].mean()*100,2))
print('3)',round((dtf['Pclass']==1).mean()*100,2))
print('4)',dtf['Age'].mean(),dtf['Age'].median())