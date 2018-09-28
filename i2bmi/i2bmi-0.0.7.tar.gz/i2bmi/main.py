

import pandas as pd
import pickle
import os
import json

def saveobj(datain,namein='output'):    
    """
    Purpose: 
        Serialize and store objects
    Input:
        datain: Object to be stored
        namein: Path of to-be-stored object
    Output:
        None
    Comments:
        N/A
    """
    with open(namein, 'wb') as fp:
        pickle.dump(datain, fp, protocol=pickle.HIGHEST_PROTOCOL)

def loadobj(namein):
    """
    Purpose: 
        Read and deserialize objects
    Input:
        namein: Path of to-be-read object
    Output:
        Read and deserialized object
    Comments:
        N/A
    """
    curdir=os.path.dirname(__file__)
    newpath=os.path.join(curdir,namein)
    
    with open(newpath, 'rb') as fp:
        data = pickle.load(fp)
        return data



def savejson(datain,namein='output'):
    with open(namein+'.json', 'w') as fp:
        json.dump(datain, fp)

def loadjson(namein):
    with open(namein+'.json', 'r') as fp:
        return json.load(fp)
		
def getmappingfile():
    """
    Purpose: 
        Return bidirectional (icd9 to icd10 and icd10 to icd9 combined) icd mapping file in pandas dataframe format
        Mapping is based on Center for Medicare and Medicaid Services General Equivalence Mappings version 2018 [https://www.cms.gov/Medicare/Coding/ICD10/2018-ICD-10-CM-and-GEMs.html]
    Input:
        None
    Output:
        bidirectional icd mapping file
    Comments:
        A diagnosis code may be mapped to none, one, or multiple diagnosis codes
        Columns for mapping file are as follows:
            source: source icd code
            target: converted icd code
            flag: 
            Approximate
            No Map
            Combination
            Scenario
            Choice List
            sourcetype: icd9 or icd10
            targettype: icd10 or icd9
    """
    curdir=os.path.dirname(__file__)
    newpath=os.path.join(curdir,'mapdf.pickle')
    return pd.read_pickle(newpath)

def getelixhauser_comorbidities():
    """
    Purpose: 
        Returns dictionary for elixhauser comorbidities based on Quan et al (2005):
            Quan H, Sundararajan V, Halfon P, Fong A, Burnand B, Luthi JC, Saunders LD, Beck CA, Feasby TE, Ghali WA. 
            Coding algorithms for defining comorbidities in ICD-9-CM and ICD-10 administrative data. 
            Medical care. 2005 Nov 1:1130-9.
        Scores for elixhauser comorbidity index is based on van Walraven et al (2009):
            van Walraven C, Austin PC, Jennings A, Quan H, Forster AJ. 
            A modification of the Elixhauser comorbidity measures into a point system for hospital death using administrative data. 
            Medical care. 2009 Jun 1:626-33.
    Input:
        N/A
    Output:
        dictionary containing icd9 codes, icd10 codes, and elixhauser comorbidity index score for each comorbidity in the elixhauser comorbidity index.
    Comments:
        N/A
    """
    return loadjson('elixhauser_comorbidities')

def checkcols(datain,idcolumn,icdcolumn):
    """
    Purpose: 
        Ensure that id column and icd column are both present in the dataframe
    Input:
        datain: diagnosis code dataframe in long format
        idcolumn: name of the patient/encounter identifier column
        icdcolumn: name of the icd code column
    Output:
        True if both id column and icd column are both present in the dataframe, False otherwise
    Comments:
        N/A
    """
    if icdcolumn is None:
        print('please specify the icd column')
        return False
    if icdcolumn not in list(datain.columns):
        print('column ['+str(icdcolumn)+'] not found in columns: '+str(datain.columns))
        return False
    if idcolumn is None:
        print('please specify the id column')
        return False
    if idcolumn not in list(datain.columns):
        print('column ['+str(idcolumn)+'] not found in columns: '+str(datain.columns))
        return False
    return True

