Code Instruction
================

The present project is aimed to develop a computer program for solving a steady solution with different numerical method. The code being used for answering all the question here is written with Python language. This program is to run with simple command::
 
  $ python main.py

Before running this Python script, please make sure that you have also *functions* folder that contains pre-defined function for specific purpose use. The problem 1 and problem 2 have different sets of python scripts. However running the script is working in the same methodology.


Quick instruction for problem 1
-------------------------------

To run the simulation, you only need to simply open the file named *main.py* using editor for example, VI on unix system::
 
  $ vi main.py

You should be able to find the following line::

  # maximum iterations
  # For problem1-b, set nIters to 1
  # For poroble1-c, set nIters big enough to run until it converge
  nIters = 20

This is to set maximum iteration number. To run the steady-state linear equation, set it to 1 in order not to repeat redundant iteration.

::

  # grid: i,j,k resolution
  iDim = 20
  jDim = 1
  kDim = 1
  # x: spatial dimension of cube
  xmin = 0.0
  xmax = 1.0
  # Boundary condition
  # Dirichlet BC:
  phi_xLeft = 1
  phi_xRight = 0

In this script, you will also find *iDim* for setting up grid size, and *xmax* for computational domain dimension. Here we are supposed to use Dirichlet boundary condition, so you should speicify the required :math:`\phi` at left and right boundaries.

If you run the simulation with this script, you will see the following files in the same directory::

  sayop@reynolds:~/data/GaTech-CourseWorks/ME-CFM/CFM01/src/pr1$ ls
  dataOut.csv  functions  main.py  prob1Solution.png

*dataOut.csv* is the text file for having numerical solution and analytical solution. And *prob1Solution.png* is a automatically produced line plot for the solution comparison.


Quick instructions for problem 2
--------------------------------

You will have following file and folder for the problem 2 and multi-grid::

  $ sayop@reynolds:~/data/GaTech-CourseWorks/ME-CFM/CFM01/src/multigrid$ ls
  functions  main.py  plotCenterData.py
  $ cd /functions
  $ ll
  drwxrwxr-x 2 sayop sayop 4096 Feb 12 23:01 ./
  drwxrwxr-x 3 sayop sayop 4096 Feb 12 23:35 ../
  -rw-rw-r-- 1 sayop sayop  859 Feb 10 21:48 exactSol.py
  -rw-rw-r-- 1 sayop sayop 1176 Feb 10 21:56 exactSol.pyc
  -rw-rw-r-- 1 sayop sayop  258 Feb 10 21:48 grid.py
  -rw-rw-r-- 1 sayop sayop  471 Feb 10 21:56 grid.pyc
  -rw-rw-r-- 1 sayop sayop 3005 Feb 12 22:39 multigrid.py
  -rw-rw-r-- 1 sayop sayop 2582 Feb 12 22:39 multigrid.pyc
  -rw-rw-r-- 1 sayop sayop 4016 Feb 11 02:03 numericalMethods.py
  -rw-rw-r-- 1 sayop sayop 3886 Feb 11 01:50 numericalMethods.py.bak
  -rw-rw-r-- 1 sayop sayop 2701 Feb 11 02:04 numericalMethods.pyc
  -rw-rw-r-- 1 sayop sayop 2105 Feb 10 21:48 post.py
  -rw-rw-r-- 1 sayop sayop 2791 Feb 10 21:56 post.pyc
  

To run the second simulation with point-iterative method, Jacobi, Gauss-Seidel and SOR for example, you also need to open the file named as *main.py* in /src/pr2/ directory::

  $ vi main.py

First user specified-inputs you will see in this file are::

  # iSwitch for numerical method choice: 0-Jacobi, 1-Gauss-Seidel
  iSwitch = 1
  iMultiGrid = 1

Here, *iSwitch* is supposed to define which method you want to use. *iSwitch=0* will allow you to use Jacobi. Or Set it to 1 to use Gauss-Seidel method and SOR method.

Followings are used for iteration controls::

  # maximum iterations
  nIters = 99999
  # if residual rate comes below this criterion, the iteration will stop!
  convergeCrit = 0.001

Set *nIters* big enough such that your simulation can go over the convergence point. *convergeCrit* is set to 0.001 as requested in the problem.

Followings are grid setup intpus::

  # grid: i,j resolution
  iDim = 40
  jDim = 40
  # x, y: spatial dimension of N^2 nodes
  xmin = 0.0
  xmax = 1.0
  ymin = 0.0
  ymax = 1.0

For the setup of SOR, you can specify :math:`\alpha` from the following line::

  # Relaxation coefficient for SOR: applies to Jacobi and Gauss-Seidel
  relaxCoeff = 1.0

