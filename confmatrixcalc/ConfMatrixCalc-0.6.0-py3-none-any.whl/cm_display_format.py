"""This module includes functions to format output displays of
one PairedCompResultSet instance,
in graphic and tabular form.

Some formatting parameters are defined by module global variables,
which can be changed by user.

*** Version History:

2018-09-15, first functional version
"""


import numpy as np
import matplotlib.pyplot as plt

from itertools import cycle, product
import logging

plt.rcParams.update({'figure.max_open_warning': 0})

logger = logging.getLogger(__name__)

# --------------------------- Default format dict:
FMT = {'colors': 'rbgk',
       'markers': 'oxs*_',
       'table_format': 'latex',  # or 'tab' for tab-delimited tables
       'figure_format': 'eps',  # or png, or pdf, for saved plots
       'credibility': 'Credibility',
       'test_cond': 'Condition',
       'stim_range': 'S',
       'resp_range': 'R',
       'axis_label': {'MI': 'MI (bits / phoneme)',
                      'PC': 'Prob. Correct (%)'},
       'percentiles': [5., 50., 95.]
       }
# = module-global dict with default settings for formatting details
# that may be changed by user

table_file_suffix = {'latex': '.tex', 'tab': '.txt'}


def _percent():
    """Percent sign, for table headers
    :return: str
    """
    return '\%' if FMT['table_format'] == 'latex' else '%'


def set_format_param(**kwargs):
    """Set / modify module-global format constants
    :param kwargs: dict with format variables
        replacing the default values in FMT
    :return: None
    """
    for (k, v) in kwargs.items():
        k = k.lower()
        if k not in FMT:
            logger.warning(f'Format setting {k}={repr(v)} is not known, not used')
        FMT[k] = v


# ---------------------------------------- Result Classes
class FigureRef():
    """Reference to a single graph instance
    """
    def __init__(self, ax, path=None, name=None):
        """
        :param ax: Axes instance containing the graph
        :param path: Path to directory where figure has been saved
        :param name: name of file, with or without suffix
        """
        self.ax = ax
        self.path = path
        self.name = name

    def __repr__(self):
        return (f'FigureRef(ax= {repr(self.ax)}, ' +
                f'path= {repr(self.path)}, name= {repr(self.name)})')

    @property
    def fig(self):
        return self.ax.figure

    def save(self, path, name=None):
        """Save figure to given path
        :param ax: Axes instance containing the graph
        :param path: Path to directory where figure has been saved
        :param name: (optional) updated name of figure file
        :return: None
        Result: updated properties path, name
        """
        if name is None:
            name = self.name
        path.mkdir(parents=True, exist_ok=True)
        f = (path / name).with_suffix('.' + FMT['figure_format'])
        self.fig.savefig(str(f))
        self.path = path
        self.name = f.name


class TableRef():
    """Reference to a single table instance,
    formatted in LaTeX OR plain tab-separated txt versions
    """
    def __init__(self, text, path=None, name=None):
        """
        :param text: single string with all table text
        :param path: Path to directory where table has been saved
        :param name: name of file, incl suffix
        """
        # store table parts instead *****???
        self.text = text
        self.path = path
        self.name = name

    def __repr__(self):
        return (f'TableRef(text= text, ' +
                f'path= {repr(self.path)}, name= {repr(self.name)})')

    def save(self, path, name=None):
        """Save table to file.
        :param path: Path to directory where tables are saved
        :param name: (optional) updated file name, with or without suffix
            suffix is determined by FMT['table_format'] anyway
        :return: None
        Result: updated properties path, name
        """
        if name is None:
            name = self.name
        path.mkdir(parents=True, exist_ok=True)   # just in case
        f = (path / name).with_suffix(table_file_suffix[FMT['table_format']])
        if self.text is not None and len(self.text) > 0:
            f.write_text(self.text, encoding='utf-8')
        self.path = path
        self.name = f.name


