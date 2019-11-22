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
data['b'] = 1
data = pd.concat([data, data], axis=0).reset_index(drop=True)
print(data.head(5))


labelList = data["y"].values.tolist()
data["v"] = [1] * int(data.shape[0]/2) + [-1] * int(data.shape[0]/2)
dataList = data.drop("y", axis=1).values.tolist()


start = time.time()
lp_optimize(
    rows=data.shape[0],
    cols=12,
    c=[0]*11 + [1],
    obj_sense=GRB.MINIMIZE,
    A=dataList,
    sense=[GRB.GREATER_EQUAL] * int(data.shape[0]/2) + [GRB.LESS_EQUAL] * int(data.shape[0]/2),
    rhs=labelList,
    lb=[-GRB.INFINITY] * 12,
    ub=[GRB.INFINITY] * 12,
    vtype=[GRB.CONTINUOUS] * 12,
    solution=[0] * 12
)
end = time.time()
print(end - start)


# Dual
start = time.time()
A_transpose = np.array(dataList).T.tolist()
lp_optimize(
    rows=len(A_transpose),
    cols=len(labelList),
    c=labelList,
    obj_sense=GRB.MAXIMIZE,
    A=A_transpose,
    sense=[GRB.EQUAL] * len(A_transpose),
    rhs=[0]*11 + [1],
    lb=[0] * int(len(labelList) / 2) + [-GRB.INFINITY] * int(len(labelList) / 2),
    ub=[GRB.INFINITY] * int(len(labelList) / 2) + [0] * int(len(labelList) / 2),
    vtype=[GRB.CONTINUOUS] * len(labelList),
    solution=[0] * len(labelList)
)
end = time.time()
print(end - start)