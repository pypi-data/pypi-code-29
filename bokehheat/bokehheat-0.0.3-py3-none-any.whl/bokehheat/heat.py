###
# title: heat.py
#
# language: python 3.6
# dependencies: bokeh, pandas, scipy
# date: 2018-08
# license: >= GPLv3
# authors: bue, jenny
#
# install:
#    pip3 install bokehheat
#
# load:
#    from bokehheat import heat
#
#    help(heat.cdendro)
#    help(heat.cbar)
#    help(heat.bbar)
#    help(heat.qbar)
#    help(heat.heatmap)
#    help(heat.clustermap)
#
# test run:
#    python3 heat.py
#
# description:
#     A python3 bokeh based categorical dendrogram and heatmap plotting library.
###

# library
from bokeh.io import output_file, reset_output, save
from bokeh.layouts import layout, row
from bokeh.models import ColorBar
from bokeh.palettes import Reds9, RdBu11
from bokeh.plotting import figure
from bokeh.transform import linear_cmap
import json
import pkg_resources
from scipy.cluster.hierarchy import cophenet, dendrogram, linkage
from scipy.spatial.distance import pdist
import sys

# error handling
with open(pkg_resources.resource_filename("bokehheat", "error.json")) as f_json:
    ds_error = json.load(f_json)

