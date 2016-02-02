import numpy as np

def findExactSolution(x,U,gamma,phi,imax):
   exact = np.zeros(imax)
   phiL = phi[0]
   phiR = phi[imax-1]
   L      = x[imax-1]

   for i in range(imax):
      exact[i] = phiL + (phiR - phiL) * (np.exp(x[i]*U[i]/gamma[i]) - 1.0) / (np.exp(L*U[i]/gamma[i]) - 1.0)
   return exact
