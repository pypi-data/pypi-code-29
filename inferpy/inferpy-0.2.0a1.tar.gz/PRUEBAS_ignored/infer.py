
import inferpy as inf
import edward as ed
import tensorflow as tf
import numpy as np


sess = ed.get_session()



k=2

N = 1000 # number of observations
# model definition
with inf.ProbModel() as m:

    # observed variable
    with inf.replicate(size=N):
        x = inf.models.Normal(loc=10, scale=1, observed=True, name="x")
        h = inf.models.Normal(loc=k*x, scale=1, observed=False, name="h")



x_train = inf.models.Normal(loc=30/10, scale=10, dim=1).sample(N)


#m.compile()
#m.fit({x.name: x_train})

qh = inf.Qmodel.new_qvar(h, check_observed=False)


x_test = x_train
h_test = k * x_train


#not working
ed.KLqp({h.dist : qh.dist}, data={x.dist : x_test}).run(n_iter=10000)


# this works
map = ed.MAP([h.dist], data={x.dist : x_test})
map.run()
h_pred = sess.run(map.latent_vars.values()[0])


# this works
ed.KLqp({ed.copy(h.dist, {x.dist : x_test}) : qh.dist}, data={}).run()


# not working
ed.KLpq({h.dist : qh.dist}, data={x.dist : x_test}).run()


# works
ed.ReparameterizationKLqp({h.dist : qh.dist}, data={x.dist : x_test}).run()


# not working
ed.ReparameterizationKLKLqp({h.dist : qh.dist}, data={x.dist : x_test}).run()


# works
ed.ReparameterizationEntropyKLqp({h.dist : qh.dist}, data={x.dist : x_test}).run()

#not working
ed.ScoreKLqp({h.dist : qh.dist}, data={x.dist : x_test}).run()

# not working
ed.ScoreKLKLqp({h.dist : qh.dist}, data={x.dist : x_test}).run()


# not working
ed.ScoreEntropyKLqp({h.dist : qh.dist}, data={x.dist : x_test}).run()




h_pred = qh.loc
x_train

err = np.sum(np.power(h_pred - h_test, 2)) / N


for i in range(0,5):
    print(str(h_test[-i])+" -- "+str(h_pred[-i]))



#np.mean(m.posterior(h).loc)