# ----------------------------------------------- Plot Functions:
def fig_percentiles(y_samples,
                    x_labels,
                    y_measure,
                    x_offset=0.1,
                    x_space=0.5,
                    **kwargs):
    """Plot percentile results for one performance measure,
    for ONE or TWO test factors.
    :param y_samples: 2D array of samples of performance measure to be displayed
        y_samples[n, t] = n-th sample in t-th test condition. where
        t is linear index for all combinations of test-factor categories in x_labels.
    :param x_labels: list of one or more tuples (test_factor, tf_category_list), where
        prod(len(tf_category_list)) == y_samples.shape[-1]
    :param y_measure: category ID of performance measure
    :param x_offset: (optional) space between case-variants of plots for each x_tick
        space for about 0.8 / x_offset sub-plots for each main test condition
    :param x_space: (optional) min space outside min and max x_tick values
    :param kwargs: (optional) dict with any additional keyword arguments for plot commands.
    :return: a FigureRef instance
    """
    if y_samples.ndim < 2 or y_samples.shape[-1] == 1:
        return None
    y_p = _get_plot_percentiles(y_samples, x_labels, FMT['percentiles'])
    (x_label, x_ticklabels) = x_labels[0]
    if len(x_labels) > 1:
        xx_labels = x_labels[1][1]
    else:
        xx_labels = ['']
    n_x = y_p.shape[1]
    n_xx = y_p.shape[0]
    x = np.arange(0., n_x) - x_offset * (n_xx - 1) / 2
    fig, ax = plt.subplots()
    for (y, c_label, c, m) in zip(y_p,
                                  xx_labels,
                                  cycle(FMT['colors']),
                                  cycle(FMT['markers'])):
        ax.plot(np.tile(x, (2, 1)),
                [y[:, 0], y[:, 2]],
                linestyle='solid', color=c, **kwargs)
        ax.plot(x, y[:, 1], linestyle='',
                marker=m, markeredgecolor=c, markerfacecolor='w',
                label=c_label, **kwargs)
        x += x_offset
    (x_min, x_max) = ax.get_xlim()
    x_min = min(x_min, -x_space)
    x_max = max(x_max, n_x - 1 + x_space)
    ax.set_xlim(x_min, x_max)
    ax.set_xticks(np.arange(n_x))
    ax.set_xticklabels(x_ticklabels)
    ax.set_ylabel(FMT['axis_label'][y_measure], fontsize='large')
    ax.set_xlabel(x_label, fontsize='large')
    if np.any([len(l) > 0 for l in xx_labels]):
        ax.legend(loc='best')
    f_name = y_measure + '_' + '_'.join(tf for (tf, _) in x_labels)
    return FigureRef(ax, name=f_name)


def fig_indiv_boxplot(y_ind,
                      x_labels,
                      y_measure,
                      x_space=0.5,
                      **kwargs):
    """Boxplot for one individual performance measure
    :param y_ind: 2D or 3D array or array-like list with individual results
        y_ind[n, t0, t1] = y_measure for n-th subject
        in test-condition (x_labels[0]: x_labels[0][t0]),
        AND (x_labels[1]: x_labels[1][t1]) if len(x_labels) > 1
    :param x_labels: list of one or more tuples (test_factor, tf_category_list), where
        prod(len(tf_category_list)) == y_samples.shape[-1]
    :param y_measure: string for y-axis label
    :param x_space: (optional) min space outside min and max x_tick values
    :param kwargs: (optional) dict with any additional keyword arguments for overall command.
    :return: a FigureRef instance
    """
    if len(y_ind) <= 1:
        return None
    y_ind = np.asarray(y_ind)
    if len(x_labels) == 0:  # no test factors, must have empty label
        x_labels = [('', [''])]
    x_label = x_labels[0][0]
    x_ticklabels = x_labels[0][1]
    xx_labels = ['']
    # = labels for sub-conditions
    if y_ind.ndim == 2:
        # no sub-conditions
        y_ind = y_ind[np.newaxis, ...]
    elif y_ind.ndim == 3:
        xx_labels = x_labels[1][1]
        y_ind = y_ind.transpose((2, 0, 1))
        # y_ind[t1, n, t0] for n-th individual result in test-cond (t0, t1)
    else:
        RuntimeError('fig_indiv_boxplot can only handle 1 or 2 test factors')
    (n_xx, n_ind, n_x) = y_ind.shape
    x_offset = min(0.2, 0.8 / len(xx_labels))
    if len(xx_labels) > 1:
        box_width = 0.8 * x_offset
    else:
        box_width = 0.5
    x_pos = np.arange(n_x) - x_offset * (n_xx - 1) / 2
    fig, ax = plt.subplots()
    for (y, c_label, c, m) in zip(y_ind,
                                  xx_labels,
                                  cycle(FMT['colors']),
                                  cycle(FMT['markers'])):
        boxprops = dict(linestyle='-', color=c)
        # flierprops = dict(marker=m, markeredgecolor=c, markerfacecolor='w', # *** markersize=12,
        #                   linestyle='none')
        whiskerprops = dict(marker='', linestyle='-', color=c)
        capprops = dict(marker='', linestyle='-', color=c)
        medianprops = dict(linestyle='-', color=c)
        ax.boxplot(y, positions=x_pos,
                   widths=box_width,
                   sym='',  # ******** no fliers
                   boxprops=boxprops,
                   medianprops=medianprops,
                   whiskerprops=whiskerprops,
                   capprops=capprops,
                   **kwargs)
        median = np.median(y, axis=0)
        ax.plot(x_pos, median, linestyle='',
                marker=m, markeredgecolor=c, markerfacecolor='w',
                label=c_label)
        x_pos += x_offset

    (x_min, x_max) = ax.get_xlim()
    x_min = min(x_min, -x_space)
    x_max = max(x_max, n_x - 1 + x_space)
    ax.set_xlim(x_min, x_max)
    ax.set_xticks(np.arange(len(x_ticklabels)))
    ax.set_xticklabels(x_ticklabels)
    ax.set_ylabel(FMT['axis_label'][y_measure], fontsize='large')
    ax.set_xlabel(x_label)
    if np.any([len(l) > 0 for l in xx_labels]):
        ax.legend(loc='best')
    f_name = y_measure + '-boxplot_' + '_'.join(tf for (tf, _) in x_labels)
    return FigureRef(ax, name=f_name)


