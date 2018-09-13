import pandas as _pd
import numpy as _np
from skgrn import data as gsd
from skgrn import inference
from sklearn.linear_model import Lasso
# from sklearn.preprocessing import StandardScaler


def load_data(netpath="gs_networks/random/N10/", datapath="gs_datasets/N10/"):

    network = "Nordling-D20100302-random-N10-L25-ID1446937.json"
    net = gsd.Model.load(network, netpath)
    datasets = gsd.Dataset.load(datapath, wildcard="Nordling-*")

    dataset = {}
    for d in datasets:
        data = gsd.Dataset.load(d)
        dataset[data.name] = data

    return net, dataset


def infer_networks_for_methods(datasets, network, methods, method_configs):

    networkinference = inference.infer_networks(datasets, node_names=network._nodes, methods={"LASSO": Lasso}, zetavec=_np.logspace(-6, 0, num=100), method_configs={})

    aests = []
    xvalt = []
    xvalv = []
    for param_estimates, validation, training in networkinference:

        aests.append(param_estimates)
        xvalv.append(validation)
        xvalt.append(training)

    aests = _pd.concat(aests)
    xvalv = _pd.concat(xvalv)
    xvalt = _pd.concat(xvalt)

    return aests, xvalv, xvalt


def Tjarnberg2013():

    net, datasets = load_data()


if __name__ == '__main__':

    Tjarnberg2013()
