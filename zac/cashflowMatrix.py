import sys
from gurobipy import *
from myMatrixLpSolver import lp_optimize	


# Put model data into dense matrices (Change from here to solve a different problem)

c = [0, 0, 0, 0, 0, 1]
obj_sense = GRB.MAXIMIZE
A = [[1, 1, 0, 0, 0, 0], 
     [0.92, 0.82, 0, 1, 0, 0],
     [0, 0, 1, -1, 0, 0],
     [0, 1.1, -1.02, 1.02, -1, 0],
     [1.3, 0, 1.5, 0, 1.02, -1]]
sense = [GRB.LESS_EQUAL, GRB.EQUAL, GRB.LESS_EQUAL, GRB.EQUAL, GRB.EQUAL]
rhs = [100, 102, 0, 0, 0];
lb=[0]*6
ub=[GRB.INFINITY]*6
vtype = [GRB.CONTINUOUS]*6
sol = [0]*6

# Optimize

success = lp_optimize(5, 6, c, obj_sense, A, sense, rhs, lb, ub, vtype, sol)

if success:
  print('x_a: %g, x_b: %g, x_c: %g, y_1: %g, y_2: %g, y_3: %g' % (sol[0], sol[1], sol[2], sol[3], sol[4], sol[5]))
