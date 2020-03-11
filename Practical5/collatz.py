# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 22:14:55 2020

@author: 郑乔木
"""

num=123
#dividing by 2 (if n is even) or multiplying by 3 and adding 1 (if n is one)
print(num)
while num != 1:
#stop at 1
    if num % 2 == 0:
        num /= 2
        print(num)
    else:
        num = num * 3 + 1
        print(num)
#generate next number and print