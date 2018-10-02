import inferpy as inf
import tensorflow as tf





sess = inf.get_session()




# p(x|y)

with inf.ProbModel() as m:
    y =  inf.models.Categorical(probs=[0.4,0.6], name="y")
    x = inf.models.Categorical(probs=inf.case({y.equal(0): [0.0, 1.0],
                                               y.equal(1): [1.0, 0.0] }), name="x")

m.sample()





with inf.ProbModel() as m2:
    a = inf.models.Normal(0,1, name="a")
    b = inf.models.Categorical(probs=inf.case({a>0: [0.0, 1.0],
                                               a<=0: [1.0, 0.0]}), name="b")



m2.sample()




with inf.ProbModel() as m3:
    d =  inf.models.Categorical(probs=[0.4,0.6], name="d")
    c = inf.models.Normal(loc=inf.case({d.equal(0): 0.,
                                        d.equal(1): 100.}), scale=1., name="c")


m3.sample()

t = inf.models.Normal(0,5,dim=1)
y = inf.models.Beta([t,0.5], 1)
z =  inf.models.Categorical(probs=[0.4,0.6], name="z")


(x>0).loc


(x and x).sample()

(x>1 and x<10).sample()



type((t>0 and t<0)) # deterministic
type((x and x))     # categorical
type(x>0)           # deterministic

(t and t>0).loc     #normal

(t>0) == False

t





(x > [[0,0,0], [0,0,0]]).loc  # broadcasting is done,




y =  inf.models.Categorical(probs=[0.8,0.2], name="y", dim=2)

p = inf.case({y.equal(0): [0.5, 0.5], y.equal(1): [1.0, 0.0] })



p = tf.constant([0.1,0.8])


p = tf.gather([[0.5, 0.5], [0.1, 0.9]], y.dist)


y.equal([0,0]).loc


p = inf.case_states(y, {0: [0.5, 0.5], 1: [1.0, 0.0] })


#####

y =  inf.models.Categorical(probs=[0.5,0.5], name="y", dim=2)
p = inf.case_states(y, {(0,0): [1.0, 0.0, 0.0, 0.0], (0,1): [0.0, 1.0, 0.0, 0.0],
                        (1, 0): [0.0, 0.0, 1.0, 0.0], (1,1): [0.0, 0.0, 0.0, 1.0]} )


with inf.replicate(size=10):
    x = inf.models.Categorical(probs=p, name="x")


sess.run([y.dist,x.dist])

####

y =  inf.models.Categorical(probs=[0.5,0.5], name="y", dim=1)
z =  inf.models.Categorical(probs=[0.5,0.5], name="z", dim=1)


p = inf.case_states((y,z), {(0,0): [1.0, 0.0, 0.0, 0.0], (0,1): [0.0, 1.0, 0.0, 0.0],
                            (1, 0): [0.0, 0.0, 1.0, 0.0], (1,1): [0.0, 0.0, 0.0, 1.0]} )

with inf.replicate(size=10):
    x = inf.models.Categorical(probs=p, name="x")


sess.run([y.dist, z.dist, x.dist])

####

p = inf.case_states([y,z], {(0,0): [1.0, 0.0, 0.0, 0.0], (0,1): [0.0, 1.0, 0.0, 0.0],
                            (1, 0): [0.0, 0.0, 1.0, 0.0], (1,1): [0.0, 0.0, 0.0, 1.0]} )

with inf.replicate(size=10):
    x = inf.models.Categorical(probs=p, name="x")


sess.run([y.dist, z.dist, x.dist])






tf.shape(p)



x

sess = inf.get_session()

sess.run([y.dist, x.dist])

########
c = t


sess.run(tf.equal(c.base_object,True))


sess.run(tf.equal(z.base_object, 0))



sess.run(t>0)
z==0
sess.run(tf.equal((z==0 and t>0).base_object,True))

(t>0).base_object







t =  inf.models.Categorical(logits=[0,0], name="t")



x = inf.models.Categorical(probs=inf.case({t.equal(0): [0.5, 0.5],
                                           t.equal(1): [1.0, 0.0] }), name="x")




x = inf.models.Categorical(probs=[0.8, 0])

N = 100


s = x.sample(N,tf_run=False)


s = tf.reshape(x.sample(N,tf_run=False), [1,N])
s

import tensorflow as tf


x

tf.reduce_mean(tf.gather(tf.constant([10,100,500]), s)).eval()