# ----------------------------------------------- Table Functions:¨

def tab_percentiles(y_samples,
                    x_labels,
                    y_label):
    """Create table with percentile results,
    one row for each combination of test-factor categories
    from ALL test factors.
    :param y_samples: 2D array of samples of performance measure to be displayed
        y_samples[n, t] = n-th sample in t-th test condition. where
        t is linear index for all combinations of test-factor categories in x_labels.
    :param x_labels: list of one or more tuples (test_factor, tf_category_list), where
        prod(len(tf_category_list)) == y_samples.shape[-1]
    :param y_label: name of performance measure
    :param perc: list of three (min, max, median) percentage values in range 0-100.
        len(perc) == y_p.shape[-1]
    :return: table string with header lines + one line for each x_ticklabels element,
    """

    def gen_rows(y, tc):
        """recursive generator of table rows,
        with one combination of test-factor categories on each row
        """
        if len(tc) == 0:
            yield [f'{y_ip:.3g}' for y_ip in y]
        else:
            for (y_i, t) in zip(y, tc[0]):
                if y_i.ndim == 1:  # only one row of percentiles
                    yield [t] + [f'{y_ip:.3g}' for y_ip in y_i]
                else:
                    for row in gen_rows(y_i, tc[1:]):
                        yield [t] + row

    # ------------------------------------------------------------
    y_p = _get_tab_percentiles(y_samples, x_labels, FMT['percentiles'])
    # y_p[..., p] is p-th percentile value
    # x_labels[0][1][t] corresponds to y_p[t, :, ..., :]
    # x_labels[1][1][t] corresponds to y_p[:, t, ..., :]
    # etc., if there are more than two test factors
    # len(x_labels) == y_p.ndim - 1
    # len(x_labels[i][1]) == y_p.shape[i]
    n_test_factors = y_p.ndim - 1
    n_perc = y_p.shape[-1]
    align = n_test_factors * 'l' + n_perc * 'r'
    # one column for each test_factor, plus one column for each percentile
    head = [x_l[0] for x_l in x_labels] + [f'{p:2.2g}{_percent()}'
                                           for p in FMT['percentiles']]
    # rows = [r for r in gen_rows(y_p, [tfc[1] for tfc in x_labels])]
    f_name = y_label + '_' + '_'.join(tf for (tf, _) in x_labels)
    return TableRef(_make_table(head, gen_rows(y_p, [tfc[1] for tfc in x_labels]), align),
                    name=f_name)


