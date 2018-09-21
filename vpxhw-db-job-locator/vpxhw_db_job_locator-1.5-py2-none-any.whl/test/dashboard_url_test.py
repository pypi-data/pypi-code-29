import pytest
import unittest

from vpxhw_db_job_locator.dashboard_url import DashboardUrl


class DashboardUrlTest(unittest.TestCase):

  def setUp(self):
    self.dburl=DashboardUrl()

  @pytest.mark.DashboardUrl
  def test_add_single_job_post_query(self):
    self.dburl.add_single_job('d1f3883fe63b01d4b8ba17c9de26a669adeccda0','libvpx_vp9','ml-cpu6','hevc_conformance_suite.txt', 'fctm_gold_model.json')

    self.assertEqual(self.dburl._jobIds, ['1e5a64568e6f4fd0a4248bbbfc3c34c3'])