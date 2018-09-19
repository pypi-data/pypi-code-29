# Perceptron class

import numpy as np
from random import choice
import matplotlib.pyplot as plt


class Perceptron:
    def __init__(self):
        self.w = []

    # train the model to fit the training data X to its correct labels y
    def train(self, X, y, max_itr=10**6):
        '''
        Train a perceptron model given a set of training data
        :param training_data: A list of data points, where training_data[0]
        contains the data points and training_data[1] contains the labels.
        Labels are +1/-1.
        :return: learned model vector
        '''

        model_size = X.shape[1]
        # select random starting weights
        w = np.random.rand(model_size) 
        

        for i in range(0,max_itr):
            # compute results according to the hypothesis
            res = np.sign(np.matmul(X,w))
            # get incorrect predictions (you can get the indices)
            misclass_idx = np.where(res!=y)[0]
            # Check the convergence criteria (if there is no misclassified
            # points, the PLA is converged and we can stop.)
            if len(misclass_idx) == 0:
                break
            # Pick one misclassified example.
            ex_idx = choice(misclass_idx)
            ex = X[ex_idx,:]
            # Update the weight vector with perceptron update rule
            w = np.add(w,(ex * y[ex_idx]))


        self.w = w
        return w

    
    # test the model on unseen data
    def test(self, X, y):
        pass
