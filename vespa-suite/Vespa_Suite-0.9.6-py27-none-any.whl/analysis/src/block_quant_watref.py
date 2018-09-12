# Python modules
from __future__ import division
import os

# 3rd party modules
import numpy as np
import xml.etree.cElementTree as ElementTree

# Our modules
import constants
import block_quant_identity
import chain_quant_watref

import vespa.common.util.xml_ as util_xml

from vespa.common.constants import Deflate
from constants import FitMacromoleculeMethod



# The HTML generated by this code contains a conditional comment for IE users.
# _IE_INCAPABLE_MSG is the content for that comment.
# We use the data URI scheme to display our image, and IE < 9 does support it.
# The conditionalcomment is a valid HTML comment. It's ignored by browsers
# except IE which is documented to look for HTML comments containing certain key
# strings. This allows us to display slightly different content to those who
# can't see the image.
# ref: http://msdn.microsoft.com/en-us/library/ms537512%28v=vs.85%29.aspx
# reF: http://www.quirksmode.org/css/condcom.html
_IE_INCAPABLE_MSG = """[if lt IE 9]>
<p><strong>Sorry, Internet Explorer 6, 7, and 8 can't display the 
image below. All other major browsers (IE 9, 
<a href="http://www.mozilla.org/">Firefox</a>, 
<a href="http://www.google.com/chrome/">Chrome</a>,
<a href="http://www.opera.com/">Opera</a>, and
<a href="http://www.apple.com/safari/">Safari</a>) 
can display it.</strong>
</p>
<![endif]
"""


# _CSS is the style sheet for the HTML that this code builds. Note that 
# wxPython's HTML control doesn't understand CSS. This is only for printing
# from the browser.
_CSS = """
    @page { margin: 20mm;          
            size: landscape;  
          }

    @media print {
        /* a4 = 210 x 297mm, US letter = 216 x 280mm. Two 20mm margins plus
        two 110mm block elements = 40 + 220 = 260mm which fits with room to
        spare on both paper sizes as long as the 'landscape' directive is
        respected.
        */
        div#table { width: 110mm; }
        div#img   { width: 110mm; }
    }
"""


# The 3 functions below are used for building HTML
def _format_column(column, places=4):
    # Given a column from the table, converts it to a nicely formatted string
    # and returns it. The column can be float, int, bool or a string. Strings
    # are returned untouched.
    if isinstance(column, float):
        column = ("%%.%dg" % places) % column
    elif isinstance(column, int) or isinstance(column, bool):
        column = str(column)
    #else:
        # It's a string, leave it alone.

    return column


def _get_max_width(table, index):
    """Get the maximum width of the given column index"""
    return max([len(_format_column(row[index])) for row in table])    


def _pretty_space_table(table, places):
    """Returns a table of data, padded for alignment
    @param table: The table to print. A list of lists.
    Each row must have the same number of columns. 
    """
    col_paddings = []

    for i in range(len(table[0])):
        col_paddings.append(_get_max_width(table, i))

    lines = []
    for row in table:
        # left col
        line = row[0].center(col_paddings[0] + 2)
        # rest of the cols
        for i in range(1, len(row)):
            col = _format_column(row[i], places).center(col_paddings[i] + 2)
            line += col
        lines.append(line)
    
    return lines





