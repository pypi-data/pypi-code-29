# -*- coding: utf-8 -*-
"""
Feb 2018
ADAPTCAST
FORECAST PAKAGE
@author: felipeardilac@gmail.com

"""
#Load utility libraries
# =============================================================================
import array
import random
#Data utilities
#import pandas as pd
import numpy as np

#To plot
# =============================================================================
# from matplotlib import pyplot
# =============================================================================
import matplotlib.pyplot as plt
from matplotlib import gridspec
import matplotlib.colors as colors
# from pandas.tools.plotting import autocorrelation_plot
# ModeL OPERATOR
#from sklearn.linear_model import LinearRegression
#from sklearn.metrics import mean_squared_error
#from math import sqrt



#GA optimization
from deap import algorithms
from deap import base
from deap import creator
from deap import tools



# =============================================================================
    
#CONSTRUCTOR
class AdaptativeOperator:
    
    
    def __init__(self,lagConf=[],window=100,forecasts=100,delta=1):
        #Define the atributes (parameters of the model)
        self.lagConf=lagConf
        self.window=window
        self.forecasts=forecasts
        self.delta=delta #Just 1 for now
        
        #A triky way to pass bay the optimazer
        self.maxLag=[]
        self.gene_length=[]
        self.windowRange=[]
        self.targetData=[]
        self.inputData=[]
        self.test_length=[]
        
        
        
    # =============================================================================
    # ====== FUNCTIONS=======================================================
    # =============================================================================
    # Create a multiple lagged state space of the shape
    # y(t)= f(y(t-1) y(t-2) x(t) x(t-1) x(t-2))    
    def shift(self, data,k):
        x=np.zeros(k, dtype=float)
        x.fill(np.nan)
        return np.hstack((x,data))[0:len(data)].T
    
    def createLags(self, inputData, lagConfiguration):
        fistCol=1
        laggedData=np.zeros(1, dtype=float)
        laggedData.fill(np.nan)
        for i in range(0, lagConfiguration.shape[0]):
            lags=lagConfiguration[i]
            if lags!=0: 
                for j in range(1, lags+1):
                    #names.append(list(data)[i]+" "+str(j))
                    if fistCol==1:
                        #laggedData=inputData.iloc[:,i].shift(j).dropna()
                        laggedData=self.shift(inputData[:,i],j).reshape(-1,1)
                        fistCol=0
                    else:
                        #laggedData=pd.concat([laggedData,inputData.iloc[:,i].shift(j)],axis=1).dropna()
                        laggedData=np.append(laggedData,self.shift(inputData[:,i],j).reshape(-1,1), axis=1)
            
                
        #laggedData.columns=names
        return laggedData
    
    def createLagsOut(self, inputData, lagConfiguration):
        fistCol=1
        laggedData=np.zeros(1, dtype=float)
        laggedData.fill(np.nan)
        for i in range(0, lagConfiguration.shape[0]):
            lags=lagConfiguration[i]
            if lags!=0: 
                for j in range(0, lags):
                    #names.append(list(data)[i]+" "+str(j))
                    if fistCol==1:
                        #laggedData=inputData.iloc[:,i].shift(j).dropna()
                        laggedData=self.shift(inputData[:,i],j).reshape(-1,1)
                        fistCol=0
                    else:
                        #laggedData=pd.concat([laggedData,inputData.iloc[:,i].shift(j)],axis=1).dropna()
                        laggedData=np.append(laggedData,self.shift(inputData[:,i],j).reshape(-1,1), axis=1)
            
                
        #laggedData.columns=names
        return laggedData
    
    
    #Calculate the Root mean squared error
    def rmse(self, target,simdata):
        #Length of the data
        n = len(target)
        #Number of NAs in the data
        nans=np.isnan(target) |  np.isnan(simdata)
        nanNumb=sum(nans)
              # RMSE
        cost = np.sqrt(sum(np.power((target[nans==0] - simdata[nans==0]),2)/(n-nanNumb)))
        return cost
    #Calculate the Normalized Root mean squared error
    def nrmse(self, target,simdata):
        #Length of the data
        n = len(target)
        #Number of NAs in the data
        nans=np.isnan(target) |  np.isnan(simdata)
        nanNumb=sum(nans)
              # NRMSE
        cost = np.sqrt(sum(np.power((target[nans==0] - simdata[nans==0]),2)/(n-nanNumb)))
        cost=cost/np.mean(target[nans==0])
        return cost
    #Calculate the Porcentual Root mean squared error
    def prmse(self, target,simdata):
        #Length of the data
        n = len(target)
        #Number of NAs in the data
        nans=np.isnan(target) |  np.isnan(simdata)
        nanNumb=sum(nans)
              # PRMSE
        cost = np.sqrt(sum(np.power((target[nans==0] - simdata[nans==0]),2)/(n-nanNumb)))
        cost=cost/target[nans==0]
        return cost
    #Calculate Nash–Sutcliffe model efficiency coefficient
    def nash(self, target,simdata):
        #Length of the data
        n = len(target)
        #Number of NAs in the data
        nans=np.isnan(target) |  np.isnan(simdata)
        nanNumb=sum(nans)
              # Nash–Sutcliffe
        cost = np.sqrt(sum(np.power((target[nans==0] - simdata[nans==0]),2)/(n-nanNumb)))
        var=np.sum(np.power((target[nans==0]-np.mean(target[nans==0])),2))
        cost=1-(cost/var)
        return cost
    #Calculate the russian hidrological criteria s/sdelta
    def ssigmadelta(self, target,simdata,delta):
        # Estimate the delta
        i=np.arange(1,len(target) - delta)
        deltas= target[i+delta] - target[i]
    
        # Mean of the deltas
        md = np.nanmean(deltas)
        # SD of the deltas
        sigmadelta = np.nanstd(deltas - md)
        # RMSE
        s=self.rmse(target,simdata)
    
        #S/sigmadelta
        ssd = s/sigmadelta
        cost = ssd
        return cost
    #Fast linear regression method
    def lmFast(self, y,x): 
    #    add col of 1s
        X = np.concatenate((np.ones((len(x),1), dtype=int), x), axis=1)  
        Y = np.array(y).reshape(-1, 1)
    #    take the ones with no nan value
        indexNA=(np.sum(np.isnan(x),axis=1)!=0).reshape(-1, 1) | (np.isnan(y)).reshape(-1, 1)
        indexNA=indexNA.reshape(-1)
    
        X=X[indexNA==0,:]
        Y=Y[indexNA==0]
        
        coef = np.linalg.solve(X.T.dot(X), X.T.dot(Y))    
    #    coef = np.linalg.lstsq(X, Y)[0]
        
    #    print("lm_ok : ",np.allclose(np.dot(X.T.dot(X), coef), X.T.dot(Y)))
        
    
        return coef
    #Predict with Fast linear regression method
    def predictlmFast(self, w,x):
      X = np.concatenate((np.ones((len(x),1), dtype=int), x), axis=1)
      Y=w.T.dot(X.T)
      return Y.reshape(-1)
    # plot Performance
    def plotPerformance(self, target,prediction,delta):
        res=target-prediction
        text1= "RMSE = " + np.array2string(np.round(self.rmse(target,prediction),  decimals= 4)) + " "+"NRMSE = "+ np.array2string(np.round(self.nrmse(target,prediction), decimals = 4)) + " "+"NASH = "+ np.array2string(np.round(self.nash(target,prediction), decimals = 4)) + " "+"S/Sd = "+ np.array2string(np.round(self.ssigmadelta(target,prediction,delta), decimals = 4))
        
        indOK=~np.isnan(target) & ~np.isnan(prediction)
        indOK=indOK.reshape(-1)
        targetOK=target.reshape(-1)[indOK]
        predictionOK=prediction.reshape(-1)[indOK]
        text2= "r = " + np.array2string(np.round(np.corrcoef(targetOK,predictionOK)[0,1],  decimals= 4))
        
        # plot it
        t = np.arange(1, len(target)+1).reshape(-1,1)
        
        fig = plt.figure(figsize=(20, 10))    
        gs = gridspec.GridSpec(2, 2, width_ratios=[3, 1])
        plt.rcParams.update({'font.size': 22})
        ax0 = plt.subplot(gs[0])
        ax0.plot(t,target,marker=".",label='Target')
        ax0.plot(t,prediction,"--",marker=".",color="#B8059A",label='Simuation')
        ax0.scatter(t[t.shape[0]-1],prediction[prediction.shape[0]-1],marker="*",color="#B8059A",s=100,label='Forecast')       
        ax0.set_title(text1)
        ax0.set_xlim([1,np.nanmax(t)+delta])
