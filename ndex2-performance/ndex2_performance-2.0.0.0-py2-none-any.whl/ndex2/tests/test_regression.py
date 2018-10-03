__author__ = 'aarongary'

import unittest

import json
import pandas as pd
import csv
import networkx as nx
import ndex2
import os
from ndex2cx.NiceCXBuilder import NiceCXBuilder

upload_server = 'dev.ndexbio.org'
upload_username = 'scratch'
upload_password = 'scratch'

path_this = os.path.dirname(os.path.abspath(__file__))


class TestRegression(unittest.TestCase):
    #@unittest.skip("Temporary skipping")
    def test_context(self):
        print('Testing: context')
        context = {
            'signor': 'http://signor.uniroma2.it/relation_result.php?id=',
            'BTO': 'http://identifiers.org/bto/BTO:',
            'uniprot': 'http://identifiers.org/uniprot/',
            'pubmed': 'http://identifiers.org/pubmed/',
            'CID': 'http://identifiers.org/pubchem.compound/',
            'SID': 'http://identifiers.org/pubchem.substance/',
            'chebi': 'http://identifiers.org/chebi/CHEBI:'
        }

        nice_cx_builder = NiceCXBuilder()
        nice_cx_builder.set_context(context)

        node_id_1 = nice_cx_builder.add_node(name='ABC', represents='ABC')
        node_id_2 = nice_cx_builder.add_node(name='DEF', represents='DEF')

        nice_cx_builder.add_node_attribute(node_id_1, 'testing_attr_double', [1.2, 2.5, 2.7])

        edge_id = nice_cx_builder.add_edge(id=1, source=node_id_1, target=node_id_2, interaction='test-relationship')

        nice_cx_builder.add_edge_attribute(edge_id, 'citation', ['pubmed:21880741'], type='list_of_string')

        nice_cx = nice_cx_builder.get_nice_cx()
        with open('my_cx.cx', 'w') as file:
            json.dump(nice_cx.to_cx(), file)

        upload_message = nice_cx.upload_to(upload_server, upload_username, upload_password)

        self.assertTrue(upload_message)

    @unittest.skip("Temporary skipping")
    def test_full_core_aspects_cx_file(self):
        print('Testing: Full_core_aspects.cx')
        path_to_network = os.path.join(path_this, 'Full_core_aspects.cx')

        with open(path_to_network, 'r') as ras_cx:
            nice_cx = ndex2.create_nice_cx_from_raw_cx(cx=json.load(ras_cx))

            upload_message = nice_cx.upload_to(upload_server, upload_username, upload_password)
            self.assertTrue(upload_message)

    @unittest.skip("Temporary skipping")
    def test_pandas_loading(self):
        print('Testing: edge_list_network_adrian_small.txt')
        path_to_network = os.path.join(path_this, 'edge_list_network_adrian_small.txt')
        niceCxBuilder = NiceCXBuilder()

        with open(path_to_network, 'r') as tsvfile:
            header = ['Source', 'Target']

            df = pd.read_csv(tsvfile,delimiter='\t',engine='python',names=header)

            nice_cx = ndex2.create_nice_cx_from_pandas(df) #NiceCXNetwork(pandas_df=df)

            upload_message = nice_cx.upload_to(upload_server, upload_username, upload_password)

            self.assertTrue('error' not in upload_message)

    @unittest.skip("Temporary skipping")
    def test_manual_build(self):
        print('Testing: Manual build with NiceCXBuilder')
        nice_cx_builder = NiceCXBuilder()

        node_id_1 = nice_cx_builder.add_node(name=1, represents=2)
        node_id_2 = nice_cx_builder.add_node(name='node%s' % str(2), represents='DEF')
        try:
            nice_cx_builder.add_node_attribute(node_id_1, 'testing_attr', None)
        except TypeError as te:
            print('Correctly identified bad node value')

        nice_cx_builder.add_node_attribute(node_id_1, 'testing_attr_double', [1.2, 2.5, 2.7])

        nice_cx_builder.add_node_attribute(node_id_1, 'testing_attr_int', [16, 4, 8])
        nice_cx_builder.add_node_attribute(node_id_1, 'testing_attr_int', [16, 4, 8]) # duplicate - should be ignored
        nice_cx_builder.add_node_attribute(node_id_1, 'testing_attr_int', [16, 4, 8]) # duplicate - should be ignored

        try:
            nice_cx_builder.add_node_attribute(node_id_1, 'testing_attr2', [10.2, 20.5, 'abc'], type='list_of_float')
        except ValueError:
            print('Correctly identified bad value in node attribute list')

        edge_id = nice_cx_builder.add_edge(id=1, source=node_id_1, target=node_id_2, interaction='test-relationship')

        nice_cx_builder.add_edge_attribute(edge_id, 'testing_attr', [1.2, 2.5, '2.7'], type='list_of_float')
        nice_cx_builder.add_edge_attribute(edge_id, 'testing_attr', [1.2, 2.5, '2.7'], type='list_of_float') # duplicate - should be ignored
        nice_cx_builder.add_edge_attribute(edge_id, 'testing_attr', [1.2, 2.5, '2.7'], type='list_of_float') # duplicate - should be ignored

        try:
            nice_cx_builder.add_edge_attribute(edge_id, 'testing_attr2', [10.2, 20.5, 'abc'], type='list_of_float')
        except ValueError:
            print('Correctly identified bad value in list')

        nice_cx_builder.set_name('Network manual build')
        nice_cx_builder.nice_cx.set_namespaces({'ndex context': 'http://dev.ndexbio.org'})
        nice_cx = nice_cx_builder.get_nice_cx()

        node_attrs = nice_cx.get_node_attributes(node_id_1)
        edge_attrs = nice_cx.get_edge_attributes(edge_id)

        upload_message = nice_cx.upload_to(upload_server, upload_username, upload_password)

        self.assertTrue(upload_message)

        node1_attr_double = nice_cx.get_node_attribute(node_id_1, 'testing_attr_double')
        self.assertTrue(node1_attr_double.get('d') == 'list_of_double')

        node1_attr_int = nice_cx.get_node_attribute(node_id_1, 'testing_attr_int')
        self.assertTrue(node1_attr_int.get('d') == 'list_of_integer')

        self.assertTrue(len(node_attrs) == 2)
        self.assertTrue(len(edge_attrs) == 1)


if __name__ == '__main__':
    unittest.main()


