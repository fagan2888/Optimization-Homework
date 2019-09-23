from gurobipy import *


# create a model
m = Model("problem 4")

# create variables
# xi, j := represents method i for j product (gas or heating oil)
x1g = m.addVar(vtype=GRB.CONTINUOUS, name="x1g", lb=0)
x2g = m.addVar(vtype=GRB.CONTINUOUS, name="x2g", lb=0)
x3g = m.addVar(vtype=GRB.CONTINUOUS, name="x3g", lb=0)
x1h = m.addVar(vtype=GRB.CONTINUOUS, name="x1h", lb=0)
x2h = m.addVar(vtype=GRB.CONTINUOUS, name="x2h", lb=0)
x3h = m.addVar(vtype=GRB.CONTINUOUS, name="x3h", lb=0)

# integrate new variables
m.update()

# set objective
m.setObjective(
    14.75*x1g + 8.3*x2g + 4.05*x3g + 3.55*x1h + 1.5*x2h + (-0.15)*x3h,
    GRB.MAXIMIZE
)

# add constraints 
m.addConstr(x1g + x2g + x3g + x1h + x2h + x3h <= 2000, "c1")
m.addConstr(x1g + 0.2*x2g + 0.4*x3g >= 0, "c2")
m.addConstr(4.2*x1h + 2.2*x2h + 1.6*x3h >= 0, "c3")

# optimize
m.optimize()
print("Model status: ", m.status)

# print out decision variables
for v in m.getVars():
    print(v.varName, v.x, "\n")

print("-"*15)
print("Obj Value: ", m.objVal)
