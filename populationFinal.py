from individualFinal import INDIVIDUAL
from robotFinal import ROBOT
import constantsFinal as c
import pyrosim
import copy
import random

class POPULATION:
    def __init__(self,popSize):
        self.p = {}
        self.popSize = popSize

        
    def Print(self):
        for i in self.p:
            self.p[i].Print()
        print('')
            
    def Evaluate(self,envs,pb):
        for i in self.p:
            self.p[i].fitness=0
        for e in range(envs.numEnvs):
            for i in range(0,self.popSize):
                self.p[i].Start_Evaluation(envs.envs[e],pb)
            for i in range(0,self.popSize):
                self.p[i].Compute_Fitness()
                # UN/COMMENT NEXT 2 LINES TO PRINT FITNESS FOR ALL ENVIRONMENTS
                #self.p[i].Print()
            #print('')
        for i in self.p:
            self.p[i].fitness /= envs.numEnvs

    def Mutate(self):
        for i in self.p:
            self.p[i].Mutate()
            self.p[i].Mutate()

    def ReplaceWith(self,other):
        for i in range(0,self.popSize):
            if ( self.p[i].fitness < other.p[i].fitness ):
                self.p[i] = other.p[i]

    def Initialize(self):
        for i in range(0,self.popSize):
            # CHANGE HERE AND ENVIRONMENT LINE 35 TO GO BETWEEN PREDATOR/PREY
            # AND TITLE OF PICKLE IN FINAL
            # THIS ONE IS BEING EVALUATED
            self.p[i] = INDIVIDUAL(i,'prey')
            #self.p[i] = INDIVIDUAL(i,'predator')


    def Fill_From(self , other):
        self.Copy_Best_From(other)
        self.Collect_Children_From(other)

    def Copy_Best_From(self,other):
        best=0
        for i in range(c.popSize):
            if (other.p[i].fitness>other.p[best].fitness):
                best = i
        self.p[0] = copy.deepcopy(other.p[best])



    def Collect_Children_From(self,other):
        for i in range(1,other.popSize):
            winner = other.Winner_Of_Tournament_Selection()
            self.p[i] = copy.deepcopy(winner)
            self.p[i].Mutate()
            
    def Winner_Of_Tournament_Selection(other):
        p1 = random.randint(0,other.popSize-1)
        p2 = random.randint(0,other.popSize-1)
        while (p1==p2):
            p2 = random.randint(0,other.popSize-1)
        if (other.p[p1].fitness>other.p[p2].fitness):
            return other.p[p1]
        else:
            return other.p[p2]
    
################### CODE GRAVE #################

##            self.p[self.popSize+i] = INDIVIDUAL(self.popSize+i,'predator')
##            for i in range(0,self.popSize):
##                self.sim = pyrosim.Simulator( eval_time=c.evalTime, play_blind = pb, play_paused = True)
##                self.prey = ROBOT(self.sim,self.p[i].genome,self.p[i].label)
##                self.predator = ROBOT(self.sim,self.p[self.popSize+i].genome,self.p[self.popSize+i].label)
##                self.sim.start()
##            #for i in range(0,self.popSize):
##                self.sim.wait_to_finish()
##                #for i in range (0,3):
##                x = self.sim.get_sensor_data( sensor_id = self.prey.S[4])[-1]
##                self.p[i].fitness += x
##                x = self.sim.get_sensor_data( sensor_id = self.predator.S[4])[-1]
##                self.p[i+self.popSize].fitness -= x
##                del self.prey.S
##                del self.predator.S
##                del self.sim

##        for i in range(self.popSize,2*self.popSize):
##            if ( self.p[i].fitness < other.p[i].fitness ):
##                self.p[i] = other.p[i]
        
##        best=0
##        for i in range(self.popSize,2*self.popSize):
##            if (other.p[i].fitness>other.p[best].fitness):
##                best = i
##        self.p[c.popSize] = copy.deepcopy(other.p[best])

##        if (random.randint(0,1)==0):
##            p1 = random.randint(0,other.popSize-1)
##            p2 = random.randint(0,other.popSize-1)
##        else:
##            p1 = random.randint(other.popSize,2*other.popSize-1)
##            p2 = random.randint(other.popSize,2*other.popSize-1)
