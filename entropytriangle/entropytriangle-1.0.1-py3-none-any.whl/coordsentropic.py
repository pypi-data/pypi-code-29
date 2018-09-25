'''

Functions used for calculating variables used in the Entropy Triangle Plotting phase

'''

from numpy import nan_to_num as nan_to_num
from warnings import warn as warning
import pandas as pd          # DataFrames manipulation
import matplotlib.pyplot as plt


#Definition of the variables


#SMET
derivedSplitSmetCoords = ["DeltaH_Pxi", "M_Pxi", "VI_Pxi"] # Multivariate entropic coordinates
aggregateSmetCoords = ["H_Ux", "DeltaH_Px", "M_Px", "VI_Px"] # Source multivariate aggregate coordinates (Sum of derivedSplitSmetCoords)
dualAggregateSmetCoords = ["H_Ux", "DeltaH_Px", "D_Px", "VI_Px"] # SMET coords without C_P_X

#CBET
cbetEntropicCoords = ["H_U2", "H_P2", "DeltaH_P2", "M_P2", "VI_P2"] # Caracterization of the variables in a DataFrame of Channel Multivariate Entropies

#CMET
cmetEntropicCoords = ["H_U", "H_P", "DeltaH_P", "M_P", "VI_P"] # Caracterization of the variables in a DataFrame of Channel Multivariate Entropies



#' Functions to detect SMET coordinates

def hasSplitSmetCoords(df):

    """
    A function to detect if the source multivariate split entropies are present: this enables working out the multivariate split entropic coordinates (SMET)
    derivedSplitSmetCoords = ["DeltaH_Pxi", "M_Pxi", "VI_Pxi", "Name"]

    > comprobation = hasSplitSmetCoords(df)

    Parameters
    ----------
    df : DataFrame with entropic variables

    Returns
    ----------
    Boolean: (True or False) In order to check if all the variables at the input dataframe correspond to this type of coordinates

    """
    return (df.columns.isin(derivedSplitSmetCoords).sum() == len(derivedSplitSmetCoords))



def hasAggregateSmetCoords(df):	

    """
    A function to detect if the source multivariate aggregate entropic coordinates are present (SMET)
    aggregateSmetCoords = ["H_Ux", "DeltaH_Px", "M_Px", "VI_Px"]

    > comprobation = hasAggregateSmetCoords(df)

    Parameters
    ----------
    df : DataFrame with entropic variables

    Returns
    ----------
    Boolean: (True or False) In order to check if all the variables at the input dataframe correspond to this type of coordinates

    """
    return (df.columns.isin(aggregateSmetCoords).sum() == len(aggregateSmetCoords))


def hasDualAggregateSmetCoords(df):

    """
    A function to detect if the source multivariate dual aggregate entropic coordinates are present (SMET)
    dualAggregateSmetCoords = ["H_Ux", "DeltaH_Px", "D_Px", "VI_Px"]

    > comprobation = hasDualAggregateSmetCoords(df)

    Parameters
    ----------
    df : DataFrame with entropic variables

    Returns
    ----------
    Boolean: (True or False) In order to check if all the variables at the input dataframe correspond to this type of coordinates

    """
    return (df.columns.isin(dualAggregateSmetCoords).sum() == len(dualAggregateSmetCoords))



#' Functions to detect CMET coordinates

def hasCbetEntropicCoords(df):

    """
    A function to detect if the the channel binary entropic coordinates are present (CBET)
    cmetEntropicCoords = ["H_U2", "H_P2", "DeltaH_P2", "M_P2", "VI_P2"]

    > comprobation = hasCbetEntropicCoords(df)

    Parameters
    ----------
    df : DataFrame with entropic variables

    Returns
    ----------
    Boolean: (True or False) In order to check if all the variables at the input dataframe correspond to this type of coordinates

    """

    #return all(df.columns.isin(cmetEntropicCoords))
    return (df.columns.isin(cbetEntropicCoords).sum() == len(cbetEntropicCoords))


#' Functions to detect CMET coordinates

def hasCmetEntropicCoords(df):

    """
    A function to detect if the the channel multivariate entropic coordinates are present (CMET)
    cmetEntropicCoords = ["H_U", "H_P", "DeltaH_P", "M_P", "VI_P"]

    > comprobation = hasCmetEntropicCoords(df)

    Parameters
    ----------
    df : DataFrame with entropic variables

    Returns
    ----------
    Boolean: (True or False) In order to check if all the variables at the input dataframe correspond to this type of coordinates

    """

    #return all(df.columns.isin(cmetEntropicCoords))
    return (df.columns.isin(cmetEntropicCoords).sum() == len(cmetEntropicCoords))



def entcoords(df,scale=100):

    """
    A function for calculating the normalized coordinates of the entropic measures for some DataFrame.
    It can be used for SMET and CMET cases, returning a list of arrays with the normalized scaled measures

    > entropies_coordinates = entcoords(df)
    >
    > Example:
    >
    > entropies_coordinates = [array([   9.24959601,  142.19609928,    2.96110915]), array([  15.4082864 ,  119.15900389,    1.60549331])]
    >

    Parameters
    ----------
    df : DataFrame with entropic variables
    scale : The scale used for plotting the triangle

    Returns
    ----------
    coor : List with the entropic measures to plot in the De Finneti Diagram

    """

    coor = list()

    for i in range(df.shape[0]):

        if(nan_to_num(df.iloc[i].values[2:6]).sum()>1):
            coor.append((df.iloc[i].values[2:6])/df.iloc[i].values[0])

        else:
            coor.append(df.iloc[i].values[2:6])

    coor = list(map(lambda x: x * scale, coor))

    return coor


