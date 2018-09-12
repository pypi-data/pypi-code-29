import numpy as np
import base64
import ndex2
import ndex2.client as nc
import os
from ndex2.NiceCXNetwork import NiceCXNetwork
from ndex2.client import DecimalEncoder
from ndex2cx.NiceCXBuilder import NiceCXBuilder
import time

upload_server = 'dev.ndexbio.org'
upload_username = 'username'
upload_password = 'password'


params = {
    'name': 'SIM MATRIX TEST',
    'ndex_server': 'http://dev.ndexbio.org',
    'ndex_user': 'scratch3',
    'ndex_pass': 'scratch3'
}

X = np.array(
    [[1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0],
     [0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0],
     [0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0],
     [0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0],
     [0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0],
     [0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0],
     [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1],
     [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1],
     [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1]]
)

X_cols = ['ABC', 'DEF', 'GHI', 'XYZ', 'ABC1', 'DEF1', 'GHI1', 'XYZ1', 'ABC2', 'DEF2', 'GHI2', 'XYZ2', 'ABC3', 'DEF3', 'GHI3']
X_rows = ['ABC', 'DEF', 'GHI', 'XYZ', 'ABC1', 'DEF1', 'GHI1', 'XYZ1', 'ABC2', 'DEF2', 'GHI2', 'XYZ2', 'ABC3', 'DEF3', 'GHI3']


def load_matrix_to_ndex(X, X_cols, X_rows, upload_server, upload_username, upload_password):

    #ndex2.get_matrix_from_ndex(upload_server, upload_username, upload_password, '56312486-7b19-11e8-8b82-525400c25d22')
    ndex2.load_matrix_to_ndex(X, X_cols, X_rows, upload_server, upload_username, upload_password, 'ndex2 test')

    if False:
        if not X.flags['C_CONTIGUOUS']:
            X = np.ascontiguousarray(X)

        serialized = base64.b64encode(X)

        niceCxBuilder = NiceCXBuilder()
        node_id = niceCxBuilder.add_node(name='Sim Matrix', represents='Sim Matrix')
        niceCx = niceCxBuilder.get_nice_cx()

        niceCxBuilder.add_opaque_aspect('matrix', [{'v': serialized.decode('ascii')}])
        niceCxBuilder.add_opaque_aspect('matrix_cols', [{'v': X_cols}])
        niceCxBuilder.add_opaque_aspect('matrix_rows', [{'v': X_rows}])
        niceCxBuilder.add_opaque_aspect('matrix_dtype', [{'v': X.dtype.name}])
        niceCx = niceCxBuilder.get_nice_cx()
        #G_cx = NdexGraph()
        #G_cx.unclassified_cx.append(
        #    {'matrix': [serialized]})

        #G_cx.unclassified_cx.append(
        #    {'matrix_cols': X_cols})

        #G_cx.unclassified_cx.append(
        #    {'matrix_rows': X_rows})

        #G_cx.unclassified_cx.append(
        #    {'matrix_dtype': [X.dtype.name]})

        #node_id = G_cx.add_new_node(name='ABC')
        #G_cx.add_edge_between(node_id, node_id)
        #G_cx.set_name(params['name'])
        #G_cx.set_network_attribute('Description', 'testing sim matrix storage')

        print(X)
        ont_url = niceCx.upload_to(upload_server, upload_username, upload_password)
        #ont_url = G_cx.upload_to(params['ndex_server'], params['ndex_user'], params['ndex_pass'])

        return ont_url


#load_matrix_to_ndex(X, X_cols, X_rows, params['ndex_server'], params['ndex_user'], params['ndex_pass'])
new_network_url = ndex2.load_matrix_to_ndex(X, X_cols, X_rows, params['ndex_server'], params['ndex_user'], params['ndex_pass'], 'matrix test')
uuid = new_network_url.split('/')[-1]
time.sleep(2)
new_network = ndex2.get_matrix_from_ndex(params['ndex_server'], params['ndex_user'], params['ndex_pass'], uuid)
print(new_network.get_summary())
#def get_matrix_from_ndex(X, X_cols, X_rows):
#    for aspect in cx:
#        if 'matrix' in aspect:
#            assert 'matrix_dtype' in aspect
#            assert 'matrix_cols' in aspect
#            assert 'matrix_rows' in aspect

            # Convert text back into binary data
#            binary_data = base64.decodestring(aspect.get('matrix'))

#            dtype = np.dtype(aspect.get('matrix_dtype'))
#            rows = aspect.get('matrix_rows')
#            cols = aspect.get('matrix_cols')
#            dim = (len(rows), len(cols))

            # Create a NumPy array, which is nothing but a glorified
            # pointer in C to the binary data in RAM
#            X = np.frombuffer(binary_data, dtype=dtype).reshape(dim)

#    return X, rows, cols

#    return ont_url

