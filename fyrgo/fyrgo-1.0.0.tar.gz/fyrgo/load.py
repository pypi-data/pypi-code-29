#-*-coding:utf-8-*-
"""Data loading class for fargOCA.

A DataLoader instance is essentially a dict of pandas.DataFrame
objects. It gathers all available data matching specified output
directory and offsets (output index).
"""

import configparser
from pathlib import Path
from math import atan2
from sys import getsizeof

import numpy as np
import pandas as pd

from fyrgo import utils
from fyrgo.utils import Scan
from fyrgo import __path__ as fypath

fypath = Path(fypath[0])

class DataLoader:
    '''An all-purpose data-frame loader.

    %%          content (public attributes)         %%
    --------------------------------------------------
    attribute    | type
    --------------------------------------------------
    <configfile> | str
    <outputdir>  | str
    <offsets>    | list (or other iterable container)
    <loaded>     | bool
    <fields>     | pandas.DataFrame
    <profiles>   | pandas.DataFrame
    <planets>    | pandas.DataFrame
    <grid>       | dict

    Usage and features :
      * <configfile> and <outputdir> are immutables. To change any of
        them, init a new instance.

      * <offsets> are mutable through load_arrays().

      * <planets> and <grids> are light enough that we always load everything.

      * <fields> and <profiles> are a lot heavier to hold at once in the RAM.
        One can choose not to load them by setting 'offsets=[]' or 'loadall=False'.
        To load from previously defined offsets, use load_arrays().
        To load from new offsets, use load_arrays(new_offsets).

      * center_onto_planet(num) transform 2D arrays so that the
        specified planet be visually at the azimuthal
        center. Azimuthal velocities are *not* transformed to the
        rotating frame of reference.

    __getitem__() provides access to objects contained by this class'
    attributes so that you can transparently switch from a specific
    load function present in this module to a Load class object
    without rewritting your script. The dict-like way to search for
    keys (e.g. "df['key']") is recommended against the pandas way
    (e.g. "df.key").
    '''

    def __init__(
            self,
            configfile : str,
            outputdir  : str  = None,
            offsets    : list = None,
            center     : int  = None,
            loadall    : bool = True,
            planet_files_formats: Path = fypath/'utils/default_planet_format.in'
    ):

        int_types = (int, np.int8, np.int16, np.int32, np.int64)
        if isinstance(offsets, int_types):
            offsets = [offsets]
        if isinstance(configfile, Path):
            configfile = str(configfile)

        if offsets is None:
            offsets = []
        self._offsets = offsets
        self._configfile = configfile
        self._config = utils.parse_conf(configfile) # this is a fyrgo.utils.XmlTree object
        self._set_outputdir(outputdir)

        self.is_loaded = False
        self._profiles = pd.DataFrame()
        self._fields   = pd.DataFrame()

        self.load_grid()
        self.load_planets(formats=planet_files_formats)
        if loadall:
            self.load_arrays()
        self.is_centered = False
        if center is not None:
            self.center_on_planet(planet_num=center)

    def load_arrays(self, new_offsets:list=None):
        '''Load self.fields and self.profiles from self.offsets or new_offsets.

        Implementation implies that if new_offsets == self.offsets,
        (re)loading is still applied.
        '''
        if new_offsets is not None:
            self.offsets = new_offsets #implies (self.is_loaded == False), see setter offsets()
        if not self.is_loaded:
            self.load_profiles()
            self.load_fields()
            self.is_loaded = True

    def load_fields(self, sort=True):
        '''Set self.fields from self.offsets.

        self.fields is a pandas.DataFrame featuring all available 2D
        arrays that meet self.offsets (output numbers).

        2D data files' names are assumed to be formatted as
        'gas<tag><offset>.dat'
        '''
        available_data = utils.scan_fields(self.configfile, self.outputdir)
        nr = Scan.search(self._config, 'nrad', int)
        ns = Scan.search(self._config, 'nsec', int)

        data = pd.DataFrame(columns=available_data.columns, index=self.offsets)
        for tag in data.columns:
            fitag = Scan.get_filetag(tag)
            arrs = []
            for num in self.offsets:
                try:
                    availability = available_data[tag][num]
                except KeyError:
                    availability = False
                if availability:
                    filename = f'{self.outputdir}/gas{fitag}{num}.dat'
                    arr = np.fromfile(filename).reshape((nr, ns)).T
                else:
                    arr = None
                arrs.append(arr)
            data[tag] = pd.Series(arrs, index=self.offsets)

        if sort:
            if int(pd.__version__.split('.')[1]) > 20:
                data = data.reindex(labels=sorted(data.columns), axis=1)
            else:
                data = data.reindex_axis(sorted(data.columns), axis=1)
        self._fields = data

    def load_profiles(self, sort=True):
        '''Set self._profiles from self.offsets.

        self._profiles is a pandas.DataFrame featuring all available
        1D arrays that meet self.offsets (output numbers).

        1D data files' names are assumed to be formatted as
        '<tag><offset>.dat'
        '''
        available_data = utils.scan_profiles(self.configfile, self.outputdir)
        try:
            data = pd.DataFrame(columns=available_data.columns, index=self.offsets)
            for tag in data.columns:
                fitag = Scan.get_filetag(tag)
                arrs = []
                for num in self.offsets:
                    try:
                        availability = available_data[tag][num]
                    except KeyError:
                        availability = False
                    if availability:
                        filename = f'{self.outputdir}/{fitag}{num}.dat'
                        arr = np.loadtxt(filename)
                    else: arr = None
                    arrs.append(arr)
                data[tag] = pd.Series(arrs, index=self.offsets)

            if sort:
                if int(pd.__version__.split('.')[1]) > 20:
                    data = data.reindex(labels=sorted(data.columns), axis=1)
                else:
                    data = data.reindex_axis(sorted(data.columns), axis=1)
            self._profiles = data
        except AttributeError:
            self._profiles = pd.DataFrame()

    def load_planets(self, formats=fypath/'utils/default_planet_format.in'):
        '''Set self.planets.

        self.planets is a pandas.DataFrame from planet-related files.

        The following files are targeted :
        'planet<n>.dat'
        'orbit<n>.dat'
        'acc<n>.dat'

        Version compatibility notice
        ----------------------------
        One can use different formats for files loaded here.
        To do so, write a .def file formatted like fyrgo/formats/default.def
        and specify it when creating you DataLoader instance.
        '''
        all_logs = Scan.get_planet_files(self.outputdir)
        if all_logs == []:
            self._planets = pd.DataFrame()
            return
        nb = np.max([Scan.get_file_number(fi) for fi in all_logs]) + 1 #count the planets

        fmts = configparser.ConfigParser()
        fmts.read(formats)

        cols = []
        dats = []
        for col in ['planet', 'orbit', 'acc']:
            fmt = fmts['Planet Files'].get(col).split()
            dat = []
            for n in range(nb):
                filename = ''.join([self.outputdir, '/', f'{col}{n}.dat'])
                try:
                    raw = np.loadtxt(filename)
                    dic = dict(zip(fmt, [raw[:, i] for i in range(raw.shape[1])]))
                    dat.append(pd.DataFrame.from_dict(dic))
                except FileNotFoundError:
                    print(f'Warning : file {filename} does not exist.')

            if dat: #True if list not empty
                cols.append(col)
                dats.append(dat)
        self._planets = pd.DataFrame.from_dict(dict(zip(cols, dats)))

    def load_grid(self):
        '''Set self.grid from description contained in self.configfile.

        self.grid is a dict of grid specifications and radial ticks.
        cell-center ticks : rmed
        cell-edges ticks  : rinf
        '''
        #devnote : lacking feature, we can't read a custom grid defined
        #in {dims.dat, used_rads.dat} files for the moment
        nr     = Scan.search(self._config, 'nrad', int)
        ns     = Scan.search(self._config, 'nsec', int)
        rmin   = Scan.search(self._config, 'rmin', np.float64)
        rmax   = Scan.search(self._config, 'rmax', np.float64)

        try:
            spacing = Scan.search(self._config, 'radialspacing', str)
        except AttributeError:
            spacing = 'Arithmetic'
        try:
            sector  = Scan.search(self._config, 'sector', int)
        except AttributeError:
            sector  = 2*np.pi

        if spacing.lower().startswith('log'):
            rinf_ = np.array([rmin * np.exp(i * np.log(rmax/rmin)/nr) for i in range(nr+1)])
        else:
            rinf_ = np.linspace(rmin, rmax, nr+1)

        rmed = np.zeros(nr)
        for i in range(nr):
            rmed[i]  = 2.0/3.0 * (rinf_[i+1]**3 - rinf_[i]**3)/ (rinf_[i+1]**2 - rinf_[i]**2)

        rinf = rinf_[:-1]
        rsup = rinf_[1:]
        grid = {
            'nrad'   : nr,
            'nsec'   : ns,
            'rmin'   : rmin,
            'rmax'   : rmax,
            'spacing': spacing,
            'sector' : sector,
            'rinf'   : rinf,
            'rsup'   : rsup,
            'rmed'   : rmed,
            'theta'  : np.linspace(0.0, sector,ns),
            'surf'   : np.pi * (rsup**2 - rinf**2) / ns
        }

        self._grid = grid

    def center_on_planet(self, planet_num:int=0):
        '''Center the field data on the planet numbered <plt_num>.
        devnote 1 : this is a rough calculation within the precision of a
                    cell angular width. It could be refined.
        devnote 2 : planet data becomes invalid after this operation.
        devnote 3 : we do not store the applied rotation, as a result, we can't reapply it later
        '''
        if not self.is_centered:
            for offset in self.offsets:
                pladat = self['planet'][planet_num]
                select_pladat = pladat[pladat.output == offset]
                coords = select_pladat.iloc[0]
                xp = coords.x
                yp = coords.y
                tp = atan2(yp, xp) % (2 * np.pi) #theta planet

                ic = 0
                while self['theta'][ic+1] < tp:
                    ic += 1

                ns = self.grid['nsec']
                transport = int(ns/2-ic)
                permutation = [(i - transport) % ns for i in range(ns)]
                for key in self.fields.columns:
                    field = self[key].ix[offset]
                    if field is None:
                        continue
                    self[key].ix[offset] = field[permutation, :]
            self.is_centered = True

    def search(self, attr, convert=lambda x: x):
        '''Search the configuration for an parameter and optionnaly convert it from str.'''
        return Scan.search(self._config, attr, convert)

    def __getitem__(self, key: str):
        if   key in self.fields.columns:
            return self.fields[key]
        elif key in self.profiles.columns:
            return self.profiles[key]
        elif key in self.planets.columns:
            return self.planets[key]
        elif key in self.grid.keys():
            return self.grid[key]
        else:
            raise KeyError(f"data '{key}' was not found in {self.outputdir}")

    def __repr__(self):
        status = {True: 'Yes', False: 'No'}[self.is_loaded]

        deco = '------------------------'
        deco += '-'*max(len(self.outputdir), len(self.configfile))

        substitutions = ('array(', '      '), (')', '')
        arr_repr = np.array(self.offsets).__repr__()
        for subs in substitutions:
            arr_repr = arr_repr.replace(*subs)

        visio = '\n'.join([
            '\nfyrgo.DataLoader object',
            deco,
            f'output directory      {self.outputdir}',
            f'configuration file    {self.configfile}',
            deco,
            'known fields          ',
            ' '*4 + ', '.join([str(o) for o in self.fields]),
            f'Loaded                {status}',
            f'Used memory (bytes)   {getsizeof(self.fields)}',
            deco,
            'Current offsets ',
            arr_repr,
        ])
        return visio


    # Properties -----------------------------------------------------------------

    @property
    def offsets(self):
        'The offsets to load.'
        return self._offsets

    @offsets.setter
    def offsets(self, new_offsets):
        'Change offsets but do not reload.'
        self._offsets = new_offsets
        self.is_loaded = False

    @property
    def outputdir(self) -> str:
        '''Where data is supposed to be located.

        Treated as immutable.
        '''
        return self._outputdir

    def _set_outputdir(self, outputdir:str) -> None:
        'A private setter method.'
        if outputdir is None:
            outputdir = Scan.search(self._config, 'outputdir', str)
            outdir_path = (Path(self.configfile).parent / Path(outputdir)).resolve()
        else:
            outdir_path = Path(outputdir)
        assert(outdir_path.exists()), \
            "Trying to fetch data from non-existing directory '%s'" % outputdir
        self._outputdir = str(outdir_path.absolute())#todo: add a resolve() here

    @property
    def configfile(self) -> str:
        '''The configuration file that was used to run the simulation.

        Treated as immutable.
        '''
        return self._configfile


    # Special properties with no dedicated setters -------------------------------

    @property
    def grid(self) -> dict:
        '''Grid information.

        self.grid is set by self.load_grid()
        '''
        return self._grid

    @property
    def planets(self) -> pd.DataFrame:
        '''Planet related data sorted by file name and planet number.

        self.planets is set by self.load_planets()
        '''
        return self._planets

    @property
    def profiles(self) -> pd.DataFrame:
        '''1D arrays stored by offset indexing.

        self.profiles is set with self.load_fields()
        or with self.load_arrays(), alongside self.fields
        '''
        return self._profiles

    @property
    def fields(self) -> pd.DataFrame:
        '''2D arrays stored by offset indexing.

        self.fields is set with self.load_arrays()
        or with self.load_arrays(), alongside self.arrays
        '''
        return self._fields
