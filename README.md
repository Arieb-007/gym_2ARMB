# gym_2ARMB
This is part(i) of Que 1 of CS698R Assignment 1. <br />
(i)In OpenAI Gym create the environment for 2-armed Bernoulli Bandit. The environment should take α
and β as input parameters and simulate 2-armed bandit accordingly. Once you have implemented the
environment, run it using different values of α and β to make sure it is executing as expected. For, example,
you can try with (α, β) = (0, 0),(1, 0),(0, 1),(1, 1),(0.5, 0.5), etc. Report about your test cases and how
they point towards the correct implementation. You can also report about your general observations.<\br>
You can get the results by directly running the code below <br />

```
gym_2RMB/
  README.md
  setup.py
  gym_2ARMB/
    __init__.py
    envs/
      __init__.py
      BB2ARM.py
      

```


		
```
         from gym_2ARMB import B_Bandit 
	 import numpy as np
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

```
reward_matrix = array([[299863., 150228.],
       [       199585., 350324.]])
```
