Problem 2 - b
=============

For each of the Jacobi, Gauss-Seidel, and SOR methods, **express** :math:`T^k_{i,j}`, the temperature at node :math:`(i,j)` and iteration :math:`k+1`, in terms of the temperatures of its neighbors at either the current or past iterations.

- Jacobi method

  Jacobi method is to update every node points with solution from past iterations. Therefore the tempertaure on the neighbor nodes represents previous teme level, so it does not matter with the sweep direction.

.. math::
   T^{k+1}_{i,j} = \frac{1}{a_{i,j}}\left [ Q_{i,j} - a_{L}T^k_{i-1,j} - a_{R} T^k_{i+1,j} - a_{B}T^k_{i,j-1} - a_{U}T^k_{i,j+1} \right ]

- Gauss-Seidel method

  Gauss-Seidel method is different from the Jacobi method in terms of neighbor points' time level. Contrary to the Jacobi's, the Gauss-Seidel method allows us to use lately updated solution. When it sweeps in :math:`i`-direction, and :math:`j`-direction and is located on :math:`(i,j)` node, left and bottom point data have already been updated. Instead using past time level data, Gauss-Seidel method is to use the latest ones such that it promotes the faster convergence.

  Now this method propagates the infomation from left and bottom to right and up at one time level.

.. math::
   T^{k+1}_{i,j} = \frac{1}{a_{i,j}}\left [ Q_{i,j} - a_{L}T^{k+1}_{i-1,j} - a_{R} T^k_{i+1,j} - a_{B}T^{k+1}_{i,j-1} - a_{U}T^k_{i,j+1} \right ]

- Successive Over-Relaxation (SOR)

  Successive over-relaxation (SOR) is a variant of the Gauss-Seidel method, resulting in faster convergence. Thus, the basic form of this method is almost equivalent to the Gauss-Seidel method. The only difference is to put relaxation coefficient in the increment of solution. This can be expressed by:

.. math::
   T^{k+1}_{i,j} = T^k_{i,j} + \frac{\alpha}{a_{i,j}}\left [ - a_{i,j}T^k_{i,j} + Q_{i,j} - a_{L}T^{k+1}_{i-1,j} - a_{R} T^k_{i+1,j} - a_{B}T^{k+1}_{i,j-1} - a_{U}T^k_{i,j+1} \right ]
