## Copyright (c) 2015-2016, Blake C. Rawlings.
##
## This file is part of `st2smv`.

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import copy
import itertools
import pprint
import time

import networkx

from ... import ast
from ... import plugins
from ... import utils
from . import smt

logger = utils.logging.getLogger(__name__)

## Plugin information.
NAME = 'predicates'
ACTIONS = (
    plugins.actions.REFINEMENT,
)
OPTIONS = {
    'predicates': (
        int,
        (
            'generate constraints based on which combinations of the '
            'predicates that appear in the ST file can (or cannot) '
            'be satisfied; '
            'the argument is the maximum number of simultaneous predicates '
            'to consider'
        )
    )
}

MAX_COMBINATIONS = 10**4

class ConstraintWriter(object):
    """A class for generating boolean constraints given a set of
    inequalities.

    """
    def __init__(self, converter):

        ## Copy the ST comparisons and SMV variables from `converter`.
        self.predicates = []
        self.predvars = []
        self.transformed = []
        tmp = copy.deepcopy(converter.comparisons)
        for comparison in tmp:
            if comparison[1] not in self.predvars:
                self.predicates.append(comparison[0])
                self.predvars.append(comparison[1])
                self.transformed.append(ast.abs_to_disjunction(comparison[0]))
        self.referenced = copy.deepcopy(converter.referenced)
        self.flattened = [utils.flatten(x) for x in self.predicates]

        ## Create a graph of the variable relationships.
        self.var_graph = self._get_variable_graph()
        logger.info(
            'Connected variable groups:\n{}'.format(
                sorted(networkx.connected_components(self.var_graph))
            )
        )

        ## Set up some basic information about the variables.
        self.var_info = self._get_variable_info()
        logger.info('var_info: {}'.format(pprint.pformat(self.var_info)))

        ## Set up some basic information about the predicate variables.
        self.predvar_info = self._get_predvar_info()
        logger.info(
            'predvar_info: {}'.format(pprint.pformat(self.predvar_info))
        )
        self.predvar_graph = self._get_predvar_graph()

        ## Set up the groups of mutually-related predicates.
        self.groups = self._generate_groups()
        self.groups = sorted(self.groups, key=len, reverse=True)
        logger.info(
            'Connected predicate groups:\n{}'.format(
                pprint.pformat(self.groups)
            )
        )

        ## Declare other (as yet unset) variables.
        self.infeasible = []

    def generate_infeasible_combinations(self, simultaneous_predicates=2):
        """Generate a list of infeasible combinations of predicates results
        that appear in the model that `converter` will produce.  This
        modifies `self`'s members in place, and can be called multiple
        times with different values of `simultaneous_predicates` to
        produce additional infeasible combinations.

        """
        logger.info(
            'Generating infeasible predicate combos (groups of {0})...'.format(
                simultaneous_predicates
            )
        )
        t0 = time.time()
        ng = len(self.groups)
        count = 0
        for group in self.groups:
            count += 1
            (combos, skipped, n_trivial) = self._get_combinations(
                group, simultaneous_predicates
            )
            logger.info(
                'Group {}/{}: {} combinations to check '
                '(redundant: {}; trivial: {})'
                .format(
                    count, ng,
                    len(combos),
                    len(skipped),
                    n_trivial * 2**simultaneous_predicates
                )
            )
            self.infeasible += self._get_infeasible(combos)
        t1 = time.time()
        logger.info(
            'Generated infeasible predicate combos (groups of {0}): {1:.2f}s'
            .format(
                simultaneous_predicates, t1 - t0
            )
        )

    def generate_constraints(self):
        """Generate a list of SMV constraints that will enforce the infeasible
        combinations in `self.infeasible`.  Call
        `self.generate_infeasible_combinations` before calling this
        method to populate the list of infeasible combinations.

        """
        constraints = []
        connections = []

        ## Infeasible predicate combinations.
        for combo in self.infeasible:
            clauses = []
            for idx in combo:
                if combo[idx]:
                    prefix = ''
                else:
                    prefix = '!'
                clauses.append(prefix + self.predvars[idx])
            constraints.append(['INVAR', '!({0})'.format(' & '.join(clauses))])

        ## Newly-created variable connections.
        for combo in self.infeasible:
            predvars = [self.predvars[idx] for idx in combo]
            pairs = set(itertools.combinations(predvars, 2))
            connections += pairs

        return (constraints, connections)

    @utils.timing(
        log_fun=logger.info,
        log_text='Generated predicate groups: {0:.2f}s'
    )
    def _generate_groups(self):
        """Generate the groups of predicates that influence each other.  This
        has to be called after setting `self.var_info` and
        `self.var_graph`.

        """
        groups = []
        var_groups = sorted(networkx.connected_components(self.var_graph))
        for vg in var_groups:
            group = set()
            for var in vg:
                group = set.union(group, self.var_info[var]['appears_in'])
            groups.append(group)
        return groups

    def _get_combinations(self, group, k):
        """Get a list of the combinations (by index) of the predicates in
        `group`, `k` at a time, either being true or false.

        """
        combos = []
        skipped = []
        n_trivial = 0
        for combo in itertools.combinations(group, k):
            # logger.warning([self.predvars[i] for i in combo])
            sg = self.predvar_graph.subgraph(combo)
            is_trivial = False
            for this in combo:
                path_lengths = networkx.algorithms.shortest_path_length(
                    sg, source=this
                )
                if len(path_lengths) < k:
                    is_trivial = True
                    break
            if is_trivial:
                n_trivial += 1
                logger.debug(
                    'Combo trivial with k={1}: {0}'.format(combo, k)
                )
                continue
            for variation in itertools.product(*([[True, False]] * k)):
                cv = {combo[i]: variation[i] for i in range(k)}
                if self._already_marked(cv):
                    logger.debug(
                        'Combo already marked infeasible, skipping: {}'.format(
                            cv
                        )
                    )
                    skipped.append(cv)
                else:
                    combos.append(cv)
        return (combos, skipped, n_trivial)

    def _get_infeasible(self, combinations):
        """Check which of the `combinations` are infeasible."""
        infeasible = []
        if len(combinations) > MAX_COMBINATIONS:
            logger.warning(
                'Too many combinations ({0} > {1}), skipping.'.format(
                    len(combinations), MAX_COMBINATIONS
                )
            )
            return []
        for combo in combinations:
            if self._already_marked(combo):
                logger.warning(
                    'This combo was already marked infeasible: {}'.format(combo)
                )
                continue
            try:
                if smt.is_infeasible(self, combo):
                    infeasible.append(combo)
            except NotImplementedError:
                pass
        return infeasible

    def _already_marked(self, combination):
        """Check if `combination` is already marked as infeasible."""
        marked = False
        for infeas in self.infeasible:
            if len(infeas) >= len(combination):
                continue
            marked = True
            for key in infeas:
                if infeas[key] == combination.get(key):
                    pass
                else:
                    marked = False
                    break
            if marked:
                break
        return marked

    def _get_variable_info(self):
        """Check how the variables relate to each other, and which predicates
        they show up in.

        """
        var_info = {}

        ## Find out which predicates each variable appears in.
        for i, comp in enumerate(self.predicates):
            for var in self._get_vars(comp):
                if var in var_info:
                    assert isinstance(var_info[var], dict)
                    assert isinstance(var_info[var]['appears_in'], set)
                    var_info[var]['appears_in'].add(i)
                else:
                    var_info[var] = {'appears_in': {i}}

        return var_info

    def _get_variable_graph(self):
        var_graph = networkx.Graph()
        for predicate in self.predicates:
            variables = self._get_vars(predicate)
            for this in variables:
                for other in variables:
                    var_graph.add_edge(this, other)
        return var_graph

    def _get_predvar_info(self):
        pvi = {}
        for v in self.var_info:
            for pv in self.var_info[v]['appears_in']:
                if pv not in pvi:
                    pvi[pv] = set()
                pvi[pv].add(v)
        return pvi

    def _get_predvar_graph(self):
        pg = networkx.Graph()
        for pv1 in self.predvar_info:
            for pv2 in self.predvar_info:
                if pv2 == pv1:
                    continue
                for v in self.predvar_info[pv1]:
                    if v in self.predvar_info[pv2]:
                        pg.add_edge(pv1, pv2)
        return pg

    def _get_vars(self, predicate):
        """Get the set of variables that appear in `predicate`."""
        return set(
            [x for x in utils.flatten(predicate) if x in self.referenced]
        )

def compute_refinements(converter):
    """Compute the predicate constraints up to combinations of `limit`
    predicates at a time.

    """
    limit = converter.plugin_options.get('predicates', 0)
    if limit < 2:
        return ([], [])
    cw = ConstraintWriter(converter)
    for s in range(2, limit + 1):
        cw.generate_infeasible_combinations(simultaneous_predicates=s)
    (constraints, connections) = cw.generate_constraints()
    return (constraints, connections)
