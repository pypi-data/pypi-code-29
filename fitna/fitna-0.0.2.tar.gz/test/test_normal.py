import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import multivariate_normal, norm

x = np.linspace(0, 1, 100)
y = multivariate_normal.pdf(x, mean=2, cov=0.5)

fig, axes = plt.subplots(1, 1)

#myfig = plt.figure()
#subplot = myfig.add_subplot(1, 1, 1)
#axes[0, 0].plot(x, y)


def sigmoid(x):
    return (2 / (1 + np.exp(-x*5)) - 1)

#y = np.log(x) / np.log(500)
y = sigmoid(x)

axes.plot(x, y)

#gaus_mean = 2.5
#gaus_cov = 0.5
#gaus_mean = [2.5, 2.5]
#gaus_cov = [[1, 0.5], [0.5, 1]]

#random_norm = multivariate_normal.rvs(gaus_mean, gaus_cov, 10000)

#print(type(random_norm))
#print(random_norm)
#print(random_norm.T)
#print(random_norm.T[0])
#print(random_norm.T[1])

#axes[1, 0].hist(random_norm, 50, density=True, histtype='bar')

#axes[1, 1].hist2d(random_norm.T[0], random_norm.T[1], 50)


#x, y = np.mgrid[-1:1:.01, -1:1:.01]
#pos = np.dstack((x, y))
##rv = multivariate_normal([0.5, -0.2], [[2.0, 0.3], [0.3, 0.5]])
#rv = multivariate_normal(0.5, 1)
#fig2 = plt.figure()
#ax2 = fig2.add_subplot(111)
##ax2.contourf(x, y, rv.pdf(pos))

plt.show()
