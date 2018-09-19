import base64
import boto3

from orchestrate.common import safe_format
from orchestrate.core.services.base import Service


class AwsService(Service):
  def get_region(self):
    return boto3.session.Session().region_name

  def describe_cluster(self, cluster_name):
    return self.services.eks_service.describe_cluster(cluster_name=cluster_name)['cluster']

  def create_kubernetes_cluster(self, options):
    cluster_name = options['cluster_name']
    cpu_nodes_config = options.get('cpu')
    gpu_nodes_config = options.get('gpu')
    assert cpu_nodes_config or gpu_nodes_config, "Looks like your cluster config file is not" \
      " asking us to spin up any CPU or GPU machines."

    role = self.services.iam_service.ensure_eks_role(cluster_name=cluster_name)
    eks_vpc_stack = self.services.cloudformation_service.ensure_eks_vpc_stack(cluster_name=cluster_name)
    eks_vpc_stack_outputs = dict((o['OutputKey'], o['OutputValue']) for o in eks_vpc_stack.outputs)
    security_groups = eks_vpc_stack_outputs.get('SecurityGroups', '').split(',')
    subnet_ids = eks_vpc_stack_outputs.get('SubnetIds', '').split(',')

    self.services.eks_service.ensure_cluster(
      cluster_name=cluster_name,
      eks_role=role,
      security_groups=security_groups,
      subnet_ids=subnet_ids,
    )

    key_name = self.services.ec2_service.ensure_key_pair_for_cluster(cluster_name).name

    worker_stacks = []
    if cpu_nodes_config:
      cpu_worker_stack = self.services.cloudformation_service.ensure_eks_worker_stack(
        cluster_name=cluster_name,
        security_groups=eks_vpc_stack_outputs.get('SecurityGroups', '').split(','),
        vpc_id=eks_vpc_stack_outputs.get('VpcId'),
        subnet_ids=eks_vpc_stack_outputs.get('SubnetIds', '').split(','),
        max_nodes=cpu_nodes_config['max_nodes'],
        min_nodes=cpu_nodes_config['min_nodes'],
        instance_type=cpu_nodes_config['instance_type'],
        key_name=key_name,
        gpu=False,
      )
      worker_stacks.append(cpu_worker_stack)

    if gpu_nodes_config:
      gpu_instance_type = gpu_nodes_config['instance_type']
      assert gpu_instance_type.startswith('p'), safe_format(
        "The gpu instance type ({}) does not support gpus",
        gpu_instance_type
      )
      gpu_worker_stack = self.services.cloudformation_service.ensure_eks_worker_stack(
        cluster_name=cluster_name,
        security_groups=eks_vpc_stack_outputs.get('SecurityGroups', '').split(','),
        vpc_id=eks_vpc_stack_outputs.get('VpcId'),
        subnet_ids=eks_vpc_stack_outputs.get('SubnetIds', '').split(','),
        max_nodes=gpu_nodes_config['max_nodes'],
        min_nodes=gpu_nodes_config['min_nodes'],
        instance_type=gpu_nodes_config['instance_type'],
        key_name=key_name,
        gpu=True,
      )
      worker_stacks.append(gpu_worker_stack)

    node_roles = []
    for worker_stack in worker_stacks:
      self.services.cloudformation_service.wait_for_eks_worker_stack(worker_stack)
      instance_role = next(o['OutputValue'] for o in worker_stack.outputs if o['OutputKey'] == 'NodeInstanceRole')
      node_roles.append(dict(arn=instance_role))

    self.connect_kubernetes_cluster(cluster_name=cluster_name, ignore_role=True)
    self.test_kubernetes_cluster()

    cluster_access_role = self.services.iam_service.ensure_cluster_access_role(cluster_name)
    text = self.services.template_service.render_template_from_file('eks/config_map.yml.ms', dict(
      node_roles=node_roles,
      cluster_access_role=dict(
        arn=cluster_access_role.arn,
        name=cluster_access_role.name,
      ),
    ))
    self.services.kubernetes_service.apply(text)

    self.disconnect_kubernetes_cluster(cluster_name=cluster_name)
    self.connect_kubernetes_cluster(cluster_name=cluster_name)
    self.test_kubernetes_cluster(retries=3)

    self.services.kubernetes_service.ensure_plugins()

    return self.describe_cluster(cluster_name)

  def test_kubernetes_cluster(self, **kwargs):
    self.services.kubernetes_service.test_config(**kwargs)

  def connect_kubernetes_cluster(self, cluster_name, ignore_role=False):
    cluster = self.describe_cluster(cluster_name)

    if ignore_role:
      cluster_access_role_arn = None
    else:
      cluster_access_role_arn = self.services.iam_service.describe_cluster_access_role(cluster_name).arn

    # TODO(alexandra): optional role_arn is NOT the role ARN used to create the cluster
    # See Step 2 of https://docs.aws.amazon.com/eks/latest/userguide/getting-started.html
    template_args = dict(
      endpoint_url=cluster['endpoint'],
      base64_encoded_ca_cert=cluster['certificateAuthority']['data'],
      cluster_name=cluster_name,
      role_arn=cluster_access_role_arn,
    )

    self.services.kubernetes_service.write_config(
      cluster_name=cluster_name,
      string=self.services.template_service.render_template_from_file('eks/kube_config.ms', template_args),
    )

  def disconnect_kubernetes_cluster(self, cluster_name):
    self.services.kubernetes_service.ensure_config_deleted(cluster_name=cluster_name)

  def destroy_kubernetes_cluster(self, cluster_name):
    self.services.cloudformation_service.ensure_eks_worker_stack_deleted(cluster_name=cluster_name, gpu=True)
    self.services.cloudformation_service.ensure_eks_worker_stack_deleted(cluster_name=cluster_name, gpu=False)
    self.services.ec2_service.ensure_key_pair_for_cluster_deleted(cluster_name)
    self.disconnect_kubernetes_cluster(cluster_name=cluster_name)
    self.services.iam_service.ensure_cluster_access_role_deleted(cluster_name)
    self.services.eks_service.ensure_cluster_deleted(cluster_name=cluster_name)
    self.services.cloudformation_service.ensure_eks_vpc_stack_deleted(cluster_name=cluster_name)
    self.services.iam_service.ensure_eks_role_deleted(cluster_name=cluster_name)

  def login_to_container_registry(self, repository_name):
    repository = self.services.ecr_service.ensure_repositories([repository_name])['repositories'][0]
    registry_id = repository['registryId']
    authorization_data = self.services.ecr_service.get_authorization_token([registry_id])['authorizationData'][0]
    authorization_token = authorization_data['authorizationToken']
    decoded_bytes = base64.b64decode(authorization_token)
    (username, password) = decoded_bytes.decode('utf-8').split(':')
    proxy_endpoint = authorization_data['proxyEndpoint']
    return self.services.docker_service.login(
      server=proxy_endpoint,
      username=username,
      password=password,
    )
