from orchestrate.common import safe_format
from orchestrate.core.services.base import Service

class JobStatusService(Service):
  def parse_job(self, job):
    job_name = job['metadata']['name']
    conditions = [c['type'] for c in job['status'].get('conditions', []) if c['status'] == 'True']
    if conditions:
      job_status = ', '.join(conditions)
    else:
      job_status = 'Not Complete'

    experiment_id = self.services.job_runner_service.experiment_id(job_name)
    experiment = self.services.sigopt_service.safe_fetch_experiment(experiment_id)

    return dict(
      name=job_name,
      status=job_status,
      experiment_id=experiment_id or '??',
      observation_budget=str(experiment.observation_budget if experiment else 'n/a'),
      observation_count=str(experiment.progress.observation_count if experiment else 'n/a'),
    )

  def get_observations_by_pod(self, experiment_id):
    observations_by_pod = dict()
    for o in self.services.sigopt_service.iterate_observations(experiment_id):
      pod_name = o.metadata.get('pod_name') if o.metadata else 'UNKNOWN'

      if pod_name not in observations_by_pod:
        observations_by_pod[pod_name] = dict(success=0, failed=0)

      if o.failed:
        observations_by_pod[pod_name]['failed'] += 1
      else:
        observations_by_pod[pod_name]['success'] += 1

    return observations_by_pod

  def parse_pod(self, pod, observations_by_pod):
    pod_name = pod['metadata']['name']
    observations = observations_by_pod.get(pod_name, dict(success=0, failed=0))

    phase = pod['status']['phase']
    status = phase
    if phase in ['Pending', 'Failed', 'Unknown']:
      reasons = [condition['reason'] for condition in pod['status']['conditions'] if 'reason' in condition]
      if reasons:
        status = safe_format(
          '{} - {}',
          status,
          ', '.join(reasons),
        )

    return dict(
      name=pod_name,
      success=observations['success'],
      failed=observations['failed'],
      status=status,
    )
