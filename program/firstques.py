# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 14:09:06 2018

@author: user
"""
#Question1

para=input()
print(para)
sen=para.split(".")

sen[len(sen)]="UST Global specializes in Healthcare,Retail & Consumer Goods,Banking & Financial Telecom,Media & Technology,Insurance,Transportation & Logistics and Manufacturing & Utilities."
print("". join(sen))
print(para)



d={"vowels","upper","lower","special character"}
str_copy=""
str_copy=para
for i in para:
   
    if i in ("a","e","i","o","u"):
        d["vowels"]+=1
    elif i.isupper():
        d["upper"]+=1
    elif i.islower():
        d["lower"]+=1
    elif i in ("!","@","#","$","%","^","&","*","(",")","<",">","?","+","-","_","'","."):
              d["special character"]+=1
              print(d)
              str_copy=str_copy.replace(i,"")
              print("Updated paragraph is - \n",str_copy)
             
              
 #------------------------------------------------------------------------
 #Question2
 
import numpy as np
names=[]
marks=[]
sub1=[]
sub2=[]
sub3=[]
for i in range(10):
    names.append(input("Enter the names of students"))
    x,y,z=map(int,input("Enter marks for 3 subjects: ").split())
    sub1.append(x)
    sub2.append(y)
    sub3.append(z)
    print(names,sub1,sub2,sub3)
    
    mean_sub1=np.mean(sub1)
    mean_sub2=np.mean(sub2)
    mean_sub3=np.mean(sub3)
    
    med_sub1=np.median(sub1)
    med_sub2=np.median(sub2)
    med_sub3=np.median(sub3)
    d={}
    for i in range(3):
        d[names[i]]=(sub1[i]+sub2[i]+sub3[i])/3
        print(sub1.sort(),sub2.sort(),sub3.sort())
        
        for i in d:
            if d[i]>90:
                print("A+")
            elif d[i]>80:
                print("A")
            elif d[i]>70:
                print("B+")
            elif d[i]>50:
                print("C")
            elif d[i]<50:
                print("D")
                
  #-------------------------------------------------------------------
#Question4

d={"children":[],"youth":[],"middle age":[],"senior":[]}
for _ in range(5):
    name=input("Enter name")
    age=int(input("Enter age"))
    if age<15:
        d["children"].append(name)
    elif age>=15 and age<30:
        d["youth"].append(name)
    elif age>=30 and age<50:
        d["middle aged"].append(name)
    else:
        d["senior"].append(name)
        print(d)
        
#------------------------------------------------------------------------
#Question5

import numpy as np
from scripy import stats

x=[11.95,11.91,1186,11.94,12.00,11.93,12.00,11.94,12.10,11.95,11.99,11.94,11.89,12.01,11.99,11.94]        
temp=stats.itemfreq(x)
print("Frequency Distribution of this table is: \n",temp)
mean=np.mean(x)
median=np.median(x)
mode=stats.mode(x)
print("mean,median,mode are",mean(x),median(x),mode(x))   
                    
        
        
         
         
    
    
    
    
    
             
              
              
                                        
              
             
              