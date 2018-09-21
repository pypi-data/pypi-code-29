import gym
from gym.spaces import Box, Discrete


class GymEnvironment(object):
    
    def __init__(self, env):
        self.observation_space = GymSpace.create_space(env.observation_space)
        self.action_space = GymSpace.create_space(env.action_space)
        
class GymSpace(object):
    
    @staticmethod
    def create_space(space):
        if isinstance(space, Box):
            return GymBox(space)
        if isinstance(space, Discrete):
            return GymDiscrete(space)
        raise Exception("Wrong space class.")
        
class GymBox(object):
    
    def __init__(self, space: Box):
        self.space = space
        
    def size(self):
        return self.space.shape
    
    def highs(self):
        return self.space.high
    
    def lows(self):
        return self.space.low
    
    def bounds(self):
        return list(zip(self.space.low, self.space.high))
    
    def sample(self):
        return self.space.sample()
        
class GymDiscrete(object):

    def __init__(self, space: Discrete):
        self.space = space
        
    def size(self):
        return self.space.n
    
    def sample(self):
        return self.space.sample()