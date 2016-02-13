Problem 2 - e
=============

Plot and discuss convergence rate for [40,40].

  .. figure:: ./images/convergeRate.png
     :scale: 80%

  - Discussions

    - Using faster convergence scheme proves dramatical improvement of convergence performance.
    - This is because the faster convergence scheme is basically supposed to propagate the infomation faster than Jacobi method, which is based on past level info use while updating the next time level.
    - Relaxation coefficient in SOR method have an additional promotion in fast convergence.

|

- Effect of relaxation factor on convergence performace

  .. figure:: ./images/convergeRate_SOR.png
     :scale: 80%

  - Discussions

    - Using higher value of relaxation factor improves substantial fast convergence.
    - The relaxation factor cannot be used beyond 2. So recommended use of :math:`\alpha` for SOR is :math:`1 < \alpha < 2`
    - :math:`\alpha > 2` is giving an oscillated residual behavior and its mean value keeps consistent over repeated interation and it never ended.
    - Even if it is converged, the use of :math:`\alpha` greater than 1.8 is also showing an unstable residual evolution in time.
    - Best convergence performance was achieved with :math:`\alpha` = 1.9, because it ends at less than 100 iteration with current case setup.
