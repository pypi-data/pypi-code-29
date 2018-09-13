#借助非线性最小二乘法函数（leastsq），以年份为自变量，年专利累积量为因变量，对
#推广的logistic函数进行拟合。点表示实际值，线表示拟合值，公式表示拟合后的曲线。
import numpy as np
from scipy.optimize import leastsq
import matplotlib.pyplot as plt
import xlrd


###采样点(Xi,Yi)###

def shujuguiyi(xi,yi):
    x1=np.max(xi)
    x2=np.min(xi)

    y1=np.max(yi)
    y2=np.min(yi)
    
    yn = sum(yi) #申请累积量
    k = (yn-y2)/(x1-x2)
    n = len(str(int(k)))
    n1='1'
    for i in range(n-1):
        n1+='0'
    n2=int(n1)
    #print(n2)
    zi=[]
    sum1=yi[0]
    for i in yi:
        sum1=sum1+i#申请累积量
        a=sum1/n2
        zi.append(a)
    print(zi)
    return x1,x2,zi


'''def er(zi,zj):#多项式拟合函数 参数选定
    k=[]
    for j in range(1,20):
        for i in range(len(zi)):
            sum+=(zj[i]-zi[i])**2
        k.append(int(str(sum*10)+str(j)))
        n=str(min(k))[-1]
    return n'''

    
def func(p,x):
    top,slope,middle=p
    print(top,slope,middle)
    return top/(1+(np.e)**((middle-x)*slope))

def error(p,x,y,s):
    print(s)
    return func(p,x)-y


def nihe(filename,choice):
    data=xlrd.open_workbook(filename)
    sheet=data.sheets()[0]
    xi=sheet.col_values(0)   #读取第一列
    yi=sheet.col_values(1)   #读取第二列
    print(type(yi))
    ci=[]
    x1,x2,zi=shujuguiyi(xi,yi)
    plt.plot(xi,zi,'b*',label='original values')
    
    if choice==1:#如果选1 运行最小二乘法
        #TEST
        p0=[0,0,0]
        #print( error(p0,Xi,list) )

        ###主函数从此开始###
        s="Test the number of iteration" #试验最小二乘法函数leastsq得调用几次error函数才能找到使得均方误差之和最小的k、b
        Para=leastsq(error,p0,args=(xi,zi,s)) #把error函数中除了p以外的参数打包到args中
        top,slope,middle=Para[0]
        #print("top=",top,"slope=",slope,"middle=",middle)

        ###绘图，看拟合效果###
        
        #plt.plot(xi,zi,'r',label='original')
        #plt.figure(figsize=(8,6))
        #plt.scatter(xi,zi,color="red",label="Sample Point",linewidth=3) #画样本点
        x=np.linspace(x2-5,x1+5,(x1-x2)*10) # 在1983-2013画30个连续的点
        y=top/(1+(np.e)**((middle-x)*slope))

        plt.plot(x,y,color="orange",label="Fitting Line",linewidth=2) #画拟合直线
        plt.legend()
        plt.show()

        
    if choice==2:#如果选2 运行多项式拟合
        k=[]
        
        for j in range(1,15):
            
            poly=np.polyfit(xi,zi,j)
            z=np.polyval(poly,xi)
                
            sum2=0
            for i in range(len(z)):
                sum2+=(z[i]-zi[i])**2
            k.append(sum2)
            
        n=k.index(min(k))+1
        
        print(k)
        print('\n')
        print(n)
        poly=np.polyfit(xi,zi,n)
        x=np.linspace(x2-5,x1+5,(x1-x2)*10)
        z= np.polyval(poly,x)
        plt.plot(x,z)
        plt.show()

        



#top= 98.3418388602 slope= 0.120957312364 middle= 2006.12051328

