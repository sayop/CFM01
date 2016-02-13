Problem 2 - d
=============

Compare average error for grids [10,10], [20,20], [40,40], [80,80].

Here, the average error is defined as solution difference between numerical solution at final iteration and analytical solution:

  .. math::
     err = \frac{\sqrt{\sum_{i=1}^{N \times N}(\phi_i - \phi^{exac}_i)^2}}{N^2}

  .. figure:: ./images/errors.png
     :scale: 80%

  - Discussions

    - Here we see again the second order accuracy with changed of grid size. This is an outcome of central scheme finite difference method.
    - Accuracy is improved by only decreasing grid size. 
    - Impact of numerical scheme on accuracy is NOT noticeable. 
    - The details of error quantity comparison shown below are showing slight improvement of accuracy with advanced schemes, SOR with higher relaxation coefficient for instance.

|

  *Average error according to different schemes*

  +---------+---------------------+---------------------+-------------------------+-------------------------+
  |  N x N  | Jacobian            | Gauss-Seidel        | SOR (alpha = 1.2)       | SOR (alpha = 1.5)       |
  +---------+---------------------+---------------------+-------------------------+-------------------------+
  | 10x10   |  4.17597212966e-05  |  4.12637711927e-05  |  4.07371621739e-05      |  3.80998823969e-05      | 
  +---------+---------------------+---------------------+-------------------------+-------------------------+
  | 20x20   |  6.79949662608e-06  |  6.73688065785e-06  |  6.7040448814e-06       |  6.36361405949e-06      |
  +---------+---------------------+---------------------+-------------------------+-------------------------+
  | 40x40   |  1.75249104594e-06  |  1.74474732047e-06  |  1.72946829409e-06      |  1.70191775112e-06      |
  +---------+---------------------+---------------------+-------------------------+-------------------------+
  | 80x80   |  6.84568684695e-07  |  6.83126277673e-07  |  6.82203360121e-07      |  6.78950654795e-07      |
  +---------+---------------------+---------------------+-------------------------+-------------------------+

