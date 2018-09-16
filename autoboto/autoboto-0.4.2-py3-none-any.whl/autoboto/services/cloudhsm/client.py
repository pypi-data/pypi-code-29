import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("cloudhsm", *args, **kwargs)

    def add_tags_to_resource(
        self,
        _request: shapes.AddTagsToResourceRequest = None,
        *,
        resource_arn: str,
        tag_list: typing.List[shapes.Tag],
    ) -> shapes.AddTagsToResourceResponse:
        """
        This is documentation for **AWS CloudHSM Classic**. For more information, see
        [AWS CloudHSM Classic FAQs](http://aws.amazon.com/cloudhsm/faqs-classic/), the
        [AWS CloudHSM Classic User
        Guide](http://docs.aws.amazon.com/cloudhsm/classic/userguide/), and the [AWS
        CloudHSM Classic API
        Reference](http://docs.aws.amazon.com/cloudhsm/classic/APIReference/).

        **For information about the current version of AWS CloudHSM** , see [AWS
        CloudHSM](http://aws.amazon.com/cloudhsm/), the [AWS CloudHSM User
        Guide](http://docs.aws.amazon.com/cloudhsm/latest/userguide/), and the [AWS
        CloudHSM API
        Reference](http://docs.aws.amazon.com/cloudhsm/latest/APIReference/).

        Adds or overwrites one or more tags for the specified AWS CloudHSM resource.

        Each tag consists of a key and a value. Tag keys must be unique to each
        resource.
        """
        if _request is None:
            _params = {}
            if resource_arn is not ShapeBase.NOT_SET:
                _params['resource_arn'] = resource_arn
            if tag_list is not ShapeBase.NOT_SET:
                _params['tag_list'] = tag_list
            _request = shapes.AddTagsToResourceRequest(**_params)
        response = self._boto_client.add_tags_to_resource(**_request.to_boto())

        return shapes.AddTagsToResourceResponse.from_boto(response)

    def create_hapg(
        self,
        _request: shapes.CreateHapgRequest = None,
        *,
        label: str,
    ) -> shapes.CreateHapgResponse:
        """
        This is documentation for **AWS CloudHSM Classic**. For more information, see
        [AWS CloudHSM Classic FAQs](http://aws.amazon.com/cloudhsm/faqs-classic/), the
        [AWS CloudHSM Classic User
        Guide](http://docs.aws.amazon.com/cloudhsm/classic/userguide/), and the [AWS
        CloudHSM Classic API
        Reference](http://docs.aws.amazon.com/cloudhsm/classic/APIReference/).

        **For information about the current version of AWS CloudHSM** , see [AWS
        CloudHSM](http://aws.amazon.com/cloudhsm/), the [AWS CloudHSM User
        Guide](http://docs.aws.amazon.com/cloudhsm/latest/userguide/), and the [AWS
        CloudHSM API
        Reference](http://docs.aws.amazon.com/cloudhsm/latest/APIReference/).

        Creates a high-availability partition group. A high-availability partition group
        is a group of partitions that spans multiple physical HSMs.
        """
        if _request is None:
            _params = {}
            if label is not ShapeBase.NOT_SET:
                _params['label'] = label
            _request = shapes.CreateHapgRequest(**_params)
        response = self._boto_client.create_hapg(**_request.to_boto())

        return shapes.CreateHapgResponse.from_boto(response)

    def create_hsm(
        self,
        _request: shapes.CreateHsmRequest = None,
        *,
        subnet_id: str,
        ssh_key: str,
        iam_role_arn: str,
        subscription_type: typing.Union[str, shapes.SubscriptionType],
        eni_ip: str = ShapeBase.NOT_SET,
        external_id: str = ShapeBase.NOT_SET,
        client_token: str = ShapeBase.NOT_SET,
        syslog_ip: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateHsmResponse:
        """
        This is documentation for **AWS CloudHSM Classic**. For more information, see
        [AWS CloudHSM Classic FAQs](http://aws.amazon.com/cloudhsm/faqs-classic/), the
        [AWS CloudHSM Classic User
        Guide](http://docs.aws.amazon.com/cloudhsm/classic/userguide/), and the [AWS
        CloudHSM Classic API
        Reference](http://docs.aws.amazon.com/cloudhsm/classic/APIReference/).

        **For information about the current version of AWS CloudHSM** , see [AWS
        CloudHSM](http://aws.amazon.com/cloudhsm/), the [AWS CloudHSM User
        Guide](http://docs.aws.amazon.com/cloudhsm/latest/userguide/), and the [AWS
        CloudHSM API
        Reference](http://docs.aws.amazon.com/cloudhsm/latest/APIReference/).

        Creates an uninitialized HSM instance.

        There is an upfront fee charged for each HSM instance that you create with the
        `CreateHsm` operation. If you accidentally provision an HSM and want to request
        a refund, delete the instance using the DeleteHsm operation, go to the [AWS
        Support Center](https://console.aws.amazon.com/support/home), create a new case,
        and select **Account and Billing Support**.

        It can take up to 20 minutes to create and provision an HSM. You can monitor the
        status of the HSM with the DescribeHsm operation. The HSM is ready to be
        initialized when the status changes to `RUNNING`.
        """
        if _request is None:
            _params = {}
            if subnet_id is not ShapeBase.NOT_SET:
                _params['subnet_id'] = subnet_id
            if ssh_key is not ShapeBase.NOT_SET:
                _params['ssh_key'] = ssh_key
            if iam_role_arn is not ShapeBase.NOT_SET:
                _params['iam_role_arn'] = iam_role_arn
            if subscription_type is not ShapeBase.NOT_SET:
                _params['subscription_type'] = subscription_type
            if eni_ip is not ShapeBase.NOT_SET:
                _params['eni_ip'] = eni_ip
            if external_id is not ShapeBase.NOT_SET:
                _params['external_id'] = external_id
            if client_token is not ShapeBase.NOT_SET:
                _params['client_token'] = client_token
            if syslog_ip is not ShapeBase.NOT_SET:
                _params['syslog_ip'] = syslog_ip
            _request = shapes.CreateHsmRequest(**_params)
        response = self._boto_client.create_hsm(**_request.to_boto())

        return shapes.CreateHsmResponse.from_boto(response)

    def create_luna_client(
        self,
        _request: shapes.CreateLunaClientRequest = None,
        *,
        certificate: str,
        label: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateLunaClientResponse:
        """
        This is documentation for **AWS CloudHSM Classic**. For more information, see
        [AWS CloudHSM Classic FAQs](http://aws.amazon.com/cloudhsm/faqs-classic/), the
        [AWS CloudHSM Classic User
        Guide](http://docs.aws.amazon.com/cloudhsm/classic/userguide/), and the [AWS
        CloudHSM Classic API
        Reference](http://docs.aws.amazon.com/cloudhsm/classic/APIReference/).

        **For information about the current version of AWS CloudHSM** , see [AWS
        CloudHSM](http://aws.amazon.com/cloudhsm/), the [AWS CloudHSM User
        Guide](http://docs.aws.amazon.com/cloudhsm/latest/userguide/), and the [AWS
        CloudHSM API
        Reference](http://docs.aws.amazon.com/cloudhsm/latest/APIReference/).

        Creates an HSM client.
        """
        if _request is None:
            _params = {}
            if certificate is not ShapeBase.NOT_SET:
                _params['certificate'] = certificate
            if label is not ShapeBase.NOT_SET:
                _params['label'] = label
            _request = shapes.CreateLunaClientRequest(**_params)
        response = self._boto_client.create_luna_client(**_request.to_boto())

        return shapes.CreateLunaClientResponse.from_boto(response)

    def delete_hapg(
        self,
        _request: shapes.DeleteHapgRequest = None,
        *,
        hapg_arn: str,
    ) -> shapes.DeleteHapgResponse:
        """
        This is documentation for **AWS CloudHSM Classic**. For more information, see
        [AWS CloudHSM Classic FAQs](http://aws.amazon.com/cloudhsm/faqs-classic/), the
        [AWS CloudHSM Classic User
        Guide](http://docs.aws.amazon.com/cloudhsm/classic/userguide/), and the [AWS
        CloudHSM Classic API
        Reference](http://docs.aws.amazon.com/cloudhsm/classic/APIReference/).

        **For information about the current version of AWS CloudHSM** , see [AWS
        CloudHSM](http://aws.amazon.com/cloudhsm/), the [AWS CloudHSM User
        Guide](http://docs.aws.amazon.com/cloudhsm/latest/userguide/), and the [AWS
        CloudHSM API
        Reference](http://docs.aws.amazon.com/cloudhsm/latest/APIReference/).

        Deletes a high-availability partition group.
        """
        if _request is None:
            _params = {}
            if hapg_arn is not ShapeBase.NOT_SET:
                _params['hapg_arn'] = hapg_arn
            _request = shapes.DeleteHapgRequest(**_params)
        response = self._boto_client.delete_hapg(**_request.to_boto())

        return shapes.DeleteHapgResponse.from_boto(response)

    def delete_hsm(
        self,
        _request: shapes.DeleteHsmRequest = None,
        *,
        hsm_arn: str,
    ) -> shapes.DeleteHsmResponse:
        """
        This is documentation for **AWS CloudHSM Classic**. For more information, see
        [AWS CloudHSM Classic FAQs](http://aws.amazon.com/cloudhsm/faqs-classic/), the
        [AWS CloudHSM Classic User
        Guide](http://docs.aws.amazon.com/cloudhsm/classic/userguide/), and the [AWS
        CloudHSM Classic API
        Reference](http://docs.aws.amazon.com/cloudhsm/classic/APIReference/).

        **For information about the current version of AWS CloudHSM** , see [AWS
        CloudHSM](http://aws.amazon.com/cloudhsm/), the [AWS CloudHSM User
        Guide](http://docs.aws.amazon.com/cloudhsm/latest/userguide/), and the [AWS
        CloudHSM API
        Reference](http://docs.aws.amazon.com/cloudhsm/latest/APIReference/).

        Deletes an HSM. After completion, this operation cannot be undone and your key
        material cannot be recovered.
        """
        if _request is None:
            _params = {}
            if hsm_arn is not ShapeBase.NOT_SET:
                _params['hsm_arn'] = hsm_arn
            _request = shapes.DeleteHsmRequest(**_params)
        response = self._boto_client.delete_hsm(**_request.to_boto())

        return shapes.DeleteHsmResponse.from_boto(response)

    def delete_luna_client(
        self,
        _request: shapes.DeleteLunaClientRequest = None,
        *,
        client_arn: str,
    ) -> shapes.DeleteLunaClientResponse:
        """
        This is documentation for **AWS CloudHSM Classic**. For more information, see
        [AWS CloudHSM Classic FAQs](http://aws.amazon.com/cloudhsm/faqs-classic/), the
        [AWS CloudHSM Classic User
        Guide](http://docs.aws.amazon.com/cloudhsm/classic/userguide/), and the [AWS
        CloudHSM Classic API
        Reference](http://docs.aws.amazon.com/cloudhsm/classic/APIReference/).

        **For information about the current version of AWS CloudHSM** , see [AWS
        CloudHSM](http://aws.amazon.com/cloudhsm/), the [AWS CloudHSM User
        Guide](http://docs.aws.amazon.com/cloudhsm/latest/userguide/), and the [AWS
        CloudHSM API
        Reference](http://docs.aws.amazon.com/cloudhsm/latest/APIReference/).

        Deletes a client.
        """
        if _request is None:
            _params = {}
            if client_arn is not ShapeBase.NOT_SET:
                _params['client_arn'] = client_arn
            _request = shapes.DeleteLunaClientRequest(**_params)
        response = self._boto_client.delete_luna_client(**_request.to_boto())

        return shapes.DeleteLunaClientResponse.from_boto(response)

    def describe_hapg(
        self,
        _request: shapes.DescribeHapgRequest = None,
        *,
        hapg_arn: str,
    ) -> shapes.DescribeHapgResponse:
        """
        This is documentation for **AWS CloudHSM Classic**. For more information, see
        [AWS CloudHSM Classic FAQs](http://aws.amazon.com/cloudhsm/faqs-classic/), the
        [AWS CloudHSM Classic User
        Guide](http://docs.aws.amazon.com/cloudhsm/classic/userguide/), and the [AWS
        CloudHSM Classic API
        Reference](http://docs.aws.amazon.com/cloudhsm/classic/APIReference/).

        **For information about the current version of AWS CloudHSM** , see [AWS
        CloudHSM](http://aws.amazon.com/cloudhsm/), the [AWS CloudHSM User
        Guide](http://docs.aws.amazon.com/cloudhsm/latest/userguide/), and the [AWS
        CloudHSM API
        Reference](http://docs.aws.amazon.com/cloudhsm/latest/APIReference/).

        Retrieves information about a high-availability partition group.
        """
        if _request is None:
            _params = {}
            if hapg_arn is not ShapeBase.NOT_SET:
                _params['hapg_arn'] = hapg_arn
            _request = shapes.DescribeHapgRequest(**_params)
        response = self._boto_client.describe_hapg(**_request.to_boto())

        return shapes.DescribeHapgResponse.from_boto(response)

    def describe_hsm(
        self,
        _request: shapes.DescribeHsmRequest = None,
        *,
        hsm_arn: str = ShapeBase.NOT_SET,
        hsm_serial_number: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeHsmResponse:
        """
        This is documentation for **AWS CloudHSM Classic**. For more information, see
        [AWS CloudHSM Classic FAQs](http://aws.amazon.com/cloudhsm/faqs-classic/), the
        [AWS CloudHSM Classic User
        Guide](http://docs.aws.amazon.com/cloudhsm/classic/userguide/), and the [AWS
        CloudHSM Classic API
        Reference](http://docs.aws.amazon.com/cloudhsm/classic/APIReference/).

        **For information about the current version of AWS CloudHSM** , see [AWS
        CloudHSM](http://aws.amazon.com/cloudhsm/), the [AWS CloudHSM User
        Guide](http://docs.aws.amazon.com/cloudhsm/latest/userguide/), and the [AWS
        CloudHSM API
        Reference](http://docs.aws.amazon.com/cloudhsm/latest/APIReference/).

        Retrieves information about an HSM. You can identify the HSM by its ARN or its
        serial number.
        """
        if _request is None:
            _params = {}
            if hsm_arn is not ShapeBase.NOT_SET:
                _params['hsm_arn'] = hsm_arn
            if hsm_serial_number is not ShapeBase.NOT_SET:
                _params['hsm_serial_number'] = hsm_serial_number
            _request = shapes.DescribeHsmRequest(**_params)
        response = self._boto_client.describe_hsm(**_request.to_boto())

        return shapes.DescribeHsmResponse.from_boto(response)

    def describe_luna_client(
        self,
        _request: shapes.DescribeLunaClientRequest = None,
        *,
        client_arn: str = ShapeBase.NOT_SET,
        certificate_fingerprint: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeLunaClientResponse:
        """
        This is documentation for **AWS CloudHSM Classic**. For more information, see
        [AWS CloudHSM Classic FAQs](http://aws.amazon.com/cloudhsm/faqs-classic/), the
        [AWS CloudHSM Classic User
        Guide](http://docs.aws.amazon.com/cloudhsm/classic/userguide/), and the [AWS
        CloudHSM Classic API
        Reference](http://docs.aws.amazon.com/cloudhsm/classic/APIReference/).

        **For information about the current version of AWS CloudHSM** , see [AWS
        CloudHSM](http://aws.amazon.com/cloudhsm/), the [AWS CloudHSM User
        Guide](http://docs.aws.amazon.com/cloudhsm/latest/userguide/), and the [AWS
        CloudHSM API
        Reference](http://docs.aws.amazon.com/cloudhsm/latest/APIReference/).

        Retrieves information about an HSM client.
        """
        if _request is None:
            _params = {}
            if client_arn is not ShapeBase.NOT_SET:
                _params['client_arn'] = client_arn
            if certificate_fingerprint is not ShapeBase.NOT_SET:
                _params['certificate_fingerprint'] = certificate_fingerprint
            _request = shapes.DescribeLunaClientRequest(**_params)
        response = self._boto_client.describe_luna_client(**_request.to_boto())

        return shapes.DescribeLunaClientResponse.from_boto(response)

    def get_config(
        self,
        _request: shapes.GetConfigRequest = None,
        *,
        client_arn: str,
        client_version: typing.Union[str, shapes.ClientVersion],
        hapg_list: typing.List[str],
    ) -> shapes.GetConfigResponse:
        """
        This is documentation for **AWS CloudHSM Classic**. For more information, see
        [AWS CloudHSM Classic FAQs](http://aws.amazon.com/cloudhsm/faqs-classic/), the
        [AWS CloudHSM Classic User
        Guide](http://docs.aws.amazon.com/cloudhsm/classic/userguide/), and the [AWS
        CloudHSM Classic API
        Reference](http://docs.aws.amazon.com/cloudhsm/classic/APIReference/).

        **For information about the current version of AWS CloudHSM** , see [AWS
        CloudHSM](http://aws.amazon.com/cloudhsm/), the [AWS CloudHSM User
        Guide](http://docs.aws.amazon.com/cloudhsm/latest/userguide/), and the [AWS
        CloudHSM API
        Reference](http://docs.aws.amazon.com/cloudhsm/latest/APIReference/).

        Gets the configuration files necessary to connect to all high availability
        partition groups the client is associated with.
        """
        if _request is None:
            _params = {}
            if client_arn is not ShapeBase.NOT_SET:
                _params['client_arn'] = client_arn
            if client_version is not ShapeBase.NOT_SET:
                _params['client_version'] = client_version
            if hapg_list is not ShapeBase.NOT_SET:
                _params['hapg_list'] = hapg_list
            _request = shapes.GetConfigRequest(**_params)
        response = self._boto_client.get_config(**_request.to_boto())

        return shapes.GetConfigResponse.from_boto(response)

    def list_available_zones(
        self,
        _request: shapes.ListAvailableZonesRequest = None,
    ) -> shapes.ListAvailableZonesResponse:
        """
        This is documentation for **AWS CloudHSM Classic**. For more information, see
        [AWS CloudHSM Classic FAQs](http://aws.amazon.com/cloudhsm/faqs-classic/), the
        [AWS CloudHSM Classic User
        Guide](http://docs.aws.amazon.com/cloudhsm/classic/userguide/), and the [AWS
        CloudHSM Classic API
        Reference](http://docs.aws.amazon.com/cloudhsm/classic/APIReference/).

        **For information about the current version of AWS CloudHSM** , see [AWS
        CloudHSM](http://aws.amazon.com/cloudhsm/), the [AWS CloudHSM User
        Guide](http://docs.aws.amazon.com/cloudhsm/latest/userguide/), and the [AWS
        CloudHSM API
        Reference](http://docs.aws.amazon.com/cloudhsm/latest/APIReference/).

        Lists the Availability Zones that have available AWS CloudHSM capacity.
        """
        if _request is None:
            _params = {}
            _request = shapes.ListAvailableZonesRequest(**_params)
        response = self._boto_client.list_available_zones(**_request.to_boto())

        return shapes.ListAvailableZonesResponse.from_boto(response)

    def list_hapgs(
        self,
        _request: shapes.ListHapgsRequest = None,
        *,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListHapgsResponse:
        """
        This is documentation for **AWS CloudHSM Classic**. For more information, see
        [AWS CloudHSM Classic FAQs](http://aws.amazon.com/cloudhsm/faqs-classic/), the
        [AWS CloudHSM Classic User
        Guide](http://docs.aws.amazon.com/cloudhsm/classic/userguide/), and the [AWS
        CloudHSM Classic API
        Reference](http://docs.aws.amazon.com/cloudhsm/classic/APIReference/).

        **For information about the current version of AWS CloudHSM** , see [AWS
        CloudHSM](http://aws.amazon.com/cloudhsm/), the [AWS CloudHSM User
        Guide](http://docs.aws.amazon.com/cloudhsm/latest/userguide/), and the [AWS
        CloudHSM API
        Reference](http://docs.aws.amazon.com/cloudhsm/latest/APIReference/).

        Lists the high-availability partition groups for the account.

        This operation supports pagination with the use of the `NextToken` member. If
        more results are available, the `NextToken` member of the response contains a
        token that you pass in the next call to `ListHapgs` to retrieve the next set of
        items.
        """
        if _request is None:
            _params = {}
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListHapgsRequest(**_params)
        response = self._boto_client.list_hapgs(**_request.to_boto())

        return shapes.ListHapgsResponse.from_boto(response)

    def list_hsms(
        self,
        _request: shapes.ListHsmsRequest = None,
        *,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListHsmsResponse:
        """
        This is documentation for **AWS CloudHSM Classic**. For more information, see
        [AWS CloudHSM Classic FAQs](http://aws.amazon.com/cloudhsm/faqs-classic/), the
        [AWS CloudHSM Classic User
        Guide](http://docs.aws.amazon.com/cloudhsm/classic/userguide/), and the [AWS
        CloudHSM Classic API
        Reference](http://docs.aws.amazon.com/cloudhsm/classic/APIReference/).

        **For information about the current version of AWS CloudHSM** , see [AWS
        CloudHSM](http://aws.amazon.com/cloudhsm/), the [AWS CloudHSM User
        Guide](http://docs.aws.amazon.com/cloudhsm/latest/userguide/), and the [AWS
        CloudHSM API
        Reference](http://docs.aws.amazon.com/cloudhsm/latest/APIReference/).

        Retrieves the identifiers of all of the HSMs provisioned for the current
        customer.

        This operation supports pagination with the use of the `NextToken` member. If
        more results are available, the `NextToken` member of the response contains a
        token that you pass in the next call to `ListHsms` to retrieve the next set of
        items.
        """
        if _request is None:
            _params = {}
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListHsmsRequest(**_params)
        response = self._boto_client.list_hsms(**_request.to_boto())

        return shapes.ListHsmsResponse.from_boto(response)

    def list_luna_clients(
        self,
        _request: shapes.ListLunaClientsRequest = None,
        *,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListLunaClientsResponse:
        """
        This is documentation for **AWS CloudHSM Classic**. For more information, see
        [AWS CloudHSM Classic FAQs](http://aws.amazon.com/cloudhsm/faqs-classic/), the
        [AWS CloudHSM Classic User
        Guide](http://docs.aws.amazon.com/cloudhsm/classic/userguide/), and the [AWS
        CloudHSM Classic API
        Reference](http://docs.aws.amazon.com/cloudhsm/classic/APIReference/).

        **For information about the current version of AWS CloudHSM** , see [AWS
        CloudHSM](http://aws.amazon.com/cloudhsm/), the [AWS CloudHSM User
        Guide](http://docs.aws.amazon.com/cloudhsm/latest/userguide/), and the [AWS
        CloudHSM API
        Reference](http://docs.aws.amazon.com/cloudhsm/latest/APIReference/).

        Lists all of the clients.

        This operation supports pagination with the use of the `NextToken` member. If
        more results are available, the `NextToken` member of the response contains a
        token that you pass in the next call to `ListLunaClients` to retrieve the next
        set of items.
        """
        if _request is None:
            _params = {}
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListLunaClientsRequest(**_params)
        response = self._boto_client.list_luna_clients(**_request.to_boto())

        return shapes.ListLunaClientsResponse.from_boto(response)

    def list_tags_for_resource(
        self,
        _request: shapes.ListTagsForResourceRequest = None,
        *,
        resource_arn: str,
    ) -> shapes.ListTagsForResourceResponse:
        """
        This is documentation for **AWS CloudHSM Classic**. For more information, see
        [AWS CloudHSM Classic FAQs](http://aws.amazon.com/cloudhsm/faqs-classic/), the
        [AWS CloudHSM Classic User
        Guide](http://docs.aws.amazon.com/cloudhsm/classic/userguide/), and the [AWS
        CloudHSM Classic API
        Reference](http://docs.aws.amazon.com/cloudhsm/classic/APIReference/).

        **For information about the current version of AWS CloudHSM** , see [AWS
        CloudHSM](http://aws.amazon.com/cloudhsm/), the [AWS CloudHSM User
        Guide](http://docs.aws.amazon.com/cloudhsm/latest/userguide/), and the [AWS
        CloudHSM API
        Reference](http://docs.aws.amazon.com/cloudhsm/latest/APIReference/).

        Returns a list of all tags for the specified AWS CloudHSM resource.
        """
        if _request is None:
            _params = {}
            if resource_arn is not ShapeBase.NOT_SET:
                _params['resource_arn'] = resource_arn
            _request = shapes.ListTagsForResourceRequest(**_params)
        response = self._boto_client.list_tags_for_resource(
            **_request.to_boto()
        )

        return shapes.ListTagsForResourceResponse.from_boto(response)

    def modify_hapg(
        self,
        _request: shapes.ModifyHapgRequest = None,
        *,
        hapg_arn: str,
        label: str = ShapeBase.NOT_SET,
        partition_serial_list: typing.List[str] = ShapeBase.NOT_SET,
    ) -> shapes.ModifyHapgResponse:
        """
        This is documentation for **AWS CloudHSM Classic**. For more information, see
        [AWS CloudHSM Classic FAQs](http://aws.amazon.com/cloudhsm/faqs-classic/), the
        [AWS CloudHSM Classic User
        Guide](http://docs.aws.amazon.com/cloudhsm/classic/userguide/), and the [AWS
        CloudHSM Classic API
        Reference](http://docs.aws.amazon.com/cloudhsm/classic/APIReference/).

        **For information about the current version of AWS CloudHSM** , see [AWS
        CloudHSM](http://aws.amazon.com/cloudhsm/), the [AWS CloudHSM User
        Guide](http://docs.aws.amazon.com/cloudhsm/latest/userguide/), and the [AWS
        CloudHSM API
        Reference](http://docs.aws.amazon.com/cloudhsm/latest/APIReference/).

        Modifies an existing high-availability partition group.
        """
        if _request is None:
            _params = {}
            if hapg_arn is not ShapeBase.NOT_SET:
                _params['hapg_arn'] = hapg_arn
            if label is not ShapeBase.NOT_SET:
                _params['label'] = label
            if partition_serial_list is not ShapeBase.NOT_SET:
                _params['partition_serial_list'] = partition_serial_list
            _request = shapes.ModifyHapgRequest(**_params)
        response = self._boto_client.modify_hapg(**_request.to_boto())

        return shapes.ModifyHapgResponse.from_boto(response)

    def modify_hsm(
        self,
        _request: shapes.ModifyHsmRequest = None,
        *,
        hsm_arn: str,
        subnet_id: str = ShapeBase.NOT_SET,
        eni_ip: str = ShapeBase.NOT_SET,
        iam_role_arn: str = ShapeBase.NOT_SET,
        external_id: str = ShapeBase.NOT_SET,
        syslog_ip: str = ShapeBase.NOT_SET,
    ) -> shapes.ModifyHsmResponse:
        """
        This is documentation for **AWS CloudHSM Classic**. For more information, see
        [AWS CloudHSM Classic FAQs](http://aws.amazon.com/cloudhsm/faqs-classic/), the
        [AWS CloudHSM Classic User
        Guide](http://docs.aws.amazon.com/cloudhsm/classic/userguide/), and the [AWS
        CloudHSM Classic API
        Reference](http://docs.aws.amazon.com/cloudhsm/classic/APIReference/).

        **For information about the current version of AWS CloudHSM** , see [AWS
        CloudHSM](http://aws.amazon.com/cloudhsm/), the [AWS CloudHSM User
        Guide](http://docs.aws.amazon.com/cloudhsm/latest/userguide/), and the [AWS
        CloudHSM API
        Reference](http://docs.aws.amazon.com/cloudhsm/latest/APIReference/).

        Modifies an HSM.

        This operation can result in the HSM being offline for up to 15 minutes while
        the AWS CloudHSM service is reconfigured. If you are modifying a production HSM,
        you should ensure that your AWS CloudHSM service is configured for high
        availability, and consider executing this operation during a maintenance window.
        """
        if _request is None:
            _params = {}
            if hsm_arn is not ShapeBase.NOT_SET:
                _params['hsm_arn'] = hsm_arn
            if subnet_id is not ShapeBase.NOT_SET:
                _params['subnet_id'] = subnet_id
            if eni_ip is not ShapeBase.NOT_SET:
                _params['eni_ip'] = eni_ip
            if iam_role_arn is not ShapeBase.NOT_SET:
                _params['iam_role_arn'] = iam_role_arn
            if external_id is not ShapeBase.NOT_SET:
                _params['external_id'] = external_id
            if syslog_ip is not ShapeBase.NOT_SET:
                _params['syslog_ip'] = syslog_ip
            _request = shapes.ModifyHsmRequest(**_params)
        response = self._boto_client.modify_hsm(**_request.to_boto())

        return shapes.ModifyHsmResponse.from_boto(response)

    def modify_luna_client(
        self,
        _request: shapes.ModifyLunaClientRequest = None,
        *,
        client_arn: str,
        certificate: str,
    ) -> shapes.ModifyLunaClientResponse:
        """
        This is documentation for **AWS CloudHSM Classic**. For more information, see
        [AWS CloudHSM Classic FAQs](http://aws.amazon.com/cloudhsm/faqs-classic/), the
        [AWS CloudHSM Classic User
        Guide](http://docs.aws.amazon.com/cloudhsm/classic/userguide/), and the [AWS
        CloudHSM Classic API
        Reference](http://docs.aws.amazon.com/cloudhsm/classic/APIReference/).

        **For information about the current version of AWS CloudHSM** , see [AWS
        CloudHSM](http://aws.amazon.com/cloudhsm/), the [AWS CloudHSM User
        Guide](http://docs.aws.amazon.com/cloudhsm/latest/userguide/), and the [AWS
        CloudHSM API
        Reference](http://docs.aws.amazon.com/cloudhsm/latest/APIReference/).

        Modifies the certificate used by the client.

        This action can potentially start a workflow to install the new certificate on
        the client's HSMs.
        """
        if _request is None:
            _params = {}
            if client_arn is not ShapeBase.NOT_SET:
                _params['client_arn'] = client_arn
            if certificate is not ShapeBase.NOT_SET:
                _params['certificate'] = certificate
            _request = shapes.ModifyLunaClientRequest(**_params)
        response = self._boto_client.modify_luna_client(**_request.to_boto())

        return shapes.ModifyLunaClientResponse.from_boto(response)

    def remove_tags_from_resource(
        self,
        _request: shapes.RemoveTagsFromResourceRequest = None,
        *,
        resource_arn: str,
        tag_key_list: typing.List[str],
    ) -> shapes.RemoveTagsFromResourceResponse:
        """
        This is documentation for **AWS CloudHSM Classic**. For more information, see
        [AWS CloudHSM Classic FAQs](http://aws.amazon.com/cloudhsm/faqs-classic/), the
        [AWS CloudHSM Classic User
        Guide](http://docs.aws.amazon.com/cloudhsm/classic/userguide/), and the [AWS
        CloudHSM Classic API
        Reference](http://docs.aws.amazon.com/cloudhsm/classic/APIReference/).

        **For information about the current version of AWS CloudHSM** , see [AWS
        CloudHSM](http://aws.amazon.com/cloudhsm/), the [AWS CloudHSM User
        Guide](http://docs.aws.amazon.com/cloudhsm/latest/userguide/), and the [AWS
        CloudHSM API
        Reference](http://docs.aws.amazon.com/cloudhsm/latest/APIReference/).

        Removes one or more tags from the specified AWS CloudHSM resource.

        To remove a tag, specify only the tag key to remove (not the value). To
        overwrite the value for an existing tag, use AddTagsToResource.
        """
        if _request is None:
            _params = {}
            if resource_arn is not ShapeBase.NOT_SET:
                _params['resource_arn'] = resource_arn
            if tag_key_list is not ShapeBase.NOT_SET:
                _params['tag_key_list'] = tag_key_list
            _request = shapes.RemoveTagsFromResourceRequest(**_params)
        response = self._boto_client.remove_tags_from_resource(
            **_request.to_boto()
        )

        return shapes.RemoveTagsFromResourceResponse.from_boto(response)
