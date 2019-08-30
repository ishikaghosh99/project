# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 14:27:08 2019

@author: user
"""

def Sorting1(w,n,p):
    for i in range(n -1):
        for j in range(n - i - 1):
            if(w[j] > w[j + 1]):
                temp = w[j]
                w[j] = w[j + 1]
                w[j + 1] = temp
                temp1 = p[j]
                p[j] = p[j + 1]
                p[j + 1] = temp1
            
