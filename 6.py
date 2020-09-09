# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 16:55:22 2020

@author: Nishant
"""

if __name__ == '__main__':
    n = int(input())

if n<1 or n>150:
    exit


for i in range(1,n+1):
    print(i, end ="")
    i+=1
