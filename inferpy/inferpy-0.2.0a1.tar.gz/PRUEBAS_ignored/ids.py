import inferpy as inf
import tensorflow as tf
import edward as ed
import numpy as np
import tensorflow as tf


## to do: check estructure and minimal
## try an algo
## informational pred of D

class Chance(inf.models.Categorical):

    def __init__(self, probs, parents = None, name="Chance"):
        self.__probs = probs
        self.__parents = parents

        parents = [] if parents is None else parents

        if parents not in ([], np.array([])):
            p = inf.case_states(parents, probs)
        else:
            p = probs


        self.dist = inf.models.Categorical(probs=p, name=name).dist
        self.observed = False

    @property
    def probs(self):
        return self.__probs

    @property
    def parents(self):
        return self.__parents



class Decision(inf.models.Categorical):

    def __init__(self, num_options=2, name="Decision"):
        self.__num_options = num_options

        self.dist = inf.models.Categorical(logits=np.zeros(num_options), name=name).dist
        self.observed = False

    @property
    def num_options(self):
        return self.__num_options





class Utility(inf.models.Categorical):

    def __init__(self, utils=None, parents = None, name="Util"):

        if utils != None:

            self.__utils = utils
            self.__parents = parents



            parents = [] if parents is None else parents

            # Cooper transformation

            k2 = - np.min(utils.values())
            k1 = np.max(utils.values()) + k2

            self.k2 = k2
            self.k1 = k1

            import six

            pv = {}
            for (k, v) in six.iteritems(utils):
                p = (1.0 * np.abs(v + k2) / k1)[0]
                pv.update({k: [1-p, p]})

            p = inf.case_states(parents, pv)

            self.dist = inf.models.Categorical(probs=p, name=name).dist
            self.observed = False


    @property
    def utils(self):
        return self.__utils

    @property
    def parents(self):
        return self.__parents





x = Chance([0.5,0.5])

d = Decision(num_options=2)

#y = Chance(probs = { (0, 0): [1.0, 0.0, 0.0, 0.0],
#                     (0, 1): [0.0, 1.0, 0.0, 0.0],
#                     (1, 0): [0.0, 0.0, 1.0, 0.0],
#                     (1, 1): [0.0, 0.0, 0.0, 1.0]}, parents=[x,d])

sess = inf.get_session()

v = Utility(utils={(0, 0): [10.0],
                  (0, 1): [0.0],
                  (1, 0): [50.0],
                  (1, 1): [-5.0]}, parents=[x, d])




# P(v=1)

def id():
    return str(inf.models.Uniform(0,10000000).sample(1).astype(int)[0,0])


v.probs.shape

s = inf.get_session()

d_obs = inf.models.Categorical(probs=[1,0])
qv = inf.Qmodel.new_qvar(v, qvar_inf_module=inf.models, qvar_type="Categorical", check_observed=False)
#ed.inferences.ReparameterizationKLqp({v.dist : qv.dist}, {d.dist:d_obs.dist}).run(n_iter=1000)
ed.inferences.ReparameterizationKLqp({v.dist : qv.dist}, {d.dist:[0]}).run(n_iter=1000)

putil = (qv.probs/qv.probs.sum())
ud0 = v.k1 * putil[0,1] - v.k2


#ed.inferences.ReparameterizationKLqp({ed.copy(v.dist,{d.dist:d_obs.dist}) : qv.dist}, {}).run()

#ed(ed.copy(v.dist,{d.dist:d_obs.dist}).sample())





d_obs = inf.models.Categorical(probs=[0,1])
qv = inf.Qmodel.new_qvar(v, qvar_inf_module=inf.models, qvar_type="Categorical", check_observed=False)
ed.inferences.ReparameterizationKLqp({v.dist : qv.dist}, {d.dist:[1]}).run(n_iter=10000)
putil = (qv.probs/qv.probs.sum())

ud1 = v.k1 * putil[0,1] - v.k2

print([ud0,ud1])




####



a = Chance([0.5,0.5])

u = Utility(utils={0:[10], 1:[5]}, parents=[a])

qu = inf.Qmodel.new_qvar(u, qvar_inf_module=inf.models, qvar_type="Categorical", check_observed=False)
ed.inferences.ReparameterizationKLqp({u.dist : qu.dist}, {d.dist:[1]}).run(n_iter=1000)

qu.probs

pu = (qu.probs/qu.probs.sum())[0,1]

u_post = u.k1 * pu[0,1] - u.k2

import math
pu = u.k1 * (1/ (1 + math.exp(-qu.logits[0,1]))) - u.k2


with inf.replicate(size=10):
    c = inf.models.Categorical(logits=[0,0,0], dim=5)

c.event_shape


print(u_post)

qu



