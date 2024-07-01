# -*- coding: utf-8 -*-
"""
Created on Sat May 18 07:39:30 2024

@author: cs
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


df= pd.read_csv("D:\Dipankar sir\Python\\New Year Sales Data.csv",encoding= 'unicode_escape')

df.shape

df.info()

df.drop(['Status','unnamed1'],axis=1, inplace=True)

df.info()

pd.isnull(df).sum()

df.dropna(inplace=True)
pd.isnull(df).sum()

df['Amount']= df['Amount'].astype('int')
df['Amount'].dtypes

df.rename(columns= {'Product_Category':'Product_Type'})

ax= sns.countplot(x='Gender',data=df)
for bars in ax.containers:ax.bar_label(bars)

sales_gen = df.groupby (['Gender'], as_index =False)['Amount'].sum().sort_values(by='Amount',ascending=False)
sns.barplot(x ='Gender',y ='Amount',data= sales_gen)

# We can see most of the buyers are females and even the purchesing power of females are greater than male #

sales_state = df.groupby(['State'], as_index=False)['Orders'].sum().sort_values(by='Orders',ascending=False).head(10)
sns.barplot(data= sales_state, x ='State',y ='Orders')

sales_state = df.groupby(['State'], as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False).head(10)
sns.barplot(data= sales_state, x ='State',y ='Amount')

# We can sen that most of the orders and sales amount are from uttarpradesh maharastra and karnataka respectively.

sales_state = df.groupby(['Occupation'], as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False).head(10)
sns.barplot(data= sales_state, x ='Occupation',y ='Amount')

#From above graphs we can see that most of the buyers are working in IT, Healthcare and Aviation sector.

sales_state = df.groupby(['Product_Category'], as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False).head(10)
sns.barplot(data= sales_state, x ='Product_Category',y ='Amount')

### we can see that most of the sold products are from Food, Clothing and Electronics category.

