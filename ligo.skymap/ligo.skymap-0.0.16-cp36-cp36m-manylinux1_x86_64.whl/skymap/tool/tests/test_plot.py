import numpy as np
import pytest

from ... import distance
from ... import io
from . import run_entry_point


@pytest.fixture
def skymap(tmpdir):
    npix = 12
    filename = str(tmpdir / 'skymap.fits')
    distmean = 100.0
    diststd = 20.0
    distmu, distsigma, distnorm = distance.moments_to_parameters(
        distmean, diststd)
    io.write_sky_map(filename,
                     (np.tile(1 / npix, npix),
                      np.tile(distmu, npix),
                      np.tile(distsigma, npix),
                      np.tile(distnorm, npix)),
                     gps_time=1e9, objid='foobar',
                     distmean=distmean, diststd=diststd)
    return filename


@pytest.mark.parametrize('geo', [False, True])
def test_plot(tmpdir, skymap, geo):
    """Test ligo-skymap-plot."""
    pngfilename = str(tmpdir / 'skymap.png')
    args = ['ligo-skymap-plot', skymap, '-o', pngfilename, '--annotate',
            '--colorbar', '--radec', '320', '45']
    if geo:
        args.append('--geo')
    args.extend(['--contour', '90'])
    run_entry_point(*args)


def test_plot_volume(tmpdir, skymap):
    """Test ligo-skymap-plot-volume (at super-low resolution for speed)."""
    pngfilename = str(tmpdir / 'skymap3d.png')
    args = ['ligo-skymap-plot-volume', skymap, '-o', pngfilename, '--dpi', '8',
            '--annotate', '--contour', '90', '--radecdist', '320', '45', '100']
    run_entry_point(*args)
