from gurobipy import *


# create a model
m = Model("problem 4")

# create variables
# ci := crude oil used in method i
# gi := barrels of i grade gas
# hi := barrels of i grade heating oil
# 628 := barrels of grade 6 products cracked into grade 8 products
# 8210 := barrels of grade 8 products cracked into grade 10 products
xc1 = m.addVar(vtype=GRB.CONTINUOUS, name="xc1", lb=0)
xc2 = m.addVar(vtype=GRB.CONTINUOUS, name="xc2", lb=0)
xc3 = m.addVar(vtype=GRB.CONTINUOUS, name="xc3", lb=0)
xg6 = m.addVar(vtype=GRB.CONTINUOUS, name="xg6", lb=0)
xg8 = m.addVar(vtype=GRB.CONTINUOUS, name="xg8", lb=0)
xg10 = m.addVar(vtype=GRB.CONTINUOUS, name="xg10", lb=0)
xh6 = m.addVar(vtype=GRB.CONTINUOUS, name="xh6", lb=0)
xh8 = m.addVar(vtype=GRB.CONTINUOUS, name="xh8", lb=0)
xh10 = m.addVar(vtype=GRB.CONTINUOUS, name="xh10", lb=0)
x628 = m.addVar(vtype=GRB.CONTINUOUS, name="x628", lb=0)
x8210 = m.addVar(vtype=GRB.CONTINUOUS, name="x8210", lb=0)

# integrate new variables
m.update()

# set objective
m.setObjective(
    12*(xg6 + xg8 + xg10) + 5*(xh6 + xh8 + xh10) - 3.4*xc1 - 3*xc2 - 2.6*xc3 - 1*x628 - 1.5*x8210,
    GRB.MAXIMIZE
)

# add constraints 
m.addConstr(xg6 + xg8 + xg10 <= 2000)
m.addConstr(xh6 + xh8 + xh10 <= 600)
m.addConstr(6*xg6 + 8*xg8 + 10*xg10 >= 9*(xg6 + xg8 + xg10))
m.addConstr(6*xh6 + 8*xh8 + 10*xh10 >= 7*(xh6 + xh8 + xh10))
m.addConstr(0.3*xc1 + 0.4*xc2 + 0.3*xc3 == xg6 + xh6 + x628)
m.addConstr(0.5*xc1 + 0.2*xc2 + 0.3*xc3 == xg8 + xh8 + x8210 - x628)
m.addConstr(0.8*xc1 + 0.4*xc2 + 0.2*xc3 == xg10 + xh10 - x8210)

# optimize
m.optimize()
print("Model status: ", m.status)

# print out decision variables
for v in m.getVars():
    print(v.varName, v.x, "\n")

print("-"*15)
print("Obj Value: ", m.objVal)