def tab_credible_diff(diff, tf_labels, m_label):
    """Create table with credible differences among test-factor categories
    in LaTeX tabular or in simple tab-separated text format
    :param diff: list of tuples (d, p) defining jointly credible differences, where
        d = (i, j) or (i, j, c), indicating that
        prob{ tf_labels[0][1][i] > tf_labels[0][1][j] } | tf_labels[1][1][c]
            AND all previous pairs } == p
    :param tf_labels: list of one or more tuples (test_factor, tf_cats), where
        test_factor is a string defining the test factor,
        tf_cats = list of categories within this test factor
    :param m_label: string with measure label
    :return: string including all table rows, in FMT['table_fomrat']
    """
    def test_cond(d):
        """Test-factor categories for one difference tuple
        :param d: tuple (i, j) or (i, j, c), where
            i, j are indices of tf_labels[0][1]
            c (if any) is linear index into flattened list of remaining test-conditions
        :return: list of 3 or more table cells
        """
        tc = [tf_cat[0][d[0]], '>', tf_cat[0][d[1]]]
        if len(d) > 2:
            # we have additional test category columns
            t_i = np.unravel_index(d[2], tf_cat_shape[1:])
            # = index tuple into remaining sub-test-categories
            t = [tfc[i] for (i, tfc) in zip(t_i, tf_cat[1:])]
            tc.extend(t)
        return tc
    # ------------------------------------------------------------------------------

    if len(diff) == 0:
        return None
    tf = [t[0] for t in tf_labels]
    tf_cat = [t[1] for t in tf_labels]
    tf_cat_shape = [len(t) for t in tf_cat]
    # = equivalent array shape
    align = 'llc' + len(tf) * 'l' + 'r'
    h = [_make_cell(tf[0], 4, FMT['table_format'])]
    h.extend(tf[1:])  # one extra column for each additional test factor
    h.append(FMT['credibility'])
    rows = []
    col_0 = ''
    # No 'AND' starting first line
    for (d, p) in diff:
        rows.append([col_0, *test_cond(d), f'{100*p:.1f}'])
        col_0 = 'AND' # for all following rows
    f_name = m_label + '-diff_' + '_'.join(t for t in tf)
    return TableRef(_make_table(h, rows, align),
                    name=f_name)


def tab_credible_cell_diff(diff, u, cmf, tf_list=None):
    """Make table of stimulus-response cells with credibly different response probabilities
    among some pair of test-factor categories
    :param diff: list of tuples ((i, j, c), p) defining jointly credible differences, where
        indicating that
        prob{ tf_labels[0][1][i] > tf_labels[0][1][j] } in c-th 'case'
            AND all previous pairs } == p
        c is a linear index into all secondary test conditions AND the stim_range-resp_range array
    :param u: array of response-prob samples, stored as
        u[n, t, sr] = n-th sample of response probability, as when diff was calculated, such that
        u[:, i or j, c] is the response prob corresponding to found indices in diff
    :param cmf: a ConfMatrixFrame instance
    :param tf_list: (optional) list of one or more tuples (test_factor, tf_category_list), where
        len(tf_list[0][1]) == u.shape[1]
        separate input because not necessarily = cmf.test_factors.items()
    :return: a TableRef instance with formatted cell-difference table
    """
    def test_cond(d):
        """Test-factor categories for one difference tuple
        :param d: tuple (i, j, c), where
            i, j are indices of tf_labels[0][1] showing credible differences
            c is linear index into flattened array of
                remaining test-conditions AND stim_range-response categories
        :return: list of 6 or more table cells
        """
        (i, j, c) = d
        if len(tf) == 1:
            (s_ind, r_ind) = np.unravel_index(c, sr_shape)
            tc1 = []
        else:
            # we have additional test category columns
            (*t_ind, s_ind, r_ind) = np.unravel_index(c, tf_cat_shape[1:] + sr_shape)
            # = index tuple into remaining sub-test-categories
            tc1 = [tfc[i] for (i, tfc) in zip(t_ind, tf_cat[1:])]
        cell = [cmf.stim[s_ind], '->', cmf.resp[r_ind]]
        if cmf.resp[r_ind] != cmf.correct_resp[cmf.stim[s_ind]]:
            (j,i) = (i,j)
            # reverse so tf_cat[0][i] is always the BETTER one
        tc0 = [tf_cat[0][i]+':', f'{100*u_md[i, c]:.1f}',
               tf_cat[0][j]+':', f'{100*u_md[j, c]:.1f}']
        # showing main test-cond with response prob.
        return cell + tc0 + tc1
    # ------------------------------------------------------------------------------

    if len(diff) == 0:
        return None
    if tf_list is None:
        tf_list = list(cmf.test_factors.items())
    tf = [t[0] for t in tf_list]
    tf_cat = [t[1] for t in tf_list]
    tf_cat_shape = [len(tc) for tc in tf_cat]
    sr_shape = [len(cmf.stim), len(cmf.resp)]
    u_md = np.median(u, axis=0)
    align = 'lrcl' + 'lrlr' + (len(tf)-1) * 'l' + 'r'
    h = ['', FMT['stim_range'], '->', FMT['resp_range'],
         _make_cell(tf[0], 4, FMT['table_format'])
         ]
    h.extend(tf[1:])  # one extra column for each additional test factor
    h.append(FMT['credibility'])
    rows = []
    col_0 = ''
    # Space for 'AND', except on first line
    for (d, p) in diff:
        rows.append([col_0, *test_cond(d), f'{100*p:.1f}'])
        col_0 = 'AND' # for all following rows
    f_name = 'Cell-diff_' + '_'.join(t for t in tf)
    return TableRef(_make_table(h, rows, align),
                    name=f_name)


