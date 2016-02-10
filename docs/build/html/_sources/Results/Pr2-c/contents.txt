Problem 2 - c
=============

(1) **Plot** both temperature contours and centerline profiles (T vs. :math:`x` or :math:`y` through center) for each different method.


- CASE1: Jacobi method

  (a) Temperature contour

    .. figure:: ./images/prob2_NumericalJacobi.png
       :scale: 80%

  (b) Temperature along the center line

    .. figure:: ./images/solutions_Jacobi.png
       :scale: 60%
  

  - Converged at 2068th iteration
  - Averaged error: 1.75249104594e-06
  - Calculation time: 27.746111 [sec]

  
|

- CASE2: Gauss-Seidel method


  (a) Temperature contour

    .. figure:: ./images/prob2_NumericalGS.png
       :scale: 80%

  (b) Temperature along the center line

    .. figure:: ./images/solutions_GS.png
       :scale: 60%

  - Converged at 1034th iteration (faster than Jacobi method by a factor of 2)
  - Averaged error: 1.74474732047e-06
  - Calculation time: 13.999504 [sec]

|


- CASE2: Successive Over-Relaxation (SOR) method (Variant form of G-S method): :math:`\alpha` = 1.2


  (a) Temperature contour

    .. figure:: ./images/prob2_NumericalSOR.png
       :scale: 80%

  (b) Temperature along the center line

    .. figure:: ./images/solutions_SOR.png
       :scale: 60%

  - Converged at 689th iteration (faster than Jacobi method by a factor of 3)
  - Averaged error: 1.72946829409e-06
  - Calculation time: 9.319121 [sec]
