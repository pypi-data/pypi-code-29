import pandas as pd
import numpy as np
import codecs
#import random
#import string as st
# pip3 install filemagic
#import magic
import logging
#import json
#import pprint
#import spacy
from string import punctuation
from collections import Counter
#import operator
import constants
import fitter

CONFIG = {
    'LOGFILE': 'data_template.log',   # logfile path
    'CHUNKSIZE': 4096,                # size of chunk for merkle tree generation
}

import re
REGEX_EMAIL = re.compile(r'[\w\-][\w\-\.]+@[\w\-][\w\-\.]+[a-zA-Z]{1,4}')


#import en_core_web_sm
#nlp = en_core_web_sm.load()


# TODO refactor to crypto.py or utils.py
def hash_chunk(path, chunksize=4096, codec='hex'):
    """ Build merkle tree of chunked file and return both tree and root """

    import merkle
    trie = merkle.MerkleTree()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(chunksize), b''):
            trie.add(chunk)
        # Building merkle tree (root hash)
        merkle_root = trie.build()
        if codec=='hex':
            merkle_root = codecs.encode(merkle_root, 'hex_codec')
            logging.info('Data Merkle root %s', merkle_root)
    return trie.get_all_hex_chains(), merkle_root



class ColumnStats:
    def __init__(self, n_elems=None, top_k=10):
        self.n_elems = n_elems
        self.first_uppercase = 0     # num records first uppercase
        self.num_uppercase = 0       # num records uppercase
        self.length = []             # len of each record
        self.special_chars = []      # num of special chars in each record
        self.top_k = top_k

    def string_update(self, string):
        self.string = str(string)
        # check uppercase
        if self.string[0].isupper():
            self.first_uppercase += 1
        if self.string.isupper():
            self.num_uppercase += 1
        # len of each record
        self.length.append(len(self.string))
        # check special chars
        string_special_chars = 0
        for p in set(punctuation):
            if p in self.string:
                string_special_chars += 1
        self.special_chars.append(string_special_chars)

    def get_stats(self, rate = False):
        stats = {}
        stats['first_uppercase'] = self.first_uppercase

        len_counts = Counter(self.length)
        res = {}
        for k, v in len_counts.most_common(self.top_k):
            if rate:
                res[k] = round(1.*v/self.n_elems, 3)
            else:
                res[k] = v

        stats['length'] = res
        stats['special_chars'] = {}
        special_chars_counts = Counter(self.special_chars)
        res = {}
        for k, v in special_chars_counts.most_common(self.top_k):
            if rate:
                res[k] = round(1. * v / self.n_elems, 3)
            else:
                res[k] = v

        stats['special_chars'] = res
        stats['num_uppercase'] = self.num_uppercase
        return stats


class DataTemplate:
    def __init__(self, distrib = True):
        self.col_names  = []
        self.col_types  = {}
        self.col_values = {}
        self.schema = {}  # public schema

        # set configuration
        self.config = CONFIG
        self.config['REVEAL_DISTRIB'] = distrib  # fit best distribution to columnar data

        logging.basicConfig(filename=CONFIG['LOGFILE'], level=logging.DEBUG,
                            format='%(asctime)s - %(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S %p')
        logging.info('Initialized DataTemplate class')


    def load_data(self, filepath, merkle=True, codec='hex'):
        """ Load csv file into dataframe """
        # Determine file type to generate template of
        # TODO this is a hassle to get working. Can we do a more pragmatic approach by checking
        # on extension instead of using this wrapper?
        # with magic.Magic() as m:
        #    self.filetype = m.id_filename(filepath)
        # print('Detected file type', self.filetype)
        logging.info('Loading data from %s', filepath)

        # TODO read according to file type
        # Set dataframe
        self.dataframe = pd.read_csv(filepath, index_col=False)
        self.rows, self.cols = self.dataframe.shape

        # update schema
        self.schema['filetype'] = 'csv'
        self.schema['type'] = 'record'
        self.schema['description'] = ''
        self.schema['format'] = 'pandas.dataframe'

        # build merkle tree per row
        if merkle:
            logging.info('Building Merkle tree from original datafile')
            t, r = hash_chunk(filepath)
            self.trie = t

    def __element_type(self, s):
        """
        Entity Recognizer for primitive and complex types

        Primitive types
        int, float, int_neg, float_neg, bool, string (regex)

        Complex types
        email
        organization
        location
        person

        """

        int_types = (int, np.int32, np.int64)
        float_types = (np.float64, float)

        for it in int_types:
            if isinstance(s, it):
                return constants.FITCHAIN_INT

        for ft in float_types:
            if isinstance(s, ft):
                return constants.FITCHAIN_FLOAT

        if isinstance(s, np.bool):
            return constants.FITCHAIN_BOOL

        if isinstance(s, str):
            # match for email addresses
            foundemail = re.search(REGEX_EMAIL, s)
            if foundemail:
                return constants.FITCHAIN_EMAIL

            # TODO add regex for Name, Surname
            # TODO add regex for dates
            # TODO add regex for location


            #doc = nlp(s)
            #ent = doc[0].ent_type_
            #if ent:
                #return 'fitchain/' + ent
            #    pass

            return constants.FITCHAIN_STRING
        return False

    def get_template(self):
        """
        Collect stats for this dataframe and set data template
        for lazy generation
        Return json schema
        """

        if self.dataframe is None:
            logging.warning('Load data first, eg. call load_data(filepath)')
            return None

        # Generate fake data starting from column properties
        self.col_names  = self.dataframe.columns

        # set merkle tree of this datasource
        # TODO this is the ugliest way to serialize the merkle tree (!!) please fix this *shit*
        self.schema['merkle'] = str(self.trie)

        # Array of fields metadata
        self.schema['fields'] = []

        # Read columns from tabular format file
        for c in self.col_names:
            logging.info('Processing column %s (detecting types)', c)
            # create field metadata
            field = {}
            field['name'] = str(c)

            # Get all elements of this column
            this_col_values = self.dataframe[c]
            n_elements = len(this_col_values)

            # Get unique values of this column
            unique_col_values = len(set(this_col_values))
            self.col_values[c] = unique_col_values

            # Get types in this column
            column_datatype = {}

            # Statistics of this column
            column_stats = ColumnStats(n_elems = n_elements)
            for element in this_col_values:
                element_type = self.__element_type(element)
                # collect stats for this element and update column stats
                column_stats.string_update(str(element))
                #if c == 'Size':
                #    print('%s len=%s'%(element, len(str(element))))
                try:
                    column_datatype[element_type] +=1
                except:
                    column_datatype[element_type] = 1

            logging.info('Detected column datatype %s', column_datatype)
            logging.info('Statistics of column %s %s', c, column_stats.get_stats())

            if self.config['REVEAL_DISTRIB']:
                # if this column has only one type in FITCHAIN_INT, FITCHAIN_FLOAT
                col_type = list(column_datatype.keys())
                if len(col_type)==1 and col_type[0] in (constants.FITCHAIN_INT,
                                                        constants.FITCHAIN_FLOAT):
                    print('Column ', c, 'is numeric. Fitting stat distrib')
                    # Find best fit distribution (discard NaNs)
                    datafitter = fitter.Fitter(this_col_values)
                    field['distrib'] = datafitter.fit()
                else:
                    print('\n')
                    print('Column ', c, 'not numeric. Skipping fitting')

            self.col_types[c] = column_datatype
            field['type'] = column_datatype
            field['stats'] = column_stats.get_stats(rate=True)
            # append this field to schema
            self.schema['fields'].append(field)

        logging.info('Terminated')

        # Return schema as dictionary
        return self.schema
