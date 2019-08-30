# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 15:22:57 2019

@author: user
"""
#application 1
#Preparation for exam at last movement that is one day before the exam
from sorting import Sorting1
def knapSack(capacity, wt, pt, n): 
    K = [[0 for x in range(capacity+1)] for x in range(n)] 
  
    # Build table K[][] in bottom up manner 
    for i in range(n): 
        for w in range(capacity+1): 
            if i==0 or w==0: 
                K[i][w] = 0
            elif wt[i] <= w: 
                K[i][w] = max(pt[i] + K[i-1][w-wt[i]],  K[i-1][w]) 
            else: 
                K[i][w] = K[i-1][w]
    return K[n-1][capacity]

w=[]
p=[]
w.append(0);
p.append(0);
n=int(input("Please Enter the Total Number of Chapters : "))
for i in range(1,n+1):
    value = int(input("Please enter the total number of pages for the %d chapter: " %i))
    w.append(value)
    value1 = int(input("Please enter the total weightage for %d chapter: " %i))
    p.append(value1)
print("The number of page array is as :",w)
print("The Weightage array is as :",p)
capacity=int(input("Please Enter the Total Capacity of the student: "))
Sorting1(w,n+1,p)
ans=knapSack(capacity,w,p,n+1)
print("The total profit obtained is:",ans)