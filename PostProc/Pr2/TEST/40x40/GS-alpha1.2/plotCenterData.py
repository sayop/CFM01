#!/usr/bin/env python
import os
import sys
import numpy as np
import matplotlib.pyplot as plt
import csv

dataFile = './dataOut.csv'
xList = []
numericalTList = []
exactTList = []
with open(dataFile, 'rb') as csvfile:
   reader = csv.DictReader(csvfile)
   for row in reader:
      xList.append(float(row['x']))
      numericalTList.append(float(row['solution']))
      exactTList.append(float(row['exactSolution']))

MinX = 0
MaxX = 1
MinY = 0.0
MaxY = 0.08

p = plt.plot(xList,numericalTList, 'k-', label='Numerical solution')
plt.setp(p, linewidth='3.0')
p = plt.plot(xList,exactTList, 'r--', label='Exact solution')
plt.setp(p, linewidth='3.0')

plt.axis([MinX,MaxX, MinY, MaxY])
plt.xscale('linear')
plt.yscale('linear')
plt.xlabel('Position in x-direction', fontsize=22)
plt.ylabel('T', fontsize=22)
plt.text(0.25, 0.02, 'Grid resolution = 40x40', fontsize=22 )

plt.grid(True)
ax = plt.gca()
xlabels = plt.getp(ax, 'xticklabels')
ylabels = plt.getp(ax, 'yticklabels')
plt.setp(xlabels, fontsize=18)
plt.setp(ylabels, fontsize=18)
plt.legend(
          loc='lower center',
          borderpad=0.25,
          handletextpad=0.25,
          borderaxespad=0.25,
          labelspacing=0.0,
          handlelength=2.0,
          numpoints=1)
legendText = plt.gca().get_legend().get_texts()
plt.setp(legendText, fontsize=18)
legend = plt.gca().get_legend()
legend.draw_frame(False)
fig = plt.gcf()
fig.set_size_inches(8,5)
plt.tight_layout()
pltFile = 'solutions.png'
plt.savefig(pltFile, format='png')
plt.close()

print "%s DONE!!" % (pltFile)
