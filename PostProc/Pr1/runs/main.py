#!/usr/bin/env python
import sys
import numpy as np
import time
sys.path.append('./functions')
from grid import *
from descretization import *
from numericalSolution import *
from exactSolution import *
from post import *

start = time.clock()
##
## Input parameters
##

# maximum iterations
# For problem1-b, set nIters to 1
# For poroble1-c, set nIters big enough to run until it converge
nIters = 1


# grid: i,j,k resolution
iDim = 50
jDim = 1
kDim = 1
# x: spatial dimension of cube
xmin = 0.0
xmax = 1.0
# Boundary condition
# Dirichlet BC:
phi_xLeft = 1
phi_xRight = 0
# DivTermCoeff: coefficient of divergence term.
# In this project, this is equivalent to U, which is convective velocity.
# Set this value to zero for pr1-c
DivTermCoeff = np.ones((iDim))
#DivTermCoeff = np.zeros((iDim))

# grid coordinates: Structured
x = np.zeros((iDim))
x, dx = updateGrid(x, xmin, xmax, iDim)

# Gamma: diffusion coefficient
gamma = 0.1*np.ones((iDim))
# phi vector on every grid nodes
# solution space is initizlied with zeros for every elements.
phi = np.zeros((iDim))
# to store analytical solution
phiExact = np.zeros((iDim))

# source terms
Q = 0.0*np.ones((iDim))
#Q = 0.1*np.ones((iDim))
#Q = 0.1 * x


# Iteration loop:
for niter in range(nIters):
   print '------------------------------------------------'
   print '| Iters # = ', niter

   # A: coefficient matrix in system of algebraic equations
   # And, update boundary condition in A matrix
   # Actually, A and Q matrix are having fixed value at every iteration 
   # except for non-linear equations. However, A matrix needs to be
   # re-initialized because its elements are accumulated with updated 
   # coefficient during iterations.
   A = np.zeros((iDim,iDim))
   A, Q = updateDirichletBC(A, Q, iDim, phi_xLeft, phi_xRight)
   # Update gamma vector for prob. 1-c
   #gamma = 0.1 + 0.1*phi
   # update A matrix
   # A matrix is constructed by descritizing convection term and 
   # diffusion term independently. 
   A = updateAMatrix(A, iDim, dx, DivTermCoeff, gamma)
   residual = findResidual(A, Q, phi, x, iDim, niter)
   if niter == 0:
      residualInit = residual
      residual = 1.0
   else:
      residual = residual / residualInit

   print '## Residual=', residual
   if residual <= 1.0e-3:
      print "## Solution has been converged!!!!"
      break
   # Solve the systen of algebraic equations using TDMA method
   phi = solveEquations(A,iDim,Q)


# exact solution for pr1-b
exact = findExactSolution1(x,DivTermCoeff,gamma,phi,iDim)
# exact solution for pr1-c: Q=0.0
#exact = findExactSolution2(x,iDim)
# exact solution for pr1-c: Q=0.1
#exact = findExactSolution3(x,iDim)
# exact solution for pr1-c: Q=0.1x
#exact = findExactSolution4(x,iDim)

# return average error: the error is defined as RMS of 
# deviation of numerical solution from exact solution 
# at every node points
error = findAverageError(iDim, phi, exact)
print "## Average error = ", error

# time elapsed:
elapsed = (time.clock() - start)
print "## Elapsed time: ", elapsed

#print "## Exact solution: ", exact
# make a plot for solution
plotSolutions(x, phi, exact)

# store data in plain text with csv file format
writeCSV(x,phi,exact)

