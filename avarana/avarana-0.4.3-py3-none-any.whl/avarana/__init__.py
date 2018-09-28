# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 13:06:35 2018

@author: hrajiv
"""
from keras.models import Sequential
from keras.layers import Dense
import pandas as pd
import sys
import numpy as np
import xgboost
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.metrics import explained_variance_score
#from sklearn.model_selection import GridSearchCV  

name='avarana'

def parser(x):
	return pd.datetime.strptime(x, '%Y%m%d')

def lag(array, start_index, end_index, lag):
    lag_start_index = start_index-lag
    lag_end_index = end_index-lag
    return array[lag_start_index:lag_end_index]

def mean_absolute_percentage_error(y_true, y_pred): 
    y_true[y_true==0] = y_true[y_true>0].min() 
    h1 = np.abs(y_true - y_pred)
    h2 = np.divide(h1, y_true)
    return np.mean(h2)

def weighted_absolute_percentage_error(y_true, y_pred): 
    return np.abs(y_true - y_pred).sum()/y_true.sum()

def nnet_regressor(X, Y, X_test=[], Y_test=[], 
                   hidden_layers=[], activation='relu',
                   loss='mape',optimize=False):
    
    if type(hidden_layers) is not list:
        print("Hidden layers must be a list")
        sys.exit(0)
        
    model = Sequential()
    
    if len(hidden_layers) > 0 and np.sum(hidden_layers) > 0:
        first_layer = 0
        for layer_size in hidden_layers:
            if layer_size > 0 and first_layer == 0:
                model.add(Dense(layer_size, input_dim=X.shape[1], activation=activation))
                first_layer = 1
            elif layer_size > 0:
                model.add(Dense(layer_size, activation=activation))
        model.add(Dense(1, activation='linear')) #hard coded to 1 output layer
    else:
        model.add(Dense(1, input_dim=X.shape[1], activation='linear')) #hard coded to 1 output layer

    model.compile(loss=loss, optimizer='adam')
    
#    if optimize==True:
#        last_min_mape = 100
#        last_min_layer = []
#        
#        hidden_layers = []
#        for h in range(0,X.shape[1]):
#            hidden_layers.append(0)
#            for i in range(0,len(X)+1): 
#                hidden_layers[h] = i
#                model, predictions, mape = nnet_regressor(X,Y,X_test,Y_test,
#                                                        hidden_layers,activation=activation)
#                if mape < last_min_mape:
#                    last_min_layer = hidden_layers
#                    last_min_mape = mape
#        
#        print('Min layer size = ',last_min_layer, ' last min MAPE= ', last_min_mape)
    
    model.fit(X, Y, batch_size=len(Y), epochs=1000, verbose=0)
    
#    Set defaults if there is no test period in the inputs
    predictions = []
    mape = 0
    
    if len(X_test) > 0:
        predictions = model.predict(X_test).ravel()
        
        error = mean_squared_error(Y_test, predictions)
        mape = mean_absolute_percentage_error(Y_test, predictions)
        wape = weighted_absolute_percentage_error(Y_test, predictions)
        r2 = r2_score(Y_test, predictions)
        print('Hidden layers: ',hidden_layers,' R2: %.3f Test MSE: %.3f ~MAPE: %.6f WAPE: %.3f' % (r2, error, mape, wape))    
    
    return model, predictions, mape;

# define base model
def baseline_model():
	# create model
	model = Sequential()
	model.add(Dense(5, input_dim=5, kernel_initializer='normal', activation='relu'))
	model.add(Dense(1, kernel_initializer='normal'))
	# Compile model
	model.compile(loss='mape', optimizer='adam')
	return model

# XGB Configuration
def xgb_wrapper(X, Y, X_test, Y_test):
    xgb = xgboost.XGBRegressor(n_estimators=100, 
                           learning_rate=0.1, 
                           gamma=0.1, 
                           subsample=0.8,
                           colsample_bytree=0.75, 
                           max_depth=3,
                           min_child_weight=1)

    xgb.fit(X,Y)
    predictions = xgb.predict(X_test)
    mape = mean_absolute_percentage_error(Y_test.sale_qty,predictions)
    evs = explained_variance_score(predictions, Y_test)
    return xgb, predictions, mape, evs