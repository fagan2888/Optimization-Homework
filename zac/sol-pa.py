from gurobipy import *
from myMatrixLpSolver import lp_optimize

f = open('dataLR.txt', 'r')
N = 10000
C = 10
x = [[0 for j in range(C)] for i in range(N)]
y = [0 for i in range(N)]
i = -1
for line in f:
    i = i+1
    line = line.strip()
    columns = line.split(',')
    y[i] = float(columns[0])
    for j in range(0, 10):
        x[i][j] = float(columns[j+1])
f.close()

c = [0] * (C+2)
c[0] = 1
obj_sense = GRB.MINIMIZE
A = [[0 for j in range(C+2)] for i in range(2*N)]
rhs = [0 for i in range(2*N)]
for i in range(0, N):
    for j in range(C):
        A[i][j] = x[i][j]
        A[i+N][j] = -1*x[i][j]
        A[i][0] = 1
        A[i+N][0] = 1
        A[i][C+1] = 1
        A[i+N][C+1] = -1
        rhs[i] = y[i]
        rhs[i+N] = -1*y[i]

sense = [GRB.GREATER_EQUAL]*2*N
lb = [-GRB.INFINITY] * (C+2)
ub = [GRB.INFINITY] * (C+2)
vtype = [GRB.CONTINUOUS] * (C+2)
sol = [0]*(C+2)
optimum = lp_optimize(2*N, C+2, c, obj_sense, A, sense, rhs, lb, ub, vtype, sol)