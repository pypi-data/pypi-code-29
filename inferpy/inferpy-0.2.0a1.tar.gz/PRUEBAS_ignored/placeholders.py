import edward as ed
import inferpy as inf
from inferpy.models import Normal
import numpy as np

import tensorflow as tf

d, N =  1, 200000




def inf_model(x_train, y_train):
    # model definition
    with inf.ProbModel() as m:

        #define the weights
        w0 = Normal(0,1)
        #with inf.replicate(size=d):
        w = Normal(0, 1)

        # define the generative model
        with inf.replicate(size=N):
            x = Normal(0, 1, observed=True, dim=d)
            #y = Normal(w0 + inf.matmul(x,w), 1.0, observed=True)
            y = Normal(w0 + w*x, 1.0, observed=True)



    data = {x.name: x_train, y.name: y_train}

    # compile and fit the model with training data
    m.compile()
    m.fit(data)

    print(m.posterior([w, w0]))
    return [m.posterior(w).loc, m.posterior(w0).loc]



# toy data generation
y_train = inf.models.Normal(loc=1000, scale=0.1, dim=d).sample(N)
x_train = y_train/1000

#inf_res = inf_model(x_train,y_train)



#
#def ed_model(x_train, y_train):



w = ed.models.Normal(loc=tf.zeros(d), scale=tf.ones(d))
w0 = ed.models.Normal(loc=tf.zeros(1), scale=tf.ones(1))

x = ed.models.Normal(loc=tf.zeros([N,d]), scale=tf.ones([N,d]))
y = ed.models.Normal(loc=ed.dot(x, w) + w0, scale=tf.ones(N))

#qw = ed.models.Normal(loc=tf.get_variable("qw/loc", [d]), scale=1.)
#qw0 = ed.models.Normal(loc=tf.get_variable("qw0/loc", [1]), scale=1.)

x_train = inf.models.Normal(loc=10, scale=5, dim=d).sample(N)
y_train = x_train*1000 + inf.models.Normal(loc=0, scale=5, dim=d).sample(N)

qw = ed.models.Normal(loc=tf.get_variable("qw/loc", [d]),
            scale=tf.nn.softplus(tf.get_variable("qw/scale", [d])))
qw0 = ed.models.Normal(loc=tf.get_variable("qw0/loc", [1]),
            scale=tf.nn.softplus(tf.get_variable("qw0/scale", [1])))


inference = ed.MAP({w: qw, w0: qw0}, data={x: np.reshape(x_train, (N,1)), y: np.reshape(y_train, (N,))})
inference.run()


sess = ed.get_session()
sess.run(qw)
sess.run(qw0)
