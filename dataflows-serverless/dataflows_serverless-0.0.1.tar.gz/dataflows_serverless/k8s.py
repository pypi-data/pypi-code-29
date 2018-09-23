import yaml
import kubernetes
from time import sleep
from kubernetes.client.api_client import ApiException
from dataflows_serverless.constants import K8S_GET_POD_NAME_DELAY_SECONDS
from os import system


class K8S(object):

    def __init__(self, jinja_env):
        kubernetes.config.load_kube_config()
        contexts_list, current_context = kubernetes.config.list_kube_config_contexts()
        self.current_namespace = current_context['context']['namespace']
        self.jinja_env = jinja_env
        self._created_resources = []

    def _render_template(self, template, context):
        return yaml.load(self.jinja_env.get_template(template).render(**context))

    def track_resource(self, resource_type, resource):
        self._created_resources.append((resource_type, resource))
        return resource

    def cleanup_resources(self):
        print('cleaning up')
        for rtr in reversed(self._created_resources):
            resource_type, resource = rtr
            print('Deleting {}/{}'.format(resource_type, resource.to_dict().get('metadata', {}).get('name', '')))
            if resource_type == 'deployment':
                self.delete_deployment(resource)
            elif resource_type == 'service':
                self.delete_service(resource)
            elif resource_type == 'job':
                self.delete_job(resource)
            else:
                raise Exception('unexpected resource type: {}'.format(resource_type))

    def create_deployment(self, template, context, keep=False):
        api = kubernetes.client.AppsV1beta1Api()
        deployment = api.create_namespaced_deployment(body=self._render_template(template, context),
                                                      namespace=self.current_namespace)
        return deployment if keep else self.track_resource('deployment', deployment)

    def delete_deployment(self, deployment):
        deployment_name = deployment.to_dict()['metadata']['name']
        delete_options = kubernetes.client.V1DeleteOptions(grace_period_seconds=0, propagation_policy='Foreground')
        api = kubernetes.client.AppsV1beta1Api()
        return api.delete_namespaced_deployment(deployment_name, self.current_namespace, delete_options)

    def create_service(self, template, context, keep=False):
        api = kubernetes.client.CoreV1Api()
        service = api.create_namespaced_service(body=self._render_template(template, context), namespace=self.current_namespace)
        return service if keep else self.track_resource('service', service)

    def get_service(self, name):
        api = kubernetes.client.CoreV1Api()
        return api.read_namespaced_service(name, self.current_namespace)

    def delete_service(self, service):
        api = kubernetes.client.CoreV1Api()
        return api.delete_namespaced_service(service.to_dict()['metadata']['name'],
                                             self.current_namespace, kubernetes.client.V1DeleteOptions())

    def get_running_pod_name(self, label_selector, return_pending=False):
        api = kubernetes.client.CoreV1Api()
        while True:
            sleep(K8S_GET_POD_NAME_DELAY_SECONDS)
            pods = api.list_namespaced_pod(self.current_namespace, label_selector=label_selector)
            pods = pods.to_dict()['items']
            for pod in pods:
                if pod['status']['phase'] in ['Running', 'Succeeded', 'Failed']:
                    return pod['metadata']['name']
                elif return_pending and pod['status']['phase'] == 'Pending':
                    return pod['metadata']['name']

    def create_job(self, template, context):
        api = kubernetes.client.BatchV1Api()
        return self.track_resource('job',
                                   api.create_namespaced_job(self.current_namespace,
                                                             self._render_template(template, context)))

    def get_pod_phase(self, pod_name):
        api = kubernetes.client.CoreV1Api()
        try:
            pod = api.read_namespaced_pod(pod_name, self.current_namespace)
            return pod.to_dict()['status']['phase']
        except ApiException:
            return ''

    def delete_job(self, job):
        api = kubernetes.client.BatchV1Api()
        delete_options = kubernetes.client.V1DeleteOptions(grace_period_seconds=0)
        return api.delete_namespaced_job(job.to_dict()['metadata']['name'],
                                         self.current_namespace, delete_options)

    def delete_jobs(self, label_selector):
        api = kubernetes.client.BatchV1Api()
        return api.delete_collection_namespaced_job(self.current_namespace, label_selector=label_selector)
