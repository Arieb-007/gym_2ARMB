import gym
from gym import error, spaces, utils
from gym.utils import seeding
import numpy as np

class B_Bandit(gym.Env):
     def __init__(self,alpha,beta):
        self.alpha = alpha
        self.beta = beta 
            
        
        
     def seed(self,seed):
        np.random.seed(seed)
        
     def step(self,action):
        self.action = action
        stoc = np.random.rand()
        if(self.action==0 and stoc < self.alpha):
            return 1
        elif(self.action==0 and stoc > self.alpha):
            return 0
        if(self.action==1 and stoc < self.beta):
            return 1
        elif(self.action==1 and stoc > self.beta):
            return 0
     def reset(self):
        pass
        
