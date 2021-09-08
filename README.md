# gym_2ARMB
This is part(i) of Que 1 of CS698R Assignment 1. <br />
(i)In OpenAI Gym create the environment for 2-armed Bernoulli Bandit. The environment should take α
and β as input parameters and simulate 2-armed bandit accordingly. Once you have implemented the
environment, run it using different values of α and β to make sure it is executing as expected. For, example,
you can try with (α, β) = (0, 0),(1, 0),(0, 1),(1, 1),(0.5, 0.5), etc. Report about your test cases and how
they point towards the correct implementation. You can also report about your general observations.<\br>
You can get the results by directly running the code below <br />



<pre>
  <code>
	
     import gym
     from gym import error, spaces, utils
     from gym.utils import seeding
     import numpy as np

     class B_Bandit:
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
      </code>
		</pre>
		
		
```

         episodes = 1000000  #no of episodes
         action_space = 2
         alpha = .4
         beta = .7
         Q_est = np.zeros([episodes]) 
         Q_a = np.zeros([action_space])
         reward_matrix = np.zeros([2,action_space])   #reward matrix shows the statistics for (reward,chosen action)
         N = np.zeros([action_space])   # 2 arms

         env = B_Bandit(alpha,beta)

         for e in range(episodes):
            env.seed(e)                       #using episode number as seed
            action = np.random.randint(2)
            reward = env.step(action)          
            N[action]+=1
            reward_matrix[reward,action]+=1
	
   
```
