import pandas as pd
from gurobipy import *

n = 4039
data = pd.read_table('facebook_combined.txt', header=None)
data.columns = ['Edge']
data['weight'] = 1
data['Edge'] = data['Edge'].apply(lambda x: (int(x.split(' ')[0]), int(x.split(' ')[1])))
data.head()


bidirect = data.copy(deep=True)
bidirect['Edge'] = bidirect['Edge'].apply(lambda t: (t[1], t[0]))
bidirect.head()


data = pd.concat([data, bidirect], axis=0)
graph = data.set_index('Edge').to_dict()['weight']
Vertex = [i for i in range(n)]


m = Model()
nw = m.addVars(data['Edge'], vtype=GRB.CONTINUOUS, obj=graph, name="nw", lb=0)
m.modelSense = GRB.MINIMIZE
m.addConstr((nw.sum(0,'*') - nw.sum('*',0) == n - 1), "net supply")
m.addConstrs((nw.sum(i,'*') - nw.sum('*',i) == -1 for i in Vertex[1:]), "net supply")
m.update()

m.optimize()
print('Obj value:', m.objVal)
print('Average exposure time:', m.objVal / n)