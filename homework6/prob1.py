from gurobipy import *


# create a model
m = Model()

# create variables
x11 = m.addVar(vtype=GRB.CONTINUOUS, name="x11", lb=0)
x12 = m.addVar(vtype=GRB.CONTINUOUS, name="x12", lb=0)
x21 = m.addVar(vtype=GRB.CONTINUOUS, name="x21", lb=0)
x23 = m.addVar(vtype=GRB.CONTINUOUS, name="x23", lb=0)
x33 = m.addVar(vtype=GRB.CONTINUOUS, name="x33", lb=0)
x34 = m.addVar(vtype=GRB.CONTINUOUS, name="x34", lb=0)
x43 = m.addVar(vtype=GRB.CONTINUOUS, name="x43", lb=0)
x54 = m.addVar(vtype=GRB.CONTINUOUS, name="x54", lb=0)
y1 = m.addVar(vtype=GRB.BINARY, name="y1", lb=0, ub=1)
y2 = m.addVar(vtype=GRB.BINARY, name="y2", lb=0, ub=1)
y3 = m.addVar(vtype=GRB.BINARY, name="y3", lb=0, ub=1)
y4 = m.addVar(vtype=GRB.BINARY, name="y4", lb=0, ub=1)
y5 = m.addVar(vtype=GRB.BINARY, name="y5", lb=0, ub=1)


# integrate new variables
m.update()

# set objective
m.setObjective(
    190*x11 + 200*x12 + 100*x21 + 300*x23 + 400*x33 + 150*x34 + 570*x43 + 70*x54 \
    - (1000*y1 + 3000*y2 + 700*y3 + 2000*y4 + 1500*y5 \
    + 102*(x11 + x21) + 88*(x12) + 157*(x23 + x33 + x43) + 234*(x34 + x54)),
    GRB.MAXIMIZE
)

# add constraints
m.addConstr(x11 <= 30*y1)
m.addConstr(x12 <= 30*y1)
m.addConstr(x21 <= 30*y2)
m.addConstr(x23 <= 30*y2)
m.addConstr(x33 <= 30*y3)
m.addConstr(x34 <= 30*y3)
m.addConstr(x43 <= 30*y4)
m.addConstr(x54 <= 30*y5)
m.addConstr(x11 + x12 + x21 + x23 + x33 + x34 + x43 + x54 <= 100)

# optimize
m.optimize()
print("Model status: ", m.status)

# print out decision variables
for v in m.getVars():
    print(v.varName, v.x, "\n")

print("-"*15)
print("Obj Value: ", m.objVal)


'''
x11 10.0
x12 30.0
x21 0.0
x23 0.0
x33 30.0
x34 0.0
x43 30.0
x54 0.0
y1 1.0
y2 0.0
y3 1.0
y4 1.0
y5 0.0
---------------
Obj Value:  20220.0
'''