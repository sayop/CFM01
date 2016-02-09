Problem 1 - c
=============

Given conditions: :math:`U` = 0, :math:`\Gamma` = 0.1 + 0.1 :math:`\phi`, and :math:`N` = 20. 

(1) Find :math:`\phi` using TDMA for following :math:`Q` and corresponding exact solution cases:

- CASE1:  :math:`Q = 0`,  :math:`\;\; \phi(x) = -1+\sqrt{4-3x}`

  .. figure:: ./images/pr1c_case1.png
     :scale: 60%    

  - Converged at 5th iterations with residual of 0.000876728469266
  - Average error = 9.0129271003e-06
  - Calculation time [sec] = 0.001337
|

- CASE2:  :math:`Q = 0.1`,  :math:`\;\; \phi(x) = -1+\sqrt{4-2x-x^{2}}`

  .. figure:: ./images/pr1c_case2.png
     :scale: 60%

  - Converged at 5th iterations with residual of 0.000716942145114
  - Average error = 1.01159413052e-05
  - Calculation time [sec] = 0.001741

|

- CASE3:  :math:`Q = 0.1x`,  :math:`\;\; \phi(x) = -1+\sqrt{4-(8/3)x - x^{3}/3}`

  .. figure:: ./images/pr1c_case3.png
     :scale: 60%

  - Converged at 5th iterations with residual of 0.000707116960016
  - Average error = 8.99517612803e-06
  - Calculation time [sec] = 0.001404

|
