import pandas as pd

#Load the Titanic dataset into one of the data structures (NumPy or Pandas)
df=pd.read_csv('train.csv')

#Display header rows and description of the loaded dataset
print(df.head())

#Remove unnecessary features(E.g. drop unwanted columns) from the dataset
#axis=1 >> columns axis 0 >> rows
#dropping cabin as 75% of values are NAN
df.drop(['PassengerId','Cabin'],axis=1,inplace=True)

#Identify which columns have nan values so as to replace them later
print([(column,df[column].isnull().sum()) if df[column].isnull().sum()>0 else 'None' for column in df.columns])

age_mean=df.groupby(['Sex'])['Age'].mean()

df.loc[df.Sex=='male', 'Age'].fillna(age_mean['male'])
df.loc[df.Sex=='female', 'Age'].fillna(age_mean['female'])
indices = ['male','female']
import  numpy
incdex=numpy.array(2)

import matplotlib.pyplot as py
py.figure()
py.subplot(2,2,1)
py.bar([1,2],df.groupby(['Sex'])['Survived'].sum())
py.xticks([1,2],['Female','Male'])

py.subplot(2,2,2)
df['Age'].hist(bins=100)
py.xlabel("Age")
py.ylabel("Count")

py.subplot(2,2,3)
py.bar([1,2,3],df.groupby(['Pclass'])['Survived'].sum())
py.xticks([1,2,3],[1,2,3])
py.xlabel("Pclass")
py.ylabel("Survived")
py.show()

