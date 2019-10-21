from gurobipy import *


# create a model
m = Model("problem 4")

# create variables
y1 = m.addVar(vtype=GRB.CONTINUOUS, name="y1", lb=0)
y2 = m.addVar(vtype=GRB.CONTINUOUS, name="y2", lb=0)
y3 = m.addVar(vtype=GRB.CONTINUOUS, name="y3", lb=0)
y4 = m.addVar(vtype=GRB.CONTINUOUS, name="y4", lb=0)


# integrate new variables
m.update()

# set objective
m.setObjective(
    y4,
    GRB.MINIMIZE
)

# add constraints 
m.addConstr(y2 - y3 - y4 <= 0)
m.addConstr(-1*y1 + y3 - y4 <= 0)
m.addConstr(y1 - y2 - y4 <= 0)
m.addConstr(y1 + y2 + y3 == 1)

# optimize
m.optimize()
print("Model status: ", m.status)

# print out decision variables
for v in m.getVars():
    print(v.varName, v.x, "\n")

print("-"*15)
print("Obj Value: ", m.objVal)
