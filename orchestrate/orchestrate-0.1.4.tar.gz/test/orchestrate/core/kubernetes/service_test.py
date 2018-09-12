import pytest
from mock import Mock, patch

from orchestrate.core.kubernetes.service import KubernetesError, KubernetesService

DUMMY_RETURN_VALUE = object()


class TestKubernetesService(object):
  @pytest.fixture()
  def kubernetes_service(self):
    services = Mock()
    return KubernetesService(services)

  def mock_popen(self, return_code, out_msg, err_msg=None):

    def popen(*args, **kwargs):
      stdout = kwargs.pop('stdout')
      stdout.write(out_msg)
      if err_msg:
        stderr = kwargs.pop('stderr')
        stderr.write(err_msg)
      return Mock(wait=Mock(return_value=return_code))

    return Mock(side_effect=popen)

  def test_kubectl(self, kubernetes_service):
    kubernetes_service.kube_config = 'test_config'
    with patch('orchestrate.core.kubernetes.service.subprocess') as mock_subprocess:
      mock_subprocess.Popen = self.mock_popen(0, 'DUMMY_RETURN_VALUE')
      assert kubernetes_service.kubectl(['foo'], decode_json=False) == 'DUMMY_RETURN_VALUE'
      assert mock_subprocess.Popen.call_args[0][0] == ['kubectl', 'foo']

  def test_kubectl_json(self, kubernetes_service):
    kubernetes_service.kube_config = 'test_config'
    with patch('orchestrate.core.kubernetes.service.subprocess') as mock_subprocess:
      mock_subprocess.Popen = self.mock_popen(0, '{"foo": "bar"}')
      assert kubernetes_service.kubectl(['foo'], decode_json=True) == dict(foo='bar')
      assert mock_subprocess.Popen.call_args[0][0] == ['kubectl', 'foo', '-o', 'json']

  def test_kubectl_error(self, kubernetes_service):
    kubernetes_service.kube_config = 'test_config'
    with patch('orchestrate.core.kubernetes.service.subprocess') as mock_subprocess:
      return_code = 1
      out_msg = "Test kubernetes output"
      err_msg = "Test kubernetes error"
      mock_subprocess.Popen = self.mock_popen(return_code, out_msg, err_msg)
      with pytest.raises(KubernetesError) as excinfo:
        kubernetes_service.kubectl(['foo'], decode_json=False)
      assert excinfo.value.return_code == return_code
      assert excinfo.value.stdout == out_msg
      assert excinfo.value.stderr == err_msg

  def test_kubectl_get(self, kubernetes_service):
    kubernetes_service.kube_config = 'test_config'
    kubernetes_service.kubectl = Mock(return_value=DUMMY_RETURN_VALUE)
    assert kubernetes_service.kubectl_get(['foo', 'bar']) == DUMMY_RETURN_VALUE
    kubernetes_service.kubectl.assert_called_with(['get', 'foo', 'bar'], decode_json=True)

  def test_get_pods(self, kubernetes_service):
    kubernetes_service.kubectl_get = Mock(return_value=DUMMY_RETURN_VALUE)
    assert kubernetes_service.get_pods() == DUMMY_RETURN_VALUE
    kubernetes_service.kubectl_get.assert_called_with(['pods'])

  def test_get_pods_with_job_name(self, kubernetes_service):
    kubernetes_service.kubectl_get = Mock(return_value=DUMMY_RETURN_VALUE)
    assert kubernetes_service.get_pods('foobar') == DUMMY_RETURN_VALUE
    kubernetes_service.kubectl_get.assert_called_with(['pods', '--selector', 'job-name=foobar'])

  def test_get_jobs(self, kubernetes_service):
    kubernetes_service.kubectl_get = Mock(return_value=DUMMY_RETURN_VALUE)
    assert kubernetes_service.get_jobs() == DUMMY_RETURN_VALUE
    kubernetes_service.kubectl_get.assert_called_with(['jobs'])

  def test_get_jobs_with_job_name(self, kubernetes_service):
    kubernetes_service.kubectl_get = Mock(return_value=DUMMY_RETURN_VALUE)
    assert kubernetes_service.get_jobs('foobar') == DUMMY_RETURN_VALUE
    kubernetes_service.kubectl_get.assert_called_with(['jobs/foobar'])

  def test_delete_jobs(self, kubernetes_service):
    kubernetes_service.kubectl = Mock(return_value=DUMMY_RETURN_VALUE)
    assert kubernetes_service.delete_jobs('foobar') == DUMMY_RETURN_VALUE
    kubernetes_service.kubectl.assert_called_with(['delete', 'jobs', 'foobar'], decode_json=False)

  def test_get_nodes(self, kubernetes_service):
    kubernetes_service.kubectl_get = Mock(return_value=DUMMY_RETURN_VALUE)
    assert kubernetes_service.get_nodes() == DUMMY_RETURN_VALUE
    kubernetes_service.kubectl_get.assert_called_with(['nodes'])

  def test_logs(self, kubernetes_service):
    kubernetes_service.kubectl = Mock(return_value=DUMMY_RETURN_VALUE)
    assert kubernetes_service.logs('foobar') == DUMMY_RETURN_VALUE
    kubernetes_service.kubectl.assert_called_with(['logs', 'foobar'], decode_json=False)

  def test_pod_names(self, kubernetes_service):
    kubernetes_service.get_pods = Mock(return_value=dict(
      items=[
        dict(
          metadata=dict(
            name='foo',
          ),
        ),
        dict(
          metadata=dict(
            name='bar',
          ),
        ),
      ],
    ))

    assert sorted(kubernetes_service.pod_names('baz')) == ['bar', 'foo']
    kubernetes_service.get_pods.assert_called_with(job_name='baz')

  def test_start_job(self, kubernetes_service):
    kubernetes_service.kubectl = Mock(return_value=DUMMY_RETURN_VALUE)
    assert kubernetes_service.start_job('foobar') == DUMMY_RETURN_VALUE
    kubernetes_service.kubectl.assert_called_with(['create', '-f', 'foobar'], decode_json=False)

  def test_check_nodes_are_ready(self, kubernetes_service):
    kubernetes_service.get_nodes = Mock(return_value=dict(
      items=[
        dict(
          status=dict(
            conditions=[
              dict(type='Ready', status='True'),
              dict(type='foobar', status='True'),
            ],
          ),
        ),
        dict(
          status=dict(
            conditions=[
              dict(type='Ready', status='True'),
              dict(type='foobar', status='False'),
            ],
          ),
        ),
      ],
    ))
    assert kubernetes_service.check_nodes_are_ready()

  def test_check_nodes_are_not_ready(self, kubernetes_service):
    kubernetes_service.get_nodes = Mock(return_value=dict(
      items=[
        dict(
          status=dict(
            conditions=[
              dict(type='Ready', status='True'),
              dict(type='foobar', status='True'),
            ],
          ),
        ),
        dict(
          status=dict(
            conditions=[
              dict(type='Ready', status='False'),
              dict(type='foobar', status='True'),
            ],
          ),
        ),
      ],
    ))
    assert not kubernetes_service.check_nodes_are_ready()

  def test_check_job_is_done(self, kubernetes_service):
    def get_jobs(job_name):
      if job_name == 'foobar':
        return dict(status=dict(succeeded=1))
      else:
        raise Exception()
    kubernetes_service.get_jobs = Mock(side_effect=get_jobs)
    assert kubernetes_service.check_job_is_done('foobar')

  def test_check_job_is_not_done(self, kubernetes_service):
    def get_jobs(job_name):
      if job_name == 'foobar':
        return dict(status=dict())
      else:
        raise Exception()
    kubernetes_service.get_jobs = Mock(side_effect=get_jobs)
    assert not kubernetes_service.check_job_is_done('foobar')

  def test_wait_until_job_is_done(self, kubernetes_service):
    with patch('orchestrate.core.kubernetes.service.time') as mock_time:
      kubernetes_service.check_job_is_done = Mock(side_effect=[False, False, True, True, True])
      kubernetes_service.wait_until_job_is_done('foobar')
      assert kubernetes_service.check_job_is_done.call_count == 3
      assert mock_time.sleep.called

  def test_wait_until_nodes_are_ready(self, kubernetes_service):
    with patch('orchestrate.core.kubernetes.service.time') as mock_time:
      kubernetes_service.check_nodes_are_ready = Mock(side_effect=[False, False, False, True, True])
      kubernetes_service.wait_until_nodes_are_ready(num_gpus=0)
      assert kubernetes_service.check_nodes_are_ready.call_count == 4
      assert mock_time.sleep.called