# functions
def cdendro(
        df_matrix,
        s_root = 'left',
        s_method = 'single',
        s_metric = 'euclidean',
        b_optimal_ordering = True
    ):
    '''
    input:
        df_matrx: a pandas dataframe where
            the index have to cary the y axis label.
            the column have to cary the x axis label.
            the matrix as such should only cary the z axis values.

        s_root: string. where is the origin of the dendrogram?
            possible values are: left, right, top, bottom.

        s_method:string. detailed description at
            https://docs.scipy.org/doc/scipy/reference/cluster.hierarchy.html
            default single.

        s_metric: string. detailed description at
            https://docs.scipy.org/doc/scipy/reference/cluster.hierarchy.html
            default euclidean.

        b_optimal_ordering: boolean. detailed description at
            https://docs.scipy.org/doc/scipy/reference/cluster.hierarchy.html
            default is True.

    output:
        r_cophcorre: real. cophnetic correlation coefficent. check out
            https://en.wikipedia.org/wiki/Cophenetic

        ls_cat_sorted: list of string with the leaves ordered by
           the applied cluster algorithmen.

        p: bokeh plot object.

    description:
        utilizes scipys pdist, linkage, dendrogram and copdist function
        to generate a bokeh based dendrogram.

        thank you to Jorn Hees who wrote an excellent tutorial about
        hierarchical clustering and dendrograms in scipy and Daniel Russo
        who wrote the only bokeh based dendrogram implementation I was aware of
        at the time I was writing this code.
        + https://joernhees.de/blog/2015/08/26/scipy-hierarchical-clustering-and-dendrogram-tutorial/
        + https://russodanielp.github.io/plotting-a-heatmap-with-a-dendrogram-using-bokeh.html
    '''
    # index or column dendrogram
    if s_root in {'top','bottom'}:
        df_matrix = df_matrix.T

    # distance calculation
    ar_z_linkage = linkage(
        df_matrix,
        method=s_method,
        metric=s_metric,
        optimal_ordering=b_optimal_ordering,
    )
    # cophenetic correlation coefficient calculation
    # bue: how good preserves the clustering the original distance
    r_cophcorre, ar_copdist = cophenet(ar_z_linkage, pdist(df_matrix))
    # categorical leaf layout
    d_dendro = dendrogram(ar_z_linkage, no_plot=True)
    ls_cat_sorted = list(df_matrix.iloc[d_dendro['leaves'],:].index)
    # categorical to number
    d_i2cat = {}
    for i, cat in enumerate(df_matrix.index.values):
        d_i2cat.update({i: cat})
    # linkage number to categorical
    ll_z_linkage = []
    for z_linkage in ar_z_linkage:
        l_z_linkage = list(z_linkage)
        s_cat0 = d_i2cat[int(l_z_linkage[0])]
        s_cat1 = d_i2cat[int(l_z_linkage[1])]
        i_cat0_index = ls_cat_sorted.index(s_cat0)
        i_cat1_index = ls_cat_sorted.index(s_cat1)
        if (i_cat0_index < i_cat1_index):
            d_i2cat.update({len(d_i2cat): s_cat0})
        else:
            d_i2cat.update({len(d_i2cat): s_cat1})
        l_z_linkage[0] = s_cat0
        l_z_linkage[1] = s_cat1
        l_z_linkage[3] = int(l_z_linkage[3])
        ll_z_linkage.append(l_z_linkage)

    # plot categorical
    if s_root in {'right'}:
        p = figure(
            y_range=ls_cat_sorted,
            title=f"cophentic: {round(r_cophcorre,3)}",
        )
        for l_z_linkage in ll_z_linkage:
            p.line(y=[l_z_linkage[0],l_z_linkage[1]], x=[l_z_linkage[2], l_z_linkage[2]], line_color='maroon') # horizontal
            p.line(y=[l_z_linkage[0],l_z_linkage[0]], x=[l_z_linkage[2], 0], line_color='maroon') # vertikal 1
            p.line(y=[l_z_linkage[1],l_z_linkage[1]], x=[l_z_linkage[2], 0], line_color='maroon') # vertikal 2
    elif s_root in {'left'}:
        p = figure(
            y_range=ls_cat_sorted,
            title=f"cophentic: {round(r_cophcorre,3)}"
        )
        for l_z_linkage in ll_z_linkage:
            p.line(y=[l_z_linkage[0],l_z_linkage[1]], x=[-(l_z_linkage[2]), -(l_z_linkage[2])], line_color='maroon') # horizontal
            p.line(y=[l_z_linkage[0],l_z_linkage[0]], x=[-(l_z_linkage[2]), 0], line_color='maroon') # vertikal 1
            p.line(y=[l_z_linkage[1],l_z_linkage[1]], x=[-(l_z_linkage[2]), 0], line_color='maroon') # vertikal 2
    elif s_root in {'top'}:
        p = figure(
            x_range=ls_cat_sorted,
            title=f"cophentic: {round(r_cophcorre,3)}"
        )
        for l_z_linkage in ll_z_linkage:
            p.line(x=[l_z_linkage[0],l_z_linkage[1]], y=[l_z_linkage[2], l_z_linkage[2]], line_color='maroon') # horizontal
            p.line(x=[l_z_linkage[0],l_z_linkage[0]], y=[l_z_linkage[2], 0], line_color='maroon') # vertikal 1
            p.line(x=[l_z_linkage[1],l_z_linkage[1]], y=[l_z_linkage[2], 0], line_color='maroon') # vertikal 2
    elif s_root in {'bottom'}:
        p = figure(
            x_range=ls_cat_sorted,
            title=f"cophentic: {round(r_cophcorre,3)}"
        )
        for l_z_linkage in ll_z_linkage:
            p.line(x=[l_z_linkage[0],l_z_linkage[1]], y=[-(l_z_linkage[2]), -(l_z_linkage[2])], line_color='maroon') # horizontal
            p.line(x=[l_z_linkage[0],l_z_linkage[0]], y=[-(l_z_linkage[2]), 0], line_color='maroon') # vertikal 1
            p.line(x=[l_z_linkage[1],l_z_linkage[1]], y=[-(l_z_linkage[2]), 0], line_color='maroon') # vertikal 2

    # output
    return(r_cophcorre, ls_cat_sorted, p)


