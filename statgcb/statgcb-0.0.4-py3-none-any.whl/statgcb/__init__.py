# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 11:19:11 2017

@author: fblav
"""



#%%

import numpy as np
import scipy.stats as st
import itertools
import statsmodels.api as sm



GEN = [
[3,1,[[1,1]]],
[4,1,[[1,1,1]]],
[5,2,[[1,1,0],[1,0,1]]],
[5,1,[[1,1,1,1]]],
[6,3,[[1,1,0],[1,0,1],[0,1,1]]],
[6,2,[[1,1,1,0],[0,1,1,1]]],
[6,1,[[1,1,1,1,1]]],
[7,4,[[1,1,0],[1,0,1],[0,1,1]]],
[7,3,[[1,1,1,0],[0,1,1,1],[1,0,1,1]]],
[7,2,[[1,1,1,1,0],[1,1,1,0,1]]],
[7,1,[[1,1,1,1,1,1]]],
[8,4,[[1,1,1,0],[0,1,1,1],[1,0,1,1],[1,1,0,1]]],
[8,3,[[1,1,1,0,0],[1,1,0,1,0],[0,1,1,1,1]]],
[8,2,[[1,1,1,1,0,0],[1,1,0,0,1,1]]],
[8,1,[[1,1,1,1,1,1,1]]],
[9,5,[[1,1,1,0],[0,1,1,1],[1,0,1,1],[1,1,0,1],[1,1,1,1]]],
[9,4,[[1,1,1,1,0],[1,1,1,0,1],[1,1,0,1,1],[1,0,1,1,1]]],
[9,3,[[1,1,1,1,0,0],[1,0,1,0,1,1],[0,0,1,1,1,1]]],
[9,2,[[1,1,1,1,1,1,0],[1,1,1,0,1,1,1]]],
[9,1,[[1,1,1,1,1,1,1,1]]],
[10,6,[[1,1,1,0],[0,1,1,1],[1,0,1,1],[1,1,0,1],[1,1,1,1],[1,1,0,0]]],
[10,5,[[1,1,1,1,0],[1,1,1,0,1],[1,1,0,1,1],[1,0,1,1,1],[0,1,1,1,1]]],
[10,4,[[1,1,1,1,0,0],[1,1,1,0,1,0],[1,0,0,1,1,1],[0,1,0,1,1,1]]],
[10,3,[[1,1,1,0,0,0,1],[0,1,1,1,1,0,0],[1,0,1,1,0,1,0]]],
[10,2,[[1,1,1,1,1,1,0,0],[1,1,1,1,0,0,1,1]]],
[10,1,[[1,1,1,1,1,1,1,1,1]]],
[11,7,[[1,1,1,0],[0,1,1,1],[1,0,1,1],[1,1,0,1],[1,1,1,1],[1,1,0,0],[1,0,1,0]]],
[11,6,[[1,1,1,0,0],[0,1,1,1,0],[0,0,1,1,1],[1,0,1,1,0],[1,0,0,1,1],[0,1,0,1,1]]],
[11,5,[[1,1,1,1,0,0],[1,1,1,0,1,0],[1,1,0,1,1,0],[1,0,1,1,1,1],[0,1,1,1,1,1]]],
[11,4,[[1,1,1,0,0,0,1],[0,1,1,1,1,0,0],[1,0,1,1,0,1,0],[1,1,1,1,1,1,1]]],
[11,3,[[1,1,1,1,1,1,0,0],[1,1,1,1,0,0,1,1],[1,1,0,1,0,1,1]]],
[11,2,[[1,1,1,1,1,1,0,0,0],[1,1,1,0,0,0,1,1,1]]],
]


#%%
# Unique source code

def unique(ar, return_index=False, return_inverse=False,
           return_counts=False, axis=None):

    ar = np.asanyarray(ar)
    if axis is None:
        return _unique1d(ar, return_index, return_inverse, return_counts)
    if not (-ar.ndim <= axis < ar.ndim):
        raise ValueError('Invalid axis kwarg specified for unique')

    ar = np.swapaxes(ar, axis, 0)
    orig_shape, orig_dtype = ar.shape, ar.dtype
    # Must reshape to a contiguous 2D array for this to work...
    ar = ar.reshape(orig_shape[0], -1)
    ar = np.ascontiguousarray(ar)

    if ar.dtype.char in (np.typecodes['AllInteger'] +
                         np.typecodes['Datetime'] + 'S'):
        # Optimization: Creating a view of your data with a np.void data type of
        # size the number of bytes in a full row. Handles any type where items
        # have a unique binary representation, i.e. 0 is only 0, not +0 and -0.
        dtype = np.dtype((np.void, ar.dtype.itemsize * ar.shape[1]))
    else:
        dtype = [('f{i}'.format(i=i), ar.dtype) for i in range(ar.shape[1])]

    try:
        consolidated = ar.view(dtype)
    except TypeError:
        # There's no good way to do this for object arrays, etc...
        msg = 'The axis argument to unique is not supported for dtype {dt}'
        raise TypeError(msg.format(dt=ar.dtype))

    def reshape_uniq(uniq):
        uniq = uniq.view(orig_dtype)
        uniq = uniq.reshape(-1, *orig_shape[1:])
        uniq = np.swapaxes(uniq, 0, axis)
        return uniq

    output = _unique1d(consolidated, return_index,
                       return_inverse, return_counts)
    if not (return_index or return_inverse or return_counts):
        return reshape_uniq(output)
    else:
        uniq = reshape_uniq(output[0])
        return (uniq,) + output[1:]

def _unique1d(ar, return_index=False, return_inverse=False,
              return_counts=False):
    """
    Find the unique elements of an array, ignoring shape.
    """
    ar = np.asanyarray(ar).flatten()

    optional_indices = return_index or return_inverse
    optional_returns = optional_indices or return_counts

    if ar.size == 0:
        if not optional_returns:
            ret = ar
        else:
            ret = (ar,)
            if return_index:
                ret += (np.empty(0, np.intp),)
            if return_inverse:
                ret += (np.empty(0, np.intp),)
            if return_counts:
                ret += (np.empty(0, np.intp),)
        return ret

    if optional_indices:
        perm = ar.argsort(kind='mergesort' if return_index else 'quicksort')
        aux = ar[perm]
    else:
        ar.sort()
        aux = ar
    flag = np.concatenate(([True], aux[1:] != aux[:-1]))

    if not optional_returns:
        ret = aux[flag]
    else:
        ret = (aux[flag],)
        if return_index:
            ret += (perm[flag],)
        if return_inverse:
            iflag = np.cumsum(flag) - 1
            inv_idx = np.empty(ar.shape, dtype=np.intp)
            inv_idx[perm] = iflag
            ret += (inv_idx,)
        if return_counts:
            idx = np.concatenate(np.nonzero(flag) + ([ar.size],))
            ret += (np.diff(idx),)
    return ret

def intersect1d(ar1, ar2, assume_unique=False):

    if not assume_unique:
        # Might be faster than unique( intersect1d( ar1, ar2 ) )?
        ar1 = unique(ar1)
        ar2 = unique(ar2)
    aux = np.concatenate((ar1, ar2))
    aux.sort()
    return aux[:-1][aux[1:] == aux[:-1]]

def setxor1d(ar1, ar2, assume_unique=False):

    if not assume_unique:
        ar1 = unique(ar1)
        ar2 = unique(ar2)

    aux = np.concatenate((ar1, ar2))
    if aux.size == 0:
        return aux

    aux.sort()
    flag = np.concatenate(([True], aux[1:] != aux[:-1], [True]))
    return aux[flag[1:] & flag[:-1]]


def in1d(ar1, ar2, assume_unique=False, invert=False):

    ar1 = np.asarray(ar1).ravel()
    ar2 = np.asarray(ar2).ravel()

    contains_object = ar1.dtype.hasobject or ar2.dtype.hasobject


    if len(ar2) < 10 * len(ar1) ** 0.145 or contains_object:
        if invert:
            mask = np.ones(len(ar1), dtype=bool)
            for a in ar2:
                mask &= (ar1 != a)
        else:
            mask = np.zeros(len(ar1), dtype=bool)
            for a in ar2:
                mask |= (ar1 == a)
        return mask

    # Otherwise use sorting
    if not assume_unique:
        ar1, rev_idx = unique(ar1, return_inverse=True)
        ar2 = unique(ar2)

    ar = np.concatenate((ar1, ar2))

    order = ar.argsort(kind='mergesort')
    sar = ar[order]
    if invert:
        bool_ar = (sar[1:] != sar[:-1])
    else:
        bool_ar = (sar[1:] == sar[:-1])
    flag = np.concatenate((bool_ar, [invert]))
    ret = np.empty(ar.shape, dtype=bool)
    ret[order] = flag

    if assume_unique:
        return ret[:len(ar1)]
    else:
        return ret[rev_idx]


def isin(element, test_elements, assume_unique=False, invert=False):

    element = np.asarray(element)
    return in1d(element, test_elements, assume_unique=assume_unique,
                invert=invert).reshape(element.shape)


def union1d(ar1, ar2):

    return unique(np.concatenate((ar1, ar2)))

def setdiff1d(ar1, ar2, assume_unique=False):

    if assume_unique:
        ar1 = np.asarray(ar1).ravel()
    else:
        ar1 = unique(ar1)
        ar2 = unique(ar2)
    return ar1[in1d(ar1, ar2, assume_unique=True, invert=True)]
    


#%%


def cartesian(arrays, out=None):

    arrays = [np.asarray(x) for x in arrays]
    dtype = arrays[0].dtype

    n = np.prod([x.size for x in arrays])
    if out is None:
        out = np.zeros([n, len(arrays)], dtype=dtype)

    m = n / arrays[0].size
    out[:,0] = np.repeat(arrays[0], int(m))
    if arrays[1:]:
        cartesian(arrays[1:], out=out[0:int(m),1:])
        for j in range(1, arrays[0].size):
            out[j*int(m):(j+1)*int(m),1:] = out[0:int(m),1:]
    return out


def anovan(y,X,req=123456789):

    # Input matrix
    
    X = np.array(X)
    y = np.array(y)
    
    if(X.shape[0]!=len(y)):
        raise ValueError("X-y dimensions mismatch")
    
    
    # Modify each X column to make them beginning at 0
    allV = ""
    for j in range(X.shape[1]):
        allV = allV + chr(j+65)
        allval = unique(X[:,j])
        allval = np.sort(allval)
        for k in range(allval.size):
            ff=X[:,j]==allval[k]
            X[ff,j] = k
    
#%%
    
    k = []
    l = []
    m = []
    
    dimensions = np.zeros(np.size(X,1), dtype=np.int)
    for pos_col in range(0,np.size(X,1),1):
        dim = len(unique(X[:,pos_col]))
        dimensions[pos_col] = dim
        k.append(np.arange(0,dim))    
        l.append(np.size(X,1))
        m.append(np.arange(0,np.size(X,1))) 
        
    all_comb = cartesian(k)
    all_inter = cartesian(m)
    
    # Calculate SSe
    SSe = 0
    for i in range(0,len(all_comb)):
        ff = X == all_comb[i,:]
        ff = np.prod(ff, 1)==1
        selection = y[ff]
        SSe = SSe+ np.sum( (selection - np.mean(selection))**2 )
        
    # Remove the same combinations    
    for i in range(0,len(all_inter)):
        sel = np.sort(all_inter[i,:])
        all_inter[i,:] = np.sort(all_inter[i,:])
        
        
    #%% Automatic req if required
    if (np.sum(req)==123456789):
        
        allP = []
        stuff = np.arange(0,len(dimensions)).tolist()
        for L in range(0, len(stuff)+1):
          for subset in itertools.combinations(stuff, L):
            if(len(subset)>0):
                allP.append(list(subset))
                
        req = np.zeros([len(allP),len(dimensions)])
        
        for j in range(len(allP)):
            selP = allP[j]
            for k in range(len(selP)):
                req[j,selP[k]] = 1
    else:
        # Transform to list if NumpyArray
        if(type(req).__module__ == np.__name__):
            req = req.tolist()
        
        # Transform to 2D list if it contains only 1 dimension
        if(isinstance(req[0], int)):
            req = [req]
        
        if(np.sum(np.array(req)>1)>0):
            raise ValueError("Interaction matrix must only contain 0 and 1")
    
        if(np.sum(np.array(req)<0)>0):
            raise ValueError("Interaction matrix must only contain 0 and 1")
        
        # Transform to number if booleans
        for j in range(len(req)):
            req[j] = list(map(lambda x: 1 if x else 0, req[j]))
    
        if(len(req[0]) != X.shape[1]):
            raise ValueError("Interaction matrix column count mismatch with X")
        
        if(unique(np.array(req), axis=0).shape[0] < len(req)):
            raise ValueError("Presence of duplicated rows in the interaction matrix")
        
    #%%
    
    all_inter = unique(all_inter,False,False,False,0)
        
    ll = []
    for i in range(0,len(all_inter)):
        for j in range(i+1,len(all_inter)):
            ff1 = np.in1d(all_inter[j],unique(all_inter[i]))
            ff2 = np.in1d(unique(all_inter[i]),all_inter[j])
            if((np.prod(ff1)*np.prod(ff2))>0):
                ll.append(j)
    ll = unique(ll)
    if(len(ll)>0):
        all_inter = np.delete(all_inter, ll, 0)
    
    
    #%%
    
    inter_keep = []
    inter_SS = []
    all_DL = []
    
    # Calculate sum of squares
    for h in range(0,np.size(all_inter,0)):
        
        inter_sel = all_inter[h,:]
        inter_sel = unique(inter_sel)
        
        # For each variable in inter_sel get all possible values
        g = []
        for i in range(0,len(inter_sel)):
            g.append( np.arange(0,dimensions[inter_sel[i]]) )
        
        # All possible combinations
        all_pob = cartesian(g)
        
        # Calculate all means
        allmeans = []
        allsum = 0;
        alln = []
        for i in range(0,len(all_pob)):
            # Create logical filters
            k = X[:,inter_sel] == all_pob[i]
            ff = np.prod(k, 1)==1
            allmeans.append(np.mean(y[ff]))
            allsum = allsum + sum(y[ff])
            alln.append(np.sum(ff))
        
        # Calculate means between groups
        meangroup = np.mean(allmeans)
        
        # Calculate SS
        allmeans = np.array(allmeans)
        alln = np.array(alln)
        Ss = np.sum(alln*( (allmeans-meangroup)**2 ))
        
        # Keep information
        inter_SS.append( Ss )
        inter_keep.append(inter_sel)
        all_DL.append( np.prod(dimensions[inter_sel]-1) )
    
    if(np.sum(np.array(all_DL)==0)>0):
        raise ValueError("Presence of DF=0")
    
    
    # Interaction SS
    inter_SS = np.array(inter_SS)
    
    # Calculate SST
    ymean = np.mean(y)
    SSt = np.sum(  (y - ymean )**2 )
    
    
    
    #%%
    
    # Remove SS from interactions
    for interlevel in range(0,np.size(X,1)): # For each level of interaction
        for h in range(0,np.size(all_inter,0)):
            sel = unique(all_inter[h,:])
            if(interlevel == len(sel)):
                for i in range(0,np.size(all_inter,0)):
                    if (h != i):
                        tt = np.in1d(sel,all_inter[i,:] )
                        if(np.prod(tt)>0):
                            inter_SS[i] = inter_SS[i] - inter_SS[h]
    
    
    if(np.sum(np.isnan(inter_SS))>0):
        raise ValueError("Presence of SS=NaN")
    
    # Calculate DF TOTAL and ERROR
    DF_tot = len(y)-1
    DF_e = DF_tot - np.sum(all_DL)
    
    
    
    #%%
    
    # Calculate considering all interactions
    MSE = SSe / DF_e
    MS = (inter_SS) / np.array(all_DL)
    Ratio = MS/MSE
    
    p_val = np.zeros(len(all_DL))
    for i in range(0,len(all_DL)):
        p_val[i] = 1 - st.f.cdf(Ratio[i],all_DL[i],DF_e)
    
    
    
    #%%
    
    req = np.array(req)
    addE = np.sum(inter_SS)
    addDL = np.sum(all_DL)
    onlySS = []
    onlyDL = []
    onlyInter = []
    
    
    # Remove non desired interactions
    for i in range(0,np.size(req,0)):
        sel = req[i]*np.arange(1,np.size(X,1)+1)
        ff = sel>0
        sel = np.sort(sel[ff]-1)
        
        for j in range(0,len(all_inter)):
        
            sel2 = np.sort(unique(all_inter[j]))
            
            if(len(sel) == len(sel2)): # If the same size
                if(np.prod( sel == sel2 )>0): # If the contents
                    addE = addE - inter_SS[j]
                    addDL = addDL - all_DL[j]
                    onlySS.append(inter_SS[j])
                    onlyDL.append(all_DL[j])
                    onlyInter.append(inter_keep[j])
                    
                    
    # Calcule new SSE
    SSe_n = SSe + np.sum(addE)
    # Calculate new DF of noise
    DF_e_n = DF_e + np.sum(addDL)
    
    MSE_n = SSe_n / DF_e_n
    MS_n = np.array(onlySS) / np.array(onlyDL)
    Ratio_n = MS_n/MSE_n
    
    p_val_n = np.zeros(len(Ratio_n))
    for i in range(0,len(Ratio_n)):
        p_val_n[i] = 1 - st.f.cdf(Ratio_n[i],onlyDL[i],DF_e_n)
    
    # Print results
    
    print("====================================================")
    table_dict = {} # Initialize data
    for i in range(len(p_val_n)):
        rr = req[i]
        EffS = ""
        for k in range(len(rr)):
            if (rr[k]==1):
                EffS = EffS + chr(k+65)
        print("%s :   SS=%.2f   DF=%.0f   MS=%.3f   p=%.4f" % (EffS, onlySS[i], onlyDL[i], MS_n[i], p_val_n[i]))
        table_dict[EffS] = { "SS":onlySS[i], "DF":onlyDL[i], "MS":MS_n[i], "p":p_val_n[i] }
    print("Err :   SS=%.2f   DF=%.0f   MS=%.3f" % (SSe_n, DF_e_n, MSE_n))
    table_dict["Err"] = { "SS":SSe_n, "DF":DF_e_n, "MS":MSE_n }
    print("Tot :   SS=%.2f   DF=%.0f" % (SSt, DF_tot))
    table_dict["Tot"] = { "SS":SSt, "DF":DF_tot }
    print("====================================================")
    return (req,table_dict)





def make_2plan(nb_factors,nb_partial=0,nb_replicates=1):

    nbvar = nb_factors - nb_partial
    all_choices = []
    for j in range(nbvar):
        all_choices.append([1,-1])
    allC = cartesian(all_choices)
    allC = allC.tolist()
    allCr = []
    for j in range(len(allC)):
        for k in range(nb_replicates):
            allCr.append(allC[j])
    
    if(nb_partial>0):
        cc= True
        count = 0
        while cc:
            if((GEN[count][0]==nb_factors) and (GEN[count][1]==nb_partial)):
                cc = False
                generators = GEN[count][2]
            else:
                count = count + 1
        
        
    # Partial
    pos = np.arange(0,nb_factors-nb_partial)
    allCrE = np.array(allCr).astype(float)
    allCr= np.array(allCr).astype(float)
    gen_string = ""
    for j in range(nb_partial):
        sel_gen = generators[j]
        
        # Show generator
        ss = chr(65+nbvar+j) + " = "
        for k in range(len(sel_gen)):
            if(sel_gen[k]==1):
                ss = ss + chr(65+k)
        gen_string = gen_string + "Generator "+ str(j+1) +": " + ss + "\n"
        FF = np.array(sel_gen)==1
        pos_sel = pos[FF]
        v = np.array([np.prod(allCr[:,pos_sel],axis=1)]).T
        allCrE = np.append(allCrE,v,axis=1)
        
    allCrEA = np.copy(allCrE)
    
    # Extend matrix
    inter = []
    inter_nb = np.arange(0,nb_factors).tolist()
    for j in range(nb_factors):
        inter.append(chr(65+j))
    
    # Add partial choices
    for k in range(nb_partial):
        all_choices.append([1,-1])
        
    # Make 0-1 matrix
    allC = cartesian(all_choices)
    allC = (allC+1)/2
    
    allCs = np.sum(allC,axis=1).tolist()
    ii = sorted(range(len(allCs)), key=lambda k: allCs[k])
    allC = allC[ii,:]
    
    
    fc = 0
    if(nb_partial>0):
        fc = 0
    
    pos = np.arange(0,nb_factors)
    for j in range(allC.shape[0]):
        allC_sel = allC[j,:]
        if( (np.sum(allC_sel)>1) and (np.sum(allC_sel)<(nb_factors-nb_partial-fc+1)) ):
            FF = allC_sel==1
            posa = pos[FF]
            v = np.array([np.prod(allCrE[:,posa],axis=1)]).T
            allCrEA = np.append(allCrEA,v,axis=1)
            ssa = ""
            for l in range(len(allC_sel)):
                if(allC_sel[l]==1):
                    ssa = ssa + chr(l+65)
            inter.append(ssa)
    
    allCrEAu = unique(allCrEA,axis=1)
    
    ds = ""
    int_list = []
    for j in range(allCrEAu.shape[1]):
        count = 0
        sl = ""
        for k in range(allCrEA.shape[1]):
            if(np.array_equal(allCrEAu[:,j], allCrEA[:,k])):
                if(count>0):
                    ds = ds + "="
                    sl = sl + "="
                ds = ds + inter[k]
                sl = sl + inter[k]
                count = count + 1
        int_list.append([sl,allCrEAu[:,j]])
        ds = ds+ "\n"
            

    return allCr,allCrE,ds,gen_string,int_list



class exp2plan:
    
    def __init__(self):
        self.Exp = []
        self.ExpE = []
        self.ExpP = []
        self.y = []
        self.int_list = []
        self.effects = []
        self.results = []
        self.inter = []
        self.req = []
        self.generators = []
        self.real_values = False
    
    def make_plan(self,nb_factors,nb_partial=0,nb_replicates=1):
        if(nb_factors>nb_partial):
            infoexp = make_2plan(nb_factors,nb_partial,nb_replicates)
            self.Exp = infoexp[0]
            self.ExpE = infoexp[1]
            self.inter = infoexp[2]
            self.generators = infoexp[3]
            self.int_list = infoexp[4]
        else:
            print("Not valid")
    
    def specify_params(self,vals):
        vals = np.array(vals)
        if(self.inter != []):
            if( (self.ExpE.shape[1]==vals.shape[0]) and (2==vals.shape[1]) ):
                self.real_values = True
                A = np.copy(self.ExpE)
                for j in range(A.shape[1]):
                    ff = A[:,j] == -1
                    A[ff,j] = vals[j,0]
                    ff = A[:,j] == 1
                    A[ff,j] = vals[j,1]
                self.ExpP = A
            else:
                print("Mismatching dimensions")
        else:
            print("NO EXISTING PLAN, please use make_plan")
    
    def insert_results(self,y):
        if(self.inter != []):
            if(isinstance(y, np.ndarray)):
                if(len(y)>1 and y.ndim>1):
                    y = y.T
                if(y.ndim > 1 ):
                    y = y.tolist()
                    y = y[0]
                else:
                    y = y.tolist()
            if(len(y) == self.Exp.shape[0]):
                self.y = y
                y = np.array(y)
                A = [["intercept",np.mean(y)]]
                for j in range(len(self.int_list)):
                    h = self.int_list[j][1]
                    if((np.sum(h==1)>0) and (np.sum(h==-1)>0)):
                        A.append([self.int_list[j][0],(np.mean(y[h==1])-np.mean(y[h==-1]))/2])
                    else:
                        A.append([self.int_list[j][0],"intercept"])
                self.effects = A
            else:
                print("MISMATCHING DIMENSIONS BETWEEN X-y, no data inserted")
        else:
            print("NO EXISTING PLAN, please use make_plan")
    
    def anova(self,req=123456789):
        if(self.inter != []):
            if(self.y != []):
                if(isinstance(req, np.ndarray)):
                    req = req.tolist()
                if(req != 123456789):
                    if(isinstance(req[0], int)):
                        req = [req]
                    req = np.array(req)
                    req = req[:,0:self.Exp.shape[1]]
                    req = req.tolist()
                X = self.Exp
                y = self.y
                req,table_anova = anovan(y,X,req)
                self.req = req
                return table_anova
            else:
                print("No available results, cannot perform ANOVA")
        else:
            print("NO EXISTING PLAN, please use make_plan")
            
            
    def show_plan(self,tt=0):
        if(self.inter != []):
            print(str(self.Exp.shape[0]) + " runs:")
            if(tt==1):
                print(self.ExpE)
            elif(tt==0):
                print(self.Exp)
            elif(tt==2):
                if(self.real_values):
                    print(self.ExpP)
                else:
                    print(self.ExpE)
        else:
            print("NO EXISTING PLAN, please use make_plan")
            
    def show_interactions(self):
        if(self.inter != []):
            print(self.inter)
        else:
            print("NO EXISTING PLAN, please use make_plan")
    
    def show_generators(self):
        if(self.inter != []):
            if(len(self.generators) == 0):
                print("No generator, complete plan")
            else:
                print(self.generators)
        else:
            print("NO EXISTING PLAN, please use make_plan")
        
    def show_effects(self):
        if(self.y != []):
            A = self.effects
            for j in range(len(A)):
                print(A[j][0]+" : "+str(A[j][1]))
        else:
            print("No y values")
            
    def make_regressX(self):
        if(len(self.req) > 0):
            Xm = np.array([np.ones(self.Exp.shape[0]).tolist()]).T
            pos = np.arange(0,self.Exp.shape[1])
            for j in range(len(self.req)):
                FF = np.array(self.req[j])==1
                pos_sel = pos[FF]
                v = np.array([np.prod(self.Exp[:,pos_sel],axis=1)]).T
                Xm = np.append(Xm,v,axis=1)
            return Xm



def mlregress(y,X,constant=False):
    
    # Modify y if necessary
    if(isinstance(y, list)):
        y = np.array([y]).T
    elif(y.shape[0]==1):
        y = y.T
    
    # Check dimensions
    X =  np.array(X)
    if(X.shape[0]!=y.shape[0]):
        raise ValueError("Dimensions mismatch")
    
    # Add constant if required
    if(constant):
        oo = np.ones([X.shape[0],1])
        X = np.append(X,oo,axis=1)
        
  
    results = sm.OLS(y,X).fit()
    print(results.summary())
    
    b = np.linalg.inv(X.T@X)@X.T@y
    
    return b 
        


def ac(c1,c2):
    
    if(isinstance(c1, list)):
        c1 = np.array([c1]).T
    elif(len(c1.shape)==1):
        c1 = np.array([c1]).T
    
    if(isinstance(c2, list)):
        c2 = np.array([c2]).T
    elif(len(c2.shape)==1):
        c2 = np.array([c2]).T
    
    if(c1.shape[0]==c2.shape[0]):
        X = np.append(c1,c2,axis=1)
    elif(c1.shape[0]==c2.shape[1]):
        X = np.append(c1,c2.T,axis=1)
    elif(c1.shape[1]==c2.shape[0]):
        X = np.append(c1.T,c2,axis=1)    
    else:
        raise ValueError("Dimensions mismatch")
    return X

