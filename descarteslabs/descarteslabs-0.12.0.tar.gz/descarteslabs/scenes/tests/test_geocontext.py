import unittest
import mock

from descarteslabs.scenes import geocontext
import shapely.geometry


class SimpleContext(geocontext.GeoContext):
    __slots__ = ("foo", "_bar")

    def __init__(self, foo=None, bar=None):
        self.foo = foo
        self._bar = bar


class TestGeoContext(unittest.TestCase):
    def test_repr(self):
        simple = SimpleContext(1, False)
        r = repr(simple)
        expected = """SimpleContext(foo=1,
              bar=False)"""
        self.assertEqual(r, expected)

    def test_eq(self):
        simple = SimpleContext(1, False)
        simple2 = SimpleContext(1, False)
        simple_diff = SimpleContext(1, True)
        not_simple = geocontext.GeoContext()
        self.assertEqual(simple, simple)
        self.assertEqual(simple, simple2)
        self.assertNotEqual(simple, simple_diff)
        self.assertNotEqual(simple, not_simple)


class TestAOI(unittest.TestCase):
    def test_polygon_from_bounds(self):
        bounds = (-95.8364984, 39.2784859, -92.0686956, 42.7999878)
        geom = {
            'coordinates': ((
                (-92.0686956, 39.2784859),
                (-92.0686956, 42.7999878),
                (-95.8364984, 42.7999878),
                (-95.8364984, 39.2784859),
                (-92.0686956, 39.2784859)
            ),),
            'type': 'Polygon'
        }
        self.assertEqual(geom, shapely.geometry.box(*bounds).__geo_interface__)
        self.assertEqual(geocontext.AOI._polygon_from_bounds(bounds), shapely.geometry.box(*bounds).__geo_interface__)

    def test_init_base_params(self):
        geom = {
            'coordinates': [[
                [-93.52300099792355, 41.241436141055345],
                [-93.7138666, 40.703737],
                [-94.37053769704536, 40.83098709945576],
                [-94.2036617, 41.3717716],
                [-93.52300099792355, 41.241436141055345]],
            ],
            'type': 'Polygon'
        }
        resolution = 40

        ctx = geocontext.AOI(geom, resolution)
        self.assertEqual(ctx.resolution, resolution)
        self.assertEqual(ctx.bounds, (-94.37053769704536, 40.703737, -93.52300099792355, 41.3717716))
        self.assertIsInstance(ctx.geometry, shapely.geometry.Polygon)

    def test_invalid_bounds(self):
        bounds_utm = (361760.0, 4531200.0, 515360.0, 4684800.0)
        bounds_wgs84 = (-94.37053769704536, 40.703737, -93.52300099792355, 41.3717716)
        bounds_wrong_order = (bounds_wgs84[2], bounds_wgs84[1], bounds_wgs84[0], bounds_wgs84[3])
        bounds_wrong_number = bounds_wgs84[:2]
        bounds_wrong_type = dict(left=1, right=2, top=3, bottom=4)
        bounds_point = (-90.0, 35.0, -90.0, 35.0)

        geocontext.AOI._test_valid_bounds(bounds_wgs84)

        with self.assertRaises(ValueError):
            geocontext.AOI._test_valid_bounds(bounds_utm)
        with self.assertRaises(ValueError):
            geocontext.AOI._test_valid_bounds(bounds_wrong_order)
        with self.assertRaises(ValueError):
            geocontext.AOI._test_valid_bounds(bounds_wrong_number)
        with self.assertRaises(TypeError):
            geocontext.AOI._test_valid_bounds(bounds_wrong_type)
        with self.assertRaises(ValueError):
            geocontext.AOI._test_valid_bounds(bounds_point)

    def test_geojson_feature(self):
        feature = {
            'type': 'Feature',
            'geometry': {
                'coordinates': ((
                    (-93.52300099792355, 41.241436141055345),
                    (-93.7138666, 40.703737),
                    (-94.37053769704536, 40.83098709945576),
                    (-94.2036617, 41.3717716),
                    (-93.52300099792355, 41.241436141055345)),
                ),
                'type': 'Polygon'
            }
        }
        bounds_wgs84 = (-94.37053769704536, 40.703737, -93.52300099792355, 41.3717716)
        ctx = geocontext.AOI(feature, bounds=bounds_wgs84, resolution=40, crs="EPSG:3857")
        self.assertEqual(ctx.__geo_interface__, feature['geometry'])

    def test_geojson_featurecollection(self):
        feature = {
            'type': 'Feature',
            'geometry': {
                'coordinates': ((
                    (-93.52300099792355, 41.241436141055345),
                    (-93.7138666, 40.703737),
                    (-94.37053769704536, 40.83098709945576),
                    (-94.2036617, 41.3717716),
                    (-93.52300099792355, 41.241436141055345)),
                ),
                'type': 'Polygon'
            }
        }
        collection = {
            'type': 'FeatureCollection',
            'features': [feature, feature, feature],
        }
        bounds_wgs84 = (-94.37053769704536, 40.703737, -93.52300099792355, 41.3717716)
        ctx = geocontext.AOI(collection, bounds=bounds_wgs84, resolution=40, crs="EPSG:3857")
        self.assertEqual(ctx.__geo_interface__['type'], 'GeometryCollection')
        self.assertEqual(ctx.__geo_interface__['geometries'][0], feature['geometry'])

    def test_invalid(self):
        with self.assertRaises(ValueError):
            geocontext.AOI(resolution=40, shape=(120, 280))
        with self.assertRaises(TypeError):
            geocontext.AOI(shape=120)

    def test_invalid_geometry(self):
        valid_geom = {
            'coordinates': [[
                [-93.52300099792355, 41.241436141055345],
                [-93.7138666, 40.703737],
                [-94.37053769704536, 40.83098709945576],
                [-94.2036617, 41.3717716],
                [-93.52300099792355, 41.241436141055345]],
            ],
            'type': 'Polygon'
        }
        self.assertRaises(ValueError, geocontext.AOI, 1.2)
        self.assertRaises(ValueError, geocontext.AOI, {})
        self.assertRaises(ValueError, geocontext.AOI, dict(valid_geom, type='Foo'))
        self.assertRaises(ValueError, geocontext.AOI, dict(valid_geom, coordinates=1))
        self.assertRaises(ValueError, geocontext.AOI, {
            "type": "FeatureCollection",
            "features": [{"type": "Feature", "geometry": valid_geom}, "hey"],
        })

    @mock.patch.object(geocontext, "have_shapely", False)
    @mock.patch.object(geocontext, "shapely", None)
    def test_without_shapely(self):
        geom = {
            'coordinates': ((
                (-93.52300099792355, 41.241436141055345),
                (-93.7138666, 40.703737),
                (-94.37053769704536, 40.83098709945576),
                (-94.2036617, 41.3717716),
                (-93.52300099792355, 41.241436141055345)),
            ),
            'type': 'Polygon'
        }
        bounds_wgs84 = (-94.37053769704536, 40.703737, -93.52300099792355, 41.3717716)
        ctx = geocontext.AOI(geom, bounds=bounds_wgs84, resolution=40, crs="EPSG:3857")
        self.assertIs(ctx.geometry, geom)
        self.assertEqual(ctx.__geo_interface__, geom)
        self.assertEqual(ctx.bounds, bounds_wgs84)

        raster_params = ctx.raster_params
        self.assertEqual(raster_params["cutline"], geom)

        with self.assertRaises(NotImplementedError):
            geocontext.AOI(geom)

    @mock.patch.object(geocontext, "have_shapely", False)
    @mock.patch.object(geocontext, "shapely", None)
    def test_geointerface_without_shapely(self):
        geom = {
            'coordinates': ((
                (-93.52300099792355, 41.241436141055345),
                (-93.7138666, 40.703737),
                (-94.37053769704536, 40.83098709945576),
                (-94.2036617, 41.3717716),
                (-93.52300099792355, 41.241436141055345)),
            ),
            'type': 'Polygon'
        }
        geointerfaceable = mock.Mock()
        geointerfaceable.__geo_interface__ = geom

        bounds_wgs84 = (-94.37053769704536, 40.703737, -93.52300099792355, 41.3717716)
        ctx = geocontext.AOI(geometry=geointerfaceable, bounds=bounds_wgs84)
        self.assertEqual(ctx.geometry, geom)

    def test_raster_params(self):
        geom = {
            'coordinates': ((
                (-93.52300099792355, 41.241436141055345),
                (-93.7138666, 40.703737),
                (-94.37053769704536, 40.83098709945576),
                (-94.2036617, 41.3717716),
                (-93.52300099792355, 41.241436141055345)),
            ),
            'type': 'Polygon'
        }
        bounds_wgs84 = (-94.37053769704536, 40.703737, -93.52300099792355, 41.3717716)
        resolution = 40
        crs = "EPSG:32615"
        align_pixels = False

        ctx = geocontext.AOI(geom, resolution, crs, align_pixels)
        raster_params = ctx.raster_params
        expected = {
            "cutline": geom,
            "resolution": resolution,
            "srs": crs,
            "bounds_srs": "EPSG:4326",
            "align_pixels": align_pixels,
            "bounds": bounds_wgs84,
            "dimensions": None,
        }
        self.assertEqual(raster_params, expected)

    def test_help_with_too_big_resolution(self):
        aoi = geocontext.AOI(resolution=10, bounds=(-100, 35, -99.9, 35.1), crs="EPSG:4326")
        with self.assertRaises(ValueError):
            aoi.raster_params
        aoi = aoi.assign(crs="EPSG:3857")
        aoi.raster_params

    def test_assign(self):
        geom = {
            'coordinates': [[
                [-93.52300099792355, 41.241436141055345],
                [-93.7138666, 40.703737],
                [-94.37053769704536, 40.83098709945576],
                [-94.2036617, 41.3717716],
                [-93.52300099792355, 41.241436141055345]],
            ],
            'type': 'Polygon'
        }
        ctx = geocontext.AOI(resolution=40)
        ctx2 = ctx.assign(geometry=geom)
        self.assertEqual(ctx2.geometry, shapely.geometry.shape(geom))
        self.assertEqual(ctx2.resolution, 40)
        self.assertEqual(ctx2.align_pixels, True)
        self.assertEqual(ctx2.shape, None)

        ctx3 = ctx2.assign(geometry=None)
        self.assertEqual(ctx3.geometry, None)

    def test_assign_update_bounds(self):
        geom = shapely.geometry.Point(-90, 30).buffer(1).envelope
        ctx = geocontext.AOI(geometry=geom, resolution=40)

        geom_overlaps = shapely.affinity.translate(geom, xoff=1)
        self.assertTrue(geom.intersects(geom_overlaps))
        ctx_overlap = ctx.assign(geometry=geom_overlaps)
        self.assertEqual(ctx_overlap.bounds, ctx.bounds)

        ctx_updated = ctx.assign(geometry=geom_overlaps, bounds="update")
        self.assertEqual(ctx_updated.bounds, geom_overlaps.bounds)

        geom_doesnt_overlap = shapely.affinity.translate(geom, xoff=3)
        with self.assertRaises(ValueError):
            ctx.assign(geometry=geom_doesnt_overlap)
        ctx_doesnt_overlap_updated = ctx.assign(geometry=geom_doesnt_overlap, bounds="update")
        self.assertEqual(ctx_doesnt_overlap_updated.bounds, geom_doesnt_overlap.bounds)

    @mock.patch.object(geocontext, "have_shapely", False)
    @mock.patch.object(geocontext, "shapely", None)
    def test_assign_update_bounds_no_shapely_failes(self):
        geom = {
            'coordinates': ((
                (-93.52300099792355, 41.241436141055345),
                (-93.7138666, 40.703737),
                (-94.37053769704536, 40.83098709945576),
                (-94.2036617, 41.3717716),
                (-93.52300099792355, 41.241436141055345)),
            ),
            'type': 'Polygon'
        }
        bounds_wgs84 = (-94.37053769704536, 40.703737, -93.52300099792355, 41.3717716)
        ctx = geocontext.AOI(geom, bounds=bounds_wgs84)
        with self.assertRaises(NotImplementedError):
            ctx.assign(geometry=geom, bounds="update")


