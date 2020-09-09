# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 16:52:57 2020

@author: Nishant
"""

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    if n<1 or n==0 or n>100:
        exit
    if (n%2)!=0:
        print('Weird')
    else:
        if n>=2 and n<=5:
            print('Not Weird')    
        elif n>=6 and n<=20:
            print('Weird')
        elif n>20:
            print('Not Weird')  
            
