from gurobipy import *


# create a model
m = Model("problem 2")

# create variables
# xi, j := represents method i for j product (gas or heating oil)
x1 = m.addVar(vtype=GRB.CONTINUOUS, name="x1", lb=0)
x2 = m.addVar(vtype=GRB.CONTINUOUS, name="x2", lb=0)

# integrate new variables
m.update()

# set objective
m.setObjective(
    2*x1 + 3*x2,
    GRB.MAXIMIZE
)

# add constraints 
m.addConstr(0.5*x1 + 0.25*x2 <= 4)
m.addConstr(x1 + 3*x2 >= 20)
m.addConstr(x1 + x2 == 4)

# optimize
m.optimize()
print("Model status: ", m.status)

# print out decision variables
for v in m.getVars():
    print(v.varName, v.x, "\n")

print("-"*15)
print("Obj Value: ", m.objVal)