class TestDLTIle(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.key = '128:16:960.0:15:-1:37'
        cls.dltile_dict = {
            'geometry': {
                'coordinates': [[
                    [-94.64171754779824, 40.9202359006794],
                    [-92.81755164322226, 40.93177944075989],
                    [-92.81360932958779, 42.31528732533928],
                    [-94.6771717075502, 42.303172487087394],
                    [-94.64171754779824, 40.9202359006794]
                ]],
                'type': 'Polygon'
            },
            'properties': {
                'cs_code': 'EPSG:32615',
                'key': '128:16:960.0:15:-1:37',
                'outputBounds': [361760.0, 4531200.0, 515360.0, 4684800.0],
                'pad': 16,
                'resolution': 960.0,
                'ti': -1,
                'tilesize': 128,
                'tj': 37,
                'zone': 15
            },
            'type': 'Feature'
        }

    @mock.patch("descarteslabs.scenes.geocontext.Raster")
    def test_from_key(self, mock_raster):
        mock_raster_instance = mock_raster.return_value
        mock_raster_instance.dltile.return_value = self.dltile_dict

        tile = geocontext.DLTile.from_key(self.key)
        mock_raster_instance.dltile.assert_called_with(self.key)

        self.assertEqual(tile.key, self.key)
        self.assertEqual(tile.resolution, 960)
        self.assertEqual(tile.pad, 16)
        self.assertEqual(tile.tilesize, 128)
        self.assertEqual(tile.crs, "EPSG:32615")
        self.assertEqual(tile.bounds, (361760.0, 4531200.0, 515360.0, 4684800.0))
        self.assertEqual(tile.raster_params, {
            "dltile": self.key,
            "align_pixels": False,
        })
