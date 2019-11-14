import constantsFinal as c
from individualFinal import INDIVIDUAL
from robotFinal import ROBOT
import numpy as np
import pickle

class ENVIRONMENT:
    def __init__(self,e):
        self.ID = e

    def Send_To( self,sim ):
        #light = sim.send_box(x=-1, y=0, z=c.L + c.R, length=c.L, width=c.L, height=2*c.R, r=0, g=.5, b=0)
        #sim.send_light_source( body_id = light )
        #predator = ROBOT(sim,2 * np.zeros((8, 8)) - 1,'prey')

        # CHANGE HERE AND POPULATION LINE 64 TO GO BETWEEN PREDATOR/PREY
        #ROBOT(sim,2 * np.zeros((14, 14)) - 1,'prey')
        #ROBOT(sim, pickle.load(open('Saved Robots/savedPredator1.65.p','rb')),'predator')
        #ROBOT(sim,pickle.load(open('Saved Robots/savedPredator1.65.p','rb')),'predator')
        ROBOT(sim,2 * np.zeros((5, 8)) - 1,'predator')
        






        
