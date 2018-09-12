import pytest
from mock import Mock

from orchestrate.core.options_validator.service import OptionsValidatorService

class TestOptionsValidatorService(object):
  @pytest.fixture()
  def options_validator_service(self):
    services = Mock()
    return OptionsValidatorService(services)

  def test_validate_orchestrate_options(self, options_validator_service):
    options_validator_service.validate_orchestrate_options(
      name='test',
      install='pip install -r requirements.txt',
      run='python model.py',
      optimization=dict(
        metrics=[
          dict(name='accuracy'),
        ],
      ),
      aws=dict(
        ecr=dict(
          repository='orchestrate/test',
        ),
      ),
      resources_per_model=dict(
        gpus=1
      ),
      framework='keras',
      language='python3.6',
      sigopt=dict(api_token='q2o3u9kdf'),
    )

  def test_validate_orchestrate_options_ok_missing_values(self, options_validator_service):
    options_validator_service.validate_orchestrate_options(
      name='test',
      run='python model.py',
    )

  @pytest.mark.parametrize('name', ['', None, dict()])
  def test_validate_orchestrate_options_name(self, options_validator_service, name):
    with pytest.raises(AssertionError):
      options_validator_service.validate_orchestrate_options(
        name=name,
        run='python model.py',
      )

  def test_validate_optimization(self, options_validator_service):
    options_validator_service.validate_optimization(
      name='',
      metrics=[dict(name='foobar')],
      parameters=[],
    )

  def test_validate_optimization_wrong_type(self, options_validator_service):
    with pytest.raises(AssertionError):
      options_validator_service.validate_optimization(
        name='',
        metrics='foobar',
        parameters=[],
      )

  def test_validate_optimization_wrong_metric(self, options_validator_service):
    with pytest.raises(AssertionError):
      options_validator_service.validate_optimization(
        name='',
        metrics=[dict(foobar='name')],
        parameters=[],
      )

    with pytest.raises(AssertionError):
      options_validator_service.validate_optimization(
        name='',
        metrics=['name'],
        parameters=[],
      )

  def test_validate_resources_per_model(self, options_validator_service):
    options_validator_service.validate_resources_per_model(gpus=2)

  @pytest.mark.parametrize('gpus', [-1, None, dict()])
  def test_validate_resources_per_model_wrong_type(self, options_validator_service, gpus):
    with pytest.raises(AssertionError):
      options_validator_service.validate_resources_per_model(gpus=gpus)

  def test_validate_aws(self, options_validator_service):
    options_validator_service.validate_aws(
      ecr=dict(
        repository='orchestrate/test',
      ),
      aws_access_key_id='foobar',
      aws_secret_access_key='barfoo',
      region='us-east-1',
    )

  def test_validate_aws_simple(self, options_validator_service):
    options_validator_service.validate_aws(
      ecr=dict(
        repository='orchestrate/test',
      ),
    )
    options_validator_service.validate_aws()

  def test_validate_aws_ecr_requires_respostiroy(self, options_validator_service):
    with pytest.raises(AssertionError):
      options_validator_service.validate_aws(
        ecr=dict(),
      )

  def test_validate_sigopt(self, options_validator_service):
    options_validator_service.validate_sigopt(
      api_token='foobar',
    )

  def test_validate_sigopt_simple(self, options_validator_service):
    options_validator_service.validate_sigopt()

  @pytest.mark.parametrize('api_token', ['', 0])
  def test_validate_sigopt_wrong_value(self, options_validator_service, api_token):
    with pytest.raises(AssertionError):
      options_validator_service.validate_sigopt(
        api_token=api_token,
      )

  def test_validate_cluster_options(self, options_validator_service):
    options_validator_service.validate_cluster_options(
      cloud_provider='aws',
      cluster_name='test-cluster',
      cpu=dict(
        instance_type='t2.small',
        min_nodes=1,
        max_nodes=1,
      ),
      gpu=dict(
        instance_type='p3.2xlarge',
        min_nodes=2,
        max_nodes=2,
      ),
    )

  def test_validate_cluster_options_ok_missing_values(self, options_validator_service):
    options_validator_service.validate_cluster_options(
      cluster_name='test-cluster',
      cpu=dict(
        instance_type='t2.small',
        min_nodes=1,
        max_nodes=1,
      ),
      gpu=dict(
        instance_type='p3.2xlarge',
        min_nodes=2,
        max_nodes=2,
      ),
    )

    options_validator_service.validate_cluster_options(
      cloud_provider='aws',
      cluster_name='test-cluster',
      gpu=dict(
        instance_type='p3.2xlarge',
        min_nodes=2,
        max_nodes=2,
      ),
    )

    options_validator_service.validate_cluster_options(
      cloud_provider='aws',
      cluster_name='test-cluster',
      cpu=dict(
        instance_type='t2.small',
        min_nodes=1,
        max_nodes=1,
      ),
    )

  @pytest.mark.parametrize('cluster_name', ['', None, dict()])
  def test_validate_cluster_options_cluster_name(self, options_validator_service, cluster_name):
    with pytest.raises(AssertionError):
      options_validator_service.validate_cluster_options(
        cloud_provider='aws',
        cluster_name=cluster_name,
        cpu=dict(
          instance_type='t2.small',
          min_nodes=1,
          max_nodes=1,
        ),
      )

  def test_validate_cluster_options_extra_options(self, options_validator_service):
    with pytest.raises(TypeError):
      options_validator_service.validate_cluster_options(
        cloud_provider='aws',
        cluster_name='test-cluster',
        tpu=dict(
          instance_type='p3.2xlarge',
          min_nodes=2,
          max_nodes=2,
        ),
      )

  def test_validate_cluster_options_wrong_type(self, options_validator_service):
    with pytest.raises(AssertionError):
      options_validator_service.validate_cluster_options(
        cloud_provider='aws',
        cluster_name='test-cluster',
        gpu=[dict(
          instance_type='p3.2xlarge',
          min_nodes=2,
          max_nodes=2,
        )],
      )

    with pytest.raises(AssertionError):
      options_validator_service.validate_cluster_options(
        cloud_provider='aws',
        cluster_name='test-cluster',
        cpu=[dict(
          instance_type='t2.small',
          min_nodes=1,
          max_nodes=1,
        )],
      )

  def test_validate_cluster_options_ignore_values(self, options_validator_service):
    options_validator_service.validate_cluster_options(
      cloud_provider='aws',
      cluster_name='test-cluster',
      cpu=dict(
        instance_type='t2.small',
        min_nodes=1,
        max_nodes=1,
      )
    )

  def test_validate_worker_stack(self, options_validator_service):
    options_validator_service.validate_worker_stack(
      name='cpu',
      instance_type='t2.small',
      min_nodes=1,
      max_nodes=1,
    )

  def test_validate_worker_stack_ignores_values(self, options_validator_service):
    options_validator_service.validate_worker_stack(
      name='foobar',
      instance_type='bazzle',
      min_nodes=2,
      max_nodes=19,
    )

  def test_validate_worker_stack_missing_options(self, options_validator_service):
    with pytest.raises(AssertionError):
      options_validator_service.validate_worker_stack(
        name='cpu',
        min_nodes=1,
        max_nodes=1,
      )

    with pytest.raises(AssertionError):
      options_validator_service.validate_worker_stack(
        name='cpu',
        instance_type='t2.small',
        max_nodes=1,
      )

    with pytest.raises(AssertionError):
      options_validator_service.validate_worker_stack(
        name='cpu',
        instance_type='t2.small',
        min_nodes=1,
      )

  def test_validate_worker_stack_wrong_type(self, options_validator_service):
    with pytest.raises(AssertionError):
      options_validator_service.validate_worker_stack(
        name='cpu',
        instance_type=2,
        min_nodes=1,
        max_nodes=1,
      )

    with pytest.raises(AssertionError):
      options_validator_service.validate_worker_stack(
        name='cpu',
        instance_type='t2.small',
        min_nodes='1',
        max_nodes=1,
      )

    with pytest.raises(AssertionError):
      options_validator_service.validate_worker_stack(
        name='cpu',
        instance_type='t2.small',
        min_nodes=1,
        max_nodes='1',
      )

  def test_validate_worker_stack_negative(self, options_validator_service):
    with pytest.raises(AssertionError):
      options_validator_service.validate_worker_stack(
        name='cpu',
        instance_type='t2.small',
        min_nodes=-1,
        max_nodes=1,
      )

    with pytest.raises(AssertionError):
      options_validator_service.validate_worker_stack(
        name='cpu',
        instance_type='t2.small',
        min_nodes=1,
        max_nodes=-1,
      )
