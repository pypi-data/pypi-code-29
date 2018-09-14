import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math


def _get_fig_shape(n, wrap, is_row):
    if is_row:
        if wrap is None:
            return n, 1
        else:
            return wrap, math.ceil(n / wrap)
    else:
        if wrap is None:
            return 1, n
        else:
            return math.ceil(n / wrap), wrap


def aggplot(agg, groupby=None, data=None, hue=None, row=None, col=None, kind='bar', orient='v',
            sort=False, aggfunc='mean', normalize=None, figsize=None, rot=90, wrap=None,
            sharex=True, sharey=True):

    if figsize is None:
        figsize = plt.rcParams['figure.figsize']

    if not isinstance(data, pd.DataFrame):
        raise TypeError('`data` must be a DataFrame')

    params = ['agg', 'groupby', 'hue', 'row', 'col']
    locs = locals()
    for param in params:
        if locs[param] is None:
            continue
        col_name = locs[param]
        if col_name not in data.columns:
            raise ValueError('You passed {col_name} to parameter {param} which is not a '
                             'column name')

    if orient not in ['v', 'h']:
        raise ValueError('`orient` must be either "v" or "h".')

    if wrap is not None:
        if not isinstance(wrap, int):
            raise TypeError(f'`wrap` must either be None or an integer. You passed {type(wrap)}')

    agg_data = data[agg]
    agg_kind = agg_data.dtype.kind

    if agg_kind not in ['i', 'f', 'b', 'O']:
        raise TypeError(f'The data type for the `agg` column must either be boolean, integer, '
                        'float, boolean, or categorical/object and not {agg_data.dtype}')

    if groupby is not None:
        groupby_data = data[groupby]
        groupby_kind = groupby_data.dtype.kind

    if hue is not None:
        hue_data = data[hue]
        hue_kind = hue_data.dtype.kind

    if row is not None:
        row_data = data[row]
        row_kind = row_data.dtype.kind

    if col is not None:
        col_data = data[col]
        col_kind = col_data.dtype.kind

    width = .8

    if groupby is None and hue is None and row is None and col is None:
        fig, ax = plt.subplots(figsize=figsize)
        if agg_kind == 'O':
            if normalize == 'agg':
                normalize = True
            elif normalize not in [None, 'agg']:
                raise ValueError('`normalize` can only be False, one of the parameter '
                                 'names "agg", "groupby", "hue", "row", "col", '
                                 'or a combination of those parameter names in a tuple, '
                                 'if they are defined.')
            vc = agg_data.value_counts(sort=sort, normalize=normalize)
            if orient == 'v':
                ax.bar(vc.index, vc.values)
                ax.tick_params(axis='x', labelrotation=rot)
            else:
                ax.barh(vc.index, vc.values)
        elif agg_kind in 'ifb':
            value = agg_data.agg(aggfunc)
            if orient == 'v':
                ax.bar(agg, value)
            else:
                ax.barh(agg, value)
        return ax

    if groupby is None and hue is not None and row is None and col is None:
        fig, ax = plt.subplots(figsize=figsize)
        if normalize == 'hue':
            normalize = 'index'
        elif normalize == 'agg':
            normalize = 'columns'
        elif normalize == 'all':
            pass
        elif normalize is None:
            normalize=False
        else:
            raise ValueError('`normalize` can only be None, one of the parameter '
                             'names "agg", "groupby", "hue", "row", "col", or a combination '
                             'of those parameter names in a tuple, if they are defined.')
        if agg_kind == 'O':
            tbl = pd.crosstab(agg_data, hue_data, normalize=normalize)
            n_rows, n_cols = tbl.shape
            width = .8 / n_cols

            if orient == 'v':
                x_range = np.arange(n_rows)
                for i in range(n_cols):
                    x_data = x_range + i * width
                    height = tbl.iloc[:, i].values
                    ax.bar(x_data, height, width, label=tbl.columns[i])
                ax.set_xticks(x_range + width * (n_cols - 1) / 2)
                ax.set_xticklabels(tbl.index)
                ax.tick_params(axis='x', labelrotation=rot)
            else:
                x_range = np.arange(n_rows, 0, -1)
                for i in range(n_cols):
                    x_data = x_range - i * width
                    height = tbl.iloc[:, i].values
                    ax.barh(x_data, height, width, label=tbl.columns[i])
                ax.set_yticks(x_range - width * (n_cols - 1) / 2)
                ax.set_yticklabels(tbl.index)
            ax.legend()
        else:
            grouped = data.groupby(hue).agg({agg: aggfunc})
            if orient == 'v':
                ax.bar(grouped.index, grouped.values[:, 0])
                ax.tick_params(axis='x', labelrotation=rot)
            else:
                ax.barh(grouped.index[::-1], grouped.values[::-1, 0])
        return ax

    if groupby is not None and row is None and col is None:
        if agg_kind == 'O':
            raise TypeError('When the `agg` column is categorical, you cannot use `groupby`. '
                            'Instead, place the groupby column as either '
                            ' `hue`, `row`, or `col`.')
        fig, ax = plt.subplots(figsize=figsize)

        if hue is None:
            grouped = data.groupby(groupby).agg({agg: aggfunc})
            if orient == 'v':
                ax.bar(grouped.index, grouped.values[:, 0])
                ax.tick_params(axis='x', labelrotation=rot)
            else:
                ax.barh(grouped.index[::-1], grouped.values[::-1, 0])
        else:
            tbl = data.pivot_table(index=groupby, columns=hue, values=agg, aggfunc=aggfunc)
            n_rows, n_cols = tbl.shape
            width = .8 / n_cols
            if orient == 'v':
                x_range = np.arange(n_rows)
                for i in range(n_cols):
                    x_data = x_range + i * width
                    height = tbl.iloc[:, i].values
                    ax.bar(x_data, height, width, label=tbl.columns[i])
                ax.set_xticks(x_range + width * (n_cols - 1) / 2)
                ax.set_xticklabels(tbl.index)
                ax.tick_params(axis='x', labelrotation=rot)
            else:
                x_range = np.arange(n_rows, 0, -1)
                for i in range(n_cols):
                    x_data = x_range - i * width
                    height = tbl.iloc[:, i].values
                    ax.barh(x_data, height, width, label=tbl.columns[i])
                ax.set_yticks(x_range - width * (n_cols - 1) / 2)
                ax.set_yticklabels(tbl.index)
            ax.legend()

    if (row is not None and col is None) or (row is None and col is not None):
        if row is not None:
            rc_name = 'row'
            rc_col_name = row
            is_row = True
            rc_data = row_data
        else:
            rc_name = 'col'
            rc_col_name = col
            is_row = False
            rc_data = col_data

        if groupby is None:
            if hue is None:
                if agg_kind == 'O':
                    if normalize == rc_name:
                        normalize = 'columns'
                    elif normalize == 'agg':
                        normalize = 'index'
                    elif normalize == 'all':
                        pass
                    elif normalize is None:
                        normalize=False
                    else:
                        raise ValueError('`normalize` can only be False, one of the parameter '
                                         'names "agg", "groupby", "hue", "row", "col", '
                                         'or a combination '
                                         'of those parameter names in a tuple, if they are '
                                         'defined.')
                    tbl = pd.crosstab(agg_data, rc_data, normalize=normalize)
                    n_rows, n_cols = tbl.shape
                    fig_rows, fig_cols = _get_fig_shape(n_cols, wrap, is_row)
                    fig, ax_array = plt.subplots(fig_rows, fig_cols, figsize=figsize,
                                                 sharex=sharex, sharey=sharey)
                    width = .8

                    x_range = np.arange(n_rows)
                    if is_row:
                        ax_flat = ax_array.T.flatten()
                    else:
                        ax_flat = ax_array.flatten()
                    for i, ax in enumerate(ax_flat[:n_cols]):
                        height = tbl.iloc[:, i].values
                        if orient == 'v':
                            x_data = x_range
                            ax.bar(x_data, height, width)
                            ax.set_xticks(x_range)
                            ax.set_xticklabels(tbl.index)

                        if orient == 'h':
                            y_data = x_range[::-1]
                            ax.barh(y_data, height, width)

                        ax.set_title(f'{rc_col_name} = {tbl.columns[i]}')

                    if orient == 'v':
                        if ax_array.ndim == 1:
                            for ax in ax_array:
                                ax.set_xticks(x_range)
                                ax.set_xticklabels(tbl.index)
                                ax.tick_params(axis='x', labelrotation=rot)
                        else:
                            n_full_cols = n_cols % fig_cols
                            if n_full_cols == 0:
                                n_full_cols = fig_cols
                            last_row_axes = ax_array[-1, :n_full_cols]
                            for ax in last_row_axes:
                                ax.tick_params(axis='x', labelrotation=rot, labelbottom=True)
                            second_last_row_axes = ax_array[-2, n_full_cols:]
                            for ax in second_last_row_axes:
                                ax.tick_params(axis='x', labelrotation=rot, labelbottom=True)
                    else:
                        if ax_array.ndim == 1:
                            first_col_axes = ax_array[:1]
                        else:
                            first_col_axes = ax_array[:, 0]
                        for ax in first_col_axes:
                            ax.set_yticks(y_data)
                            ax.set_yticklabels(tbl.index)

                        n_full_cols = n_cols % wrap
                        if n_full_cols == 0:
                            n_full_cols = wrap

                        second_last_row_axes = ax_array[-2, n_full_cols:]
                        for ax in second_last_row_axes:
                            ax.tick_params(axis='x', labelbottom=True)

                        fig.tight_layout()

                    for ax in ax_flat[n_cols:]:
                        ax.remove()
                else:
                    # just one aggregation per Axes
                    # will rarely happen
                    tbl = data.groupby(rc_col_name).agg({agg: aggfunc})
                    n_rows = tbl.shape[0]
                    fig_rows, fig_cols = _get_fig_shape(n_rows, wrap, is_row)
                    fig, ax_array = plt.subplots(fig_rows, fig_cols, figsize=figsize,
                                                 sharex=sharex, sharey=sharey)
                    if is_row:
                        ax_flat = ax_array.T.flatten()
                    else:
                        ax_flat = ax_array.flatten()

                    for i, ax in enumerate(ax_flat[:n_rows]):
                        height = tbl.iloc[i]
                        idx = tbl.index[i]
                        if orient == 'v':
                            ax.bar(idx, height, width=.5)
                            ax.tick_params(labelbottom=False)

                        if orient == 'h':
                            ax.barh(idx, height)
                            ax.tick_params(labelleft=False)

                        ax.set_title(f'{rc_col_name} = {idx}')

                    if orient == 'h':
                        if ax_array.ndim == 1:
                            for ax in ax_array:
                                ax.tick_params(labelbottom=True)
                        else:
                            ax.tick_params(labelbottom=True)

                    for ax in ax_flat[n_rows:]:
                        ax.remove()

                    fig.tight_layout()
            else:
                # hue is not None
                if agg_kind == 'O':
                    tbl = data.groupby([rc_col_name, agg, hue]).size().unstack(fill_value=0)
                    row_levels = tbl.index.levels[0]

                    if normalize == 'all':
                        tbl = tbl / tbl.values.sum()
                    elif normalize == rc_name:
                        tbl = tbl.div(tbl.groupby(rc_col_name).sum().sum(axis=1), axis=0, level=0)
                    elif normalize == 'agg':
                        tbl = tbl.div(tbl.groupby(agg).sum().sum(axis=1), axis=0, level=1)
                    elif normalize == 'hue':
                        tbl = tbl / tbl.sum()
                    elif normalize is None:
                        pass
                    elif isinstance(normalize, tuple):
                        n_set = set(normalize)
                        if n_set == set((rc_name, 'hue')):
                            tbl = tbl.div(tbl.groupby(rc_col_name).sum(), axis=0)
                        elif n_set == set((rc_name, 'agg')):
                            tbl = tbl.div(tbl.sum(1), axis=0, level=1)
                        elif n_set == set(('agg', 'hue')):
                            t1 = tbl.groupby(agg).sum()
                            tbl = tbl / t1
                    else:
                        raise ValueError('`normalize` must either be None, one of the strings, '
                                         '"all", "agg", "hue", "row", "col", or a tuple '
                                         'containing a combination of "agg", "hue", "row", "col".')

                    # number of total plotting surfaces
                    n_axes = len(row_levels)
                    fig_rows, fig_cols = _get_fig_shape(n_axes, wrap, is_row)
                    fig, ax_array = plt.subplots(fig_rows, fig_cols, figsize=figsize,
                                                 sharex=sharex, sharey=sharey)
                    if is_row:
                        ax_flat = ax_array.T.flatten()
                    else:
                        ax_flat = ax_array.flatten()
                    for i, (row_level, ax) in enumerate(zip(row_levels, ax_flat[:n_axes])):
                        cur_tbl = tbl.loc[row_level]
                        n_rows, n_cols = cur_tbl.shape
                        width = .8 / n_cols

                        if orient == 'v':
                            x_range = np.arange(n_rows)
                            for j in range(n_cols):
                                x_data = x_range + j * width
                                height = cur_tbl.iloc[:, j].values
                                if i == 0:
                                    ax.bar(x_data, height, width, label=cur_tbl.columns[j])
                                else:
                                    ax.bar(x_data, height, width)
                            ax.set_xticks(x_range + width * (n_cols - 1) / 2)
                            ax.set_xticklabels(cur_tbl.index)
                            ax.tick_params(axis='x', labelrotation=rot)
                            ax.set_title(f'{rc_col_name} = {row_level}')
                        else:
                            x_range = np.arange(n_rows, 0, -1)
                            for j in range(n_cols):
                                x_data = x_range - j * width
                                height = cur_tbl.iloc[:, j].values
                                if i == 0:
                                    ax.barh(x_data, height, width, label=cur_tbl.columns[j])
                                else:
                                    ax.barh(x_data, height, width)
                            ax.set_yticks(x_range - width * (n_cols - 1) / 2)
                            ax.set_yticklabels(cur_tbl.index)
                            ax.tick_params(axis='x', labelrotation=rot)
                            ax.set_title(f'{rc_col_name} = {row_level}')

                    if normalize is False:
                        fig.suptitle('Total Count', y=1.01, fontsize=20)
                    elif normalize == 'all':
                        fig.suptitle('Normalized Count by all', y=1.01, fontsize=20)
                    elif isinstance(normalize, tuple):
                        locs = locals()
                        cols = [locs[norm] for norm in normalize]
                        normalized_columns = ', '.join(cols)
                        fig.suptitle(f'Normalized Count by {normalized_columns}', y=1.01,
                                     fontsize=20)
                    else:
                        normalized_column = locals()[normalize]
                        fig.suptitle(f'Normalized Count by {normalized_column}', y=1.01, fontsize=20)

                    fig.legend()
                    fig.tight_layout()
                else:
                    tbl = data.groupby([rc_col_name, hue]).agg({agg: aggfunc}).squeeze().unstack()
                    row_levels = tbl.index
                    n_axes = len(row_levels)
                    fig_rows, fig_cols = _get_fig_shape(n_axes, wrap, is_row)
                    fig, ax_array = plt.subplots(fig_rows, fig_cols, figsize=figsize,
                                                 sharex=sharex, sharey=sharey)
                    if is_row:
                        ax_flat = ax_array.T.flatten()
                    else:
                        ax_flat = ax_array.flatten()
                    for i, (row_level, ax) in enumerate(zip(row_levels, ax_flat[:n_axes])):
                        n_cols = len(tbl.columns)
                        height = tbl.iloc[i].values
                        ax.set_title(f'{rc_col_name} = {row_level}')
                        if orient == 'v':
                            x_range = np.arange(n_cols)
                            for x1, h1 in zip(x_range, height):
                                ax.bar(x1, h1)
                            ax.set_xticks(x_range)
                            ax.set_xticklabels(tbl.columns)
                            ax.tick_params(axis='x', labelrotation=rot)
                        else:
                            x_range = np.arange(n_cols, 0, -1)
                            for x1, h1 in zip(x_range, height):
                                ax.barh(x1, h1)
                            ax.set_yticks(x_range)
                            ax.set_yticklabels(tbl.columns)
                    fig.text(-.05, 0.5, f'{agg}', va='center', rotation='vertical', fontsize=20)
                    fig.tight_layout()

                for ax in ax_flat[n_axes:]:
                    ax.remove()

                if ax_array.ndim == 2:
                    n_full_cols = n_axes % fig_cols
                    if n_full_cols == 0:
                        n_full_cols = fig_cols
                    last_row_axes = ax_array[-1, :n_full_cols]
                    for ax in last_row_axes:
                        ax.tick_params(axis='x', labelrotation=rot, labelbottom=True)
                    second_last_row_axes = ax_array[-2, n_full_cols:]
                    for ax in second_last_row_axes:
                        ax.tick_params(axis='x', labelrotation=rot, labelbottom=True)

            return fig
        else:
            # groupby is not none
            if agg_kind == 'O':
                raise TypeError('When the `agg` column is categorical, you cannot use `groupby`. '
                                'Instead, place the groupby column as either '
                                ' `hue`, `row`, or `col`.')
            else:
                if hue is None:
                    tbl = data.groupby([groupby, rc_col_name]).agg({agg: aggfunc}).squeeze().unstack()
                    n_axes = len(tbl.columns)
                    n_bars = len(tbl)
                    fig_rows, fig_cols = _get_fig_shape(n_axes, wrap, is_row)
                    fig, ax_array = plt.subplots(fig_rows, fig_cols, figsize=figsize,
                                                 sharex=sharex, sharey=sharey)
                    if is_row:
                        ax_flat = ax_array.T.flatten()
                    else:
                        ax_flat = ax_array.flatten()
                    for i, ax in enumerate(ax_flat[:n_axes]):
                        height = tbl.iloc[:, i].values
                        ax.set_title(f'{rc_col_name} = {tbl.columns[i]}')
                        if orient == 'v':
                            x_range = np.arange(n_bars)
                            for x1, h1 in zip(x_range, height):
                                ax.bar(x1, h1)
                            ax.set_xticks(x_range)
                            ax.set_xticklabels(tbl.index)
                            ax.tick_params(axis='x', labelrotation=rot)
                        else:
                            x_range = np.arange(n_bars, 0, -1)
                            for x1, h1 in zip(x_range, height):
                                ax.barh(x1, h1)
                            ax.set_yticks(x_range)
                            ax.set_yticklabels(tbl.index)
                    for ax in ax_flat[n_axes:]:
                        ax.remove()

                    if ax_array.ndim == 2:
                        n_full_cols = n_axes % fig_cols
                        if n_full_cols == 0:
                            n_full_cols = fig_cols
                        second_last_row_axes = ax_array[-2, n_full_cols:]
                        for ax in second_last_row_axes:
                            ax.tick_params(axis='x', labelrotation=rot, labelbottom=True)
                else:
                    tbl = data.groupby([groupby, hue, rc_col_name]).agg({agg: aggfunc}).squeeze().unstack()
                    n_axes = len(tbl.columns)
                    n_bars = len(tbl)
                    fig_rows, fig_cols = _get_fig_shape(n_axes, wrap, is_row)
                    fig, ax_array = plt.subplots(fig_rows, fig_cols, figsize=figsize,
                                                 sharex=sharex, sharey=sharey)
                    if is_row:
                        ax_flat = ax_array.T.flatten()
                    else:
                        ax_flat = ax_array.flatten()
                    for i, (col_name, ax) in enumerate(zip(tbl.columns, ax_flat[:n_axes])):
                        cur_tbl = tbl[col_name].unstack()
                        n_groups = len(cur_tbl.columns)
                        ax.set_title(f'{rc_col_name} = {col_name}')
                        x_labels = cur_tbl.index
                        n_bars = len(x_labels)
                        width = .8 / n_groups
                        x_range = np.arange(n_bars)
                        for j, hue_name in enumerate(cur_tbl.columns):
                            height = cur_tbl[hue_name].values
                            label_name = hue_name
                            if i > 0:
                                label_name = ''
                            if orient == 'v':
                                ax.bar(x_range + j * width, height, width, label=label_name)
                                ax.set_xticks(x_range + j / 2 * width)
                                ax.set_xticklabels(x_labels)
                                ax.tick_params(axis='x', labelrotation=rot)
                            else:
                                x_range = np.arange(n_bars, 0, -1)
                                ax.barh(x_range + 1 - j * width, height, width, label=label_name)
                                ax.set_yticks(x_range + width * n_groups / 2 + width)
                                ax.set_yticklabels(x_labels[::-1])
                    for ax in ax_flat[n_axes:]:
                        ax.remove()

                    fig.legend()
                    fig.tight_layout()
                return fig
    if row is not None and col is not None:
        if groupby is None and hue is None:
            if agg_kind == 'O':
                tbl = data.groupby([row, col, agg]).size().unstack()
            else:
                tbl = data.groupby([row, col]).agg({agg: aggfunc})
            row_levels = tbl.index.levels[0]
            col_levels = tbl.index.levels[1]
            fig_rows = len(row_levels)
            fig_cols = len(col_levels)
            fig, ax_array = plt.subplots(fig_rows, fig_cols, figsize=figsize,
                                         sharex=sharex, sharey=sharey)
            for i, row_level in enumerate(row_levels):
                for j, col_level in enumerate(col_levels):
                    ax = ax_array[i, j]
                    cur_tbl = tbl.loc[(row_level, col_level)]
                    height = cur_tbl.values
                    x_labels = cur_tbl.index
                    ax.bar(x_labels, height)
                    ax.set_title(f'{row} = {row_level} | {col} = {col_level}')
                    ax.tick_params(axis='x', labelrotation=rot)
            fig.tight_layout()
            return fig

        if (groupby is not None and hue is None) or (groupby is None and hue is not None):
            grouping_col = groupby or hue
            if agg_kind == 'O':
                raise TypeError('When the `agg` column is categorical, you cannot use `groupby`. '
                                'Instead, place the groupby column as either '
                                ' `hue`, `row`, or `col`.')
            tbl = data.groupby([row, col, grouping_col]).agg({agg: aggfunc}).squeeze().unstack()
            row_levels = tbl.index.levels[0]
            col_levels = tbl.index.levels[1]
            fig_rows = len(row_levels)
            fig_cols = len(col_levels)
            fig, ax_array = plt.subplots(fig_rows, fig_cols, figsize=figsize,
                                         sharex=sharex, sharey=sharey)
            for i, row_level in enumerate(row_levels):
                for j, col_level in enumerate(col_levels):
                    ax = ax_array[i, j]
                    cur_tbl = tbl.loc[(row_level, col_level)]
                    height = cur_tbl.values
                    x_labels = cur_tbl.index
                    ax.bar(x_labels, height)
                    ax.set_title(f'{row} = {row_level} | {col} = {col_level}')
                    ax.tick_params(axis='x', labelrotation=rot)
            return fig

        if groupby is not None and hue is not None:
            if agg_kind == 'O':
                raise TypeError('When the `agg` column is categorical, you cannot use `groupby`. '
                                'Instead, place the groupby column as either '
                                ' `hue`, `row`, or `col`.')
            tbl = data.groupby([row, col, groupby, hue]).agg({agg: aggfunc}).squeeze().unstack()
            row_levels = tbl.index.levels[0]
            col_levels = tbl.index.levels[1]
            fig_rows = len(row_levels)
            fig_cols = len(col_levels)
            fig, ax_array = plt.subplots(fig_rows, fig_cols, figsize=figsize,
                                         sharex=sharex, sharey=sharey)
            for i, row_level in enumerate(row_levels):
                for j, col_level in enumerate(col_levels):
                    ax = ax_array[i, j]
                    cur_tbl = tbl.loc[(row_level, col_level)]
                    n_groups = len(cur_tbl.columns)
                    n_bars = len(cur_tbl.index)
                    x_range = np.arange(n_bars)
                    x_labels = cur_tbl.index
                    hue_labels = cur_tbl.columns
                    width = .8 / n_groups

                    for k in range(n_groups):
                        if i == 0 and j == 0:
                            label_name = hue_labels[k]
                        else:
                            label_name = ''
                        height = cur_tbl.iloc[:, k]
                        if kind == 'point':
                            ax.plot(x_range, height, label=label_name, marker="o")
                        elif kind == 'box':
                            ax.boxplot
                        else:
                            if orient == 'v':
                                ax.bar(x_range + k * width, height, width, label=label_name)
                            else:
                                ax.barh(x_range[::-1] + 1 - k * width, height, width, label=label_name)
                    ax.set_title(f'{row} = {row_level} | {col} = {col_level}')
                    ax.tick_params(axis='x', labelrotation=rot)
                    if kind == 'point':
                        ax.set_xticks(x_range)
                        ax.set_xticklabels(x_labels)
                    else:
                        if orient == 'v':
                            ax.set_xticks(x_range + width * (n_groups - 1) / 2)
                            ax.set_xticklabels(x_labels)
                        else:
                            ax.set_yticks(x_range + 1 - width * (n_groups - 1) / 2)
                            ax.set_yticklabels(x_labels[::-1])


                        # ax.tick_params(axis='y', labelleft=True)
            fig.legend()
            # fig.subplots_adjust(wspace=.2)
            # fig.tight_layout()
            return fig