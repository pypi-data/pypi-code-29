import numpy as np
import csv
import collections
import os
from inspect import getmembers, isfunction
import types
import sys
np.set_printoptions(suppress=True)
pkg_version ='0.4.3.7.2'

def convert_t_x_y_dict(time_stamp, x, y):
    myDict = {}
    for i, line in enumerate(x):
        myDict[i] = (x[i], y[i])
    return myDict

def get_cols_csv(input_file, hasTrailComma = False):
    """
    Get csv/txt file "without/with trailing comma" and return a list for each column in the csv/txt
    """
    with open(input_file, 'r') as my_file:
        my_list = list(csv.reader(my_file, delimiter=','))
    
    if hasTrailComma:
        # remove last column of commas in the array: 3 means 4th column, 1 means delete a column
        temp_array = np.delete(np.array(my_list),3,1)
    else:
        temp_array = np.array(my_list, dtype=np.float)

    return temp_array.astype(np.float)[:,0].tolist(), temp_array.astype(np.float)[:,1].tolist(), temp_array.astype(np.float)[:,2].tolist()

def interpolate((x1, y1), (x2, y2), TOTAL_VAL = 140):
    """
    Input: two tuples, and total values between those two tuples
    """
    x_val = []
    y_val = []
    for i in range(1, TOTAL_VAL):
        a = float(i) / TOTAL_VAL             # rescale 0 < i < n --> 0 < a < 1
        x = (1 - a) * x1 + a * x2    # interpolate x coordinate
        y = (1 - a) * y1 + a * y2    # interpolate y coordinate
        x_val.append(x)
        y_val.append(y)
    x_val.append(x2)
    y_val.append(y2)

    return x_val, y_val

def interpolate_from_file(file_path):
    time, x, y = get_cols_csv(file_path)
    myDict = {}
    for i, line in enumerate(x):
        myDict[i+1] = (x[i], y[i])

    print myDict
    odd = myDict.keys()[::2]
    even = myDict.keys()[1::2]

    x_val_odd = []
    y_val_odd = []
    x_val_even = []
    y_val_even = []
    x_from_file_odd = []
    y_from_file_odd = []
    x_from_file_even = []
    y_from_file_even = []
    
    for i in range(len(odd) - 1):
        x_val_odd, y_val_odd = interpolate(myDict[odd[i]], myDict[odd[i+1]])
        x_from_file_odd.extend(x_val_odd)
        y_from_file_odd.extend(y_val_odd)

    for i in range(len(even) - 1):
        x_val_even, y_val_even = interpolate(myDict[even[i]], myDict[even[i+1]])
        x_from_file_even.extend(x_val_even)
        y_from_file_even.extend(y_val_even)
    
    return x_from_file_odd, y_from_file_odd, x_from_file_even, y_from_file_even

def generate_time_stamp(init_stamp = 0.0, final_time_stamp = 0.5, step_size = 0.005):
    time_stamp = []
    while init_stamp < final_time_stamp:
        time_stamp.append(init_stamp)
        init_stamp = init_stamp + step_size
    return map(float, np.around(time_stamp,decimals=5))
    
def get_folder_names(prim_type):
    """
        returns input_folder, right_swf_folder and left_swf_folder
    """
    if prim_type == 10:
        return ('forward/', 'Dyn_F_S_L')
    if prim_type == 20:
        # Not yet available
        return ('forward/', 'Dyn_F_S_R')
    if prim_type == 1:
        return ('forward/', 'Dyn_F_C_R', 'Dyn_F_C_L')
    if prim_type == 2:
        return ('backward/', 'Dyn_B_C_R', 'Dyn_B_C_L')
    if prim_type == 3:
        return ('LL/', 'Dyn_LL_C_R', 'Dyn_LL_C_L')
    if prim_type == 4:
        return ('LR/', 'Dyn_LR_C_R', 'Dyn_LR_C_L')
    if prim_type == 5:
        return ('diag_FL/', 'Dyn_FDL_C_R', 'Dyn_FDL_C_L')
    if prim_type == 6:
        return ['diag_FR/', 'Dyn_FDR_C_R', 'Dyn_FDR_C_L']
    if prim_type == 7:
        return ('diag_BL/', 'Dyn_BDL_C_R', 'Dyn_BDL_C_L')
    if prim_type == 8:
        return ('diag_BR/', 'Dyn_BDR_C_R', 'Dyn_BDR_C_L')
    if prim_type == 9:
        return ('curve_FL/', 'Dyn_FCL_C_L', 'Dyn_FCL_C_L')
    if prim_type == 10:
        return ('curve_FR/', 'Dyn_FCR_C_L', 'Dyn_FCR_C_L')

