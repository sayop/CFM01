import numpy as np

def findExactSolution(x, y, imax, jmax):
   exacT = np.zeros((imax,jmax))
   infinitN = 100
   pi = np.pi
   for j in range(jmax-1):
      if j == 0: continue
      for i in range(imax-1):
         if i == 0: continue

         tmp = 0.0
         for n in range(infinitN):
            if not n % 2: continue
            for m in range(infinitN):
               if not m % 2: continue
               aa = 1.0 / (n*m)
               bb = 1.0 / (n**2 + m**2)
               tmp += aa * bb * np.sin(pi*n*x[i]) * np.sin(pi*m*y[j])
         exacT[i][j] = 16.0 * tmp / pi**4
               
   return exacT