def cleanicd(dfin,icdcolumn):
    """
    Purpose: 
        Strip whitespace and period from icd codes
    Input:
        dfin: diagnosis code dataframe in long format
        icdcolumn: name of the icd code column
    Output:
        Returns diagnosis dataframe with cleaned up icd code column
    Comments:
        Assuming checkcols has already been performed prior to running this function
    """
    dfin[icdcolumn] = dfin[icdcolumn].astype(str).str.replace('.', '').str.replace(' ','')
    return dfin

def icdconv(datain, idcolumn=None, icdcolumn=None, typecol='ICDtype'):
    """
    Purpose: 
        Convert icd9 to icd10 codes, as well as icd10 to icd9 codes and return a diagnosis dataframe that includes both the original code and the converted code in long format
    Input:
        datain: diagnosis code dataframe in long format
        idcolumn: name of the patient/encounter identifier column
        icdcolumn: name of the icd code column
        typecol: column that indicates if the diagnosis code is in icd9 or icd10
    Output:
        Diagnosis dataframe that includes both the original code and the converted code in long format
    Comments:
        N/A
    """
    mapdf = getmappingfile()
    unqcodes = list(mapdf.source.unique())

    #if pandas dataframe
    if type(datain) == pd.core.frame.DataFrame:
        if checkcols(datain, idcolumn, icdcolumn) == False:
            return None
        dataout_original = datain.loc[:, [idcolumn, icdcolumn]].copy()

        dataout_original=cleanicd(dataout_original,icdcolumn)
        
        dataout_original[typecol] = None
        dataout_original = dataout_original.merge(
            mapdf.loc[:, ['source', 'target', 'sourcetype', 'targettype']],
            left_on=icdcolumn,
            right_on='source',
            how='left')
        #display(dataout_original)
        for icdcode in dataout_original.loc[dataout_original['sourcetype']
                                            .isnull(), icdcolumn]:
            print('Underspecified or unidentifiable diagnosis code: ' + str(icdcode))

        #dataout_original = dataout_original.loc[(dataout_original['sourcetype'].notnull()), :]
        dataout_converted = dataout_original.loc[(dataout_original[
            'target'].notnull()), [idcolumn, 'target', 'targettype']]
        dataout_converted.columns = [idcolumn, icdcolumn, typecol]
        dataout_original = dataout_original.loc[:, [
            idcolumn, icdcolumn, 'sourcetype'
        ]].drop_duplicates()
        dataout_original.columns = [idcolumn, icdcolumn, typecol]
        return pd.concat([dataout_original, dataout_converted], axis=0)   
    
    

    
def icdtophenotype(datain,idcolumn=None,icdcolumn=None,featurematrix=False):
    """
    Purpose: 
        Map icd codes to Elixhauser comorbidites (Quan et al. 2005) and return comorbidity dataframe
    Input:
        datain: diagnosis code dataframe in long format
        idcolumn: name of the patient/encounter identifier column
        icdcolumn: name of the icd code column
        featurematrix: if False, returns a long-format diagnosis dataframe, if True, returns a binary feature-matrix-format diagnosis dataframe
    Output:
        Depending on the featurematrix parameter, either a long-format diagnosis dataframe or a binary feature-matrix-format diagnosis dataframe
    Comments:
        N/A
    """
    elixhauser_comorbidities=getelixhauser_comorbidities()
    
    if checkcols(datain, idcolumn, icdcolumn) == False:
        return None
    
    dataout=datain.copy()
    dataout=cleanicd(dataout,icdcolumn)
    dataout['comorbidity']=None
    
    for como in elixhauser_comorbidities:
        print('Currently processing: '+como+'                                                         ',end="\r",flush=True)
        
        dataout.loc[dataout[icdcolumn].str.startswith(tuple(elixhauser_comorbidities[como]['icd9']+elixhauser_comorbidities[como]['icd10']),na=False),'comorbidity']=como
        
    
    if not featurematrix:
        return dataout
    
    dataout=pd.concat([dataout[idcolumn],pd.get_dummies(dataout['comorbidity'])],axis=1).groupby(idcolumn).max()
    
    return dataout
    
    

