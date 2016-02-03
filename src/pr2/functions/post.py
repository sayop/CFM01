import numpy as np
import matplotlib.pyplot as plt
import csv

def plotContour(x,y,phi,pltFile):
   xi, yi = np.meshgrid(x, y)
   zi = phi

   plt.imshow(zi, vmin=zi.min(), vmax=0.075, origin='lower', extent=[x.min(), x.max(), y.min(), y.max()])
   plt.colorbar()

   plt.xscale('linear')
   plt.yscale('linear')
   plt.xlabel('x', fontsize=18)
   plt.ylabel('y', fontsize=18)
   plt.grid(True)
   ax = plt.gca()
   xlabels = plt.getp(ax, 'xticklabels')
   ylabels = plt.getp(ax, 'yticklabels')
   plt.setp(xlabels, fontsize=15)
   plt.setp(ylabels, fontsize=15)

   fig = plt.gcf()
   fig.set_size_inches(6,5)
   plt.tight_layout()
   plt.savefig(pltFile, format='png')
   plt.close()

   print "%s DONE!!" % (pltFile)
   plt.show()

def writeCSV(x,y,phi,exact,yLoc):
   print '# Writing a csv file to store line data in x-direction'
   csvFile = 'dataOut.csv'
   c = csv.writer(open(csvFile, "wb"))
   c.writerow(["#","x","solution","exactSolution"])

   jmax = len(y)
   for j in range(jmax-1):
      if (y[j] <= yLoc) and (y[j+1] > yLoc):
         jL = j
         jR = j + 1
         distL = yLoc - y[jL]
         distR = y[jR] - yLoc
      else:
         continue

   phiMid = []
   exacMid = []
   for i in range(len(x)):
      phiMid.append( phi[i][jL] + phi[i][jR] * distL / (distL + distR) )
      exacMid.append( exact[i][jL] + exact[i][jR] * distL / (distL + distR) )
   dataLength = min(len(x), len(phiMid), len(exacMid))
   for n in range(dataLength):
      c.writerow([x[n], phiMid[n], exacMid[n]])