def qbar(df_axis_annot, s_yx, s_z, r_low, r_high, ls_color_palette, s_root):
    """
    input:
        df_axis_annot: pandas dataframe for y or x axis annotation.

        s_yx: string. column label which specifies the column with the
            samples (or variables) labels to be annotated. e.g.: patient_id.

        s_z: string. column label which specifies the column with the
            quantitative annotation. e.g. age_year.

        r_low: quantitative minimum value. the dataset can contain lower values,
            but for color labeling they will be mapped to this minimum value.
            e.g.: 0.

        r_high: quantitative maximum value. the dataset can contain higher values,
            but for color labeling they will be mapped to this maximum value.
            e.g.: 100

        ls_color_palette: a list color strings to specify the color spectrum.
            this variable is compatible with the ordinary bokeh palettes:
            https://bokeh.pydata.org/en/latest/docs/reference/palettes.html

        s_root: string. how should the bar be placed?
          left and right will result in vertical bar, top and bottom will
          result in a horizontal bar.
          possible values are: left, right, top, bottom.

    output:
        p: bokeh plot object.

    description:
        this function will return an interactive bokeh based
        annotation bar plot for a quantitative variable.
    """
    # color declaration
    d_zcolormapper = linear_cmap(
        field_name=s_z,
        palette=ls_color_palette,
        low=r_low,
        high=r_high
    )

    # tooltip declaration
    lt_tooltip = [
        (s_yx, f"@{s_yx}"),
        (s_z, f"@{s_z}"),
    ]

    # generate figure
    if (s_root in {"left", "right"}):
        p = figure(
            y_range=df_axis_annot[s_yx],
            title=s_z,
            tooltips=lt_tooltip,
        )
        p.hbar(
            source=df_axis_annot,
            y=s_yx,
            right=s_z,
            left=r_low,
            height=0.9,
            color=d_zcolormapper,
        )
        p.yaxis.visible = False
    elif (s_root in {"top", "bottom"}):
        p = figure(
            x_range=df_axis_annot[s_yx],
            title=s_z,
            title_location="right",
            tooltips=lt_tooltip,
        )
        p.vbar(
            source=df_axis_annot,
            x=s_yx,
            top=s_z,
            bottom=r_low,
            width=0.9,
            color=d_zcolormapper,
        )
        p.xaxis.visible = False
    else:
        sys.exit("Error at bokehheat.qbar: {}".format(
            ds_error["root_unknown"].format(s_root)
        ))
    # result
    return(p)


# the bar plot categorical
def cbar(df_axis_annot, s_yx, s_z, s_zcolor, s_root):
    """
    input:
        df_axis_annot: pandas dataframe for y or x axis annotation.

        s_yx: string. column label which specifies the column with the
            samples (or variables) labels to be annotated. e.g.: patient_id.

        s_z: string. column label which specifies the column with the
            quantitative annotation. e.g. age_year.

        s_zcolor: string. column label which specifies the column with the
            color strings related to the categorical annotation.

        s_root: string. how should the bar be placed?
          left and right will result in vertical bar, top and bottom will
          result in a horizontal bar.
          possible values are: left, right, top, bottom.

    output:
        p: bokeh plot object.

    description:
        this function will return an interactive bokeh based
        annotation bar for a categorical variable.
    """
    # tooltip declaration
    lt_tooltip = [
        (s_yx, f"@{s_yx}"),
        (s_z, f"@{s_z}"),
    ]
    # generate figure
    if (s_root in {"left", "right"}):
        p = figure(
            y_range=df_axis_annot[s_yx],
            title = s_z,
            tooltips = lt_tooltip,
        )
        p.hbar(
            source=df_axis_annot,
            y=s_yx,
            right=1,
            left=0,
            height=0.9,
            color=s_zcolor,
        )
    elif (s_root in {"top", "bottom"}):
        p = figure(
            x_range=df_axis_annot[s_yx],
            title = s_z,
            title_location="right",
            tooltips = lt_tooltip,
        )
        p.vbar(
            source=df_axis_annot,
            x=s_yx,
            top=1,
            bottom=0,
            width=0.9,
            color=s_zcolor,
        )
    else:
        sys.exit("Error at bokehheat.cbar: {}".format(
            ds_error["root_unknown"].format(s_root)
        ))
    p.xaxis.visible = False
    p.yaxis.visible = False
    # result
    return(p)


