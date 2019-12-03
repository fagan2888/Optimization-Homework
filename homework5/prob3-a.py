from gurobipy import *


# create a model
m = Model()

# create variables
sab = m.addVar(vtype=GRB.CONTINUOUS, name="sab", lb=0)
sac = m.addVar(vtype=GRB.CONTINUOUS, name="sac", lb=0)
sae = m.addVar(vtype=GRB.CONTINUOUS, name="sae", lb=0)
sbc = m.addVar(vtype=GRB.CONTINUOUS, name="sbc", lb=0)
sbe = m.addVar(vtype=GRB.CONTINUOUS, name="sbe", lb=0)
sce = m.addVar(vtype=GRB.CONTINUOUS, name="sce", lb=0)
abb = m.addVar(vtype=GRB.CONTINUOUS, name="abb", lb=0)
acc = m.addVar(vtype=GRB.CONTINUOUS, name="acc", lb=0)
aee = m.addVar(vtype=GRB.CONTINUOUS, name="aee", lb=0)
bcc = m.addVar(vtype=GRB.CONTINUOUS, name="bcc", lb=0)
bee = m.addVar(vtype=GRB.CONTINUOUS, name="bee", lb=0)
cee = m.addVar(vtype=GRB.CONTINUOUS, name="cee", lb=0)
aba = m.addVar(vtype=GRB.CONTINUOUS, name="aba", lb=0)
aca = m.addVar(vtype=GRB.CONTINUOUS, name="aca", lb=0)
aea = m.addVar(vtype=GRB.CONTINUOUS, name="aea", lb=0)
bcb = m.addVar(vtype=GRB.CONTINUOUS, name="bcb", lb=0)
beb = m.addVar(vtype=GRB.CONTINUOUS, name="beb", lb=0)
cec = m.addVar(vtype=GRB.CONTINUOUS, name="cec", lb=0)
at = m.addVar(vtype=GRB.CONTINUOUS, name="at", lb=0)
bt = m.addVar(vtype=GRB.CONTINUOUS, name="bt", lb=0)
ct = m.addVar(vtype=GRB.CONTINUOUS, name="ct", lb=0)
et = m.addVar(vtype=GRB.CONTINUOUS, name="et", lb=0)
z = m.addVar(vtype=GRB.CONTINUOUS, name="z", lb=0)


# integrate new variables
m.update()

# set objective
# sum of outflow of s
m.setObjective(
    z, 
    GRB.MAXIMIZE
)

# add constraints
# input/output constraints
m.addConstr(-1*(sab + sac + sae + sbc + sbe + sce) == -z)
m.addConstr(at + bt + ct + et == z)
# capacity constraints
m.addConstr(sab <= 2)
m.addConstr(sac <= 2)
m.addConstr(sae <= 2)
m.addConstr(sbc <= 2)
m.addConstr(sbe <= 2)
m.addConstr(sce <= 2)
m.addConstr(at <= 5)
m.addConstr(bt <= 5)
m.addConstr(ct <= 4)
m.addConstr(et <= 3)
# inflow equals to outflow constraints
m.addConstr(sab == aba + abb)
m.addConstr(sac == aca + acc)
m.addConstr(sae == aea + aee)
m.addConstr(sbc == bcb + bcc)
m.addConstr(sbe == beb + bee)
m.addConstr(sce == cec + cee)
m.addConstr(at == aba + aca + aea)
m.addConstr(bt == abb + bcb + beb)
m.addConstr(ct == acc + bcc + cec)
m.addConstr(et == aee + bee + cee)


# optimize
m.optimize()
print("Model status: ", m.status)

# print out decision variables
for v in m.getVars():
    print(v.varName, v.x, "\n")

print("-"*15)
print("Obj Value: ", m.objVal)