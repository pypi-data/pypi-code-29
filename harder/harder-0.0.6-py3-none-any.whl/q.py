from harder.gym import GymEnvironment, GymBox
import numpy as np


class Q_base(object):
    
    def __init__(self):
        raise Exception("Overwrite")
    
    def get(self):
        raise Exception("Overwrite")
        
    def get_action_values(self):
        raise Exception("Overwrite")
        
    def update(self):
        raise Exception("Overwrite")
        
        
class Q_dict(Q_base):
    
    def __init__(self, env: GymEnvironment, initial_value=0.0):
        if isinstance(env.observation_space, GymBox) or isinstance(env.action_space, GymBox):
            raise Exception("Only works with discrete spaces")
        self._dictionary = {}
        for key in range(env.observation_space.size()):
            self._dictionary[key] = np.ones(env.action_space.size()) * initial_value
            
    def get(self, state, action):
        return self._dictionary[state][action]
    
    def get_action_values(self, state):
        return self._dictionary[state]
    
    def update(self, state, action, value):
        self._dictionary[state][action] += value