#        ax0.set_ylim([np.nanmin(target),np.nanmax(target)])
        ax0.legend()
        
        
        ax1 = plt.subplot(gs[1])
        ax1.scatter(target, 
                    prediction,s=10,
                    color="black",marker="o")
        ax1.set_title(text2)
        ax1.set_xlim([np.nanmin(target),np.nanmax(target)])
        ax1.set_ylim([np.nanmin(target),np.nanmax(target)])
        # The regresion fit
        fit=self.lmFast(target.reshape(-1, 1),prediction.reshape(-1, 1)) 
        y1=self.predictlmFast(fit,target.reshape(-1, 1))
        ax1.plot(target,y1,"--",color="#8B008B")
        
        
    
        ax2 = plt.subplot(gs[2])
        #ax2.stem(t,res,color="#05B851",markerfmt=" ")
        ax2.stem(res, markerfmt=' ')
        ax2.set_title("Residuals")
        ax2.set_xlim([1,np.nanmax(t)])
        ax2.set_ylim([np.nanmin(res),np.nanmax(res)])
        
        ax3 = plt.subplot(gs[3])
        n_bins=np.round(np.log(res.shape[0],order=2)+1).astype(int)
    #    n_bins=14
        # N is the count in each bin, bins is the lower-limit of the bin
        N, bins, patches = ax3.hist(res.reshape(-1)[indOK], bins=n_bins)
            # We'll color code by height, but you could use any scalar
        fracs = N.astype(float) / N.max()
       # we need to normalize the data to 0..1 for the full range of the colormap
        norm = colors.Normalize(fracs.min(), fracs.max())
        # Now, we'll loop through our objects and set the color of each accordingly
        for thisfrac, thispatch in zip(fracs, patches):
            #color = plt.cm.viridis(norm(thisfrac))
            color = plt.cm.viridis(norm(thisfrac)*(2/3))
            thispatch.set_facecolor(color)
        ax3.set_title("Hist Residuals")
        
        plt.tight_layout()
        return plt
    # Interpolate a dataset using a linear model of
    # all variables in the set
    def interpolate(self, data):  
        # Create a copy to interpolate
        InterpData=data
        for i in np.arange(0,data.shape[1]):
            # index of missing values
            indexNA=np.isnan(data[:,i])
            if np.sum(indexNA)!=0:
                # Create a liner model
                y_ok=data[indexNA==0,i]
                x=np.delete(data, np.s_[i], axis=1) 
                x_ok=x[indexNA==0,:]
                x_nan=x[indexNA==1,:]
                fit1=self.lmFast(y_ok,x_ok)            
                # interpolate
                tInerp1=self.predictlmFast(fit1, x_nan)
        
                # update the df with the interpolated values
                InterpData[indexNA,i]=tInerp1
        
                tInerp2=InterpData[:,i]
                # THE REST UNABLE TO BE INTERPOLATED
                if np.sum(np.isnan(tInerp2))!=0:
                    
                           
                    indexNA=np.isnan(tInerp2)
                    index=np.arange(0,tInerp2.shape[0]) 
                
                    tInerp2[indexNA] =np.interp(index[indexNA==1],index[indexNA==0], tInerp2[indexNA==0])
                    # update the df with the interpolated values
                    InterpData[:,i]=tInerp2
            
        return InterpData
    
    #AppLy adaptative operator for forecast
    def predict(self, targetData,inputData,lagConf,window,delta,numberCrossVal):
        
        # Parameters
    # =============================================================================
    #     inputData=input
    #     targetData=target
    # =============================================================================
        lagConfiguration=lagConf
        windowSize=window
        numberOfForecasts=numberCrossVal
        
        # target+input data
        # (it's not cheating because it use only the lags)
        allData=np.append(targetData,inputData,axis=1)
        inputLagedData=self.createLags(allData,lagConfiguration)
        # trim the imput if the delta is > 1
        if delta>1:
            inputLagedData=inputLagedData[:inputLagedData.shape[0]-(delta-1)]
            targetData=targetData[(delta-1):]
            
        
        # target+laged data      
        fullData=np.concatenate((targetData.reshape(-1,1),inputLagedData.reshape(-1,np.nansum(lagConfiguration))), axis=1)
        # Get the lenght of the data    
        dataLength=len(fullData)
        # Get the number of predictors
        numberOfLagedVaribles=inputLagedData.shape[1]
        
        # Check if the number of observations in
        # the calibration window is at least
        # same size+2 of the number of preditor variables
        if numberOfLagedVaribles+1>windowSize:
            #You need a bigger calibration window
            windowSize=numberOfLagedVaribles+2 #At least 2 degrees of freedom
            
        # Extract the validation data set
        #validationData=targetData[seq(dataLength-numberOfForecasts+1,dataLength)]
        validationData=targetData[np.arange(dataLength-numberOfForecasts,dataLength)].reshape(-1,1)
        
        # Create a vector to store the simulations
        simulatedData=np.zeros((numberOfForecasts,1), dtype=float)
        simulatedData.fill(np.nan)    
        
        # Realize the forecast for each calibration window
        for j in range(0,numberOfForecasts):
        
            # select the window for the specific forecast
            windowIndex=np.arange(dataLength-numberOfForecasts+1+j-windowSize-1,
            dataLength-numberOfForecasts+1+j)
            
            
            # Calibration set for the window -1 index
            train=fullData[windowIndex[np.arange(0,len(windowIndex)-1)],:]
            test=fullData[windowIndex[len(windowIndex)-1],:].reshape(1,-1)
            
            y=train[:,0].reshape(-1,1)
            x=train[:,range(1,train.shape[1])] 
            
            
            # Create a liner model
    # =============================================================================
            fit=self.lmFast(y,x)
    # =============================================================================
            
    
            # forecast one index outsie of the calibration window set
    # =============================================================================
            simulatedData[j,0]=self.predictlmFast(fit,test[:,range(1,train.shape[1])])

    
    # =============================================================================
            
        #FORECAST OUTSIDE THE DATA SET  
        Xout=self.createLagsOut(allData, lagConfiguration)
        #Trim it, just to get the last value 
        Xout=Xout[Xout.shape[0]-1,:].reshape(1,-1)
        # Predict using latest data
        forecast=self.predictlmFast(fit,Xout)
        
        # Wrap it with nans for the indexes ot the forecast
        nans=np.zeros(delta)
        nans[:]=np.nan
        #Target+nans for the delta
        validationData=np.append(validationData,nans.reshape(-1,1)).reshape(-1,1)
        #nans for the Target+delta
        simulatedData=np.append(simulatedData,nans).reshape(-1,1)
        #The last value is the target
        simulatedData[simulatedData.shape[0]-1]=forecast 
        return   validationData,simulatedData
    
    # =============================================================================
    #GA OPTIMIZATION FUNCTIONS
    # =============================================================================
       
    def initIndividual(self,icls, content):
        return icls(content)

    def initPopulation(self,pcls, ind_init,maxLag,popSize,gene_length):        
        
    
    #    the lag configurations as single variables
        singleVariables=np.identity(gene_length-1).astype(int)
        for d in range(2,maxLag):
            singleVariables=np.concatenate((singleVariables,d*np.identity(gene_length-1).astype(int)),axis=0)
    
    #    Add single lags with the average window
        contents = np.concatenate(((np.round(maxLag/2)*np.ones(singleVariables.shape[0])).astype(int).reshape(-1,1),
                                  singleVariables),axis=1).astype(int)
     
     
    #    the rest just random
        randomPortion=popSize-contents.shape[0]
        if randomPortion>0:    
            contents = np.concatenate((contents,
            np.random.randint(0, high=maxLag, size=(randomPortion,contents.shape[1]))),
            axis=0).astype(int)
        return pcls(ind_init(c) for c in contents) 
    
    
    
    def decode(chromosome):    
        # Decode GA solution to windowSize and lagConf    
        windowSize = windowRange[chromosome[0]]
        lagConf =  np.array( chromosome[1:], dtype=np.int32) 
        return windowSize,lagConf
    
    def objectiveFunction(self,chromosome):
        # Decode GA solution to windowSize and lagConf  
        #windowSize,lagConf=decode(chromosome)
        windowSize = self.windowRange[chromosome[0]]
        lagConf =  np.array( chromosome[1:], dtype=np.int32) 
 
        
        # Return fitness score of 99999 if window_size or num_unit is zero
        if np.sum(lagConf) == 0:
            cost=99999
    #        print('Validation s/sd: ',cost,'\n')
            return cost,
        else:
            target,forecast=self.predict(self.targetData,self.inputData,
                                      lagConf,
                                      windowSize,self.delta,
                                      self.test_length)
        
            cost=self.ssigmadelta(target,forecast,self.delta)
            if np.isnan(cost) or cost==0:
                bizarro=666
    
        return cost, 
    
    
    
     #Fit adaptative operator for forecast
    def fit(self, targetData,inputData,maxLag,windowLimits,delta,numberCrossVal,ngen,popSize):
       #Ger some parameters 
        test_length=numberCrossVal        
        minWindow=windowLimits[0]
        maxWindow=windowLimits[1]
        # =============================================================================
        # SET OPTIMIZATION PARAMETERS
        # =============================================================================
       #A triky way to pass bay the optimazer
        self.gene_length=inputData.shape[1]+1 #All variables and window        
        self.windowRange=np.round(np.linspace(minWindow, maxWindow, num=1+maxLag)).astype(int)
        self.targetData=targetData
        self.inputData=inputData       
        self.test_length=numberCrossVal
        self.maxLag=maxLag
        self.popSize=popSize
        self.delta=delta
        
        creator.create("FitnessMax", base.Fitness, weights=(-1.0,))
        creator.create("Individual", array.array, typecode='b', fitness=creator.FitnessMax)
        
        toolbox = base.Toolbox()
        
        # Attribute generator
        toolbox.register("attr_bool", random.randint, 0, maxLag)
        
        
        
        

        toolbox.register("evaluate", self.objectiveFunction)
        
        toolbox.register("mate", tools.cxTwoPoint)
        toolbox.register("mutate", tools.mutFlipBit, indpb=1/self.gene_length)
        #toolbox.register("select", tools.selBest, k=5)
        toolbox.register("select", tools.selTournament, tournsize=5)
        toolbox.register("migrate", tools.migRing, k=5, selection=tools.selBest,
            replacement=tools.selRandom)
        
        toolbox.register("variaton", algorithms.varAnd, toolbox=toolbox, cxpb=0.7, mutpb=0.3)

        # =============================================================================
        # ============================ RUN IT =========================================
      
        # Structure initializers GA
        toolbox.register("individual_guess", self.initIndividual, creator.Individual)
        toolbox.register("population_guess", self.initPopulation, list, toolbox.individual_guess)    
    
        pop = toolbox.population_guess(self.maxLag,self.popSize,self.gene_length)
        toolbox.register("population_guess", self.initPopulation, list, creator.Individual)
        hof = tools.HallOfFame(1)
        stats = tools.Statistics(lambda ind: ind.fitness.values)
        stats.register("avg", np.mean)
        stats.register("std", np.std)
        stats.register("min", np.min)
        stats.register("max", np.max)
                
        pop, log = algorithms.eaSimple(pop, toolbox, cxpb=0.5, mutpb=0.2, ngen=ngen, 
        stats=stats, halloffame=hof, verbose=True)
                
        best_individuals = tools.selBest(pop,k = 1)
                
                
        for bi in best_individuals:
        # Decode GA solution to integer for window_size and num_units
            best_windowSize = self.windowRange[bi[0]]
            best_lagConf =  np.array( bi[1:], dtype=np.int32) 
            print('\nDELTA: ', delta)
            print('\nBest Window Size: ', best_windowSize, ', Best Lag Config: ', best_lagConf)
            target,forecast=self.predict(targetData,inputData,
                                                  best_lagConf,
                                                  best_windowSize,
                                                  delta,numberCrossVal)
                
        cost=self.ssigmadelta(target,forecast,delta)
        print('Validation s/sd: ', cost,'\n')
        
        self.lagConf=best_lagConf
        self.window=best_windowSize
            
        return   best_windowSize,best_lagConf
    
    def predictSteps(self, targetData,inputData,stepsAhead,maxLag,windowLimits,numberCrossVal,ngen,popSize):
        
        forecasts=np.zeros(stepsAhead)
        error=np.zeros(stepsAhead)
        for step in range(1,stepsAhead+1):
            best_windowSize,best_lagConf=self.fit(targetData,inputData,maxLag,windowLimits,step,numberCrossVal,ngen,popSize)
            
            #APPLY OPERATOR
            target,simulation=self.predict(targetData,inputData,best_lagConf,best_windowSize,step,numberCrossVal)
            #PLOT PERFORMANCE
