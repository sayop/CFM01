import numpy as np

def pointIterJacobi(phi, Q, lamda, imax, jmax, alpha, dx, dy):
   newT = np.zeros((imax,jmax))
   # this will keep boundary condition fixed
   dxSqr = dx * dx
   dySqr = dy * dy
   # convergence check variable
   deltaSqr = 0.0
   for j in range(jmax-1):
      #if j == 0: continue
      for i in range(imax-1):
         #if i == 0: continue
         if i == 0 or i == imax - 1 or j == 0 or j == jmax - 1:
            newT[i][j] = phi[i][j] # fix boundary values
            continue
         # coeff * T_{i-1,j} in finite difference equation
         neighborL = - lamda[i][j] / dxSqr * phi[i-1][j]
         # coeff * T_{i+1,j} in finite difference equation
         neighborR = - lamda[i][j] / dxSqr * phi[i+1][j]
         # coeff * T_{i,j-1} in finite difference equation
         neighborS = - lamda[i][j] / dySqr * phi[i][j-1]
         # coeff * T_{i,j+1} in finite difference equation
         neighborN = - lamda[i][j] / dySqr * phi[i][j+1]
         # This is coefficient for my PHI at location (i,j).
         myCoef    = 2.0 * lamda[i][j] * (1.0/dxSqr + 1.0/dySqr)
         # update NEW phi
         newPhi = (Q[i][j] - neighborL - neighborR - neighborS - neighborN) / myCoef
         phiIncrement = newPhi - phi[i][j]
         newT[i][j] = phi[i][j] + alpha * phiIncrement

         # compute RMS of difference between solutions at iterations
         deltaSqr += phiIncrement ** 2
   numberOfInnerPoints = (imax-2) * (jmax-2)
   deltaRMS = np.sqrt(deltaSqr / numberOfInnerPoints)

   return newT, deltaRMS


def pointIterGS(phi, Q, lamda, imax, jmax, alpha, dx, dy):
   dxSqr = dx * dx
   dySqr = dy * dy
   # convergence check variable
   deltaSqr = 0.0
   for j in range(jmax-1):
      if j == 0: continue
      for i in range(imax-1):
         if i == 0: continue
         # coeff * T_{i-1,j} in finite difference equation
         neighborL = - lamda[i][j] / dxSqr * phi[i-1][j]
         # coeff * T_{i+1,j} in finite difference equation
         neighborR = - lamda[i][j] / dxSqr * phi[i+1][j]
         # coeff * T_{i,j-1} in finite difference equation
         neighborS = - lamda[i][j] / dySqr * phi[i][j-1]
         # coeff * T_{i,j+1} in finite difference equation
         neighborN = - lamda[i][j] / dySqr * phi[i][j+1]
         # This is coefficient for my PHI at location (i,j).
         myCoef    = 2.0 * lamda[i][j] * (1.0/dxSqr + 1.0/dySqr)
         # update NEW phi
         newPhi = (Q[i][j] - neighborL - neighborR - neighborS - neighborN) / myCoef
         phiIncrement = newPhi - phi[i][j]
         phi[i][j] = phi[i][j] + alpha * phiIncrement

         # compute RMS of difference between solutions at iterations
         deltaSqr += phiIncrement ** 2
   numberOfInnerPoints = (imax-2) * (jmax-2)
   deltaRMS = np.sqrt(deltaSqr / numberOfInnerPoints)

   return phi, deltaRMS




def computeResidual(phi, Q, lamda, imax, jmax, dx, dy):
   # A 2D matrix is defined for storing residuals
   rMatrix = np.zeros((imax,jmax))
   residual = 0.0
   dxSqr = dx * dx
   dySqr = dy * dy
   for j in range(jmax-1):
      if j == 0: continue
      for i in range(imax-1):
         if i == 0: continue
         # This is coefficient for my PHI at location (i,j).
         me        = 2.0 * (1.0/dxSqr + 1.0/dySqr) * phi[i][j]
         # coeff * T_{i-1,j} in finite difference equation
         neighborL = - lamda[i][j] / dxSqr * phi[i-1][j]
         # coeff * T_{i+1,j} in finite difference equation
         neighborR = - lamda[i][j] / dxSqr * phi[i+1][j]
         # coeff * T_{i,j-1} in finite difference equation
         neighborS = - lamda[i][j] / dySqr * phi[i][j-1]
         # coeff * T_{i,j+1} in finite difference equation
         neighborN = - lamda[i][j] / dySqr * phi[i][j+1]
         rho = Q[i][j] - me - neighborL - neighborR - neighborS - neighborN
         residual += rho ** 2
         rMatrix[i][j] = rho

   numberOfInnerPoints = (imax-2) * (jmax-2)
   residual = residual / numberOfInnerPoints
   residual = np.sqrt(residual)
   return residual, rMatrix
