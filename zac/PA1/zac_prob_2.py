import os
import sys
import time
import numpy as np
import pandas as pd
from gurobipy import *
from myMatrixLpSolver import lp_optimize


data = pd.read_table('dataLR.txt', sep=',', header=None)
data.rename(
    columns={0: "y",1: "x1",2: "x2",3: "x3",4: "x4",5: "x5",6: "x6",7: "x7",8: "x8",9: "x9",10: "x10"}, 
    inplace=True
)
N = data.shape[0]


data['b'] = 1
data = pd.concat([data, data], axis=0).reset_index(drop=True)
labelList = data["y"]


data.drop("y", axis=1, inplace=True)
data = data.values
I = np.identity(n=N)
II = np.concatenate((I, np.negative(I)), axis=0)
data = np.concatenate((data, II), axis=1)


start = time.time()
lp_optimize(
    rows=data.shape[0],
    cols=data.shape[1],
    c=[0]*11 + [1]*N,
    obj_sense=GRB.MINIMIZE,
    A=data.tolist(),
    sense=[GRB.GREATER_EQUAL] * int(data.shape[0]/2) + [GRB.LESS_EQUAL] * int(data.shape[0]/2),
    rhs=labelList,
    lb=[-GRB.INFINITY] * (11 + N),
    ub=[GRB.INFINITY] * (11 + N),
    vtype=[GRB.CONTINUOUS] * (11 + N),
    solution=[0]*(11 + N)
)
end = time.time()
print(end - start)



# Dual
start = time.time()
A_transpose = data.T.tolist()
lp_optimize(
    rows=len(A_transpose),
    cols=len(labelList),
    c=labelList,
    obj_sense=GRB.MAXIMIZE,
    A=A_transpose,
    sense=[GRB.EQUAL] * len(A_transpose),
    rhs=[0]*11 + [1]*N,
    lb=[0] * int(len(labelList) / 2) + [-GRB.INFINITY] * int(len(labelList) / 2),
    ub=[GRB.INFINITY] * int(len(labelList) / 2) + [0] * int(len(labelList) / 2),
    vtype=[GRB.CONTINUOUS] * len(labelList),
    solution=[0] * len(labelList)
)
end = time.time()
print(end - start)
