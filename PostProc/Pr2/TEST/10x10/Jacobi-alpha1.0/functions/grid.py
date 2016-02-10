
def updateGrid(x, y, xmin, xmax, ymin, ymax, imax, jmax):
   dx = (xmax - xmin) / (imax - 1)
   dy = (ymax - ymin) / (jmax - 1)
   for i in range(imax):
      x[i] = xmin + dx * i

   for j in range(jmax):
      y[j] = ymin + dy * j

   return x, y, dx, dy
