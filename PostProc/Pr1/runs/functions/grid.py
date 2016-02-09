
def updateGrid(x, xmin, xmax, imax):
   dx = (xmax - xmin) / (imax - 1)
   for i in range(imax):
      x[i] = xmin + dx * i
   return x, dx
