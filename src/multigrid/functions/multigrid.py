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

def computeOnCoarseGrid(rMatF,Q,gammaF,imax,jmax,dx,dy,iSwitch,relaxCoeff):
   niters = 100
   convergeCrit = 0.001

   # rMatF: residual matrix for fine grid
   # rMatC: residual matrix for coarse grid
   icmax = int(imax/2)
   jcmax = int(jmax/2)

   # Reconstruct matricees for coarse grid before applying iteration methods.
   rMatC  = transferFineToCoarse(rMatF,imax,jmax)
   QC     = transferFineToCoarse(Q,imax,jmax)
   gammaC = transferFineToCoarse(gammaF,imax,jmax)
   # error is going to be solved as an unkown vector and will be added to 
   # estimate the future step guess value for PHI.
   errorC  = np.zeros((icmax,jcmax))

   if iSwitch == 0:
      print '|- Running Jacobi for updating error matrix in coarse grid...'
   elif iSwitch == 1:
      print '|- Running GS for updating error matrix in coarse grid...'
   for n in range(niters):
      print '|-- Sub-iteration #', n+1
      if n == 0: residualInit, dump = computeResidual(errorC, QC, gammaC, icmax, jcmax, 2.0*dx, 2.0*dy)
      if iSwitch == 0:
         errorC, deltaRMS = pointIterJacobi(errorC, QC, gammaC, icmax, jcmax, relaxCoeff, 2.0*dx, 2.0*dy)
      elif iSwitch == 1:
         errorC, deltaRMS = pointIterGS(errorC, QC, gammaC, icmax, jcmax, relaxCoeff, 2.0*dx, 2.0*dy)
      # compute residual for updated solution
      residual, dump = computeResidual(errorC, QC, gammaC, icmax, jcmax, 2.0*dx, 2.0*dy)

      # check convergence rate:
      convergenceRate = residual / residualInit
      if convergenceRate <= convergeCrit:
         print '| SUB-ITERATIONS CONVERGED SUCCESSFULLY at', convergenceRate, '!!!!'
         break
