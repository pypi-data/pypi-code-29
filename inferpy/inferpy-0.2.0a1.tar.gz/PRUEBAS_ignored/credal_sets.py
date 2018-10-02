import inferpy as inf
import numpy as np

K = 4   # extreme points
N = 1   # num vars
M = 3   # states per var


with inf.ProbModel() as m:

    with inf.replicate(K):
        px = inf.models.Normal(np.ones(M) / M, scale=1)

    with inf.replicate(K*N):

        tx = inf.models.Categorical(logits=np.zeros(K), observed=True)
        x = inf.models.Categorical(probs = px[tx])



train_tx = np.arange(0,K,1).reshape((K,1))



m.compile(infMethod='MCMC')
m.fit({tx : train_tx})


tx.sample()

tx.shape

px[1]

