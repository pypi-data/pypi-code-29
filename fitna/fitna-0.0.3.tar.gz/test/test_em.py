import fitna
import numpy as np


normal_params = [
    fitna.data.NormalDist(norm=1, mean=np.array([4.5, 4.5]), cov=np.array([[1, -0.5], [-0.5, 1]]), size=10),
    fitna.data.NormalDist(norm=1, mean=np.array([6.0, 7.0]), cov=np.array([[1,  0.5], [ 0.5, 1]]), size=10)
]

normal_mixture = fitna.data.NormalMixture(normal_params)
data_points = normal_mixture.rvs()

print('*** NormalMixture ***')

data_points_combo = np.concatenate(data_points, 1)
print(data_points)
print(data_points_combo)
print(data_points_combo.T)
print('concatenated data shape:', data_points_combo.T.shape)

#data_cov = np.cov(data_points_combo.T)
#print(data_cov)


initial_estimates = [
    fitna.data.NormalDist(norm=0.5, mean=np.array([3.0, 5.0]), cov=np.array([[1, 0.0], [0.0, 1]]) ),
    fitna.data.NormalDist(norm=0.5, mean=np.array([8.0, 8.0]), cov=np.array([[1, 0.5], [0.5, 1]]) )
]


ll_new, all_estimates = fitna.em.do_em(data_points_combo.T, initial_estimates, 1e-6, 5)

print('*** Original params ***')
print(normal_params)

print('*** Initial estimates ***')
print(initial_estimates)

#print('*** All estimates ***')
#print(all_estimates)
