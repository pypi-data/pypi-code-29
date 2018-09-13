import pickle
import pandas as pd
import re
import numpy as np
import sys
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_curve,auc

import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import matplotlib as mpl


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Function to calculate missing values by columns
def missing_values_table(data,topK=20):
    #计算topK个缺失值，及百分比
    mis_val = data.isnull().sum()
    mis_val_percent = 100 * data.isnull().sum() / len(data)
    mis_val_table = pd.concat([mis_val, mis_val_percent], axis=1)
    mis_val_table_ren_columns = mis_val_table.rename(
    columns = {0 : 'Missing Values', 1 : '% of Total Values'})
    mis_val_table_ren_columns = mis_val_table_ren_columns[
        mis_val_table_ren_columns.iloc[:,1]!=0].sort_values(
    '% of Total Values', ascending=False).round(2)
    
    print ("Your selected dataframe has " + str(data.shape[1]) + " columns.\n" 
        "There are " + str(mis_val_table_ren_columns.shape[0]) +
          " columns that have missing values.")
    print('_'*60)
    print(mis_val_table_ren_columns.head(topK))

# Function to print columns types
def column_types_table(data,figShow =True, figsize = None):
    '''
    计算数据的类型及占比
    '''
    print('Number of each type of columns:')
    count_dtype = pd.DataFrame(data.dtypes.value_counts()).reset_index()
    count_dtype.columns = ['name','total']
    print(count_dtype)

    print('\nNumber of unique classes in each columns:')
    for i in count_dtype['name'].values:
        print('_'*40)
        print('Type: ',i)
        df = pd.DataFrame(data.select_dtypes(i).apply(pd.Series.nunique, axis=0)).sort_values(by=[0],ascending=True).rename(columns={0:'NUNIQUE'})
        if figShow:
            if figsize:
                fig = plt.gcf()
                fig.set_size_inches(figsize)
            ax = plt.gca()
            df.plot.barh(ax=ax)
            plt.show()
        print(df)

# Function to screen big diffrence feature between Train and Test
def train_test_distribution_difference(train_data,test_data,ignored_col=[],min_threshold=0.8,max_threshold=1.25):
    '''
    通过计算train和test的describe,对std和mean做除，比较train和test的分布是否一致，对于不一致的特征滤除
    return std_calc.index.values,mean_calc.index.values,both,union
    '''
    print('Screening big difference between train and test: ')
    print('Min Threshold: ',min_threshold,' \nMax Threshold: ',max_threshold)
    object_col = train_data.select_dtypes('object').columns
    numerical_col = list(set(train_data.columns)-set(object_col)-set(ignored_col))
    print('Numerical Length:' ,len(numerical_col))
    train_des = train_data[numerical_col].describe().T
    test_des = test_data[numerical_col].describe().T
    calc_diff = train_des/test_des
    std_calc = calc_diff[(calc_diff['std']>=min_threshold) & (calc_diff['std']<=max_threshold)]
    print('Std feature length: ',std_calc.shape[0])
    print('Std cover: \n',std_calc.index.values)
    mean_calc = calc_diff[(calc_diff['mean']>=min_threshold) & (calc_diff['mean']<=max_threshold)]
    print('Mean feature length: ',mean_calc.shape[0])
    print('Mean cover: \n',mean_calc.index.values)
    both = list(set(std_calc.index.values)&set(mean_calc.index.values))
    print('Both mean std: ',len(both))
    print('Both cover: \n',both)
    union = list(set(std_calc.index.values)|set(mean_calc.index.values))
    print('Union mean std: ',len(union))
    print('Union cover: \n',union)
    # Return 4 Seq
    return std_calc.index.values,mean_calc.index.values,both,union

