import pytest
from mock import Mock

from orchestrate.core.ecr.service import AwsEcrService

class TestAwsEcrService(object):
  @pytest.fixture
  def services(self):
    return Mock()

  def test_with_region_name(self, services):
    ecr_service = AwsEcrService(services, region_name='foobar')
    assert ecr_service.client is not None
