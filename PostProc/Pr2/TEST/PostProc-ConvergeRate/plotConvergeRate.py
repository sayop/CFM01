#!/usr/bin/env python
import os
import sys
import numpy as np
import matplotlib.pyplot as plt
import csv


# Read Jacobian converge rate
dataFile = '../40x40/Jacobi-alpha1.0/convergenceRate.csv'
iterList1 = []
converge1 = []
with open(dataFile, 'rb') as csvfile:
   reader = csv.DictReader(csvfile)
   for row in reader:
      iterList1.append(float(row['iter']))
      converge1.append(float(row['converge']))


# Read G-S converge rate
dataFile = '../40x40/GS-alpha1.0/convergenceRate.csv'
iterList2 = []
converge2 = []
with open(dataFile, 'rb') as csvfile:
   reader = csv.DictReader(csvfile)
   for row in reader:
      iterList2.append(float(row['iter']))
      converge2.append(float(row['converge']))


# Read SOR1.2 converge rate
dataFile = '../40x40/GS-alpha1.2/convergenceRate.csv'
iterList3 = []
converge3 = []
with open(dataFile, 'rb') as csvfile:
   reader = csv.DictReader(csvfile)
   for row in reader:
      iterList3.append(float(row['iter']))
      converge3.append(float(row['converge']))


# Read G-S converge rate
dataFile = '../40x40/GS-alpha1.5/convergenceRate.csv'
iterList4 = []
converge4 = []
with open(dataFile, 'rb') as csvfile:
   reader = csv.DictReader(csvfile)
   for row in reader:
      iterList4.append(float(row['iter']))
      converge4.append(float(row['converge']))

MinX = 0
MaxX = 2200
MinY = 0.001
MaxY = 1.0

p = plt.plot(iterList1,converge1, 'k-', label='Jacobi')
plt.setp(p, linewidth='3.0')
p = plt.plot(iterList2,converge2, 'r--', label='Gauss-Seidel')
plt.setp(p, linewidth='3.0')
p = plt.plot(iterList3,converge3, 'c--', label='SOR, alpha=1.2')
plt.setp(p, linewidth='3.0')
p = plt.plot(iterList4,converge4, 'b--', label='SOR, alpha=1.5')
plt.setp(p, linewidth='3.0')


plt.axis([MinX,MaxX, MinY, MaxY])
plt.xscale('linear')
plt.yscale('log')
plt.xlabel('Number of iterations', fontsize=22)
plt.ylabel('Normalized residual', fontsize=22)

plt.grid(True)
ax = plt.gca()
xlabels = plt.getp(ax, 'xticklabels')
ylabels = plt.getp(ax, 'yticklabels')
plt.setp(xlabels, fontsize=18)
plt.setp(ylabels, fontsize=18)
plt.legend(
          loc='upper right',
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
pltFile = 'convergeRate.png'
plt.savefig(pltFile, format='png')
plt.close()

print "%s DONE!!" % (pltFile)
