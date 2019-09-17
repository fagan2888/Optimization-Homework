from gurobipy import *


# create a model
m = Model("problem 1")

# create variables 
# x1 := 1000 barrels of oil
# x2 := 1000 barrels of aviation fuel
# x3 := 1000 barrels of heating oil
# x4 := 1000 barrels of processed aviation fuel
# x5 := 1000 barrels of processed heating oil
x1 = m.addVar(vtype=GRB.CONTINUOUS, name="x1", lb=0)
x2 = m.addVar(vtype=GRB.CONTINUOUS, name="x2", lb=0)
x3 = m.addVar(vtype=GRB.CONTINUOUS, name="x3", lb=0)
x4 = m.addVar(vtype=GRB.CONTINUOUS, name="x4", lb=0)
x5 = m.addVar(vtype=GRB.CONTINUOUS, name="x5", lb=0)

# integrate new variables
m.update()

# set objective
m.setObjective(
    -40*x1 + 60*(x2-x4) + 40*(x3-x5) + 130*x4 + 90*x5,
    GRB.MAXIMIZE
)

# add constraints
# we can only buy 20,000 barrels of oil a day
m.addConstr(x1 <= 20, "c0")
# 1000 barrels of oil can yields 500 barrels of aviation fuel
# and 500 barrels of heating oil
m.addConstr(0.5*x1 - x2 >= 0, "c1")
m.addConstr(0.5*x1 - x3 >= 0, "c2")
# we only have 8hrs cracker time per day
m.addConstr(60*x4 + 45*x5 <= 60*8, "c3")
# cracked aviation fuel < aviation fuel
m.addConstr(x2 - x4 >= 0, "c4")
# cracked heating oil < heating oil
m.addConstr(x3 - x5 >= 0, "c5")

# optimize
m.optimize()
print("Model status: ", m.status)

# print out decision variables
for v in m.getVars():
    print(v.varName, v.x, "\n")

print("-"*15)
print("Obj Value: ", m.objVal)
