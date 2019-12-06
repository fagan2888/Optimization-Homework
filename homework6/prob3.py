from gurobipy import *


# create a model
m = Model()

# create variables
xa = m.addVar(vtype=GRB.INTEGER, name="xa", lb=0)
xh = m.addVar(vtype=GRB.INTEGER, name="xh", lb=0)
rm = m.addVar(vtype=GRB.BINARY, name="rm", lb=0)
rs = m.addVar(vtype=GRB.BINARY, name="rs", lb=0)


# integrate new variables
m.update()

# set objective
m.setObjective(
    xa*(48000 - 40000) + xh*(46000 - 40000) - rm*1200000 - rs*2800000,
    GRB.MAXIMIZE
)

# add constraints
m.addConstr(xa + xh <= 10000)
m.addConstr(rm*(xh - 3*xa) >= 0)
m.addConstr(rm + rs == 1)

# optimize
m.optimize()
print("Model status: ", m.status)

# print out decision variables
for v in m.getVars():
    print(v.varName, v.x, "\n")

print("-"*15)
print("Obj Value: ", m.objVal)