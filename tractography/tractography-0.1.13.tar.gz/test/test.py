#TODO change it to real test

from src.tractography.io import read_ply#,write_ply
from dipy.tracking.streamline import set_number_of_points
import sys
import numpy as np

data1=read_ply('../data/132118/m_ex_atr-left_shore.ply')
#data2=read_ply('../data/150019/m_ex_atr-left_shore.ply')
#data2=read_ply('../data/terget.ply',[0,1,2])

def transform_bundles(datain,mat):
    new_data=[]
    for fib in datain:
        temp=[]
        for  vert in fib:
            vert = np.append(vert,1)
            vert = np.matmul(vert,mat)
            temp.append(vert[:-1])
            #print(vert[:-1])
        new_data.append(np.array(temp))
    return new_data

x=transform_bundles(data1,np.eye(4))
x=set_number_of_points(x,20)
print(x)

#data_1 = set_number_of_points(data1,20)
#data_2 = set_number_of_points(data2,20)

#print(data_1[0]*np.eye(4))
'''
match=[]
for i in range(len(data_1)):
    difr=sys.maxsize
    #print(difr)
    pos=-1,-1
    for j in range(len(data_2)):
        temp_dif=np.linalg.norm(data_1[i]-data_2[j])
        #temp_dif = sum(sum(abs(data_1[i]-data_2[j])))
        #print(temp_dif)
        if temp_dif<difr:
            difr=temp_dif
            pos = i,j
    match.append(pos)

#print(match)
#print(match[0][0])
print(data_1[match[0][0]])
#print(match[0][1])
print(data_2[match[0][1]])
'''