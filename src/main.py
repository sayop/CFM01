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
nIters = 20

# grid: i,j,k resolution
iDim = 10
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
DivTermCoeff = np.ones((iDim))
#DivTermCoeff = np.zeros((iDim))

# grid coordinates: Structured
x = np.zeros((iDim))
x, dx = updateGrid(x, xmin, xmax, iDim)

# Gamma: diffusion coefficient
gamma = 0.1*np.ones((iDim))
# phi vector on every grid nodes
#phi = np.zeros((iDim, nDepVars))
phi = np.zeros((iDim))
# to store analytical solution
phiExact = np.zeros((iDim))

# Iteration loop:
for niter in range(nIters):
   print '------------------------------------------------'
   print '| Iters # = ', niter
   # A: coefficient matrix in system of algebraic equations
   A = np.zeros((iDim,iDim))
   # source terms
   #Q = np.zeros((iDim))
   Q = 0.0*np.ones((iDim))
   # update A matrix
   # Update gamma vector for prob. 1-c
   #for n in range(iDim):
   #   gamma[n] = 0.1 + 0.1 * phi[n]
   A = updateAMatrix(A, iDim, dx, DivTermCoeff, gamma)
   # update boundary condition in A matrix
   A, Q = updateDirichletBC(A, Q, iDim, phi_xLeft, phi_xRight)
   # Solve the systen of algebraic equations
   phi = solveEquations(A,iDim,Q)

exact = findExactSolution(x,DivTermCoeff,gamma,phi,iDim)

# time elapsed:
elapsed = (time.clock() - start)
print "## Elapsed time: ", elapsed

#print "## Exact solution: ", exact
# make a plot for solution
plotSolutions(x, phi, exact)

# store data in plain text with csv file format
writeCSV(x,phi)

