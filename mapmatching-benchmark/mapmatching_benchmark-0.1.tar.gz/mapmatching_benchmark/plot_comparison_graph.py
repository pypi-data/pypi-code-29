from mapmatching_benchmark.init import config

import numpy as np
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D
from mapmatching_benchmark.results import plot_data

# plot
fig = plt.figure(figsize=(4, 3))
ax = fig.add_subplot(111, projection='3d')

for algorithm, periods in plot_data.items():
	non_zero_periods = periods[np.all(periods > 0, axis=1)]

	ax.scatter(non_zero_periods[:,1] / 1000, non_zero_periods[:,2], non_zero_periods[:,0], marker=algorithm.symbol,
				c=algorithm.color)

ax.set_xlabel('Km per second')
ax.set_ylabel('Period length')
ax.set_zlabel('Route Mismatch Fraction')
# for conf, content in record_csv_content:

plt.savefig(config.images.main_comparison, bbox_inches='tight', transparent=True)

plt.show()