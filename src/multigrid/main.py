#!/usr/bin/env python
import sys
import numpy as np
import time
sys.path.append('./functions')
from grid import *
from numericalMethods import *
from exactSol import *
from post import *
from multigrid import *

start = time.clock()
##
## Input parameters
##

# iSwitch for numerical method choice: 0-Jacobi, 1-Gauss-Seidel
iSwitch = 0

# maximum iterations
nIters = 1

# if residual rate comes below this criterion, the iteration will stop!
convergeCrit = 0.001

# grid: i,j resolution
iDim = 8
jDim = 8
icDim = int(iDim / 2)
jcDim = int(jDim / 2)
# x, y: spatial dimension of N^2 nodes
xmin = 0.0
xmax = 1.0
ymin = 0.0
ymax = 1.0
# Relaxation coefficient for SOR: applies to Jacobi and Gauss-Seidel
relaxCoeff = 1.0
# grid coordinates: Structured
x = np.zeros((iDim))
y = np.zeros((jDim))
x, y, dx, dy = updateGrid(x, y, xmin, xmax, ymin, ymax, iDim, jDim)
# solution space: T
# solution space is initizlied with zeros for every elements.
T = np.zeros((iDim,jDim))
# diffusion coefficient: lambda is held constant as one
thermDiffusivity = np.ones((iDim,jDim))
# Source Term matrix: Q{ixj}
Sources = np.ones((iDim,jDim))

residualTrace = []

for niter in range(nIters):

   #compute residual at initial state
   if niter == 0: residualInit, rMat = computeResidual(T, Sources, thermDiffusivity, iDim, jDim, dx, dy)

   # go for point-iterations: will update new time level
   if iSwitch == 0:
      # 0: runs for Jacobi method with relaxation coefficient.
      newT, deltaRMS = pointIterJacobi(T, Sources, thermDiffusivity, iDim, jDim, relaxCoeff, dx, dy)
   elif iSwitch == 1:
      # 1: runs for Jacobi method with relaxation coefficient.
      newT, deltaRMS = pointIterGS(T, Sources, thermDiffusivity, iDim, jDim, relaxCoeff, dx, dy)

   # compute residual for updated solution
   residual, rMat = computeResidual(newT, Sources, thermDiffusivity, iDim, jDim, dx, dy)   

   #
   # Go into coarse grid calculation for multigrid method
   # 
   computeOnCoarseGrid(rMat,Sources,thermDiffusivity,iDim,jDim,dx,dy,iSwitch,relaxCoeff)

   # check convergence rate:
   convergenceRate = residual / residualInit
   print '| Convergence rate: ', convergenceRate
   residualTrace.append(convergenceRate)
   if convergenceRate <= convergeCrit: 
      print '| CONVERGED SUCCESSFULLY at', convergenceRate, '!!!!'
      break
   
   # update T
   T = newT
   #print T
   print '| Iters # = ', niter, 'Done!!'

# time elapsed:
elapsed = (time.clock() - start)
print "## Elapsed time: ", elapsed

# exacsolution space
exacT = findExactSolution(x, y, iDim, jDim)

# return average error: the error is defined as RMS of 
# deviation of numerical solution from exact solution 
# at every node points
error = findAverageError(iDim, jDim, T, exacT)
print "## Average error = ", error

plotContour(x, y, T, 'prob2_NumericalTemperature.png')
plotContour(x, y, exacT, 'prob2_ExactTemperature.png')
writeCSV(x, y, dx, dy, T, exacT, 0.5)
writeConvergenceTrace(residualTrace)