class _Settings(object):
    """
    This object contains the parameter settings (inputs) used to perform the
    processing being done in this processing block. These are stored separately
    to delineate inputs/outputs and to simplify load/save of preset values.

    In here we also package all the functionality needed to save and recall
    these values to/from an XML node.

    """
    # The XML_VERSION enables us to change the XML output format in the future
    XML_VERSION = "1.0.0"

    def __init__(self, attributes=None):
        """
        Most of these values appear in a GUI when the app first starts.

        Watref Processing Parameters
        -----------------------------------------

        xxx - xxxxxxxxxxxxxxxx
        xxx - xxxxxxxxxxxxxxxx
        xxx - xxxxxxxxxxxxxxxx
        xxx - xxxxxxxxxxxxxxxx
        xxx - xxxxxxxxxxxxxxxx
        
        GM, WM, CSF percentages Ernst et.al. 1993 Absolute quantitation of
        water and metabolites in the human brain. I. Compartments and water.
        J Magn Reson B 102:1-8

        """
        #------------------------------------------------------------
        # Watref Processing Variables
        #------------------------------------------------------------

        self.watref_dataset_id              = ''
        self.watref_filename                = ''
        self.sequence_te                    = 30.0
        self.water_averages                 = 1
        self.metabolite_averages            = 1
        self.apply_water_correction         = True
        self.tissue_content_gm              = 60.0
        self.tissue_content_wm              = 40.0
        self.tissue_content_csf             = 0.0
        self.water_content_gm               = 0.78
        self.water_content_wm               = 0.65
        self.water_content_csf              = 0.97
        self.water_t2_gm                    = 110.0
        self.water_t2_wm                    = 80.0
        self.water_t2_csf                   = 350.0
        self.apply_metabolite_correction    = True
        self.metabolite_t2                  = 160.0

        self.watref_dataset                 = None

        if attributes is not None:
            self.inflate(attributes)


    ##### Standard Methods and Properties #####################################

    def __str__(self):
        return self.__unicode__().encode("utf-8")


    def __unicode__(self):
        lines = [ ]
        lines.append("--- Block Watref Settings ---")
        lines.append("watref_dataset_id           : " + unicode(self.watref_dataset_id))
        lines.append("watref_filename             : " + unicode(self.watref_filename))
        lines.append("sequence_te                 : " + unicode(self.sequence_te))
        lines.append("water_averages              : " + unicode(self.water_averages))
        lines.append("metabolite_averages         : " + unicode(self.metabolite_averages))
        lines.append("apply_water_correction      : " + unicode(self.water_t2_csf))
        lines.append("tissue_content_gm           : " + unicode(self.tissue_content_gm))
        lines.append("tissue_content_wm           : " + unicode(self.tissue_content_wm))
        lines.append("tissue_content_csf          : " + unicode(self.tissue_content_csf))
        lines.append("water_content_gm            : " + unicode(self.water_content_gm))
        lines.append("water_content_wm            : " + unicode(self.water_content_wm))
        lines.append("water_content_csf           : " + unicode(self.water_content_csf))
        lines.append("water_t2_gm                 : " + unicode(self.water_t2_gm))
        lines.append("water_t2_wm                 : " + unicode(self.water_t2_wm))
        lines.append("water_t2_csf                : " + unicode(self.water_t2_csf))
        lines.append("apply_metabolite_correction : " + unicode(self.water_t2_csf))
        lines.append("metabolite_t2               : " + unicode(self.metabolite_t2))

        # __unicode__() must return a Unicode object. In practice the code
        # above always generates Unicode, but we ensure it here.
        return u'\n'.join(lines)


    def deflate(self, flavor=Deflate.ETREE):
        if flavor == Deflate.ETREE:
            e = ElementTree.Element("settings", {"version" : self.XML_VERSION})

            util_xml.TextSubElement(e, "watref_filename",             self.watref_filename)
            util_xml.TextSubElement(e, "water_averages",              self.water_averages)
            util_xml.TextSubElement(e, "sequence_te",                 self.sequence_te)
            util_xml.TextSubElement(e, "apply_water_correction",      self.apply_water_correction)
            util_xml.TextSubElement(e, "metabolite_averages",         self.metabolite_averages)
            util_xml.TextSubElement(e, "tissue_content_gm",           self.tissue_content_gm)
            util_xml.TextSubElement(e, "tissue_content_wm",           self.tissue_content_wm)
            util_xml.TextSubElement(e, "tissue_content_csf",          self.tissue_content_csf)
            util_xml.TextSubElement(e, "water_content_gm",            self.water_content_gm)
            util_xml.TextSubElement(e, "water_content_wm",            self.water_content_wm)
            util_xml.TextSubElement(e, "water_content_csf",           self.water_content_csf)
            util_xml.TextSubElement(e, "water_t2_gm",                 self.water_t2_gm)
            util_xml.TextSubElement(e, "water_t2_wm",                 self.water_t2_wm)
            util_xml.TextSubElement(e, "water_t2_csf",                self.water_t2_csf)
            util_xml.TextSubElement(e, "apply_metabolite_correction", self.apply_metabolite_correction)
            util_xml.TextSubElement(e, "metabolite_t2",               self.metabolite_t2)
            
            # In the next line, we *have* to save the uuid values from the
            # actual object rather than from the attribute above, in
            # order for the associated dataset uuid to reflect the new id
            # that is given in the top level dataset. Associated datasets are
            # given new temporary uuid values so that if the main dataset is
            # saved and immediately loaded back in, we do not get collisions
            # between the newly opened datasets and already existing ones.
            if self.watref_dataset is not None:
                util_xml.TextSubElement(e, "watref_dataset_id",        self.watref_dataset.id)

            return e

        elif flavor == Deflate.DICTIONARY:
            return self.__dict__.copy()


    def inflate(self, source):
        if hasattr(source, "makeelement"):
            # Quacks like an ElementTree.Element

            # in some cases below, we need to check if a value returns None
            # because in mrs_dataset versions prior to 1.1.0, HLSVD was its own
            # tab not a sub-tab of spectral, thus some of these attributes were
            # not present in the settings

            for name in ("apply_water_correction",
                         "apply_metabolite_correction" ):
                val = source.findtext(name)
                if val:
                    setattr(self, name, util_xml.BOOLEANS[val])

            for name in ("watref_filename",
                         "watref_dataset_id", ):
                val = source.findtext(name)
                if val is not None: setattr(self, name, val)

            for name in ("sequence_te",
                         "tissue_content_gm",
                         "tissue_content_wm",
                         "tissue_content_csf",
                         "water_content_gm",
                         "water_content_wm",
                         "water_content_csf",
                         "water_t2_gm",
                         "water_t2_wm",
                         "water_t2_csf",
                         "metabolite_t2",
                        ):
                val = source.findtext(name)
                if val:  setattr(self, name, float(val))

            for name in ("water_averages",
                         "metabolite_averages", 
                        ):
                val = source.findtext(name)
                if val:  setattr(self, name, int(val))

        elif hasattr(source, "keys"):
            # Quacks like a dict
            for key in source.keys():
                if hasattr(self, key):
                    setattr(self, key, source[key])




