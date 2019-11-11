from gurobipy import *


# create a model
m = Model()

# create variables
ab = m.addVar(vtype=GRB.INTEGER, name="ab", ub=40, lb=0)
ac = m.addVar(vtype=GRB.INTEGER, name="ac", ub=30, lb=0)
da = m.addVar(vtype=GRB.INTEGER, name="da", ub=120, lb=0)
ae = m.addVar(vtype=GRB.INTEGER, name="ae", ub=12, lb=0)
af = m.addVar(vtype=GRB.INTEGER, name="af", ub=60, lb=0)
ag = m.addVar(vtype=GRB.INTEGER, name="ag", ub=40, lb=0)
bc = m.addVar(vtype=GRB.INTEGER, name="bc", ub=30, lb=0)
db = m.addVar(vtype=GRB.INTEGER, name="db", ub=70, lb=0)
be = m.addVar(vtype=GRB.INTEGER, name="be", ub=15, lb=0)
fb = m.addVar(vtype=GRB.INTEGER, name="fb", ub=40, lb=0)
gb = m.addVar(vtype=GRB.INTEGER, name="gb", ub=12, lb=0)
cd = m.addVar(vtype=GRB.INTEGER, name="cd", ub=90, lb=0)
ce = m.addVar(vtype=GRB.INTEGER, name="ce", ub=11, lb=0)
fc = m.addVar(vtype=GRB.INTEGER, name="fc", ub=20, lb=0)
cg = m.addVar(vtype=GRB.INTEGER, name="cg", ub=60, lb=0)
de = m.addVar(vtype=GRB.INTEGER, name="de", ub=40, lb=0)
fd = m.addVar(vtype=GRB.INTEGER, name="fd", ub=15, lb=0)
dg = m.addVar(vtype=GRB.INTEGER, name="dg", ub=20, lb=0)
fe = m.addVar(vtype=GRB.INTEGER, name="fe", ub=20, lb=0)
ge = m.addVar(vtype=GRB.INTEGER, name="ge", ub=30, lb=0)
fg = m.addVar(vtype=GRB.INTEGER, name="fg", ub=70, lb=0)

# integrate new variables
m.update()

# set objective
m.setObjective(
    0.003*(ab+ac+da+ae+af+ag+bc+db+be+fb+gb+cd+ce+fc+cg+de+fd+dg+fe+ge+fg),
    GRB.MINIMIZE
)

# add constraints
m.addConstr(-1*(ab + ac + ae + af + ag) + da == -1*160)
m.addConstr(-1*(bc + be) + ab + db + fb + gb == 0)
m.addConstr(-1*(cd + ce + cg) + ac + bc + fc == 0)
m.addConstr(-1*(da + db + de + dg) + cd + fd == 0)
m.addConstr(ae + be + ce + de + fe + ge == 0)
m.addConstr(-1*(fb + fc + fd + fe + fg) + af == 0)
m.addConstr(-1*(gb + ge) + ag + cg + dg + fg == 160)

# optimize
m.optimize()
print("Model status: ", m.status)

# print out decision variables
for v in m.getVars():
    print(v.varName, v.x, "\n")

print("-"*15)
print("Obj Value: ", m.objVal)
