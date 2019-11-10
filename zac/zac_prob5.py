from gurobipy import *


# create a model
m = Model()

# create variables
x1 = m.addVar(vtype=GRB.CONTINUOUS, name="x1", lb=0)
x2 = m.addVar(vtype=GRB.CONTINUOUS, name="x2", lb=0)
x3 = m.addVar(vtype=GRB.CONTINUOUS, name="x3", lb=0)
x4 = m.addVar(vtype=GRB.CONTINUOUS, name="x4", lb=0)
x5 = m.addVar(vtype=GRB.CONTINUOUS, name="x5", lb=0)
x6 = m.addVar(vtype=GRB.CONTINUOUS, name="x6", lb=0)
x7 = m.addVar(vtype=GRB.CONTINUOUS, name="x7", lb=0)
y1 = m.addVar(vtype=GRB.INTEGER, name="y1", lb=0, ub=1)
y2 = m.addVar(vtype=GRB.INTEGER, name="y2", lb=0, ub=1)
y3 = m.addVar(vtype=GRB.INTEGER, name="y3", lb=0, ub=1)
y4 = m.addVar(vtype=GRB.INTEGER, name="y4", lb=0, ub=1)
y5 = m.addVar(vtype=GRB.INTEGER, name="y5", lb=0, ub=1)
y6 = m.addVar(vtype=GRB.INTEGER, name="y6", lb=0, ub=1)
y7 = m.addVar(vtype=GRB.INTEGER, name="y7", lb=0, ub=1)

# integrate new variables
m.update()

# set objective
m.setObjective(
    33*x1 + 30*x2 + 26*x3 + 24*x4 + 19*x5 + 18*x6 + 17*x7 + 1000*(y1 + y2 + y3 + y4 + y5 + y6 + y7),
    GRB.MINIMIZE
)

# add constraints 
m.addConstr(x1 >= 400)
m.addConstr(x1 + x2 >= 700)
m.addConstr(x1 + x2 + x3 >= 1200)
m.addConstr(x1 + x2 + x3 + x4 >= 1900)
m.addConstr(x1 + x2 + x3 + x4 + x5 >= 2100)
m.addConstr(x1 + x2 + x3 + x4 + x5 + x6 >= 2500)
m.addConstr(x1 + x2 + x3 + x4 + x5 + x6 + x7 >= 2700)
m.addConstr(x1 <= 400*y1)
m.addConstr(x2 <= 700*y2)
m.addConstr(x3 <= 1200*y3)
m.addConstr(x4 <= 1900*y4)
m.addConstr(x5 <= 2100*y5)
m.addConstr(x6 <= 2500*y6)
m.addConstr(x7 <= 2700*y7)

# optimize
m.optimize()
print("Model status: ", m.status)

# print out decision variables
for v in m.getVars():
    print(v.varName, v.x, "\n")

print("-"*15)
print("Obj Value: ", m.objVal)