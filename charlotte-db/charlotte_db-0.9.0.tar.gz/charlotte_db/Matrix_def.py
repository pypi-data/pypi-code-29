import re
from numpy import ndarray
import sys
import numpy as np
import tensorflow as tf


def digit_float_str(str):
    try:
        final = int(str)
    except ValueError:
        try:
            final = float(str)
        except ValueError:
            return final
    return final


def py_matrix_to_str(matrix):
    # Check if is a vector
    term = False
    for item in matrix:
        term = not isinstance(item, list)
        if not term:
            break
    if term:
        return ','.join(map(str, matrix))

    # Check if matrix is valid
    if not isinstance(matrix, list):
        raise TypeError('Expecting valid python matrix - Got ' + str(type(matrix)) + ' instead')
    temp = -1
    for row in matrix:
        if not isinstance(row, list):
            raise Exception('py_matrix_to_string - Not a valid matrix')
        curr = len(row)
        if (temp == -1):
            temp = curr
        if (temp != curr):
            raise Exception('py_matrix_to_string - Python matrix not valid - Was expecting an n x m matrix')

    # Convert matrix to string
    col_delim = ' '
    row_delim = ';'
    if isinstance(matrix[0][0], float):
        return "PYTHON_" + row_delim.join(col_delim.join('%0.5f' % x for x in y) for y in matrix)
    if isinstance(matrix[0][0], int):
        return "PYTHON_" + row_delim.join(col_delim.join('%0.0f' % x for x in y) for y in matrix)
    if isinstance(matrix[0][0], str):
        return "PYTHON_" + row_delim.join(col_delim.join(x for x in y) for y in matrix)
    else:
        return "PYTHON_" + row_delim.join(col_delim.join(x for x in y) for y in matrix)


def str_to_py_matrix(input_string):
    if input_string[:6] == "PYTHON":
        matrix = str_to_np_matrix(input_string)
        return matrix
    else:
        return "String is not from a 2D list matrix string"


def np_matrix_to_str(matrix):
    col_delim = ' '
    row_delim = ';'
    if not isinstance(matrix, ndarray):
        raise Exception('Was Expecting a numpy array as input - Got a ' + str(type(matrix)) + ' instead')
    try:
        if matrix.ndim == 1:
            return col_delim.join(x for x in matrix)
        for (x, y), value in np.ndenumerate(matrix):
            if isinstance(matrix[x, y], str):
                matrix[x, y] = matrix[x, y].replace(' ', '##')
        if matrix.ndim == 2:
            #Check the type of data inside the numpy array using .dtype property
            #and string the data accordingly
            input_type = np.array(matrix)
            input_type = str(input_type.dtype)
            if 'float' in input_type:
                matrix = row_delim.join(col_delim.join('%0.5f' % x for x in y) for y in matrix)
                matrix = matrix.replace("; ;", " ")
                matrix = matrix.replace(";;;", ";")
                return "NUMPY_" + matrix.replace(";.;", ".")
            if 'int' in input_type:
                matrix = row_delim.join(col_delim.join('%0.0f' % x for x in y) for y in matrix)
                matrix = matrix.replace("; ;", " ")
                return "NUMPY_" + matrix
            if 'str' in input_type:
                matrix = row_delim.join(col_delim.join(x for x in y) for y in matrix)
                matrix = matrix.replace("; ;", " ")
                matrix = matrix.replace(";;;", ";")
                return "NUMPY_" + matrix
            else:
                return "NUMPY_" + row_delim.join(col_delim.join(x for x in y) for y in matrix)
        else:
            raise Exception('Was expecting a numpy matrix. Got a ' + str(matrix.ndim) + 'D numpy instead')
    except TypeError:
        raise Exception('Input matrix is not valid')


def str_to_np_matrix(input_str):
    if sys.version_info[0] < 3:
        input_str = input_str.split('_')
    else:
        input_str = input_str.decode('utf-8')
        input_str = input_str.split('_')
    input_str = input_str[1]
    if not isinstance(input_str, str):
        raise Exception("Was expecting str but got " + str(type(input_str)) + " instead")
    try:
        matrix = np.matrix(input_str)
    except NameError:
        input_str = input_str.replace(';', '"],["')
        input_str = input_str.replace(' ', '","')
        input_str = '[["' + input_str + '"]]'
        # Replace ## for spaces
        input_str = input_str.replace('##', ' ')
        input_str = input_str.replace('[,', '[')
        matrix = np.matrix(eval(input_str))
        for (x, y), value in np.ndenumerate(matrix):
            if matrix[x, y].isdigit():
                matrix[x, y] = int(matrix[x, y])
    except TypeError:
        input_str = input_str.replace(';', '"],["')
        input_str = input_str.replace(' ', '","')
        input_str = '[["' + input_str + '"]]'
        matrix = np.matrix(eval(input_str))
        for (x, y), value in np.ndenumerate(matrix):
            if matrix[x, y].isdigit():
                matrix[x, y] = int(matrix[x, y])
    return matrix


def tensor_to_str(tensor):
    session = tf.Session()
    #read in tensor contents
    str_tensor = str(session.run(tensor))
    #Tensor parsing
    str_tensor = str_tensor.replace('\n', ',')
    pattern = re.compile(r'(,){2,}')
    pattern_s = re.compile(r'(\s){2,}')
    str_tensor = re.sub(pattern_s, ',', str_tensor)
    str_tensor = re.sub(' ', ',', str_tensor)
    str_tensor = re.sub(pattern, ',', str_tensor)
    str_tensor = re.sub(r"(?!(([^']*'){2})*[^']*$),", " ", str_tensor)
    str_tensor = str_tensor.replace("[,", '[')
    type = tf.Variable(tensor)
    type = str(type.dtype)
    type = re.search("'(.*)'", type)
    #Add meta data to string
    str_tensor = str_tensor + "_" + type.group(1) + "_tensor"
    session.close()
    return str_tensor


def str_to_tensor(str_tensor):
    if sys.version_info[0] < 3:
        str_tensor = str_tensor.split('_')
    else:
        str_tensor = str_tensor.decode('utf-8')
        str_tensor = str_tensor.split('_')
    np_array = np.array(eval(str_tensor[0]))
    tensor_type = str_tensor[1]
    if str_tensor[3] != "tensor":
        raise Exception("String is not a tensor")
    tensor = tf.convert_to_tensor(np_array)
    tensor = tf.cast(tensor, tensor_type)
    return tensor