# ------------------------------------------module-internal help functions:

# more variants may be added for other table formats

table_begin = {'latex': lambda align: '\\begin{tabular}{' + ' '.join(c for c in align) + '}\n',
               'tab': lambda align: ''}
table_head_sep = {'latex':'\hline\n',
                  'tab':''}
table_cell_sep = {'latex': ' & ',
                  'tab':' \t '}
table_row_sep = {'latex': '\\\\ \n',
                 'tab': '\n'}
table_end = {'latex':'\hline\n\end{tabular}',
             'tab': ''}


def _make_cell(text, col_span, fmt):
    """Format multi-column table cell, usually only for header line
    :param text: cell contents
    :param col_span: number of columns to span
    :param fmt: str key for table format
    :return: string with latex or plain cell contents
    """
    if fmt == 'latex' and col_span > 1:
        return '\multicolumn{' + f'{col_span}' + '}{c}' + '{' + text + '}'
    else:
        return text  # + tabs ???? ***************


def _make_table(header, rows, col_alignment):
    """Generate a string with table text.
    :param header: list with one string for each table column
    :param rows: iterable of rows, where
        each row is a list of string objects for each column in this row
    :param col_alignment: list of alignment symbols, l, r, or c
        len(col_alignment) == len(header) == len(row), for every row in rows

    :return: single string with complete table
    """
    def make_row(cells, fmt):
        return table_cell_sep[fmt].join(f'{c}' for c in cells) + table_row_sep[fmt]
    # ------------------------------------------------------------------------

    fmt = FMT['table_format']
    t = table_begin[fmt](col_alignment)
    t += table_head_sep[fmt]
    t += make_row(header, fmt)
    t += table_head_sep[fmt]
    t += ''.join((make_row(r, fmt) for r in rows))
    t += table_end[fmt]
    return t


def _get_plot_percentiles(m_samples, tf_list, perc):   # ****** use FMT['percentiles'] ****
    """Calculate percentiles in suitable form, and labels for displaying
    only for the FIRST and SECOND test-factor categories.
    :param m_samples: 2D array of samples of one performance measure
        m_samples[n, t] = n-th sample for t-th test condition
        m_samples.shape[-1] == prod(cmf.n_test_factor_conditions)
    :param tf_list: list of (tf, tf_cats) elements
    :param perc: list with (exactly three ***?) percentile values, in percent
    :return: y_p = 3D array of quantiles, with y_p[..., p] =  perc[p] percentile value
        y_p[t, :, :] = percentiles for tf_list[0][1][t]
        y_p[:, t, :] = percentiles for tf_list[1][1][t]
            etc., ****** for now max TWO test factors to be plotted
    """
    n_tfc = [len(tfc[1]) for tfc in tf_list]
    # prod(n_tfc) == m_samples.shape[-1]
    if len(n_tfc) == 1:
        m_samples = m_samples.T[:, np.newaxis, :]
        # y_p = np.percentile(m_samples, perc, axis=-1)
        # return y_p.T
    else:
        m_samples = m_samples.T.reshape((*n_tfc[:2], -1))
    y_p = np.percentile(m_samples, perc, axis=-1)
    return y_p.transpose((2, 1, 0))


def _get_tab_percentiles(m_samples, tf_list, perc):
    """Calculate percentiles in suitable form for tab_percentile tables,
    including ALL test-factor categories.
    :param m_samples: 2D array of samples of one performance measure
        m_samples[n, t] = n-th sample for t-th test condition
        m_samples.shape[-1] == prod(cmf.n_test_factor_conditions)
    :param tf_list: list of (tf, tf_cats) elements
    :param perc: list with (exactly three ***?) percentile values, in percent
    :return: q = mD array of quantiles, with y_p[..., p] =  perc[p] percentile value
        q[t, :, :] = percentiles for tf_list[0][1][t]
        q[:, t, :] = percentiles for tf_list[1][1][t]
        etc.
        q.ndim == 1 + len(tf_list)
    """
    n_tfc = [len(tfc[1]) for tfc in tf_list]
    # prod(n_tfc) == m_samples.shape[-1]
    q = np.percentile(m_samples, perc, axis=0)
    # = quantiles for ALL combinations of test-factor categories
    return q.T.reshape((*n_tfc, -1))
