from gurobipy import *


# create a model
m = Model()

# create variables
s = m.addVar(vtype=GRB.CONTINUOUS, name="s", lb=-GRB.INFINITY)
t = m.addVar(vtype=GRB.CONTINUOUS, name="t", lb=-GRB.INFINITY)
a = m.addVar(vtype=GRB.CONTINUOUS, name="a", lb=-GRB.INFINITY)
b = m.addVar(vtype=GRB.CONTINUOUS, name="b", lb=-GRB.INFINITY)
c = m.addVar(vtype=GRB.CONTINUOUS, name="c", lb=-GRB.INFINITY)


# integrate new variables
m.update()

# set objective
m.setObjective(
    s - t,
    GRB.MAXIMIZE
)

# add constraints 
m.addConstr(s - a <= 5)
m.addConstr(s - b <= 8)
m.addConstr(b - a <= -10)
m.addConstr(a - c <= 2)
m.addConstr(c - b <= 3)
m.addConstr(c - t <= 3)
m.addConstr(b - t <= 4)

# optimize
m.optimize()
print("Model status: ", m.status)

# print out decision variables
for v in m.getVars():
    print(v.varName, v.x, "\n")

print("-"*15)
print("Obj Value: ", m.objVal)
