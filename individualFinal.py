import pyrosim
import random
import pickle
import math
import numpy as np
import constantsFinal as c
from robotFinal import ROBOT

class INDIVIDUAL:
    def __init__(self,i,label):
        self.fitness = 0
        self.ID = i
        self.label = label
        if ( self.label == 'prey'):
            #self.genome = pickle.load(open('savedPrey.p','rb'))
            self.genome = 2 * np.random.random_sample((10, 14)) - 1
        else:
            #self.genome = pickle.load(open('savedPredator.p','rb'))
            self.genome = 2 * np.random.random_sample((5, 8)) - 1
            #self.genome = pickle.load(open('Saved Robots/savedPredator1.65.p','rb'))
        
    def Start_Evaluation(self, env, pb):
        self.sim = pyrosim.Simulator( eval_time=c.evalTime, play_blind = pb, play_paused = True)
        self.robot = ROBOT(self.sim,self.genome,self.label)
        env.Send_To( self.sim )
        self.sim.start()

    def Compute_Fitness(self):
        self.sim.wait_to_finish()
        if ( self.label == 'prey'):
            for i in range (4,6):
                DistVec = self.sim.get_sensor_data( sensor_id = self.robot.S[i+4])
                self.fitness += np.mean(DistVec)/40
                ColorVec = self.sim.get_sensor_data( sensor_id = self.robot.S[i+4], svi=1)
                self.fitness += np.mean(ColorVec)
            
##            for i in range (0,8):
##                #x = self.sim.get_sensor_data( sensor_id = self.robot.S[i+4])[-1]
##                #self.fitness += x
##                x = self.sim.get_sensor_data( sensor_id = self.robot.S[i+4])
##                self.fitness += x[-1]
##                add=0
##                for j in range (0,len(x)-1):
##                    if ( x[j]<x[j+1]):
##                        add += 1
##                self.fitness += add/(c.evalTime/5)
        else:
            for i in range (0,1):
                x = self.sim.get_sensor_data( sensor_id = self.robot.S[i+4])[-1]
                self.fitness += x
        del self.robot.S
        del self.sim

    def Mutate(self):
        if ( self.label == 'prey'):
            rowToMutate = random.randint(0,9)
            colToMutate = random.randint(0,9)
        else:
            rowToMutate = random.randint(0,4)
            colToMutate = random.randint(0,7)
        newWeight = random.gauss( self.genome[rowToMutate,colToMutate] , math.fabs(self.genome[rowToMutate,colToMutate]) )
        if newWeight>1:
            self.genome[rowToMutate,colToMutate]=1
        elif newWeight<-1:
            self.genome[rowToMutate,colToMutate]=-1
        else:
            self.genome[rowToMutate,colToMutate]=newWeight

    def Print(self):
        print('['+str(self.ID)+' '+str(self.fitness)+']'),
              
        #print(self.fitness),