def comorbidityindex(datain,scorecol='Elixhauser_Comorbidity_Score',scoreonly=False):
    """
    Purpose: 
        Return Elixhauser Index Score dataframe
    Input:
        datain: phenotype featurematrix
        scorecol: name of the Elixhauser Index Score column in the returned dataframe
        scoreonly: if True, only returns the Elixhauser Index Score, if False, returns the full binary comorbidity dataframe in addition to the Elixhauser Index Score
    Output:
        Elixhauser Index Score dataframe
    Comments:
        N/A
    """

    dataout=datain.copy()
    
    if dataout is None:
        return None
    
    elixhauser_comorbidities=getelixhauser_comorbidities()
    for como in list(dataout.columns):
        dataout.loc[:,como]*=elixhauser_comorbidities[como]['score']
    
    dataout[scorecol]=dataout.sum(axis=1)
    if scoreonly:
        return dataout.loc[:,[scorecol]]
    
    return dataout
    
def comorbiditypipeline(datain, idcolumn=None, icdcolumn=None,scorecol='Elixhauser_Comorbidity_Score'):
    """
    Purpose: 
        Return Elixhauser Index Score dataframe
    Input:
        datain: phenotype featurematrix
        scorecol: name of the Elixhauser Index Score column in the returned dataframe
        scoreonly: if True, only returns the Elixhauser Index Score, if False, returns the full binary comorbidity dataframe in addition to the Elixhauser Index Score
    Output:
        Elixhauser Index Score dataframe
    Comments:
        N/A
    """
    convdiagdf=icdconv(datain, idcolumn=idcolumn, icdcolumn=icdcolumn, typecol='ICDtype')
    phenodf=icdtophenotype(convdiagdf,idcolumn=idcolumn,icdcolumn=icdcolumn,featurematrix=True)
    #display(phenodf.sum(axis=0))
    comodf=comorbidityindex(phenodf,scorecol=scorecol,scoreonly=True)
    return pd.concat([phenodf,comodf],axis=1)

	
def binterp(dfin,idcol,itemcol,valuecol,timecol,bins='30T',binmethod=np.median,method=None,order=1,missimpute=np.median):
    """
    Purpose: 
        Return Elixhauser Index Score dataframe
    Input:
        datain: phenotype featurematrix
        scorecol: name of the Elixhauser Index Score column in the returned dataframe
        scoreonly: if True, only returns the Elixhauser Index Score, if False, returns the full binary comorbidity dataframe in addition to the Elixhauser Index Score
    Output:
        Elixhauser Index Score dataframe
    Comments:
        N/A
    """
    df=dfin.loc[:,[idcol,itemcol,valuecol,timecol]]
    output={}
    
    missimputedf=dfin.groupby(itemcol)[valuecol].agg(missimpute)
    
    
    for curid in df[idcol].unique():
        
        temp=df.loc[df[idcol]==curid,:].pivot_table(index=timecol, columns=itemcol,values=valuecol)
        temp=temp.resample(bins).apply(binmethod)
        
        #no value whatsoever
        for misscol in temp.columns[temp.notnull().sum(axis=0)==0]:
            temp.at[pd.Timedelta(0),misscol]=missimputedf[misscol]
            print('{} had no value in {}'.format(curid,misscol))
        #can't impute with only 1 value
        for misscol in temp.columns[temp.notnull().sum(axis=0)==1]:
            temp.loc[:,misscol]=temp.loc[:,misscol].ffill().bfill()
            print('{} had 1 value in {}'.format(curid,misscol))
        
        
        if method in ['ffill','bfill','default',None,'']:
            temp=temp.ffill().bfill()
        else:
            temp.index=temp.index.values.astype(float)
            temp=temp.interpolate(method=method,order=order,limit_direction='both')
            temp.index=pd.to_timedelta(temp.index)
        
        output[curid]=temp
    return output