Problem 2 - f
=============

**Compare** computational time obtained with different methods and evaluate the time complexity of the methods.

The scaling test has been done for the different numerical methods on 40x40 grid case. The computational time was measured solely for the essential parts of computing process. Pre- and Post-processing computation was not included in that time measurement. The following table show the direct comparison of time consumed with different methods as well as average error.

 +-----------+---------------+-------------------+
 | methods   | Compute time  | average error     |
 +-----------+---------------+-------------------+
 | Jacobi    | 29.486377     | 1.75249104594e-06 |
 +-----------+---------------+-------------------+
 | G-S       | 14.826672     | 1.74474732047e-06 |
 +-----------+---------------+-------------------+
 | SOR 1.2   | 9.79673       | 1.72946829409e-06 |
 +-----------+---------------+-------------------+
 | SOR 1.5   | 4.852003      | 1.70191775112e-06 |
 +-----------+---------------+-------------------+
 | SOR 1.8   | 1.53902       | 1.39199894688e-06 |
 +-----------+---------------+-------------------+
 | SOR 1.9   | 1.150155      | 5.73021575907e-07 |
 +-----------+---------------+-------------------+
 | SOR 1.95  | 2.353955      | 5.96044300326e-07 |
 +-----------+---------------+-------------------+

 - Discussions

   - As observed in the previous section, the best performance was achieved with choice of :math:`\alpha` = 1.95 usign SOR method. 
   - The computational time is reduced almost by a factor of 25 from the worst case. 
   - This dramatical improvement is obtained even with slightly improved average error.
   - All of the numerical method used here is esentially based on iterative method which is supposed to propagate the updated info to the final solution.
   - For that reason, the over-relaxed increment of solution is actually aimed to promote the speed of infomation propagation such that it fastly reaches to the converged solution.
   - However, exceesive promotion with greater value than :math:`\alpha` = 2 is likely to make over-shoot effect of increment that incudes divergence of the solution.
