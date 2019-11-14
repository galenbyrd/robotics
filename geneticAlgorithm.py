from environments import ENVIRONMENTS
from population import POPULATION
import constants as c

envs = ENVIRONMENTS(c.numEnvs)
parents = POPULATION(c.popSize)
parents.Initialize()
parents.Evaluate(envs,True)
print(0),
parents.Print()

for g in range(1,c.numGens):
    children = POPULATION(c.popSize)
    children.Fill_From(parents)
    children.Evaluate(envs,True)
    print(g),
    children.Print()
    parents.ReplaceWith(children)

best=0
for i in parents.p:
    if (parents.p[i].fitness>parents.p[best].fitness):
        best=i
for e in range(envs.numEnvs):
    parents.p[best].Start_Evaluation(envs.envs[e],False)

