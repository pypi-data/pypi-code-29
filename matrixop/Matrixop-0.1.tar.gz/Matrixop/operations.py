import numpy as np
class Matrix(object):
    """
    Matrix class for computing basic matrix operations on data
    """    
        
    
    
    def add (self, a,b ):
        """Function to add two matrices together
        
        Args: 
            a - first matrix
            b- second matrix
        
        Returns: 
            d : addition of matrix a and b 
    
        """
        
        a = np.asmatrix(a) # converting a to array
        b = np.asmatrix(b) # converting b to array
        
        assert a.shape == b.shape , "Dimensions of both inputs must be equal"
        d =np.zeros((a.shape[0],a.shape[1]))
        for row in range(a.shape[0]):
    
            for col in range(a.shape[1]):
                d[row,col] = a[row,col] + b[row,col]
        return d
    
    def subtract(self, a, b):
        """Function to subtract two matrices
        
        Args: 
            a - first matrix
            b- second matrix
        
        Returns: 
            d : subtraction of matrix a and b 
    
        """
        
        a = np.asmatrix(a) # converting a to array
        b = np.asmatrix(b)  # converting b to array
        assert a.shape == b.shape , "Dimensions of both inputs must be equal"
        d =np.zeros((a.shape[0],b.shape[1]))  # creating a matrix of zeros
        for row in range(a.shape[0]):
    
            for col in range(a.shape[1]):
                d[row,col] = a[row,col] + b[row,col]
        return d
    
    def matmul(self,a, b):
        """Function to multiply 2 matrices
        
        Args: 
            a - first matrix
            b- second matrix
        
        Returns: 
            out : multiplication results of matrix a and b 
        """
        
        a = np.asmatrix(a)  # # converting a to array
        b = np.asmatrix(b) # # converting b to array
        
        assert a.shape[1] == b.shape[0], "column dimension of input 1 should be equal to row dimension of input 2"
           
        
        out = np.zeros((a.shape[0], b.shape[1]))
        for row in range(a.shape[0]):
        
    
            for col in range(b.shape[1]):
            
        
    
                for k in range(a.shape[1]):
                    out[row, col] += a[row, k] * b[k, col]
        return out
        
    
    def transpose(self, a):
        """Function to compute the transpose of a matrix
        
        Args: 
            a - matrix
        
        Returns: 
            tr : transpose of the matrix
    
        """
        rez = [[a[j][i] for j in range(len(a))] for i in range(len(a[0]))] 
        tr = np.asmatrix(rez)
        
        return tr
    
    def scalarMul(self, matrix ,scalar):
        """Function to multiply a matrix by a scalar
        
       Args: 
            matrix -  matrix
            scalar - scalar
        
        Returns: 
            mul : multiplication of the matrix by the scalar 
    
        """
        
        mul = np.zeros((matrix.shape[0],matrix.shape[1]))
        matrix = np.asmatrix(matrix)
        
        for row in range(matrix.shape[0]):
            for col in range(matrix.shape[1]):
                mul[row,col] = scalar * matrix[row, col] 
                
        return mul
                