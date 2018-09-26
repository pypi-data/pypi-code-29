# -*- coding: utf-8 -*-

"""Constants for Bio2BEL UniProt."""

import os

from bio2bel import get_data_dir

MODULE_NAME = 'uniprot'

DATA_DIR = get_data_dir(MODULE_NAME)

MAPPINGS_URL = 'ftp://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/idmapping/' \
               'by_organism/HUMAN_9606_idmapping_selected.tab.gz'
MAPPINGS_PATH = os.path.join(DATA_DIR, 'HUMAN_9606_idmapping_selected.tab.gz')
SLIM_MAPPINGS_PATH = os.path.join(DATA_DIR, 'slim.HUMAN_9606_idmapping_selected.tab.gz')
