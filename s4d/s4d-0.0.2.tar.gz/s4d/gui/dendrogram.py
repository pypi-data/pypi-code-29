
from matplotlib import pyplot as plot
from matplotlib import ticker
import numpy as np
import scipy.cluster.hierarchy as hac
import copy


def plot_dendrogram(merge, thr, size=(25,6), log=False):
    minv = 0

    def my_formatter(x, pos):
        v = x
        if log:
            v = np.exp(v)
        v -= minv

        return "{:10.3f}".format(v)

    def link(merge, log):
        cluster_lst = list()
        idx = dict()
        qt = dict()
        k=0;
        while merge[k][0] < 0:
            name = merge[k][1]
            cluster_lst.append(name)
            idx[name] = k
            qt[name] = 1
            k += 1

        l = k
        links = np.zeros((l-1, 4))

        while k < len(merge):
            m = merge[k][0]
            name_i = merge[k][1]
            name_j = merge[k][2]
            v_ij = merge[k][3]

            qt[name_i] += 1
            links[m, 0] = idx[name_i]
            links[m, 1] = idx[name_j]
            links[m, 2] = v_ij
            links[m, 3] = qt[name_i]
            idx[name_i] = m+l
            idx[name_j] = -1

            k+= 1

        min = -np.min(links[:,2])+2
        links[:,2] += min

        if log:
            links[:,2] = np.log(links[:,2])

        return cluster_lst, links, min

    merge = copy.deepcopy(merge)

    plot.figure(figsize=size)
    cluster_list, link_mat, minv = link(merge, log)

    t=thr+minv
    if log:
        t = np.log(t)

    dendro_data = hac.dendrogram(link_mat, labels=cluster_list, color_threshold=t)
    for i, d in zip(dendro_data['icoord'], dendro_data['dcoord']):
        x = 0.5 * sum(i[1:3])
        y = d[1]
        v = y
        if log:
            v = np.exp(v)
        v -= minv
        plot.plot(x, y, 'o', c="b")
        plot.annotate("{:10.3f}".format(v), (x, y), xytext=(0, -5),
                     textcoords='offset points',
                     va='top', ha='center')

    plot.axhline(y=t, c='r')
    plot.annotate("{:10.3f}".format(thr), (0, t), xytext=(25, 25),
                 textcoords='offset points',
                     va='top', ha='center')

    ax = plot.gca()
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(my_formatter))

    plot.plot()

    return link_mat, dendro_data