import matplotlib.pyplot as plt
import csv

def plotSolutions(x,phi,exact):
   imax = len(x)
   pltFile = 'prob1Solution.png'
   MinX = min(x)
   MaxX = max(x)
   MinY = min(exact)
   MaxY = 1.1*max(phi)

   p = plt.plot(x,phi, 'k-', label='Numerical solution')
   p = plt.plot(x,exact, 'r-', label='Analytical solution')

   plt.setp(p, linewidth='2.0')
   plt.axis([MinX,MaxX, MinY, MaxY])
   plt.xscale('linear')
   plt.yscale('linear')
   plt.xlabel('x', fontsize=22)
   plt.ylabel('phi', fontsize=22)

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
   plt.savefig(pltFile, format='png')
   plt.close()

   print "%s DONE!!" % (pltFile)


def writeCSV(x,phi):
   print '# Writing a csv file to store data...'
   csvFile = 'dataOut.csv'
   c = csv.writer(open(csvFile, "wb"))
   c.writerow(["#","x","solution"])
   dataLength = min(len(x), len(phi))
   for n in range(dataLength):
      c.writerow([x[n], phi[n]])
