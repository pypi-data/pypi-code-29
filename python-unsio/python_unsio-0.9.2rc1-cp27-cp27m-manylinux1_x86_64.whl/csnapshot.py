#!/usr/bin/env python
from __future__ import print_function

# from py_unstools import *         # import py_unstools package
import sys
import unsio
try:
    from uns_simu import *
    from cfalcon import *
    from ccod import *
except:
    print("Unable to import [uns_projects modules]....", file=sys.stderr)
import numpy as np
#from IPython import embed

#
# class CSsnapshot
#


class CSnapshot:
    """Operations on UNS snapshots"""
    __uns = None
    __verbose = False
    __float32 = True
    __loaded = False
    __analysis = None
    simname = None
    select = None
#
# constructor
#

    def __init__(self, simname, select="all", times="all", float32=True, verbose=False, verbose_debug=False):
        self.__verbose = verbose
        self.simname = simname
        self.select = select
        self.__vdebug = verbose_debug
        if self.__vdebug:
            print(">>", float32)
        if simname is not None:
            if float32:
                if self.__vdebug:
                    print("32 bits", simname, select, times,
                          verbose, type(simname), type(select))
                self.__uns = unsio.CunsIn(simname, select, times, verbose)
            else:
                if self.__vdebug:
                    print("64 bits", simname, select, times, verbose)
                self.__uns = unsio.CunsInD(simname, select, times, verbose)
            if not self.__uns.isValid():
                raise RuntimeError("UNS not valid")
        else:
            None

    def debugOn(self):
        self.__vdebug = True
#
# nextFrame
#

    def nextFrame(self, bits=""):
        """
        Load the next snapshot. Data retreival depend from bits (array selected) and
        components selected during instanciation

        Argument :
        for bits explanation, please visit :
        https://projets.lam.fr/projects/unsio/wiki/UnsioVariablesUtilisation#How-to-select-data-at-loading

        Return :
        1 if success, 0 otherwise

        """
        if not self.__uns.isValid():
            raise RuntimeError("UNS not valid")
        else:
            ok = self.__uns.nextFrame(bits)
            if ok:
                self.__loaded = True
            return ok
#
# close
#

    def close(self):
        if not self.__uns.isValid():
            raise RuntimeError("UNS not valid")
        self.__uns.close()
#
# kill
#

    def kill(self):
        if not self.__uns.isValid():
            raise RuntimeError("UNS not valid")
        self.close()
#
# getInterfaceType
#

    def getInterfaceType(self):
        """
        return uns snapshot's Interface type
        """
        if not self.__uns.isValid():
            raise RuntimeError("UNS not valid")
        return self.__uns.getInterfaceType()
#
# getFileStructure
#

    def getFileStructure(self):
        """
        return uns snapshot's File structure
        """
        if not self.__uns.isValid():
            raise RuntimeError("UNS not valid")
        return self.__uns.getFileStructure()
#
# getFileName
#

    def getFileName(self):
        """
        return uns snapshot's File name
        """
        if not self.__uns.isValid():
            raise RuntimeError("UNS not valid")
        return self.__uns.getFileName()
#
# getData
#

    def getData(self, select, tag=None, data_type=np.float32):
        """
        General method to get Data from uns snapshot

        Argument:
        - select : component or list of components (ex: gas or gas,stars)
        - tag    : pos,vel,mass,rho...etc see https://projets.lam.fr/projects/unsio/wiki/GetDataDescription

        IMPORTANT : if 'tag' is None, then 'select' is treated as 'tag' (see above)

        Return :
            status,numpy_array       (if tag is not None)
            status,value             (if tag is None)
            in both case, status=1 if success, 0 otherwise
        """

        if not self.__uns.isValid():
            raise RuntimeError("UNS not valid")
        if not self.__loaded:
            raise RuntimeError("Snapshot not loaded")

        status = 1
        ret_data = np.zeros(0, dtype=data_type)  # initalyse an empty array
        for comp in select.split(","):
            if self.__vdebug:
                print ("comp :", comp)
            ok, type, data = self.__getData(comp, tag, data_type)
            if (ok):
                if type == 2:  # array
                    ret_data = np.append(ret_data, data)
                else:
                    ret_data = data[0]
            else:
                status = 0  # one component missing
            if self.__vdebug:
                print ("ok=", ok, " data=", data.size,
                       " ret_data=", ret_data.size)
        return status, ret_data
