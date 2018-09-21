from mapmatching_benchmark.init import config

import numpy as np
import matplotlib.pyplot as plt

from mapmatching_benchmark.results import plot_data, Algorithm

def autolabel(rects):
	for rect in rects:
		h = rect.get_height()
		ax.text(rect.get_x()+rect.get_width()/2., 1.05*h, '%d'%int(h),
				ha='center', va='bottom')



# plot
fig = plt.figure(figsize=(4, 3))
ax = fig.add_subplot(111)

width = 2
index = 0
xtickstep = 10
xticks = np.array(list(range(1 * xtickstep, (len(plot_data[Algorithm.HMM][:,2]) + 1) * xtickstep, xtickstep)))
ax.set_xticklabels([int(x) for x in plot_data[Algorithm.HMM][:,2]])
ax.set_xticks(xticks)

bars = []
legend_data = []
legend_labels = []
shift = [-0.75 * width, 0, 0.75 * width]
for algorithm, periods in plot_data.items():
	non_zero_periods = periods[np.all(periods > 0, axis=1)]

	# ax.plot(non_zero_periods[:,2], non_zero_periods[:,0], marker=algorithm.symbol,
	# 			c=algorithm.color)
	# shift = width / 4 * 3 if index == 1 else - width / 2
	bar = ax.bar(xticks + shift[index], periods[:,0], width, color=algorithm.color)
	bars.append(bar)
	legend_data.append(bar[0])
	legend_labels.append(algorithm.label)
	index += 1

ax.set_xlabel('Period length')
ax.set_ylabel('Route mismatch Fraction')
ax.legend( legend_data, legend_labels)
# for bar in bars:
# 	autolabel(bar)
# for conf, content in record_csv_content:

plt.savefig(config.images.accuracy_period, bbox_inches='tight', transparent=True)

plt.show()