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
    if line.startswith('>'):
        write=re.findall(r'gene:(.+) gene_biotype',line)
        name=write[0]
        out='Name:'+name
        nfile.write(out)
        out='                  '
        nfile.write(out)
        while True:
            line=ofile.readline()

            if line.startswith('>') or not line:
                out='Length:'+str(count)+'\n'
                nfile.write(out)
                count=0
                break
            count+=len(line)-1
    if not line:
        break

ofile.close()
nfile.close()

        
            
    