# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 15:36:18 2020

@author: 郑乔木
"""
import re

filename=input("Please input a  filename as the new fasta file:")
file=open(filename,'w')
ofile=open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')
nfile=open('mito_gene.fa')
line=ofile.readline()

count=0
file.write('$ head -10 rc.fa \n')

def rc(seq):
    result=""
    for b in seq[:]:
        if b=="A":
            result=result+"T"
        elif b=="T":
            result=result+"A"
        elif b=="C":
            result=result+"G"
        elif b=="G":
            result=result+"C"
    return result

while True:
    mg=nfile.readline()
    name=re.findall(r'Name:(.+)                  L',mg)
    length=re.findall('Length:(.+)\n',mg)
    out='>'+name[0]+'         '+length[0]+'\n'
    file.write(out)
    
    while True:
            line=ofile.readline()
            if line.startswith('>') or not line:
                out='\n'
                file.write(out)
                break
            file.write(rc(line))
       
    if not line:
        break