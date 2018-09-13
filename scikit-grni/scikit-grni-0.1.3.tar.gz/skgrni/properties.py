import numpy as _np
from scipy.stats import chi2 as _chi2
from .utils import confidence_alpha as _alpha, svd as _svd


class SNR:

    def __init__(self, data=None, noise=None, df=None, s2=None, alpha=_alpha):
        "docstring"

        # ddof = _np.asarray(ddof)

        if data is not None:
            self.X = data

        if noise is not None:
            self.E = noise

        if s2 is not None:
            if isinstance(s2, float) or isinstance(s2, int):
                s2 = [s2]

            self.s2 = s2

        self.alpha = alpha

    def __getitem__(self, index):

        if (index == "Y") and (not hasattr(self, index)):
            return -self.P
        else:
            return getattr(self, index)

    def df(self, axis=None, ddof=0):

        if axis is None:
            df = max(_np.prod(self["X"].shape) - 1 - ddof, 1)
        else:
            df = max(self["X"].shape[axis] - 1 - ddof, 1)

        return df

    def SNRmatrixspectra(self, s2=None, true_value=False, ddof=0):

        if true_value and not hasattr(self, "E"):
            raise ValueError("True SNR values can only be calculated when noise matrix E is known.")

        if s2 is None:
            s2 = self.s2[0]

        df = self.df(ddof=ddof)

        chi2inv = _chi2.ppf(1 - self.alpha, df)

        SNR = []
        if true_value:
            ESigma = _svd(self.noise["E"], compute_uv=False)
            for S_n in _svd(self["X"], compute_uv=False):
                SNR.append(S_n / _np.max(ESigma))
        else:
            for S_n in _svd(self["X"], compute_uv=False):
                SNR.append(S_n / _np.sqrt(chi2inv * s2))

        SNR = _np.array(SNR)

        return SNR

    def SNRvectorspectra(self, s2=None, true_value=False, ddof=0):

        if true_value and not hasattr(self, "E"):
            raise ValueError("True SNR values can only be calculated when noise matrix E is known.")

        SNR = []
        if true_value:
            for i in self["X"]:
                SNR.append(_np.linalg.norm(self["X"][i]) / _np.linalg.norm(self["E"][i]))

        else:
            df = self.df(ddof=ddof, axis=1)

            if s2 is not None:
                if isinstance(s2, float) or isinstance(s2, int):
                    s2 = [s2] * df
                elif len(s2) == 1:
                    s2 = list(s2) * df

            else:
                if hasattr(self, "CVE"):
                    S2 = _np.diag(self.CVE)
                else:
                    raise ValueError("A vector 's2' of variances must be supplied. Scalars will be transformed")

            chi2inv = _chi2.ppf(1 - self.alpha, df)

            for i, x in enumerate(self["X"]):
                SNR.append(_np.linalg.norm(self["X"][x]) / _np.sqrt(chi2inv * S2[i]))

        SNR = _np.array(SNR)

        return SNR

    def scaleVariance2SNR(self, SNR, n=None, ddof=0):
        """Scale the variance to match a wished SNR given data X"""

        if n is None:
            n = min(self["X"].shape)

        S_n = _svd(self["X"], compute_uv=False)[n]
        df = self.df(ddof=ddof)

        chi2inv = _chi2.ppf(1 - self.alpha, df)

        s2 = S_n**2 / (chi2inv * SNR**2)

        return s2

    def estimateSNR4Variance(self, s2, n=None, ddof=0):
        """Scale SNR to wished a variance given data X"""

        if n is None:
            n = min(self["X"].shape)

        S_n = _svd(self["X"], compute_uv=False)[n]
        df = self.df(ddof=ddof)

        chi2inv = _chi2.ppf(1 - self.alpha, df)

        SNR = S_n / (_np.sqrt(chi2inv) * s2)

        return SNR
