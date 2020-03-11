# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 22:46:00 2020

@author: 郑乔木
"""



num = 6666
#choose largest power of 2
#add it to result
#minus it
#choose largest power of 2 for the reminder, add, an so on
#stop when reminder is 0

result = str(6666)+ " is"
while num != 0:

    while num == 6666:
        for i in range(0,13):
            if num >= 2**i and num < 2**(i+1):
                result = result + " 2**" + str(i)
                num = num - 2**i

    for i in range(0,13):
        if num >= 2**i and num < 2**(i+1):
            result = result + " + 2**" + str(i)
            num = num - 2**i


print(result)