def file_path(prim_type, print_prim = False):

    input_folder, right_swf_folder, left_swf_folder = get_folder_names(prim_type)

    if print_prim:
        print "Primitive used: ", input_folder, right_swf_folder, left_swf_folder

    prim_folder = os.environ['MATLAB_PRIM']+'/'
    output_folder = os.environ['VREP_HOME']+'/Primitives/HRP4_Primitives/' 
    
    pcom_file = prim_folder+input_folder+'pCoM1.txt'
    vcom_file = prim_folder+input_folder+'vCoM1.txt'

    pcom_l = output_folder+left_swf_folder+'/pCoM_'+left_swf_folder+'.txt'
    vcom_l = output_folder+left_swf_folder+'/vCoM_'+left_swf_folder+'.txt'
    pcom_r = output_folder+right_swf_folder+'/pCoM_'+right_swf_folder+'.txt'
    vcom_r = output_folder+right_swf_folder+'/vCoM_'+right_swf_folder+'.txt'

    pl_file = prim_folder+input_folder+'pl1.txt'
    vl_file = prim_folder+input_folder+'vl1.txt'
    pr_file = prim_folder+input_folder+'pr1.txt'
    vr_file = prim_folder+input_folder+'vr1.txt'

    pl_out = output_folder+left_swf_folder+'/pfoot_'+left_swf_folder+'.txt'
    vl_out = output_folder+left_swf_folder+'/vfoot_'+left_swf_folder+'.txt'
    pr_out = output_folder+right_swf_folder+'/pfoot_'+right_swf_folder+'.txt'
    vr_out = output_folder+right_swf_folder+'/vfoot_'+right_swf_folder+'.txt'

    return pcom_file, vcom_file, pcom_l, vcom_l, pcom_r, vcom_r, pl_file, vl_file, pr_file, vr_file, pl_out, vl_out, pr_out, vr_out

def create_csv(input_file, output_file, needed_ts, time_stamp_limit = 0.5):
    myDict = {}
    tempDict = {}

    time_stamp = generate_time_stamp(0.0, time_stamp_limit)
    # to remove the trailing comma and create a new csv file
    temp_file = input_file+'temp'
    with open(input_file, 'r') as r, open(temp_file, 'w') as w:    
        for num, line in enumerate(r):
            newline = line[:-2] + "\n" if "\n" in line else line[:-1]
            w.write(newline)

    # create a dictionary with row[i][0] as key and row[i][1] row[i][2] as keys
    with open(temp_file, "rb") as f:
        reader = csv.reader(f, delimiter=",", quoting=csv.QUOTE_NONNUMERIC)
        for i, line in enumerate(reader):
            tempDict[line[0]] = line[-2:]
        # sort the dict with ascending keys
        myDict = collections.OrderedDict(sorted(tempDict.items()))

    # write the necessary values to a txt file
    out_file = open(output_file,"w")
    for i, val in enumerate(needed_ts[:-1]):
        file_str = str(np.around(np.array(time_stamp),5)[i])+','+str(myDict[val][0])+','+str(myDict[val][1])+','+'\n'
        out_file.write(file_str)
    os.remove(temp_file)

    # return dictionary from new csv file as: myDict[timestamp] = x, y
    return myDict

def is_local(object):
    return isinstance(object, types.FunctionType) and object.__module__ == __name__

def get_functions():
    a = [name for name, value in getmembers(sys.modules[__name__], predicate=is_local)]
    if 'get_functions' in a: a.remove('get_functions')
    if 'is_local' in a: a.remove('is_local')
    return a