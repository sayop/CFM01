#!/usr/bin/env python
import sys
import numpy as np
import time
sys.path.append('./functions')
from grid import *

start = time.clock()
##
## Input parameters
##

# maximum iterations
nIters = 2

# grid: i,j resolution
iDim = 5
jDim = 5
# x, y: spatial dimension of N^2 nodes
xmin = 0.0
xmax = 1.0
ymin = 0.0
ymax = 1.0
# grid coordinates: Structured
x = np.zeros((iDim))
y = np.zeros((jDim))
x, y, dx, dy = updateGrid(x, y, xmin, xmax, ymin, ymax, iDim, jDim)
# solution space: T
# solution space is initizlied with zeros for every elements.
T = np.zeros((iDim,jDim))
# Boundary condition: T is set to zero on all walls.
Twall = 0.0
# diffusion coefficient: lambda is held constant as one
thermDiffusivity = np.ones((iDim,jDim))
# Source Term matrix: Q{ixj}
Sources = np.zeros((iDim,jDim))

for niter in range(nIters)
   print '------------------------------------------------'
   print '| Iters # = ', niter

   # i-sweep
