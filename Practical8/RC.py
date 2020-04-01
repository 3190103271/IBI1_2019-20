# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 13:57:19 2020

@author: 郑乔木
"""

#first define a converting function
def compl_cvt(seq):
    compl_seq=""#create an empty string
    for b in seq[:]:
#judge each nucleotide base and convert it by adding them to the empty string one by one
        if b=="A":
            compl_seq="T"+compl_seq
        elif b=="T":
            compl_seq="A"+compl_seq
        elif b=="C":
            compl_seq="G"+compl_seq
        elif b=="G":
            compl_seq="C"+compl_seq
        else:#if the user mis-type the sqeuence, remind the user an undefined base
            print("undefined base","{}".format(b))
            break#jump out from the loop
    return compl_seq#return the complementary sequence
#test the function
#ask the user to input a DNA sequence
sequence = 'ATGCGACTACGATCGAGGGCCAT'
#use the function to convert
compl_sequence=compl_cvt(sequence)
#formattedly output the complementary sequence
print("The complementary sequence of the given DNA:\n{}".format(compl_sequence))        