#
# Zeta.
#
# Copyright 2014, 2015, 2016, 2017 Tobias Rossmann.
#
# This package is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by the
# Free Software Foundation, either version 3 of the License, or (at your
# option) any later version.
#
# This software is distributed in the hope that it will be useful,
# but without any warranty; without even the implied warranty of
# merchantability or fitness for a particular purpose.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# this software; if not, see <http://www.gnu.org/licenses>.
#

from functools import partial
import pkg_resources

import common

import addmany

import examples
from subobjects import SubobjectZetaProcessor
from reps import RepresentationProcessor

from ask import AskProcessor

from algebra import Algebra
from abstract import ReductionError
from toric import ToricDatum
from util import create_logger
from common import symbolic_count_varieties

import surf
import smurf
import abstract
import subobjects
import reps
import ask
import util
import cycrat
import triangulate

from laurent import LaurentPolynomial

from subobjects import Strategy

from sage.all import Infinity, var
import sage

__version__ = pkg_resources.get_distribution("zetalib").version
__date__ = 'July 2018'

logger = create_logger(__name__)

from reps import IgusaProcessor

# The following is supposed to detect a bug which is present (at least)
# in version 7.5.1 and 7.6 of Sage.
__SERIES_BUG = False
def __check_sage_bugs():
    x,y,z = var('x y z')
    if y.series(x) != (z.series(x))(z=y):
        __SERIES_BUG = True

__check_sage_bugs()

class Profile(object):
    SAVE_MEMORY = 1
    NORMAL = 2
    SPEED = 3

def lookup(entry=None, what=None, type='topological'):
    if entry is None:
        return [(i, examples.names[i][:]) for i, _ in enumerate(examples.algebras)]

    i = examples.id.get(entry)
    if i is None:
        try:
            i = int(entry)
        except ValueError:
            raise KeyError('Unknown algebra')
    if i < 0 or i >= len(examples.algebras):
        raise KeyError('Invalid index')

    if what is None:
        return examples.algebras[i]
    elif what == 'id':
        return i
    elif what == 'names':
        return examples.names[i]

    if type == 'topological':
        D = examples.topzetas
    elif type in ['p-adic', 'local']:
        D = examples.padzetas
    else:
        raise ValueError('unknown type')
    return D[i].get(what, None)

def zeta_function(type, L, objects=None, optimise_basis=False,
                  ncpus=None, alt_ncpus=None, strategy=None, profile=None, verbose=False,
                  optlevel=None, addmany_dispatcher=None, mode=None, debug=None):
    if type not in ['p-adic', 'topological']:
        raise ValueError('Unknown type of zeta function')

    if type == 'p-adic':
        if common.count is None:
            raise RuntimeError('LattE/count is required in order to compute p-adic zeta functions')
        elif __SERIES_BUG:
            raise RuntimeError('power series expansions in this version of Sage cannot be trusted')

    # Multiprocessing.
    if ncpus is None:
        ncpus = Infinity
    from multiprocessing import cpu_count
    common.ncpus = min(ncpus, cpu_count())

    if alt_ncpus is None:
        alt_ncpus = common.ncpus
    common._alt_ncpus = alt_ncpus

    if addmany_dispatcher is None:
        addmany_dispatcher = 'numerator'
    common.addmany_dispatcher = addmany_dispatcher

    common.debug = False if debug is None else debug

    if optlevel is None:
        optlevel = 1
    common.optimisation_level = optlevel

    # Reduction strategies.
    if strategy is None:
        strategy = Strategy.NORMAL

    # Memory profiles.
    if profile is None:
        profile = Profile.NORMAL
    if profile not in [Profile.SAVE_MEMORY, Profile.NORMAL, Profile.SPEED]:
        raise ValueError('Invalid profile')
    if profile == Profile.SAVE_MEMORY:
        common.save_memory = True
        common.plumber = True
    elif profile == Profile.NORMAL:
        common.save_memory = False
        common.plumber = True
    elif profile == Profile.SPEED:
        common.save_memory = False
        common.plumber = False

    if verbose:
        from logging import INFO, DEBUG
        loglevels = [(logger, INFO), (smurf.logger, INFO), (surf.logger, INFO),
                     (torus.logger, INFO), (abstract.logger, INFO),
                     (cycrat.logger, INFO), (triangulate.logger, INFO),
                     (reps.logger, INFO), (subobjects.logger, INFO),
                     (ask.logger, INFO),
                     (addmany.logger, INFO), ]
        oldlevels = []

        for m,level in loglevels:
            old = m.getEffectiveLevel()
            oldlevels.append(old)
            m.setLevel(min(old,level))

    # Try to detect polynomials and lists of polynomials.
    polynomials = None
    try:
        _ = L.exponents()
    except:
        try:
            if not isinstance(L, basestring) and not isinstance(L,sage.matrix.matrix_dense.Matrix_dense) and objects != 'orbits':
                polynomials = list(L)
        except:
            pass
    else:
        polynomials = [L]

    if (polynomials is None) and not isinstance(L, algebra.Algebra) and not isinstance(L,sage.matrix.matrix_dense.Matrix_dense) and objects != 'orbits':
        L = lookup(L)

    if polynomials is not None:
        proc = IgusaProcessor(*polynomials)
    elif objects in ['subalgebras', 'ideals']:
        proc = SubobjectZetaProcessor(L, objects, strategy=strategy)
    elif objects == 'reps':
        proc = RepresentationProcessor(L)
    elif objects == 'ask':
        proc = AskProcessor(L, mode=mode)
    elif objects == 'orbits':
        # NOTE: we don't currently check if L really spans a matrix Lie algebra
        proc = AskProcessor(util.matlist_to_mat(util.basis_of_matrix_algebra(L, product='Lie')), mode=mode)
    elif objects == 'cc':
        if not L.is_Lie() and not L.is_nilpotent():
            raise ValueError('need a nilpotent Lie algebra in order to enumerate conjugacy classes')
        proc = AskProcessor(util.matlist_to_mat(L._adjoint_representation()), mode=mode)
    else:
        raise ValueError('unknown objects [%s]' % objects)

    if optimise_basis:
        logger.info('Searching for a good basis...')
        proc.optimise()
        logger.info('Picked a basis.')

    if verbose:
        print proc

    try:
        if type == 'p-adic':
            return proc.padically_evaluate(shuffle=True)
        elif type == 'topological':
            return proc.topologically_evaluate(shuffle=True)
    finally:
        if verbose:
            for ((m,_),level) in zip(loglevels,oldlevels):
                m.setLevel(level)

