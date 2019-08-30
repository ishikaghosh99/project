# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 19:09:09 2019

@author: user
"""
#0/1 knapscak using dynamic programing
#main code
from sorting import Sorting1
from knapsackalgo import knapSack


        
w=[]
p=[]
w.append(0);
p.append(0);
n=int(input("Please Enter the Total Number of Quantity : "))
for i in range(1,n+1):
    value = int(input("Please enter the %d Element of Weight array: " %i))
    w.append(value)
print("The weight array is as :",w)
for i in range(1,n+1):
    value1 = int(input("Please enter the %d Element of Profit array: " %i))
    p.append(value1)
print("The profit array is as :",p)
capacity=int(input("Please Enter the Total Capacity : "))
print("The 0/1 Knapsack table is given as followed: ")
print()
Sorting1(w,n+1,p)
ans=knapSack(capacity,w,p,n+1)
print()
print("The total profit obtained is:",ans)