#
# __getData
#

    def __getData(self, comp_value, tag=None, data_type=np.float32):
        if self.__vdebug:
            print ("array=", tag, data_type)
        if tag is None:  # only one value
            tab_value_F = ["time"]
            tab_value_I = ["nbody", "nsel"]
            ok = 0
            ret_data = np.zeros(1, dtype=data_type)
            data = 0
            # proceed __uns.getValue()
            if tab_value_F.count(comp_value) > 0:
                ok, ret_data[0] = self.__uns.getValueF(comp_value)
            else:
                if tab_value_I.count(comp_value) > 0:
                    ok, ret_data[0] = self.__uns.getValueI(comp_value)
            # ret_data[0]=data
            if self.__vdebug:
                print ("ok,data", ok, data)
            return ok, 1, ret_data
        else:
            if tag != "id":
                ok, data = self.__uns.getArrayF(comp_value, tag)
            else:
                ok, data = self.__uns.getArrayI(comp_value, tag)
            return ok, 2, data
#
# getMaxRadius
#

    def getMaxRadius(self, select, percen=100., x=True, y=True, z=True, com=True, bins=10000):
        """
        Compute radius where percen% of the particles belong

        Return :
        status,radius (status=0 if something goes wrong)


        Arguments:
        select    : selected component
        percen    : keep percen% particles
        x         : 1st dimension ?
        y         : 2nd dimension ?
        z         : 3rd dimension ?
        com       : center on mass ?
        bins      : number of bins to build histogram

        """
        if not self.__uns.isValid():
            raise RuntimeError("UNS not valid")

        radius = -1
        ok, pos = self.getData(select, "pos")  # get pos
        if pos.size > 0:
            if com:  # resquest com
                ok, mass = self.getData(select, "mass")  # get mass
                if not ok:  # no mass
                    mass = np.ones(pos.size/3)  # fake mass
                cxv = self.center(pos, None, mass, True)  # centering
            # reshape pos 1d array to 2d array [nbody,3]
            pos2d = np.reshape(pos, (-1, 3))
            xx = 0.
            if x:
                xx = pos2d[:, 0]
            yy = 0.
            if y:
                yy = pos2d[:, 1]
            zz = 0.
            if z:
                zz = pos2d[:, 2]
            # compute radius
            r2 = np.sqrt(xx**2+yy**2+zz**2)
            # compute histogram
            hist, bin_edges = np.histogram(r2, bins=bins)
            status = 1
            radius = bin_edges[(hist.cumsum()*100./r2.size) <= percen][-1]
        else:
            status = 0

        return status, radius
#
# shift
#

    def shift(self, data, center):
        """
        shift data array to center

        Return :
        Center coordinates

        Arguments:
        data        : one dimension numpy array ( nbody x 3 ), pos or vel
        center      : coordinates where to shift ( 1D array with 3 values)
        """
        data = np.reshape(
            data, (-1, 3))       # data reshaped in a 2D array [nbody,3]
        data[:, 0] -= center[0]
        data[:, 1] -= center[1]
        data[:, 2] -= center[2]


#
# center
#
    def center(self, pos, vel, data_weight, center=False):
        """
        Center positions and/or velocities (if requested) according to weight

        Return :
        Center coordinates

        Arguments:
        pos         : one dimension numpy array ( nbody x 3 )
        vel         : one dimension numpy array ( nbody x 3 )
        data_weight : one dimension numpy array ( nbody     )
        center      : boolean, if False no centering
        """
        cxv = np.zeros(6, dtype='f')
        cxv[:] = np.NaN
        if pos is not None:
            cxv[0:3] = self.__centerOnWeight(pos, data_weight, center)

        if vel is not None:
            cxv[3:6] = self.__centerOnWeight(vel, data_weight, center)
        return cxv
