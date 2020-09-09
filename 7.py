# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 16:34:37 2020

@author: Nishant
"""
def print_full_name(a, b):
    if (len(a) or len(b))<=10:
        print('Hello '+ a +" "+ b + '! ' + 'You just delved into python.')
    else:
        exit
    

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)