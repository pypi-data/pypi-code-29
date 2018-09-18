import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("eks", *args, **kwargs)

    def create_cluster(
        self,
        _request: shapes.CreateClusterRequest = None,
        *,
        name: str,
        role_arn: str,
        resources_vpc_config: shapes.VpcConfigRequest,
        version: str = ShapeBase.NOT_SET,
        client_request_token: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateClusterResponse:
        """
        Creates an Amazon EKS control plane.

        The Amazon EKS control plane consists of control plane instances that run the
        Kubernetes software, like `etcd` and the API server. The control plane runs in
        an account managed by AWS, and the Kubernetes API is exposed via the Amazon EKS
        API server endpoint.

        Amazon EKS worker nodes run in your AWS account and connect to your cluster's
        control plane via the Kubernetes API server endpoint and a certificate file that
        is created for your cluster.

        The cluster control plane is provisioned across multiple Availability Zones and
        fronted by an Elastic Load Balancing Network Load Balancer. Amazon EKS also
        provisions elastic network interfaces in your VPC subnets to provide
        connectivity from the control plane instances to the worker nodes (for example,
        to support `kubectl exec`, `logs`, and `proxy` data flows).

        After you create an Amazon EKS cluster, you must configure your Kubernetes
        tooling to communicate with the API server and launch worker nodes into your
        cluster. For more information, see [Managing Cluster
        Authentication](http://docs.aws.amazon.com/eks/latest/userguide/managing-
        auth.html) and [Launching Amazon EKS Worker
        Nodes](http://docs.aws.amazon.com/eks/latest/userguide/launch-workers.html)in
        the _Amazon EKS User Guide_.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if role_arn is not ShapeBase.NOT_SET:
                _params['role_arn'] = role_arn
            if resources_vpc_config is not ShapeBase.NOT_SET:
                _params['resources_vpc_config'] = resources_vpc_config
            if version is not ShapeBase.NOT_SET:
                _params['version'] = version
            if client_request_token is not ShapeBase.NOT_SET:
                _params['client_request_token'] = client_request_token
            _request = shapes.CreateClusterRequest(**_params)
        response = self._boto_client.create_cluster(**_request.to_boto())

        return shapes.CreateClusterResponse.from_boto(response)

    def delete_cluster(
        self,
        _request: shapes.DeleteClusterRequest = None,
        *,
        name: str,
    ) -> shapes.DeleteClusterResponse:
        """
        Deletes the Amazon EKS cluster control plane.

        If you have active services in your cluster that are associated with a load
        balancer, you must delete those services before deleting the cluster so that the
        load balancers are deleted properly. Otherwise, you can have orphaned resources
        in your VPC that prevent you from being able to delete the VPC. For more
        information, see [Deleting a
        Cluster](http://docs.aws.amazon.com/eks/latest/userguide/delete-cluster.html) in
        the _Amazon EKS User Guide_.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            _request = shapes.DeleteClusterRequest(**_params)
        response = self._boto_client.delete_cluster(**_request.to_boto())

        return shapes.DeleteClusterResponse.from_boto(response)

    def describe_cluster(
        self,
        _request: shapes.DescribeClusterRequest = None,
        *,
        name: str,
    ) -> shapes.DescribeClusterResponse:
        """
        Returns descriptive information about an Amazon EKS cluster.

        The API server endpoint and certificate authority data returned by this
        operation are required for `kubelet` and `kubectl` to communicate with your
        Kubernetes API server. For more information, see [Create a kubeconfig for Amazon
        EKS](http://docs.aws.amazon.com/eks/latest/userguide/create-kubeconfig.html).

        The API server endpoint and certificate authority data are not available until
        the cluster reaches the `ACTIVE` state.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            _request = shapes.DescribeClusterRequest(**_params)
        response = self._boto_client.describe_cluster(**_request.to_boto())

        return shapes.DescribeClusterResponse.from_boto(response)

    def list_clusters(
        self,
        _request: shapes.ListClustersRequest = None,
        *,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListClustersResponse:
        """
        Lists the Amazon EKS clusters in your AWS account in the specified Region.
        """
        if _request is None:
            _params = {}
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListClustersRequest(**_params)
        response = self._boto_client.list_clusters(**_request.to_boto())

        return shapes.ListClustersResponse.from_boto(response)
