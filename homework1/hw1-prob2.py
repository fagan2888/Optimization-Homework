from gurobipy import *


# create a model
m = Model("problem 2")

# create variables
# x1 := oz that process 1 produced
# x2 := oz that process 2 produced
# x3 := hiring hours
x1 = m.addVar(vtype=GRB.CONTINUOUS, name="x1", lb=0)
x2 = m.addVar(vtype=GRB.CONTINUOUS, name="x2", lb=0)
x3 = m.addVar(vtype=GRB.CONTINUOUS, name="x3", lb=0)

# integrate new variables
m.update()

# set objective
m.setObjective(
    5*x1 + 5*x2 - 100*x3,
    GRB.MAXIMIZE
)

# add constraints
# max labors are 20000
# max chemicals are 35000
m.addConstr(1/3*x1 + 2/5*x2 <= 20000, "c1")
m.addConstr(2/3*x1 + 3/5*x2 <= 35000, "c2")
# the number of product should larger than
# the number of sells
m.addConstr(x1 + x2 - 200*x3 - 1000 >= 0, "c3")

# optimize
m.optimize()
print("Model status: ", m.status)

# print out decision variables
for v in m.getVars():
    print(v.varName, v.x, "\n")

print("-"*15)
print("Obj Value: ", m.objVal)
