from environmentsFinal import ENVIRONMENTS
from populationFinal import POPULATION
import constantsFinal as c
import pickle
import matplotlib.pyplot as plt

def plotfig(fitness):
    fig1, ax1 = plt.subplots()
    ax1.plot(fitness)
    # DONT FORGET TO CHANGE PLOT TITLE
    ax1.set_title("Fitness of ray-sensing predator over time")
    ax1.set_xlabel("Generation")
    ax1.set_ylabel("Fitness")
    fig1.savefig("RayPrey", bbox_inches='tight')
    plt.close()

fitnessHistory = []
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
    fitnessHistory.append(children.p[0].fitness)
    parents.ReplaceWith(children)

plotfig(fitnessHistory)
#fig1, ax1 = plt.subplots()
#ax1.plot(fitnessHistory)
#ax1.set_title("Fitness evolution over time")
#ax1.set_xlabel("Generation")
#ax1.set_ylabel("Fitness")

best=0
for i in parents.p:
    if (parents.p[i].fitness>parents.p[best].fitness):
        best=i
for e in range(envs.numEnvs):
    parents.p[best].Start_Evaluation(envs.envs[e],False)
pickle.dump(parents.p[best].genome,open('savedRayPredator'+"{0:.3f}".format(parents.p[best].fitness)+'.p','wb'))