# the bar plot categorical
def bbar(df_axis_annot, s_yx, s_z, s_true_color, s_false_color, s_root):
    """
    input:
        df_axis_annot: pandas dataframe for y or x axis annotation.

        s_yx: string. column label which specifies the column with the
            samples (or variables) labels to be annotated. e.g.: patient_id.

        s_z: string. column label which specifies the column with the
            boolean annotation.

        s_true_color: string. specifies a color hex or name like 'Black'.

        s_false_color: string. specifies a color hex or name like 'Yellow'.

        s_root: string. how should the bar be placed?
          left and right will result in vertical bar, top and bottom will
          result in a horizontal bar.
          possible values are: left, right, top, bottom.

    output:
        p: bokeh plot object.

    description:
        this function will return an interactive bokeh based
        annotation bar for a boolean variable.
    """
    d_color = {True : s_true_color, False : s_false_color}
    df_axis_annot["boolean_color"] = df_axis_annot[s_z].apply(lambda n: d_color[n])
    p = cbar(
        df_axis_annot=df_axis_annot,
        s_yx=s_yx,
        s_z=s_z,
        s_zcolor="boolean_color",
        s_root=s_root
    )
    # result
    return(p)


# the heatmap
def heatmap(df_matrix, ls_color_palette, r_low, r_high, s_z="value"):
    """
    input:
        df_matrx: a dataframe in same xy orientation as the final heatmap.
          the index should cary the y axis label.
          the column should cary the x axis label.
          the matrix as such should only cary the z axis values.

        ls_color_palette: a list color strings to specify the color spectrum.
            this variable is compatible with the ordinary bokeh palettes:
            https://bokeh.pydata.org/en/latest/docs/reference/palettes.html

        r_low: quantitative minimum value. the dataset can contain lower values,
            but for color labeling they will be mapped to this minimum value.
            e.g.: -8.

        r_high: quantitative maximum value. the dataset can contain lower values,
            but for color labeling they will be mapped to this maximum value.
            e.g.: 8.

        s_z: string. label that specifies what the values in the matrix actually
            are. e.g.: 'gene expression [log2]'

    output:
        p: bokeh plot object.

    description:
        this function will return a bokeh based interactive heatmap plot.
        the color are representing the z value.
    """
    # handle y and x axis name
    if (df_matrix.index.name == None):
        df_matrix.index.name = "y_axis"
    if (df_matrix.columns.name == None):
        df_matrix.columns.name = "x_axis"
    s_y = df_matrix.index.name
    s_x = df_matrix.columns.name

    # melt dataframe
    df_tidy = df_matrix.reset_index().melt(
        id_vars=[df_matrix.index.name],
        value_name=s_z
    )
    # color declaration
    d_zcolormapper = linear_cmap(
        field_name=s_z,
        palette=ls_color_palette,
        low=r_low,
        high=r_high
    )
    # tooltip declaration
    lt_tooltip = [
        (s_y, f"@{s_y}"),
        (s_x, f"@{s_x}"),
        (s_z, f"@{s_z}"),
    ]
    # generate figure
    o_colorbar = ColorBar(color_mapper=d_zcolormapper['transform'])
    p = figure(
        y_range=df_matrix.index.values,
        x_range=df_matrix.columns.values,
        tools = "box_zoom,hover,pan,reset",  # have to be set hardcoded
        active_drag = "box_zoom",  # have to be set hardcoded
        tooltips=lt_tooltip,
        title=s_z,
    )
    p.rect(
        source=df_tidy,
        x=s_x,
        y=s_y,
        color=d_zcolormapper,
        width=1,
        height=1,
    )
    p.add_layout(o_colorbar, place='left')
    p.yaxis.major_label_orientation = "horizontal"
    p.xaxis.major_label_orientation = "vertical"
    # out
    return(p)


