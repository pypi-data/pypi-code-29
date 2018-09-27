#-------------------------------------------------------------------------------
# Licence:
# Copyright (c) 2013-2018 Luzzi Valerio for Gecosistema S.r.l.
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
#
# Name:
# Purpose:
#
# Author:      Luzzi Valerio
#
# Created:     03/06/2014
#-------------------------------------------------------------------------------
from  gecosistema_core import *
import math,datetime

def strftime(frmt, text):
    """
    strftime
    """
    if not text:
        return ""
    elif isinstance(text, (datetime.datetime,datetime.date,) ):
        return text.strftime(frmt)
    elif isstring(text):
        date = datetime.datetime.strptime(text, "%Y-%m-%d")
        return date.strftime(frmt)

    return ""

def sun_NR(doy,lat):
    """
    Function to calculate the maximum sunshine duration N and incoming radiation
    at the top of the atmosphere from day of year and latitude.

    NOTE: Only valid for latitudes between 0 and 67 degrees (tropics and
    temperate zone)

    Input:
        - doy: (array of) day of year
        - lat: latitude in degrees, negative for southern hemisphere

    Output:
        - N: (array of) maximum sunshine hours [h]
        - Rext: (array of) extraterrestrial radiation [J/day]
    """

    # Set solar constant [W/m2]
    S = 1367.0 # [W/m2]
    # Convert latitude [degrees] to radians
    latrad = lat * math.pi / 180.0
    # Determine length of doy array
    #l = scipy.size(doy)
    # Check if we have a single value or an array
    #if l < 2:   # Dealing with single value...
        # calculate solar declination dt [radians]
    dt = 0.409 * math.sin(2 * math.pi / 365 * doy - 1.39)
    # calculate sunset hour angle [radians]
    ws = math.acos(-math.tan(latrad) * math.tan(dt))
    # Calculate sunshine duration N [h]
    N = 24 / math.pi * ws
    # Calculate day angle j [radians]
    j = 2 * math.pi / 365.25 * doy
    # Calculate relative distance to sun
    dr = 1.0 + 0.03344 * math.cos(j - 0.048869)
    # Calculate Rext
    Rext = S * 86400 / math.pi * dr * (ws * math.sin(latrad) * math.sin(dt) + math.sin(ws) * math.cos(latrad) * math.cos(dt))
    return Rext

def HargreavesSamani( Tmin, Tmax, date, lat=44.0, lam=2.45, kRs=0.16):
    """
    HargreavesSamani
    """

    if (Tmax is None or Tmin is None or date is None):
        return None

    jul = strftime("%j",date)
    #lam=2.45 # [MJ/kg]
    #kRs=0.16 #0.16 internal and 0.19 coastal
    julianday=float(jul)
    Ra  = sun_NR(julianday,lat)/1000000
    Pow = 0.5
    #ET0 =  0.0135*kRs*(Ra/lam)*numpy.sqrt(Tmax-Tmin)*(Tmed+17.8)
    #ET0 =  0.0135*kRs*(Ra/lam)*numpy.sqrt(Tmax-Tmin)*((Tmax+Tmin)/2+17.8)

    #ET0 = 0.0135*kRs*(Ra/lam)*numpy.power((Tmax-Tmin),0.6 )*((Tmax+Tmin)/2+17.8)
    ET0  = 0.0135*kRs*(Ra/lam)*(abs(Tmax-Tmin)**Pow)*((Tmax+Tmin)/2+17.8)
    return ET0

if __name__=="__main__":

    for Tmax, Tmin, date in [(25,36,"2018-08-07"),]:
        print HargreavesSamani( Tmin, Tmax, date )

    print HargreavesSamani(18,33,'2018-08-08',44.0,2.45,0.16);