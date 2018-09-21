import random
import numpy as np
from harder.q import Q_base


class Policy(object):
    
    def __init__(self, q: Q_base):
        self._q = q
        
    def act(self, state, epsilon=None):
        if not epsilon or random.random() > epsilon:
            return np.argmax(self._q.get_action_values(state))
        else:
            return random.choice(np.arange(len(self._q.get_action_values(state))))
        
    def get_probs(self, state, epsilon):
        policy_s = np.ones(len(self._q.get_action_values(state))) * epsilon / len(self._q.get_action_values(state))
        best_a = np.argmax(self._q.get_action_values(state))
        policy_s[best_a] = 1 - epsilon + (epsilon / len(self._q.get_action_values(state)))
        return policy_s