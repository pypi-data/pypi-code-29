import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import click


@click.command()
@click.argument('filename')
@click.argument('column')
def hist(filename, column):#, second_column=None):
    df = pd.read_csv(filename)

    plt.hist(df[column])
    ax = plt.gca()
    ax.set(title=filename, xlabel=column.title(), ylabel="Frequency")
    plt.show()


@click.command()
@click.argument('filename')
@click.argument('column')
@click.argument('column2')
def hist2(filename, column, column2):
    df = pd.read_csv(filename)
    H, x, y = np.histogram2d(df[column], df[column2], bins=80)
    plt.imshow(H.T, extent=[x[0], x[-1], y[0], y[-1]], cmap='gray_r', origin='lower', aspect='auto')
    ax = plt.gca()
    ax.set(title=filename, xlabel=column.title(), ylabel=column2.title())
    plt.show()



@click.command()
@click.argument('filename')
def show(filename):
    df = pd.read_csv(filename)
    summary = pd.DataFrame([df.dtypes, df.count(), df.min(), df.max()], index=['dtype', 'count', 'min', 'max']).T
    summary.index.name = 'column'
    print(summary)
