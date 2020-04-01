# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 09:20:46 2020

@author: 郑乔木
"""

DNA = ['A','T','G','C','T','T','C','A','G','A','A','A','G','G','T','C','T','T','A','C','G']
nucleotides = {}
nucleotides['A'] = DNA.count('A') 
nucleotides['T'] = DNA.count('T') 
nucleotides['C'] = DNA.count('C') 
nucleotides['G'] = DNA.count('G') 
print(nucleotides)

import matplotlib.pyplot as pyplot
labels = 'A','T','C','G'
sizes = [nucleotides['A'],nucleotides['T'],nucleotides['C'],nucleotides['G']]
pyplot.pie(sizes,labels=labels,autopct='%1.1f%%',labeldistance=1.1,startangle=90,pctdistance = 0.6,)
pyplot.title('pie of the four DNA nucleotides')
pyplot.axis('equal')
pyplot.show()