# Function to analysis label describe
def label_analysis(data,label_name=None,feature_name=[],descirbePrint = True, figShow=True,figsize=None):
    '''
    将选定特征分标签对比
    figShow: bool, 是否输出不同标签特定特征的均值分布图像
    figsize: tuple, 调节该图像的大小(15,10)
    '''
    print('LABEL CATEGORY Analysis')
    count_label = pd.DataFrame(data[label_name].value_counts()).reset_index()
    count_label.columns = ['cate','total']
    print(count_label)
    try:
        data[label_name].astype(int).plot.hist(edgecolor='w',title='label number distribution')
        plt.show()
    except:
        data[label_name].fillna(-1).astype(int).plot.hist(edgecolor='w',title='label number distribution')
        plt.show()
    # Describe 01
    if len(feature_name)==0:
        feature_name = [i for i in data.columns if i not in [label_name,]]
    if figShow:
        if figsize:
            fig = plt.gcf()
            fig.set_size_inches(figsize)
        ax = plt.gca()
        data[feature_name].groupby(train[label_name]).agg('mean').plot.bar(ax=ax,title='mean value')
        plt.show()
    if descirbePrint:
        print('Want To Watch: ',len(feature_name))
        print(feature_name)
        print('Describe in each columns: ')
        for i in count_label['cate'].values:
            print('Cate: ',i)
            print(data[data[label_name].astype(int)==i][feature_name].describe())

    print('CALC CORR')
    correlations = data.corr()[label_name].sort_values()
    print('Most Positive Correlations:\n', correlations.tail(15))
    print('\nMost Negative Correlations:\n', correlations.head(15))

def roc_auc_plot(y_test,y_proba):
	#ytest为真实的标签，shuffleResult[:,1]为预测结果为坏盘的概率
	fpr, tpr, thresholds = roc_curve(y_test,y_proba)
	roc_auc = auc(fpr, tpr)#auc值，roc曲线下面积大小
	plt.plot(fpr,tpr,label='auc = %0.2f' % roc_auc,color='r')
	plt.xlim(0,1)
	plt.ylim(0,1)
	plt.plot([0,1],[0,1],label='randomPrecict')
	plt.legend(loc='best')
	plt.xlabel('False Positive Rate')  
	plt.ylabel('True Positive Rate')
	plt.title(u'2016测试集(1000个好盘112个坏盘混合)的ROC曲线:')
	plt.show()
	
def unique(lst):
    '''
    统计列表中元素出现个数，返回一个字典
    '''
    return dict(zip(*np.unique(lst, return_counts=True)))

def read_data(filename, chunkSize=5000000,**kwargs):    
    '''
    读取大文件csv
    eg: ST4000DM000 = read_data('/data/ST4000DM000.csv',5000000)
    '''
    reader = pd.read_csv(filename, iterator=True,**kwargs)
    loop = True
    chunks = []
    while loop:
        try:
            chunk = reader.get_chunk(chunkSize)
            chunks.append(chunk)
        except StopIteration:
            loop = False
            print ("'" + re.findall(r'\w*\.',filename)[0][:-1]+"'",'has been read successfully!')
    data = pd.concat(chunks, ignore_index=True)
    return data
    
def read_pickle(filename):
    '''
    从pkl中读取数据
    eg: featuresList = readPickle('/data/features.pkl')
    '''
    f = open(filename,'rb')
    pkls = pickle.load(f)
    f.close()
    return pkls
    
def save_pickle(filename,pkls):
    '''
    将数据存为序列化文件pkl，
    eg: savePickle('/data/features.pkl',featuresList)
    '''
    f = open(filename,'wb')
    pickle.dump(pkls,f)
    f.close()    

def mem_usage(element,ctype = 'G'):
    if ctype=='G':
        mem = sys.getsizeof(element)/2**30
    elif ctype=='M':
        mem = sys.getsizeof(element)/2**20
    elif ctype=='K':
        mem = sys.getsizeof(element)/2**10
    else:
        print('ctype error!')
        return False
    print(f'memory usage: {mem:.2f}{ctype}')
    return mem




def get_data_ndays(data,fromday=0,today=10):
    data_group = data.groupby('serial_number')
    return data_group.apply(lambda x: x.iloc[fromday:today,:]).reset_index(drop=True)



