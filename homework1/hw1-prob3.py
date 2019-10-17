from gurobipy import *


# create a model
m = Model("problem 3")

# create variables
# xi, j := represents method i for j product (gas or heating oil)
x1 = m.addVar(vtype=GRB.CONTINUOUS, name="x1", lb=0)
x2 = m.addVar(vtype=GRB.CONTINUOUS, name="x2", lb=0)
x3 = m.addVar(vtype=GRB.CONTINUOUS, name="x3", lb=0)

# integrate new variables
m.update()

# set objective
m.setObjective(
    3*x1 - 2*x2,
    GRB.MINIMIZE
)

# add constraints 
m.addConstr(3*x1 + x2 - 12 <= 0, "c1")
m.addConstr(3*x1 - 2*x2 - x3 == 12, "c2")
m.addConstr(x1 - 2 >= 0, "c3")

# optimize
m.optimize()
print("Model status: ", m.status)

# print out decision variables
for v in m.getVars():
    print(v.varName, v.x, "\n")

print("-"*15)
print("Obj Value: ", m.objVal)
