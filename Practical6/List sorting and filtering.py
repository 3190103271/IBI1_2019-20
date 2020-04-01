# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 09:53:18 2020

@author: 郑乔木
"""

gene_lengths=[9410,3944141,4442,105338,19149,76779,126550,36296,842,15981]
gene_lengths.sort()


del(gene_lengths[9])
del(gene_lengths[0])
print(gene_lengths)


import matplotlib.pyplot as plt
score = gene_lengths
plt.boxplot(score,
            vert=True,
            whis=1.5,
            patch_artist=True,
            meanline=True,showmeans=True,
            showbox=True,
            showcaps=True,
            showfliers=True,
            notch=False
            )
plt.show()

