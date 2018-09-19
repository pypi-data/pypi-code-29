import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pyreto_db import documents
import mongoengine as me
import datetime


#MONGO_DB = 'two-reservoir'
MONGO_DB = 'parflow-test'
MONGO_CONNECTION_DATA = {
    'db': MONGO_DB,
    'host': 'mongodb://localhost',
}


def main(search_name, ax1, ax2, color, stats=None):
    client = me.connect(**MONGO_CONNECTION_DATA)

    search = documents.Search.objects(name=search_name).first()

    print('Processing search: {}'.format(search['name']))

    if stats is None:
        stats = search.objectives_to_dataframe().describe()

    start = search['started_at']
    now = start + datetime.timedelta(seconds=300)
    if now > datetime.datetime.now():
        now = datetime.datetime.now()

    dt = now - start

    ref_point = np.ones(2)*1.5
    hypervolumes = {}

    dates = pd.date_range(start, now, freq='10S')
    for i, d in enumerate(dates[::-1]):
        delta = d - start
        non_dom = search.non_dominated_individuals(evaluated_at__lte=d)
        df = documents.Individual.many_objectives_to_dataframe(non_dom)

        if len(df) > 0:
            df.plot(x='deficit', y='transferred', ax=ax1, marker='o', legend=False, color=color,
                    alpha=1.0-0.8*i/len(dates))

            hv = search.hypervolume(normalise_stats=stats, evaluated_at__lte=d)
            value = hv.compute(ref_point)
            hypervolumes[delta] = value
            print('After {}s {} individuals in non-dominated frontier with hyper-volume {:.2f}.'.format(delta, len(df), value))

    hypervolumes = pd.Series(hypervolumes)
    hypervolumes.plot(ax=ax2, marker='o', color=color, label=search_name)

    return stats


if __name__ == '__main__':
    fig, (ax1, ax2) = plt.subplots(nrows=2)

    colors = plt.rcParams['axes.prop_cycle'].by_key()['color']

    stats = main("test-search", ax1, ax2, colors[0])
    main('two-reservoir-monthly', ax1, ax2, colors[1], stats=stats)
    ax2.legend()
    ax2.set_ylabel('Normalised hyper-volume.')
    plt.tight_layout()
    plt.show()
