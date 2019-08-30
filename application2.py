# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 16:30:58 2019

@author: user
"""
#application 2
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
n=int(input("Please Enter the Total number of product that the system needs to earn profit: "))
for i in range(1,n+1):
    value = int(input("Please enter the cost of %d product to buy : " %i))
    w.append(value)
print("The weight array is as :",w)
for i in range(1,n+1):
    value1 = int(input("Please enter the profit that the system must gain after buying %d product: " %i))
    p.append(value1)
print("The profit array is as :",p)
capacity=int(input("Please Enter the Total Capital of the company : "))
Sorting1(w,n+1,p)
ans=knapSack(capacity,w,p,n+1)
print("The total profit obtained  is:",ans)