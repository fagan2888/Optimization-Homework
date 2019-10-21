from gurobipy import *


# create a model
m = Model("problem 4")

# create variables
# xi, j := represents method i for j product (gas or heating oil)
y1 = m.addVar(vtype=GRB.CONTINUOUS, name="y1", lb=0)
y2 = m.addVar(vtype=GRB.CONTINUOUS, name="y2", lb=0)
y3 = m.addVar(vtype=GRB.CONTINUOUS, name="y3", lb=0)
y4 = m.addVar(vtype=GRB.CONTINUOUS, name="y4", lb=0)
y5 = m.addVar(vtype=GRB.CONTINUOUS, name="y5", lb=0)

# integrate new variables
m.update()

# set objective
m.setObjective(
    y5,
    GRB.MINIMIZE
)

# add constraints 
m.addConstr(2*y1 - y2 + 3*y3 - 2*y4 - y5 <= 0)
m.addConstr(y1 + 4*y2 - 3*y3 + 0*y4 - y5 <= 0)
m.addConstr(0*y1 - 2*y2 - 1*y3 + 3*y4 - y5 <= 0)
m.addConstr(y1 + y2 + y3 + y4 == 1)

# optimize
m.optimize()
print("Model status: ", m.status)

# print out decision variables
for v in m.getVars():
    print(v.varName, v.x, "\n")

print("-"*15)
print("Obj Value: ", m.objVal)