# the cluster heatmap
def clustermap(
        df_matrix,
        ls_color_palette,
        r_low,
        r_high,
        s_z = "value",
        tt_axis_annot = (),
        b_xdendo = False,
        b_ydendo = False,
        s_method = 'single',
        s_metric = 'euclidean',
        b_optimal_ordering = True,
        i_px = 80,
        i_height = 8,
        i_width = 8,
        s_filename = "clustermap.html",
        s_filetitel = "Bokeh Plot",
    ):
    """
    input:
        df_matrx: a dataframe in same xy orientation as the final heatmap.
            the index have to cary the y axis label.
            the column have to cary the x axis label.
            the matrix as such should only cary the z axis values.

        ls_color_palette: a list color strings to specify the color spectrum.
            this variable is compatible with the ordinary bokeh palettes:
            https://bokeh.pydata.org/en/latest/docs/reference/palettes.html

        r_low: quantitative minimum value. the dataset can contain lower values,
            but for color labeling they will be mapped to this minimum value.
            e.g.: -8.

        r_high: quantitative maximum value. the dataset can contain lower values,
            but for color labeling they will be mapped to this maximum value.
            e.g.: 8.

        s_z: string. label that specifies what the values in the matrix actually
            are. e.g.: 'gene expression [log2]'

        tt_axis_annot: axis annotation tuple.
            categorical and quantitative axis annotation tuples are possible.
            t_axis_annot_boolean = (df_axis_annot, ls_z, s_true_color, s_false_color)
            t_axis_annot_categorical = (df_axis_annot, ls_z, ls_zcolor)
            t_axis_annot_quantitative = (df_axis_annot, ls_z, lr_low, lr_high, lls_color_palette)

            df_axis_annot: pandas datafarme for y or x axis annotation.
                the df_axis_annot index have to carry df_matrix index or column related labels.
                the df_axis_annot column have to carry all needed s_z and s_zcolor labels.

            ls_z: list of annotation labels which should be turned into annotation bars.

            s_true_color: string. color hex or name for True s_z values. e.g 'Yellow'.

            s_false_color: string. color hex or name for False s_z values. e.g. 'Black'.

            ls_zcolor: list of categorical s_z annotation related color column labels.

            lr_low: list of quantitative s_z annotation related minimum values.

            lr_high: list of quantitative s_z annotation related maximum values.

            lls_color_palette: list of quantitative s_z annotation related color palette lists.

        b_ydendro and b_xdendro: boolean, if True the y respective x axis
            get clustered with the specified s_method and s_metiric.
            if False the axis order from the df_matrix is preserved.
            default is False.

        s_method:string. detailed description at
            https://docs.scipy.org/doc/scipy/reference/cluster.hierarchy.html
            default single.

        s_metric: string. detailed description at
            https://docs.scipy.org/doc/scipy/reference/cluster.hierarchy.html
            default euclidean.

        b_optimal_ordering: boolean. detailed description at
          https://docs.scipy.org/doc/scipy/reference/cluster.hierarchy.html
          default is True.

        i_px: integer. clustermap pixel unit.
            the top dendrogram is 2 times this unit high and 8 times this unit width,
            the right dendrogram is 8 time this unit high and 2 times this unit width,
            the top annotation bars are 1 time this unit high and 8 times this unit width,
            the right annotation bars are 8 time this unit high and 1 time this unit width,
            the heatmap is 8 time this unit high and 8 times this unit width.
            if you need smaller labels increase this unit and make the overall plot
            smaller with your browsers zoom function (Ctrl -).
            if you need bigger labels do the opposite.
            default is 80 pixels.

        i_height: integer. i_px * i_height specifies the heatmap height.

        i_width: integer. i_px * i_with specifies the heatmap width.

        s_filename: filename of the resulting html file.
            default is clustermap.html,

        s_filetitel: clustermap plot title.
            this title will be visible as browser tab label.
            default is Bokeh Plot.

    output:
        clustermap.html: resulting html file with the s_filname attribute specified
            file name.

        o_layout: clustermap bokeh layout object.

        ls_yaxis: list of string with the leaves the same ordered
            as the heatmap y axis.

        ls_xaxis: list of string with the leaves the same ordered
            as the heatmap x axis.

    description:
        this function will return an interactive bokeh based clustermap related
        html file, bokeh layout object, list of y axis and list x axis labels.
    """
    ls_yaxis = list(df_matrix.index)
    ls_xaxis = list(df_matrix.columns)

    # handle y and x axis name
    if (df_matrix.index.name == None):
        df_matrix.index.name = "y_axis"
    if (df_matrix.columns.name == None):
        df_matrix.columns.name = "x_axis"

    # cluster y and x
    if (b_ydendo):
        r_cophcorre, ls_yaxis, p_ydendro = cdendro(
            df_matrix,
            s_root='right',
            s_method=s_method,
            s_metric=s_metric,
            b_optimal_ordering=b_optimal_ordering,
        )
        p_ydendro.height = i_height * i_px
        p_ydendro.width = 2 * i_px
        p_ydendro.yaxis.visible = False
        p_ydendro.toolbar_location = None
        df_matrix = df_matrix.loc[ls_yaxis,:]
    if (b_xdendo):
        r_cophcorre, ls_xaxis, p_xdendro = cdendro(
            df_matrix,
            s_root='top',
            s_method=s_method,
            s_metric=s_metric,
            b_optimal_ordering=b_optimal_ordering,
        )
        p_xdendro.height = 2 * i_px
        p_xdendro.width = i_width * i_px
        p_xdendro.xaxis.visible = False
        p_xdendro.toolbar_location = None
        df_matrix = df_matrix.loc[:,ls_xaxis]

    # generate heat map
    p_heatmap = heatmap(
        df_matrix,
        ls_color_palette=ls_color_palette,
        r_low=r_low,
        r_high=r_high,
        s_z=s_z,
    )
    p_heatmap.height = i_height * i_px
    p_heatmap.width = i_width * i_px
    p_heatmap.toolbar_location="below"

    # link dendrogram
    if (b_ydendo):
        p_ydendro.y_range = p_heatmap.y_range
    if (b_xdendo):
        p_xdendro.x_range = p_heatmap.x_range

    # generate y and axis annotation
    lp_ybar = []
    lp_xbar = []
    es_ymatrix = set(df_matrix.index)
    es_xmatrix = set(df_matrix.columns)
    if (len(es_ymatrix) != df_matrix.shape[0]):
        sys.exit("Error at bokehheat.clustermap: {}".format(
            ds_error["y_axis_unique"].format(list(df_matrix.index))
        ))
    if (len(es_xmatrix) != df_matrix.shape[1]):
        sys.exit("Error at bokehheat.clustermap: {}".format(
            ds_error["x_axis_unique"].format(list(df_matrix.columns))
        ))

    for t_axis_annot in tt_axis_annot:

        # check if root is top or right
        es_axis = set(t_axis_annot[0].index)
        b_ok = False
        ls_root = []
        if (len(es_ymatrix.intersection(es_axis)) > 0):
            ls_root.append('right')
            b_ok = True
        if (len(es_xmatrix.intersection(es_axis)) > 0):
            ls_root.append('top')
            b_ok = True
        if not (b_ok):
            sys.exit("Error at bokehheat.clustermap: {}".format(
                ds_error["axis_annot_none"].format(t_axis_annot[1])
            ))

        # categorical
        # t_axis_annot = (df_axis_annot, ls_z, ls_zcolor)
        if (len(t_axis_annot) == 3):
            # extract relevant columns of the dataframe
            for n, s_bz in enumerate(t_axis_annot[1]):
                s_bzcolor = t_axis_annot[2][n]
                df_axis = t_axis_annot[0].loc[:,[s_bz, s_bzcolor]]
                # get df_axis index name
                for s_root in ls_root:
                    # reorder df_axis and include missing values
                    if (s_root == 'top'):
                        df_axis = df_axis.reindex(df_matrix.columns)
                        df_axis = df_axis.loc[df_matrix.columns,:]
                        df_axis.index.name = df_matrix.columns.name
                    else:
                        df_axis = df_axis.reindex(df_matrix.index)
                        df_axis = df_axis.loc[df_matrix.index,:]
                        df_axis.index.name = df_matrix.index.name
                    # call cbar
                    p_bar = cbar(
                        df_axis_annot=df_axis.reset_index(),
                        s_yx=df_axis.index.name,
                        s_z=s_bz,
                        s_zcolor=s_bzcolor,
                        s_root=s_root,
                    )
                    p_bar.toolbar_location = None
                    if (s_root == 'top'):
                        p_bar.x_range = p_heatmap.x_range
                        p_bar.height = i_px
                        p_bar.width = i_width * i_px
                        lp_xbar.append(p_bar)
                    else:
                        p_bar.y_range = p_heatmap.y_range
                        p_bar.height = i_height * i_px
                        p_bar.width = i_px
                        lp_ybar.append(p_bar)

        # boolean
        # t_axis_annot_boolean = (df_axis_annot, ls_z, s_true_color, s_false_color)
        elif (len(t_axis_annot) == 4):
            s_true_color = t_axis_annot[2]
            s_false_color = t_axis_annot[3]
            # extract relevant columns of the dataframe
            for n, s_bz in enumerate(t_axis_annot[1]):
                se_axis = t_axis_annot[0].loc[:,s_bz]
                # get se_axis index name
                for s_root in ls_root:
                    # reorder df_axis and include missing values
                    if (s_root == 'top'):
                        se_axis = se_axis.reindex(df_matrix.columns)
                        se_axis = se_axis.loc[df_matrix.columns]
                        se_axis.index.name = df_matrix.columns.name
                    else:
                        se_axis = se_axis.reindex(df_matrix.index)
                        se_axis = se_axis.loc[df_matrix.index]
                        se_axis.index.name = df_matrix.index.name
                    # call bbar
                    p_bar = bbar(
                        df_axis_annot=se_axis.reset_index(),
                        s_yx=se_axis.index.name,
                        s_z=s_bz,
                        s_true_color=t_axis_annot[2],
                        s_false_color=t_axis_annot[3],
                        s_root=s_root,
                    )
                    p_bar.toolbar_location = None
                    if (s_root == 'top'):
                        p_bar.x_range = p_heatmap.x_range
                        p_bar.height = i_px
                        p_bar.width = i_width * i_px
                        lp_xbar.append(p_bar)
                    else:
                        p_bar.y_range = p_heatmap.y_range
                        p_bar.height = i_height * i_px
                        p_bar.width = i_px
                        lp_ybar.append(p_bar)

        # quantitative
        # t_axis_annot = (df_axis_annot, ls_z, lr_low, lr_high, lls_color_palette)
        elif (len(t_axis_annot) == 5):
            # extract relevant columns of the dataframe
            for n, s_bz in enumerate(t_axis_annot[1]):
                r_blow = t_axis_annot[2][n]
                r_bhigh = t_axis_annot[3][n]
                ls_bcolor = t_axis_annot[4][n]
                se_axis = t_axis_annot[0].loc[:,s_bz]
                # get se_axis index name
                if (se_axis.index.name == None):
                    se_axis.index.name = "variable"
                for s_root in ls_root:
                    # reorder df_axis and include missing values
                    if (s_root == 'top'):
                        se_axis = se_axis.reindex(df_matrix.columns)
                        se_axis = se_axis.loc[df_matrix.columns]
                    else:
                        se_axis = se_axis.reindex(df_matrix.index)
                        se_axis = se_axis.loc[df_matrix.index]
                    # call qbar
                    p_bar = qbar(
                        df_axis_annot=se_axis.reset_index(),
                        s_yx=se_axis.index.name,
                        s_z=s_bz,
                        r_low=r_blow,
                        r_high=r_bhigh,
                        ls_color_palette=ls_bcolor,
                        s_root=s_root,
                    )
                    p_bar.toolbar_location = None
                    if (s_root == 'top'):
                        p_bar.x_range = p_heatmap.x_range
                        p_bar.height = i_px
                        p_bar.width = i_width * i_px
                        lp_xbar.append(p_bar)
                    else:
                        p_bar.y_range = p_heatmap.y_range
                        p_bar.height = i_height * i_px
                        p_bar.width = i_px
                        lp_ybar.append(p_bar)
        # error
        else:
            sys.exit("Error at bokehheat.clustermap: {}".format(
                ds_error["axis_annot_invalid"].format(t_axis_annot)
            ))

    ### put output top down together ###
    reset_output()
    output_file(s_filename, title=s_filetitel)
    lp_out = []
    lp_top = []
    llp_middle = []
    lp_bottom = []
    # check for top dendrogram
    if (b_xdendo):
        lp_top.append(p_xdendro)
    # check for top axis annotation
    for p_xbar in lp_xbar:
        llp_middle.append([p_xbar])
    # all
    lp_bottom.append(p_heatmap)
    # check for right side axis annotation
    for p_ybar in lp_ybar:
        lp_bottom.append(p_ybar)
    # check for right side dendogram
    if (b_ydendo):
        lp_bottom.append(p_ydendro)
    # kick out top row when only None
    if (len(lp_top) > 0):
        lp_out.append(lp_top)
    # kick out middle row when no top axis annotation
    if (len(llp_middle) > 0):
        for lp_middle in llp_middle:
            lp_out.append(lp_middle)
    # bottom row has always heatmap
    lp_out.append(row(lp_bottom))

    # output
    o_layout = layout(lp_out, sizing_mode='fixed')
    save(o_layout)
    return(o_layout, ls_yaxis, ls_xaxis)



