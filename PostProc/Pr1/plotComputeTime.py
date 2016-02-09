#!/usr/bin/env python
import os
import sys
import numpy as np
import matplotlib.pyplot as plt
import csv

dataFile = './ComputeTime.csv'
nList = []
errList = []
with open(dataFile, 'rb') as csvfile:
   reader = csv.DictReader(csvfile)
   for row in reader:
      nList.append(int(row['n']))
      errList.append(float(row['compute time']))

MinX = 0
MaxX = 55
MinY = 0.9*min(errList)
MaxY = 1.05*max(errList)

#p = plt.plot(nList,errList, 'k-', label='label')
p = plt.plot(nList,errList, 'k-o', label=None)

plt.setp(p, linewidth='2.0')
plt.axis([MinX,MaxX, MinY, MaxY])
plt.xscale('linear')
plt.yscale('linear')
plt.xlabel('Grid size', fontsize=22)
plt.ylabel('Calculation time [sec]', fontsize=22)

plt.grid(True)
ax = plt.gca()
xlabels = plt.getp(ax, 'xticklabels')
ylabels = plt.getp(ax, 'yticklabels')
plt.setp(xlabels, fontsize=18)
plt.setp(ylabels, fontsize=18)
plt.legend(
          loc='lower left',
          borderpad=0.25,
          handletextpad=0.25,
          borderaxespad=0.25,
          labelspacing=0.0,
          handlelength=2.0,
          numpoints=1)
#legendText = plt.gca().get_legend().get_texts()
#plt.setp(legendText, fontsize=18)
#legend = plt.gca().get_legend()
#legend.draw_frame(False)
fig = plt.gcf()
fig.set_size_inches(8,5)
plt.tight_layout()
pltFile = 'computeTime.png'
plt.savefig(pltFile, format='png')
plt.close()

print "%s DONE!!" % (pltFile)
