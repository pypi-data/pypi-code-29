"""
Sparse matrix library
"""



import numpy as np
import pandas as pd
import scipy.sparse
import csv
import os

class Loc(object):
    def __init__(self, df):
        self.__df = df
    
    @property    
    def df(self):
        return self.__df
    
    @staticmethod
    def get_indices(k, index):
        """
        Return the indices related to k where k can be a list of indices,
        a list of search terms or a single index.
        
        Parameters
        ----------
        k : int, str, list, tuple
            Either indices or search terms to find indices
        index : pd.Index
            A row or column index to search
        """
        
        if isinstance(k, str):
            # find index in str
            ix = np.where(index == k)[0]
        else:
            # Test if index is list that contains strings as we can
            # do matching on that
            
            strs = False
            
            if isinstance(k, list) or isinstance(k, tuple):
                for x in k:
                    if isinstance(x, str):
                        strs = True
                        break
            
            if strs:
                # If there are strings, assume we want to do a search
                ix = np.where(index.isin(k))[0]
            else:
                # If all else fails, use k as is
                ix = k
            
        return ix
    
    def __getitem__(self, key):
        if len(key) != 2:
            return None
        
        ix = Loc.get_indices(key[1], self.df.columns)
        iy = Loc.get_indices(key[0], self.df.index)
            
        return SparseDataFrame(self.df.matrix[iy, ix], index=self.df.index[iy], columns=self.df.columns[ix])
    

class SparseDataFrame(object):
    def __init__(self, matrix, index=None, columns=None):
        if isinstance(matrix, scipy.sparse.csc.csc_matrix):
            self.__matrix = matrix
        if isinstance(matrix, scipy.sparse.csr.csr_matrix):
            self.__matrix = matrix.tocsc()
        else:
            self.__matrix = scipy.sparse.csc.csc_matrix(matrix)
        
        self.index = index
        self.columns = columns
    
    @property    
    def matrix(self):
        return self.__matrix

    @property
    def index(self):
        return self.__index
    
    @index.setter
    def index(self, index):
        if index is None:
            return
        
        if isinstance(index, pd.Index):
            self.__index = index
        else:
            self.__index = pd.Index(index)
        
    @property
    def columns(self):
        return self.__columns
    
    @columns.setter
    def columns(self, index):
        if index is None:
            return
        
        if isinstance(index, pd.Index):
            self.__columns = index
        else:
            self.__columns = pd.Index(index) #np.array(columns)
    
    @property
    def loc(self):
        return Loc(self)
    
    @property
    def T(self):
        return self.transpose()
    

    def transpose(self):
        return SparseDataFrame(self.matrix.transpose(), index=self.columns, columns=self.index)
    
    def toarray(self):
        return self.matrix.toarray()
    
    def __getitem__(self, key):
        return self.loc[key]
    
    def remove_empty_rows(self):
        return self[np.where(self.sum(axis=1) > 0)[0],:]
    
    @property
    def array(self):
        return self.toarray()
    
    @property
    def shape(self):
        """
        Return the matrix dimensions.
        
        Returns
        -------
        tuple
            The dimensions of matrix
        """
        
        return self.__matrix.shape
    
    def save(self, name, header=True, index=True):
        """
        Save sparse dataframe to file.
        
        Parameters
        ----------
        name : str
            Name to save file to which can include directory prefix. The
            files will be created by adding suffixes to the name to create
            a set of three files representing the columns, rows and matrix
        """
        
        scipy.sparse.save_npz('{}.npz'.format(name), self.matrix, compressed=True)
        index_to_csv('{}.index.tsv'.format(name), self.index, 'Gene')
        index_to_csv('{}.columns.tsv'.format(name), self.columns, 'Barcode')
        
        
    def sum(self, axis=0):
        """
        Return the sum of values along a matrix dimension.
        
        Parameters
        ----------
        axis : int, optional
            The dimension (0 = columns, 1 = rows) along which to return the
            sums.
        """
        
        return np.asarray(self.matrix.sum(axis=axis)).ravel()

    
    def multiply(self, x):
        return SparseDataFrame(self.matrix.multiply(x), index=self.index, columns=self.columns)
    
    
    def apply(self, f):
        m = self.matrix.astype(np.float64)
        
        m.data = f(m.data)

        return SparseDataFrame(m, index=self.index, columns=self.columns)
    
    
    def copy(self):
        """
        Return a copy of the matrix
        """
        
        return SparseDataFrame(self.matrix.copy(), index=self.index, columns=self.columns)
    
    
    def _copy(self, t=np.float64):
        return self.matrix.copy().astype(t)
    
    
    def power(self, p):
        """
        Raise base to power of each element.
        
        Parameters
        ----------
        p : float
            The base.
        
        Returns
        -------
        SparseDataFrame
            A copy of the data frame with p^x.
        """
        
        # copy data
        m = self._copy()
        
        m.data = np.power(2, m.data)
        
        return SparseDataFrame(m, index=self.index, columns=self.columns)
    
    def log2(self, add=1):
        """
        Log2 all data values.
        
        Parameters
        ----------
        add : float, optional
            Defaults to adding 1 to data values to cope with zero entries
        
        Returns
        -------
        SparseDataFrame
            A copy of the data frame with log2 values.
        """
        
        # copy data
        m = self._copy()
        
        # inplace add 1
        np.add(m.data, 1.0, out=m.data)
        
        # in place log2
        np.log2(m.data, out=m.data)
        
        return SparseDataFrame(m, index=self.index, columns=self.columns)
        
        
def read_sparse(prefix):
    """
    Read sparse matrix files from disk into a dataframe.
    
    Parameters
    ----------
    prefix : str
        The name of the file set (its common prefix) which can include the
        directory the files are in.
    
    Returns
    -------
    SparseDataFrame
        A sparse data frame representing a matrix with row and column headings
    """
    
    f = '{}.npz'.format(prefix)
    
    if not os.path.exists(f):
        print('There does not appear to be any data located at {}.'.format(prefix))
        return None
    
    matrix = scipy.sparse.load_npz(f)
    
    f = '{}.index.tsv'.format(prefix)
    
    if not os.path.exists(f):
        return None
    
    index = read_index(f)
    
    f = '{}.columns.tsv'.format(prefix)
    
    if not os.path.exists(f):
        return None
    
    columns = read_index(f)
    
    return SparseDataFrame(matrix, index=index, columns=columns)
    

def index_to_csv(f, data, name):
    """
    Write an index to file.
    
    Parameters
    ----------
    f : str
        filename to write to
    data : numpy.ndarray
        values to write to file, one per row
    name : str
        heading in file (usually ignored when reading).
    """
    
    f = open(f, 'w')

    try:
        writer = csv.writer(f)
        writer.writerow([name])
        for d in data:
            writer.writerow([d])
    finally:
        f.close()
        
        
def read_index(f):
    """
    Read indices/column headings from a tsv file.
    
    Parameters
    ----------
    f : str
        File to read
        
    Returns
    -------
    np.array
        An array of strings
    """
    
    f = open(f, 'r')
    
    reader = csv.reader(f)
    
    # skip the header
    next(reader) 
    
    d = []
    
    try:
        for tokens in reader:
            # Only append the first element in the row
            d.append(tokens[0])
    finally:
        f.close()
        
    return np.array(d)