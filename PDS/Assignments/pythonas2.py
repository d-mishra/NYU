# -*- coding: utf-8 -*-
"""
@author: DM
"""

import sys
from matplotlib import cm
import matplotlib.pyplot as plt
import pprint 

# function for cycling  colors across the bar charts
colors = ['red', 'blue', 'green']
i = -1
def getCycledColor():
    global i, colors
    if i < len(colors):
        i = i + 1
        return colors[i]
    else:
        i = -1

p = sys.stdin.read()

p = p.splitlines()

b = [""]

for line in p:
    
    t = line.strip().split("\t")
    
    #make the list the correct size for all columns
    while len(b)<len(t):
        b.extend([""])
            
    #add row data to nestd lists
    ct=0 
    while ct < len(t):
        if len(b[ct]) == 0:
            b[ct] = [int(t[ct])]
        else:
            b[ct].append(int(t[ct]))
        ct = ct + 1

#pprint.pprint(b)
    
#plot each column    
for yplot in b:
    plt.plot(yplot)

plt.show()
plt.cla()


#plot bar chart    



for yplot in b:    
    plt.bar( range(0, len(yplot)), yplot,facecolor=getCycledColor(), width=0.5)
plt.show()
plt.cla()


pprint.pprint(b)
#sys.stdout.write(b[0])