class BlockQuantWatref(block_quant_identity.BlockQuantIdentity):
    """
    This is a building block object that can be used to create a list of
    processing blocks.

    This object represents the settings and results involved in processing
    data from the Time Domain to the Frequency Domain (TDFD) for the spectral
    dimension.

    In here we also package all the functionality needed to save and recall
    these values to/from an XML node.

    """
    # The XML_VERSION enables us to change the XML output format in the future
    XML_VERSION = "1.0.0"

    def __init__(self, attributes=None):
        """

        General Parameters
        -----------------------------------------

        id          A permanent, unique identifying string for this
                    object. Typically serves as a "source_id" for
                    some other object. It is part of the provenance
                    for this processing functor chain

        source_id   The unique identifier used to find the input data
                    for this object. It may refer to one whole object
                    that has only one result, OR it could refer to s
                    single results inside an object that has multiple
                    results.

        Quant Processing Parameters
        -----------------------------------------

        set                 Settings object


        """
        block_quant_identity.BlockQuantIdentity.__init__(self, attributes)

        #----------------------------------------
        # processing parameters
        self.set = _Settings()

        #----------------------------------------
        # results storage
        self.watref_results = None


        if attributes is not None:
            self.inflate(attributes)

        self.chain = None


    ##### Standard Methods and Properties #####################################

    def __str__(self):
        return self.__unicode__().encode("utf-8")


    def __unicode__(self):

        lines = [ ]
        lines.append("--------- BlockQuantWatref -------------\n")
        lines =  u'\n'.join(lines)

        lines = lines + self.set.__unicode__()

        return lines


    def create_chain(self, dataset):
        self.chain = chain_quant_watref.ChainQuantWatref(dataset, self)


    def check_parameter_dimensions(self, dataset):
        """
        Checks the "nparam" dimension in the results to see if the number of 
        parameters in the model has changed. Only resets results if this
        dimension has changed.
        
        """
        fit = dataset.blocks['fit']
        nparam = fit.calc_nparameters()
            
        if self.watref_results.shape[0] != nparam:
            self._reset_dimensional_data(dataset)



    def _reset_dimensional_data(self, dataset):
        """
        Resets (to zero) and resizes dimensionally-dependent data
        
        watref_results  - fit parameters from optimization
        
        """
        dims = dataset.spectral_dims
        fit  = dataset.blocks['fit']
        
        nparam = fit.calc_nparameters()
        
        if self.watref_results is None:
        
            self.watref_results = np.zeros((nparam, dims[1], dims[2], dims[3]))      
        
        else:
            param_dims = list(dims)
            param_dims[0] = nparam

            # maintain results if no dimension has changed
            if self.watref_results.shape[::-1] != param_dims:
                self.watref_results = np.zeros((nparam, dims[1], dims[2], dims[3]))      


    def get_associated_datasets(self, is_main_dataset=True):
        """
        Returns a list of datasets associated with this object

        The 'is_main_dataset' flag allows the method to know if it is the top
        level dataset gathering associated datasets, or some dataset that is
        only associated with the top dataset. This is used to stop circular
        logic conditions where one or more datasets refer to each other.

        """
        # Call base class first
        datasets = block_quant_identity.BlockQuantIdentity.get_associated_datasets(self, is_main_dataset)

        if self.set.watref_dataset:
            # watref may have some ECC or CoilCombine processing that uses 
            # other datasets, so we need to return these as well as itself
            datasets += self.set.watref_dataset.get_associated_datasets(is_main_dataset=False)
            datasets += [self.set.watref_dataset,]
        else:
            return []
        
        return datasets


    def set_associated_datasets(self, datasets):
        for dataset in datasets:
            if dataset.id == self.set.watref_dataset_id:
                self.set.watref_dataset = dataset


    def attach_dataset_water_quant(self, dataset):
        ''' attaches the provided dataset as the input to water quant algorithm'''
        self.set.watref_dataset    = dataset
        self.set.watref_dataset_id = dataset.id        


    def deflate(self, flavor=Deflate.ETREE):
        if flavor == Deflate.ETREE:
            e = ElementTree.Element("block_quant_watref",
                                      { "id" : self.id,
                                        "version" : self.XML_VERSION})

            util_xml.TextSubElement(e, "behave_as_preset", self.behave_as_preset)

            e.append(self.set.deflate())

            if not self.behave_as_preset:
                if self.watref_results is not None:
                    e.append(util_xml.numpy_array_to_element(self.watref_results,'watref_results'))

            return e

        elif flavor == Deflate.DICTIONARY:
            return self.__dict__.copy()


    def inflate(self, source):
        if hasattr(source, "makeelement"):
            # Quacks like an ElementTree.Element

            self.id = source.get("id")

            val = source.findtext("behave_as_preset")   # default is False
            if val is not None:
                self.behave_as_preset = util_xml.BOOLEANS[val]

            self.set = util_xml.find_settings(source, "")
            self.set = _Settings(self.set)

            if not self.behave_as_preset:

                # Explicit tests for None necessary in the code below. See:
                # http://scion.duhs.duke.edu/vespa/project/ticket/35
                temp = source.find("watref_results")
                if temp is not None:
                    self.watref_results = util_xml.element_to_numpy_array(temp)

        elif hasattr(source, "keys"):
            # Quacks like a dict
            for key in source.keys():
                if hasattr(self, key):
                    setattr(self, key, source[key])


    def results_as_csv(self, voxel, fit, lw=0.0, lwmin=0.0, lwmax=0.0, source="", dsetname=""):
        """
        Given a voxel, linewidth params, and a data source (often a filename), 
        returns CSV-formatted (comma separated variables)string containing both
        the voxel fitting results and header string descriptions for each 
        column.

        """
        hdr = []
        val = []

        dsetname = dsetname.replace(",","_") # some users have commas in filenames    
        path, fname = os.path.split(dsetname)

        hdr.append('Dataset Name')        
        val.append(fname+", ")
        
        nmet = len(fit.set.prior_list)
        
        names = fit.set.prior_list
        res   = self.watref_results[:,voxel[0],voxel[1],voxel[2]]
        crao  = fit.cramer_rao[ :,voxel[0],voxel[1],voxel[2]]

        if len(crao) != len(res):
            crao = res * 0

        if fit.set.macromol_model == FitMacromoleculeMethod.SINGLE_BASIS_DATASET:
            hdr.append('MMBL')
            val.append(str(res[nmet*2+4])+", 0.0")

        for i, item in enumerate(names):
            hdr.append(item)        
            val.append(str(res[i]*1e6)+","+str(crao[i]))

        hdr.append('Linewidth ')        
        val.append(str(lw)+", 0.0")

        return val, hdr


    def results_as_csv_orig(self, voxel, fit, lw=0.0, lwmin=0.0, lwmax=0.0, source="", dsetname=""):
        """
        Given a voxel, linewidth params, and a data source (often a filename), 
        returns CSV-formatted (comma separated variables)string containing both
        the voxel fitting results and header string descriptions for each 
        column.

        """
        hdr = []
        val = []

        hdr.append('Filename')   
        source = source.replace(",","_")     # some users have commas in filenames 
        val.append(source)

        hdr.append('Dataset Name')        
        dsetname = dsetname.replace(",","_") # some users have commas in filenames    
        val.append(dsetname)
        
        hdr.append('Voxel')
        val.append(str(voxel[0])+' '+str(voxel[1])+' '+str(voxel[2]))
        
        nmet = len(fit.set.prior_list)
        
        names = fit.set.prior_list
        res   = self.watref_results[:,voxel[0],voxel[1],voxel[2]]
        crao  = fit.cramer_rao[ :,voxel[0],voxel[1],voxel[2]]
        conf  = fit.confidence[ :,voxel[0],voxel[1],voxel[2]]
        stats = fit.fit_stats[  :,voxel[0],voxel[1],voxel[2]]
        # both cramer-rao and confidence intervals may be off/on
        if len(crao) != len(res):
            crao = res * 0
        if len(conf) != len(res):
            conf = res * 0

        for i, item in enumerate(names):
            hdr.append('Area '+item)        
            hdr.append('CrRao[%]')        
            hdr.append('CnfInt[%]')        
            val.append(str(res[i]))
            val.append(str(crao[i]))
            val.append(str(conf[i]))

        for i,item in enumerate(names):
            hdr.append('PPM '+item)        
            hdr.append('CrRao[%]')        
            hdr.append('CnfInt[%]')        
            val.append(str(res[i+nmet]))
            val.append(str(crao[i+nmet]))
            val.append(str(conf[i+nmet]))

        hdr.append('Ta ')        
        hdr.append('CrRao[%]')        
        hdr.append('CnfInt[%]')        
        val.append(str(res[nmet*2+0]))
        val.append(str(crao[nmet*2+0]))
        val.append(str(conf[nmet*2+0]))

        hdr.append('Tb ')        
        hdr.append('CrRao[%]')        
        hdr.append('CnfInt[%]')        
        val.append(str(res[nmet*2+1]))
        val.append(str(crao[nmet*2+1]))
        val.append(str(conf[nmet*2+1]))

        hdr.append('Phase0 ')        
        hdr.append('CrRao[%]')        
        hdr.append('CnfInt[%]')        
        val.append(str(res[nmet*2+2]))
        val.append(str(crao[nmet*2+2]))
        val.append(str(conf[nmet*2+2]))

        hdr.append('Phase1 ')        
        hdr.append('CrRao[%]')        
        hdr.append('CnfInt[%]')        
        val.append(str(res[nmet*2+3]))
        val.append(str(crao[nmet*2+3]))
        val.append(str(conf[nmet*2+3]))

        hdr.append('Linewidth ')        
        hdr.append('Max LW')        
        hdr.append('Min LW')        
        val.append(str(lw))
        val.append(str(lwmax))
        val.append(str(lwmin))

        hdr.append('ChiSquare ')        
        val.append(str(stats[0]))

        hdr.append('WtChiSquare ')        
        val.append(str(stats[1]))

        hdr.append('Math Finite Error ')        
        matherr = str(stats[2] != 0)
        val.append(str(matherr))

        return val, hdr



    def results_as_html(self, voxel, fit, lw=0.0, lwmin=0.0, lwmax=0.0, 
                        data_source="", image=None):
        """
        Given a voxel, linewidth params, and a data source (often a filename), 
        returns HTML-formatted results for that voxel. The HTML is appropriate 
        for the wx.Html control (which understand limited HTML) as well as for
        writing to a file.

        If the image param is populated, it should be a tuple of 
        (mime_type, image_data). The former should be a string like "image/png".
        The latter should be base64-encoded image data.
        """
        
        # First we assemble the data we need.
        nmet = len(fit.set.prior_list)
        
        names = fit.set.prior_list
        res   = self.watref_results[:,voxel[0],voxel[1],voxel[2]]
        crao  = fit.cramer_rao[:,voxel[0],voxel[1],voxel[2]]
        conf  = fit.confidence[:,voxel[0],voxel[1],voxel[2]]
        stats = fit.fit_stats[:,voxel[0],voxel[1],voxel[2]]
        # both cramer-rao and confidence intervals may be off/on
        if len(crao) != len(res):
            crao = res * 0
        if len(conf) != len(res):
            conf = res * 0

        table1 = [['Area Results', 'Conc [mM]', ' CrRao[%]', ' CnfInt[%]']]
        for i, item in enumerate(names):
            table1.append([item, res[i], crao[i], conf[i]])

        if fit.set.macromol_model == FitMacromoleculeMethod.SINGLE_BASIS_DATASET:
            table1.append(['MMol', res[nmet*2+4], 0.0, 0.0])
            
        table1 = _pretty_space_table(table1, places=4)

        table2 = [['PPM Results', 'PPM', ' CrRao[ppm]', ' CnfInt[ppm]']]
        for i,item in enumerate(names):
            table2.append([item, res[i+nmet], crao[i+nmet], conf[i+nmet]])

        if fit.set.macromol_model == FitMacromoleculeMethod.SINGLE_BASIS_DATASET:
            table2.append(['MMol', res[nmet*2+5], 0.0, 0.0])

        table2 = _pretty_space_table(table2, places=4)

        table3 =     [['Global Results', 'Value', ' CrRao[delta]', ' CnfInt[%]']]
        table3.append(['Ta',     res[nmet*2+0], crao[nmet*2+0], conf[nmet*2+0] ])
        table3.append(['Tb',     res[nmet*2+1], crao[nmet*2+1], conf[nmet*2+1] ])
        table3.append(['Phase0', res[nmet*2+2], crao[nmet*2+2], conf[nmet*2+2] ])
        table3.append(['Phase1', res[nmet*2+3], crao[nmet*2+3], conf[nmet*2+3] ])
        table3 = _pretty_space_table(table3, places=5)
        
        table4 = [['Calculation Results', ' Value', '  Max LW', '  Min LW']]
        table4.append(['Linewidth', lw, lwmax, lwmin])
        table4.append(['ChiSquare', stats[0], ' ', ' '])
        table4.append(['Weighted ChiSquare', stats[1], ' ', ' '])
        matherr = str(stats[2] != 0)
        table4.append(['Math Finite Error', matherr, ' ', ' '])
        table4 = _pretty_space_table(table4, places=5)

        # Now that the data is assembled, we HTML-ify it.
        html = ElementTree.Element("html")
        head = ElementTree.SubElement(html, "head")
        style = util_xml.TextSubElement(head, "style", _CSS)
        style.set("type", "text/css")

        body = ElementTree.SubElement(html, "body")
        
        util_xml.TextSubElement(body, "h2", "Analysis Results - Water Reference Quantitation")

        e_div = ElementTree.SubElement(body, "div")

        if data_source:
            e_tt = util_xml.TextSubElement(e_div, "tt", "Data Source: ")
            util_xml.TextSubElement(e_tt, "small", data_source)
            ElementTree.SubElement(e_div, "br")
            
        voxel = [x + 1 for x in voxel]
        util_xml.TextSubElement(e_div, "tt", 'Voxel: (%d,%d,%d)' % tuple(voxel))

        if image:
            # If there's image data, we assume that this will be written to 
            # a file for display in a proper browser, so we can use slightly
            # fancier HTML.
            mime_type, image_data = image

            e_div = ElementTree.SubElement(body, "div", 
                                           { "id" : "image",
                                             "style" : "float: right; width: 50%",
                                           }
                                          )

            e_div.append(ElementTree.Comment(_IE_INCAPABLE_MSG))

            # In order to keep the HTML + image in one file, we use the
            # little-known "data" scheme.
            # ref: http://en.wikipedia.org/wiki/Data_URI_scheme
            src = "data:%s;base64,%s" % (mime_type, image_data)

            ElementTree.SubElement(e_div, "img", 
                                           {"style" : "width: 90%",
                                            "src" : src
                                            })


        e_div = ElementTree.SubElement(body, "div", {"id" : "table"})

        tables = (table1, table2, table3, table4)

        for table in tables:
            title = table[0]
            e_pre = ElementTree.SubElement(e_div, "pre")
            e_u = ElementTree.SubElement(e_pre, "u")
            util_xml.TextSubElement(e_u, "b", title)
            e = util_xml.TextSubElement(e_div, "pre", '\n'.join(table[1:]))
            
        # Keep in mind that HTML is whitespace sensitive, and if you call 
        # util_xml.indent() on the HTML, it will change the formatting.

        return ElementTree.tostring(html)


######################    Private methods







#--------------------------------------------------------------------
# test code

def _test():

    pass


if __name__ == '__main__':
    _test()