if __name__ == '__main__':
    ###
    # test and demo case
    # run:
    #    python3 heat.py
    ###

    # library
    from bokeh.palettes import Reds9, YlGn8, Colorblind8
    import numpy as np
    import pandas as pd

    # prepare some data
    ls_sample = ['sampleA','sampleB','sampleC','sampleD','sampleE','sampleF','sampleG','sampleH']
    ls_variable = ['geneA','geneB','geneC','geneD','geneE','geneF','geneG','geneH', 'geneI']
    ar_z = np.random.rand(8,9)
    df_matrix = pd.DataFrame(ar_z)
    df_matrix.index = ls_sample
    df_matrix.columns = ls_variable
    df_matrix.index.name = 'y'
    df_matrix.columns.name = 'x'

    df_sample = pd.DataFrame({
        'y': ls_sample,
        'age_year': list(np.random.randint(0,101, 8)),
        'sampletype': ['LumA','LumA','LumA','LumB','LumB','Basal','Basal','Basal'],
        'sampletype_color': ['Cyan','Cyan','Cyan','Blue','Blue','Red','Red','Red'],
        'sampleboole': [False, False, True, True, True, True, False, False],
    })
    df_sample.index = df_sample.y

    df_variable = pd.DataFrame({
        'x': ls_variable,
        'genereal': list(np.random.random(9) * 2 - 1),
        'genetype': ['Lig','Lig','Lig','Lig','Lig','Lig','Rec','Rec','Rec'],
        'genetype_color': ['Yellow','Yellow','Yellow','Yellow','Yellow','Yellow','Brown','Brown','Brown'],
        'geneboole': [False, False, False, True, True, True, False, False, False],
    })
    df_variable.index = df_variable.x

    t_ycat = (
        df_sample,
        ['sampletype'],
        ['sampletype_color'],
    )
    t_yboole = (
        df_sample,
        ['sampleboole'],
        'Red',  # True
        'Black',  # False
    )
    t_yquant = (
        df_sample,
        ['age_year'],
        [0],
        [128],
        [YlGn8],
    )
    t_xcat = (
        df_variable,
        ['genetype'],
        ['genetype_color'],
    )
    t_xboole = (
        df_variable,
        ['geneboole'],
        'Red',  # True
        'Black',  # False
    )
    t_xquant = (
        df_variable,
        ['genereal'],
        [-1],
        [1],
        [Colorblind8],
    )
    tt_catboolquant = (t_ycat, t_yboole, t_yquant, t_xquant, t_xboole, t_xcat)
    #tt_catboolquant = (t_ycat, t_yboole, t_yquant)
    #tt_catboolquant = (t_xquant, t_xboole, t_xcat)

    s_file = "theclustermap.html"
    o_clustermap, ls_xaxis, ls_yaxis = clustermap(
        df_matrix = df_matrix,
        ls_color_palette = Reds9,
        r_low = 0,
        r_high = 1,
        s_z = "log2",
        tt_axis_annot = tt_catboolquant,
        b_ydendo = True,
        b_xdendo = True,
        #s_method='single',
        #s_metric='euclidean',
        #b_optimal_ordering=True,
        i_px = 80,
        i_height = 8,
        i_width = 8,
        s_filename=s_file,
        s_filetitel="the Clustermap",
    )

    # output
    print(f"\ncheck out: {s_file}")
    print(f"y axis is: {ls_yaxis}")
    print(f"x axis is: {ls_xaxis}")
