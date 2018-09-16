import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("opsworkscm", *args, **kwargs)

    def associate_node(
        self,
        _request: shapes.AssociateNodeRequest = None,
        *,
        server_name: str,
        node_name: str,
        engine_attributes: typing.List[shapes.EngineAttribute],
    ) -> shapes.AssociateNodeResponse:
        """
        Associates a new node with the server. For more information about how to
        disassociate a node, see DisassociateNode.

        On a Chef server: This command is an alternative to `knife bootstrap`.

        Example (Chef): `aws opsworks-cm associate-node --server-name _MyServer_ --node-
        name _MyManagedNode_ --engine-attributes "Name= _CHEF_ORGANIZATION_
        ,Value=default" "Name= _CHEF_NODE_PUBLIC_KEY_ ,Value= _public-key-pem_ "`

        On a Puppet server, this command is an alternative to the `puppet cert sign`
        command that signs a Puppet node CSR.

        Example (Chef): `aws opsworks-cm associate-node --server-name _MyServer_ --node-
        name _MyManagedNode_ --engine-attributes "Name= _PUPPET_NODE_CSR_ ,Value= _csr-
        pem_ "`

        A node can can only be associated with servers that are in a `HEALTHY` state.
        Otherwise, an `InvalidStateException` is thrown. A `ResourceNotFoundException`
        is thrown when the server does not exist. A `ValidationException` is raised when
        parameters of the request are not valid. The AssociateNode API call can be
        integrated into Auto Scaling configurations, AWS Cloudformation templates, or
        the user data of a server's instance.
        """
        if _request is None:
            _params = {}
            if server_name is not ShapeBase.NOT_SET:
                _params['server_name'] = server_name
            if node_name is not ShapeBase.NOT_SET:
                _params['node_name'] = node_name
            if engine_attributes is not ShapeBase.NOT_SET:
                _params['engine_attributes'] = engine_attributes
            _request = shapes.AssociateNodeRequest(**_params)
        response = self._boto_client.associate_node(**_request.to_boto())

        return shapes.AssociateNodeResponse.from_boto(response)

    def create_backup(
        self,
        _request: shapes.CreateBackupRequest = None,
        *,
        server_name: str,
        description: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateBackupResponse:
        """
        Creates an application-level backup of a server. While the server is in the
        `BACKING_UP` state, the server cannot be changed, and no additional backup can
        be created.

        Backups can be created for servers in `RUNNING`, `HEALTHY`, and `UNHEALTHY`
        states. By default, you can create a maximum of 50 manual backups.

        This operation is asynchronous.

        A `LimitExceededException` is thrown when the maximum number of manual backups
        is reached. An `InvalidStateException` is thrown when the server is not in any
        of the following states: RUNNING, HEALTHY, or UNHEALTHY. A
        `ResourceNotFoundException` is thrown when the server is not found. A
        `ValidationException` is thrown when parameters of the request are not valid.
        """
        if _request is None:
            _params = {}
            if server_name is not ShapeBase.NOT_SET:
                _params['server_name'] = server_name
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            _request = shapes.CreateBackupRequest(**_params)
        response = self._boto_client.create_backup(**_request.to_boto())

        return shapes.CreateBackupResponse.from_boto(response)

    def create_server(
        self,
        _request: shapes.CreateServerRequest = None,
        *,
        server_name: str,
        instance_profile_arn: str,
        instance_type: str,
        service_role_arn: str,
        associate_public_ip_address: bool = ShapeBase.NOT_SET,
        disable_automated_backup: bool = ShapeBase.NOT_SET,
        engine: str = ShapeBase.NOT_SET,
        engine_model: str = ShapeBase.NOT_SET,
        engine_version: str = ShapeBase.NOT_SET,
        engine_attributes: typing.List[shapes.EngineAttribute
                                      ] = ShapeBase.NOT_SET,
        backup_retention_count: int = ShapeBase.NOT_SET,
        key_pair: str = ShapeBase.NOT_SET,
        preferred_maintenance_window: str = ShapeBase.NOT_SET,
        preferred_backup_window: str = ShapeBase.NOT_SET,
        security_group_ids: typing.List[str] = ShapeBase.NOT_SET,
        subnet_ids: typing.List[str] = ShapeBase.NOT_SET,
        backup_id: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateServerResponse:
        """
        Creates and immedately starts a new server. The server is ready to use when it
        is in the `HEALTHY` state. By default, you can create a maximum of 10 servers.

        This operation is asynchronous.

        A `LimitExceededException` is thrown when you have created the maximum number of
        servers (10). A `ResourceAlreadyExistsException` is thrown when a server with
        the same name already exists in the account. A `ResourceNotFoundException` is
        thrown when you specify a backup ID that is not valid or is for a backup that
        does not exist. A `ValidationException` is thrown when parameters of the request
        are not valid.

        If you do not specify a security group by adding the `SecurityGroupIds`
        parameter, AWS OpsWorks creates a new security group.

        _Chef Automate:_ The default security group opens the Chef server to the world
        on TCP port 443. If a KeyName is present, AWS OpsWorks enables SSH access. SSH
        is also open to the world on TCP port 22.

        _Puppet Enterprise:_ The default security group opens TCP ports 22, 443, 4433,
        8140, 8142, 8143, and 8170. If a KeyName is present, AWS OpsWorks enables SSH
        access. SSH is also open to the world on TCP port 22.

        By default, your server is accessible from any IP address. We recommend that you
        update your security group rules to allow access from known IP addresses and
        address ranges only. To edit security group rules, open Security Groups in the
        navigation pane of the EC2 management console.
        """
        if _request is None:
            _params = {}
            if server_name is not ShapeBase.NOT_SET:
                _params['server_name'] = server_name
            if instance_profile_arn is not ShapeBase.NOT_SET:
                _params['instance_profile_arn'] = instance_profile_arn
            if instance_type is not ShapeBase.NOT_SET:
                _params['instance_type'] = instance_type
            if service_role_arn is not ShapeBase.NOT_SET:
                _params['service_role_arn'] = service_role_arn
            if associate_public_ip_address is not ShapeBase.NOT_SET:
                _params['associate_public_ip_address'
                       ] = associate_public_ip_address
            if disable_automated_backup is not ShapeBase.NOT_SET:
                _params['disable_automated_backup'] = disable_automated_backup
            if engine is not ShapeBase.NOT_SET:
                _params['engine'] = engine
            if engine_model is not ShapeBase.NOT_SET:
                _params['engine_model'] = engine_model
            if engine_version is not ShapeBase.NOT_SET:
                _params['engine_version'] = engine_version
            if engine_attributes is not ShapeBase.NOT_SET:
                _params['engine_attributes'] = engine_attributes
            if backup_retention_count is not ShapeBase.NOT_SET:
                _params['backup_retention_count'] = backup_retention_count
            if key_pair is not ShapeBase.NOT_SET:
                _params['key_pair'] = key_pair
            if preferred_maintenance_window is not ShapeBase.NOT_SET:
                _params['preferred_maintenance_window'
                       ] = preferred_maintenance_window
            if preferred_backup_window is not ShapeBase.NOT_SET:
                _params['preferred_backup_window'] = preferred_backup_window
            if security_group_ids is not ShapeBase.NOT_SET:
                _params['security_group_ids'] = security_group_ids
            if subnet_ids is not ShapeBase.NOT_SET:
                _params['subnet_ids'] = subnet_ids
            if backup_id is not ShapeBase.NOT_SET:
                _params['backup_id'] = backup_id
            _request = shapes.CreateServerRequest(**_params)
        response = self._boto_client.create_server(**_request.to_boto())

        return shapes.CreateServerResponse.from_boto(response)

    def delete_backup(
        self,
        _request: shapes.DeleteBackupRequest = None,
        *,
        backup_id: str,
    ) -> shapes.DeleteBackupResponse:
        """
        Deletes a backup. You can delete both manual and automated backups. This
        operation is asynchronous.

        An `InvalidStateException` is thrown when a backup deletion is already in
        progress. A `ResourceNotFoundException` is thrown when the backup does not
        exist. A `ValidationException` is thrown when parameters of the request are not
        valid.
        """
        if _request is None:
            _params = {}
            if backup_id is not ShapeBase.NOT_SET:
                _params['backup_id'] = backup_id
            _request = shapes.DeleteBackupRequest(**_params)
        response = self._boto_client.delete_backup(**_request.to_boto())

        return shapes.DeleteBackupResponse.from_boto(response)

    def delete_server(
        self,
        _request: shapes.DeleteServerRequest = None,
        *,
        server_name: str,
    ) -> shapes.DeleteServerResponse:
        """
        Deletes the server and the underlying AWS CloudFormation stacks (including the
        server's EC2 instance). When you run this command, the server state is updated
        to `DELETING`. After the server is deleted, it is no longer returned by
        `DescribeServer` requests. If the AWS CloudFormation stack cannot be deleted,
        the server cannot be deleted.

        This operation is asynchronous.

        An `InvalidStateException` is thrown when a server deletion is already in
        progress. A `ResourceNotFoundException` is thrown when the server does not
        exist. A `ValidationException` is raised when parameters of the request are not
        valid.
        """
        if _request is None:
            _params = {}
            if server_name is not ShapeBase.NOT_SET:
                _params['server_name'] = server_name
            _request = shapes.DeleteServerRequest(**_params)
        response = self._boto_client.delete_server(**_request.to_boto())

        return shapes.DeleteServerResponse.from_boto(response)

    def describe_account_attributes(
        self,
        _request: shapes.DescribeAccountAttributesRequest = None,
    ) -> shapes.DescribeAccountAttributesResponse:
        """
        Describes your account attributes, and creates requests to increase limits
        before they are reached or exceeded.

        This operation is synchronous.
        """
        if _request is None:
            _params = {}
            _request = shapes.DescribeAccountAttributesRequest(**_params)
        response = self._boto_client.describe_account_attributes(
            **_request.to_boto()
        )

        return shapes.DescribeAccountAttributesResponse.from_boto(response)

    def describe_backups(
        self,
        _request: shapes.DescribeBackupsRequest = None,
        *,
        backup_id: str = ShapeBase.NOT_SET,
        server_name: str = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.DescribeBackupsResponse:
        """
        Describes backups. The results are ordered by time, with newest backups first.
        If you do not specify a BackupId or ServerName, the command returns all backups.

        This operation is synchronous.

        A `ResourceNotFoundException` is thrown when the backup does not exist. A
        `ValidationException` is raised when parameters of the request are not valid.
        """
        if _request is None:
            _params = {}
            if backup_id is not ShapeBase.NOT_SET:
                _params['backup_id'] = backup_id
            if server_name is not ShapeBase.NOT_SET:
                _params['server_name'] = server_name
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.DescribeBackupsRequest(**_params)
        response = self._boto_client.describe_backups(**_request.to_boto())

        return shapes.DescribeBackupsResponse.from_boto(response)

    def describe_events(
        self,
        _request: shapes.DescribeEventsRequest = None,
        *,
        server_name: str,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.DescribeEventsResponse:
        """
        Describes events for a specified server. Results are ordered by time, with
        newest events first.

        This operation is synchronous.

        A `ResourceNotFoundException` is thrown when the server does not exist. A
        `ValidationException` is raised when parameters of the request are not valid.
        """
        if _request is None:
            _params = {}
            if server_name is not ShapeBase.NOT_SET:
                _params['server_name'] = server_name
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.DescribeEventsRequest(**_params)
        response = self._boto_client.describe_events(**_request.to_boto())

        return shapes.DescribeEventsResponse.from_boto(response)

    def describe_node_association_status(
        self,
        _request: shapes.DescribeNodeAssociationStatusRequest = None,
        *,
        node_association_status_token: str,
        server_name: str,
    ) -> shapes.DescribeNodeAssociationStatusResponse:
        """
        Returns the current status of an existing association or disassociation request.

        A `ResourceNotFoundException` is thrown when no recent association or
        disassociation request with the specified token is found, or when the server
        does not exist. A `ValidationException` is raised when parameters of the request
        are not valid.
        """
        if _request is None:
            _params = {}
            if node_association_status_token is not ShapeBase.NOT_SET:
                _params['node_association_status_token'
                       ] = node_association_status_token
            if server_name is not ShapeBase.NOT_SET:
                _params['server_name'] = server_name
            _request = shapes.DescribeNodeAssociationStatusRequest(**_params)
        response = self._boto_client.describe_node_association_status(
            **_request.to_boto()
        )

        return shapes.DescribeNodeAssociationStatusResponse.from_boto(response)

    def describe_servers(
        self,
        _request: shapes.DescribeServersRequest = None,
        *,
        server_name: str = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.DescribeServersResponse:
        """
        Lists all configuration management servers that are identified with your
        account. Only the stored results from Amazon DynamoDB are returned. AWS OpsWorks
        CM does not query other services.

        This operation is synchronous.

        A `ResourceNotFoundException` is thrown when the server does not exist. A
        `ValidationException` is raised when parameters of the request are not valid.
        """
        if _request is None:
            _params = {}
            if server_name is not ShapeBase.NOT_SET:
                _params['server_name'] = server_name
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.DescribeServersRequest(**_params)
        response = self._boto_client.describe_servers(**_request.to_boto())

        return shapes.DescribeServersResponse.from_boto(response)

    def disassociate_node(
        self,
        _request: shapes.DisassociateNodeRequest = None,
        *,
        server_name: str,
        node_name: str,
        engine_attributes: typing.List[shapes.EngineAttribute
                                      ] = ShapeBase.NOT_SET,
    ) -> shapes.DisassociateNodeResponse:
        """
        Disassociates a node from an AWS OpsWorks CM server, and removes the node from
        the server's managed nodes. After a node is disassociated, the node key pair is
        no longer valid for accessing the configuration manager's API. For more
        information about how to associate a node, see AssociateNode.

        A node can can only be disassociated from a server that is in a `HEALTHY` state.
        Otherwise, an `InvalidStateException` is thrown. A `ResourceNotFoundException`
        is thrown when the server does not exist. A `ValidationException` is raised when
        parameters of the request are not valid.
        """
        if _request is None:
            _params = {}
            if server_name is not ShapeBase.NOT_SET:
                _params['server_name'] = server_name
            if node_name is not ShapeBase.NOT_SET:
                _params['node_name'] = node_name
            if engine_attributes is not ShapeBase.NOT_SET:
                _params['engine_attributes'] = engine_attributes
            _request = shapes.DisassociateNodeRequest(**_params)
        response = self._boto_client.disassociate_node(**_request.to_boto())

        return shapes.DisassociateNodeResponse.from_boto(response)

    def restore_server(
        self,
        _request: shapes.RestoreServerRequest = None,
        *,
        backup_id: str,
        server_name: str,
        instance_type: str = ShapeBase.NOT_SET,
        key_pair: str = ShapeBase.NOT_SET,
    ) -> shapes.RestoreServerResponse:
        """
        Restores a backup to a server that is in a `CONNECTION_LOST`, `HEALTHY`,
        `RUNNING`, `UNHEALTHY`, or `TERMINATED` state. When you run RestoreServer, the
        server's EC2 instance is deleted, and a new EC2 instance is configured.
        RestoreServer maintains the existing server endpoint, so configuration
        management of the server's client devices (nodes) should continue to work.

        This operation is asynchronous.

        An `InvalidStateException` is thrown when the server is not in a valid state. A
        `ResourceNotFoundException` is thrown when the server does not exist. A
        `ValidationException` is raised when parameters of the request are not valid.
        """
        if _request is None:
            _params = {}
            if backup_id is not ShapeBase.NOT_SET:
                _params['backup_id'] = backup_id
            if server_name is not ShapeBase.NOT_SET:
                _params['server_name'] = server_name
            if instance_type is not ShapeBase.NOT_SET:
                _params['instance_type'] = instance_type
            if key_pair is not ShapeBase.NOT_SET:
                _params['key_pair'] = key_pair
            _request = shapes.RestoreServerRequest(**_params)
        response = self._boto_client.restore_server(**_request.to_boto())

        return shapes.RestoreServerResponse.from_boto(response)

    def start_maintenance(
        self,
        _request: shapes.StartMaintenanceRequest = None,
        *,
        server_name: str,
        engine_attributes: typing.List[shapes.EngineAttribute
                                      ] = ShapeBase.NOT_SET,
    ) -> shapes.StartMaintenanceResponse:
        """
        Manually starts server maintenance. This command can be useful if an earlier
        maintenance attempt failed, and the underlying cause of maintenance failure has
        been resolved. The server is in an `UNDER_MAINTENANCE` state while maintenance
        is in progress.

        Maintenance can only be started on servers in `HEALTHY` and `UNHEALTHY` states.
        Otherwise, an `InvalidStateException` is thrown. A `ResourceNotFoundException`
        is thrown when the server does not exist. A `ValidationException` is raised when
        parameters of the request are not valid.
        """
        if _request is None:
            _params = {}
            if server_name is not ShapeBase.NOT_SET:
                _params['server_name'] = server_name
            if engine_attributes is not ShapeBase.NOT_SET:
                _params['engine_attributes'] = engine_attributes
            _request = shapes.StartMaintenanceRequest(**_params)
        response = self._boto_client.start_maintenance(**_request.to_boto())

        return shapes.StartMaintenanceResponse.from_boto(response)

    def update_server(
        self,
        _request: shapes.UpdateServerRequest = None,
        *,
        server_name: str,
        disable_automated_backup: bool = ShapeBase.NOT_SET,
        backup_retention_count: int = ShapeBase.NOT_SET,
        preferred_maintenance_window: str = ShapeBase.NOT_SET,
        preferred_backup_window: str = ShapeBase.NOT_SET,
    ) -> shapes.UpdateServerResponse:
        """
        Updates settings for a server.

        This operation is synchronous.
        """
        if _request is None:
            _params = {}
            if server_name is not ShapeBase.NOT_SET:
                _params['server_name'] = server_name
            if disable_automated_backup is not ShapeBase.NOT_SET:
                _params['disable_automated_backup'] = disable_automated_backup
            if backup_retention_count is not ShapeBase.NOT_SET:
                _params['backup_retention_count'] = backup_retention_count
            if preferred_maintenance_window is not ShapeBase.NOT_SET:
                _params['preferred_maintenance_window'
                       ] = preferred_maintenance_window
            if preferred_backup_window is not ShapeBase.NOT_SET:
                _params['preferred_backup_window'] = preferred_backup_window
            _request = shapes.UpdateServerRequest(**_params)
        response = self._boto_client.update_server(**_request.to_boto())

        return shapes.UpdateServerResponse.from_boto(response)

    def update_server_engine_attributes(
        self,
        _request: shapes.UpdateServerEngineAttributesRequest = None,
        *,
        server_name: str,
        attribute_name: str,
        attribute_value: str = ShapeBase.NOT_SET,
    ) -> shapes.UpdateServerEngineAttributesResponse:
        """
        Updates engine-specific attributes on a specified server. The server enters the
        `MODIFYING` state when this operation is in progress. Only one update can occur
        at a time. You can use this command to reset a Chef server's private key
        (`CHEF_PIVOTAL_KEY`), a Chef server's admin password
        (`CHEF_DELIVERY_ADMIN_PASSWORD`), or a Puppet server's admin password
        (`PUPPET_ADMIN_PASSWORD`).

        This operation is asynchronous.

        This operation can only be called for servers in `HEALTHY` or `UNHEALTHY`
        states. Otherwise, an `InvalidStateException` is raised. A
        `ResourceNotFoundException` is thrown when the server does not exist. A
        `ValidationException` is raised when parameters of the request are not valid.
        """
        if _request is None:
            _params = {}
            if server_name is not ShapeBase.NOT_SET:
                _params['server_name'] = server_name
            if attribute_name is not ShapeBase.NOT_SET:
                _params['attribute_name'] = attribute_name
            if attribute_value is not ShapeBase.NOT_SET:
                _params['attribute_value'] = attribute_value
            _request = shapes.UpdateServerEngineAttributesRequest(**_params)
        response = self._boto_client.update_server_engine_attributes(
            **_request.to_boto()
        )

        return shapes.UpdateServerEngineAttributesResponse.from_boto(response)
