import numpy as np
from numericalMethods import *

def transferFineToCoarse(F,imax,jmax):
   icmax = int(imax/2)
   jcmax = int(jmax/2)
   C = np.zeros((icmax,jcmax))
   for j in range(jcmax):
      for i in range(icmax):
         C[i][j] = 0.25 * ( F[2*i][2*j] +
                            F[2*i][2*j+1] +
                            F[2*i+1][2*j] +
                            F[2*i+1][2*j+1] )

   return C

def prolongCoarseToFine(C,icmax,jcmax):
   imax = int(2*icmax)
   jmax = int(2*jcmax)
   F = np.zeros((imax,jmax))
  
   for j in range(jmax-1):
      if j == 0: continue
      jR = int(round(j/2.0))
      jL = jR - 1
      if (int(j/2) == jL):
         jClose = jL
         jFar   = jR
      else:
         jClose = jR
         jFar   = jL
      for i in range(imax-1):
         if i == 0: continue
         iR = int(round(i/2.0))
         iL = iR - 1
         if (int(i/2) == iL):
            iClose = iL
            iFar   = iR
         else:
            iClose = iR
            iFar   = iL
         F[i][j] = 0.25 * ( 0.25*C[iFar][jFar] + 0.75*C[iClose][jFar] ) + 0.75 * ( 0.25*C[iFar][jClose] + 0.75*C[iClose][jClose] )
   return F


def computeOnCoarseGrid(rMatF,Q,gammaF,errorF,imax,jmax,dx,dy,iSwitch,relaxCoeff):
   niters = 10
   convergeCrit = 0.01

   # rMatF: residual matrix for fine grid
   # rMatC: residual matrix for coarse grid
   icmax = int(imax/2)
   jcmax = int(jmax/2)

   # Reconstruct matricees for coarse grid before applying iteration methods.
   rMatC  = transferFineToCoarse(rMatF,imax,jmax)
   gammaC = transferFineToCoarse(gammaF,imax,jmax)
   # error is going to be solved as an unkown vector and will be added to 
   # estimate the future step guess value for PHI.
   #errorC  = np.zeros((icmax,jcmax))
   # Initial guess of error matrix is given from the fine grid's error matrix and multiplied by 0.1 for under relaxing.
   errorC = 0.5 * transferFineToCoarse(errorF,imax,jmax)

   if iSwitch == 0:
      print '|- Running Jacobi for updating error matrix in coarse grid...'
   elif iSwitch == 1:
      print '|- Running GS for updating error matrix in coarse grid...'
   for n in range(niters):
      #print '|-- Sub-iteration #', n+1, 'for coarse grid'
      if n == 0: residualInit, dump = computeResidual(errorC, rMatC, gammaC, icmax, jcmax, 2.0*dx, 2.0*dy)
      if iSwitch == 0:
         errorC, deltaRMS = pointIterJacobi(errorC, rMatC, gammaC, icmax, jcmax, relaxCoeff, 2.0*dx, 2.0*dy)
      elif iSwitch == 1:
         errorC, deltaRMS = pointIterGS(errorC, rMatC, gammaC, icmax, jcmax, relaxCoeff, 2.0*dx, 2.0*dy)
      # compute residual for updated solution
      residual, dump = computeResidual(errorC, rMatC, gammaC, icmax, jcmax, 2.0*dx, 2.0*dy)

      # check convergence rate:
      convergenceRate = residual / residualInit
      if convergenceRate <= convergeCrit:
         print '|-- Sub-iteration converged successfully at', convergenceRate, '!!!!'
         break

   errorF = prolongCoarseToFine(errorC,icmax,jcmax)

   return errorF
