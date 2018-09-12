import tensorflow as tf
import random

def prop(type_list,fn):
    """
    >>> prop(["boolean"],lambda b: b)
    False
    >>> prop(["int"],lambda x: (1 <= x and x <= 100))
    True
    >>> prop(["int","boolean"],lambda x,b : (1 <= x and x <= 100) and b)
    False
    """
    num_dim = 10
    max_dim = 100
    min_dim = 1
    random_list = []

    for j in type_list:
        if j == "boolean":
            random_list.append(lambda : random.randint(0, 1) == 1)
        elif j =="int":
            random_list.append(lambda : random.randint(min_dim, max_dim))
        else:
            random_list.append(lambda : random.randint(min_dim, max_dim))

    for i in range(num_dim):
        arg = list(map(lambda x: x(),random_list))
        v = fn(*arg)
        if not v :
            return False

    return True

def shape2list(shape):
    def myint(x):
        try:
            return int(x)
        except:
            return None
    x_shape = list(map(myint, list(shape)))
    return x_shape

def shape_eq(x,shape):
    """
    >>> shape_eq("hogehoge",None)
    True
    >>> shape_eq("hogehoge",[1,2,3])
    False
    >>> shape_eq(tf.zeros([1,2,3],dtype=tf.float32),[1,2,3])
    True
    >>> shape_eq(tf.zeros([1,2,3],dtype=tf.float32),[1,2,4])
    shape: exp=[1, 2, 4] got=[1, 2, 3]
    False
    >>> shape_eq(tf.placeholder(tf.float32,[None,2,3]),[None,2,3])
    True
    """
    if shape == None:
        return True
    elif not hasattr(x,"shape"):
        return False
    else:
        def myint(x):
            try:
                return int(x)
            except:
                return None
        x_shape = shape2list(x.shape)
        t = x_shape == shape
        if not t:
            print(f"shape: exp={shape} got={x_shape}")
        return t

def dtype_eq(x,dtype):
    """
    >>> dtype_eq("hogehoge",None)
    True
    >>> dtype_eq("hogehoge",tf.float32)
    False
    >>> dtype_eq(tf.zeros([1,2,3],dtype=tf.float32),tf.float32)
    True
    """
    if dtype == None :
        return True
    elif not hasattr(x,"dtype"):
        return False
    else:
        return x.dtype == dtype

def type_eq(x,shape,dtype):
    return shape_eq(x,shape) and dtype_eq(x,dtype)

def inout_eq(fn,in_shape,in_dtype,out_shape,out_dtype):
    v = fn(tf.zeros(in_shape,dtype=in_dtype))
    r = type_eq(v,out_shape,out_dtype)
    return r

