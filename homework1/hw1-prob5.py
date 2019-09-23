from gurobipy import *


# create a model
m = Model("problem 5")

# create variables
# xi := represent i stock
x1 = m.addVar(vtype=GRB.CONTINUOUS, name="x1", lb=0)
x2 = m.addVar(vtype=GRB.CONTINUOUS, name="x2", lb=0)
x3 = m.addVar(vtype=GRB.CONTINUOUS, name="x3", lb=0)
x4 = m.addVar(vtype=GRB.CONTINUOUS, name="x4", lb=0)
x5 = m.addVar(vtype=GRB.CONTINUOUS, name="x5", lb=0)
x6 = m.addVar(vtype=GRB.CONTINUOUS, name="x6", lb=0)
x7 = m.addVar(vtype=GRB.CONTINUOUS, name="x7", lb=0)
x8 = m.addVar(vtype=GRB.CONTINUOUS, name="x8", lb=0)
x9 = m.addVar(vtype=GRB.CONTINUOUS, name="x9", lb=0)
x10 = m.addVar(vtype=GRB.CONTINUOUS, name="x10", lb=0)

# integrate new variables
m.update()

# set objective
m.setObjective(
    36*x1 + 39*x2 + 42*x3 + 45*x4 + 51*x5 + 55*x6 + 63*x7 + 64*x8 + 66*x9 + 70*x10,
    GRB.MAXIMIZE
)

# add constraints 
m.addConstr((100 - x1)*(0.99*30 - 0.3*10) + (100 - x2)*(0.99*34 - 0.3*9) + (100 - x3)*(0.99*43 - 0.3*13) + (100 - x4)*(0.99*47 - 0.3*12) + (100 - x5)*(0.99*49 - 0.3*9) + (100 - x6)*(0.99*53 - 0.3*8) + (100 - x7)*(0.99*60 - 0.3*10) + (100 - x8)*(0.99*62 - 0.3*7) + (100 - x9)*(0.99*64 - 0.3*4) + (100 - x10)*(0.99*66 - 0.3*1) == 30000, "c1")
m.addConstr(x1 <= 100)
m.addConstr(x2 <= 100)
m.addConstr(x3 <= 100)
m.addConstr(x4 <= 100)
m.addConstr(x5 <= 100)
m.addConstr(x6 <= 100)
m.addConstr(x7 <= 100)
m.addConstr(x8 <= 100)
m.addConstr(x9 <= 100)
m.addConstr(x10 <= 100)

# optimize
m.optimize()
print("Model status: ", m.status)

# print out decision variables
for v in m.getVars():
    print(v.varName, v.x, "\n")

print("-"*15)
print("Obj Value: ", m.objVal)
