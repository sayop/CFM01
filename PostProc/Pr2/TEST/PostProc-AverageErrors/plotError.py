#!/usr/bin/env python
import os
import sys
import numpy as np
import matplotlib.pyplot as plt
import csv

dataFile = './averageError.csv'
nList = []
errorJacobi = []
errorGS = []
errorSOR12 = []
errorSOR15 = []
with open(dataFile, 'rb') as csvfile:
   reader = csv.DictReader(csvfile)
   for row in reader:
      nList.append(float(row['n']))
      errorJacobi.append(float(row['Jacobi']))
      errorGS.append(float(row['GS']))
      errorSOR12.append(float(row['SOR1.2']))
      errorSOR15.append(float(row['SOR1.5']))

MinX = 5
MaxX = 85
MinY = 5e-07
MaxY = 5e-05

p = plt.plot(nList,errorJacobi, 'k-o', markersize=8, fillstyle='full', label='Jacobi')
plt.setp(p, linewidth='3.0')
p = plt.plot(nList,errorGS, 'r--d', markersize=8, fillstyle='full', label='Gauss-Seidel')
plt.setp(p, linewidth='3.0')
p = plt.plot(nList,errorSOR12, 'c--s', markersize=8, fillstyle='full', label='SOR, alpha=1.2')
plt.setp(p, linewidth='3.0')
p = plt.plot(nList,errorSOR15, 'b-->', markersize=8, fillstyle='full', label='SOR, alpha=1.5')
plt.setp(p, linewidth='3.0')

plt.axis([MinX,MaxX, MinY, MaxY])
plt.xscale('linear')
plt.yscale('log')
plt.xlabel('N', fontsize=22)
plt.ylabel('Averaged error', fontsize=22)

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
legendText = plt.gca().get_legend().get_texts()
plt.setp(legendText, fontsize=18)
legend = plt.gca().get_legend()
legend.draw_frame(False)
fig = plt.gcf()
fig.set_size_inches(8,5)
plt.tight_layout()
pltFile = 'errors.png'
plt.savefig(pltFile, format='png')
plt.close()

print "%s DONE!!" % (pltFile)
