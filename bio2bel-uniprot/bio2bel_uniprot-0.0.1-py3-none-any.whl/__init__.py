# -*- coding: utf-8 -*-

"""Bio2BEL UniProt is a package for downloading, parsing, storing, and serializing UniProt."""

from .parser import get_mappings_df, get_slim_mappings_df  # noqa: F401

__version__ = '0.0.1'

__title__ = 'bio2bel_uniprot'
__description__ = "A package for downloading, parsing, storing, and serializing UniProt"
__url__ = 'https://github.com/bio2bel/uniprot'

__author__ = 'Charles Tapley Hoyt'
__email__ = 'charles.hoyt@scai.fraunhofer.de'

__license__ = 'MIT License'
__copyright__ = 'Copyright (c) 2017-2018 Charles Tapley Hoyt'
