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

def writeCSV(x,y,dx,dy,phi,exact,yLoc):
   print '# Writing a csv file to store line data in x-direction'
   csvFile = 'dataOut.csv'
   c = csv.writer(open(csvFile, "wb"))
   c.writerow(["x","solution","exactSolution"])

   imax = len(x)
   jmax = len(y)
   phiIDW = []
   exactIDW = []
   diagonal = np.sqrt(dx **2 + dy ** 2)
   # inverse distance weighting
   p = 2
   for n in range(imax):
      tmp1 = 0.0
      tmp2 = 0.0
      tmp3 = 0.0
      xMeas = x[n]
      yMeas = yLoc
      for j in range(jmax):
         for i in range(imax):
            dist = np.sqrt( (xMeas - x[i]) ** 2 +
                            (yMeas - y[j]) ** 2 )
            dist = max(1e-9,dist)
            
            if dist > 0.5*diagonal:
               continue
            else:
               wi = 1.0 / dist ** p
               tmp1 += wi
               tmp2 += wi * phi[i][j]
               tmp3 += wi * exact[i][j]

      phiIDW.append(tmp2/tmp1)
      exactIDW.append(tmp3/tmp1)
            
   dataLength = len(x)
   for n in range(dataLength):
      c.writerow([x[n], phiIDW[n], exactIDW[n]])


def writeConvergenceTrace(residual):
   ndata = len(residual)
   print '# Writing convergence rate trace...'
   csvFile = 'convergenceRate.csv'
   c = csv.writer(open(csvFile, "wb"))
   c.writerow(["iter","converge"])

   for n in range(ndata):
      c.writerow([n+1,residual[n]])
