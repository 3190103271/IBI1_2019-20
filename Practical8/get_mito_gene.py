# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 14:02:24 2020

@author: 郑乔木
"""

import re

ofile=open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')
nfile=open('mito_gene.fa','w')

line=ofile.readline()
count=0

while True:
    if line.startswith('>'):#identify the genes
        write=re.findall(r'gene:(.+) gene_biotype',line)
        name=write[0]
        out='Name:'+name#write the name
        nfile.write(out)
        out='                  '#insert space
        nfile.write(out)
        while True:
            line=ofile.readline()

            if line.startswith('>') or not line:
                out='Length:'+str(count)+'\n'
                nfile.write(out)#write the length when finishing counting
                count=0
                break
            count+=len(line)-1#count the length
    if not line:
        break

ofile.close()
nfile.close()

        
            
    