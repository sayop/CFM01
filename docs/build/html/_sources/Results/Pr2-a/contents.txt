Problem 2 - a
=============

Given two-dimensional steady heat equation (Poisson's equation:

.. math::
   \lambda\left ( \frac{\partial^2T}{\partial x^2} + \frac{\partial^2 T}{\partial y^2}\right ) + Q = 0

**Discretize** the PDE using a central difference scheme to generate a matrix equation :math:`[A]{T}={Q}`.

Applying second order accuracy central scheme to each second derivative with respect to :math:`x` and :math:`y` gives

.. math::
   \lambda\left [ \frac{T_{i-1,j}-2T_{i,j}+T_{i+1,j}}{\Delta x^2} + \frac{T_{i,j-1} - 2T_{i,j} + 2T_{i,j+1}}{\Delta y^2} \right ] + Q_{i,j} = 0

To construct the coefficient matrix of system of linear equations, the coefficients of each neighbor point should be organized as shown below:

.. math::
   a_{i-1,j}T_{i-1,j} + a_{i+1,j}T_{i+1,j} + a_{i,j-1}T_{i,j-1} + a_{i,j+1}T_{i,j+1} = Q_{i,j}

where each coefficietns are recast in terms of diffusivity and grid size:

.. math::
   a_{L} = a_{R} = \frac{\lambda}{\Delta x^2}

.. math::
   a_{B} = a_{U} =  \frac{\lambda}{\Delta y^2}

and

.. math::
   a_{i,j} = -\left ( \frac{2\lambda}{\Delta x^2} + \frac{2\lambda}{\Delta y^2} \right )

Here, :math:`L`, :math:`R`, :math:`B`, and :math:`U` indicate 'Left', 'Right', 'Bottom' and 'Up' neighbors, respectively.

The coefficients based on a single point :math:`(i,j)` will compose :math:`i\times j`-th row.

.. math::
   AT=Q

where :math:`T` and :math:`Q` are vector having :math:`n^4` elements:

.. math::
   \begin{bmatrix} T_{1,1} & T_{1,2} & \cdots  & T_{1,n} & T_{2,1} & \cdots  & T_{2,n} & \cdots & T_{i,j} & \cdots & T_{n,n} \end{bmatrix}^{T}

.. math::
   \begin{bmatrix} Q_{1,1} & Q_{1,2} & \cdots  & Q_{1,n} & Q_{2,1} & \cdots  & Q_{2,n} & \cdots & Q_{i,j} & \cdots & Q_{n,n} \end{bmatrix}^{T}


