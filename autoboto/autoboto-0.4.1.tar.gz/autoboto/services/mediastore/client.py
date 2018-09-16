import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("mediastore", *args, **kwargs)

    def create_container(
        self,
        _request: shapes.CreateContainerInput = None,
        *,
        container_name: str,
    ) -> shapes.CreateContainerOutput:
        """
        Creates a storage container to hold objects. A container is similar to a bucket
        in the Amazon S3 service.
        """
        if _request is None:
            _params = {}
            if container_name is not ShapeBase.NOT_SET:
                _params['container_name'] = container_name
            _request = shapes.CreateContainerInput(**_params)
        response = self._boto_client.create_container(**_request.to_boto())

        return shapes.CreateContainerOutput.from_boto(response)

    def delete_container(
        self,
        _request: shapes.DeleteContainerInput = None,
        *,
        container_name: str,
    ) -> shapes.DeleteContainerOutput:
        """
        Deletes the specified container. Before you make a `DeleteContainer` request,
        delete any objects in the container or in any folders in the container. You can
        delete only empty containers.
        """
        if _request is None:
            _params = {}
            if container_name is not ShapeBase.NOT_SET:
                _params['container_name'] = container_name
            _request = shapes.DeleteContainerInput(**_params)
        response = self._boto_client.delete_container(**_request.to_boto())

        return shapes.DeleteContainerOutput.from_boto(response)

    def delete_container_policy(
        self,
        _request: shapes.DeleteContainerPolicyInput = None,
        *,
        container_name: str,
    ) -> shapes.DeleteContainerPolicyOutput:
        """
        Deletes the access policy that is associated with the specified container.
        """
        if _request is None:
            _params = {}
            if container_name is not ShapeBase.NOT_SET:
                _params['container_name'] = container_name
            _request = shapes.DeleteContainerPolicyInput(**_params)
        response = self._boto_client.delete_container_policy(
            **_request.to_boto()
        )

        return shapes.DeleteContainerPolicyOutput.from_boto(response)

    def delete_cors_policy(
        self,
        _request: shapes.DeleteCorsPolicyInput = None,
        *,
        container_name: str,
    ) -> shapes.DeleteCorsPolicyOutput:
        """
        Deletes the cross-origin resource sharing (CORS) configuration information that
        is set for the container.

        To use this operation, you must have permission to perform the
        `MediaStore:DeleteCorsPolicy` action. The container owner has this permission by
        default and can grant this permission to others.
        """
        if _request is None:
            _params = {}
            if container_name is not ShapeBase.NOT_SET:
                _params['container_name'] = container_name
            _request = shapes.DeleteCorsPolicyInput(**_params)
        response = self._boto_client.delete_cors_policy(**_request.to_boto())

        return shapes.DeleteCorsPolicyOutput.from_boto(response)

    def describe_container(
        self,
        _request: shapes.DescribeContainerInput = None,
        *,
        container_name: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeContainerOutput:
        """
        Retrieves the properties of the requested container. This request is commonly
        used to retrieve the endpoint of a container. An endpoint is a value assigned by
        the service when a new container is created. A container's endpoint does not
        change after it has been assigned. The `DescribeContainer` request returns a
        single `Container` object based on `ContainerName`. To return all `Container`
        objects that are associated with a specified AWS account, use ListContainers.
        """
        if _request is None:
            _params = {}
            if container_name is not ShapeBase.NOT_SET:
                _params['container_name'] = container_name
            _request = shapes.DescribeContainerInput(**_params)
        response = self._boto_client.describe_container(**_request.to_boto())

        return shapes.DescribeContainerOutput.from_boto(response)

    def get_container_policy(
        self,
        _request: shapes.GetContainerPolicyInput = None,
        *,
        container_name: str,
    ) -> shapes.GetContainerPolicyOutput:
        """
        Retrieves the access policy for the specified container. For information about
        the data that is included in an access policy, see the [AWS Identity and Access
        Management User Guide](https://aws.amazon.com/documentation/iam/).
        """
        if _request is None:
            _params = {}
            if container_name is not ShapeBase.NOT_SET:
                _params['container_name'] = container_name
            _request = shapes.GetContainerPolicyInput(**_params)
        response = self._boto_client.get_container_policy(**_request.to_boto())

        return shapes.GetContainerPolicyOutput.from_boto(response)

    def get_cors_policy(
        self,
        _request: shapes.GetCorsPolicyInput = None,
        *,
        container_name: str,
    ) -> shapes.GetCorsPolicyOutput:
        """
        Returns the cross-origin resource sharing (CORS) configuration information that
        is set for the container.

        To use this operation, you must have permission to perform the
        `MediaStore:GetCorsPolicy` action. By default, the container owner has this
        permission and can grant it to others.
        """
        if _request is None:
            _params = {}
            if container_name is not ShapeBase.NOT_SET:
                _params['container_name'] = container_name
            _request = shapes.GetCorsPolicyInput(**_params)
        response = self._boto_client.get_cors_policy(**_request.to_boto())

        return shapes.GetCorsPolicyOutput.from_boto(response)

    def list_containers(
        self,
        _request: shapes.ListContainersInput = None,
        *,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.ListContainersOutput:
        """
        Lists the properties of all containers in AWS Elemental MediaStore.

        You can query to receive all the containers in one response. Or you can include
        the `MaxResults` parameter to receive a limited number of containers in each
        response. In this case, the response includes a token. To get the next set of
        containers, send the command again, this time with the `NextToken` parameter
        (with the returned token as its value). The next set of responses appears, with
        a token if there are still more containers to receive.

        See also DescribeContainer, which gets the properties of one container.
        """
        if _request is None:
            _params = {}
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.ListContainersInput(**_params)
        response = self._boto_client.list_containers(**_request.to_boto())

        return shapes.ListContainersOutput.from_boto(response)

    def put_container_policy(
        self,
        _request: shapes.PutContainerPolicyInput = None,
        *,
        container_name: str,
        policy: str,
    ) -> shapes.PutContainerPolicyOutput:
        """
        Creates an access policy for the specified container to restrict the users and
        clients that can access it. For information about the data that is included in
        an access policy, see the [AWS Identity and Access Management User
        Guide](https://aws.amazon.com/documentation/iam/).

        For this release of the REST API, you can create only one policy for a
        container. If you enter `PutContainerPolicy` twice, the second command modifies
        the existing policy.
        """
        if _request is None:
            _params = {}
            if container_name is not ShapeBase.NOT_SET:
                _params['container_name'] = container_name
            if policy is not ShapeBase.NOT_SET:
                _params['policy'] = policy
            _request = shapes.PutContainerPolicyInput(**_params)
        response = self._boto_client.put_container_policy(**_request.to_boto())

        return shapes.PutContainerPolicyOutput.from_boto(response)

    def put_cors_policy(
        self,
        _request: shapes.PutCorsPolicyInput = None,
        *,
        container_name: str,
        cors_policy: typing.List[shapes.CorsRule],
    ) -> shapes.PutCorsPolicyOutput:
        """
        Sets the cross-origin resource sharing (CORS) configuration on a container so
        that the container can service cross-origin requests. For example, you might
        want to enable a request whose origin is http://www.example.com to access your
        AWS Elemental MediaStore container at my.example.container.com by using the
        browser's XMLHttpRequest capability.

        To enable CORS on a container, you attach a CORS policy to the container. In the
        CORS policy, you configure rules that identify origins and the HTTP methods that
        can be executed on your container. The policy can contain up to 398,000
        characters. You can add up to 100 rules to a CORS policy. If more than one rule
        applies, the service uses the first applicable rule listed.
        """
        if _request is None:
            _params = {}
            if container_name is not ShapeBase.NOT_SET:
                _params['container_name'] = container_name
            if cors_policy is not ShapeBase.NOT_SET:
                _params['cors_policy'] = cors_policy
            _request = shapes.PutCorsPolicyInput(**_params)
        response = self._boto_client.put_cors_policy(**_request.to_boto())

        return shapes.PutCorsPolicyOutput.from_boto(response)
