import pickle
import datetime
import logging
import pandas as pd
import numpy as np
from scipy import linalg
from scipy import stats
import biogeme.version as bv
import biogeme.filenames as bf
import biogeme.exceptions as excep


def calcPValue(t):
    """ Calculates the p value of a parameter from its t-statistic.
    Args:
        :param t: t-statistics
        :type real
    Return: p-value
    """
    p = 2.0 * (1.0 - stats.norm.cdf(abs(t)))
    return p

class beta:
    """ Class gathering the information related to the parameters of the model

    Args:
        :param name: name of the parameter
        :type str

        :param: value: value of the parameter
        :type float
    """
    def __init__(self,name,value):
        self.name = name
        self.value = value
        self.stdErr = None
        self.tTest = None
        self.pValue = None
        self.robust_stdErr = None
        self.robust_tTest = None
        self.robust_pValue = None
        self.bootstrap_stdErr = None
        self.bootstrap_tTest = None
        self.bootstrap_pValue = None
        

    def setStdErr(self,se):
        """ Records the standard error, and calculates and records 
            the corresponding t-statistic and p-value
        Args:
            :param se: standard error

        Returns: nothing
        """
        self.stdErr = se
        self.tTest = np.nan_to_num(self.value / se)
        self.pValue = calcPValue(self.tTest)

    def setRobustStdErr(self,se):
        """ Records the robust standard error, and calculates and records 
            the corresponding t-statistic and p-value
        Args:
            :param se: robust standard error
        
        Returns: nothing
        """
        self.robust_stdErr = se
        self.robust_tTest = np.nan_to_num(self.value / se)
        self.robust_pValue = calcPValue(self.robust_tTest)

    def setBootstrapStdErr(self,se):
        self.bootstrap_stdErr = se
        self.bootstrap_tTest = np.nan_to_num(self.value / se)
        self.bootstrap_pValue = calcPValue(self.robust_tTest)
        
        
    def __str__(self):
        str = "{:15}: {:.3g}".format(self.name,self.value)
        if self.stdErr is not None:
            str += "[{:.3g} {:.3g} {:.3g}]".format(self.stdErr,self.tTest,self.pValue)
        if self.robust_stdErr is not None:
            str += "[{:.3g} {:.3g} {:.3g}]".format(self.robust_stdErr,self.robust_tTest,self.robust_pValue)
        if self.bootstrap_stdErr is not None:
            str += "[{:.3g} {:.3g} {:.3g}]".format(self.bootstrap_stdErr,self.bootstrap_tTest,self.bootstrap_pValue)
        return str

class rawResults:
    def __init__(self,theModel,betaValues,fgHb,bootstrap=None):
        """ Ctor """

        self.modelName = theModel.modelName
        self.nparam = len(betaValues)
        self.betaValues = betaValues
        self.betaNames = theModel.freeBetaNames
        self.initLogLike = theModel.initLogLike
        self.betas = list()
        for b,n in zip(betaValues,self.betaNames):
            self.betas.append(beta(n,b))
        self.logLike = fgHb[0]
        self.g = fgHb[1]
        self.H = fgHb[2]
        self.bhhh = fgHb[3]
        self.dataname = theModel.database.name
        self.sampleSize = theModel.database.getSampleSize()
        self.numberOfObservations = theModel.database.getNumberOfObservations()
        self.monteCarlo = theModel.monteCarlo
        self.numberOfDraws = theModel.numberOfDraws
        self.excludedData = theModel.database.excludedData
        self.dataProcessingTime = theModel.database.dataProcessingTime
        self.drawsProcessingTime = theModel.drawsProcessingTime
        self.optimizationTime = theModel.optimizationTime
        self.gradientNorm = linalg.norm(self.g)
        self.optimizationMessage = theModel.optimizationMessage
        self.numberOfFunctionEval = theModel.numberOfFunctionEval
        self.numberOfIterations = theModel.numberOfIterations
        self.numberOfThreads = theModel.numberOfThreads
        self.htmlFileName = None
        self.pickleFileName = None
        self.bootstrap = bootstrap
        if bootstrap is not None:
            self.bootstrapTime = theModel.bootstrapTime
    