def confusion_matrix_plot_matplotlib(y_truth, y_predict,normalize = False, cmap=plt.cm.cool,title='Confusion matrix',figsize=None,silent = False):
    """Matplotlib绘制混淆矩阵图
    parameters
    ----------
        y_truth: 真实的y的值, 1d array
        y_predict: 预测的y的值, 1d array
        cmap: 画混淆矩阵图的配色风格, 使用cm.Blues，更多风格请参考官网
        figsize: 图像大小,figsize=(20,20)
        
    """
                                     
    mpl.rcParams['axes.unicode_minus']=False
    mpl.rcParams['font.sans-serif'] = ['Droid Sans Fallback']#设置matplotlib中文字体
    from sklearn.metrics import confusion_matrix
    cm = confusion_matrix(y_truth, y_predict)    
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        #print('Confusion matrix, without normalization')
        rate_raw = []
        rate_col = []
        for i in range(cm.shape[0]):            
            i_rate_raw = cm[i,i]/cm.sum(axis=0)[i]
            i_rate_col = cm[i,i]/cm.sum(axis=1)[i]
            rate_col.append(i_rate_col)
            rate_raw.append(i_rate_raw)
            if not silent:
                print('第{}类被正确识别比例:{:.2f}  预测出的第{}类真实比例:{:.2f}'.format(i,i_rate_col,i,i_rate_raw))
        if not silent:
            print('平均正确识别率:{:.2f}    平均正确预测率:{:.2f}'.format(sum(rate_col)/len(rate_col),sum(rate_raw)/len(rate_raw)))
    
    plt.matshow(cm, cmap=cmap)  # 混淆矩阵图
    plt.colorbar()  # 颜色标签
    plt.title(title)
    for x in range(len(cm)):  # 数据标签        
        for y in range(len(cm)):
            plt.annotate(cm[x, y], xy=(y, x), horizontalalignment='center', verticalalignment='center')
 
    plt.ylabel('True label')  # 坐标轴标签
    plt.xlabel('Predicted label')  # 坐标轴标签
    if figsize:
        fig = plt.gcf()
        fig.set_size_inches(figsize)
    plt.show()  # 显示作图

def model_train(model, data):
    xTrain,xTest,yTrain,yTest = train_test_split(data.drop(['failure'],1),data['failure'])
    model.fit(xTrain,yTrain)
    confusion_matrix_plot_matplotlib(yTest,model.predict(xTest))
    return model

def model_predict(model,data):    
    serial_number = get_serial_number(data)
    predict_result = model.predict(data).tolist()    
    return dict(zip(serial_number,predict_result))

def model_predict_proba(model,data):    
    serial_number = get_serial_number(data)
    predict_result_proba = model.predict_proba(data)[:,1].tolist()    
    return dict(zip(serial_number,predict_result_proba))



def model_xgb_multi(data,n_class=4,normalized=False):
    from sklearn.utils import shuffle
    data =shuffle(data)
    xTrain,xTest,yTrain,yTest = train_test_split(data.drop(['failure'],1),data['failure'])
    import xgboost as xgb
    xg_train = xgb.DMatrix(xTrain, label=yTrain)
    xg_test = xgb.DMatrix(xTest, label=yTest)                                                                                                                                                
    # setup parameters for xgboost  
    param = {}  
    # use softmax multi-class classification  
    param['objective'] = 'multi:softmax'  
    # scale weight of positive examples  
    param['eta'] = 0.1  
    param['max_depth'] = 6  
    param['silent'] = 1  
    param['nthread'] = 4  
    param['num_class'] = n_class
#early stop
    watchlist = [ (xg_train,'train'), (xg_test, 'test') ]  
    model = xgb.train(param,dtrain=xg_train, evals=watchlist,early_stopping_rounds=10);  
    # get prediction  
    
    confusion_matrix_plot_matplotlib(yTest,model.predict(xg_test),normalize=normalized)
    return model

def series_to_supervised(data, n_in=1, n_out=1, dropnan=True):
    """
    Frame a time series as a supervised learning dataset.
    Arguments:
        data: Sequence of observations as a list or NumPy array.
        n_in: Number of lag observations as input (X).
        n_out: Number of observations as output (y).
        dropnan: Boolean whether or not to drop rows with NaN values.
    Returns:
        Pandas DataFrame of series framed for supervised learning.
    """
    n_vars = 1 if type(data) is list else data.shape[1]
    df = DataFrame(data)
    cols, names = list(), list()
    # input sequence (t-n, ... t-1)
    for i in range(n_in, 0, -1):
        cols.append(df.shift(i))
        names += [('var%d(t-%d)' % (j+1, i)) for j in range(n_vars)]
    # forecast sequence (t, t+1, ... t+n)
    for i in range(0, n_out):
        cols.append(df.shift(-i))
        if i == 0:
            names += [('var%d(t)' % (j+1)) for j in range(n_vars)]
        else:
            names += [('var%d(t+%d)' % (j+1, i)) for j in range(n_vars)]
    # put it all together
    agg = concat(cols, axis=1)
    agg.columns = names
    # drop rows with NaN values
    if dropnan:
        agg.dropna(inplace=True)
    return agg.reset_index(drop=True)
