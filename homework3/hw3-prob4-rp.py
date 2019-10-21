from gurobipy import *


# create a model
m = Model("problem 4")

# create variables
# xi, j := represents method i for j product (gas or heating oil)
x1 = m.addVar(vtype=GRB.CONTINUOUS, name="x1", lb=0)
x2 = m.addVar(vtype=GRB.CONTINUOUS, name="x2", lb=0)
x3 = m.addVar(vtype=GRB.CONTINUOUS, name="x3", lb=0)
x4 = m.addVar(vtype=GRB.CONTINUOUS, name="x4", lb=0)


# integrate new variables
m.update()

# set objective
m.setObjective(
    x4,
    GRB.MAXIMIZE
)

# add constraints 
m.addConstr(-1*x2 + x3 - x4 >= 0)
m.addConstr(x1 - x3 - x4 >= 0)
m.addConstr(-1*x1 + x2 - x4 >= 0)
m.addConstr(x1 + x2 + x3 == 1)

# optimize
m.optimize()
print("Model status: ", m.status)

# print out decision variables
for v in m.getVars():
    print(v.varName, v.x, "\n")

print("-"*15)
print("Obj Value: ", m.objVal)
