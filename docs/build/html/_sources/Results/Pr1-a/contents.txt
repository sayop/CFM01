Problem 1 - a
=============

Develop a finite difference algorithm using central differences for the solution of the transport equation. Describe the essential steps.

Given equation: 

.. math::

   U\frac{\partial \phi}{\partial x} = \frac{\partial}{\partial x} \left ( \Gamma \frac{\partial \phi}{\partial x} \right ) + Q

To make the given form of equation convenient to be converted into descritized algebraic equations, terms having dependent variables are sorted out in the left hand side leaving :math:`Q` in the right hand side as:

.. math::
   U\frac{\partial \phi}{\partial x} - \frac{\partial}{\partial x} \left ( \Gamma \frac{\partial \phi}{\partial x} \right ) = + Q

Now, the left hand side is composed of convection term and diffusion term, respectively. These two term are going to be referred to as *divergence* term and *laplacian* term, respectively.

- Divergence term descritization:

  .. math::
     U\frac{\partial \phi}{\partial x}:\;\; U\left ( \frac{\phi_{i+1} - \phi_{i-1}}{\Delta  x} \right )

  Again, further descritzation should be done for the remaining first derivative in the middle points at :math:`i+1/2` and :math:`i-1/2` and it leads to:

  .. math::
     -\frac{1}{\Delta x} \left [ \frac{\Gamma_{i+1/2}\left ( \phi_{i+1} - \phi_{i-1} \right ) - \Gamma_{i-1/2}\left ( \phi_{i} - \phi_{i-1} \right )}{\Delta x} \right ]



- Laplacian term descritization:

  .. math::
     - \frac{\partial}{\partial x} \left ( \Gamma \frac{\partial \phi}{\partial x} \right ): \;\; -\frac{1}{\Delta x} \left [ \left ( \Gamma \frac{\partial \phi}{\partial x} \right )_{i+1/2} - \left ( \Gamma \frac{\partial \phi}{\partial x} \right )_{i-1/2} \right ]

Constructing every terms with source term in right hand side at :math:`i` node point becomes such that the final form has three terms with respective corresponding :math:`i` node and neightbor points, :math:`i-1` and :math:`i+1` will become:

  .. math::
     a_{i-1} \phi_{i-1} + a_{i} \phi_{i} + a_{i+1} \phi_{i+1} = Q_{i}

  where, 

  .. math::
     a_{i} = \frac{\left ( \Gamma_{i+1/2} + \Gamma_{i-1/2} \right )}{\Delta x^2}

  .. math::
     a_{i-1} = - \left ( \frac{\Gamma_{i-1/2}}{\Delta x^2} + \frac{U}{\Delta x} \right )

  .. math::
     a_{i+1} = - \left ( \frac{\Gamma_{i+1/2}}{\Delta x^2} - \frac{U}{\Delta x} \right )


Here again we need to quantify the diffusion coefficient :math:`\Gamma` at middle points where are not actually in presence. Therefore, linear interpolation is done for those middle point for having diffusivity in the second derivative terms:

  .. math::
     \Gamma_{i+1/2} = \frac{1}{2}\left ( \Gamma_{i+1} + \Gamma_{i-1} \right )


Now we have single algebraic equation for each single node point. The node point is now linked to the neighbor right next to it. Thus, we can construct tri-diagonal matrix for those coefficients when we construct system of linear equations in 1-dimensional problem: :math:`A \Phi = Q`. :math:`A` can be described as a matrix or tensor form with two ranks. :math:`\Phi` and :math:`Q` are vectors.




