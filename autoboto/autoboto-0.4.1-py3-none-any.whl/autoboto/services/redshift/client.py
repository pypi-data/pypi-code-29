import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("redshift", *args, **kwargs)

    def accept_reserved_node_exchange(
        self,
        _request: shapes.AcceptReservedNodeExchangeInputMessage = None,
        *,
        reserved_node_id: str,
        target_reserved_node_offering_id: str,
    ) -> shapes.AcceptReservedNodeExchangeOutputMessage:
        """
        Exchanges a DC1 Reserved Node for a DC2 Reserved Node with no changes to the
        configuration (term, payment type, or number of nodes) and no additional costs.
        """
        if _request is None:
            _params = {}
            if reserved_node_id is not ShapeBase.NOT_SET:
                _params['reserved_node_id'] = reserved_node_id
            if target_reserved_node_offering_id is not ShapeBase.NOT_SET:
                _params['target_reserved_node_offering_id'
                       ] = target_reserved_node_offering_id
            _request = shapes.AcceptReservedNodeExchangeInputMessage(**_params)
        response = self._boto_client.accept_reserved_node_exchange(
            **_request.to_boto()
        )

        return shapes.AcceptReservedNodeExchangeOutputMessage.from_boto(
            response
        )

    def authorize_cluster_security_group_ingress(
        self,
        _request: shapes.AuthorizeClusterSecurityGroupIngressMessage = None,
        *,
        cluster_security_group_name: str,
        cidrip: str = ShapeBase.NOT_SET,
        ec2_security_group_name: str = ShapeBase.NOT_SET,
        ec2_security_group_owner_id: str = ShapeBase.NOT_SET,
    ) -> shapes.AuthorizeClusterSecurityGroupIngressResult:
        """
        Adds an inbound (ingress) rule to an Amazon Redshift security group. Depending
        on whether the application accessing your cluster is running on the Internet or
        an Amazon EC2 instance, you can authorize inbound access to either a Classless
        Interdomain Routing (CIDR)/Internet Protocol (IP) range or to an Amazon EC2
        security group. You can add as many as 20 ingress rules to an Amazon Redshift
        security group.

        If you authorize access to an Amazon EC2 security group, specify
        _EC2SecurityGroupName_ and _EC2SecurityGroupOwnerId_. The Amazon EC2 security
        group and Amazon Redshift cluster must be in the same AWS region.

        If you authorize access to a CIDR/IP address range, specify _CIDRIP_. For an
        overview of CIDR blocks, see the Wikipedia article on [Classless Inter-Domain
        Routing](http://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing).

        You must also associate the security group with a cluster so that clients
        running on these IP addresses or the EC2 instance are authorized to connect to
        the cluster. For information about managing security groups, go to [Working with
        Security Groups](http://docs.aws.amazon.com/redshift/latest/mgmt/working-with-
        security-groups.html) in the _Amazon Redshift Cluster Management Guide_.
        """
        if _request is None:
            _params = {}
            if cluster_security_group_name is not ShapeBase.NOT_SET:
                _params['cluster_security_group_name'
                       ] = cluster_security_group_name
            if cidrip is not ShapeBase.NOT_SET:
                _params['cidrip'] = cidrip
            if ec2_security_group_name is not ShapeBase.NOT_SET:
                _params['ec2_security_group_name'] = ec2_security_group_name
            if ec2_security_group_owner_id is not ShapeBase.NOT_SET:
                _params['ec2_security_group_owner_id'
                       ] = ec2_security_group_owner_id
            _request = shapes.AuthorizeClusterSecurityGroupIngressMessage(
                **_params
            )
        response = self._boto_client.authorize_cluster_security_group_ingress(
            **_request.to_boto()
        )

        return shapes.AuthorizeClusterSecurityGroupIngressResult.from_boto(
            response
        )

    def authorize_snapshot_access(
        self,
        _request: shapes.AuthorizeSnapshotAccessMessage = None,
        *,
        snapshot_identifier: str,
        account_with_restore_access: str,
        snapshot_cluster_identifier: str = ShapeBase.NOT_SET,
    ) -> shapes.AuthorizeSnapshotAccessResult:
        """
        Authorizes the specified AWS customer account to restore the specified snapshot.

        For more information about working with snapshots, go to [Amazon Redshift
        Snapshots](http://docs.aws.amazon.com/redshift/latest/mgmt/working-with-
        snapshots.html) in the _Amazon Redshift Cluster Management Guide_.
        """
        if _request is None:
            _params = {}
            if snapshot_identifier is not ShapeBase.NOT_SET:
                _params['snapshot_identifier'] = snapshot_identifier
            if account_with_restore_access is not ShapeBase.NOT_SET:
                _params['account_with_restore_access'
                       ] = account_with_restore_access
            if snapshot_cluster_identifier is not ShapeBase.NOT_SET:
                _params['snapshot_cluster_identifier'
                       ] = snapshot_cluster_identifier
            _request = shapes.AuthorizeSnapshotAccessMessage(**_params)
        response = self._boto_client.authorize_snapshot_access(
            **_request.to_boto()
        )

        return shapes.AuthorizeSnapshotAccessResult.from_boto(response)

    def copy_cluster_snapshot(
        self,
        _request: shapes.CopyClusterSnapshotMessage = None,
        *,
        source_snapshot_identifier: str,
        target_snapshot_identifier: str,
        source_snapshot_cluster_identifier: str = ShapeBase.NOT_SET,
    ) -> shapes.CopyClusterSnapshotResult:
        """
        Copies the specified automated cluster snapshot to a new manual cluster
        snapshot. The source must be an automated snapshot and it must be in the
        available state.

        When you delete a cluster, Amazon Redshift deletes any automated snapshots of
        the cluster. Also, when the retention period of the snapshot expires, Amazon
        Redshift automatically deletes it. If you want to keep an automated snapshot for
        a longer period, you can make a manual copy of the snapshot. Manual snapshots
        are retained until you delete them.

        For more information about working with snapshots, go to [Amazon Redshift
        Snapshots](http://docs.aws.amazon.com/redshift/latest/mgmt/working-with-
        snapshots.html) in the _Amazon Redshift Cluster Management Guide_.
        """
        if _request is None:
            _params = {}
            if source_snapshot_identifier is not ShapeBase.NOT_SET:
                _params['source_snapshot_identifier'
                       ] = source_snapshot_identifier
            if target_snapshot_identifier is not ShapeBase.NOT_SET:
                _params['target_snapshot_identifier'
                       ] = target_snapshot_identifier
            if source_snapshot_cluster_identifier is not ShapeBase.NOT_SET:
                _params['source_snapshot_cluster_identifier'
                       ] = source_snapshot_cluster_identifier
            _request = shapes.CopyClusterSnapshotMessage(**_params)
        response = self._boto_client.copy_cluster_snapshot(**_request.to_boto())

        return shapes.CopyClusterSnapshotResult.from_boto(response)

    def create_cluster(
        self,
        _request: shapes.CreateClusterMessage = None,
        *,
        cluster_identifier: str,
        node_type: str,
        master_username: str,
        master_user_password: str,
        db_name: str = ShapeBase.NOT_SET,
        cluster_type: str = ShapeBase.NOT_SET,
        cluster_security_groups: typing.List[str] = ShapeBase.NOT_SET,
        vpc_security_group_ids: typing.List[str] = ShapeBase.NOT_SET,
        cluster_subnet_group_name: str = ShapeBase.NOT_SET,
        availability_zone: str = ShapeBase.NOT_SET,
        preferred_maintenance_window: str = ShapeBase.NOT_SET,
        cluster_parameter_group_name: str = ShapeBase.NOT_SET,
        automated_snapshot_retention_period: int = ShapeBase.NOT_SET,
        port: int = ShapeBase.NOT_SET,
        cluster_version: str = ShapeBase.NOT_SET,
        allow_version_upgrade: bool = ShapeBase.NOT_SET,
        number_of_nodes: int = ShapeBase.NOT_SET,
        publicly_accessible: bool = ShapeBase.NOT_SET,
        encrypted: bool = ShapeBase.NOT_SET,
        hsm_client_certificate_identifier: str = ShapeBase.NOT_SET,
        hsm_configuration_identifier: str = ShapeBase.NOT_SET,
        elastic_ip: str = ShapeBase.NOT_SET,
        tags: typing.List[shapes.Tag] = ShapeBase.NOT_SET,
        kms_key_id: str = ShapeBase.NOT_SET,
        enhanced_vpc_routing: bool = ShapeBase.NOT_SET,
        additional_info: str = ShapeBase.NOT_SET,
        iam_roles: typing.List[str] = ShapeBase.NOT_SET,
        maintenance_track_name: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateClusterResult:
        """
        Creates a new cluster.

        To create a cluster in Virtual Private Cloud (VPC), you must provide a cluster
        subnet group name. The cluster subnet group identifies the subnets of your VPC
        that Amazon Redshift uses when creating the cluster. For more information about
        managing clusters, go to [Amazon Redshift
        Clusters](http://docs.aws.amazon.com/redshift/latest/mgmt/working-with-
        clusters.html) in the _Amazon Redshift Cluster Management Guide_.
        """
        if _request is None:
            _params = {}
            if cluster_identifier is not ShapeBase.NOT_SET:
                _params['cluster_identifier'] = cluster_identifier
            if node_type is not ShapeBase.NOT_SET:
                _params['node_type'] = node_type
            if master_username is not ShapeBase.NOT_SET:
                _params['master_username'] = master_username
            if master_user_password is not ShapeBase.NOT_SET:
                _params['master_user_password'] = master_user_password
            if db_name is not ShapeBase.NOT_SET:
                _params['db_name'] = db_name
            if cluster_type is not ShapeBase.NOT_SET:
                _params['cluster_type'] = cluster_type
            if cluster_security_groups is not ShapeBase.NOT_SET:
                _params['cluster_security_groups'] = cluster_security_groups
            if vpc_security_group_ids is not ShapeBase.NOT_SET:
                _params['vpc_security_group_ids'] = vpc_security_group_ids
            if cluster_subnet_group_name is not ShapeBase.NOT_SET:
                _params['cluster_subnet_group_name'] = cluster_subnet_group_name
            if availability_zone is not ShapeBase.NOT_SET:
                _params['availability_zone'] = availability_zone
            if preferred_maintenance_window is not ShapeBase.NOT_SET:
                _params['preferred_maintenance_window'
                       ] = preferred_maintenance_window
            if cluster_parameter_group_name is not ShapeBase.NOT_SET:
                _params['cluster_parameter_group_name'
                       ] = cluster_parameter_group_name
            if automated_snapshot_retention_period is not ShapeBase.NOT_SET:
                _params['automated_snapshot_retention_period'
                       ] = automated_snapshot_retention_period
            if port is not ShapeBase.NOT_SET:
                _params['port'] = port
            if cluster_version is not ShapeBase.NOT_SET:
                _params['cluster_version'] = cluster_version
            if allow_version_upgrade is not ShapeBase.NOT_SET:
                _params['allow_version_upgrade'] = allow_version_upgrade
            if number_of_nodes is not ShapeBase.NOT_SET:
                _params['number_of_nodes'] = number_of_nodes
            if publicly_accessible is not ShapeBase.NOT_SET:
                _params['publicly_accessible'] = publicly_accessible
            if encrypted is not ShapeBase.NOT_SET:
                _params['encrypted'] = encrypted
            if hsm_client_certificate_identifier is not ShapeBase.NOT_SET:
                _params['hsm_client_certificate_identifier'
                       ] = hsm_client_certificate_identifier
            if hsm_configuration_identifier is not ShapeBase.NOT_SET:
                _params['hsm_configuration_identifier'
                       ] = hsm_configuration_identifier
            if elastic_ip is not ShapeBase.NOT_SET:
                _params['elastic_ip'] = elastic_ip
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            if kms_key_id is not ShapeBase.NOT_SET:
                _params['kms_key_id'] = kms_key_id
            if enhanced_vpc_routing is not ShapeBase.NOT_SET:
                _params['enhanced_vpc_routing'] = enhanced_vpc_routing
            if additional_info is not ShapeBase.NOT_SET:
                _params['additional_info'] = additional_info
            if iam_roles is not ShapeBase.NOT_SET:
                _params['iam_roles'] = iam_roles
            if maintenance_track_name is not ShapeBase.NOT_SET:
                _params['maintenance_track_name'] = maintenance_track_name
            _request = shapes.CreateClusterMessage(**_params)
        response = self._boto_client.create_cluster(**_request.to_boto())

        return shapes.CreateClusterResult.from_boto(response)

    def create_cluster_parameter_group(
        self,
        _request: shapes.CreateClusterParameterGroupMessage = None,
        *,
        parameter_group_name: str,
        parameter_group_family: str,
        description: str,
        tags: typing.List[shapes.Tag] = ShapeBase.NOT_SET,
    ) -> shapes.CreateClusterParameterGroupResult:
        """
        Creates an Amazon Redshift parameter group.

        Creating parameter groups is independent of creating clusters. You can associate
        a cluster with a parameter group when you create the cluster. You can also
        associate an existing cluster with a parameter group after the cluster is
        created by using ModifyCluster.

        Parameters in the parameter group define specific behavior that applies to the
        databases you create on the cluster. For more information about parameters and
        parameter groups, go to [Amazon Redshift Parameter
        Groups](http://docs.aws.amazon.com/redshift/latest/mgmt/working-with-parameter-
        groups.html) in the _Amazon Redshift Cluster Management Guide_.
        """
        if _request is None:
            _params = {}
            if parameter_group_name is not ShapeBase.NOT_SET:
                _params['parameter_group_name'] = parameter_group_name
            if parameter_group_family is not ShapeBase.NOT_SET:
                _params['parameter_group_family'] = parameter_group_family
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            _request = shapes.CreateClusterParameterGroupMessage(**_params)
        response = self._boto_client.create_cluster_parameter_group(
            **_request.to_boto()
        )

        return shapes.CreateClusterParameterGroupResult.from_boto(response)

    def create_cluster_security_group(
        self,
        _request: shapes.CreateClusterSecurityGroupMessage = None,
        *,
        cluster_security_group_name: str,
        description: str,
        tags: typing.List[shapes.Tag] = ShapeBase.NOT_SET,
    ) -> shapes.CreateClusterSecurityGroupResult:
        """
        Creates a new Amazon Redshift security group. You use security groups to control
        access to non-VPC clusters.

        For information about managing security groups, go to [Amazon Redshift Cluster
        Security Groups](http://docs.aws.amazon.com/redshift/latest/mgmt/working-with-
        security-groups.html) in the _Amazon Redshift Cluster Management Guide_.
        """
        if _request is None:
            _params = {}
            if cluster_security_group_name is not ShapeBase.NOT_SET:
                _params['cluster_security_group_name'
                       ] = cluster_security_group_name
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            _request = shapes.CreateClusterSecurityGroupMessage(**_params)
        response = self._boto_client.create_cluster_security_group(
            **_request.to_boto()
        )

        return shapes.CreateClusterSecurityGroupResult.from_boto(response)

    def create_cluster_snapshot(
        self,
        _request: shapes.CreateClusterSnapshotMessage = None,
        *,
        snapshot_identifier: str,
        cluster_identifier: str,
        tags: typing.List[shapes.Tag] = ShapeBase.NOT_SET,
    ) -> shapes.CreateClusterSnapshotResult:
        """
        Creates a manual snapshot of the specified cluster. The cluster must be in the
        `available` state.

        For more information about working with snapshots, go to [Amazon Redshift
        Snapshots](http://docs.aws.amazon.com/redshift/latest/mgmt/working-with-
        snapshots.html) in the _Amazon Redshift Cluster Management Guide_.
        """
        if _request is None:
            _params = {}
            if snapshot_identifier is not ShapeBase.NOT_SET:
                _params['snapshot_identifier'] = snapshot_identifier
            if cluster_identifier is not ShapeBase.NOT_SET:
                _params['cluster_identifier'] = cluster_identifier
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            _request = shapes.CreateClusterSnapshotMessage(**_params)
        response = self._boto_client.create_cluster_snapshot(
            **_request.to_boto()
        )

        return shapes.CreateClusterSnapshotResult.from_boto(response)

    def create_cluster_subnet_group(
        self,
        _request: shapes.CreateClusterSubnetGroupMessage = None,
        *,
        cluster_subnet_group_name: str,
        description: str,
        subnet_ids: typing.List[str],
        tags: typing.List[shapes.Tag] = ShapeBase.NOT_SET,
    ) -> shapes.CreateClusterSubnetGroupResult:
        """
        Creates a new Amazon Redshift subnet group. You must provide a list of one or
        more subnets in your existing Amazon Virtual Private Cloud (Amazon VPC) when
        creating Amazon Redshift subnet group.

        For information about subnet groups, go to [Amazon Redshift Cluster Subnet
        Groups](http://docs.aws.amazon.com/redshift/latest/mgmt/working-with-cluster-
        subnet-groups.html) in the _Amazon Redshift Cluster Management Guide_.
        """
        if _request is None:
            _params = {}
            if cluster_subnet_group_name is not ShapeBase.NOT_SET:
                _params['cluster_subnet_group_name'] = cluster_subnet_group_name
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if subnet_ids is not ShapeBase.NOT_SET:
                _params['subnet_ids'] = subnet_ids
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            _request = shapes.CreateClusterSubnetGroupMessage(**_params)
        response = self._boto_client.create_cluster_subnet_group(
            **_request.to_boto()
        )

        return shapes.CreateClusterSubnetGroupResult.from_boto(response)

    def create_event_subscription(
        self,
        _request: shapes.CreateEventSubscriptionMessage = None,
        *,
        subscription_name: str,
        sns_topic_arn: str,
        source_type: str = ShapeBase.NOT_SET,
        source_ids: typing.List[str] = ShapeBase.NOT_SET,
        event_categories: typing.List[str] = ShapeBase.NOT_SET,
        severity: str = ShapeBase.NOT_SET,
        enabled: bool = ShapeBase.NOT_SET,
        tags: typing.List[shapes.Tag] = ShapeBase.NOT_SET,
    ) -> shapes.CreateEventSubscriptionResult:
        """
        Creates an Amazon Redshift event notification subscription. This action requires
        an ARN (Amazon Resource Name) of an Amazon SNS topic created by either the
        Amazon Redshift console, the Amazon SNS console, or the Amazon SNS API. To
        obtain an ARN with Amazon SNS, you must create a topic in Amazon SNS and
        subscribe to the topic. The ARN is displayed in the SNS console.

        You can specify the source type, and lists of Amazon Redshift source IDs, event
        categories, and event severities. Notifications will be sent for all events you
        want that match those criteria. For example, you can specify source type =
        cluster, source ID = my-cluster-1 and mycluster2, event categories =
        Availability, Backup, and severity = ERROR. The subscription will only send
        notifications for those ERROR events in the Availability and Backup categories
        for the specified clusters.

        If you specify both the source type and source IDs, such as source type =
        cluster and source identifier = my-cluster-1, notifications will be sent for all
        the cluster events for my-cluster-1. If you specify a source type but do not
        specify a source identifier, you will receive notice of the events for the
        objects of that type in your AWS account. If you do not specify either the
        SourceType nor the SourceIdentifier, you will be notified of events generated
        from all Amazon Redshift sources belonging to your AWS account. You must specify
        a source type if you specify a source ID.
        """
        if _request is None:
            _params = {}
            if subscription_name is not ShapeBase.NOT_SET:
                _params['subscription_name'] = subscription_name
            if sns_topic_arn is not ShapeBase.NOT_SET:
                _params['sns_topic_arn'] = sns_topic_arn
            if source_type is not ShapeBase.NOT_SET:
                _params['source_type'] = source_type
            if source_ids is not ShapeBase.NOT_SET:
                _params['source_ids'] = source_ids
            if event_categories is not ShapeBase.NOT_SET:
                _params['event_categories'] = event_categories
            if severity is not ShapeBase.NOT_SET:
                _params['severity'] = severity
            if enabled is not ShapeBase.NOT_SET:
                _params['enabled'] = enabled
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            _request = shapes.CreateEventSubscriptionMessage(**_params)
        response = self._boto_client.create_event_subscription(
            **_request.to_boto()
        )

        return shapes.CreateEventSubscriptionResult.from_boto(response)

    def create_hsm_client_certificate(
        self,
        _request: shapes.CreateHsmClientCertificateMessage = None,
        *,
        hsm_client_certificate_identifier: str,
        tags: typing.List[shapes.Tag] = ShapeBase.NOT_SET,
    ) -> shapes.CreateHsmClientCertificateResult:
        """
        Creates an HSM client certificate that an Amazon Redshift cluster will use to
        connect to the client's HSM in order to store and retrieve the keys used to
        encrypt the cluster databases.

        The command returns a public key, which you must store in the HSM. In addition
        to creating the HSM certificate, you must create an Amazon Redshift HSM
        configuration that provides a cluster the information needed to store and use
        encryption keys in the HSM. For more information, go to [Hardware Security
        Modules](http://docs.aws.amazon.com/redshift/latest/mgmt/working-with-HSM.html)
        in the Amazon Redshift Cluster Management Guide.
        """
        if _request is None:
            _params = {}
            if hsm_client_certificate_identifier is not ShapeBase.NOT_SET:
                _params['hsm_client_certificate_identifier'
                       ] = hsm_client_certificate_identifier
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            _request = shapes.CreateHsmClientCertificateMessage(**_params)
        response = self._boto_client.create_hsm_client_certificate(
            **_request.to_boto()
        )

        return shapes.CreateHsmClientCertificateResult.from_boto(response)

    def create_hsm_configuration(
        self,
        _request: shapes.CreateHsmConfigurationMessage = None,
        *,
        hsm_configuration_identifier: str,
        description: str,
        hsm_ip_address: str,
        hsm_partition_name: str,
        hsm_partition_password: str,
        hsm_server_public_certificate: str,
        tags: typing.List[shapes.Tag] = ShapeBase.NOT_SET,
    ) -> shapes.CreateHsmConfigurationResult:
        """
        Creates an HSM configuration that contains the information required by an Amazon
        Redshift cluster to store and use database encryption keys in a Hardware
        Security Module (HSM). After creating the HSM configuration, you can specify it
        as a parameter when creating a cluster. The cluster will then store its
        encryption keys in the HSM.

        In addition to creating an HSM configuration, you must also create an HSM client
        certificate. For more information, go to [Hardware Security
        Modules](http://docs.aws.amazon.com/redshift/latest/mgmt/working-with-HSM.html)
        in the Amazon Redshift Cluster Management Guide.
        """
        if _request is None:
            _params = {}
            if hsm_configuration_identifier is not ShapeBase.NOT_SET:
                _params['hsm_configuration_identifier'
                       ] = hsm_configuration_identifier
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if hsm_ip_address is not ShapeBase.NOT_SET:
                _params['hsm_ip_address'] = hsm_ip_address
            if hsm_partition_name is not ShapeBase.NOT_SET:
                _params['hsm_partition_name'] = hsm_partition_name
            if hsm_partition_password is not ShapeBase.NOT_SET:
                _params['hsm_partition_password'] = hsm_partition_password
            if hsm_server_public_certificate is not ShapeBase.NOT_SET:
                _params['hsm_server_public_certificate'
                       ] = hsm_server_public_certificate
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            _request = shapes.CreateHsmConfigurationMessage(**_params)
        response = self._boto_client.create_hsm_configuration(
            **_request.to_boto()
        )

        return shapes.CreateHsmConfigurationResult.from_boto(response)

    def create_snapshot_copy_grant(
        self,
        _request: shapes.CreateSnapshotCopyGrantMessage = None,
        *,
        snapshot_copy_grant_name: str,
        kms_key_id: str = ShapeBase.NOT_SET,
        tags: typing.List[shapes.Tag] = ShapeBase.NOT_SET,
    ) -> shapes.CreateSnapshotCopyGrantResult:
        """
        Creates a snapshot copy grant that permits Amazon Redshift to use a customer
        master key (CMK) from AWS Key Management Service (AWS KMS) to encrypt copied
        snapshots in a destination region.

        For more information about managing snapshot copy grants, go to [Amazon Redshift
        Database Encryption](http://docs.aws.amazon.com/redshift/latest/mgmt/working-
        with-db-encryption.html) in the _Amazon Redshift Cluster Management Guide_.
        """
        if _request is None:
            _params = {}
            if snapshot_copy_grant_name is not ShapeBase.NOT_SET:
                _params['snapshot_copy_grant_name'] = snapshot_copy_grant_name
            if kms_key_id is not ShapeBase.NOT_SET:
                _params['kms_key_id'] = kms_key_id
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            _request = shapes.CreateSnapshotCopyGrantMessage(**_params)
        response = self._boto_client.create_snapshot_copy_grant(
            **_request.to_boto()
        )

        return shapes.CreateSnapshotCopyGrantResult.from_boto(response)

    def create_tags(
        self,
        _request: shapes.CreateTagsMessage = None,
        *,
        resource_name: str,
        tags: typing.List[shapes.Tag],
    ) -> None:
        """
        Adds one or more tags to a specified resource.

        A resource can have up to 50 tags. If you try to create more than 50 tags for a
        resource, you will receive an error and the attempt will fail.

        If you specify a key that already exists for the resource, the value for that
        key will be updated with the new value.
        """
        if _request is None:
            _params = {}
            if resource_name is not ShapeBase.NOT_SET:
                _params['resource_name'] = resource_name
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            _request = shapes.CreateTagsMessage(**_params)
        response = self._boto_client.create_tags(**_request.to_boto())

    def delete_cluster(
        self,
        _request: shapes.DeleteClusterMessage = None,
        *,
        cluster_identifier: str,
        skip_final_cluster_snapshot: bool = ShapeBase.NOT_SET,
        final_cluster_snapshot_identifier: str = ShapeBase.NOT_SET,
    ) -> shapes.DeleteClusterResult:
        """
        Deletes a previously provisioned cluster. A successful response from the web
        service indicates that the request was received correctly. Use DescribeClusters
        to monitor the status of the deletion. The delete operation cannot be canceled
        or reverted once submitted. For more information about managing clusters, go to
        [Amazon Redshift
        Clusters](http://docs.aws.amazon.com/redshift/latest/mgmt/working-with-
        clusters.html) in the _Amazon Redshift Cluster Management Guide_.

        If you want to shut down the cluster and retain it for future use, set
        _SkipFinalClusterSnapshot_ to `false` and specify a name for
        _FinalClusterSnapshotIdentifier_. You can later restore this snapshot to resume
        using the cluster. If a final cluster snapshot is requested, the status of the
        cluster will be "final-snapshot" while the snapshot is being taken, then it's
        "deleting" once Amazon Redshift begins deleting the cluster.

        For more information about managing clusters, go to [Amazon Redshift
        Clusters](http://docs.aws.amazon.com/redshift/latest/mgmt/working-with-
        clusters.html) in the _Amazon Redshift Cluster Management Guide_.
        """
        if _request is None:
            _params = {}
            if cluster_identifier is not ShapeBase.NOT_SET:
                _params['cluster_identifier'] = cluster_identifier
            if skip_final_cluster_snapshot is not ShapeBase.NOT_SET:
                _params['skip_final_cluster_snapshot'
                       ] = skip_final_cluster_snapshot
            if final_cluster_snapshot_identifier is not ShapeBase.NOT_SET:
                _params['final_cluster_snapshot_identifier'
                       ] = final_cluster_snapshot_identifier
            _request = shapes.DeleteClusterMessage(**_params)
        response = self._boto_client.delete_cluster(**_request.to_boto())

        return shapes.DeleteClusterResult.from_boto(response)

    def delete_cluster_parameter_group(
        self,
        _request: shapes.DeleteClusterParameterGroupMessage = None,
        *,
        parameter_group_name: str,
    ) -> None:
        """
        Deletes a specified Amazon Redshift parameter group.

        You cannot delete a parameter group if it is associated with a cluster.
        """
        if _request is None:
            _params = {}
            if parameter_group_name is not ShapeBase.NOT_SET:
                _params['parameter_group_name'] = parameter_group_name
            _request = shapes.DeleteClusterParameterGroupMessage(**_params)
        response = self._boto_client.delete_cluster_parameter_group(
            **_request.to_boto()
        )

    def delete_cluster_security_group(
        self,
        _request: shapes.DeleteClusterSecurityGroupMessage = None,
        *,
        cluster_security_group_name: str,
    ) -> None:
        """
        Deletes an Amazon Redshift security group.

        You cannot delete a security group that is associated with any clusters. You
        cannot delete the default security group.

        For information about managing security groups, go to [Amazon Redshift Cluster
        Security Groups](http://docs.aws.amazon.com/redshift/latest/mgmt/working-with-
        security-groups.html) in the _Amazon Redshift Cluster Management Guide_.
        """
        if _request is None:
            _params = {}
            if cluster_security_group_name is not ShapeBase.NOT_SET:
                _params['cluster_security_group_name'
                       ] = cluster_security_group_name
            _request = shapes.DeleteClusterSecurityGroupMessage(**_params)
        response = self._boto_client.delete_cluster_security_group(
            **_request.to_boto()
        )

    def delete_cluster_snapshot(
        self,
        _request: shapes.DeleteClusterSnapshotMessage = None,
        *,
        snapshot_identifier: str,
        snapshot_cluster_identifier: str = ShapeBase.NOT_SET,
    ) -> shapes.DeleteClusterSnapshotResult:
        """
        Deletes the specified manual snapshot. The snapshot must be in the `available`
        state, with no other users authorized to access the snapshot.

        Unlike automated snapshots, manual snapshots are retained even after you delete
        your cluster. Amazon Redshift does not delete your manual snapshots. You must
        delete manual snapshot explicitly to avoid getting charged. If other accounts
        are authorized to access the snapshot, you must revoke all of the authorizations
        before you can delete the snapshot.
        """
        if _request is None:
            _params = {}
            if snapshot_identifier is not ShapeBase.NOT_SET:
                _params['snapshot_identifier'] = snapshot_identifier
            if snapshot_cluster_identifier is not ShapeBase.NOT_SET:
                _params['snapshot_cluster_identifier'
                       ] = snapshot_cluster_identifier
            _request = shapes.DeleteClusterSnapshotMessage(**_params)
        response = self._boto_client.delete_cluster_snapshot(
            **_request.to_boto()
        )

        return shapes.DeleteClusterSnapshotResult.from_boto(response)

    def delete_cluster_subnet_group(
        self,
        _request: shapes.DeleteClusterSubnetGroupMessage = None,
        *,
        cluster_subnet_group_name: str,
    ) -> None:
        """
        Deletes the specified cluster subnet group.
        """
        if _request is None:
            _params = {}
            if cluster_subnet_group_name is not ShapeBase.NOT_SET:
                _params['cluster_subnet_group_name'] = cluster_subnet_group_name
            _request = shapes.DeleteClusterSubnetGroupMessage(**_params)
        response = self._boto_client.delete_cluster_subnet_group(
            **_request.to_boto()
        )

    def delete_event_subscription(
        self,
        _request: shapes.DeleteEventSubscriptionMessage = None,
        *,
        subscription_name: str,
    ) -> None:
        """
        Deletes an Amazon Redshift event notification subscription.
        """
        if _request is None:
            _params = {}
            if subscription_name is not ShapeBase.NOT_SET:
                _params['subscription_name'] = subscription_name
            _request = shapes.DeleteEventSubscriptionMessage(**_params)
        response = self._boto_client.delete_event_subscription(
            **_request.to_boto()
        )

    def delete_hsm_client_certificate(
        self,
        _request: shapes.DeleteHsmClientCertificateMessage = None,
        *,
        hsm_client_certificate_identifier: str,
    ) -> None:
        """
        Deletes the specified HSM client certificate.
        """
        if _request is None:
            _params = {}
            if hsm_client_certificate_identifier is not ShapeBase.NOT_SET:
                _params['hsm_client_certificate_identifier'
                       ] = hsm_client_certificate_identifier
            _request = shapes.DeleteHsmClientCertificateMessage(**_params)
        response = self._boto_client.delete_hsm_client_certificate(
            **_request.to_boto()
        )

    def delete_hsm_configuration(
        self,
        _request: shapes.DeleteHsmConfigurationMessage = None,
        *,
        hsm_configuration_identifier: str,
    ) -> None:
        """
        Deletes the specified Amazon Redshift HSM configuration.
        """
        if _request is None:
            _params = {}
            if hsm_configuration_identifier is not ShapeBase.NOT_SET:
                _params['hsm_configuration_identifier'
                       ] = hsm_configuration_identifier
            _request = shapes.DeleteHsmConfigurationMessage(**_params)
        response = self._boto_client.delete_hsm_configuration(
            **_request.to_boto()
        )

    def delete_snapshot_copy_grant(
        self,
        _request: shapes.DeleteSnapshotCopyGrantMessage = None,
        *,
        snapshot_copy_grant_name: str,
    ) -> None:
        """
        Deletes the specified snapshot copy grant.
        """
        if _request is None:
            _params = {}
            if snapshot_copy_grant_name is not ShapeBase.NOT_SET:
                _params['snapshot_copy_grant_name'] = snapshot_copy_grant_name
            _request = shapes.DeleteSnapshotCopyGrantMessage(**_params)
        response = self._boto_client.delete_snapshot_copy_grant(
            **_request.to_boto()
        )

    def delete_tags(
        self,
        _request: shapes.DeleteTagsMessage = None,
        *,
        resource_name: str,
        tag_keys: typing.List[str],
    ) -> None:
        """
        Deletes a tag or tags from a resource. You must provide the ARN of the resource
        from which you want to delete the tag or tags.
        """
        if _request is None:
            _params = {}
            if resource_name is not ShapeBase.NOT_SET:
                _params['resource_name'] = resource_name
            if tag_keys is not ShapeBase.NOT_SET:
                _params['tag_keys'] = tag_keys
            _request = shapes.DeleteTagsMessage(**_params)
        response = self._boto_client.delete_tags(**_request.to_boto())

    def describe_cluster_db_revisions(
        self,
        _request: shapes.DescribeClusterDbRevisionsMessage = None,
        *,
        cluster_identifier: str = ShapeBase.NOT_SET,
        max_records: int = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
    ) -> shapes.ClusterDbRevisionsMessage:
        """
        Returns an array of `ClusterDbRevision` objects.
        """
        if _request is None:
            _params = {}
            if cluster_identifier is not ShapeBase.NOT_SET:
                _params['cluster_identifier'] = cluster_identifier
            if max_records is not ShapeBase.NOT_SET:
                _params['max_records'] = max_records
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            _request = shapes.DescribeClusterDbRevisionsMessage(**_params)
        response = self._boto_client.describe_cluster_db_revisions(
            **_request.to_boto()
        )

        return shapes.ClusterDbRevisionsMessage.from_boto(response)

    def describe_cluster_parameter_groups(
        self,
        _request: shapes.DescribeClusterParameterGroupsMessage = None,
        *,
        parameter_group_name: str = ShapeBase.NOT_SET,
        max_records: int = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
        tag_keys: typing.List[str] = ShapeBase.NOT_SET,
        tag_values: typing.List[str] = ShapeBase.NOT_SET,
    ) -> shapes.ClusterParameterGroupsMessage:
        """
        Returns a list of Amazon Redshift parameter groups, including parameter groups
        you created and the default parameter group. For each parameter group, the
        response includes the parameter group name, description, and parameter group
        family name. You can optionally specify a name to retrieve the description of a
        specific parameter group.

        For more information about parameters and parameter groups, go to [Amazon
        Redshift Parameter
        Groups](http://docs.aws.amazon.com/redshift/latest/mgmt/working-with-parameter-
        groups.html) in the _Amazon Redshift Cluster Management Guide_.

        If you specify both tag keys and tag values in the same request, Amazon Redshift
        returns all parameter groups that match any combination of the specified keys
        and values. For example, if you have `owner` and `environment` for tag keys, and
        `admin` and `test` for tag values, all parameter groups that have any
        combination of those values are returned.

        If both tag keys and values are omitted from the request, parameter groups are
        returned regardless of whether they have tag keys or values associated with
        them.
        """
        if _request is None:
            _params = {}
            if parameter_group_name is not ShapeBase.NOT_SET:
                _params['parameter_group_name'] = parameter_group_name
            if max_records is not ShapeBase.NOT_SET:
                _params['max_records'] = max_records
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            if tag_keys is not ShapeBase.NOT_SET:
                _params['tag_keys'] = tag_keys
            if tag_values is not ShapeBase.NOT_SET:
                _params['tag_values'] = tag_values
            _request = shapes.DescribeClusterParameterGroupsMessage(**_params)
        paginator = self.get_paginator("describe_cluster_parameter_groups"
                                      ).paginate(**_request.to_boto())
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ClusterParameterGroupsMessage.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ClusterParameterGroupsMessage.from_boto(response)

    def describe_cluster_parameters(
        self,
        _request: shapes.DescribeClusterParametersMessage = None,
        *,
        parameter_group_name: str,
        source: str = ShapeBase.NOT_SET,
        max_records: int = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
    ) -> shapes.ClusterParameterGroupDetails:
        """
        Returns a detailed list of parameters contained within the specified Amazon
        Redshift parameter group. For each parameter the response includes information
        such as parameter name, description, data type, value, whether the parameter
        value is modifiable, and so on.

        You can specify _source_ filter to retrieve parameters of only specific type.
        For example, to retrieve parameters that were modified by a user action such as
        from ModifyClusterParameterGroup, you can specify _source_ equal to _user_.

        For more information about parameters and parameter groups, go to [Amazon
        Redshift Parameter
        Groups](http://docs.aws.amazon.com/redshift/latest/mgmt/working-with-parameter-
        groups.html) in the _Amazon Redshift Cluster Management Guide_.
        """
        if _request is None:
            _params = {}
            if parameter_group_name is not ShapeBase.NOT_SET:
                _params['parameter_group_name'] = parameter_group_name
            if source is not ShapeBase.NOT_SET:
                _params['source'] = source
            if max_records is not ShapeBase.NOT_SET:
                _params['max_records'] = max_records
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            _request = shapes.DescribeClusterParametersMessage(**_params)
        paginator = self.get_paginator("describe_cluster_parameters").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ClusterParameterGroupDetails.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ClusterParameterGroupDetails.from_boto(response)

    def describe_cluster_security_groups(
        self,
        _request: shapes.DescribeClusterSecurityGroupsMessage = None,
        *,
        cluster_security_group_name: str = ShapeBase.NOT_SET,
        max_records: int = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
        tag_keys: typing.List[str] = ShapeBase.NOT_SET,
        tag_values: typing.List[str] = ShapeBase.NOT_SET,
    ) -> shapes.ClusterSecurityGroupMessage:
        """
        Returns information about Amazon Redshift security groups. If the name of a
        security group is specified, the response will contain only information about
        only that security group.

        For information about managing security groups, go to [Amazon Redshift Cluster
        Security Groups](http://docs.aws.amazon.com/redshift/latest/mgmt/working-with-
        security-groups.html) in the _Amazon Redshift Cluster Management Guide_.

        If you specify both tag keys and tag values in the same request, Amazon Redshift
        returns all security groups that match any combination of the specified keys and
        values. For example, if you have `owner` and `environment` for tag keys, and
        `admin` and `test` for tag values, all security groups that have any combination
        of those values are returned.

        If both tag keys and values are omitted from the request, security groups are
        returned regardless of whether they have tag keys or values associated with
        them.
        """
        if _request is None:
            _params = {}
            if cluster_security_group_name is not ShapeBase.NOT_SET:
                _params['cluster_security_group_name'
                       ] = cluster_security_group_name
            if max_records is not ShapeBase.NOT_SET:
                _params['max_records'] = max_records
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            if tag_keys is not ShapeBase.NOT_SET:
                _params['tag_keys'] = tag_keys
            if tag_values is not ShapeBase.NOT_SET:
                _params['tag_values'] = tag_values
            _request = shapes.DescribeClusterSecurityGroupsMessage(**_params)
        paginator = self.get_paginator("describe_cluster_security_groups"
                                      ).paginate(**_request.to_boto())
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ClusterSecurityGroupMessage.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ClusterSecurityGroupMessage.from_boto(response)

    def describe_cluster_snapshots(
        self,
        _request: shapes.DescribeClusterSnapshotsMessage = None,
        *,
        cluster_identifier: str = ShapeBase.NOT_SET,
        snapshot_identifier: str = ShapeBase.NOT_SET,
        snapshot_type: str = ShapeBase.NOT_SET,
        start_time: datetime.datetime = ShapeBase.NOT_SET,
        end_time: datetime.datetime = ShapeBase.NOT_SET,
        max_records: int = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
        owner_account: str = ShapeBase.NOT_SET,
        tag_keys: typing.List[str] = ShapeBase.NOT_SET,
        tag_values: typing.List[str] = ShapeBase.NOT_SET,
        cluster_exists: bool = ShapeBase.NOT_SET,
    ) -> shapes.SnapshotMessage:
        """
        Returns one or more snapshot objects, which contain metadata about your cluster
        snapshots. By default, this operation returns information about all snapshots of
        all clusters that are owned by you AWS customer account. No information is
        returned for snapshots owned by inactive AWS customer accounts.

        If you specify both tag keys and tag values in the same request, Amazon Redshift
        returns all snapshots that match any combination of the specified keys and
        values. For example, if you have `owner` and `environment` for tag keys, and
        `admin` and `test` for tag values, all snapshots that have any combination of
        those values are returned. Only snapshots that you own are returned in the
        response; shared snapshots are not returned with the tag key and tag value
        request parameters.

        If both tag keys and values are omitted from the request, snapshots are returned
        regardless of whether they have tag keys or values associated with them.
        """
        if _request is None:
            _params = {}
            if cluster_identifier is not ShapeBase.NOT_SET:
                _params['cluster_identifier'] = cluster_identifier
            if snapshot_identifier is not ShapeBase.NOT_SET:
                _params['snapshot_identifier'] = snapshot_identifier
            if snapshot_type is not ShapeBase.NOT_SET:
                _params['snapshot_type'] = snapshot_type
            if start_time is not ShapeBase.NOT_SET:
                _params['start_time'] = start_time
            if end_time is not ShapeBase.NOT_SET:
                _params['end_time'] = end_time
            if max_records is not ShapeBase.NOT_SET:
                _params['max_records'] = max_records
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            if owner_account is not ShapeBase.NOT_SET:
                _params['owner_account'] = owner_account
            if tag_keys is not ShapeBase.NOT_SET:
                _params['tag_keys'] = tag_keys
            if tag_values is not ShapeBase.NOT_SET:
                _params['tag_values'] = tag_values
            if cluster_exists is not ShapeBase.NOT_SET:
                _params['cluster_exists'] = cluster_exists
            _request = shapes.DescribeClusterSnapshotsMessage(**_params)
        paginator = self.get_paginator("describe_cluster_snapshots").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.SnapshotMessage.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.SnapshotMessage.from_boto(response)

    def describe_cluster_subnet_groups(
        self,
        _request: shapes.DescribeClusterSubnetGroupsMessage = None,
        *,
        cluster_subnet_group_name: str = ShapeBase.NOT_SET,
        max_records: int = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
        tag_keys: typing.List[str] = ShapeBase.NOT_SET,
        tag_values: typing.List[str] = ShapeBase.NOT_SET,
    ) -> shapes.ClusterSubnetGroupMessage:
        """
        Returns one or more cluster subnet group objects, which contain metadata about
        your cluster subnet groups. By default, this operation returns information about
        all cluster subnet groups that are defined in you AWS account.

        If you specify both tag keys and tag values in the same request, Amazon Redshift
        returns all subnet groups that match any combination of the specified keys and
        values. For example, if you have `owner` and `environment` for tag keys, and
        `admin` and `test` for tag values, all subnet groups that have any combination
        of those values are returned.

        If both tag keys and values are omitted from the request, subnet groups are
        returned regardless of whether they have tag keys or values associated with
        them.
        """
        if _request is None:
            _params = {}
            if cluster_subnet_group_name is not ShapeBase.NOT_SET:
                _params['cluster_subnet_group_name'] = cluster_subnet_group_name
            if max_records is not ShapeBase.NOT_SET:
                _params['max_records'] = max_records
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            if tag_keys is not ShapeBase.NOT_SET:
                _params['tag_keys'] = tag_keys
            if tag_values is not ShapeBase.NOT_SET:
                _params['tag_values'] = tag_values
            _request = shapes.DescribeClusterSubnetGroupsMessage(**_params)
        paginator = self.get_paginator("describe_cluster_subnet_groups"
                                      ).paginate(**_request.to_boto())
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ClusterSubnetGroupMessage.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ClusterSubnetGroupMessage.from_boto(response)

    def describe_cluster_tracks(
        self,
        _request: shapes.DescribeClusterTracksMessage = None,
        *,
        maintenance_track_name: str = ShapeBase.NOT_SET,
        max_records: int = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
    ) -> shapes.TrackListMessage:
        """
        Returns a list of all the available maintenance tracks.
        """
        if _request is None:
            _params = {}
            if maintenance_track_name is not ShapeBase.NOT_SET:
                _params['maintenance_track_name'] = maintenance_track_name
            if max_records is not ShapeBase.NOT_SET:
                _params['max_records'] = max_records
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            _request = shapes.DescribeClusterTracksMessage(**_params)
        response = self._boto_client.describe_cluster_tracks(
            **_request.to_boto()
        )

        return shapes.TrackListMessage.from_boto(response)

    def describe_cluster_versions(
        self,
        _request: shapes.DescribeClusterVersionsMessage = None,
        *,
        cluster_version: str = ShapeBase.NOT_SET,
        cluster_parameter_group_family: str = ShapeBase.NOT_SET,
        max_records: int = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
    ) -> shapes.ClusterVersionsMessage:
        """
        Returns descriptions of the available Amazon Redshift cluster versions. You can
        call this operation even before creating any clusters to learn more about the
        Amazon Redshift versions. For more information about managing clusters, go to
        [Amazon Redshift
        Clusters](http://docs.aws.amazon.com/redshift/latest/mgmt/working-with-
        clusters.html) in the _Amazon Redshift Cluster Management Guide_.
        """
        if _request is None:
            _params = {}
            if cluster_version is not ShapeBase.NOT_SET:
                _params['cluster_version'] = cluster_version
            if cluster_parameter_group_family is not ShapeBase.NOT_SET:
                _params['cluster_parameter_group_family'
                       ] = cluster_parameter_group_family
            if max_records is not ShapeBase.NOT_SET:
                _params['max_records'] = max_records
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            _request = shapes.DescribeClusterVersionsMessage(**_params)
        paginator = self.get_paginator("describe_cluster_versions").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ClusterVersionsMessage.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ClusterVersionsMessage.from_boto(response)

    def describe_clusters(
        self,
        _request: shapes.DescribeClustersMessage = None,
        *,
        cluster_identifier: str = ShapeBase.NOT_SET,
        max_records: int = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
        tag_keys: typing.List[str] = ShapeBase.NOT_SET,
        tag_values: typing.List[str] = ShapeBase.NOT_SET,
    ) -> shapes.ClustersMessage:
        """
        Returns properties of provisioned clusters including general cluster properties,
        cluster database properties, maintenance and backup properties, and security and
        access properties. This operation supports pagination. For more information
        about managing clusters, go to [Amazon Redshift
        Clusters](http://docs.aws.amazon.com/redshift/latest/mgmt/working-with-
        clusters.html) in the _Amazon Redshift Cluster Management Guide_.

        If you specify both tag keys and tag values in the same request, Amazon Redshift
        returns all clusters that match any combination of the specified keys and
        values. For example, if you have `owner` and `environment` for tag keys, and
        `admin` and `test` for tag values, all clusters that have any combination of
        those values are returned.

        If both tag keys and values are omitted from the request, clusters are returned
        regardless of whether they have tag keys or values associated with them.
        """
        if _request is None:
            _params = {}
            if cluster_identifier is not ShapeBase.NOT_SET:
                _params['cluster_identifier'] = cluster_identifier
            if max_records is not ShapeBase.NOT_SET:
                _params['max_records'] = max_records
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            if tag_keys is not ShapeBase.NOT_SET:
                _params['tag_keys'] = tag_keys
            if tag_values is not ShapeBase.NOT_SET:
                _params['tag_values'] = tag_values
            _request = shapes.DescribeClustersMessage(**_params)
        paginator = self.get_paginator("describe_clusters").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ClustersMessage.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ClustersMessage.from_boto(response)

    def describe_default_cluster_parameters(
        self,
        _request: shapes.DescribeDefaultClusterParametersMessage = None,
        *,
        parameter_group_family: str,
        max_records: int = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeDefaultClusterParametersResult:
        """
        Returns a list of parameter settings for the specified parameter group family.

        For more information about parameters and parameter groups, go to [Amazon
        Redshift Parameter
        Groups](http://docs.aws.amazon.com/redshift/latest/mgmt/working-with-parameter-
        groups.html) in the _Amazon Redshift Cluster Management Guide_.
        """
        if _request is None:
            _params = {}
            if parameter_group_family is not ShapeBase.NOT_SET:
                _params['parameter_group_family'] = parameter_group_family
            if max_records is not ShapeBase.NOT_SET:
                _params['max_records'] = max_records
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            _request = shapes.DescribeDefaultClusterParametersMessage(**_params)
        paginator = self.get_paginator("describe_default_cluster_parameters"
                                      ).paginate(**_request.to_boto())
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.DescribeDefaultClusterParametersResult.from_boto(
            first_page
        )
        result._page_iterator = page_generator
        return result

        return shapes.DescribeDefaultClusterParametersResult.from_boto(response)

    def describe_event_categories(
        self,
        _request: shapes.DescribeEventCategoriesMessage = None,
        *,
        source_type: str = ShapeBase.NOT_SET,
    ) -> shapes.EventCategoriesMessage:
        """
        Displays a list of event categories for all event source types, or for a
        specified source type. For a list of the event categories and source types, go
        to [Amazon Redshift Event
        Notifications](http://docs.aws.amazon.com/redshift/latest/mgmt/working-with-
        event-notifications.html).
        """
        if _request is None:
            _params = {}
            if source_type is not ShapeBase.NOT_SET:
                _params['source_type'] = source_type
            _request = shapes.DescribeEventCategoriesMessage(**_params)
        response = self._boto_client.describe_event_categories(
            **_request.to_boto()
        )

        return shapes.EventCategoriesMessage.from_boto(response)

    def describe_event_subscriptions(
        self,
        _request: shapes.DescribeEventSubscriptionsMessage = None,
        *,
        subscription_name: str = ShapeBase.NOT_SET,
        max_records: int = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
        tag_keys: typing.List[str] = ShapeBase.NOT_SET,
        tag_values: typing.List[str] = ShapeBase.NOT_SET,
    ) -> shapes.EventSubscriptionsMessage:
        """
        Lists descriptions of all the Amazon Redshift event notification subscriptions
        for a customer account. If you specify a subscription name, lists the
        description for that subscription.

        If you specify both tag keys and tag values in the same request, Amazon Redshift
        returns all event notification subscriptions that match any combination of the
        specified keys and values. For example, if you have `owner` and `environment`
        for tag keys, and `admin` and `test` for tag values, all subscriptions that have
        any combination of those values are returned.

        If both tag keys and values are omitted from the request, subscriptions are
        returned regardless of whether they have tag keys or values associated with
        them.
        """
        if _request is None:
            _params = {}
            if subscription_name is not ShapeBase.NOT_SET:
                _params['subscription_name'] = subscription_name
            if max_records is not ShapeBase.NOT_SET:
                _params['max_records'] = max_records
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            if tag_keys is not ShapeBase.NOT_SET:
                _params['tag_keys'] = tag_keys
            if tag_values is not ShapeBase.NOT_SET:
                _params['tag_values'] = tag_values
            _request = shapes.DescribeEventSubscriptionsMessage(**_params)
        paginator = self.get_paginator("describe_event_subscriptions").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.EventSubscriptionsMessage.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.EventSubscriptionsMessage.from_boto(response)

    def describe_events(
        self,
        _request: shapes.DescribeEventsMessage = None,
        *,
        source_identifier: str = ShapeBase.NOT_SET,
        source_type: typing.Union[str, shapes.SourceType] = ShapeBase.NOT_SET,
        start_time: datetime.datetime = ShapeBase.NOT_SET,
        end_time: datetime.datetime = ShapeBase.NOT_SET,
        duration: int = ShapeBase.NOT_SET,
        max_records: int = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
    ) -> shapes.EventsMessage:
        """
        Returns events related to clusters, security groups, snapshots, and parameter
        groups for the past 14 days. Events specific to a particular cluster, security
        group, snapshot or parameter group can be obtained by providing the name as a
        parameter. By default, the past hour of events are returned.
        """
        if _request is None:
            _params = {}
            if source_identifier is not ShapeBase.NOT_SET:
                _params['source_identifier'] = source_identifier
            if source_type is not ShapeBase.NOT_SET:
                _params['source_type'] = source_type
            if start_time is not ShapeBase.NOT_SET:
                _params['start_time'] = start_time
            if end_time is not ShapeBase.NOT_SET:
                _params['end_time'] = end_time
            if duration is not ShapeBase.NOT_SET:
                _params['duration'] = duration
            if max_records is not ShapeBase.NOT_SET:
                _params['max_records'] = max_records
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            _request = shapes.DescribeEventsMessage(**_params)
        paginator = self.get_paginator("describe_events").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.EventsMessage.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.EventsMessage.from_boto(response)

    def describe_hsm_client_certificates(
        self,
        _request: shapes.DescribeHsmClientCertificatesMessage = None,
        *,
        hsm_client_certificate_identifier: str = ShapeBase.NOT_SET,
        max_records: int = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
        tag_keys: typing.List[str] = ShapeBase.NOT_SET,
        tag_values: typing.List[str] = ShapeBase.NOT_SET,
    ) -> shapes.HsmClientCertificateMessage:
        """
        Returns information about the specified HSM client certificate. If no
        certificate ID is specified, returns information about all the HSM certificates
        owned by your AWS customer account.

        If you specify both tag keys and tag values in the same request, Amazon Redshift
        returns all HSM client certificates that match any combination of the specified
        keys and values. For example, if you have `owner` and `environment` for tag
        keys, and `admin` and `test` for tag values, all HSM client certificates that
        have any combination of those values are returned.

        If both tag keys and values are omitted from the request, HSM client
        certificates are returned regardless of whether they have tag keys or values
        associated with them.
        """
        if _request is None:
            _params = {}
            if hsm_client_certificate_identifier is not ShapeBase.NOT_SET:
                _params['hsm_client_certificate_identifier'
                       ] = hsm_client_certificate_identifier
            if max_records is not ShapeBase.NOT_SET:
                _params['max_records'] = max_records
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            if tag_keys is not ShapeBase.NOT_SET:
                _params['tag_keys'] = tag_keys
            if tag_values is not ShapeBase.NOT_SET:
                _params['tag_values'] = tag_values
            _request = shapes.DescribeHsmClientCertificatesMessage(**_params)
        paginator = self.get_paginator("describe_hsm_client_certificates"
                                      ).paginate(**_request.to_boto())
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.HsmClientCertificateMessage.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.HsmClientCertificateMessage.from_boto(response)

    def describe_hsm_configurations(
        self,
        _request: shapes.DescribeHsmConfigurationsMessage = None,
        *,
        hsm_configuration_identifier: str = ShapeBase.NOT_SET,
        max_records: int = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
        tag_keys: typing.List[str] = ShapeBase.NOT_SET,
        tag_values: typing.List[str] = ShapeBase.NOT_SET,
    ) -> shapes.HsmConfigurationMessage:
        """
        Returns information about the specified Amazon Redshift HSM configuration. If no
        configuration ID is specified, returns information about all the HSM
        configurations owned by your AWS customer account.

        If you specify both tag keys and tag values in the same request, Amazon Redshift
        returns all HSM connections that match any combination of the specified keys and
        values. For example, if you have `owner` and `environment` for tag keys, and
        `admin` and `test` for tag values, all HSM connections that have any combination
        of those values are returned.

        If both tag keys and values are omitted from the request, HSM connections are
        returned regardless of whether they have tag keys or values associated with
        them.
        """
        if _request is None:
            _params = {}
            if hsm_configuration_identifier is not ShapeBase.NOT_SET:
                _params['hsm_configuration_identifier'
                       ] = hsm_configuration_identifier
            if max_records is not ShapeBase.NOT_SET:
                _params['max_records'] = max_records
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            if tag_keys is not ShapeBase.NOT_SET:
                _params['tag_keys'] = tag_keys
            if tag_values is not ShapeBase.NOT_SET:
                _params['tag_values'] = tag_values
            _request = shapes.DescribeHsmConfigurationsMessage(**_params)
        paginator = self.get_paginator("describe_hsm_configurations").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.HsmConfigurationMessage.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.HsmConfigurationMessage.from_boto(response)

    def describe_logging_status(
        self,
        _request: shapes.DescribeLoggingStatusMessage = None,
        *,
        cluster_identifier: str,
    ) -> shapes.LoggingStatus:
        """
        Describes whether information, such as queries and connection attempts, is being
        logged for the specified Amazon Redshift cluster.
        """
        if _request is None:
            _params = {}
            if cluster_identifier is not ShapeBase.NOT_SET:
                _params['cluster_identifier'] = cluster_identifier
            _request = shapes.DescribeLoggingStatusMessage(**_params)
        response = self._boto_client.describe_logging_status(
            **_request.to_boto()
        )

        return shapes.LoggingStatus.from_boto(response)

    def describe_orderable_cluster_options(
        self,
        _request: shapes.DescribeOrderableClusterOptionsMessage = None,
        *,
        cluster_version: str = ShapeBase.NOT_SET,
        node_type: str = ShapeBase.NOT_SET,
        max_records: int = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
    ) -> shapes.OrderableClusterOptionsMessage:
        """
        Returns a list of orderable cluster options. Before you create a new cluster you
        can use this operation to find what options are available, such as the EC2
        Availability Zones (AZ) in the specific AWS region that you can specify, and the
        node types you can request. The node types differ by available storage, memory,
        CPU and price. With the cost involved you might want to obtain a list of cluster
        options in the specific region and specify values when creating a cluster. For
        more information about managing clusters, go to [Amazon Redshift
        Clusters](http://docs.aws.amazon.com/redshift/latest/mgmt/working-with-
        clusters.html) in the _Amazon Redshift Cluster Management Guide_.
        """
        if _request is None:
            _params = {}
            if cluster_version is not ShapeBase.NOT_SET:
                _params['cluster_version'] = cluster_version
            if node_type is not ShapeBase.NOT_SET:
                _params['node_type'] = node_type
            if max_records is not ShapeBase.NOT_SET:
                _params['max_records'] = max_records
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            _request = shapes.DescribeOrderableClusterOptionsMessage(**_params)
        paginator = self.get_paginator("describe_orderable_cluster_options"
                                      ).paginate(**_request.to_boto())
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.OrderableClusterOptionsMessage.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.OrderableClusterOptionsMessage.from_boto(response)

    def describe_reserved_node_offerings(
        self,
        _request: shapes.DescribeReservedNodeOfferingsMessage = None,
        *,
        reserved_node_offering_id: str = ShapeBase.NOT_SET,
        max_records: int = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
    ) -> shapes.ReservedNodeOfferingsMessage:
        """
        Returns a list of the available reserved node offerings by Amazon Redshift with
        their descriptions including the node type, the fixed and recurring costs of
        reserving the node and duration the node will be reserved for you. These
        descriptions help you determine which reserve node offering you want to
        purchase. You then use the unique offering ID in you call to
        PurchaseReservedNodeOffering to reserve one or more nodes for your Amazon
        Redshift cluster.

        For more information about reserved node offerings, go to [Purchasing Reserved
        Nodes](http://docs.aws.amazon.com/redshift/latest/mgmt/purchase-reserved-node-
        instance.html) in the _Amazon Redshift Cluster Management Guide_.
        """
        if _request is None:
            _params = {}
            if reserved_node_offering_id is not ShapeBase.NOT_SET:
                _params['reserved_node_offering_id'] = reserved_node_offering_id
            if max_records is not ShapeBase.NOT_SET:
                _params['max_records'] = max_records
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            _request = shapes.DescribeReservedNodeOfferingsMessage(**_params)
        paginator = self.get_paginator("describe_reserved_node_offerings"
                                      ).paginate(**_request.to_boto())
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ReservedNodeOfferingsMessage.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ReservedNodeOfferingsMessage.from_boto(response)

    def describe_reserved_nodes(
        self,
        _request: shapes.DescribeReservedNodesMessage = None,
        *,
        reserved_node_id: str = ShapeBase.NOT_SET,
        max_records: int = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
    ) -> shapes.ReservedNodesMessage:
        """
        Returns the descriptions of the reserved nodes.
        """
        if _request is None:
            _params = {}
            if reserved_node_id is not ShapeBase.NOT_SET:
                _params['reserved_node_id'] = reserved_node_id
            if max_records is not ShapeBase.NOT_SET:
                _params['max_records'] = max_records
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            _request = shapes.DescribeReservedNodesMessage(**_params)
        paginator = self.get_paginator("describe_reserved_nodes").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ReservedNodesMessage.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ReservedNodesMessage.from_boto(response)

    def describe_resize(
        self,
        _request: shapes.DescribeResizeMessage = None,
        *,
        cluster_identifier: str,
    ) -> shapes.ResizeProgressMessage:
        """
        Returns information about the last resize operation for the specified cluster.
        If no resize operation has ever been initiated for the specified cluster, a
        `HTTP 404` error is returned. If a resize operation was initiated and completed,
        the status of the resize remains as `SUCCEEDED` until the next resize.

        A resize operation can be requested using ModifyCluster and specifying a
        different number or type of nodes for the cluster.
        """
        if _request is None:
            _params = {}
            if cluster_identifier is not ShapeBase.NOT_SET:
                _params['cluster_identifier'] = cluster_identifier
            _request = shapes.DescribeResizeMessage(**_params)
        response = self._boto_client.describe_resize(**_request.to_boto())

        return shapes.ResizeProgressMessage.from_boto(response)

    def describe_snapshot_copy_grants(
        self,
        _request: shapes.DescribeSnapshotCopyGrantsMessage = None,
        *,
        snapshot_copy_grant_name: str = ShapeBase.NOT_SET,
        max_records: int = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
        tag_keys: typing.List[str] = ShapeBase.NOT_SET,
        tag_values: typing.List[str] = ShapeBase.NOT_SET,
    ) -> shapes.SnapshotCopyGrantMessage:
        """
        Returns a list of snapshot copy grants owned by the AWS account in the
        destination region.

        For more information about managing snapshot copy grants, go to [Amazon Redshift
        Database Encryption](http://docs.aws.amazon.com/redshift/latest/mgmt/working-
        with-db-encryption.html) in the _Amazon Redshift Cluster Management Guide_.
        """
        if _request is None:
            _params = {}
            if snapshot_copy_grant_name is not ShapeBase.NOT_SET:
                _params['snapshot_copy_grant_name'] = snapshot_copy_grant_name
            if max_records is not ShapeBase.NOT_SET:
                _params['max_records'] = max_records
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            if tag_keys is not ShapeBase.NOT_SET:
                _params['tag_keys'] = tag_keys
            if tag_values is not ShapeBase.NOT_SET:
                _params['tag_values'] = tag_values
            _request = shapes.DescribeSnapshotCopyGrantsMessage(**_params)
        response = self._boto_client.describe_snapshot_copy_grants(
            **_request.to_boto()
        )

        return shapes.SnapshotCopyGrantMessage.from_boto(response)

    def describe_table_restore_status(
        self,
        _request: shapes.DescribeTableRestoreStatusMessage = None,
        *,
        cluster_identifier: str = ShapeBase.NOT_SET,
        table_restore_request_id: str = ShapeBase.NOT_SET,
        max_records: int = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
    ) -> shapes.TableRestoreStatusMessage:
        """
        Lists the status of one or more table restore requests made using the
        RestoreTableFromClusterSnapshot API action. If you don't specify a value for the
        `TableRestoreRequestId` parameter, then `DescribeTableRestoreStatus` returns the
        status of all table restore requests ordered by the date and time of the request
        in ascending order. Otherwise `DescribeTableRestoreStatus` returns the status of
        the table specified by `TableRestoreRequestId`.
        """
        if _request is None:
            _params = {}
            if cluster_identifier is not ShapeBase.NOT_SET:
                _params['cluster_identifier'] = cluster_identifier
            if table_restore_request_id is not ShapeBase.NOT_SET:
                _params['table_restore_request_id'] = table_restore_request_id
            if max_records is not ShapeBase.NOT_SET:
                _params['max_records'] = max_records
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            _request = shapes.DescribeTableRestoreStatusMessage(**_params)
        response = self._boto_client.describe_table_restore_status(
            **_request.to_boto()
        )

        return shapes.TableRestoreStatusMessage.from_boto(response)

    def describe_tags(
        self,
        _request: shapes.DescribeTagsMessage = None,
        *,
        resource_name: str = ShapeBase.NOT_SET,
        resource_type: str = ShapeBase.NOT_SET,
        max_records: int = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
        tag_keys: typing.List[str] = ShapeBase.NOT_SET,
        tag_values: typing.List[str] = ShapeBase.NOT_SET,
    ) -> shapes.TaggedResourceListMessage:
        """
        Returns a list of tags. You can return tags from a specific resource by
        specifying an ARN, or you can return all tags for a given type of resource, such
        as clusters, snapshots, and so on.

        The following are limitations for `DescribeTags`:

          * You cannot specify an ARN and a resource-type value together in the same request.

          * You cannot use the `MaxRecords` and `Marker` parameters together with the ARN parameter.

          * The `MaxRecords` parameter can be a range from 10 to 50 results to return in a request.

        If you specify both tag keys and tag values in the same request, Amazon Redshift
        returns all resources that match any combination of the specified keys and
        values. For example, if you have `owner` and `environment` for tag keys, and
        `admin` and `test` for tag values, all resources that have any combination of
        those values are returned.

        If both tag keys and values are omitted from the request, resources are returned
        regardless of whether they have tag keys or values associated with them.
        """
        if _request is None:
            _params = {}
            if resource_name is not ShapeBase.NOT_SET:
                _params['resource_name'] = resource_name
            if resource_type is not ShapeBase.NOT_SET:
                _params['resource_type'] = resource_type
            if max_records is not ShapeBase.NOT_SET:
                _params['max_records'] = max_records
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            if tag_keys is not ShapeBase.NOT_SET:
                _params['tag_keys'] = tag_keys
            if tag_values is not ShapeBase.NOT_SET:
                _params['tag_values'] = tag_values
            _request = shapes.DescribeTagsMessage(**_params)
        response = self._boto_client.describe_tags(**_request.to_boto())

        return shapes.TaggedResourceListMessage.from_boto(response)

    def disable_logging(
        self,
        _request: shapes.DisableLoggingMessage = None,
        *,
        cluster_identifier: str,
    ) -> shapes.LoggingStatus:
        """
        Stops logging information, such as queries and connection attempts, for the
        specified Amazon Redshift cluster.
        """
        if _request is None:
            _params = {}
            if cluster_identifier is not ShapeBase.NOT_SET:
                _params['cluster_identifier'] = cluster_identifier
            _request = shapes.DisableLoggingMessage(**_params)
        response = self._boto_client.disable_logging(**_request.to_boto())

        return shapes.LoggingStatus.from_boto(response)

    def disable_snapshot_copy(
        self,
        _request: shapes.DisableSnapshotCopyMessage = None,
        *,
        cluster_identifier: str,
    ) -> shapes.DisableSnapshotCopyResult:
        """
        Disables the automatic copying of snapshots from one region to another region
        for a specified cluster.

        If your cluster and its snapshots are encrypted using a customer master key
        (CMK) from AWS KMS, use DeleteSnapshotCopyGrant to delete the grant that grants
        Amazon Redshift permission to the CMK in the destination region.
        """
        if _request is None:
            _params = {}
            if cluster_identifier is not ShapeBase.NOT_SET:
                _params['cluster_identifier'] = cluster_identifier
            _request = shapes.DisableSnapshotCopyMessage(**_params)
        response = self._boto_client.disable_snapshot_copy(**_request.to_boto())

        return shapes.DisableSnapshotCopyResult.from_boto(response)

    def enable_logging(
        self,
        _request: shapes.EnableLoggingMessage = None,
        *,
        cluster_identifier: str,
        bucket_name: str,
        s3_key_prefix: str = ShapeBase.NOT_SET,
    ) -> shapes.LoggingStatus:
        """
        Starts logging information, such as queries and connection attempts, for the
        specified Amazon Redshift cluster.
        """
        if _request is None:
            _params = {}
            if cluster_identifier is not ShapeBase.NOT_SET:
                _params['cluster_identifier'] = cluster_identifier
            if bucket_name is not ShapeBase.NOT_SET:
                _params['bucket_name'] = bucket_name
            if s3_key_prefix is not ShapeBase.NOT_SET:
                _params['s3_key_prefix'] = s3_key_prefix
            _request = shapes.EnableLoggingMessage(**_params)
        response = self._boto_client.enable_logging(**_request.to_boto())

        return shapes.LoggingStatus.from_boto(response)

    def enable_snapshot_copy(
        self,
        _request: shapes.EnableSnapshotCopyMessage = None,
        *,
        cluster_identifier: str,
        destination_region: str,
        retention_period: int = ShapeBase.NOT_SET,
        snapshot_copy_grant_name: str = ShapeBase.NOT_SET,
    ) -> shapes.EnableSnapshotCopyResult:
        """
        Enables the automatic copy of snapshots from one region to another region for a
        specified cluster.
        """
        if _request is None:
            _params = {}
            if cluster_identifier is not ShapeBase.NOT_SET:
                _params['cluster_identifier'] = cluster_identifier
            if destination_region is not ShapeBase.NOT_SET:
                _params['destination_region'] = destination_region
            if retention_period is not ShapeBase.NOT_SET:
                _params['retention_period'] = retention_period
            if snapshot_copy_grant_name is not ShapeBase.NOT_SET:
                _params['snapshot_copy_grant_name'] = snapshot_copy_grant_name
            _request = shapes.EnableSnapshotCopyMessage(**_params)
        response = self._boto_client.enable_snapshot_copy(**_request.to_boto())

        return shapes.EnableSnapshotCopyResult.from_boto(response)

    def get_cluster_credentials(
        self,
        _request: shapes.GetClusterCredentialsMessage = None,
        *,
        db_user: str,
        cluster_identifier: str,
        db_name: str = ShapeBase.NOT_SET,
        duration_seconds: int = ShapeBase.NOT_SET,
        auto_create: bool = ShapeBase.NOT_SET,
        db_groups: typing.List[str] = ShapeBase.NOT_SET,
    ) -> shapes.ClusterCredentials:
        """
        Returns a database user name and temporary password with temporary authorization
        to log on to an Amazon Redshift database. The action returns the database user
        name prefixed with `IAM:` if `AutoCreate` is `False` or `IAMA:` if `AutoCreate`
        is `True`. You can optionally specify one or more database user groups that the
        user will join at log on. By default, the temporary credentials expire in 900
        seconds. You can optionally specify a duration between 900 seconds (15 minutes)
        and 3600 seconds (60 minutes). For more information, see [Using IAM
        Authentication to Generate Database User
        Credentials](http://docs.aws.amazon.com/redshift/latest/mgmt/generating-user-
        credentials.html) in the Amazon Redshift Cluster Management Guide.

        The AWS Identity and Access Management (IAM)user or role that executes
        GetClusterCredentials must have an IAM policy attached that allows access to all
        necessary actions and resources. For more information about permissions, see
        [Resource Policies for
        GetClusterCredentials](http://docs.aws.amazon.com/redshift/latest/mgmt/redshift-
        iam-access-control-identity-based.html#redshift-policy-
        resources.getclustercredentials-resources) in the Amazon Redshift Cluster
        Management Guide.

        If the `DbGroups` parameter is specified, the IAM policy must allow the
        `redshift:JoinGroup` action with access to the listed `dbgroups`.

        In addition, if the `AutoCreate` parameter is set to `True`, then the policy
        must include the `redshift:CreateClusterUser` privilege.

        If the `DbName` parameter is specified, the IAM policy must allow access to the
        resource `dbname` for the specified database name.
        """
        if _request is None:
            _params = {}
            if db_user is not ShapeBase.NOT_SET:
                _params['db_user'] = db_user
            if cluster_identifier is not ShapeBase.NOT_SET:
                _params['cluster_identifier'] = cluster_identifier
            if db_name is not ShapeBase.NOT_SET:
                _params['db_name'] = db_name
            if duration_seconds is not ShapeBase.NOT_SET:
                _params['duration_seconds'] = duration_seconds
            if auto_create is not ShapeBase.NOT_SET:
                _params['auto_create'] = auto_create
            if db_groups is not ShapeBase.NOT_SET:
                _params['db_groups'] = db_groups
            _request = shapes.GetClusterCredentialsMessage(**_params)
        response = self._boto_client.get_cluster_credentials(
            **_request.to_boto()
        )

        return shapes.ClusterCredentials.from_boto(response)

    def get_reserved_node_exchange_offerings(
        self,
        _request: shapes.GetReservedNodeExchangeOfferingsInputMessage = None,
        *,
        reserved_node_id: str,
        max_records: int = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
    ) -> shapes.GetReservedNodeExchangeOfferingsOutputMessage:
        """
        Returns an array of DC2 ReservedNodeOfferings that matches the payment type,
        term, and usage price of the given DC1 reserved node.
        """
        if _request is None:
            _params = {}
            if reserved_node_id is not ShapeBase.NOT_SET:
                _params['reserved_node_id'] = reserved_node_id
            if max_records is not ShapeBase.NOT_SET:
                _params['max_records'] = max_records
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            _request = shapes.GetReservedNodeExchangeOfferingsInputMessage(
                **_params
            )
        response = self._boto_client.get_reserved_node_exchange_offerings(
            **_request.to_boto()
        )

        return shapes.GetReservedNodeExchangeOfferingsOutputMessage.from_boto(
            response
        )

    def modify_cluster(
        self,
        _request: shapes.ModifyClusterMessage = None,
        *,
        cluster_identifier: str,
        cluster_type: str = ShapeBase.NOT_SET,
        node_type: str = ShapeBase.NOT_SET,
        number_of_nodes: int = ShapeBase.NOT_SET,
        cluster_security_groups: typing.List[str] = ShapeBase.NOT_SET,
        vpc_security_group_ids: typing.List[str] = ShapeBase.NOT_SET,
        master_user_password: str = ShapeBase.NOT_SET,
        cluster_parameter_group_name: str = ShapeBase.NOT_SET,
        automated_snapshot_retention_period: int = ShapeBase.NOT_SET,
        preferred_maintenance_window: str = ShapeBase.NOT_SET,
        cluster_version: str = ShapeBase.NOT_SET,
        allow_version_upgrade: bool = ShapeBase.NOT_SET,
        hsm_client_certificate_identifier: str = ShapeBase.NOT_SET,
        hsm_configuration_identifier: str = ShapeBase.NOT_SET,
        new_cluster_identifier: str = ShapeBase.NOT_SET,
        publicly_accessible: bool = ShapeBase.NOT_SET,
        elastic_ip: str = ShapeBase.NOT_SET,
        enhanced_vpc_routing: bool = ShapeBase.NOT_SET,
        maintenance_track_name: str = ShapeBase.NOT_SET,
        encrypted: bool = ShapeBase.NOT_SET,
        kms_key_id: str = ShapeBase.NOT_SET,
    ) -> shapes.ModifyClusterResult:
        """
        Modifies the settings for a cluster. For example, you can add another security
        or parameter group, update the preferred maintenance window, or change the
        master user password. Resetting a cluster password or modifying the security
        groups associated with a cluster do not need a reboot. However, modifying a
        parameter group requires a reboot for parameters to take effect. For more
        information about managing clusters, go to [Amazon Redshift
        Clusters](http://docs.aws.amazon.com/redshift/latest/mgmt/working-with-
        clusters.html) in the _Amazon Redshift Cluster Management Guide_.

        You can also change node type and the number of nodes to scale up or down the
        cluster. When resizing a cluster, you must specify both the number of nodes and
        the node type even if one of the parameters does not change.
        """
        if _request is None:
            _params = {}
            if cluster_identifier is not ShapeBase.NOT_SET:
                _params['cluster_identifier'] = cluster_identifier
            if cluster_type is not ShapeBase.NOT_SET:
                _params['cluster_type'] = cluster_type
            if node_type is not ShapeBase.NOT_SET:
                _params['node_type'] = node_type
            if number_of_nodes is not ShapeBase.NOT_SET:
                _params['number_of_nodes'] = number_of_nodes
            if cluster_security_groups is not ShapeBase.NOT_SET:
                _params['cluster_security_groups'] = cluster_security_groups
            if vpc_security_group_ids is not ShapeBase.NOT_SET:
                _params['vpc_security_group_ids'] = vpc_security_group_ids
            if master_user_password is not ShapeBase.NOT_SET:
                _params['master_user_password'] = master_user_password
            if cluster_parameter_group_name is not ShapeBase.NOT_SET:
                _params['cluster_parameter_group_name'
                       ] = cluster_parameter_group_name
            if automated_snapshot_retention_period is not ShapeBase.NOT_SET:
                _params['automated_snapshot_retention_period'
                       ] = automated_snapshot_retention_period
            if preferred_maintenance_window is not ShapeBase.NOT_SET:
                _params['preferred_maintenance_window'
                       ] = preferred_maintenance_window
            if cluster_version is not ShapeBase.NOT_SET:
                _params['cluster_version'] = cluster_version
            if allow_version_upgrade is not ShapeBase.NOT_SET:
                _params['allow_version_upgrade'] = allow_version_upgrade
            if hsm_client_certificate_identifier is not ShapeBase.NOT_SET:
                _params['hsm_client_certificate_identifier'
                       ] = hsm_client_certificate_identifier
            if hsm_configuration_identifier is not ShapeBase.NOT_SET:
                _params['hsm_configuration_identifier'
                       ] = hsm_configuration_identifier
            if new_cluster_identifier is not ShapeBase.NOT_SET:
                _params['new_cluster_identifier'] = new_cluster_identifier
            if publicly_accessible is not ShapeBase.NOT_SET:
                _params['publicly_accessible'] = publicly_accessible
            if elastic_ip is not ShapeBase.NOT_SET:
                _params['elastic_ip'] = elastic_ip
            if enhanced_vpc_routing is not ShapeBase.NOT_SET:
                _params['enhanced_vpc_routing'] = enhanced_vpc_routing
            if maintenance_track_name is not ShapeBase.NOT_SET:
                _params['maintenance_track_name'] = maintenance_track_name
            if encrypted is not ShapeBase.NOT_SET:
                _params['encrypted'] = encrypted
            if kms_key_id is not ShapeBase.NOT_SET:
                _params['kms_key_id'] = kms_key_id
            _request = shapes.ModifyClusterMessage(**_params)
        response = self._boto_client.modify_cluster(**_request.to_boto())

        return shapes.ModifyClusterResult.from_boto(response)

    def modify_cluster_db_revision(
        self,
        _request: shapes.ModifyClusterDbRevisionMessage = None,
        *,
        cluster_identifier: str,
        revision_target: str,
    ) -> shapes.ModifyClusterDbRevisionResult:
        """
        Modifies the database revision of a cluster. The database revision is a unique
        revision of the database running in a cluster.
        """
        if _request is None:
            _params = {}
            if cluster_identifier is not ShapeBase.NOT_SET:
                _params['cluster_identifier'] = cluster_identifier
            if revision_target is not ShapeBase.NOT_SET:
                _params['revision_target'] = revision_target
            _request = shapes.ModifyClusterDbRevisionMessage(**_params)
        response = self._boto_client.modify_cluster_db_revision(
            **_request.to_boto()
        )

        return shapes.ModifyClusterDbRevisionResult.from_boto(response)

    def modify_cluster_iam_roles(
        self,
        _request: shapes.ModifyClusterIamRolesMessage = None,
        *,
        cluster_identifier: str,
        add_iam_roles: typing.List[str] = ShapeBase.NOT_SET,
        remove_iam_roles: typing.List[str] = ShapeBase.NOT_SET,
    ) -> shapes.ModifyClusterIamRolesResult:
        """
        Modifies the list of AWS Identity and Access Management (IAM) roles that can be
        used by the cluster to access other AWS services.

        A cluster can have up to 10 IAM roles associated at any time.
        """
        if _request is None:
            _params = {}
            if cluster_identifier is not ShapeBase.NOT_SET:
                _params['cluster_identifier'] = cluster_identifier
            if add_iam_roles is not ShapeBase.NOT_SET:
                _params['add_iam_roles'] = add_iam_roles
            if remove_iam_roles is not ShapeBase.NOT_SET:
                _params['remove_iam_roles'] = remove_iam_roles
            _request = shapes.ModifyClusterIamRolesMessage(**_params)
        response = self._boto_client.modify_cluster_iam_roles(
            **_request.to_boto()
        )

        return shapes.ModifyClusterIamRolesResult.from_boto(response)

    def modify_cluster_parameter_group(
        self,
        _request: shapes.ModifyClusterParameterGroupMessage = None,
        *,
        parameter_group_name: str,
        parameters: typing.List[shapes.Parameter],
    ) -> shapes.ClusterParameterGroupNameMessage:
        """
        Modifies the parameters of a parameter group.

        For more information about parameters and parameter groups, go to [Amazon
        Redshift Parameter
        Groups](http://docs.aws.amazon.com/redshift/latest/mgmt/working-with-parameter-
        groups.html) in the _Amazon Redshift Cluster Management Guide_.
        """
        if _request is None:
            _params = {}
            if parameter_group_name is not ShapeBase.NOT_SET:
                _params['parameter_group_name'] = parameter_group_name
            if parameters is not ShapeBase.NOT_SET:
                _params['parameters'] = parameters
            _request = shapes.ModifyClusterParameterGroupMessage(**_params)
        response = self._boto_client.modify_cluster_parameter_group(
            **_request.to_boto()
        )

        return shapes.ClusterParameterGroupNameMessage.from_boto(response)

    def modify_cluster_subnet_group(
        self,
        _request: shapes.ModifyClusterSubnetGroupMessage = None,
        *,
        cluster_subnet_group_name: str,
        subnet_ids: typing.List[str],
        description: str = ShapeBase.NOT_SET,
    ) -> shapes.ModifyClusterSubnetGroupResult:
        """
        Modifies a cluster subnet group to include the specified list of VPC subnets.
        The operation replaces the existing list of subnets with the new list of
        subnets.
        """
        if _request is None:
            _params = {}
            if cluster_subnet_group_name is not ShapeBase.NOT_SET:
                _params['cluster_subnet_group_name'] = cluster_subnet_group_name
            if subnet_ids is not ShapeBase.NOT_SET:
                _params['subnet_ids'] = subnet_ids
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            _request = shapes.ModifyClusterSubnetGroupMessage(**_params)
        response = self._boto_client.modify_cluster_subnet_group(
            **_request.to_boto()
        )

        return shapes.ModifyClusterSubnetGroupResult.from_boto(response)

    def modify_event_subscription(
        self,
        _request: shapes.ModifyEventSubscriptionMessage = None,
        *,
        subscription_name: str,
        sns_topic_arn: str = ShapeBase.NOT_SET,
        source_type: str = ShapeBase.NOT_SET,
        source_ids: typing.List[str] = ShapeBase.NOT_SET,
        event_categories: typing.List[str] = ShapeBase.NOT_SET,
        severity: str = ShapeBase.NOT_SET,
        enabled: bool = ShapeBase.NOT_SET,
    ) -> shapes.ModifyEventSubscriptionResult:
        """
        Modifies an existing Amazon Redshift event notification subscription.
        """
        if _request is None:
            _params = {}
            if subscription_name is not ShapeBase.NOT_SET:
                _params['subscription_name'] = subscription_name
            if sns_topic_arn is not ShapeBase.NOT_SET:
                _params['sns_topic_arn'] = sns_topic_arn
            if source_type is not ShapeBase.NOT_SET:
                _params['source_type'] = source_type
            if source_ids is not ShapeBase.NOT_SET:
                _params['source_ids'] = source_ids
            if event_categories is not ShapeBase.NOT_SET:
                _params['event_categories'] = event_categories
            if severity is not ShapeBase.NOT_SET:
                _params['severity'] = severity
            if enabled is not ShapeBase.NOT_SET:
                _params['enabled'] = enabled
            _request = shapes.ModifyEventSubscriptionMessage(**_params)
        response = self._boto_client.modify_event_subscription(
            **_request.to_boto()
        )

        return shapes.ModifyEventSubscriptionResult.from_boto(response)

    def modify_snapshot_copy_retention_period(
        self,
        _request: shapes.ModifySnapshotCopyRetentionPeriodMessage = None,
        *,
        cluster_identifier: str,
        retention_period: int,
    ) -> shapes.ModifySnapshotCopyRetentionPeriodResult:
        """
        Modifies the number of days to retain automated snapshots in the destination
        region after they are copied from the source region.
        """
        if _request is None:
            _params = {}
            if cluster_identifier is not ShapeBase.NOT_SET:
                _params['cluster_identifier'] = cluster_identifier
            if retention_period is not ShapeBase.NOT_SET:
                _params['retention_period'] = retention_period
            _request = shapes.ModifySnapshotCopyRetentionPeriodMessage(
                **_params
            )
        response = self._boto_client.modify_snapshot_copy_retention_period(
            **_request.to_boto()
        )

        return shapes.ModifySnapshotCopyRetentionPeriodResult.from_boto(
            response
        )

    def purchase_reserved_node_offering(
        self,
        _request: shapes.PurchaseReservedNodeOfferingMessage = None,
        *,
        reserved_node_offering_id: str,
        node_count: int = ShapeBase.NOT_SET,
    ) -> shapes.PurchaseReservedNodeOfferingResult:
        """
        Allows you to purchase reserved nodes. Amazon Redshift offers a predefined set
        of reserved node offerings. You can purchase one or more of the offerings. You
        can call the DescribeReservedNodeOfferings API to obtain the available reserved
        node offerings. You can call this API by providing a specific reserved node
        offering and the number of nodes you want to reserve.

        For more information about reserved node offerings, go to [Purchasing Reserved
        Nodes](http://docs.aws.amazon.com/redshift/latest/mgmt/purchase-reserved-node-
        instance.html) in the _Amazon Redshift Cluster Management Guide_.
        """
        if _request is None:
            _params = {}
            if reserved_node_offering_id is not ShapeBase.NOT_SET:
                _params['reserved_node_offering_id'] = reserved_node_offering_id
            if node_count is not ShapeBase.NOT_SET:
                _params['node_count'] = node_count
            _request = shapes.PurchaseReservedNodeOfferingMessage(**_params)
        response = self._boto_client.purchase_reserved_node_offering(
            **_request.to_boto()
        )

        return shapes.PurchaseReservedNodeOfferingResult.from_boto(response)

    def reboot_cluster(
        self,
        _request: shapes.RebootClusterMessage = None,
        *,
        cluster_identifier: str,
    ) -> shapes.RebootClusterResult:
        """
        Reboots a cluster. This action is taken as soon as possible. It results in a
        momentary outage to the cluster, during which the cluster status is set to
        `rebooting`. A cluster event is created when the reboot is completed. Any
        pending cluster modifications (see ModifyCluster) are applied at this reboot.
        For more information about managing clusters, go to [Amazon Redshift
        Clusters](http://docs.aws.amazon.com/redshift/latest/mgmt/working-with-
        clusters.html) in the _Amazon Redshift Cluster Management Guide_.
        """
        if _request is None:
            _params = {}
            if cluster_identifier is not ShapeBase.NOT_SET:
                _params['cluster_identifier'] = cluster_identifier
            _request = shapes.RebootClusterMessage(**_params)
        response = self._boto_client.reboot_cluster(**_request.to_boto())

        return shapes.RebootClusterResult.from_boto(response)

    def reset_cluster_parameter_group(
        self,
        _request: shapes.ResetClusterParameterGroupMessage = None,
        *,
        parameter_group_name: str,
        reset_all_parameters: bool = ShapeBase.NOT_SET,
        parameters: typing.List[shapes.Parameter] = ShapeBase.NOT_SET,
    ) -> shapes.ClusterParameterGroupNameMessage:
        """
        Sets one or more parameters of the specified parameter group to their default
        values and sets the source values of the parameters to "engine-default". To
        reset the entire parameter group specify the _ResetAllParameters_ parameter. For
        parameter changes to take effect you must reboot any associated clusters.
        """
        if _request is None:
            _params = {}
            if parameter_group_name is not ShapeBase.NOT_SET:
                _params['parameter_group_name'] = parameter_group_name
            if reset_all_parameters is not ShapeBase.NOT_SET:
                _params['reset_all_parameters'] = reset_all_parameters
            if parameters is not ShapeBase.NOT_SET:
                _params['parameters'] = parameters
            _request = shapes.ResetClusterParameterGroupMessage(**_params)
        response = self._boto_client.reset_cluster_parameter_group(
            **_request.to_boto()
        )

        return shapes.ClusterParameterGroupNameMessage.from_boto(response)

    def resize_cluster(
        self,
        _request: shapes.ResizeClusterMessage = None,
        *,
        cluster_identifier: str,
        number_of_nodes: int,
        cluster_type: str = ShapeBase.NOT_SET,
        node_type: str = ShapeBase.NOT_SET,
        classic: bool = ShapeBase.NOT_SET,
    ) -> shapes.ResizeClusterResult:
        """
        Changes the size of the cluster. You can change the cluster's type, or change
        the number or type of nodes. The default behavior is to use the elastic resize
        method. With an elastic resize your cluster is avaialble for read and write
        operations more quickly than with the classic resize method.

        Elastic resize operations have the following restrictions:

          * You can only resize clusters of the following types:

            * dc2.large

            * dc2.8xlarge

            * ds2.xlarge

            * ds2.8xlarge

          * The type of nodes you add must match the node type for the cluster.
        """
        if _request is None:
            _params = {}
            if cluster_identifier is not ShapeBase.NOT_SET:
                _params['cluster_identifier'] = cluster_identifier
            if number_of_nodes is not ShapeBase.NOT_SET:
                _params['number_of_nodes'] = number_of_nodes
            if cluster_type is not ShapeBase.NOT_SET:
                _params['cluster_type'] = cluster_type
            if node_type is not ShapeBase.NOT_SET:
                _params['node_type'] = node_type
            if classic is not ShapeBase.NOT_SET:
                _params['classic'] = classic
            _request = shapes.ResizeClusterMessage(**_params)
        response = self._boto_client.resize_cluster(**_request.to_boto())

        return shapes.ResizeClusterResult.from_boto(response)

    def restore_from_cluster_snapshot(
        self,
        _request: shapes.RestoreFromClusterSnapshotMessage = None,
        *,
        cluster_identifier: str,
        snapshot_identifier: str,
        snapshot_cluster_identifier: str = ShapeBase.NOT_SET,
        port: int = ShapeBase.NOT_SET,
        availability_zone: str = ShapeBase.NOT_SET,
        allow_version_upgrade: bool = ShapeBase.NOT_SET,
        cluster_subnet_group_name: str = ShapeBase.NOT_SET,
        publicly_accessible: bool = ShapeBase.NOT_SET,
        owner_account: str = ShapeBase.NOT_SET,
        hsm_client_certificate_identifier: str = ShapeBase.NOT_SET,
        hsm_configuration_identifier: str = ShapeBase.NOT_SET,
        elastic_ip: str = ShapeBase.NOT_SET,
        cluster_parameter_group_name: str = ShapeBase.NOT_SET,
        cluster_security_groups: typing.List[str] = ShapeBase.NOT_SET,
        vpc_security_group_ids: typing.List[str] = ShapeBase.NOT_SET,
        preferred_maintenance_window: str = ShapeBase.NOT_SET,
        automated_snapshot_retention_period: int = ShapeBase.NOT_SET,
        kms_key_id: str = ShapeBase.NOT_SET,
        node_type: str = ShapeBase.NOT_SET,
        enhanced_vpc_routing: bool = ShapeBase.NOT_SET,
        additional_info: str = ShapeBase.NOT_SET,
        iam_roles: typing.List[str] = ShapeBase.NOT_SET,
        maintenance_track_name: str = ShapeBase.NOT_SET,
    ) -> shapes.RestoreFromClusterSnapshotResult:
        """
        Creates a new cluster from a snapshot. By default, Amazon Redshift creates the
        resulting cluster with the same configuration as the original cluster from which
        the snapshot was created, except that the new cluster is created with the
        default cluster security and parameter groups. After Amazon Redshift creates the
        cluster, you can use the ModifyCluster API to associate a different security
        group and different parameter group with the restored cluster. If you are using
        a DS node type, you can also choose to change to another DS node type of the
        same size during restore.

        If you restore a cluster into a VPC, you must provide a cluster subnet group
        where you want the cluster restored.

        For more information about working with snapshots, go to [Amazon Redshift
        Snapshots](http://docs.aws.amazon.com/redshift/latest/mgmt/working-with-
        snapshots.html) in the _Amazon Redshift Cluster Management Guide_.
        """
        if _request is None:
            _params = {}
            if cluster_identifier is not ShapeBase.NOT_SET:
                _params['cluster_identifier'] = cluster_identifier
            if snapshot_identifier is not ShapeBase.NOT_SET:
                _params['snapshot_identifier'] = snapshot_identifier
            if snapshot_cluster_identifier is not ShapeBase.NOT_SET:
                _params['snapshot_cluster_identifier'
                       ] = snapshot_cluster_identifier
            if port is not ShapeBase.NOT_SET:
                _params['port'] = port
            if availability_zone is not ShapeBase.NOT_SET:
                _params['availability_zone'] = availability_zone
            if allow_version_upgrade is not ShapeBase.NOT_SET:
                _params['allow_version_upgrade'] = allow_version_upgrade
            if cluster_subnet_group_name is not ShapeBase.NOT_SET:
                _params['cluster_subnet_group_name'] = cluster_subnet_group_name
            if publicly_accessible is not ShapeBase.NOT_SET:
                _params['publicly_accessible'] = publicly_accessible
            if owner_account is not ShapeBase.NOT_SET:
                _params['owner_account'] = owner_account
            if hsm_client_certificate_identifier is not ShapeBase.NOT_SET:
                _params['hsm_client_certificate_identifier'
                       ] = hsm_client_certificate_identifier
            if hsm_configuration_identifier is not ShapeBase.NOT_SET:
                _params['hsm_configuration_identifier'
                       ] = hsm_configuration_identifier
            if elastic_ip is not ShapeBase.NOT_SET:
                _params['elastic_ip'] = elastic_ip
            if cluster_parameter_group_name is not ShapeBase.NOT_SET:
                _params['cluster_parameter_group_name'
                       ] = cluster_parameter_group_name
            if cluster_security_groups is not ShapeBase.NOT_SET:
                _params['cluster_security_groups'] = cluster_security_groups
            if vpc_security_group_ids is not ShapeBase.NOT_SET:
                _params['vpc_security_group_ids'] = vpc_security_group_ids
            if preferred_maintenance_window is not ShapeBase.NOT_SET:
                _params['preferred_maintenance_window'
                       ] = preferred_maintenance_window
            if automated_snapshot_retention_period is not ShapeBase.NOT_SET:
                _params['automated_snapshot_retention_period'
                       ] = automated_snapshot_retention_period
            if kms_key_id is not ShapeBase.NOT_SET:
                _params['kms_key_id'] = kms_key_id
            if node_type is not ShapeBase.NOT_SET:
                _params['node_type'] = node_type
            if enhanced_vpc_routing is not ShapeBase.NOT_SET:
                _params['enhanced_vpc_routing'] = enhanced_vpc_routing
            if additional_info is not ShapeBase.NOT_SET:
                _params['additional_info'] = additional_info
            if iam_roles is not ShapeBase.NOT_SET:
                _params['iam_roles'] = iam_roles
            if maintenance_track_name is not ShapeBase.NOT_SET:
                _params['maintenance_track_name'] = maintenance_track_name
            _request = shapes.RestoreFromClusterSnapshotMessage(**_params)
        response = self._boto_client.restore_from_cluster_snapshot(
            **_request.to_boto()
        )

        return shapes.RestoreFromClusterSnapshotResult.from_boto(response)

    def restore_table_from_cluster_snapshot(
        self,
        _request: shapes.RestoreTableFromClusterSnapshotMessage = None,
        *,
        cluster_identifier: str,
        snapshot_identifier: str,
        source_database_name: str,
        source_table_name: str,
        new_table_name: str,
        source_schema_name: str = ShapeBase.NOT_SET,
        target_database_name: str = ShapeBase.NOT_SET,
        target_schema_name: str = ShapeBase.NOT_SET,
    ) -> shapes.RestoreTableFromClusterSnapshotResult:
        """
        Creates a new table from a table in an Amazon Redshift cluster snapshot. You
        must create the new table within the Amazon Redshift cluster that the snapshot
        was taken from.

        You cannot use `RestoreTableFromClusterSnapshot` to restore a table with the
        same name as an existing table in an Amazon Redshift cluster. That is, you
        cannot overwrite an existing table in a cluster with a restored table. If you
        want to replace your original table with a new, restored table, then rename or
        drop your original table before you call `RestoreTableFromClusterSnapshot`. When
        you have renamed your original table, then you can pass the original name of the
        table as the `NewTableName` parameter value in the call to
        `RestoreTableFromClusterSnapshot`. This way, you can replace the original table
        with the table created from the snapshot.
        """
        if _request is None:
            _params = {}
            if cluster_identifier is not ShapeBase.NOT_SET:
                _params['cluster_identifier'] = cluster_identifier
            if snapshot_identifier is not ShapeBase.NOT_SET:
                _params['snapshot_identifier'] = snapshot_identifier
            if source_database_name is not ShapeBase.NOT_SET:
                _params['source_database_name'] = source_database_name
            if source_table_name is not ShapeBase.NOT_SET:
                _params['source_table_name'] = source_table_name
            if new_table_name is not ShapeBase.NOT_SET:
                _params['new_table_name'] = new_table_name
            if source_schema_name is not ShapeBase.NOT_SET:
                _params['source_schema_name'] = source_schema_name
            if target_database_name is not ShapeBase.NOT_SET:
                _params['target_database_name'] = target_database_name
            if target_schema_name is not ShapeBase.NOT_SET:
                _params['target_schema_name'] = target_schema_name
            _request = shapes.RestoreTableFromClusterSnapshotMessage(**_params)
        response = self._boto_client.restore_table_from_cluster_snapshot(
            **_request.to_boto()
        )

        return shapes.RestoreTableFromClusterSnapshotResult.from_boto(response)

    def revoke_cluster_security_group_ingress(
        self,
        _request: shapes.RevokeClusterSecurityGroupIngressMessage = None,
        *,
        cluster_security_group_name: str,
        cidrip: str = ShapeBase.NOT_SET,
        ec2_security_group_name: str = ShapeBase.NOT_SET,
        ec2_security_group_owner_id: str = ShapeBase.NOT_SET,
    ) -> shapes.RevokeClusterSecurityGroupIngressResult:
        """
        Revokes an ingress rule in an Amazon Redshift security group for a previously
        authorized IP range or Amazon EC2 security group. To add an ingress rule, see
        AuthorizeClusterSecurityGroupIngress. For information about managing security
        groups, go to [Amazon Redshift Cluster Security
        Groups](http://docs.aws.amazon.com/redshift/latest/mgmt/working-with-security-
        groups.html) in the _Amazon Redshift Cluster Management Guide_.
        """
        if _request is None:
            _params = {}
            if cluster_security_group_name is not ShapeBase.NOT_SET:
                _params['cluster_security_group_name'
                       ] = cluster_security_group_name
            if cidrip is not ShapeBase.NOT_SET:
                _params['cidrip'] = cidrip
            if ec2_security_group_name is not ShapeBase.NOT_SET:
                _params['ec2_security_group_name'] = ec2_security_group_name
            if ec2_security_group_owner_id is not ShapeBase.NOT_SET:
                _params['ec2_security_group_owner_id'
                       ] = ec2_security_group_owner_id
            _request = shapes.RevokeClusterSecurityGroupIngressMessage(
                **_params
            )
        response = self._boto_client.revoke_cluster_security_group_ingress(
            **_request.to_boto()
        )

        return shapes.RevokeClusterSecurityGroupIngressResult.from_boto(
            response
        )

    def revoke_snapshot_access(
        self,
        _request: shapes.RevokeSnapshotAccessMessage = None,
        *,
        snapshot_identifier: str,
        account_with_restore_access: str,
        snapshot_cluster_identifier: str = ShapeBase.NOT_SET,
    ) -> shapes.RevokeSnapshotAccessResult:
        """
        Removes the ability of the specified AWS customer account to restore the
        specified snapshot. If the account is currently restoring the snapshot, the
        restore will run to completion.

        For more information about working with snapshots, go to [Amazon Redshift
        Snapshots](http://docs.aws.amazon.com/redshift/latest/mgmt/working-with-
        snapshots.html) in the _Amazon Redshift Cluster Management Guide_.
        """
        if _request is None:
            _params = {}
            if snapshot_identifier is not ShapeBase.NOT_SET:
                _params['snapshot_identifier'] = snapshot_identifier
            if account_with_restore_access is not ShapeBase.NOT_SET:
                _params['account_with_restore_access'
                       ] = account_with_restore_access
            if snapshot_cluster_identifier is not ShapeBase.NOT_SET:
                _params['snapshot_cluster_identifier'
                       ] = snapshot_cluster_identifier
            _request = shapes.RevokeSnapshotAccessMessage(**_params)
        response = self._boto_client.revoke_snapshot_access(
            **_request.to_boto()
        )

        return shapes.RevokeSnapshotAccessResult.from_boto(response)

    def rotate_encryption_key(
        self,
        _request: shapes.RotateEncryptionKeyMessage = None,
        *,
        cluster_identifier: str,
    ) -> shapes.RotateEncryptionKeyResult:
        """
        Rotates the encryption keys for a cluster.
        """
        if _request is None:
            _params = {}
            if cluster_identifier is not ShapeBase.NOT_SET:
                _params['cluster_identifier'] = cluster_identifier
            _request = shapes.RotateEncryptionKeyMessage(**_params)
        response = self._boto_client.rotate_encryption_key(**_request.to_boto())

        return shapes.RotateEncryptionKeyResult.from_boto(response)
