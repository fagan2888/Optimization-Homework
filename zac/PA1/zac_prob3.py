from gurobipy import *


# create a model
m = Model()

# create variables
t1 = m.addVar(vtype=GRB.CONTINUOUS, name="t1", lb=0)
t2 = m.addVar(vtype=GRB.CONTINUOUS, name="t2", lb=0)
t3 = m.addVar(vtype=GRB.CONTINUOUS, name="t3", lb=0)
t4 = m.addVar(vtype=GRB.CONTINUOUS, name="t4", lb=0)
t5 = m.addVar(vtype=GRB.CONTINUOUS, name="t5", lb=0)
t6 = m.addVar(vtype=GRB.CONTINUOUS, name="t6", lb=0)
t7 = m.addVar(vtype=GRB.CONTINUOUS, name="t7", lb=0)
t8 = m.addVar(vtype=GRB.CONTINUOUS, name="t8", lb=0)
t9 = m.addVar(vtype=GRB.CONTINUOUS, name="t9", lb=0)
t10 = m.addVar(vtype=GRB.CONTINUOUS, name="t10", lb=0)
t11 = m.addVar(vtype=GRB.CONTINUOUS, name="t11", lb=0)
t12 = m.addVar(vtype=GRB.CONTINUOUS, name="t12", lb=0)
t13 = m.addVar(vtype=GRB.CONTINUOUS, name="t13", lb=0)


# integrate new variables
m.update()

# set objective
m.setObjective(
    -1*(t1 + 2*t2 + 3*t3 + 4*t4 + 2*t5 + t6 + 2*t7 + 6*t8 + 10*t9 + 5*t10 + 3*t11 + 3*t12 + 2*t13),
    GRB.MINIMIZE
)

# add constraints 
m.addConstr(t4 + t3 + t1 == 1)
m.addConstr(t7 - t4 == 0)
m.addConstr(t6 - t2 - t3 == 0)
m.addConstr(t2 + t5 - t1 == 0)
m.addConstr(t10 - t6 - t7 == 0)
m.addConstr(t8 + t9 - t5 == 0)
m.addConstr(t11 + t12 - t10 - t8 == 0)
m.addConstr(t13 - t12 == 0)
m.addConstr(-1*t13 - t11 - t9 == -1)

# optimize
m.optimize()
print("Model status: ", m.status)

# print out decision variables
for v in m.getVars():
    print(v.varName, v.x, "\n")

print("-"*15)
print("Obj Value: ", m.objVal)



############################
############################
############################
# Dual

# create a model
m = Model()

# create variables
ys = m.addVar(vtype=GRB.CONTINUOUS, name="ys", lb=-0)
yt = m.addVar(vtype=GRB.CONTINUOUS, name="yt", lb=-0)
ya = m.addVar(vtype=GRB.CONTINUOUS, name="ya", lb=-0)
yb = m.addVar(vtype=GRB.CONTINUOUS, name="yb", lb=-0)
yc = m.addVar(vtype=GRB.CONTINUOUS, name="yc", lb=-0)
yd = m.addVar(vtype=GRB.CONTINUOUS, name="yd", lb=-0)
ye = m.addVar(vtype=GRB.CONTINUOUS, name="ye", lb=-0)
yf = m.addVar(vtype=GRB.CONTINUOUS, name="yf", lb=-0)
yg = m.addVar(vtype=GRB.CONTINUOUS, name="yg", lb=-0)


# integrate new variables
m.update()

# set objective
m.setObjective(
    yt - ys,
    GRB.MINIMIZE
)

# add constraints 
m.addConstr(-1*ys + yc >= 1)
m.addConstr(-1*yc + yb >= 2)
m.addConstr(-1*ys + yb >= 3)
m.addConstr(-1*ys + ya >= 4)
m.addConstr(-1*yc + ye >= 2)
m.addConstr(-1*yb + yd >= 1)
m.addConstr(-1*ya + yd >= 2)
m.addConstr(-1*yc + yf >= 6)
m.addConstr(-1*yc + yt >= 10)
m.addConstr(-1*yd + yf >= 5)
m.addConstr(-1*yf + yt >= 3)
m.addConstr(-1*yf + yg >= 3)
m.addConstr(-1*yg + yt >= 2)


# optimize
m.optimize()
print("Model status: ", m.status)

# print out decision variables
for v in m.getVars():
    print(v.varName, v.x, "\n")

print("-"*15)
print("Obj Value: ", m.objVal)



