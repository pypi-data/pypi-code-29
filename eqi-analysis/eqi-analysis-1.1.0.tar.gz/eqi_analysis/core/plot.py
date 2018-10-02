import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


def _label_odd_months(dt_values):
    return ('{}.{}'.format(dt.year, dt.month) if dt.month % 2 != 0 else '' for
            dt in dt_values)


def bar_line(df, ax, bar_columns, line_columns, width=0.9,
             alpha=.5,
             title='', xlabel='', ylabel='', **plot_kwargs):
    xlabel = xlabel or df.index.name
    col_len = len(df.columns)
    indices = np.arange(len(df))
    colors_line = ['red', 'black'] * int(col_len / 5. + 1)
    for label, color in zip(line_columns, colors_line):
        ax.plot(indices, df[label], color=color)
    for i, label in zip(range(col_len), bar_columns):
        kwargs = plot_kwargs
        kwargs.update({'label': label})
        ax.bar(indices, df[label], width=width, alpha=alpha if i else 1,
               **kwargs)
        plt.xticks(indices + .5 * width,
                   _label_odd_months(pd.to_datetime(df.index.values)),
                   rotation=90)
    ax.legend(loc='lower right')
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.grid(True)


def set_plt_size():
    small_size = 15
    medium_size = 18
    big_size = 20

    plt.rc('font', size=small_size)
    plt.rc('axes', titlesize=small_size)
    plt.rc('axes', labelsize=medium_size)
    plt.rc('xtick', labelsize=small_size)
    plt.rc('ytick', labelsize=small_size)
    plt.rc('legend', fontsize=small_size)
    plt.rc('figure', titlesize=big_size)
