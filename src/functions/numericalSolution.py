import numpy as np

def solveEquations(A,imax,Q):
   print '# Finding numerical solutions...'
   # forward elimination:
   # Reference: http://www.cfd-online.com/Wiki/Tridiagonal_matrix_algorithm_-_TDMA_%28Thomas_algorithm%29
   # Forward elimination:
   for i in range(imax):
      if i == 0: continue
      m = A[i][i-1] / A[i-1][i-1]
      A[i][i] = A[i][i] - m * A[i-1][i]
      Q[i] = Q[i] - m * Q[i-1]
   # Backward substitution:
   phi = np.zeros(imax)
   for i in reversed(range(imax)):
      if i == imax-1: 
         phi[i] = Q[i] / A[i][i]
      else:
         phi[i] = (Q[i] - A[i][i+1] * phi[i+1]) / A[i][i]
   
   
   # Reference: https://en.wikipedia.org/wiki/Tridiagonal_matrix_algorithm
   # Forward sweep
   #for i in range(imax-1):
   #   if i == 0:
   #      A[i][i+1] = A[i][i+1] / A[i][i]
   #      Q[i]      = Q[i] / A[i][i]
   #   else:
   #      A[i][i+1] = A[i][i+1] / (A[i][i] - A[i][i-1] * A[i-1][i])
   #      Q[i]      = (Q[i] - A[i][i-1] * Q[i-1]) / (A[i][i] - A[i][i-1] * A[i-1][i])
   #   A[i][i] = 1.0
   ## Backward substitution:
   #phi = np.zeros(imax)
   #for i in reversed(range(imax)):
   #   if i == imax-1:
   #      phi[i] = Q[i]
   #   else:
   #      phi[i] = Q[i] - A[i][i+1] * phi[i+1]


   return phi

