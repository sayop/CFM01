import numpy as np

def findExactSolution1(x,U,gamma,phi,imax):
   exact = np.zeros(imax)
   phiL = phi[0]
   phiR = phi[imax-1]
   L      = x[imax-1]

   for i in range(imax):
      exact[i] = phiL + (phiR - phiL) * (np.exp(x[i]*U[i]/gamma[i]) - 1.0) / (np.exp(L*U[i]/gamma[i]) - 1.0)
   return exact

def findExactSolution2(x,imax):
   exact = np.zeros(imax)
   for i in range(imax):
      exact[i] = -1.0 + np.sqrt(4.0 - 3.0 * x[i])

   return exact

def findExactSolution3(x,imax):
   exact = np.zeros(imax)
   for i in range(imax):
      exact[i] = -1.0 + np.sqrt(4.0 - 2.0 * x[i] - x[i]**2)

   return exact

def findExactSolution4(x,imax):
   exact = np.zeros(imax)
   for i in range(imax):
      exact[i] = -1.0 + np.sqrt(4.0 - (8.0/3.0) * x[i] - x[i]**3 / 3.0)

   return exact


def findAverageError(imax, phi, exact):
   errorRMS = 0.0
   for i in range(imax):
      errorRMS += (phi[i] - exact[i]) ** 2

   errorRMS = np.sqrt(errorRMS) / imax
   
   return errorRMS