#            self.plotPerformance(target,simulation,step)
            #Get the rmse
            error[step-1]=self.rmse(target,simulation)
            #GRAB FORECAST
            forecasts[step-1]=simulation[simulation.shape[0]-1]           
            

        return forecasts,error
#        return target,simulation
    def plotSteps(self, target,forecasts,error):
        numberOfSteps=forecasts.shape[0]
        # plot it
        #For the x axes
        t = np.arange(1, len(target)+1+numberOfSteps).reshape(-1,1)
        
        #add  nans to fil the vectors
        nans1=np.zeros(numberOfSteps)
        nans1[:]=np.nan
        targetPlt=np.append(target,nans1.reshape(-1,1)).reshape(-1,1)
        
        nans2=np.zeros(target.shape[0])
        nans2[:]=np.nan
        forecastsPlt=np.append(nans2.reshape(-1,1),forecasts).reshape(-1,1)
        
        # The target    
        ax0 = plt.subplot()
        ax0.plot(t,targetPlt,marker=".",label='Target')
        
        # The steps and confidence intervals to plot
        nans3=np.zeros(target.shape[0]-1)# minus the las value (just 4 display)
        
        nans3[:]=np.nan
        stepsPlt=np.hstack((nans3,target[-1],forecasts.reshape(-1))) 
        
        errorPlt=np.hstack((nans3,0,error.reshape(-1)))
        
        ax0.fill_between(t.reshape(-1), stepsPlt-errorPlt, stepsPlt+errorPlt,color="#b675f3")
        
        ax0.scatter(t,forecastsPlt,marker=".",color="black",s=100,label='Forecast')                   
        ax0.plot(t.reshape(-1), stepsPlt,"--",color="#8400d5")
                  
        
        ax0.set_title("Forecast")
        ax0.set_xlim([np.nanmax(t)-numberOfSteps-10,np.nanmax(t)+1])
#        ax0.set_ylim([np.nanmin(target),np.nanmax(target)])
        ax0.legend()
        
        return 0