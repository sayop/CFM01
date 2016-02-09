def constructDivergenceTerm(A,imax,dx,DivTermCoeff):
   print '# Constructing divergence term(s) in discretized domain...'

   # Central difference
   for i in range(imax-1):
      if (i == 0): continue
      iL = i - 1
      iR = i + 1
      A[i][i]  += 0
      A[i][iL] += - 0.5 * DivTermCoeff[i] / dx 
      A[i][iR] += 0.5 * DivTermCoeff[i] / dx

   return A

def constructLaplacianTerm(A,imax,dx,gamma):
   print '# Constructing Laplacian term(s) in discretized domain...'

   for i in range(imax-1):
      if (i == 0): continue
      iL = i - 1
      iR = i + 1
      # update central value of gamma between two neighbor nodes
      # gammaL: gamma at i-1/2, gammaR: gamma at 1+1/2
      gammaL = 0.5*(gamma[i] + gamma[i-1])
      gammaR = 0.5*(gamma[i] + gamma[i+1])
      # 1 / dx^2
      InvDxSquare = 1.0 / (dx * dx)
      A[i][i]  += InvDxSquare * (gammaR + gammaL)
      A[i][iL] += - InvDxSquare * gammaL 
      A[i][iR] += - InvDxSquare * gammaR 

   return A

def updateDirichletBC(A,Q,imax,phiLeft,phiRight):
   print '# Updating boundary conditions...'

   # Left boundary
   i = 0
   A[i][i] = 1
   Q[i] = phiLeft
   # Right boundary
   i = imax - 1
   A[i][i] = 1
   Q[i] = phiRight

   return A, Q

def updateAMatrix(A,imax,dx,DivTermCoeff,gamma):
   print '## Updating A matrix...'

   A = constructDivergenceTerm(A,imax,dx,DivTermCoeff)
   A = constructLaplacianTerm(A,imax,dx,gamma)

   return A

