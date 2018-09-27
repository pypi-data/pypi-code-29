"""Methods to look for available data from output directory."""

import os
import re
import numpy as np
import pandas as pd

from .parse import parse_conf, XmlTree


def scan_fields(configfile: str, outputdir: str = None) -> pd.DataFrame:
    '''Return a pandas.DataFrame describing available 2D binary files.

    Data is looked for in <outputdir>.
    '''
    config    = parse_conf(configfile)
    if outputdir is None:
        outputdir = Scan.search(config, 'outputdir', str)
    fields    = Scan.get_2d_files(outputdir)

    finums = [Scan.get_file_number(fi) for fi in fields]
    maxoutput = np.max(finums)
    available = pd.DataFrame(index=range(maxoutput+1))
    for tag in Scan.get_tags(fields):
        fitag = Scan.get_filetag(tag)
        dat = ["gas%s%d.dat" % (fitag,n) in fields for n in range(maxoutput+1)]
        available[tag] = pd.Series(dat, index=available.index)
    return available


def scan_profiles(configfile: str, outputdir: str = None) -> pd.DataFrame:
    '''Return a pandas.DataFrame describing available 1D ascii files.

    Data is looked for in <outputdir>.
    '''
    config    = parse_conf(configfile)
    if outputdir is None:
        outputdir = Scan.search(config, 'outputdir', str)
    profiles  = Scan.get_1d_files(outputdir)

    try:
        maxoutput = np.max([Scan.get_file_number(fi) for fi in profiles])
    except ValueError:
        return None
    available = pd.DataFrame(index=range(maxoutput+1))
    for tag in Scan.get_tags(profiles, dim=1):
        fitag = Scan.get_filetag(tag)
        dat = ["%s%d.dat" % (fitag,n) in profiles for n in range(maxoutput+1)]
        available[tag] = pd.Series(dat, index=available.index)
    return available


class Scan:
    '''A small namespace embedding chunks of the main function 'scan_fields'.'''
    @staticmethod
    def search(
            configtree : XmlTree,
            attr : str,
            convert = lambda x: x
    ):
        '''Fetch a parameter from configtree and convert it.'''
        attr = attr.lower()
        res = configtree.find('.//*[@%s]' % attr)
        if res is None:
            raise AttributeError(f'Could not find parameter <{attr}>')
        rawattr = res.get(attr)
        return convert(rawattr)

    @staticmethod
    def get_2d_files(path: str) -> list:
        '''Return a list of files found in <path> with prefix 'gas'.

        Namely the 2d binary arrays.
        '''
        found = list(filter(lambda x: x.startswith('gas'), os.listdir(path)))
        return found

    @staticmethod
    def get_1d_files(path: str) -> list:
        '''Return a list of files found in <path> with '1D' in their name.

        Namely the 1D ascii arrays.
        '''
        found = list(filter(lambda x: '1D' in x, os.listdir(path)))
        return found

    @staticmethod
    def get_planet_files(path: str) -> list:
        '''Return a list of found planet related log files.'''
        found = list(filter(lambda x:
                            x.startswith('planet')
                            or x.startswith('orbit')
                            or x.startswith('acc'), os.listdir(path)))
        return found

    @staticmethod
    def get_file_number(filename : str) -> int:
        '''Return an integer contained in the filename.'''
        raw = re.search(r'\d+.dat', filename).group(0)
        file_number = int(raw[:-4])
        return file_number

    @staticmethod
    def get_tags(filelist: list, dim: int = 2) -> list:
        '''Return all unique tags from <dim>D files.

        Dimension of data array is assumed to be implicit from the filename.
        Used formats :
              if dim==2: 'gas<tag><outnum>.dat'
              if dim==1: '<tag>1D<num>_<outnum>.dat
        '''
        tags = []
        if dim == 2:
            cut = 3 # handling the "gas" prefix
            dimtag = ''
        elif dim == 1:
            dimtag = '1D'
            cut = 0
        else:
            raise ValueError('dim should be either 1 or 2.')

        for fi in filelist:
            if '_' in fi:
                exp = r'[a-zA-Z]+%s\d+' % (dimtag)
            else        :
                exp = r'[a-zA-Z]+%s'    % (dimtag)
            tag = re.search(exp,fi[cut:]).group(0)
            if tag not in tags:
                tags.append(tag)
        return tags

    @staticmethod
    def get_filetag(tag : str) -> str:
        '''Return the minimal string representing what dat is about'''
        if tag[-1] in '0123456789':
            fitag = ''.join([tag,'_'])
        else:
            fitag = tag
        return fitag
