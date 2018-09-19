"""
This example shows the trade-off (pareto frontier) of deficit against cost by altering a reservoir control curve.

Two types of control curve are possible. The first is a monthly control curve containing one value for each
month. The second is a harmonic control curve with cosine terms around a mean. Both Parameter objects
are part of pywr.parameters.

Inspyred is used in this example to perform a multi-objective optimisation using the NSGA-II algorithm. The
script should be run twice (once with --harmonic) to generate results for both types of control curve. Following
this --plot can be used to generate an animation and PNG of the pareto frontier.

"""
import json
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pywr.recorders import Recorder
from pyreto_db import documents
import mongoengine as me
import datetime


MONGO_DB = 'two-reservoir'
MONGO_CONNECTION_DATA = {
    'db': MONGO_DB,
    'host': 'mongodb://localhost',
}


class PyretoDBRecorder(Recorder):
    def __init__(self, *args, **kwargs):
        self.search_id = kwargs.pop('search_id')
        self.connection_kwargs = kwargs.pop('connection_kwargs', {})
        super().__init__(*args, **kwargs)
        self.created_at = None

    def _generate_variable_documents(self):

        for variable in self.model.variables:
            # TODO add variable bounds
            value = {}
            try:
                value['doubles'] = list(variable.get_double_variables())
            except NotImplementedError:
                pass

            try:
                value['integers'] = list(variable.get_integer_variables())
            except NotImplementedError:
                pass

            yield documents.Variable(name=variable.name, value=value)

    def _generate_objective_documents(self):

        for objective in self.model.objectives:
            yield documents.Objective(name=objective.name, value=objective.aggregated_value(),
                                      minimise=objective.is_objective == 'minimise')

    def reset(self):
        self.created_at = None

    def before(self):
        if self.created_at is None:
            self.created_at = datetime.datetime.now()

    def finish(self):

        # Connect to the database
        client = me.connect(**self.connection_kwargs)
        search = documents.Search.objects(id=self.search_id).first()
        client.close()

        evaluated_at = datetime.datetime.now()
        # TODO runtime statistics
        individual = documents.Individual(
            variables=list(self._generate_variable_documents()),
            objectives=list(self._generate_objective_documents()),
            constraints=list(),  # TODO complete constraints
            created_at=self.created_at,
            evaluated_at=evaluated_at,
            search=search,
        )
        import time
        print('Saving ...', end='')
        t0 = time.time()
        individual.save()
        print(' done in {:.2f}s'.format(time.time() - t0))
        client.close()

PyretoDBRecorder.register()


def get_model_data(search_id, harmonic=True):

    with open('two_reservoir.json') as fh:
        data = json.load(fh)

    if harmonic:
        # Patch the control curve parameter
        data['parameters']['control_curve'] = {
            'type': 'AnnualHarmonicSeries',
            'mean': 0.5,
            'amplitudes': [0.5, 0.0],
            'phases': [0.0, 0.0],
            'mean_upper_bounds': 1.0,
            'amplitude_upper_bounds': 1.0,
            'is_variable': True
        }

    data['recorders']['pyreto-db'] = {
        'type': 'PyretoDBRecorder',
        'search_id': search_id,
        'connection_kwargs': MONGO_CONNECTION_DATA
    }

    return data


def create_new_search(drop=True, **kwargs):
    client = me.connect(**MONGO_CONNECTION_DATA)

    if drop:
        client.drop_database(MONGO_DB)

    if 'started_at' not in kwargs:
        kwargs['started_at'] = datetime.datetime.now()

    search = documents.Search(**kwargs)
    search.save()
    return search


def platypus_main(harmonic=False, drop=True):
    import platypus
    from pywr.optimisation.platypus import PlatypusWrapper

    search_name = 'two-reservoir-' + ('harmonic' if harmonic else 'monthly')
    print(search_name)

    search = create_new_search(name=search_name, algorithm='NSGAII',
                               tags=['platypus', ], drop=drop)

    wrapper = PlatypusWrapper(get_model_data(search.id, harmonic=harmonic))

    with platypus.ProcessPoolEvaluator() as evaluator:
    #with platypus.MapEvaluator() as evaluator:
        algorithm = platypus.NSGAII(wrapper.problem, population_size=100, evaluator=evaluator)
        algorithm.run(2500)




if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--harmonic', action='store_true', help='Use an harmonic control curve.')
    parser.add_argument('--no-drop-db', action='store_true', help='Drop the mongo database before starting.')
    args = parser.parse_args()

    platypus_main(harmonic=args.harmonic, drop=not args.no_drop_db)