#
# __centerOnWeight
#

    def __centerOnWeight(self, data, data_weight, center):
        # reshape array in x,y,z arrays
        # data reshaped in a 2D array [nbody,3]
        data = np.reshape(data, (-1, 3))
        x = data[:, 0]                      # x coordinates
        y = data[:, 1]                      # y coordinates
        z = data[:, 2]                      # z coordinates

        # center according weight
        xcom = np.average(x.astype(np.float64),
                          weights=data_weight.astype(np.float64))
        ycom = np.average(y.astype(np.float64),
                          weights=data_weight.astype(np.float64))
        zcom = np.average(z.astype(np.float64),
                          weights=data_weight.astype(np.float64))

        if center == True:
            data[:, 0] -= xcom
            data[:, 1] -= ycom
            data[:, 2] -= zcom

        return xcom, ycom, zcom
    #
    #
    #

    def centerOnFile(self, pos, vel, mass, com, component, center_file, analysis=None):
        """
        center positions and velocities according to paramaters

        Return :
        True if center has been found

        Arguments:
        pos         : one dimension numpy array ( nbody x 3 )
        vel         : one dimension numpy array ( nbody x 3 )
        mass        : one dimension numpy array ( nbody     )
        center_file : can be an absolute file or a string like '@mdf001' means find COD of this simulation
        com         : boolean, if True and !center_file then center according to COM

        """

        if analysis is not None:
            self.__analysis = analysis

        if center_file is None and com:  # no center file but COM reqested
            print("Centering via COM", file=sys.stderr)
            cxv = self.center(pos, vel, data_weight=mass, center=True)
            print("COM =", cxv, file=sys.stderr)
        else:
            if center_file is not None:
                ok, tcxv = self._getCenterFromFile(center_file, component)
                if ok:
                    print("Centering according to [%s]\n" % (center_file), tcxv[1:4], file=sys.stderr)
                    self.shift(pos, tcxv[1:4])
                else:
                    print("No center found according to [%s]\n" % (center_file), file=sys.stderr)
            else:
                pass

    #
    #
    #
    def _getCenterFromFile(self, center_cod, comp=None):
        """
        Return :
          boolean,tcxv  (boolean True if file exist)

        Arguments:
        According to argument 'center_cod'
        - if it's cod file, will return cod
        - if it's '@sim' it will return sim's cod at component comp
        """
        # embed()
        # check if simu
        if self.__vdebug:
            print(" __getCenterFromFile [%s]" % (center_cod), file=sys.stderr)
        if os.path.isfile(center_cod):  # it's a file
            ok, time = self.getData("time")
            return CCod(None).getCodFromFile(center_cod, time)
        else:
            tmp = center_cod.split('@')
            if (len(tmp) > 1):  # it's simulation name
                simname = tmp[1]
                if self.__vdebug:
                    print("Simulation name from COD [%s] comp <%s>\n" % (
                        simname, comp))
                    print("SELF.__ANALYSIS = <%s>" % (self.__analysis))
                cod = CCod(simname, verbose_debug=self.__vdebug)
                ok, time = self.getData("time")
                cod_base = None
                if self.__analysis is not None:
                    if hasattr(self.__analysis, "cod_dir"):
                        cod_base = self.__analysis.cod_dir
                if self.__vdebug:
                    print(" def __getCenterCod -> cod_base=[%s]" % (cod_base))
                return cod.getCodFromComp(comp, time, cod_file_base=cod_base)

        print("Unknown centering file[%s]\nNo centering..." % (center_cod), file=sys.stderr)

        return False, []

#
# computeDensity
#
    def computeDensity(self, pos, mass, K=32, N=1, method=0, ncrit=None):
        """
        Compute local density using falcON algorithm


        Return :
        boolean, rho, hsml

        Arguments :
        see getDensity from cfalcon modules
        """

        c = CFalcon()  # new falcon object
        return c.getDensity(pos, mass)  # compute density
