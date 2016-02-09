import numpy as np

def solveEquations(A,imax,Q):
   print '# Finding numerical solutions...'
   # forward elimination:
   # Reference: http://www.cfd-online.com/Wiki/Tridiagonal_matrix_algorithm_-_TDMA_%28Thomas_algorithm%29
   # Forward elimination:
   b = np.zeros(imax)
   d = np.zeros(imax)
   b[0] = A[0][0]
   d[0] = Q[0]
   for i in range(imax):
      if i == 0: continue
      m = A[i][i-1] / b[i-1]
      #A[i][i] = A[i][i] - m * A[i-1][i]
      b[i] = A[i][i] - m * A[i-1][i]
      d[i] = Q[i] - m * d[i-1]
   # Backward substitution:
   phi = np.zeros(imax)
   for i in reversed(range(imax)):
      if i == imax-1: 
         phi[i] = d[i] / b[i]
      else:
         phi[i] = (d[i] - A[i][i+1] * phi[i+1]) / b[i]
   
   return phi

def findResidual(A, Q, phi, x, imax, niter):
   print '# Finding residual at %s iteration(s)...' % (niter + 1)
   residual = 0.0
   for i in range(imax):
      tmp = 0.0
      for j in range(imax):
         tmp += A[i][j] * phi[j]

      residual += (Q[i] - tmp) ** 2

   residual = np.sqrt(residual) / imax

   return residual