class bioResults:
    def __init__(self,rawResults=None,pickleFile=None):
        if rawResults is not None:
            self.data = rawResults
            self.dumpData()
        elif pickleFile is not None:
            with open(pickleFile, 'rb') as f:
                self.data = pickle.load(f)
        else:
            raise excep.biogemeError("No data provided.")
            
        self.calculateStats()

    def dumpData(self): 
        self.data.pickleFileName = bf.getNewFileName(self.data.modelName,"pickle")
        with open(self.data.pickleFileName, 'wb') as f:
            pickle.dump(self.data, f)
#        print("Results dumped on file {}".format(pickleFile))
#        print("Can be read using the following statement:")
#        print("import pickle") 
#        print("with open('{}', 'rb') as f:".format(pickleFile))
#        print("    data = pickle.load(f)")
        
    def calculateTest(self,i,j,matrix):
        vi = self.data.betaValues[i]
        vj = self.data.betaValues[j]
        varI = matrix[i,i]
        varJ = matrix[j,j]
        covar = matrix[i,j]
        test = np.nan_to_num((vi - vj) / np.sqrt(varI + varJ - 2.0 * covar))
        return test
    
    def calculateStats(self):
        self.data.likelihoodRatioTest = -2.0 * (self.data.initLogLike - self.data.logLike)
        self.data.rhoSquare = np.nan_to_num(1.0 - self.data.logLike / self.data.initLogLike)
        self.data.rhoBarSquare = np.nan_to_num(1.0 - (self.data.logLike-self.data.nparam) / self.data.initLogLike)
        self.data.akaike = 2.0 * self.data.nparam - 2.0 * self.data.logLike
        self.data.bayesian = - 2.0 * self.data.logLike + self.data.nparam * np.log(self.data.sampleSize) 
        # We calculate the eigenstructure to report in case of singularity
        self.data.eigenValues,self.data.eigenvectors = linalg.eigh(-np.nan_to_num(self.data.H))
        U, self.data.singularValues,V = linalg.svd(-np.nan_to_num(self.data.H))
        # We use the pseudo inverse in case the matrix is singular
        self.data.varCovar = -linalg.pinv(np.nan_to_num(self.data.H))
        for i in range(self.data.nparam):
            self.data.betas[i].setStdErr(np.sqrt(self.data.varCovar[i,i]))

        d = np.diag(self.data.varCovar)
        if (d > 0).all():
            diag = np.diag(np.sqrt(d))
            diagInv = linalg.inv(diag)
            self.data.correlation = diagInv.dot(self.data.varCovar.dot(diagInv))
        else:
            self.data.correlation = np.full_like(self.data.varCovar,np.finfo(float).max)

        
        # Robust estimator
        self.data.robust_varCovar = self.data.varCovar.dot(self.data.bhhh.dot(self.data.varCovar))
        for i in range(self.data.nparam):
            self.data.betas[i].setRobustStdErr(np.sqrt(self.data.robust_varCovar[i,i]))
        rd = np.diag(self.data.robust_varCovar)
        if (rd > 0).all():
            diag = np.diag(np.sqrt(rd))
            diagInv = linalg.inv(diag)
            self.data.robust_correlation = diagInv.dot(self.data.robust_varCovar.dot(diagInv))
        else:
            self.data.robust_correlation = np.full_like(self.data.robust_varCovar,np.finfo(float).max)
            
        # Bootstrap
        if self.data.bootstrap is not None:
            self.data.bootstrap_varCovar = np.cov(self.data.bootstrap,rowvar=False)
            for i in range(self.data.nparam):
                self.data.betas[i].setBootstrapStdErr(np.sqrt(self.data.bootstrap_varCovar[i,i]))
            rd = np.diag(self.data.bootstrap_varCovar)
            if (rd > 0).all():
                diag = np.diag(np.sqrt(rd))
                diagInv = linalg.inv(diag)
                self.data.bootstrap_correlation = diagInv.dot(self.data.bootstrap_varCovar.dot(diagInv))
            else:
                self.data.bootstrap_correlation = np.full_like(self.data.bootstrap_varCovar,np.finfo(float))

        self.data.secondOrderTable = dict()
        for i in range(self.data.nparam):
            for j in range(i):
                t = self.calculateTest(i,j,self.data.varCovar)
                p = calcPValue(t)
                trob = self.calculateTest(i,j,self.data.robust_varCovar)
                prob = calcPValue(trob)
                if self.data.bootstrap is not None:
                    tboot = self.calculateTest(i,j,self.data.bootstrap_varCovar)
                    pboot = calcPValue(tboot)
                name = (self.data.betaNames[i],self.data.betaNames[j])
                if self.data.bootstrap is not None:
                    self.data.secondOrderTable[name] = [self.data.varCovar[i,j],self.data.correlation[i,j],t,p,self.data.robust_varCovar[i,j],self.data.robust_correlation[i,j],trob,prob,self.data.bootstrap_varCovar[i,j],self.data.bootstrap_correlation[i,j],tboot,pboot]
                else:
                    self.data.secondOrderTable[name] = [self.data.varCovar[i,j],self.data.correlation[i,j],t,p,self.data.robust_varCovar[i,j],self.data.robust_correlation[i,j],trob,prob]

        self.data.smallestEigenValue = min(self.data.eigenValues)
        self.data.smallestSingularValue = min(self.data.singularValues)

    def __str__(self):
        r = "\n"
        r += "Results for model ["+self.data.modelName+"]\n"
        if self.data.htmlFileName is not None :
            r += "Output file:\t\t\t{}\n".format(self.data.htmlFileName)
        r += "Nbr of parameters:\t\t{}\n".format(self.data.nparam)
        r += "Sample size:\t\t\t{}\n".format(self.data.sampleSize)
        if self.data.sampleSize != self.data.numberOfObservations:
            r += "Observations:\t\t\t{}\n".format(self.data.numberOfObservations)
        r += "Excluded data:\t\t\t{}\n".format(self.data.excludedData)
        r += "Init log likelihood:\t\t{:.7g}\n".format(self.data.initLogLike)
        r += "Final log likelihood:\t\t{:.7g}\n".format(self.data.logLike)
        r += "Likelihood ratio test:\t\t{:.7g}\n".format(self.data.likelihoodRatioTest)
        r += "Rho square:\t\t\t{:.3g}\n".format(self.data.rhoSquare)
        r += "Rho bar square:\t\t\t{:.3g}\n".format(self.data.rhoBarSquare)
        r += "Akaike Information Criterion:\t{:.7g}\n".format(self.data.akaike)
        r += "Bayesian Information Criterion:\t{:.7g}\n".format(self.data.bayesian)
        r += "Final gradient norm:\t\t{:.7g}\n".format(self.data.gradientNorm)
        r += "\n".join(["{}".format(b) for b in self.data.betas])
        r += "\n"
        for k,v in self.data.secondOrderTable.items():
            r += "{}:\t{:.3g}\t{:.3g}\t{:.3g}\t{:.3g}\t{:.3g}\t{:.3g}\t{:.3g}\t{:.3g}\n".format(k,*v)
        return r

    def getHtml(self):
        now = datetime.datetime.now()
        h = self.getHtmlHeader()
        h += bv.getHtml()
        h += self.getHtmlFooter()
        h += "<p>This file has automatically been generated on {}</p>\n".format(now)
        h += "<p>If you drag this HTML file into the Calc application of <a href='http://www.openoffice.org/' target='_blank'>OpenOffice</a>, or the spreadsheet of <a href='https://www.libreoffice.org/' target='_blank'>LibreOffice</a>, you will be able to perform additional calculations.</p>\n"
        h += "<table>\n"
        h += "<tr class=biostyle><td align=right><strong>Report file</strong>:	</td><td>"+self.data.htmlFileName+"</td></tr>\n"
        h += "<tr class=biostyle><td align=right><strong>Database name</strong>:	</td><td>"+self.data.dataname+"</td></tr>\n"
        h += "</table>\n"

        ### Include here the part on statistics

        h += "<h1>Estimation report</h1>\n"

        h += "<table border='0'>\n"
        h += "<tr class=biostyle><td align=right ><strong>Number of estimated parameters</strong>: </td> <td>{}</td></tr>\n".format(self.data.nparam)
        h += "<tr class=biostyle><td align=right ><strong>Sample size</strong>:</td> <td>{}</td></tr>\n".format(self.data.sampleSize)
        if self.data.sampleSize != self.data.numberOfObservations:
            h += "<tr class=biostyle><td align=right ><strong>Observations</strong>:</td> <td>{}</td></tr>\n".format(self.data.numberOfObservations)
        h += "<tr class=biostyle><td align=right ><strong>Excluded observations</strong>:</td> <td>{}</td></tr>\n".format(self.data.excludedData)
        h += "<tr class=biostyle><td align=right><strong>Init log likelihood</strong>:	</td> <td>{:.7g}</td></tr>\n".format(self.data.initLogLike)
        h += "<tr class=biostyle><td align=right><strong>Final log likelihood</strong>:	</td> <td>{:.7g}</td></tr>\n".format(self.data.logLike)
        h += "<tr class=biostyle><td align=right><strong>Likelihood ratio test for the init. model</strong>:	</td> <td>{:.7g}</td></tr>\n".format(self.data.likelihoodRatioTest)
        h += "<tr class=biostyle><td align=right><strong>Rho-square for the init. model</strong>:	</td> <td>{:.3g}</td></tr>\n".format(self.data.rhoSquare)
        h += "<tr class=biostyle><td align=right><strong>Rho-square-bar for the init. model</strong>:	</td> <td>{:.3g}</td></tr>\n".format(self.data.rhoBarSquare)
        h += "<tr class=biostyle><td align=right><strong>Akaike Information Criterion</strong>:	</td> <td>{:.7g}</td></tr>\n".format(self.data.akaike)
        h += "<tr class=biostyle><td align=right><strong>Bayesian Information Criterion</strong>:	</td> <td>{:.7g}</td></tr>\n".format(self.data.bayesian)
        h += "<tr class=biostyle><td align=right><strong>Final gradient norm</strong>:	</td> <td>{:.4E}</td></tr>\n".format(self.data.gradientNorm)
        h += "<tr class=biostyle><td align=right><strong>Diagnostic</strong>:	</td> <td>{}</td></tr>\n".format(self.data.optimizationMessage)
        h += "<tr class=biostyle><td align=right><strong>Database readings</strong>:	</td> <td>{}</td></tr>\n".format(self.data.numberOfFunctionEval)
        h += "<tr class=biostyle><td align=right><strong>Iterations</strong>:	</td> <td>{}</td></tr>\n".format(self.data.numberOfIterations)
        h += "<tr class=biostyle><td align=right><strong>Data processing time</strong>:	</td> <td>{}</td></tr>\n".format(self.data.dataProcessingTime)
        if self.data.monteCarlo:
            h += "<tr class=biostyle><td align=right><strong>Number of draws</strong>:	</td> <td>{}</td></tr>\n".format(self.data.numberOfDraws)
            h += "<tr class=biostyle><td align=right><strong>Draws generation time</strong>:	</td> <td>{}</td></tr>\n".format(self.data.drawsProcessingTime)
        h += "<tr class=biostyle><td align=right><strong>Optimization time</strong>:	</td> <td>{}</td></tr>\n".format(self.data.optimizationTime)
        if self.data.bootstrap is not None:
            h += "<tr class=biostyle><td align=right><strong>Bootstrapping time</strong>:	</td> <td>{}</td></tr>\n".format(self.data.bootstrapTime)
        h += "<tr class=biostyle><td align=right><strong>Nbr of threads</strong>:	</td> <td>{}</td></tr>\n".format(self.data.numberOfThreads)
        h += "</table>\n"
        h += "<h1>Estimated parameters</h1>\n"
        h += "<p><font size='-1'>Click on the headers of the columns to sort the table  [<a href='http://www.kryogenix.org/code/browser/sorttable/' target='_blank'>Credits</a>]</font></p>\n"
        h += "<table border='1' class='sortable'>\n"
        h += "<tr class=biostyle><th>Name </th><th>Value</th><th>Std err</th><th>t-test</th><th>p-value</th><th>Robust Std err</th><th>Robust t-test</th><th>p-value</th>"
        if self.data.bootstrap is not None:
            h += "<th>Bootstrap[{}] Std err</th><th>Bootstrap t-test</th><th>p-value</th>".format(len(self.data.bootstrap))
        h += "</tr>\n"
        for b in self.data.betas:
            h += "<tr class=biostyle><td>{}</td><td>{:.3g}</td><td>{:.3g}</td><td>{:.3g}</td><td>{:.3g}</td><td>{:.3g}</td><td>{:.3g}</td><td>{:.3g}</td>".format(b.name,b.value,b.stdErr,b.tTest,b.pValue,b.robust_stdErr,b.robust_tTest,b.robust_pValue)
            if self.data.bootstrap is not None:
                h += "<td>{:.3g}</td><td>{:.3g}</td><td>{:.3g}</td>".format(b.bootstrap_stdErr,b.bootstrap_tTest,b.bootstrap_pValue)
            
            h += "</tr>\n"

        h += "</table>\n"
        h += "<h2>Correlation of coefficients</h2>\n"
        h += "<p><font size='-1'>Click on the headers of the columns to sort the table [<a href='http://www.kryogenix.org/code/browser/sorttable/' target='_blank'>Credits</a>]</font></p>\n"
        h += "<table border='1' class='sortable'>\n"
        h += "<tr class=biostyle><th>Coefficient1</th><th>Coefficient2</th><th>Covariance</th><th>Correlation</th><th>t-test</th><th>p-value</th><th>Rob. cov.</th><th>Rob. corr.</th><th>Rob. t-test</th><th>p-value</th>"
        if self.data.bootstrap is not None:
            h += "<th>Boot. cov.</th><th>Boot. corr.</th><th>Boot. t-test</th><th>p-value</th>"
        h += "</tr>\n" 
        for k,v in self.data.secondOrderTable.items():
            if self.data.bootstrap is not None:
                h += "<tr class=biostyle><td>{}</td><td>{}</td><td>{:.3g}</td><td>{:.3g}</td><td>{:.3g}</td><td>{:.3g}</td><td>{:.3g}</td><td>{:.3g}</td><td>{:.3g}</td><td>{:.3g}</td><td>{:.3g}</td><td>{:.3g}</td><td>{:.3g}</td><td>{:.3g}</td></tr>\n".format(k[0],k[1],*v)
            else:
                h += "<tr class=biostyle><td>{}</td><td>{}</td><td>{:.3g}</td><td>{:.3g}</td><td>{:.3g}</td><td>{:.3g}</td><td>{:.3g}</td><td>{:.3g}</td><td>{:.3g}</td><td>{:.3g}</td></tr>\n".format(k[0],k[1],*v)
        h += "</table>\n"
        
        h += "<p>Smallest eigenvalue: {:.6g}</p>\n".format(self.data.smallestEigenValue)
        h += "<p>Smallest singular value: {:.6g}</p>\n".format(self.data.smallestSingularValue)
        return h

    def getBetaValues(self):
        values = dict()
        for b in self.data.betas:
            values[b.name] = b.value
        return values

    def getRobustVarCovar(self):
        names = [b.name for b in self.data.betas]
        vc = pd.DataFrame(index=names,columns=names)
        for i in range(len(self.data.betas)):
            for j in range(len(self.data.betas)):
                vc.at[self.data.betas[i].name, self.data.betas[j].name] = self.data.robust_varCovar[i,j]
        return vc   
    
    def writeHtml(self):
        self.data.htmlFileName = bf.getNewFileName(self.data.modelName,"html")
        f = open(self.data.htmlFileName,"w")
        f.write(self.getHtml())
        f.close()
    
    def getHtmlHeader(self):
        h = ""
        h += "<html>"
        h += "<head>"
        h += "<script src='http://transp-or.epfl.ch/biogeme/sorttable.js'></script>"
        h += "<meta http-equiv='Content-Type' content='text/html; charset=utf-8' />"
        h += "<title>"+self.data.modelName+" - Report from biogeme "+bv.getVersion()+" ["+bv.versionDate+"]</title>"
        h += "<meta name='keywords' content='biogeme, discrete choice, random utility'>"
        h += "<meta name='description' content='Report from biogeme "+bv.getVersion()+" ["+bv.versionDate+"]'>"
        h += "<meta name='author' content='"+bv.author+"'>"
        h += "<style type=text/css>"
        h += ".biostyle"
        h += "	{font-size:10.0pt;"
        h += "	font-weight:400;"
        h += "	font-style:normal;"
        h += "	font-family:Courier;}"
        h += ".boundstyle"
        h += "	{font-size:10.0pt;"
        h += "	font-weight:400;"
        h += "	font-style:normal;"
        h += "	font-family:Courier;"
        h += "        color:red}"
        h += "</style>"
        h += "</head>"
        h += "<body bgcolor='#ffffff'>"
        return h

    def getHtmlFooter(self):
        return "</html>"
        
    def getBetasForSensitivityAnalysis(self,size=100):
        simulatedBetas = np.random.multivariate_normal(self.data.betaValues, self.data.robust_varCovar, size, check_valid='warn')
        return simulatedBetas
        
    
