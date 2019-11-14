from environmentFinal import ENVIRONMENT
import constantsFinal as c

class ENVIRONMENTS:
    def __init__(self,numEnvs):
        self.envs = {}
        self.numEnvs = numEnvs
        for e in range(self.numEnvs):
            self.envs[e] = ENVIRONMENT(e)