def do(type, L, objects='subalgebras', filename=None, save_memory=None, symbolic=False, **kwargs):
    if save_memory is None:
        save_memory = bool(type == 'p-adic')

    D = { 'optimise_basis': True,
          'strategy': Strategy.NORMAL if type == 'p-adic' else Strategy.PREEMPTIVE,
          'profile': Profile.SAVE_MEMORY if save_memory else Profile.NORMAL,
          'verbose': True,
          }

    if symbolic:
        common.symbolic = True
        D.update({ 'debug': True,
                   'addmany_dispatcher': 'symbolic',
                   'optlevel': 0.2 })
    else:
        common.symbolic = False

    D.update(kwargs)
    Z = zeta_function(type, L, objects, **D)
    if filename is True:
        if not isinstance(L, basestring):
            raise ValueError
        filename = objects + '-' + L + '.' + {'p-adic': 'pad', 'topological': 'top'}[type]
    if filename:
        with open(filename, 'w') as f: f.write(str(Z))
    return Z

topological_zeta_function = partial(do, 'topological', strategy=Strategy.NORMAL, verbose=False)
local_zeta_function = partial(do, 'p-adic', strategy=Strategy.NORMAL, verbose=False)

top = partial(do, 'topological')
pad = partial(do, 'p-adic')

def check(name, objects='subalgebras', type='p-adic', **kwargs):
    L = lookup(name)
    W = lookup(name, objects, type)
    if W is None:
        raise RuntimeError('zeta function not contained in database')

    Z = do(type, L, objects, **kwargs)
   
    if Z != W:
        print 'Computed: ', Z
        print 'Database: ', W
        raise RuntimeError('computed zeta function of %s differs from entry in the database' % name)

    print
    print 'Algebra #%d' % lookup(name,'id')
    print 'Names: %s' % ', '.join(lookup(name,'names'))
    print 'Objects:', objects
    print 'Type:', type
    print 'Zeta:', Z
    print 'Confirmed.'
    return True

def checkall(objects='reps', type='p-adic', **kwargs):
    ids = []

    for i, _ in lookup():
        if lookup(i, objects, type) is not None:
            check(i, objects, type, **kwargs)
            ids.append(i)

    print
    print 'Objects:', objects
    print 'Type:', type
    print 'Confirmed zeta functions for the following algebras:'

    for i in ids:
        print '#%d:\t%s' % (i, ', '.join(lookup(i, 'names')))
    print 'Total number:', len(ids)
    
if __SERIES_BUG:
    logger.critical(
            """This version of Sage may compute incorrect symbolic power series
expansions. Computations of p-adic zeta functions are therefore
unavailable. Try using a different version of Sage such as 7.4.""")

    
_banner_text = """
ZZZZZZZZZZZZZZZZZZZ                           tttt                           
Z:::::::::::::::::Z                        ttt:::t                           
Z:::::::::::::::::Z                        t:::::t                           
Z:::ZZZZZZZZ:::::Z                         t:::::t                           
ZZZZZ     Z:::::Z     eeeeeeeeeeee   ttttttt:::::ttttttt     aaaaaaaaaaaaa   
        Z:::::Z     ee::::::::::::ee t:::::::::::::::::t     a::::::::::::a  
       Z:::::Z     e::::::eeeee:::::et:::::::::::::::::t     aaaaaaaaa:::::a 
      Z:::::Z     e::::::e     e:::::tttttt:::::::tttttt              a::::a 
     Z:::::Z      e:::::::eeeee::::::e     t:::::t             aaaaaaa:::::a 
    Z:::::Z       e:::::::::::::::::e      t:::::t           aa::::::::::::a 
   Z:::::Z        e::::::eeeeeeeeeee       t:::::t          a::::aaaa::::::a 
ZZZ:::::Z     ZZZZe:::::::e                t:::::t    ttttta::::a    a:::::a 
Z::::::ZZZZZZZZ:::e::::::::e               t::::::tttt:::::a::::a    a:::::a 
Z:::::::::::::::::Ze::::::::eeeeeeee       tt::::::::::::::a:::::aaaa::::::a 
Z:::::::::::::::::Z ee:::::::::::::e         tt:::::::::::tta::::::::::aa:::a
ZZZZZZZZZZZZZZZZZZZ   eeeeeeeeeeeeee           ttttttttttt   aaaaaaaaaa  aaaa

%s
%s
                             by   
                                 Tobias Rossmann
""" % ('{:>77}'.format('VERSION ' + __version__),
       '{:>77}'.format('Released: ' + __date__))

def banner():
    print(_banner_text)
