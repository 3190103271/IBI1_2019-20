# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 13:35:48 2020

@author: 郑乔木
"""


import os 
import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np
#import library

os.chdir("D:\IBI\practical\practical\IBI1_2019-20\Practical7") 
covid_data = pd.read_csv("full_data.csv")
#get the file

print(covid_data.iloc[:,0:15:3])

my_location=[]
for n in range (0,7996):
    location=covid_data.loc[n,"location"]
    my_location.append(location=="Afghanistan")#get the Boolean of data
    
x=covid_data.loc[my_location,"total_cases"]

print(x)


world=[]

for n in range (0,7996):
    location=covid_data.loc[n,"location"]
    world.append(location=="World")
    
    
nc=covid_data.loc[world,"new_cases"]
d=covid_data.loc[world,"date"]#get date
nd=covid_data.loc[world,"new_deaths"]

print(np.mean(nc))
print(np.median(nc))

plt.boxplot(nc)

#plt.plot(d, nc, 'b+')#blue and +
#plt.plot(d, nc, 'r+')#red and +
#plt.plot(d, nc, 'bo')#blue and dot

plt.plot(d, nc , 'b+', d, nd , 'r+')
plt.xticks(d.iloc[0:len(d):4],rotation=-90)
plt.ylabel('number')
plt.xlabel('date')
plt.title('new cases and new deaths worldwide')
plt.show()#show the first plot or it will be placed




sk=[]
k=[]
c=[]
for n in range (0,7996):#get data as before
    location=covid_data.loc[n,"location"]
    sk.append(location=="South Korea")
    k.append(location=="Kenya")
    c.append(location=="Colombia")
  
skd=covid_data.loc[sk,"date"]
skt=covid_data.loc[sk,"total_cases"]
kd=covid_data.loc[k,"date"]
kt=covid_data.loc[k,"total_cases"]
cd=covid_data.loc[c,"date"]
ct=covid_data.loc[c,"total_cases"]

plt.plot(skd, skt , 'b+', kd, kt , 'r+' , cd, ct ,'g+')
plt.xticks(skd.iloc[0:len(skd):4],rotation=-90)
plt.ylabel('number')
plt.xlabel('date')
plt.title('new cases and new deaths in South Korea, Kenya, Colombia')