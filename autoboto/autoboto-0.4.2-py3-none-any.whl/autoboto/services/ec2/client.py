import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("ec2", *args, **kwargs)

    def accept_reserved_instances_exchange_quote(
        self,
        _request: shapes.AcceptReservedInstancesExchangeQuoteRequest = None,
        *,
        reserved_instance_ids: typing.List[str],
        dry_run: bool = ShapeBase.NOT_SET,
        target_configurations: typing.List[shapes.TargetConfigurationRequest
                                          ] = ShapeBase.NOT_SET,
    ) -> shapes.AcceptReservedInstancesExchangeQuoteResult:
        """
        Accepts the Convertible Reserved Instance exchange quote described in the
        GetReservedInstancesExchangeQuote call.
        """
        if _request is None:
            _params = {}
            if reserved_instance_ids is not ShapeBase.NOT_SET:
                _params['reserved_instance_ids'] = reserved_instance_ids
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            if target_configurations is not ShapeBase.NOT_SET:
                _params['target_configurations'] = target_configurations
            _request = shapes.AcceptReservedInstancesExchangeQuoteRequest(
                **_params
            )
        response = self._boto_client.accept_reserved_instances_exchange_quote(
            **_request.to_boto()
        )

        return shapes.AcceptReservedInstancesExchangeQuoteResult.from_boto(
            response
        )

    def accept_vpc_endpoint_connections(
        self,
        _request: shapes.AcceptVpcEndpointConnectionsRequest = None,
        *,
        service_id: str,
        vpc_endpoint_ids: typing.List[str],
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> shapes.AcceptVpcEndpointConnectionsResult:
        """
        Accepts one or more interface VPC endpoint connection requests to your VPC
        endpoint service.
        """
        if _request is None:
            _params = {}
            if service_id is not ShapeBase.NOT_SET:
                _params['service_id'] = service_id
            if vpc_endpoint_ids is not ShapeBase.NOT_SET:
                _params['vpc_endpoint_ids'] = vpc_endpoint_ids
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.AcceptVpcEndpointConnectionsRequest(**_params)
        response = self._boto_client.accept_vpc_endpoint_connections(
            **_request.to_boto()
        )

        return shapes.AcceptVpcEndpointConnectionsResult.from_boto(response)

    def accept_vpc_peering_connection(
        self,
        _request: shapes.AcceptVpcPeeringConnectionRequest = None,
        *,
        dry_run: bool = ShapeBase.NOT_SET,
        vpc_peering_connection_id: str = ShapeBase.NOT_SET,
    ) -> shapes.AcceptVpcPeeringConnectionResult:
        """
        Accept a VPC peering connection request. To accept a request, the VPC peering
        connection must be in the `pending-acceptance` state, and you must be the owner
        of the peer VPC. Use DescribeVpcPeeringConnections to view your outstanding VPC
        peering connection requests.

        For an inter-region VPC peering connection request, you must accept the VPC
        peering connection in the region of the accepter VPC.
        """
        if _request is None:
            _params = {}
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            if vpc_peering_connection_id is not ShapeBase.NOT_SET:
                _params['vpc_peering_connection_id'] = vpc_peering_connection_id
            _request = shapes.AcceptVpcPeeringConnectionRequest(**_params)
        response = self._boto_client.accept_vpc_peering_connection(
            **_request.to_boto()
        )

        return shapes.AcceptVpcPeeringConnectionResult.from_boto(response)

    def allocate_address(
        self,
        _request: shapes.AllocateAddressRequest = None,
        *,
        domain: typing.Union[str, shapes.DomainType] = ShapeBase.NOT_SET,
        address: str = ShapeBase.NOT_SET,
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> shapes.AllocateAddressResult:
        """
        Allocates an Elastic IP address to your AWS account. After you allocate the
        Elastic IP address you can associate it with an instance or network interface.
        After you release an Elastic IP address, it is released to the IP address pool
        and can be allocated to a different AWS account.

        [EC2-VPC] If you release an Elastic IP address, you might be able to recover it.
        You cannot recover an Elastic IP address that you released after it is allocated
        to another AWS account. You cannot recover an Elastic IP address for
        EC2-Classic. To attempt to recover an Elastic IP address that you released,
        specify it in this operation.

        An Elastic IP address is for use either in the EC2-Classic platform or in a VPC.
        By default, you can allocate 5 Elastic IP addresses for EC2-Classic per region
        and 5 Elastic IP addresses for EC2-VPC per region.

        For more information, see [Elastic IP
        Addresses](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-
        addresses-eip.html) in the _Amazon Elastic Compute Cloud User Guide_.
        """
        if _request is None:
            _params = {}
            if domain is not ShapeBase.NOT_SET:
                _params['domain'] = domain
            if address is not ShapeBase.NOT_SET:
                _params['address'] = address
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.AllocateAddressRequest(**_params)
        response = self._boto_client.allocate_address(**_request.to_boto())

        return shapes.AllocateAddressResult.from_boto(response)

    def allocate_hosts(
        self,
        _request: shapes.AllocateHostsRequest = None,
        *,
        availability_zone: str,
        instance_type: str,
        quantity: int,
        auto_placement: typing.Union[str, shapes.AutoPlacement] = ShapeBase.
        NOT_SET,
        client_token: str = ShapeBase.NOT_SET,
    ) -> shapes.AllocateHostsResult:
        """
        Allocates a Dedicated Host to your account. At a minimum, specify the instance
        size type, Availability Zone, and quantity of hosts to allocate.
        """
        if _request is None:
            _params = {}
            if availability_zone is not ShapeBase.NOT_SET:
                _params['availability_zone'] = availability_zone
            if instance_type is not ShapeBase.NOT_SET:
                _params['instance_type'] = instance_type
            if quantity is not ShapeBase.NOT_SET:
                _params['quantity'] = quantity
            if auto_placement is not ShapeBase.NOT_SET:
                _params['auto_placement'] = auto_placement
            if client_token is not ShapeBase.NOT_SET:
                _params['client_token'] = client_token
            _request = shapes.AllocateHostsRequest(**_params)
        response = self._boto_client.allocate_hosts(**_request.to_boto())

        return shapes.AllocateHostsResult.from_boto(response)

    def assign_ipv6_addresses(
        self,
        _request: shapes.AssignIpv6AddressesRequest = None,
        *,
        network_interface_id: str,
        ipv6_address_count: int = ShapeBase.NOT_SET,
        ipv6_addresses: typing.List[str] = ShapeBase.NOT_SET,
    ) -> shapes.AssignIpv6AddressesResult:
        """
        Assigns one or more IPv6 addresses to the specified network interface. You can
        specify one or more specific IPv6 addresses, or you can specify the number of
        IPv6 addresses to be automatically assigned from within the subnet's IPv6 CIDR
        block range. You can assign as many IPv6 addresses to a network interface as you
        can assign private IPv4 addresses, and the limit varies per instance type. For
        information, see [IP Addresses Per Network Interface Per Instance
        Type](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-
        eni.html#AvailableIpPerENI) in the _Amazon Elastic Compute Cloud User Guide_.
        """
        if _request is None:
            _params = {}
            if network_interface_id is not ShapeBase.NOT_SET:
                _params['network_interface_id'] = network_interface_id
            if ipv6_address_count is not ShapeBase.NOT_SET:
                _params['ipv6_address_count'] = ipv6_address_count
            if ipv6_addresses is not ShapeBase.NOT_SET:
                _params['ipv6_addresses'] = ipv6_addresses
            _request = shapes.AssignIpv6AddressesRequest(**_params)
        response = self._boto_client.assign_ipv6_addresses(**_request.to_boto())

        return shapes.AssignIpv6AddressesResult.from_boto(response)

    def assign_private_ip_addresses(
        self,
        _request: shapes.AssignPrivateIpAddressesRequest = None,
        *,
        network_interface_id: str,
        allow_reassignment: bool = ShapeBase.NOT_SET,
        private_ip_addresses: typing.List[str] = ShapeBase.NOT_SET,
        secondary_private_ip_address_count: int = ShapeBase.NOT_SET,
    ) -> None:
        """
        Assigns one or more secondary private IP addresses to the specified network
        interface. You can specify one or more specific secondary IP addresses, or you
        can specify the number of secondary IP addresses to be automatically assigned
        within the subnet's CIDR block range. The number of secondary IP addresses that
        you can assign to an instance varies by instance type. For information about
        instance types, see [Instance
        Types](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html)
        in the _Amazon Elastic Compute Cloud User Guide_. For more information about
        Elastic IP addresses, see [Elastic IP
        Addresses](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-
        addresses-eip.html) in the _Amazon Elastic Compute Cloud User Guide_.

        AssignPrivateIpAddresses is available only in EC2-VPC.
        """
        if _request is None:
            _params = {}
            if network_interface_id is not ShapeBase.NOT_SET:
                _params['network_interface_id'] = network_interface_id
            if allow_reassignment is not ShapeBase.NOT_SET:
                _params['allow_reassignment'] = allow_reassignment
            if private_ip_addresses is not ShapeBase.NOT_SET:
                _params['private_ip_addresses'] = private_ip_addresses
            if secondary_private_ip_address_count is not ShapeBase.NOT_SET:
                _params['secondary_private_ip_address_count'
                       ] = secondary_private_ip_address_count
            _request = shapes.AssignPrivateIpAddressesRequest(**_params)
        response = self._boto_client.assign_private_ip_addresses(
            **_request.to_boto()
        )

    def associate_address(
        self,
        _request: shapes.AssociateAddressRequest = None,
        *,
        allocation_id: str = ShapeBase.NOT_SET,
        instance_id: str = ShapeBase.NOT_SET,
        public_ip: str = ShapeBase.NOT_SET,
        allow_reassociation: bool = ShapeBase.NOT_SET,
        dry_run: bool = ShapeBase.NOT_SET,
        network_interface_id: str = ShapeBase.NOT_SET,
        private_ip_address: str = ShapeBase.NOT_SET,
    ) -> shapes.AssociateAddressResult:
        """
        Associates an Elastic IP address with an instance or a network interface. Before
        you can use an Elastic IP address, you must allocate it to your account.

        An Elastic IP address is for use in either the EC2-Classic platform or in a VPC.
        For more information, see [Elastic IP
        Addresses](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-
        addresses-eip.html) in the _Amazon Elastic Compute Cloud User Guide_.

        [EC2-Classic, VPC in an EC2-VPC-only account] If the Elastic IP address is
        already associated with a different instance, it is disassociated from that
        instance and associated with the specified instance. If you associate an Elastic
        IP address with an instance that has an existing Elastic IP address, the
        existing address is disassociated from the instance, but remains allocated to
        your account.

        [VPC in an EC2-Classic account] If you don't specify a private IP address, the
        Elastic IP address is associated with the primary IP address. If the Elastic IP
        address is already associated with a different instance or a network interface,
        you get an error unless you allow reassociation. You cannot associate an Elastic
        IP address with an instance or network interface that has an existing Elastic IP
        address.

        This is an idempotent operation. If you perform the operation more than once,
        Amazon EC2 doesn't return an error, and you may be charged for each time the
        Elastic IP address is remapped to the same instance. For more information, see
        the _Elastic IP Addresses_ section of [Amazon EC2
        Pricing](http://aws.amazon.com/ec2/pricing/).
        """
        if _request is None:
            _params = {}
            if allocation_id is not ShapeBase.NOT_SET:
                _params['allocation_id'] = allocation_id
            if instance_id is not ShapeBase.NOT_SET:
                _params['instance_id'] = instance_id
            if public_ip is not ShapeBase.NOT_SET:
                _params['public_ip'] = public_ip
            if allow_reassociation is not ShapeBase.NOT_SET:
                _params['allow_reassociation'] = allow_reassociation
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            if network_interface_id is not ShapeBase.NOT_SET:
                _params['network_interface_id'] = network_interface_id
            if private_ip_address is not ShapeBase.NOT_SET:
                _params['private_ip_address'] = private_ip_address
            _request = shapes.AssociateAddressRequest(**_params)
        response = self._boto_client.associate_address(**_request.to_boto())

        return shapes.AssociateAddressResult.from_boto(response)

    def associate_dhcp_options(
        self,
        _request: shapes.AssociateDhcpOptionsRequest = None,
        *,
        dhcp_options_id: str,
        vpc_id: str,
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> None:
        """
        Associates a set of DHCP options (that you've previously created) with the
        specified VPC, or associates no DHCP options with the VPC.

        After you associate the options with the VPC, any existing instances and all new
        instances that you launch in that VPC use the options. You don't need to restart
        or relaunch the instances. They automatically pick up the changes within a few
        hours, depending on how frequently the instance renews its DHCP lease. You can
        explicitly renew the lease using the operating system on the instance.

        For more information, see [DHCP Options
        Sets](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_DHCP_Options.html)
        in the _Amazon Virtual Private Cloud User Guide_.
        """
        if _request is None:
            _params = {}
            if dhcp_options_id is not ShapeBase.NOT_SET:
                _params['dhcp_options_id'] = dhcp_options_id
            if vpc_id is not ShapeBase.NOT_SET:
                _params['vpc_id'] = vpc_id
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.AssociateDhcpOptionsRequest(**_params)
        response = self._boto_client.associate_dhcp_options(
            **_request.to_boto()
        )

    def associate_iam_instance_profile(
        self,
        _request: shapes.AssociateIamInstanceProfileRequest = None,
        *,
        iam_instance_profile: shapes.IamInstanceProfileSpecification,
        instance_id: str,
    ) -> shapes.AssociateIamInstanceProfileResult:
        """
        Associates an IAM instance profile with a running or stopped instance. You
        cannot associate more than one IAM instance profile with an instance.
        """
        if _request is None:
            _params = {}
            if iam_instance_profile is not ShapeBase.NOT_SET:
                _params['iam_instance_profile'] = iam_instance_profile
            if instance_id is not ShapeBase.NOT_SET:
                _params['instance_id'] = instance_id
            _request = shapes.AssociateIamInstanceProfileRequest(**_params)
        response = self._boto_client.associate_iam_instance_profile(
            **_request.to_boto()
        )

        return shapes.AssociateIamInstanceProfileResult.from_boto(response)

    def associate_route_table(
        self,
        _request: shapes.AssociateRouteTableRequest = None,
        *,
        route_table_id: str,
        subnet_id: str,
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> shapes.AssociateRouteTableResult:
        """
        Associates a subnet with a route table. The subnet and route table must be in
        the same VPC. This association causes traffic originating from the subnet to be
        routed according to the routes in the route table. The action returns an
        association ID, which you need in order to disassociate the route table from the
        subnet later. A route table can be associated with multiple subnets.

        For more information, see [Route
        Tables](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Route_Tables.html)
        in the _Amazon Virtual Private Cloud User Guide_.
        """
        if _request is None:
            _params = {}
            if route_table_id is not ShapeBase.NOT_SET:
                _params['route_table_id'] = route_table_id
            if subnet_id is not ShapeBase.NOT_SET:
                _params['subnet_id'] = subnet_id
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.AssociateRouteTableRequest(**_params)
        response = self._boto_client.associate_route_table(**_request.to_boto())

        return shapes.AssociateRouteTableResult.from_boto(response)

    def associate_subnet_cidr_block(
        self,
        _request: shapes.AssociateSubnetCidrBlockRequest = None,
        *,
        ipv6_cidr_block: str,
        subnet_id: str,
    ) -> shapes.AssociateSubnetCidrBlockResult:
        """
        Associates a CIDR block with your subnet. You can only associate a single IPv6
        CIDR block with your subnet. An IPv6 CIDR block must have a prefix length of
        /64.
        """
        if _request is None:
            _params = {}
            if ipv6_cidr_block is not ShapeBase.NOT_SET:
                _params['ipv6_cidr_block'] = ipv6_cidr_block
            if subnet_id is not ShapeBase.NOT_SET:
                _params['subnet_id'] = subnet_id
            _request = shapes.AssociateSubnetCidrBlockRequest(**_params)
        response = self._boto_client.associate_subnet_cidr_block(
            **_request.to_boto()
        )

        return shapes.AssociateSubnetCidrBlockResult.from_boto(response)

    def associate_vpc_cidr_block(
        self,
        _request: shapes.AssociateVpcCidrBlockRequest = None,
        *,
        vpc_id: str,
        amazon_provided_ipv6_cidr_block: bool = ShapeBase.NOT_SET,
        cidr_block: str = ShapeBase.NOT_SET,
    ) -> shapes.AssociateVpcCidrBlockResult:
        """
        Associates a CIDR block with your VPC. You can associate a secondary IPv4 CIDR
        block, or you can associate an Amazon-provided IPv6 CIDR block. The IPv6 CIDR
        block size is fixed at /56.

        For more information about associating CIDR blocks with your VPC and applicable
        restrictions, see [VPC and Subnet
        Sizing](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Subnets.html#VPC_Sizing)
        in the _Amazon Virtual Private Cloud User Guide_.
        """
        if _request is None:
            _params = {}
            if vpc_id is not ShapeBase.NOT_SET:
                _params['vpc_id'] = vpc_id
            if amazon_provided_ipv6_cidr_block is not ShapeBase.NOT_SET:
                _params['amazon_provided_ipv6_cidr_block'
                       ] = amazon_provided_ipv6_cidr_block
            if cidr_block is not ShapeBase.NOT_SET:
                _params['cidr_block'] = cidr_block
            _request = shapes.AssociateVpcCidrBlockRequest(**_params)
        response = self._boto_client.associate_vpc_cidr_block(
            **_request.to_boto()
        )

        return shapes.AssociateVpcCidrBlockResult.from_boto(response)

    def attach_classic_link_vpc(
        self,
        _request: shapes.AttachClassicLinkVpcRequest = None,
        *,
        groups: typing.List[str],
        instance_id: str,
        vpc_id: str,
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> shapes.AttachClassicLinkVpcResult:
        """
        Links an EC2-Classic instance to a ClassicLink-enabled VPC through one or more
        of the VPC's security groups. You cannot link an EC2-Classic instance to more
        than one VPC at a time. You can only link an instance that's in the `running`
        state. An instance is automatically unlinked from a VPC when it's stopped - you
        can link it to the VPC again when you restart it.

        After you've linked an instance, you cannot change the VPC security groups that
        are associated with it. To change the security groups, you must first unlink the
        instance, and then link it again.

        Linking your instance to a VPC is sometimes referred to as _attaching_ your
        instance.
        """
        if _request is None:
            _params = {}
            if groups is not ShapeBase.NOT_SET:
                _params['groups'] = groups
            if instance_id is not ShapeBase.NOT_SET:
                _params['instance_id'] = instance_id
            if vpc_id is not ShapeBase.NOT_SET:
                _params['vpc_id'] = vpc_id
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.AttachClassicLinkVpcRequest(**_params)
        response = self._boto_client.attach_classic_link_vpc(
            **_request.to_boto()
        )

        return shapes.AttachClassicLinkVpcResult.from_boto(response)

    def attach_internet_gateway(
        self,
        _request: shapes.AttachInternetGatewayRequest = None,
        *,
        internet_gateway_id: str,
        vpc_id: str,
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> None:
        """
        Attaches an internet gateway to a VPC, enabling connectivity between the
        internet and the VPC. For more information about your VPC and internet gateway,
        see the [Amazon Virtual Private Cloud User
        Guide](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/).
        """
        if _request is None:
            _params = {}
            if internet_gateway_id is not ShapeBase.NOT_SET:
                _params['internet_gateway_id'] = internet_gateway_id
            if vpc_id is not ShapeBase.NOT_SET:
                _params['vpc_id'] = vpc_id
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.AttachInternetGatewayRequest(**_params)
        response = self._boto_client.attach_internet_gateway(
            **_request.to_boto()
        )

    def attach_network_interface(
        self,
        _request: shapes.AttachNetworkInterfaceRequest = None,
        *,
        device_index: int,
        instance_id: str,
        network_interface_id: str,
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> shapes.AttachNetworkInterfaceResult:
        """
        Attaches a network interface to an instance.
        """
        if _request is None:
            _params = {}
            if device_index is not ShapeBase.NOT_SET:
                _params['device_index'] = device_index
            if instance_id is not ShapeBase.NOT_SET:
                _params['instance_id'] = instance_id
            if network_interface_id is not ShapeBase.NOT_SET:
                _params['network_interface_id'] = network_interface_id
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.AttachNetworkInterfaceRequest(**_params)
        response = self._boto_client.attach_network_interface(
            **_request.to_boto()
        )

        return shapes.AttachNetworkInterfaceResult.from_boto(response)

    def attach_volume(
        self,
        _request: shapes.AttachVolumeRequest = None,
        *,
        device: str,
        instance_id: str,
        volume_id: str,
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> shapes.VolumeAttachment:
        """
        Attaches an EBS volume to a running or stopped instance and exposes it to the
        instance with the specified device name.

        Encrypted EBS volumes may only be attached to instances that support Amazon EBS
        encryption. For more information, see [Amazon EBS
        Encryption](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html)
        in the _Amazon Elastic Compute Cloud User Guide_.

        For a list of supported device names, see [Attaching an EBS Volume to an
        Instance](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-attaching-
        volume.html). Any device names that aren't reserved for instance store volumes
        can be used for EBS volumes. For more information, see [Amazon EC2 Instance
        Store](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html)
        in the _Amazon Elastic Compute Cloud User Guide_.

        If a volume has an AWS Marketplace product code:

          * The volume can be attached only to a stopped instance.

          * AWS Marketplace product codes are copied from the volume to the instance.

          * You must be subscribed to the product.

          * The instance type and operating system of the instance must support the product. For example, you can't detach a volume from a Windows instance and attach it to a Linux instance.

        For more information about EBS volumes, see [Attaching Amazon EBS
        Volumes](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-attaching-
        volume.html) in the _Amazon Elastic Compute Cloud User Guide_.
        """
        if _request is None:
            _params = {}
            if device is not ShapeBase.NOT_SET:
                _params['device'] = device
            if instance_id is not ShapeBase.NOT_SET:
                _params['instance_id'] = instance_id
            if volume_id is not ShapeBase.NOT_SET:
                _params['volume_id'] = volume_id
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.AttachVolumeRequest(**_params)
        response = self._boto_client.attach_volume(**_request.to_boto())

        return shapes.VolumeAttachment.from_boto(response)

    def attach_vpn_gateway(
        self,
        _request: shapes.AttachVpnGatewayRequest = None,
        *,
        vpc_id: str,
        vpn_gateway_id: str,
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> shapes.AttachVpnGatewayResult:
        """
        Attaches a virtual private gateway to a VPC. You can attach one virtual private
        gateway to one VPC at a time.

        For more information, see [AWS Managed VPN
        Connections](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_VPN.html)
        in the _Amazon Virtual Private Cloud User Guide_.
        """
        if _request is None:
            _params = {}
            if vpc_id is not ShapeBase.NOT_SET:
                _params['vpc_id'] = vpc_id
            if vpn_gateway_id is not ShapeBase.NOT_SET:
                _params['vpn_gateway_id'] = vpn_gateway_id
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.AttachVpnGatewayRequest(**_params)
        response = self._boto_client.attach_vpn_gateway(**_request.to_boto())

        return shapes.AttachVpnGatewayResult.from_boto(response)

    def authorize_security_group_egress(
        self,
        _request: shapes.AuthorizeSecurityGroupEgressRequest = None,
        *,
        group_id: str,
        dry_run: bool = ShapeBase.NOT_SET,
        ip_permissions: typing.List[shapes.IpPermission] = ShapeBase.NOT_SET,
        cidr_ip: str = ShapeBase.NOT_SET,
        from_port: int = ShapeBase.NOT_SET,
        ip_protocol: str = ShapeBase.NOT_SET,
        to_port: int = ShapeBase.NOT_SET,
        source_security_group_name: str = ShapeBase.NOT_SET,
        source_security_group_owner_id: str = ShapeBase.NOT_SET,
    ) -> None:
        """
        [EC2-VPC only] Adds one or more egress rules to a security group for use with a
        VPC. Specifically, this action permits instances to send traffic to one or more
        destination IPv4 or IPv6 CIDR address ranges, or to one or more destination
        security groups for the same VPC. This action doesn't apply to security groups
        for use in EC2-Classic. For more information, see [Security Groups for Your
        VPC](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_SecurityGroups.html)
        in the _Amazon Virtual Private Cloud User Guide_. For more information about
        security group limits, see [Amazon VPC
        Limits](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Appendix_Limits.html).

        Each rule consists of the protocol (for example, TCP), plus either a CIDR range
        or a source group. For the TCP and UDP protocols, you must also specify the
        destination port or port range. For the ICMP protocol, you must also specify the
        ICMP type and code. You can use -1 for the type or code to mean all types or all
        codes. You can optionally specify a description for the rule.

        Rule changes are propagated to affected instances as quickly as possible.
        However, a small delay might occur.
        """
        if _request is None:
            _params = {}
            if group_id is not ShapeBase.NOT_SET:
                _params['group_id'] = group_id
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            if ip_permissions is not ShapeBase.NOT_SET:
                _params['ip_permissions'] = ip_permissions
            if cidr_ip is not ShapeBase.NOT_SET:
                _params['cidr_ip'] = cidr_ip
            if from_port is not ShapeBase.NOT_SET:
                _params['from_port'] = from_port
            if ip_protocol is not ShapeBase.NOT_SET:
                _params['ip_protocol'] = ip_protocol
            if to_port is not ShapeBase.NOT_SET:
                _params['to_port'] = to_port
            if source_security_group_name is not ShapeBase.NOT_SET:
                _params['source_security_group_name'
                       ] = source_security_group_name
            if source_security_group_owner_id is not ShapeBase.NOT_SET:
                _params['source_security_group_owner_id'
                       ] = source_security_group_owner_id
            _request = shapes.AuthorizeSecurityGroupEgressRequest(**_params)
        response = self._boto_client.authorize_security_group_egress(
            **_request.to_boto()
        )

    def authorize_security_group_ingress(
        self,
        _request: shapes.AuthorizeSecurityGroupIngressRequest = None,
        *,
        cidr_ip: str = ShapeBase.NOT_SET,
        from_port: int = ShapeBase.NOT_SET,
        group_id: str = ShapeBase.NOT_SET,
        group_name: str = ShapeBase.NOT_SET,
        ip_permissions: typing.List[shapes.IpPermission] = ShapeBase.NOT_SET,
        ip_protocol: str = ShapeBase.NOT_SET,
        source_security_group_name: str = ShapeBase.NOT_SET,
        source_security_group_owner_id: str = ShapeBase.NOT_SET,
        to_port: int = ShapeBase.NOT_SET,
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> None:
        """
        Adds one or more ingress rules to a security group.

        Rule changes are propagated to instances within the security group as quickly as
        possible. However, a small delay might occur.

        [EC2-Classic] This action gives one or more IPv4 CIDR address ranges permission
        to access a security group in your account, or gives one or more security groups
        (called the _source groups_ ) permission to access a security group for your
        account. A source group can be for your own AWS account, or another. You can
        have up to 100 rules per group.

        [EC2-VPC] This action gives one or more IPv4 or IPv6 CIDR address ranges
        permission to access a security group in your VPC, or gives one or more other
        security groups (called the _source groups_ ) permission to access a security
        group for your VPC. The security groups must all be for the same VPC or a peer
        VPC in a VPC peering connection. For more information about VPC security group
        limits, see [Amazon VPC
        Limits](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Appendix_Limits.html).

        You can optionally specify a description for the security group rule.
        """
        if _request is None:
            _params = {}
            if cidr_ip is not ShapeBase.NOT_SET:
                _params['cidr_ip'] = cidr_ip
            if from_port is not ShapeBase.NOT_SET:
                _params['from_port'] = from_port
            if group_id is not ShapeBase.NOT_SET:
                _params['group_id'] = group_id
            if group_name is not ShapeBase.NOT_SET:
                _params['group_name'] = group_name
            if ip_permissions is not ShapeBase.NOT_SET:
                _params['ip_permissions'] = ip_permissions
            if ip_protocol is not ShapeBase.NOT_SET:
                _params['ip_protocol'] = ip_protocol
            if source_security_group_name is not ShapeBase.NOT_SET:
                _params['source_security_group_name'
                       ] = source_security_group_name
            if source_security_group_owner_id is not ShapeBase.NOT_SET:
                _params['source_security_group_owner_id'
                       ] = source_security_group_owner_id
            if to_port is not ShapeBase.NOT_SET:
                _params['to_port'] = to_port
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.AuthorizeSecurityGroupIngressRequest(**_params)
        response = self._boto_client.authorize_security_group_ingress(
            **_request.to_boto()
        )

    def bundle_instance(
        self,
        _request: shapes.BundleInstanceRequest = None,
        *,
        instance_id: str,
        storage: shapes.Storage,
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> shapes.BundleInstanceResult:
        """
        Bundles an Amazon instance store-backed Windows instance.

        During bundling, only the root device volume (C:\\) is bundled. Data on other
        instance store volumes is not preserved.

        This action is not applicable for Linux/Unix instances or Windows instances that
        are backed by Amazon EBS.
        """
        if _request is None:
            _params = {}
            if instance_id is not ShapeBase.NOT_SET:
                _params['instance_id'] = instance_id
            if storage is not ShapeBase.NOT_SET:
                _params['storage'] = storage
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.BundleInstanceRequest(**_params)
        response = self._boto_client.bundle_instance(**_request.to_boto())

        return shapes.BundleInstanceResult.from_boto(response)

    def cancel_bundle_task(
        self,
        _request: shapes.CancelBundleTaskRequest = None,
        *,
        bundle_id: str,
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> shapes.CancelBundleTaskResult:
        """
        Cancels a bundling operation for an instance store-backed Windows instance.
        """
        if _request is None:
            _params = {}
            if bundle_id is not ShapeBase.NOT_SET:
                _params['bundle_id'] = bundle_id
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.CancelBundleTaskRequest(**_params)
        response = self._boto_client.cancel_bundle_task(**_request.to_boto())

        return shapes.CancelBundleTaskResult.from_boto(response)

    def cancel_conversion_task(
        self,
        _request: shapes.CancelConversionRequest = None,
        *,
        conversion_task_id: str,
        dry_run: bool = ShapeBase.NOT_SET,
        reason_message: str = ShapeBase.NOT_SET,
    ) -> None:
        """
        Cancels an active conversion task. The task can be the import of an instance or
        volume. The action removes all artifacts of the conversion, including a
        partially uploaded volume or instance. If the conversion is complete or is in
        the process of transferring the final disk image, the command fails and returns
        an exception.

        For more information, see [Importing a Virtual Machine Using the Amazon EC2
        CLI](http://docs.aws.amazon.com/AWSEC2/latest/CommandLineReference/ec2-cli-
        vmimport-export.html).
        """
        if _request is None:
            _params = {}
            if conversion_task_id is not ShapeBase.NOT_SET:
                _params['conversion_task_id'] = conversion_task_id
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            if reason_message is not ShapeBase.NOT_SET:
                _params['reason_message'] = reason_message
            _request = shapes.CancelConversionRequest(**_params)
        response = self._boto_client.cancel_conversion_task(
            **_request.to_boto()
        )

    def cancel_export_task(
        self,
        _request: shapes.CancelExportTaskRequest = None,
        *,
        export_task_id: str,
    ) -> None:
        """
        Cancels an active export task. The request removes all artifacts of the export,
        including any partially-created Amazon S3 objects. If the export task is
        complete or is in the process of transferring the final disk image, the command
        fails and returns an error.
        """
        if _request is None:
            _params = {}
            if export_task_id is not ShapeBase.NOT_SET:
                _params['export_task_id'] = export_task_id
            _request = shapes.CancelExportTaskRequest(**_params)
        response = self._boto_client.cancel_export_task(**_request.to_boto())

    def cancel_import_task(
        self,
        _request: shapes.CancelImportTaskRequest = None,
        *,
        cancel_reason: str = ShapeBase.NOT_SET,
        dry_run: bool = ShapeBase.NOT_SET,
        import_task_id: str = ShapeBase.NOT_SET,
    ) -> shapes.CancelImportTaskResult:
        """
        Cancels an in-process import virtual machine or import snapshot task.
        """
        if _request is None:
            _params = {}
            if cancel_reason is not ShapeBase.NOT_SET:
                _params['cancel_reason'] = cancel_reason
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            if import_task_id is not ShapeBase.NOT_SET:
                _params['import_task_id'] = import_task_id
            _request = shapes.CancelImportTaskRequest(**_params)
        response = self._boto_client.cancel_import_task(**_request.to_boto())

        return shapes.CancelImportTaskResult.from_boto(response)

    def cancel_reserved_instances_listing(
        self,
        _request: shapes.CancelReservedInstancesListingRequest = None,
        *,
        reserved_instances_listing_id: str,
    ) -> shapes.CancelReservedInstancesListingResult:
        """
        Cancels the specified Reserved Instance listing in the Reserved Instance
        Marketplace.

        For more information, see [Reserved Instance
        Marketplace](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ri-market-
        general.html) in the _Amazon Elastic Compute Cloud User Guide_.
        """
        if _request is None:
            _params = {}
            if reserved_instances_listing_id is not ShapeBase.NOT_SET:
                _params['reserved_instances_listing_id'
                       ] = reserved_instances_listing_id
            _request = shapes.CancelReservedInstancesListingRequest(**_params)
        response = self._boto_client.cancel_reserved_instances_listing(
            **_request.to_boto()
        )

        return shapes.CancelReservedInstancesListingResult.from_boto(response)

    def cancel_spot_fleet_requests(
        self,
        _request: shapes.CancelSpotFleetRequestsRequest = None,
        *,
        spot_fleet_request_ids: typing.List[str],
        terminate_instances: bool,
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> shapes.CancelSpotFleetRequestsResponse:
        """
        Cancels the specified Spot Fleet requests.

        After you cancel a Spot Fleet request, the Spot Fleet launches no new Spot
        Instances. You must specify whether the Spot Fleet should also terminate its
        Spot Instances. If you terminate the instances, the Spot Fleet request enters
        the `cancelled_terminating` state. Otherwise, the Spot Fleet request enters the
        `cancelled_running` state and the instances continue to run until they are
        interrupted or you terminate them manually.
        """
        if _request is None:
            _params = {}
            if spot_fleet_request_ids is not ShapeBase.NOT_SET:
                _params['spot_fleet_request_ids'] = spot_fleet_request_ids
            if terminate_instances is not ShapeBase.NOT_SET:
                _params['terminate_instances'] = terminate_instances
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.CancelSpotFleetRequestsRequest(**_params)
        response = self._boto_client.cancel_spot_fleet_requests(
            **_request.to_boto()
        )

        return shapes.CancelSpotFleetRequestsResponse.from_boto(response)

    def cancel_spot_instance_requests(
        self,
        _request: shapes.CancelSpotInstanceRequestsRequest = None,
        *,
        spot_instance_request_ids: typing.List[str],
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> shapes.CancelSpotInstanceRequestsResult:
        """
        Cancels one or more Spot Instance requests.

        Canceling a Spot Instance request does not terminate running Spot Instances
        associated with the request.
        """
        if _request is None:
            _params = {}
            if spot_instance_request_ids is not ShapeBase.NOT_SET:
                _params['spot_instance_request_ids'] = spot_instance_request_ids
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.CancelSpotInstanceRequestsRequest(**_params)
        response = self._boto_client.cancel_spot_instance_requests(
            **_request.to_boto()
        )

        return shapes.CancelSpotInstanceRequestsResult.from_boto(response)

    def confirm_product_instance(
        self,
        _request: shapes.ConfirmProductInstanceRequest = None,
        *,
        instance_id: str,
        product_code: str,
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> shapes.ConfirmProductInstanceResult:
        """
        Determines whether a product code is associated with an instance. This action
        can only be used by the owner of the product code. It is useful when a product
        code owner must verify whether another user's instance is eligible for support.
        """
        if _request is None:
            _params = {}
            if instance_id is not ShapeBase.NOT_SET:
                _params['instance_id'] = instance_id
            if product_code is not ShapeBase.NOT_SET:
                _params['product_code'] = product_code
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.ConfirmProductInstanceRequest(**_params)
        response = self._boto_client.confirm_product_instance(
            **_request.to_boto()
        )

        return shapes.ConfirmProductInstanceResult.from_boto(response)

    def copy_fpga_image(
        self,
        _request: shapes.CopyFpgaImageRequest = None,
        *,
        source_fpga_image_id: str,
        source_region: str,
        dry_run: bool = ShapeBase.NOT_SET,
        description: str = ShapeBase.NOT_SET,
        name: str = ShapeBase.NOT_SET,
        client_token: str = ShapeBase.NOT_SET,
    ) -> shapes.CopyFpgaImageResult:
        """
        Copies the specified Amazon FPGA Image (AFI) to the current region.
        """
        if _request is None:
            _params = {}
            if source_fpga_image_id is not ShapeBase.NOT_SET:
                _params['source_fpga_image_id'] = source_fpga_image_id
            if source_region is not ShapeBase.NOT_SET:
                _params['source_region'] = source_region
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if client_token is not ShapeBase.NOT_SET:
                _params['client_token'] = client_token
            _request = shapes.CopyFpgaImageRequest(**_params)
        response = self._boto_client.copy_fpga_image(**_request.to_boto())

        return shapes.CopyFpgaImageResult.from_boto(response)

    def copy_image(
        self,
        _request: shapes.CopyImageRequest = None,
        *,
        name: str,
        source_image_id: str,
        source_region: str,
        client_token: str = ShapeBase.NOT_SET,
        description: str = ShapeBase.NOT_SET,
        encrypted: bool = ShapeBase.NOT_SET,
        kms_key_id: str = ShapeBase.NOT_SET,
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> shapes.CopyImageResult:
        """
        Initiates the copy of an AMI from the specified source region to the current
        region. You specify the destination region by using its endpoint when making the
        request.

        Copies of encrypted backing snapshots for the AMI are encrypted. Copies of
        unencrypted backing snapshots remain unencrypted, unless you set `Encrypted`
        during the copy operation. You cannot create an unencrypted copy of an encrypted
        backing snapshot.

        For more information about the prerequisites and limits when copying an AMI, see
        [Copying an
        AMI](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/CopyingAMIs.html) in the
        _Amazon Elastic Compute Cloud User Guide_.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if source_image_id is not ShapeBase.NOT_SET:
                _params['source_image_id'] = source_image_id
            if source_region is not ShapeBase.NOT_SET:
                _params['source_region'] = source_region
            if client_token is not ShapeBase.NOT_SET:
                _params['client_token'] = client_token
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if encrypted is not ShapeBase.NOT_SET:
                _params['encrypted'] = encrypted
            if kms_key_id is not ShapeBase.NOT_SET:
                _params['kms_key_id'] = kms_key_id
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.CopyImageRequest(**_params)
        response = self._boto_client.copy_image(**_request.to_boto())

        return shapes.CopyImageResult.from_boto(response)

    def copy_snapshot(
        self,
        _request: shapes.CopySnapshotRequest = None,
        *,
        source_region: str,
        source_snapshot_id: str,
        description: str = ShapeBase.NOT_SET,
        destination_region: str = ShapeBase.NOT_SET,
        encrypted: bool = ShapeBase.NOT_SET,
        kms_key_id: str = ShapeBase.NOT_SET,
        presigned_url: str = ShapeBase.NOT_SET,
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> shapes.CopySnapshotResult:
        """
        Copies a point-in-time snapshot of an EBS volume and stores it in Amazon S3. You
        can copy the snapshot within the same region or from one region to another. You
        can use the snapshot to create EBS volumes or Amazon Machine Images (AMIs). The
        snapshot is copied to the regional endpoint that you send the HTTP request to.

        Copies of encrypted EBS snapshots remain encrypted. Copies of unencrypted
        snapshots remain unencrypted, unless the `Encrypted` flag is specified during
        the snapshot copy operation. By default, encrypted snapshot copies use the
        default AWS Key Management Service (AWS KMS) customer master key (CMK); however,
        you can specify a non-default CMK with the `KmsKeyId` parameter.

        To copy an encrypted snapshot that has been shared from another account, you
        must have permissions for the CMK used to encrypt the snapshot.

        Snapshots created by copying another snapshot have an arbitrary volume ID that
        should not be used for any purpose.

        For more information, see [Copying an Amazon EBS
        Snapshot](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-copy-
        snapshot.html) in the _Amazon Elastic Compute Cloud User Guide_.
        """
        if _request is None:
            _params = {}
            if source_region is not ShapeBase.NOT_SET:
                _params['source_region'] = source_region
            if source_snapshot_id is not ShapeBase.NOT_SET:
                _params['source_snapshot_id'] = source_snapshot_id
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if destination_region is not ShapeBase.NOT_SET:
                _params['destination_region'] = destination_region
            if encrypted is not ShapeBase.NOT_SET:
                _params['encrypted'] = encrypted
            if kms_key_id is not ShapeBase.NOT_SET:
                _params['kms_key_id'] = kms_key_id
            if presigned_url is not ShapeBase.NOT_SET:
                _params['presigned_url'] = presigned_url
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.CopySnapshotRequest(**_params)
        response = self._boto_client.copy_snapshot(**_request.to_boto())

        return shapes.CopySnapshotResult.from_boto(response)

    def create_customer_gateway(
        self,
        _request: shapes.CreateCustomerGatewayRequest = None,
        *,
        bgp_asn: int,
        public_ip: str,
        type: typing.Union[str, shapes.GatewayType],
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> shapes.CreateCustomerGatewayResult:
        """
        Provides information to AWS about your VPN customer gateway device. The customer
        gateway is the appliance at your end of the VPN connection. (The device on the
        AWS side of the VPN connection is the virtual private gateway.) You must provide
        the Internet-routable IP address of the customer gateway's external interface.
        The IP address must be static and may be behind a device performing network
        address translation (NAT).

        For devices that use Border Gateway Protocol (BGP), you can also provide the
        device's BGP Autonomous System Number (ASN). You can use an existing ASN
        assigned to your network. If you don't have an ASN already, you can use a
        private ASN (in the 64512 - 65534 range).

        Amazon EC2 supports all 2-byte ASN numbers in the range of 1 - 65534, with the
        exception of 7224, which is reserved in the `us-east-1` region, and 9059, which
        is reserved in the `eu-west-1` region.

        For more information about VPN customer gateways, see [AWS Managed VPN
        Connections](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_VPN.html)
        in the _Amazon Virtual Private Cloud User Guide_.

        You cannot create more than one customer gateway with the same VPN type, IP
        address, and BGP ASN parameter values. If you run an identical request more than
        one time, the first request creates the customer gateway, and subsequent
        requests return information about the existing customer gateway. The subsequent
        requests do not create new customer gateway resources.
        """
        if _request is None:
            _params = {}
            if bgp_asn is not ShapeBase.NOT_SET:
                _params['bgp_asn'] = bgp_asn
            if public_ip is not ShapeBase.NOT_SET:
                _params['public_ip'] = public_ip
            if type is not ShapeBase.NOT_SET:
                _params['type'] = type
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.CreateCustomerGatewayRequest(**_params)
        response = self._boto_client.create_customer_gateway(
            **_request.to_boto()
        )

        return shapes.CreateCustomerGatewayResult.from_boto(response)

    def create_default_subnet(
        self,
        _request: shapes.CreateDefaultSubnetRequest = None,
        *,
        availability_zone: str,
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> shapes.CreateDefaultSubnetResult:
        """
        Creates a default subnet with a size `/20` IPv4 CIDR block in the specified
        Availability Zone in your default VPC. You can have only one default subnet per
        Availability Zone. For more information, see [Creating a Default
        Subnet](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/default-
        vpc.html#create-default-subnet) in the _Amazon Virtual Private Cloud User
        Guide_.
        """
        if _request is None:
            _params = {}
            if availability_zone is not ShapeBase.NOT_SET:
                _params['availability_zone'] = availability_zone
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.CreateDefaultSubnetRequest(**_params)
        response = self._boto_client.create_default_subnet(**_request.to_boto())

        return shapes.CreateDefaultSubnetResult.from_boto(response)

    def create_default_vpc(
        self,
        _request: shapes.CreateDefaultVpcRequest = None,
        *,
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> shapes.CreateDefaultVpcResult:
        """
        Creates a default VPC with a size `/16` IPv4 CIDR block and a default subnet in
        each Availability Zone. For more information about the components of a default
        VPC, see [Default VPC and Default
        Subnets](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/default-vpc.html)
        in the _Amazon Virtual Private Cloud User Guide_. You cannot specify the
        components of the default VPC yourself.

        If you deleted your previous default VPC, you can create a default VPC. You
        cannot have more than one default VPC per Region.

        If your account supports EC2-Classic, you cannot use this action to create a
        default VPC in a Region that supports EC2-Classic. If you want a default VPC in
        a Region that supports EC2-Classic, see "I really want a default VPC for my
        existing EC2 account. Is that possible?" in the [Default VPCs
        FAQ](http://aws.amazon.com/vpc/faqs/#Default_VPCs).
        """
        if _request is None:
            _params = {}
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.CreateDefaultVpcRequest(**_params)
        response = self._boto_client.create_default_vpc(**_request.to_boto())

        return shapes.CreateDefaultVpcResult.from_boto(response)

    def create_dhcp_options(
        self,
        _request: shapes.CreateDhcpOptionsRequest = None,
        *,
        dhcp_configurations: typing.List[shapes.NewDhcpConfiguration],
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> shapes.CreateDhcpOptionsResult:
        """
        Creates a set of DHCP options for your VPC. After creating the set, you must
        associate it with the VPC, causing all existing and new instances that you
        launch in the VPC to use this set of DHCP options. The following are the
        individual DHCP options you can specify. For more information about the options,
        see [RFC 2132](http://www.ietf.org/rfc/rfc2132.txt).

          * `domain-name-servers` \- The IP addresses of up to four domain name servers, or AmazonProvidedDNS. The default DHCP option set specifies AmazonProvidedDNS. If specifying more than one domain name server, specify the IP addresses in a single parameter, separated by commas. ITo have your instance to receive a custom DNS hostname as specified in `domain-name`, you must set `domain-name-servers` to a custom DNS server.

          * `domain-name` \- If you're using AmazonProvidedDNS in `us-east-1`, specify `ec2.internal`. If you're using AmazonProvidedDNS in another region, specify `region.compute.internal` (for example, `ap-northeast-1.compute.internal`). Otherwise, specify a domain name (for example, `MyCompany.com`). This value is used to complete unqualified DNS hostnames. **Important** : Some Linux operating systems accept multiple domain names separated by spaces. However, Windows and other Linux operating systems treat the value as a single domain, which results in unexpected behavior. If your DHCP options set is associated with a VPC that has instances with multiple operating systems, specify only one domain name.

          * `ntp-servers` \- The IP addresses of up to four Network Time Protocol (NTP) servers.

          * `netbios-name-servers` \- The IP addresses of up to four NetBIOS name servers.

          * `netbios-node-type` \- The NetBIOS node type (1, 2, 4, or 8). We recommend that you specify 2 (broadcast and multicast are not currently supported). For more information about these node types, see [RFC 2132](http://www.ietf.org/rfc/rfc2132.txt).

        Your VPC automatically starts out with a set of DHCP options that includes only
        a DNS server that we provide (AmazonProvidedDNS). If you create a set of
        options, and if your VPC has an internet gateway, make sure to set the `domain-
        name-servers` option either to `AmazonProvidedDNS` or to a domain name server of
        your choice. For more information, see [DHCP Options
        Sets](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_DHCP_Options.html)
        in the _Amazon Virtual Private Cloud User Guide_.
        """
        if _request is None:
            _params = {}
            if dhcp_configurations is not ShapeBase.NOT_SET:
                _params['dhcp_configurations'] = dhcp_configurations
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.CreateDhcpOptionsRequest(**_params)
        response = self._boto_client.create_dhcp_options(**_request.to_boto())

        return shapes.CreateDhcpOptionsResult.from_boto(response)

    def create_egress_only_internet_gateway(
        self,
        _request: shapes.CreateEgressOnlyInternetGatewayRequest = None,
        *,
        vpc_id: str,
        client_token: str = ShapeBase.NOT_SET,
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> shapes.CreateEgressOnlyInternetGatewayResult:
        """
        [IPv6 only] Creates an egress-only internet gateway for your VPC. An egress-only
        internet gateway is used to enable outbound communication over IPv6 from
        instances in your VPC to the internet, and prevents hosts outside of your VPC
        from initiating an IPv6 connection with your instance.
        """
        if _request is None:
            _params = {}
            if vpc_id is not ShapeBase.NOT_SET:
                _params['vpc_id'] = vpc_id
            if client_token is not ShapeBase.NOT_SET:
                _params['client_token'] = client_token
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.CreateEgressOnlyInternetGatewayRequest(**_params)
        response = self._boto_client.create_egress_only_internet_gateway(
            **_request.to_boto()
        )

        return shapes.CreateEgressOnlyInternetGatewayResult.from_boto(response)

    def create_fleet(
        self,
        _request: shapes.CreateFleetRequest = None,
        *,
        launch_template_configs: typing.List[shapes.
                                             FleetLaunchTemplateConfigRequest],
        target_capacity_specification: shapes.
        TargetCapacitySpecificationRequest,
        dry_run: bool = ShapeBase.NOT_SET,
        client_token: str = ShapeBase.NOT_SET,
        spot_options: shapes.SpotOptionsRequest = ShapeBase.NOT_SET,
        on_demand_options: shapes.OnDemandOptionsRequest = ShapeBase.NOT_SET,
        excess_capacity_termination_policy: typing.
        Union[str, shapes.
              FleetExcessCapacityTerminationPolicy] = ShapeBase.NOT_SET,
        terminate_instances_with_expiration: bool = ShapeBase.NOT_SET,
        type: typing.Union[str, shapes.FleetType] = ShapeBase.NOT_SET,
        valid_from: datetime.datetime = ShapeBase.NOT_SET,
        valid_until: datetime.datetime = ShapeBase.NOT_SET,
        replace_unhealthy_instances: bool = ShapeBase.NOT_SET,
        tag_specifications: typing.List[shapes.TagSpecification
                                       ] = ShapeBase.NOT_SET,
    ) -> shapes.CreateFleetResult:
        """
        Launches an EC2 Fleet.

        You can create a single EC2 Fleet that includes multiple launch specifications
        that vary by instance type, AMI, Availability Zone, or subnet.

        For more information, see [Launching an EC2
        Fleet](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-fleet.html) in the
        _Amazon Elastic Compute Cloud User Guide_.
        """
        if _request is None:
            _params = {}
            if launch_template_configs is not ShapeBase.NOT_SET:
                _params['launch_template_configs'] = launch_template_configs
            if target_capacity_specification is not ShapeBase.NOT_SET:
                _params['target_capacity_specification'
                       ] = target_capacity_specification
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            if client_token is not ShapeBase.NOT_SET:
                _params['client_token'] = client_token
            if spot_options is not ShapeBase.NOT_SET:
                _params['spot_options'] = spot_options
            if on_demand_options is not ShapeBase.NOT_SET:
                _params['on_demand_options'] = on_demand_options
            if excess_capacity_termination_policy is not ShapeBase.NOT_SET:
                _params['excess_capacity_termination_policy'
                       ] = excess_capacity_termination_policy
            if terminate_instances_with_expiration is not ShapeBase.NOT_SET:
                _params['terminate_instances_with_expiration'
                       ] = terminate_instances_with_expiration
            if type is not ShapeBase.NOT_SET:
                _params['type'] = type
            if valid_from is not ShapeBase.NOT_SET:
                _params['valid_from'] = valid_from
            if valid_until is not ShapeBase.NOT_SET:
                _params['valid_until'] = valid_until
            if replace_unhealthy_instances is not ShapeBase.NOT_SET:
                _params['replace_unhealthy_instances'
                       ] = replace_unhealthy_instances
            if tag_specifications is not ShapeBase.NOT_SET:
                _params['tag_specifications'] = tag_specifications
            _request = shapes.CreateFleetRequest(**_params)
        response = self._boto_client.create_fleet(**_request.to_boto())

        return shapes.CreateFleetResult.from_boto(response)

    def create_flow_logs(
        self,
        _request: shapes.CreateFlowLogsRequest = None,
        *,
        resource_ids: typing.List[str],
        resource_type: typing.Union[str, shapes.FlowLogsResourceType],
        traffic_type: typing.Union[str, shapes.TrafficType],
        dry_run: bool = ShapeBase.NOT_SET,
        client_token: str = ShapeBase.NOT_SET,
        deliver_logs_permission_arn: str = ShapeBase.NOT_SET,
        log_group_name: str = ShapeBase.NOT_SET,
        log_destination_type: typing.
        Union[str, shapes.LogDestinationType] = ShapeBase.NOT_SET,
        log_destination: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateFlowLogsResult:
        """
        Creates one or more flow logs to capture information about IP traffic for a
        specific network interface, subnet, or VPC.

        Flow log data for a monitored network interface is recorded as flow log records,
        which are log events consisting of fields that describe the traffic flow. For
        more information, see [Flow Log
        Records](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/flow-
        logs.html#flow-log-records) in the _Amazon Virtual Private Cloud User Guide_.

        When publishing to CloudWatch Logs, flow log records are published to a log
        group, and each network interface has a unique log stream in the log group. When
        publishing to Amazon S3, flow log records for all of the monitored network
        interfaces are published to a single log file object that is stored in the
        specified bucket.

        For more information, see [VPC Flow
        Logs](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/flow-logs.html) in
        the _Amazon Virtual Private Cloud User Guide_.
        """
        if _request is None:
            _params = {}
            if resource_ids is not ShapeBase.NOT_SET:
                _params['resource_ids'] = resource_ids
            if resource_type is not ShapeBase.NOT_SET:
                _params['resource_type'] = resource_type
            if traffic_type is not ShapeBase.NOT_SET:
                _params['traffic_type'] = traffic_type
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            if client_token is not ShapeBase.NOT_SET:
                _params['client_token'] = client_token
            if deliver_logs_permission_arn is not ShapeBase.NOT_SET:
                _params['deliver_logs_permission_arn'
                       ] = deliver_logs_permission_arn
            if log_group_name is not ShapeBase.NOT_SET:
                _params['log_group_name'] = log_group_name
            if log_destination_type is not ShapeBase.NOT_SET:
                _params['log_destination_type'] = log_destination_type
            if log_destination is not ShapeBase.NOT_SET:
                _params['log_destination'] = log_destination
            _request = shapes.CreateFlowLogsRequest(**_params)
        response = self._boto_client.create_flow_logs(**_request.to_boto())

        return shapes.CreateFlowLogsResult.from_boto(response)

    def create_fpga_image(
        self,
        _request: shapes.CreateFpgaImageRequest = None,
        *,
        input_storage_location: shapes.StorageLocation,
        dry_run: bool = ShapeBase.NOT_SET,
        logs_storage_location: shapes.StorageLocation = ShapeBase.NOT_SET,
        description: str = ShapeBase.NOT_SET,
        name: str = ShapeBase.NOT_SET,
        client_token: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateFpgaImageResult:
        """
        Creates an Amazon FPGA Image (AFI) from the specified design checkpoint (DCP).

        The create operation is asynchronous. To verify that the AFI is ready for use,
        check the output logs.

        An AFI contains the FPGA bitstream that is ready to download to an FPGA. You can
        securely deploy an AFI on one or more FPGA-accelerated instances. For more
        information, see the [AWS FPGA Hardware Development
        Kit](https://github.com/aws/aws-fpga/).
        """
        if _request is None:
            _params = {}
            if input_storage_location is not ShapeBase.NOT_SET:
                _params['input_storage_location'] = input_storage_location
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            if logs_storage_location is not ShapeBase.NOT_SET:
                _params['logs_storage_location'] = logs_storage_location
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if client_token is not ShapeBase.NOT_SET:
                _params['client_token'] = client_token
            _request = shapes.CreateFpgaImageRequest(**_params)
        response = self._boto_client.create_fpga_image(**_request.to_boto())

        return shapes.CreateFpgaImageResult.from_boto(response)

    def create_image(
        self,
        _request: shapes.CreateImageRequest = None,
        *,
        instance_id: str,
        name: str,
        block_device_mappings: typing.List[shapes.BlockDeviceMapping
                                          ] = ShapeBase.NOT_SET,
        description: str = ShapeBase.NOT_SET,
        dry_run: bool = ShapeBase.NOT_SET,
        no_reboot: bool = ShapeBase.NOT_SET,
    ) -> shapes.CreateImageResult:
        """
        Creates an Amazon EBS-backed AMI from an Amazon EBS-backed instance that is
        either running or stopped.

        If you customized your instance with instance store volumes or EBS volumes in
        addition to the root device volume, the new AMI contains block device mapping
        information for those volumes. When you launch an instance from this new AMI,
        the instance automatically launches with those additional volumes.

        For more information, see [Creating Amazon EBS-Backed Linux
        AMIs](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/creating-an-ami-
        ebs.html) in the _Amazon Elastic Compute Cloud User Guide_.
        """
        if _request is None:
            _params = {}
            if instance_id is not ShapeBase.NOT_SET:
                _params['instance_id'] = instance_id
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if block_device_mappings is not ShapeBase.NOT_SET:
                _params['block_device_mappings'] = block_device_mappings
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            if no_reboot is not ShapeBase.NOT_SET:
                _params['no_reboot'] = no_reboot
            _request = shapes.CreateImageRequest(**_params)
        response = self._boto_client.create_image(**_request.to_boto())

        return shapes.CreateImageResult.from_boto(response)

    def create_instance_export_task(
        self,
        _request: shapes.CreateInstanceExportTaskRequest = None,
        *,
        instance_id: str,
        description: str = ShapeBase.NOT_SET,
        export_to_s3_task: shapes.ExportToS3TaskSpecification = ShapeBase.
        NOT_SET,
        target_environment: typing.Union[str, shapes.
                                         ExportEnvironment] = ShapeBase.NOT_SET,
    ) -> shapes.CreateInstanceExportTaskResult:
        """
        Exports a running or stopped instance to an S3 bucket.

        For information about the supported operating systems, image formats, and known
        limitations for the types of instances you can export, see [Exporting an
        Instance as a VM Using VM Import/Export](http://docs.aws.amazon.com/vm-
        import/latest/userguide/vmexport.html) in the _VM Import/Export User Guide_.
        """
        if _request is None:
            _params = {}
            if instance_id is not ShapeBase.NOT_SET:
                _params['instance_id'] = instance_id
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if export_to_s3_task is not ShapeBase.NOT_SET:
                _params['export_to_s3_task'] = export_to_s3_task
            if target_environment is not ShapeBase.NOT_SET:
                _params['target_environment'] = target_environment
            _request = shapes.CreateInstanceExportTaskRequest(**_params)
        response = self._boto_client.create_instance_export_task(
            **_request.to_boto()
        )

        return shapes.CreateInstanceExportTaskResult.from_boto(response)

    def create_internet_gateway(
        self,
        _request: shapes.CreateInternetGatewayRequest = None,
        *,
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> shapes.CreateInternetGatewayResult:
        """
        Creates an internet gateway for use with a VPC. After creating the internet
        gateway, you attach it to a VPC using AttachInternetGateway.

        For more information about your VPC and internet gateway, see the [Amazon
        Virtual Private Cloud User
        Guide](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/).
        """
        if _request is None:
            _params = {}
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.CreateInternetGatewayRequest(**_params)
        response = self._boto_client.create_internet_gateway(
            **_request.to_boto()
        )

        return shapes.CreateInternetGatewayResult.from_boto(response)

    def create_key_pair(
        self,
        _request: shapes.CreateKeyPairRequest = None,
        *,
        key_name: str,
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> shapes.KeyPair:
        """
        Creates a 2048-bit RSA key pair with the specified name. Amazon EC2 stores the
        public key and displays the private key for you to save to a file. The private
        key is returned as an unencrypted PEM encoded PKCS#1 private key. If a key with
        the specified name already exists, Amazon EC2 returns an error.

        You can have up to five thousand key pairs per region.

        The key pair returned to you is available only in the region in which you create
        it. If you prefer, you can create your own key pair using a third-party tool and
        upload it to any region using ImportKeyPair.

        For more information, see [Key
        Pairs](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html) in
        the _Amazon Elastic Compute Cloud User Guide_.
        """
        if _request is None:
            _params = {}
            if key_name is not ShapeBase.NOT_SET:
                _params['key_name'] = key_name
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.CreateKeyPairRequest(**_params)
        response = self._boto_client.create_key_pair(**_request.to_boto())

        return shapes.KeyPair.from_boto(response)

    def create_launch_template(
        self,
        _request: shapes.CreateLaunchTemplateRequest = None,
        *,
        launch_template_name: str,
        launch_template_data: shapes.RequestLaunchTemplateData,
        dry_run: bool = ShapeBase.NOT_SET,
        client_token: str = ShapeBase.NOT_SET,
        version_description: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateLaunchTemplateResult:
        """
        Creates a launch template. A launch template contains the parameters to launch
        an instance. When you launch an instance using RunInstances, you can specify a
        launch template instead of providing the launch parameters in the request.
        """
        if _request is None:
            _params = {}
            if launch_template_name is not ShapeBase.NOT_SET:
                _params['launch_template_name'] = launch_template_name
            if launch_template_data is not ShapeBase.NOT_SET:
                _params['launch_template_data'] = launch_template_data
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            if client_token is not ShapeBase.NOT_SET:
                _params['client_token'] = client_token
            if version_description is not ShapeBase.NOT_SET:
                _params['version_description'] = version_description
            _request = shapes.CreateLaunchTemplateRequest(**_params)
        response = self._boto_client.create_launch_template(
            **_request.to_boto()
        )

        return shapes.CreateLaunchTemplateResult.from_boto(response)

    def create_launch_template_version(
        self,
        _request: shapes.CreateLaunchTemplateVersionRequest = None,
        *,
        launch_template_data: shapes.RequestLaunchTemplateData,
        dry_run: bool = ShapeBase.NOT_SET,
        client_token: str = ShapeBase.NOT_SET,
        launch_template_id: str = ShapeBase.NOT_SET,
        launch_template_name: str = ShapeBase.NOT_SET,
        source_version: str = ShapeBase.NOT_SET,
        version_description: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateLaunchTemplateVersionResult:
        """
        Creates a new version for a launch template. You can specify an existing version
        of launch template from which to base the new version.

        Launch template versions are numbered in the order in which they are created.
        You cannot specify, change, or replace the numbering of launch template
        versions.
        """
        if _request is None:
            _params = {}
            if launch_template_data is not ShapeBase.NOT_SET:
                _params['launch_template_data'] = launch_template_data
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            if client_token is not ShapeBase.NOT_SET:
                _params['client_token'] = client_token
            if launch_template_id is not ShapeBase.NOT_SET:
                _params['launch_template_id'] = launch_template_id
            if launch_template_name is not ShapeBase.NOT_SET:
                _params['launch_template_name'] = launch_template_name
            if source_version is not ShapeBase.NOT_SET:
                _params['source_version'] = source_version
            if version_description is not ShapeBase.NOT_SET:
                _params['version_description'] = version_description
            _request = shapes.CreateLaunchTemplateVersionRequest(**_params)
        response = self._boto_client.create_launch_template_version(
            **_request.to_boto()
        )

        return shapes.CreateLaunchTemplateVersionResult.from_boto(response)

    def create_nat_gateway(
        self,
        _request: shapes.CreateNatGatewayRequest = None,
        *,
        allocation_id: str,
        subnet_id: str,
        client_token: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateNatGatewayResult:
        """
        Creates a NAT gateway in the specified public subnet. This action creates a
        network interface in the specified subnet with a private IP address from the IP
        address range of the subnet. Internet-bound traffic from a private subnet can be
        routed to the NAT gateway, therefore enabling instances in the private subnet to
        connect to the internet. For more information, see [NAT
        Gateways](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/vpc-nat-
        gateway.html) in the _Amazon Virtual Private Cloud User Guide_.
        """
        if _request is None:
            _params = {}
            if allocation_id is not ShapeBase.NOT_SET:
                _params['allocation_id'] = allocation_id
            if subnet_id is not ShapeBase.NOT_SET:
                _params['subnet_id'] = subnet_id
            if client_token is not ShapeBase.NOT_SET:
                _params['client_token'] = client_token
            _request = shapes.CreateNatGatewayRequest(**_params)
        response = self._boto_client.create_nat_gateway(**_request.to_boto())

        return shapes.CreateNatGatewayResult.from_boto(response)

    def create_network_acl(
        self,
        _request: shapes.CreateNetworkAclRequest = None,
        *,
        vpc_id: str,
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> shapes.CreateNetworkAclResult:
        """
        Creates a network ACL in a VPC. Network ACLs provide an optional layer of
        security (in addition to security groups) for the instances in your VPC.

        For more information, see [Network
        ACLs](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_ACLs.html) in
        the _Amazon Virtual Private Cloud User Guide_.
        """
        if _request is None:
            _params = {}
            if vpc_id is not ShapeBase.NOT_SET:
                _params['vpc_id'] = vpc_id
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.CreateNetworkAclRequest(**_params)
        response = self._boto_client.create_network_acl(**_request.to_boto())

        return shapes.CreateNetworkAclResult.from_boto(response)

    def create_network_acl_entry(
        self,
        _request: shapes.CreateNetworkAclEntryRequest = None,
        *,
        egress: bool,
        network_acl_id: str,
        protocol: str,
        rule_action: typing.Union[str, shapes.RuleAction],
        rule_number: int,
        cidr_block: str = ShapeBase.NOT_SET,
        dry_run: bool = ShapeBase.NOT_SET,
        icmp_type_code: shapes.IcmpTypeCode = ShapeBase.NOT_SET,
        ipv6_cidr_block: str = ShapeBase.NOT_SET,
        port_range: shapes.PortRange = ShapeBase.NOT_SET,
    ) -> None:
        """
        Creates an entry (a rule) in a network ACL with the specified rule number. Each
        network ACL has a set of numbered ingress rules and a separate set of numbered
        egress rules. When determining whether a packet should be allowed in or out of a
        subnet associated with the ACL, we process the entries in the ACL according to
        the rule numbers, in ascending order. Each network ACL has a set of ingress
        rules and a separate set of egress rules.

        We recommend that you leave room between the rule numbers (for example, 100,
        110, 120, ...), and not number them one right after the other (for example, 101,
        102, 103, ...). This makes it easier to add a rule between existing ones without
        having to renumber the rules.

        After you add an entry, you can't modify it; you must either replace it, or
        create an entry and delete the old one.

        For more information about network ACLs, see [Network
        ACLs](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_ACLs.html) in
        the _Amazon Virtual Private Cloud User Guide_.
        """
        if _request is None:
            _params = {}
            if egress is not ShapeBase.NOT_SET:
                _params['egress'] = egress
            if network_acl_id is not ShapeBase.NOT_SET:
                _params['network_acl_id'] = network_acl_id
            if protocol is not ShapeBase.NOT_SET:
                _params['protocol'] = protocol
            if rule_action is not ShapeBase.NOT_SET:
                _params['rule_action'] = rule_action
            if rule_number is not ShapeBase.NOT_SET:
                _params['rule_number'] = rule_number
            if cidr_block is not ShapeBase.NOT_SET:
                _params['cidr_block'] = cidr_block
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            if icmp_type_code is not ShapeBase.NOT_SET:
                _params['icmp_type_code'] = icmp_type_code
            if ipv6_cidr_block is not ShapeBase.NOT_SET:
                _params['ipv6_cidr_block'] = ipv6_cidr_block
            if port_range is not ShapeBase.NOT_SET:
                _params['port_range'] = port_range
            _request = shapes.CreateNetworkAclEntryRequest(**_params)
        response = self._boto_client.create_network_acl_entry(
            **_request.to_boto()
        )

    def create_network_interface(
        self,
        _request: shapes.CreateNetworkInterfaceRequest = None,
        *,
        subnet_id: str,
        description: str = ShapeBase.NOT_SET,
        dry_run: bool = ShapeBase.NOT_SET,
        groups: typing.List[str] = ShapeBase.NOT_SET,
        ipv6_address_count: int = ShapeBase.NOT_SET,
        ipv6_addresses: typing.List[shapes.InstanceIpv6Address
                                   ] = ShapeBase.NOT_SET,
        private_ip_address: str = ShapeBase.NOT_SET,
        private_ip_addresses: typing.List[shapes.PrivateIpAddressSpecification
                                         ] = ShapeBase.NOT_SET,
        secondary_private_ip_address_count: int = ShapeBase.NOT_SET,
    ) -> shapes.CreateNetworkInterfaceResult:
        """
        Creates a network interface in the specified subnet.

        For more information about network interfaces, see [Elastic Network
        Interfaces](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html)
        in the _Amazon Virtual Private Cloud User Guide_.
        """
        if _request is None:
            _params = {}
            if subnet_id is not ShapeBase.NOT_SET:
                _params['subnet_id'] = subnet_id
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            if groups is not ShapeBase.NOT_SET:
                _params['groups'] = groups
            if ipv6_address_count is not ShapeBase.NOT_SET:
                _params['ipv6_address_count'] = ipv6_address_count
            if ipv6_addresses is not ShapeBase.NOT_SET:
                _params['ipv6_addresses'] = ipv6_addresses
            if private_ip_address is not ShapeBase.NOT_SET:
                _params['private_ip_address'] = private_ip_address
            if private_ip_addresses is not ShapeBase.NOT_SET:
                _params['private_ip_addresses'] = private_ip_addresses
            if secondary_private_ip_address_count is not ShapeBase.NOT_SET:
                _params['secondary_private_ip_address_count'
                       ] = secondary_private_ip_address_count
            _request = shapes.CreateNetworkInterfaceRequest(**_params)
        response = self._boto_client.create_network_interface(
            **_request.to_boto()
        )

        return shapes.CreateNetworkInterfaceResult.from_boto(response)

    def create_network_interface_permission(
        self,
        _request: shapes.CreateNetworkInterfacePermissionRequest = None,
        *,
        network_interface_id: str,
        permission: typing.Union[str, shapes.InterfacePermissionType],
        aws_account_id: str = ShapeBase.NOT_SET,
        aws_service: str = ShapeBase.NOT_SET,
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> shapes.CreateNetworkInterfacePermissionResult:
        """
        Grants an AWS-authorized account permission to attach the specified network
        interface to an instance in their account.

        You can grant permission to a single AWS account only, and only one account at a
        time.
        """
        if _request is None:
            _params = {}
            if network_interface_id is not ShapeBase.NOT_SET:
                _params['network_interface_id'] = network_interface_id
            if permission is not ShapeBase.NOT_SET:
                _params['permission'] = permission
            if aws_account_id is not ShapeBase.NOT_SET:
                _params['aws_account_id'] = aws_account_id
            if aws_service is not ShapeBase.NOT_SET:
                _params['aws_service'] = aws_service
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.CreateNetworkInterfacePermissionRequest(**_params)
        response = self._boto_client.create_network_interface_permission(
            **_request.to_boto()
        )

        return shapes.CreateNetworkInterfacePermissionResult.from_boto(response)

    def create_placement_group(
        self,
        _request: shapes.CreatePlacementGroupRequest = None,
        *,
        group_name: str,
        strategy: typing.Union[str, shapes.PlacementStrategy],
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> None:
        """
        Creates a placement group in which to launch instances. The strategy of the
        placement group determines how the instances are organized within the group.

        A `cluster` placement group is a logical grouping of instances within a single
        Availability Zone that benefit from low network latency, high network
        throughput. A `spread` placement group places instances on distinct hardware.

        For more information, see [Placement
        Groups](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-
        groups.html) in the _Amazon Elastic Compute Cloud User Guide_.
        """
        if _request is None:
            _params = {}
            if group_name is not ShapeBase.NOT_SET:
                _params['group_name'] = group_name
            if strategy is not ShapeBase.NOT_SET:
                _params['strategy'] = strategy
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.CreatePlacementGroupRequest(**_params)
        response = self._boto_client.create_placement_group(
            **_request.to_boto()
        )

    def create_reserved_instances_listing(
        self,
        _request: shapes.CreateReservedInstancesListingRequest = None,
        *,
        client_token: str,
        instance_count: int,
        price_schedules: typing.List[shapes.PriceScheduleSpecification],
        reserved_instances_id: str,
    ) -> shapes.CreateReservedInstancesListingResult:
        """
        Creates a listing for Amazon EC2 Standard Reserved Instances to be sold in the
        Reserved Instance Marketplace. You can submit one Standard Reserved Instance
        listing at a time. To get a list of your Standard Reserved Instances, you can
        use the DescribeReservedInstances operation.

        Only Standard Reserved Instances with a capacity reservation can be sold in the
        Reserved Instance Marketplace. Convertible Reserved Instances and Standard
        Reserved Instances with a regional benefit cannot be sold.

        The Reserved Instance Marketplace matches sellers who want to resell Standard
        Reserved Instance capacity that they no longer need with buyers who want to
        purchase additional capacity. Reserved Instances bought and sold through the
        Reserved Instance Marketplace work like any other Reserved Instances.

        To sell your Standard Reserved Instances, you must first register as a seller in
        the Reserved Instance Marketplace. After completing the registration process,
        you can create a Reserved Instance Marketplace listing of some or all of your
        Standard Reserved Instances, and specify the upfront price to receive for them.
        Your Standard Reserved Instance listings then become available for purchase. To
        view the details of your Standard Reserved Instance listing, you can use the
        DescribeReservedInstancesListings operation.

        For more information, see [Reserved Instance
        Marketplace](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ri-market-
        general.html) in the _Amazon Elastic Compute Cloud User Guide_.
        """
        if _request is None:
            _params = {}
            if client_token is not ShapeBase.NOT_SET:
                _params['client_token'] = client_token
            if instance_count is not ShapeBase.NOT_SET:
                _params['instance_count'] = instance_count
            if price_schedules is not ShapeBase.NOT_SET:
                _params['price_schedules'] = price_schedules
            if reserved_instances_id is not ShapeBase.NOT_SET:
                _params['reserved_instances_id'] = reserved_instances_id
            _request = shapes.CreateReservedInstancesListingRequest(**_params)
        response = self._boto_client.create_reserved_instances_listing(
            **_request.to_boto()
        )

        return shapes.CreateReservedInstancesListingResult.from_boto(response)

    def create_route(
        self,
        _request: shapes.CreateRouteRequest = None,
        *,
        route_table_id: str,
        destination_cidr_block: str = ShapeBase.NOT_SET,
        destination_ipv6_cidr_block: str = ShapeBase.NOT_SET,
        dry_run: bool = ShapeBase.NOT_SET,
        egress_only_internet_gateway_id: str = ShapeBase.NOT_SET,
        gateway_id: str = ShapeBase.NOT_SET,
        instance_id: str = ShapeBase.NOT_SET,
        nat_gateway_id: str = ShapeBase.NOT_SET,
        network_interface_id: str = ShapeBase.NOT_SET,
        vpc_peering_connection_id: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateRouteResult:
        """
        Creates a route in a route table within a VPC.

        You must specify one of the following targets: internet gateway or virtual
        private gateway, NAT instance, NAT gateway, VPC peering connection, network
        interface, or egress-only internet gateway.

        When determining how to route traffic, we use the route with the most specific
        match. For example, traffic is destined for the IPv4 address `192.0.2.3`, and
        the route table includes the following two IPv4 routes:

          * `192.0.2.0/24` (goes to some target A)

          * `192.0.2.0/28` (goes to some target B)

        Both routes apply to the traffic destined for `192.0.2.3`. However, the second
        route in the list covers a smaller number of IP addresses and is therefore more
        specific, so we use that route to determine where to target the traffic.

        For more information about route tables, see [Route
        Tables](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Route_Tables.html)
        in the _Amazon Virtual Private Cloud User Guide_.
        """
        if _request is None:
            _params = {}
            if route_table_id is not ShapeBase.NOT_SET:
                _params['route_table_id'] = route_table_id
            if destination_cidr_block is not ShapeBase.NOT_SET:
                _params['destination_cidr_block'] = destination_cidr_block
            if destination_ipv6_cidr_block is not ShapeBase.NOT_SET:
                _params['destination_ipv6_cidr_block'
                       ] = destination_ipv6_cidr_block
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            if egress_only_internet_gateway_id is not ShapeBase.NOT_SET:
                _params['egress_only_internet_gateway_id'
                       ] = egress_only_internet_gateway_id
            if gateway_id is not ShapeBase.NOT_SET:
                _params['gateway_id'] = gateway_id
            if instance_id is not ShapeBase.NOT_SET:
                _params['instance_id'] = instance_id
            if nat_gateway_id is not ShapeBase.NOT_SET:
                _params['nat_gateway_id'] = nat_gateway_id
            if network_interface_id is not ShapeBase.NOT_SET:
                _params['network_interface_id'] = network_interface_id
            if vpc_peering_connection_id is not ShapeBase.NOT_SET:
                _params['vpc_peering_connection_id'] = vpc_peering_connection_id
            _request = shapes.CreateRouteRequest(**_params)
        response = self._boto_client.create_route(**_request.to_boto())

        return shapes.CreateRouteResult.from_boto(response)

    def create_route_table(
        self,
        _request: shapes.CreateRouteTableRequest = None,
        *,
        vpc_id: str,
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> shapes.CreateRouteTableResult:
        """
        Creates a route table for the specified VPC. After you create a route table, you
        can add routes and associate the table with a subnet.

        For more information, see [Route
        Tables](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Route_Tables.html)
        in the _Amazon Virtual Private Cloud User Guide_.
        """
        if _request is None:
            _params = {}
            if vpc_id is not ShapeBase.NOT_SET:
                _params['vpc_id'] = vpc_id
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.CreateRouteTableRequest(**_params)
        response = self._boto_client.create_route_table(**_request.to_boto())

        return shapes.CreateRouteTableResult.from_boto(response)

    def create_security_group(
        self,
        _request: shapes.CreateSecurityGroupRequest = None,
        *,
        description: str,
        group_name: str,
        vpc_id: str = ShapeBase.NOT_SET,
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> shapes.CreateSecurityGroupResult:
        """
        Creates a security group.

        A security group is for use with instances either in the EC2-Classic platform or
        in a specific VPC. For more information, see [Amazon EC2 Security
        Groups](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-network-
        security.html) in the _Amazon Elastic Compute Cloud User Guide_ and [Security
        Groups for Your
        VPC](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_SecurityGroups.html)
        in the _Amazon Virtual Private Cloud User Guide_.

        EC2-Classic: You can have up to 500 security groups.

        EC2-VPC: You can create up to 500 security groups per VPC.

        When you create a security group, you specify a friendly name of your choice.
        You can have a security group for use in EC2-Classic with the same name as a
        security group for use in a VPC. However, you can't have two security groups for
        use in EC2-Classic with the same name or two security groups for use in a VPC
        with the same name.

        You have a default security group for use in EC2-Classic and a default security
        group for use in your VPC. If you don't specify a security group when you launch
        an instance, the instance is launched into the appropriate default security
        group. A default security group includes a default rule that grants instances
        unrestricted network access to each other.

        You can add or remove rules from your security groups using
        AuthorizeSecurityGroupIngress, AuthorizeSecurityGroupEgress,
        RevokeSecurityGroupIngress, and RevokeSecurityGroupEgress.
        """
        if _request is None:
            _params = {}
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if group_name is not ShapeBase.NOT_SET:
                _params['group_name'] = group_name
            if vpc_id is not ShapeBase.NOT_SET:
                _params['vpc_id'] = vpc_id
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.CreateSecurityGroupRequest(**_params)
        response = self._boto_client.create_security_group(**_request.to_boto())

        return shapes.CreateSecurityGroupResult.from_boto(response)

    def create_snapshot(
        self,
        _request: shapes.CreateSnapshotRequest = None,
        *,
        volume_id: str,
        description: str = ShapeBase.NOT_SET,
        tag_specifications: typing.List[shapes.TagSpecification
                                       ] = ShapeBase.NOT_SET,
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> shapes.Snapshot:
        """
        Creates a snapshot of an EBS volume and stores it in Amazon S3. You can use
        snapshots for backups, to make copies of EBS volumes, and to save data before
        shutting down an instance.

        When a snapshot is created, any AWS Marketplace product codes that are
        associated with the source volume are propagated to the snapshot.

        You can take a snapshot of an attached volume that is in use. However, snapshots
        only capture data that has been written to your EBS volume at the time the
        snapshot command is issued; this may exclude any data that has been cached by
        any applications or the operating system. If you can pause any file systems on
        the volume long enough to take a snapshot, your snapshot should be complete.
        However, if you cannot pause all file writes to the volume, you should unmount
        the volume from within the instance, issue the snapshot command, and then
        remount the volume to ensure a consistent and complete snapshot. You may remount
        and use your volume while the snapshot status is `pending`.

        To create a snapshot for EBS volumes that serve as root devices, you should stop
        the instance before taking the snapshot.

        Snapshots that are taken from encrypted volumes are automatically encrypted.
        Volumes that are created from encrypted snapshots are also automatically
        encrypted. Your encrypted volumes and any associated snapshots always remain
        protected.

        You can tag your snapshots during creation. For more information, see [Tagging
        Your Amazon EC2
        Resources](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html)
        in the _Amazon Elastic Compute Cloud User Guide_.

        For more information, see [Amazon Elastic Block
        Store](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AmazonEBS.html) and
        [Amazon EBS
        Encryption](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html)
        in the _Amazon Elastic Compute Cloud User Guide_.
        """
        if _request is None:
            _params = {}
            if volume_id is not ShapeBase.NOT_SET:
                _params['volume_id'] = volume_id
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if tag_specifications is not ShapeBase.NOT_SET:
                _params['tag_specifications'] = tag_specifications
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.CreateSnapshotRequest(**_params)
        response = self._boto_client.create_snapshot(**_request.to_boto())

        return shapes.Snapshot.from_boto(response)

    def create_spot_datafeed_subscription(
        self,
        _request: shapes.CreateSpotDatafeedSubscriptionRequest = None,
        *,
        bucket: str,
        dry_run: bool = ShapeBase.NOT_SET,
        prefix: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateSpotDatafeedSubscriptionResult:
        """
        Creates a data feed for Spot Instances, enabling you to view Spot Instance usage
        logs. You can create one data feed per AWS account. For more information, see
        [Spot Instance Data
        Feed](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-data-feeds.html)
        in the _Amazon EC2 User Guide for Linux Instances_.
        """
        if _request is None:
            _params = {}
            if bucket is not ShapeBase.NOT_SET:
                _params['bucket'] = bucket
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            if prefix is not ShapeBase.NOT_SET:
                _params['prefix'] = prefix
            _request = shapes.CreateSpotDatafeedSubscriptionRequest(**_params)
        response = self._boto_client.create_spot_datafeed_subscription(
            **_request.to_boto()
        )

        return shapes.CreateSpotDatafeedSubscriptionResult.from_boto(response)

    def create_subnet(
        self,
        _request: shapes.CreateSubnetRequest = None,
        *,
        cidr_block: str,
        vpc_id: str,
        availability_zone: str = ShapeBase.NOT_SET,
        ipv6_cidr_block: str = ShapeBase.NOT_SET,
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> shapes.CreateSubnetResult:
        """
        Creates a subnet in an existing VPC.

        When you create each subnet, you provide the VPC ID and IPv4 CIDR block for the
        subnet. After you create a subnet, you can't change its CIDR block. The size of
        the subnet's IPv4 CIDR block can be the same as a VPC's IPv4 CIDR block, or a
        subset of a VPC's IPv4 CIDR block. If you create more than one subnet in a VPC,
        the subnets' CIDR blocks must not overlap. The smallest IPv4 subnet (and VPC)
        you can create uses a /28 netmask (16 IPv4 addresses), and the largest uses a
        /16 netmask (65,536 IPv4 addresses).

        If you've associated an IPv6 CIDR block with your VPC, you can create a subnet
        with an IPv6 CIDR block that uses a /64 prefix length.

        AWS reserves both the first four and the last IPv4 address in each subnet's CIDR
        block. They're not available for use.

        If you add more than one subnet to a VPC, they're set up in a star topology with
        a logical router in the middle.

        If you launch an instance in a VPC using an Amazon EBS-backed AMI, the IP
        address doesn't change if you stop and restart the instance (unlike a similar
        instance launched outside a VPC, which gets a new IP address when restarted).
        It's therefore possible to have a subnet with no running instances (they're all
        stopped), but no remaining IP addresses available.

        For more information about subnets, see [Your VPC and
        Subnets](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Subnets.html)
        in the _Amazon Virtual Private Cloud User Guide_.
        """
        if _request is None:
            _params = {}
            if cidr_block is not ShapeBase.NOT_SET:
                _params['cidr_block'] = cidr_block
            if vpc_id is not ShapeBase.NOT_SET:
                _params['vpc_id'] = vpc_id
            if availability_zone is not ShapeBase.NOT_SET:
                _params['availability_zone'] = availability_zone
            if ipv6_cidr_block is not ShapeBase.NOT_SET:
                _params['ipv6_cidr_block'] = ipv6_cidr_block
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.CreateSubnetRequest(**_params)
        response = self._boto_client.create_subnet(**_request.to_boto())

        return shapes.CreateSubnetResult.from_boto(response)

    def create_tags(
        self,
        _request: shapes.CreateTagsRequest = None,
        *,
        resources: typing.List[str],
        tags: typing.List[shapes.Tag],
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> None:
        """
        Adds or overwrites one or more tags for the specified Amazon EC2 resource or
        resources. Each resource can have a maximum of 50 tags. Each tag consists of a
        key and optional value. Tag keys must be unique per resource.

        For more information about tags, see [Tagging Your
        Resources](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html)
        in the _Amazon Elastic Compute Cloud User Guide_. For more information about
        creating IAM policies that control users' access to resources based on tags, see
        [Supported Resource-Level Permissions for Amazon EC2 API
        Actions](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-supported-iam-
        actions-resources.html) in the _Amazon Elastic Compute Cloud User Guide_.
        """
        if _request is None:
            _params = {}
            if resources is not ShapeBase.NOT_SET:
                _params['resources'] = resources
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.CreateTagsRequest(**_params)
        response = self._boto_client.create_tags(**_request.to_boto())

    def create_volume(
        self,
        _request: shapes.CreateVolumeRequest = None,
        *,
        availability_zone: str,
        encrypted: bool = ShapeBase.NOT_SET,
        iops: int = ShapeBase.NOT_SET,
        kms_key_id: str = ShapeBase.NOT_SET,
        size: int = ShapeBase.NOT_SET,
        snapshot_id: str = ShapeBase.NOT_SET,
        volume_type: typing.Union[str, shapes.VolumeType] = ShapeBase.NOT_SET,
        dry_run: bool = ShapeBase.NOT_SET,
        tag_specifications: typing.List[shapes.TagSpecification
                                       ] = ShapeBase.NOT_SET,
    ) -> shapes.Volume:
        """
        Creates an EBS volume that can be attached to an instance in the same
        Availability Zone. The volume is created in the regional endpoint that you send
        the HTTP request to. For more information see [Regions and
        Endpoints](http://docs.aws.amazon.com/general/latest/gr/rande.html).

        You can create a new empty volume or restore a volume from an EBS snapshot. Any
        AWS Marketplace product codes from the snapshot are propagated to the volume.

        You can create encrypted volumes with the `Encrypted` parameter. Encrypted
        volumes may only be attached to instances that support Amazon EBS encryption.
        Volumes that are created from encrypted snapshots are also automatically
        encrypted. For more information, see [Amazon EBS
        Encryption](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html)
        in the _Amazon Elastic Compute Cloud User Guide_.

        You can tag your volumes during creation. For more information, see [Tagging
        Your Amazon EC2
        Resources](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html)
        in the _Amazon Elastic Compute Cloud User Guide_.

        For more information, see [Creating an Amazon EBS
        Volume](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-creating-
        volume.html) in the _Amazon Elastic Compute Cloud User Guide_.
        """
        if _request is None:
            _params = {}
            if availability_zone is not ShapeBase.NOT_SET:
                _params['availability_zone'] = availability_zone
            if encrypted is not ShapeBase.NOT_SET:
                _params['encrypted'] = encrypted
            if iops is not ShapeBase.NOT_SET:
                _params['iops'] = iops
            if kms_key_id is not ShapeBase.NOT_SET:
                _params['kms_key_id'] = kms_key_id
            if size is not ShapeBase.NOT_SET:
                _params['size'] = size
            if snapshot_id is not ShapeBase.NOT_SET:
                _params['snapshot_id'] = snapshot_id
            if volume_type is not ShapeBase.NOT_SET:
                _params['volume_type'] = volume_type
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            if tag_specifications is not ShapeBase.NOT_SET:
                _params['tag_specifications'] = tag_specifications
            _request = shapes.CreateVolumeRequest(**_params)
        response = self._boto_client.create_volume(**_request.to_boto())

        return shapes.Volume.from_boto(response)

    def create_vpc(
        self,
        _request: shapes.CreateVpcRequest = None,
        *,
        cidr_block: str,
        amazon_provided_ipv6_cidr_block: bool = ShapeBase.NOT_SET,
        dry_run: bool = ShapeBase.NOT_SET,
        instance_tenancy: typing.Union[str, shapes.Tenancy] = ShapeBase.NOT_SET,
    ) -> shapes.CreateVpcResult:
        """
        Creates a VPC with the specified IPv4 CIDR block. The smallest VPC you can
        create uses a /28 netmask (16 IPv4 addresses), and the largest uses a /16
        netmask (65,536 IPv4 addresses). For more information about how large to make
        your VPC, see [Your VPC and
        Subnets](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Subnets.html)
        in the _Amazon Virtual Private Cloud User Guide_.

        You can optionally request an Amazon-provided IPv6 CIDR block for the VPC. The
        IPv6 CIDR block uses a /56 prefix length, and is allocated from Amazon's pool of
        IPv6 addresses. You cannot choose the IPv6 range for your VPC.

        By default, each instance you launch in the VPC has the default DHCP options,
        which include only a default DNS server that we provide (AmazonProvidedDNS). For
        more information, see [DHCP Options
        Sets](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_DHCP_Options.html)
        in the _Amazon Virtual Private Cloud User Guide_.

        You can specify the instance tenancy value for the VPC when you create it. You
        can't change this value for the VPC after you create it. For more information,
        see [Dedicated
        Instances](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/dedicated-
        instance.html) in the _Amazon Elastic Compute Cloud User Guide_.
        """
        if _request is None:
            _params = {}
            if cidr_block is not ShapeBase.NOT_SET:
                _params['cidr_block'] = cidr_block
            if amazon_provided_ipv6_cidr_block is not ShapeBase.NOT_SET:
                _params['amazon_provided_ipv6_cidr_block'
                       ] = amazon_provided_ipv6_cidr_block
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            if instance_tenancy is not ShapeBase.NOT_SET:
                _params['instance_tenancy'] = instance_tenancy
            _request = shapes.CreateVpcRequest(**_params)
        response = self._boto_client.create_vpc(**_request.to_boto())

        return shapes.CreateVpcResult.from_boto(response)

    def create_vpc_endpoint(
        self,
        _request: shapes.CreateVpcEndpointRequest = None,
        *,
        vpc_id: str,
        service_name: str,
        dry_run: bool = ShapeBase.NOT_SET,
        vpc_endpoint_type: typing.Union[str, shapes.
                                        VpcEndpointType] = ShapeBase.NOT_SET,
        policy_document: str = ShapeBase.NOT_SET,
        route_table_ids: typing.List[str] = ShapeBase.NOT_SET,
        subnet_ids: typing.List[str] = ShapeBase.NOT_SET,
        security_group_ids: typing.List[str] = ShapeBase.NOT_SET,
        client_token: str = ShapeBase.NOT_SET,
        private_dns_enabled: bool = ShapeBase.NOT_SET,
    ) -> shapes.CreateVpcEndpointResult:
        """
        Creates a VPC endpoint for a specified service. An endpoint enables you to
        create a private connection between your VPC and the service. The service may be
        provided by AWS, an AWS Marketplace partner, or another AWS account. For more
        information, see [VPC
        Endpoints](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/vpc-
        endpoints.html) in the _Amazon Virtual Private Cloud User Guide_.

        A `gateway` endpoint serves as a target for a route in your route table for
        traffic destined for the AWS service. You can specify an endpoint policy to
        attach to the endpoint that will control access to the service from your VPC.
        You can also specify the VPC route tables that use the endpoint.

        An `interface` endpoint is a network interface in your subnet that serves as an
        endpoint for communicating with the specified service. You can specify the
        subnets in which to create an endpoint, and the security groups to associate
        with the endpoint network interface.

        Use DescribeVpcEndpointServices to get a list of supported services.
        """
        if _request is None:
            _params = {}
            if vpc_id is not ShapeBase.NOT_SET:
                _params['vpc_id'] = vpc_id
            if service_name is not ShapeBase.NOT_SET:
                _params['service_name'] = service_name
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            if vpc_endpoint_type is not ShapeBase.NOT_SET:
                _params['vpc_endpoint_type'] = vpc_endpoint_type
            if policy_document is not ShapeBase.NOT_SET:
                _params['policy_document'] = policy_document
            if route_table_ids is not ShapeBase.NOT_SET:
                _params['route_table_ids'] = route_table_ids
            if subnet_ids is not ShapeBase.NOT_SET:
                _params['subnet_ids'] = subnet_ids
            if security_group_ids is not ShapeBase.NOT_SET:
                _params['security_group_ids'] = security_group_ids
            if client_token is not ShapeBase.NOT_SET:
                _params['client_token'] = client_token
            if private_dns_enabled is not ShapeBase.NOT_SET:
                _params['private_dns_enabled'] = private_dns_enabled
            _request = shapes.CreateVpcEndpointRequest(**_params)
        response = self._boto_client.create_vpc_endpoint(**_request.to_boto())

        return shapes.CreateVpcEndpointResult.from_boto(response)

    def create_vpc_endpoint_connection_notification(
        self,
        _request: shapes.CreateVpcEndpointConnectionNotificationRequest = None,
        *,
        connection_notification_arn: str,
        connection_events: typing.List[str],
        dry_run: bool = ShapeBase.NOT_SET,
        service_id: str = ShapeBase.NOT_SET,
        vpc_endpoint_id: str = ShapeBase.NOT_SET,
        client_token: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateVpcEndpointConnectionNotificationResult:
        """
        Creates a connection notification for a specified VPC endpoint or VPC endpoint
        service. A connection notification notifies you of specific endpoint events. You
        must create an SNS topic to receive notifications. For more information, see
        [Create a Topic](http://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html) in
        the _Amazon Simple Notification Service Developer Guide_.

        You can create a connection notification for interface endpoints only.
        """
        if _request is None:
            _params = {}
            if connection_notification_arn is not ShapeBase.NOT_SET:
                _params['connection_notification_arn'
                       ] = connection_notification_arn
            if connection_events is not ShapeBase.NOT_SET:
                _params['connection_events'] = connection_events
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            if service_id is not ShapeBase.NOT_SET:
                _params['service_id'] = service_id
            if vpc_endpoint_id is not ShapeBase.NOT_SET:
                _params['vpc_endpoint_id'] = vpc_endpoint_id
            if client_token is not ShapeBase.NOT_SET:
                _params['client_token'] = client_token
            _request = shapes.CreateVpcEndpointConnectionNotificationRequest(
                **_params
            )
        response = self._boto_client.create_vpc_endpoint_connection_notification(
            **_request.to_boto()
        )

        return shapes.CreateVpcEndpointConnectionNotificationResult.from_boto(
            response
        )

    def create_vpc_endpoint_service_configuration(
        self,
        _request: shapes.CreateVpcEndpointServiceConfigurationRequest = None,
        *,
        network_load_balancer_arns: typing.List[str],
        dry_run: bool = ShapeBase.NOT_SET,
        acceptance_required: bool = ShapeBase.NOT_SET,
        client_token: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateVpcEndpointServiceConfigurationResult:
        """
        Creates a VPC endpoint service configuration to which service consumers (AWS
        accounts, IAM users, and IAM roles) can connect. Service consumers can create an
        interface VPC endpoint to connect to your service.

        To create an endpoint service configuration, you must first create a Network
        Load Balancer for your service. For more information, see [VPC Endpoint
        Services](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/endpoint-
        service.html) in the _Amazon Virtual Private Cloud User Guide_.
        """
        if _request is None:
            _params = {}
            if network_load_balancer_arns is not ShapeBase.NOT_SET:
                _params['network_load_balancer_arns'
                       ] = network_load_balancer_arns
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            if acceptance_required is not ShapeBase.NOT_SET:
                _params['acceptance_required'] = acceptance_required
            if client_token is not ShapeBase.NOT_SET:
                _params['client_token'] = client_token
            _request = shapes.CreateVpcEndpointServiceConfigurationRequest(
                **_params
            )
        response = self._boto_client.create_vpc_endpoint_service_configuration(
            **_request.to_boto()
        )

        return shapes.CreateVpcEndpointServiceConfigurationResult.from_boto(
            response
        )

    def create_vpc_peering_connection(
        self,
        _request: shapes.CreateVpcPeeringConnectionRequest = None,
        *,
        dry_run: bool = ShapeBase.NOT_SET,
        peer_owner_id: str = ShapeBase.NOT_SET,
        peer_vpc_id: str = ShapeBase.NOT_SET,
        vpc_id: str = ShapeBase.NOT_SET,
        peer_region: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateVpcPeeringConnectionResult:
        """
        Requests a VPC peering connection between two VPCs: a requester VPC that you own
        and an accepter VPC with which to create the connection. The accepter VPC can
        belong to another AWS account and can be in a different Region to the requester
        VPC. The requester VPC and accepter VPC cannot have overlapping CIDR blocks.

        Limitations and rules apply to a VPC peering connection. For more information,
        see the
        [limitations](http://docs.aws.amazon.com/AmazonVPC/latest/PeeringGuide/vpc-
        peering-basics.html#vpc-peering-limitations) section in the _VPC Peering Guide_.

        The owner of the accepter VPC must accept the peering request to activate the
        peering connection. The VPC peering connection request expires after 7 days,
        after which it cannot be accepted or rejected.

        If you create a VPC peering connection request between VPCs with overlapping
        CIDR blocks, the VPC peering connection has a status of `failed`.
        """
        if _request is None:
            _params = {}
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            if peer_owner_id is not ShapeBase.NOT_SET:
                _params['peer_owner_id'] = peer_owner_id
            if peer_vpc_id is not ShapeBase.NOT_SET:
                _params['peer_vpc_id'] = peer_vpc_id
            if vpc_id is not ShapeBase.NOT_SET:
                _params['vpc_id'] = vpc_id
            if peer_region is not ShapeBase.NOT_SET:
                _params['peer_region'] = peer_region
            _request = shapes.CreateVpcPeeringConnectionRequest(**_params)
        response = self._boto_client.create_vpc_peering_connection(
            **_request.to_boto()
        )

        return shapes.CreateVpcPeeringConnectionResult.from_boto(response)

    def create_vpn_connection(
        self,
        _request: shapes.CreateVpnConnectionRequest = None,
        *,
        customer_gateway_id: str,
        type: str,
        vpn_gateway_id: str,
        dry_run: bool = ShapeBase.NOT_SET,
        options: shapes.VpnConnectionOptionsSpecification = ShapeBase.NOT_SET,
    ) -> shapes.CreateVpnConnectionResult:
        """
        Creates a VPN connection between an existing virtual private gateway and a VPN
        customer gateway. The only supported connection type is `ipsec.1`.

        The response includes information that you need to give to your network
        administrator to configure your customer gateway.

        We strongly recommend that you use HTTPS when calling this operation because the
        response contains sensitive cryptographic information for configuring your
        customer gateway.

        If you decide to shut down your VPN connection for any reason and later create a
        new VPN connection, you must reconfigure your customer gateway with the new
        information returned from this call.

        This is an idempotent operation. If you perform the operation more than once,
        Amazon EC2 doesn't return an error.

        For more information, see [AWS Managed VPN
        Connections](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_VPN.html)
        in the _Amazon Virtual Private Cloud User Guide_.
        """
        if _request is None:
            _params = {}
            if customer_gateway_id is not ShapeBase.NOT_SET:
                _params['customer_gateway_id'] = customer_gateway_id
            if type is not ShapeBase.NOT_SET:
                _params['type'] = type
            if vpn_gateway_id is not ShapeBase.NOT_SET:
                _params['vpn_gateway_id'] = vpn_gateway_id
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            if options is not ShapeBase.NOT_SET:
                _params['options'] = options
            _request = shapes.CreateVpnConnectionRequest(**_params)
        response = self._boto_client.create_vpn_connection(**_request.to_boto())

        return shapes.CreateVpnConnectionResult.from_boto(response)

    def create_vpn_connection_route(
        self,
        _request: shapes.CreateVpnConnectionRouteRequest = None,
        *,
        destination_cidr_block: str,
        vpn_connection_id: str,
    ) -> None:
        """
        Creates a static route associated with a VPN connection between an existing
        virtual private gateway and a VPN customer gateway. The static route allows
        traffic to be routed from the virtual private gateway to the VPN customer
        gateway.

        For more information about VPN connections, see [AWS Managed VPN
        Connections](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_VPN.html)
        in the _Amazon Virtual Private Cloud User Guide_.
        """
        if _request is None:
            _params = {}
            if destination_cidr_block is not ShapeBase.NOT_SET:
                _params['destination_cidr_block'] = destination_cidr_block
            if vpn_connection_id is not ShapeBase.NOT_SET:
                _params['vpn_connection_id'] = vpn_connection_id
            _request = shapes.CreateVpnConnectionRouteRequest(**_params)
        response = self._boto_client.create_vpn_connection_route(
            **_request.to_boto()
        )

    def create_vpn_gateway(
        self,
        _request: shapes.CreateVpnGatewayRequest = None,
        *,
        type: typing.Union[str, shapes.GatewayType],
        availability_zone: str = ShapeBase.NOT_SET,
        amazon_side_asn: int = ShapeBase.NOT_SET,
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> shapes.CreateVpnGatewayResult:
        """
        Creates a virtual private gateway. A virtual private gateway is the endpoint on
        the VPC side of your VPN connection. You can create a virtual private gateway
        before creating the VPC itself.

        For more information about virtual private gateways, see [AWS Managed VPN
        Connections](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_VPN.html)
        in the _Amazon Virtual Private Cloud User Guide_.
        """
        if _request is None:
            _params = {}
            if type is not ShapeBase.NOT_SET:
                _params['type'] = type
            if availability_zone is not ShapeBase.NOT_SET:
                _params['availability_zone'] = availability_zone
            if amazon_side_asn is not ShapeBase.NOT_SET:
                _params['amazon_side_asn'] = amazon_side_asn
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.CreateVpnGatewayRequest(**_params)
        response = self._boto_client.create_vpn_gateway(**_request.to_boto())

        return shapes.CreateVpnGatewayResult.from_boto(response)

    def delete_customer_gateway(
        self,
        _request: shapes.DeleteCustomerGatewayRequest = None,
        *,
        customer_gateway_id: str,
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> None:
        """
        Deletes the specified customer gateway. You must delete the VPN connection
        before you can delete the customer gateway.
        """
        if _request is None:
            _params = {}
            if customer_gateway_id is not ShapeBase.NOT_SET:
                _params['customer_gateway_id'] = customer_gateway_id
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.DeleteCustomerGatewayRequest(**_params)
        response = self._boto_client.delete_customer_gateway(
            **_request.to_boto()
        )

    def delete_dhcp_options(
        self,
        _request: shapes.DeleteDhcpOptionsRequest = None,
        *,
        dhcp_options_id: str,
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> None:
        """
        Deletes the specified set of DHCP options. You must disassociate the set of DHCP
        options before you can delete it. You can disassociate the set of DHCP options
        by associating either a new set of options or the default set of options with
        the VPC.
        """
        if _request is None:
            _params = {}
            if dhcp_options_id is not ShapeBase.NOT_SET:
                _params['dhcp_options_id'] = dhcp_options_id
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.DeleteDhcpOptionsRequest(**_params)
        response = self._boto_client.delete_dhcp_options(**_request.to_boto())

    def delete_egress_only_internet_gateway(
        self,
        _request: shapes.DeleteEgressOnlyInternetGatewayRequest = None,
        *,
        egress_only_internet_gateway_id: str,
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> shapes.DeleteEgressOnlyInternetGatewayResult:
        """
        Deletes an egress-only internet gateway.
        """
        if _request is None:
            _params = {}
            if egress_only_internet_gateway_id is not ShapeBase.NOT_SET:
                _params['egress_only_internet_gateway_id'
                       ] = egress_only_internet_gateway_id
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.DeleteEgressOnlyInternetGatewayRequest(**_params)
        response = self._boto_client.delete_egress_only_internet_gateway(
            **_request.to_boto()
        )

        return shapes.DeleteEgressOnlyInternetGatewayResult.from_boto(response)

    def delete_fleets(
        self,
        _request: shapes.DeleteFleetsRequest = None,
        *,
        fleet_ids: typing.List[str],
        terminate_instances: bool,
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> shapes.DeleteFleetsResult:
        """
        Deletes the specified EC2 Fleet.

        After you delete an EC2 Fleet, it launches no new instances. You must specify
        whether an EC2 Fleet should also terminate its instances. If you terminate the
        instances, the EC2 Fleet enters the `deleted_terminating` state. Otherwise, the
        EC2 Fleet enters the `deleted_running` state, and the instances continue to run
        until they are interrupted or you terminate them manually.
        """
        if _request is None:
            _params = {}
            if fleet_ids is not ShapeBase.NOT_SET:
                _params['fleet_ids'] = fleet_ids
            if terminate_instances is not ShapeBase.NOT_SET:
                _params['terminate_instances'] = terminate_instances
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.DeleteFleetsRequest(**_params)
        response = self._boto_client.delete_fleets(**_request.to_boto())

        return shapes.DeleteFleetsResult.from_boto(response)

    def delete_flow_logs(
        self,
        _request: shapes.DeleteFlowLogsRequest = None,
        *,
        flow_log_ids: typing.List[str],
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> shapes.DeleteFlowLogsResult:
        """
        Deletes one or more flow logs.
        """
        if _request is None:
            _params = {}
            if flow_log_ids is not ShapeBase.NOT_SET:
                _params['flow_log_ids'] = flow_log_ids
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.DeleteFlowLogsRequest(**_params)
        response = self._boto_client.delete_flow_logs(**_request.to_boto())

        return shapes.DeleteFlowLogsResult.from_boto(response)

    def delete_fpga_image(
        self,
        _request: shapes.DeleteFpgaImageRequest = None,
        *,
        fpga_image_id: str,
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> shapes.DeleteFpgaImageResult:
        """
        Deletes the specified Amazon FPGA Image (AFI).
        """
        if _request is None:
            _params = {}
            if fpga_image_id is not ShapeBase.NOT_SET:
                _params['fpga_image_id'] = fpga_image_id
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.DeleteFpgaImageRequest(**_params)
        response = self._boto_client.delete_fpga_image(**_request.to_boto())

        return shapes.DeleteFpgaImageResult.from_boto(response)

    def delete_internet_gateway(
        self,
        _request: shapes.DeleteInternetGatewayRequest = None,
        *,
        internet_gateway_id: str,
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> None:
        """
        Deletes the specified internet gateway. You must detach the internet gateway
        from the VPC before you can delete it.
        """
        if _request is None:
            _params = {}
            if internet_gateway_id is not ShapeBase.NOT_SET:
                _params['internet_gateway_id'] = internet_gateway_id
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.DeleteInternetGatewayRequest(**_params)
        response = self._boto_client.delete_internet_gateway(
            **_request.to_boto()
        )

    def delete_key_pair(
        self,
        _request: shapes.DeleteKeyPairRequest = None,
        *,
        key_name: str,
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> None:
        """
        Deletes the specified key pair, by removing the public key from Amazon EC2.
        """
        if _request is None:
            _params = {}
            if key_name is not ShapeBase.NOT_SET:
                _params['key_name'] = key_name
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.DeleteKeyPairRequest(**_params)
        response = self._boto_client.delete_key_pair(**_request.to_boto())

    def delete_launch_template(
        self,
        _request: shapes.DeleteLaunchTemplateRequest = None,
        *,
        dry_run: bool = ShapeBase.NOT_SET,
        launch_template_id: str = ShapeBase.NOT_SET,
        launch_template_name: str = ShapeBase.NOT_SET,
    ) -> shapes.DeleteLaunchTemplateResult:
        """
        Deletes a launch template. Deleting a launch template deletes all of its
        versions.
        """
        if _request is None:
            _params = {}
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            if launch_template_id is not ShapeBase.NOT_SET:
                _params['launch_template_id'] = launch_template_id
            if launch_template_name is not ShapeBase.NOT_SET:
                _params['launch_template_name'] = launch_template_name
            _request = shapes.DeleteLaunchTemplateRequest(**_params)
        response = self._boto_client.delete_launch_template(
            **_request.to_boto()
        )

        return shapes.DeleteLaunchTemplateResult.from_boto(response)

    def delete_launch_template_versions(
        self,
        _request: shapes.DeleteLaunchTemplateVersionsRequest = None,
        *,
        versions: typing.List[str],
        dry_run: bool = ShapeBase.NOT_SET,
        launch_template_id: str = ShapeBase.NOT_SET,
        launch_template_name: str = ShapeBase.NOT_SET,
    ) -> shapes.DeleteLaunchTemplateVersionsResult:
        """
        Deletes one or more versions of a launch template. You cannot delete the default
        version of a launch template; you must first assign a different version as the
        default. If the default version is the only version for the launch template, you
        must delete the entire launch template using DeleteLaunchTemplate.
        """
        if _request is None:
            _params = {}
            if versions is not ShapeBase.NOT_SET:
                _params['versions'] = versions
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            if launch_template_id is not ShapeBase.NOT_SET:
                _params['launch_template_id'] = launch_template_id
            if launch_template_name is not ShapeBase.NOT_SET:
                _params['launch_template_name'] = launch_template_name
            _request = shapes.DeleteLaunchTemplateVersionsRequest(**_params)
        response = self._boto_client.delete_launch_template_versions(
            **_request.to_boto()
        )

        return shapes.DeleteLaunchTemplateVersionsResult.from_boto(response)

    def delete_nat_gateway(
        self,
        _request: shapes.DeleteNatGatewayRequest = None,
        *,
        nat_gateway_id: str,
    ) -> shapes.DeleteNatGatewayResult:
        """
        Deletes the specified NAT gateway. Deleting a NAT gateway disassociates its
        Elastic IP address, but does not release the address from your account. Deleting
        a NAT gateway does not delete any NAT gateway routes in your route tables.
        """
        if _request is None:
            _params = {}
            if nat_gateway_id is not ShapeBase.NOT_SET:
                _params['nat_gateway_id'] = nat_gateway_id
            _request = shapes.DeleteNatGatewayRequest(**_params)
        response = self._boto_client.delete_nat_gateway(**_request.to_boto())

        return shapes.DeleteNatGatewayResult.from_boto(response)

    def delete_network_acl(
        self,
        _request: shapes.DeleteNetworkAclRequest = None,
        *,
        network_acl_id: str,
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> None:
        """
        Deletes the specified network ACL. You can't delete the ACL if it's associated
        with any subnets. You can't delete the default network ACL.
        """
        if _request is None:
            _params = {}
            if network_acl_id is not ShapeBase.NOT_SET:
                _params['network_acl_id'] = network_acl_id
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.DeleteNetworkAclRequest(**_params)
        response = self._boto_client.delete_network_acl(**_request.to_boto())

    def delete_network_acl_entry(
        self,
        _request: shapes.DeleteNetworkAclEntryRequest = None,
        *,
        egress: bool,
        network_acl_id: str,
        rule_number: int,
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> None:
        """
        Deletes the specified ingress or egress entry (rule) from the specified network
        ACL.
        """
        if _request is None:
            _params = {}
            if egress is not ShapeBase.NOT_SET:
                _params['egress'] = egress
            if network_acl_id is not ShapeBase.NOT_SET:
                _params['network_acl_id'] = network_acl_id
            if rule_number is not ShapeBase.NOT_SET:
                _params['rule_number'] = rule_number
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.DeleteNetworkAclEntryRequest(**_params)
        response = self._boto_client.delete_network_acl_entry(
            **_request.to_boto()
        )

    def delete_network_interface(
        self,
        _request: shapes.DeleteNetworkInterfaceRequest = None,
        *,
        network_interface_id: str,
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> None:
        """
        Deletes the specified network interface. You must detach the network interface
        before you can delete it.
        """
        if _request is None:
            _params = {}
            if network_interface_id is not ShapeBase.NOT_SET:
                _params['network_interface_id'] = network_interface_id
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.DeleteNetworkInterfaceRequest(**_params)
        response = self._boto_client.delete_network_interface(
            **_request.to_boto()
        )

    def delete_network_interface_permission(
        self,
        _request: shapes.DeleteNetworkInterfacePermissionRequest = None,
        *,
        network_interface_permission_id: str,
        force: bool = ShapeBase.NOT_SET,
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> shapes.DeleteNetworkInterfacePermissionResult:
        """
        Deletes a permission for a network interface. By default, you cannot delete the
        permission if the account for which you're removing the permission has attached
        the network interface to an instance. However, you can force delete the
        permission, regardless of any attachment.
        """
        if _request is None:
            _params = {}
            if network_interface_permission_id is not ShapeBase.NOT_SET:
                _params['network_interface_permission_id'
                       ] = network_interface_permission_id
            if force is not ShapeBase.NOT_SET:
                _params['force'] = force
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.DeleteNetworkInterfacePermissionRequest(**_params)
        response = self._boto_client.delete_network_interface_permission(
            **_request.to_boto()
        )

        return shapes.DeleteNetworkInterfacePermissionResult.from_boto(response)

    def delete_placement_group(
        self,
        _request: shapes.DeletePlacementGroupRequest = None,
        *,
        group_name: str,
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> None:
        """
        Deletes the specified placement group. You must terminate all instances in the
        placement group before you can delete the placement group. For more information,
        see [Placement
        Groups](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-
        groups.html) in the _Amazon Elastic Compute Cloud User Guide_.
        """
        if _request is None:
            _params = {}
            if group_name is not ShapeBase.NOT_SET:
                _params['group_name'] = group_name
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.DeletePlacementGroupRequest(**_params)
        response = self._boto_client.delete_placement_group(
            **_request.to_boto()
        )

    def delete_route(
        self,
        _request: shapes.DeleteRouteRequest = None,
        *,
        route_table_id: str,
        destination_cidr_block: str = ShapeBase.NOT_SET,
        destination_ipv6_cidr_block: str = ShapeBase.NOT_SET,
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> None:
        """
        Deletes the specified route from the specified route table.
        """
        if _request is None:
            _params = {}
            if route_table_id is not ShapeBase.NOT_SET:
                _params['route_table_id'] = route_table_id
            if destination_cidr_block is not ShapeBase.NOT_SET:
                _params['destination_cidr_block'] = destination_cidr_block
            if destination_ipv6_cidr_block is not ShapeBase.NOT_SET:
                _params['destination_ipv6_cidr_block'
                       ] = destination_ipv6_cidr_block
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.DeleteRouteRequest(**_params)
        response = self._boto_client.delete_route(**_request.to_boto())

    def delete_route_table(
        self,
        _request: shapes.DeleteRouteTableRequest = None,
        *,
        route_table_id: str,
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> None:
        """
        Deletes the specified route table. You must disassociate the route table from
        any subnets before you can delete it. You can't delete the main route table.
        """
        if _request is None:
            _params = {}
            if route_table_id is not ShapeBase.NOT_SET:
                _params['route_table_id'] = route_table_id
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.DeleteRouteTableRequest(**_params)
        response = self._boto_client.delete_route_table(**_request.to_boto())

    def delete_security_group(
        self,
        _request: shapes.DeleteSecurityGroupRequest = None,
        *,
        group_id: str = ShapeBase.NOT_SET,
        group_name: str = ShapeBase.NOT_SET,
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> None:
        """
        Deletes a security group.

        If you attempt to delete a security group that is associated with an instance,
        or is referenced by another security group, the operation fails with
        `InvalidGroup.InUse` in EC2-Classic or `DependencyViolation` in EC2-VPC.
        """
        if _request is None:
            _params = {}
            if group_id is not ShapeBase.NOT_SET:
                _params['group_id'] = group_id
            if group_name is not ShapeBase.NOT_SET:
                _params['group_name'] = group_name
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.DeleteSecurityGroupRequest(**_params)
        response = self._boto_client.delete_security_group(**_request.to_boto())

    def delete_snapshot(
        self,
        _request: shapes.DeleteSnapshotRequest = None,
        *,
        snapshot_id: str,
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> None:
        """
        Deletes the specified snapshot.

        When you make periodic snapshots of a volume, the snapshots are incremental, and
        only the blocks on the device that have changed since your last snapshot are
        saved in the new snapshot. When you delete a snapshot, only the data not needed
        for any other snapshot is removed. So regardless of which prior snapshots have
        been deleted, all active snapshots will have access to all the information
        needed to restore the volume.

        You cannot delete a snapshot of the root device of an EBS volume used by a
        registered AMI. You must first de-register the AMI before you can delete the
        snapshot.

        For more information, see [Deleting an Amazon EBS
        Snapshot](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-deleting-
        snapshot.html) in the _Amazon Elastic Compute Cloud User Guide_.
        """
        if _request is None:
            _params = {}
            if snapshot_id is not ShapeBase.NOT_SET:
                _params['snapshot_id'] = snapshot_id
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.DeleteSnapshotRequest(**_params)
        response = self._boto_client.delete_snapshot(**_request.to_boto())

    def delete_spot_datafeed_subscription(
        self,
        _request: shapes.DeleteSpotDatafeedSubscriptionRequest = None,
        *,
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> None:
        """
        Deletes the data feed for Spot Instances.
        """
        if _request is None:
            _params = {}
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.DeleteSpotDatafeedSubscriptionRequest(**_params)
        response = self._boto_client.delete_spot_datafeed_subscription(
            **_request.to_boto()
        )

    def delete_subnet(
        self,
        _request: shapes.DeleteSubnetRequest = None,
        *,
        subnet_id: str,
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> None:
        """
        Deletes the specified subnet. You must terminate all running instances in the
        subnet before you can delete the subnet.
        """
        if _request is None:
            _params = {}
            if subnet_id is not ShapeBase.NOT_SET:
                _params['subnet_id'] = subnet_id
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.DeleteSubnetRequest(**_params)
        response = self._boto_client.delete_subnet(**_request.to_boto())

    def delete_tags(
        self,
        _request: shapes.DeleteTagsRequest = None,
        *,
        resources: typing.List[str],
        dry_run: bool = ShapeBase.NOT_SET,
        tags: typing.List[shapes.Tag] = ShapeBase.NOT_SET,
    ) -> None:
        """
        Deletes the specified set of tags from the specified set of resources.

        To list the current tags, use DescribeTags. For more information about tags, see
        [Tagging Your
        Resources](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html)
        in the _Amazon Elastic Compute Cloud User Guide_.
        """
        if _request is None:
            _params = {}
            if resources is not ShapeBase.NOT_SET:
                _params['resources'] = resources
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            _request = shapes.DeleteTagsRequest(**_params)
        response = self._boto_client.delete_tags(**_request.to_boto())

    def delete_volume(
        self,
        _request: shapes.DeleteVolumeRequest = None,
        *,
        volume_id: str,
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> None:
        """
        Deletes the specified EBS volume. The volume must be in the `available` state
        (not attached to an instance).

        The volume can remain in the `deleting` state for several minutes.

        For more information, see [Deleting an Amazon EBS
        Volume](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-deleting-
        volume.html) in the _Amazon Elastic Compute Cloud User Guide_.
        """
        if _request is None:
            _params = {}
            if volume_id is not ShapeBase.NOT_SET:
                _params['volume_id'] = volume_id
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.DeleteVolumeRequest(**_params)
        response = self._boto_client.delete_volume(**_request.to_boto())

    def delete_vpc(
        self,
        _request: shapes.DeleteVpcRequest = None,
        *,
        vpc_id: str,
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> None:
        """
        Deletes the specified VPC. You must detach or delete all gateways and resources
        that are associated with the VPC before you can delete it. For example, you must
        terminate all instances running in the VPC, delete all security groups
        associated with the VPC (except the default one), delete all route tables
        associated with the VPC (except the default one), and so on.
        """
        if _request is None:
            _params = {}
            if vpc_id is not ShapeBase.NOT_SET:
                _params['vpc_id'] = vpc_id
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.DeleteVpcRequest(**_params)
        response = self._boto_client.delete_vpc(**_request.to_boto())

    def delete_vpc_endpoint_connection_notifications(
        self,
        _request: shapes.DeleteVpcEndpointConnectionNotificationsRequest = None,
        *,
        connection_notification_ids: typing.List[str],
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> shapes.DeleteVpcEndpointConnectionNotificationsResult:
        """
        Deletes one or more VPC endpoint connection notifications.
        """
        if _request is None:
            _params = {}
            if connection_notification_ids is not ShapeBase.NOT_SET:
                _params['connection_notification_ids'
                       ] = connection_notification_ids
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.DeleteVpcEndpointConnectionNotificationsRequest(
                **_params
            )
        response = self._boto_client.delete_vpc_endpoint_connection_notifications(
            **_request.to_boto()
        )

        return shapes.DeleteVpcEndpointConnectionNotificationsResult.from_boto(
            response
        )

    def delete_vpc_endpoint_service_configurations(
        self,
        _request: shapes.DeleteVpcEndpointServiceConfigurationsRequest = None,
        *,
        service_ids: typing.List[str],
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> shapes.DeleteVpcEndpointServiceConfigurationsResult:
        """
        Deletes one or more VPC endpoint service configurations in your account. Before
        you delete the endpoint service configuration, you must reject any `Available`
        or `PendingAcceptance` interface endpoint connections that are attached to the
        service.
        """
        if _request is None:
            _params = {}
            if service_ids is not ShapeBase.NOT_SET:
                _params['service_ids'] = service_ids
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.DeleteVpcEndpointServiceConfigurationsRequest(
                **_params
            )
        response = self._boto_client.delete_vpc_endpoint_service_configurations(
            **_request.to_boto()
        )

        return shapes.DeleteVpcEndpointServiceConfigurationsResult.from_boto(
            response
        )

    def delete_vpc_endpoints(
        self,
        _request: shapes.DeleteVpcEndpointsRequest = None,
        *,
        vpc_endpoint_ids: typing.List[str],
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> shapes.DeleteVpcEndpointsResult:
        """
        Deletes one or more specified VPC endpoints. Deleting a gateway endpoint also
        deletes the endpoint routes in the route tables that were associated with the
        endpoint. Deleting an interface endpoint deletes the endpoint network
        interfaces.
        """
        if _request is None:
            _params = {}
            if vpc_endpoint_ids is not ShapeBase.NOT_SET:
                _params['vpc_endpoint_ids'] = vpc_endpoint_ids
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.DeleteVpcEndpointsRequest(**_params)
        response = self._boto_client.delete_vpc_endpoints(**_request.to_boto())

        return shapes.DeleteVpcEndpointsResult.from_boto(response)

    def delete_vpc_peering_connection(
        self,
        _request: shapes.DeleteVpcPeeringConnectionRequest = None,
        *,
        vpc_peering_connection_id: str,
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> shapes.DeleteVpcPeeringConnectionResult:
        """
        Deletes a VPC peering connection. Either the owner of the requester VPC or the
        owner of the accepter VPC can delete the VPC peering connection if it's in the
        `active` state. The owner of the requester VPC can delete a VPC peering
        connection in the `pending-acceptance` state. You cannot delete a VPC peering
        connection that's in the `failed` state.
        """
        if _request is None:
            _params = {}
            if vpc_peering_connection_id is not ShapeBase.NOT_SET:
                _params['vpc_peering_connection_id'] = vpc_peering_connection_id
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.DeleteVpcPeeringConnectionRequest(**_params)
        response = self._boto_client.delete_vpc_peering_connection(
            **_request.to_boto()
        )

        return shapes.DeleteVpcPeeringConnectionResult.from_boto(response)

    def delete_vpn_connection(
        self,
        _request: shapes.DeleteVpnConnectionRequest = None,
        *,
        vpn_connection_id: str,
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> None:
        """
        Deletes the specified VPN connection.

        If you're deleting the VPC and its associated components, we recommend that you
        detach the virtual private gateway from the VPC and delete the VPC before
        deleting the VPN connection. If you believe that the tunnel credentials for your
        VPN connection have been compromised, you can delete the VPN connection and
        create a new one that has new keys, without needing to delete the VPC or virtual
        private gateway. If you create a new VPN connection, you must reconfigure the
        customer gateway using the new configuration information returned with the new
        VPN connection ID.
        """
        if _request is None:
            _params = {}
            if vpn_connection_id is not ShapeBase.NOT_SET:
                _params['vpn_connection_id'] = vpn_connection_id
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.DeleteVpnConnectionRequest(**_params)
        response = self._boto_client.delete_vpn_connection(**_request.to_boto())

    def delete_vpn_connection_route(
        self,
        _request: shapes.DeleteVpnConnectionRouteRequest = None,
        *,
        destination_cidr_block: str,
        vpn_connection_id: str,
    ) -> None:
        """
        Deletes the specified static route associated with a VPN connection between an
        existing virtual private gateway and a VPN customer gateway. The static route
        allows traffic to be routed from the virtual private gateway to the VPN customer
        gateway.
        """
        if _request is None:
            _params = {}
            if destination_cidr_block is not ShapeBase.NOT_SET:
                _params['destination_cidr_block'] = destination_cidr_block
            if vpn_connection_id is not ShapeBase.NOT_SET:
                _params['vpn_connection_id'] = vpn_connection_id
            _request = shapes.DeleteVpnConnectionRouteRequest(**_params)
        response = self._boto_client.delete_vpn_connection_route(
            **_request.to_boto()
        )

    def delete_vpn_gateway(
        self,
        _request: shapes.DeleteVpnGatewayRequest = None,
        *,
        vpn_gateway_id: str,
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> None:
        """
        Deletes the specified virtual private gateway. We recommend that before you
        delete a virtual private gateway, you detach it from the VPC and delete the VPN
        connection. Note that you don't need to delete the virtual private gateway if
        you plan to delete and recreate the VPN connection between your VPC and your
        network.
        """
        if _request is None:
            _params = {}
            if vpn_gateway_id is not ShapeBase.NOT_SET:
                _params['vpn_gateway_id'] = vpn_gateway_id
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.DeleteVpnGatewayRequest(**_params)
        response = self._boto_client.delete_vpn_gateway(**_request.to_boto())

    def deregister_image(
        self,
        _request: shapes.DeregisterImageRequest = None,
        *,
        image_id: str,
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> None:
        """
        Deregisters the specified AMI. After you deregister an AMI, it can't be used to
        launch new instances; however, it doesn't affect any instances that you've
        already launched from the AMI. You'll continue to incur usage costs for those
        instances until you terminate them.

        When you deregister an Amazon EBS-backed AMI, it doesn't affect the snapshot
        that was created for the root volume of the instance during the AMI creation
        process. When you deregister an instance store-backed AMI, it doesn't affect the
        files that you uploaded to Amazon S3 when you created the AMI.
        """
        if _request is None:
            _params = {}
            if image_id is not ShapeBase.NOT_SET:
                _params['image_id'] = image_id
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.DeregisterImageRequest(**_params)
        response = self._boto_client.deregister_image(**_request.to_boto())

    def describe_account_attributes(
        self,
        _request: shapes.DescribeAccountAttributesRequest = None,
        *,
        attribute_names: typing.List[
            typing.Union[str, shapes.AccountAttributeName]] = ShapeBase.NOT_SET,
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> shapes.DescribeAccountAttributesResult:
        """
        Describes attributes of your AWS account. The following are the supported
        account attributes:

          * `supported-platforms`: Indicates whether your account can launch instances into EC2-Classic and EC2-VPC, or only into EC2-VPC.

          * `default-vpc`: The ID of the default VPC for your account, or `none`.

          * `max-instances`: The maximum number of On-Demand Instances that you can run.

          * `vpc-max-security-groups-per-interface`: The maximum number of security groups that you can assign to a network interface.

          * `max-elastic-ips`: The maximum number of Elastic IP addresses that you can allocate for use with EC2-Classic. 

          * `vpc-max-elastic-ips`: The maximum number of Elastic IP addresses that you can allocate for use with EC2-VPC.
        """
        if _request is None:
            _params = {}
            if attribute_names is not ShapeBase.NOT_SET:
                _params['attribute_names'] = attribute_names
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.DescribeAccountAttributesRequest(**_params)
        response = self._boto_client.describe_account_attributes(
            **_request.to_boto()
        )

        return shapes.DescribeAccountAttributesResult.from_boto(response)

    def describe_addresses(
        self,
        _request: shapes.DescribeAddressesRequest = None,
        *,
        filters: typing.List[shapes.Filter] = ShapeBase.NOT_SET,
        public_ips: typing.List[str] = ShapeBase.NOT_SET,
        allocation_ids: typing.List[str] = ShapeBase.NOT_SET,
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> shapes.DescribeAddressesResult:
        """
        Describes one or more of your Elastic IP addresses.

        An Elastic IP address is for use in either the EC2-Classic platform or in a VPC.
        For more information, see [Elastic IP
        Addresses](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-
        addresses-eip.html) in the _Amazon Elastic Compute Cloud User Guide_.
        """
        if _request is None:
            _params = {}
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if public_ips is not ShapeBase.NOT_SET:
                _params['public_ips'] = public_ips
            if allocation_ids is not ShapeBase.NOT_SET:
                _params['allocation_ids'] = allocation_ids
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.DescribeAddressesRequest(**_params)
        response = self._boto_client.describe_addresses(**_request.to_boto())

        return shapes.DescribeAddressesResult.from_boto(response)

    def describe_aggregate_id_format(
        self,
        _request: shapes.DescribeAggregateIdFormatRequest = None,
        *,
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> shapes.DescribeAggregateIdFormatResult:
        """
        Describes the longer ID format settings for all resource types in a specific
        region. This request is useful for performing a quick audit to determine whether
        a specific region is fully opted in for longer IDs (17-character IDs).

        This request only returns information about resource types that support longer
        IDs.

        The following resource types support longer IDs: `bundle` | `conversion-task` |
        `customer-gateway` | `dhcp-options` | `elastic-ip-allocation` | `elastic-ip-
        association` | `export-task` | `flow-log` | `image` | `import-task` | `instance`
        | `internet-gateway` | `network-acl` | `network-acl-association` | `network-
        interface` | `network-interface-attachment` | `prefix-list` | `reservation` |
        `route-table` | `route-table-association` | `security-group` | `snapshot` |
        `subnet` | `subnet-cidr-block-association` | `volume` | `vpc` | `vpc-cidr-block-
        association` | `vpc-endpoint` | `vpc-peering-connection` | `vpn-connection` |
        `vpn-gateway`.
        """
        if _request is None:
            _params = {}
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.DescribeAggregateIdFormatRequest(**_params)
        response = self._boto_client.describe_aggregate_id_format(
            **_request.to_boto()
        )

        return shapes.DescribeAggregateIdFormatResult.from_boto(response)

    def describe_availability_zones(
        self,
        _request: shapes.DescribeAvailabilityZonesRequest = None,
        *,
        filters: typing.List[shapes.Filter] = ShapeBase.NOT_SET,
        zone_names: typing.List[str] = ShapeBase.NOT_SET,
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> shapes.DescribeAvailabilityZonesResult:
        """
        Describes one or more of the Availability Zones that are available to you. The
        results include zones only for the region you're currently using. If there is an
        event impacting an Availability Zone, you can use this request to view the state
        and any provided message for that Availability Zone.

        For more information, see [Regions and Availability
        Zones](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-
        availability-zones.html) in the _Amazon Elastic Compute Cloud User Guide_.
        """
        if _request is None:
            _params = {}
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if zone_names is not ShapeBase.NOT_SET:
                _params['zone_names'] = zone_names
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.DescribeAvailabilityZonesRequest(**_params)
        response = self._boto_client.describe_availability_zones(
            **_request.to_boto()
        )

        return shapes.DescribeAvailabilityZonesResult.from_boto(response)

    def describe_bundle_tasks(
        self,
        _request: shapes.DescribeBundleTasksRequest = None,
        *,
        bundle_ids: typing.List[str] = ShapeBase.NOT_SET,
        filters: typing.List[shapes.Filter] = ShapeBase.NOT_SET,
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> shapes.DescribeBundleTasksResult:
        """
        Describes one or more of your bundling tasks.

        Completed bundle tasks are listed for only a limited time. If your bundle task
        is no longer in the list, you can still register an AMI from it. Just use
        `RegisterImage` with the Amazon S3 bucket name and image manifest name you
        provided to the bundle task.
        """
        if _request is None:
            _params = {}
            if bundle_ids is not ShapeBase.NOT_SET:
                _params['bundle_ids'] = bundle_ids
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.DescribeBundleTasksRequest(**_params)
        response = self._boto_client.describe_bundle_tasks(**_request.to_boto())

        return shapes.DescribeBundleTasksResult.from_boto(response)

    def describe_classic_link_instances(
        self,
        _request: shapes.DescribeClassicLinkInstancesRequest = None,
        *,
        filters: typing.List[shapes.Filter] = ShapeBase.NOT_SET,
        dry_run: bool = ShapeBase.NOT_SET,
        instance_ids: typing.List[str] = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeClassicLinkInstancesResult:
        """
        Describes one or more of your linked EC2-Classic instances. This request only
        returns information about EC2-Classic instances linked to a VPC through
        ClassicLink. You cannot use this request to return information about other
        instances.
        """
        if _request is None:
            _params = {}
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            if instance_ids is not ShapeBase.NOT_SET:
                _params['instance_ids'] = instance_ids
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.DescribeClassicLinkInstancesRequest(**_params)
        response = self._boto_client.describe_classic_link_instances(
            **_request.to_boto()
        )

        return shapes.DescribeClassicLinkInstancesResult.from_boto(response)

    def describe_conversion_tasks(
        self,
        _request: shapes.DescribeConversionTasksRequest = None,
        *,
        conversion_task_ids: typing.List[str] = ShapeBase.NOT_SET,
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> shapes.DescribeConversionTasksResult:
        """
        Describes one or more of your conversion tasks. For more information, see the
        [VM Import/Export User Guide](http://docs.aws.amazon.com/vm-
        import/latest/userguide/).

        For information about the import manifest referenced by this API action, see [VM
        Import
        Manifest](http://docs.aws.amazon.com/AWSEC2/latest/APIReference/manifest.html).
        """
        if _request is None:
            _params = {}
            if conversion_task_ids is not ShapeBase.NOT_SET:
                _params['conversion_task_ids'] = conversion_task_ids
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.DescribeConversionTasksRequest(**_params)
        response = self._boto_client.describe_conversion_tasks(
            **_request.to_boto()
        )

        return shapes.DescribeConversionTasksResult.from_boto(response)

    def describe_customer_gateways(
        self,
        _request: shapes.DescribeCustomerGatewaysRequest = None,
        *,
        customer_gateway_ids: typing.List[str] = ShapeBase.NOT_SET,
        filters: typing.List[shapes.Filter] = ShapeBase.NOT_SET,
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> shapes.DescribeCustomerGatewaysResult:
        """
        Describes one or more of your VPN customer gateways.

        For more information about VPN customer gateways, see [AWS Managed VPN
        Connections](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_VPN.html)
        in the _Amazon Virtual Private Cloud User Guide_.
        """
        if _request is None:
            _params = {}
            if customer_gateway_ids is not ShapeBase.NOT_SET:
                _params['customer_gateway_ids'] = customer_gateway_ids
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.DescribeCustomerGatewaysRequest(**_params)
        response = self._boto_client.describe_customer_gateways(
            **_request.to_boto()
        )

        return shapes.DescribeCustomerGatewaysResult.from_boto(response)

    def describe_dhcp_options(
        self,
        _request: shapes.DescribeDhcpOptionsRequest = None,
        *,
        dhcp_options_ids: typing.List[str] = ShapeBase.NOT_SET,
        filters: typing.List[shapes.Filter] = ShapeBase.NOT_SET,
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> shapes.DescribeDhcpOptionsResult:
        """
        Describes one or more of your DHCP options sets.

        For more information, see [DHCP Options
        Sets](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_DHCP_Options.html)
        in the _Amazon Virtual Private Cloud User Guide_.
        """
        if _request is None:
            _params = {}
            if dhcp_options_ids is not ShapeBase.NOT_SET:
                _params['dhcp_options_ids'] = dhcp_options_ids
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.DescribeDhcpOptionsRequest(**_params)
        response = self._boto_client.describe_dhcp_options(**_request.to_boto())

        return shapes.DescribeDhcpOptionsResult.from_boto(response)

    def describe_egress_only_internet_gateways(
        self,
        _request: shapes.DescribeEgressOnlyInternetGatewaysRequest = None,
        *,
        dry_run: bool = ShapeBase.NOT_SET,
        egress_only_internet_gateway_ids: typing.List[str] = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeEgressOnlyInternetGatewaysResult:
        """
        Describes one or more of your egress-only internet gateways.
        """
        if _request is None:
            _params = {}
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            if egress_only_internet_gateway_ids is not ShapeBase.NOT_SET:
                _params['egress_only_internet_gateway_ids'
                       ] = egress_only_internet_gateway_ids
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.DescribeEgressOnlyInternetGatewaysRequest(
                **_params
            )
        response = self._boto_client.describe_egress_only_internet_gateways(
            **_request.to_boto()
        )

        return shapes.DescribeEgressOnlyInternetGatewaysResult.from_boto(
            response
        )

    def describe_elastic_gpus(
        self,
        _request: shapes.DescribeElasticGpusRequest = None,
        *,
        elastic_gpu_ids: typing.List[str] = ShapeBase.NOT_SET,
        dry_run: bool = ShapeBase.NOT_SET,
        filters: typing.List[shapes.Filter] = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeElasticGpusResult:
        """
        Describes the Elastic GPUs associated with your instances. For more information
        about Elastic GPUs, see [Amazon EC2 Elastic
        GPUs](http://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/elastic-gpus.html).
        """
        if _request is None:
            _params = {}
            if elastic_gpu_ids is not ShapeBase.NOT_SET:
                _params['elastic_gpu_ids'] = elastic_gpu_ids
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.DescribeElasticGpusRequest(**_params)
        response = self._boto_client.describe_elastic_gpus(**_request.to_boto())

        return shapes.DescribeElasticGpusResult.from_boto(response)

    def describe_export_tasks(
        self,
        _request: shapes.DescribeExportTasksRequest = None,
        *,
        export_task_ids: typing.List[str] = ShapeBase.NOT_SET,
    ) -> shapes.DescribeExportTasksResult:
        """
        Describes one or more of your export tasks.
        """
        if _request is None:
            _params = {}
            if export_task_ids is not ShapeBase.NOT_SET:
                _params['export_task_ids'] = export_task_ids
            _request = shapes.DescribeExportTasksRequest(**_params)
        response = self._boto_client.describe_export_tasks(**_request.to_boto())

        return shapes.DescribeExportTasksResult.from_boto(response)

    def describe_fleet_history(
        self,
        _request: shapes.DescribeFleetHistoryRequest = None,
        *,
        fleet_id: str,
        start_time: datetime.datetime,
        dry_run: bool = ShapeBase.NOT_SET,
        event_type: typing.Union[str, shapes.FleetEventType] = ShapeBase.
        NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeFleetHistoryResult:
        """
        Describes the events for the specified EC2 Fleet during the specified time.
        """
        if _request is None:
            _params = {}
            if fleet_id is not ShapeBase.NOT_SET:
                _params['fleet_id'] = fleet_id
            if start_time is not ShapeBase.NOT_SET:
                _params['start_time'] = start_time
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            if event_type is not ShapeBase.NOT_SET:
                _params['event_type'] = event_type
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.DescribeFleetHistoryRequest(**_params)
        response = self._boto_client.describe_fleet_history(
            **_request.to_boto()
        )

        return shapes.DescribeFleetHistoryResult.from_boto(response)

    def describe_fleet_instances(
        self,
        _request: shapes.DescribeFleetInstancesRequest = None,
        *,
        fleet_id: str,
        dry_run: bool = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        filters: typing.List[shapes.Filter] = ShapeBase.NOT_SET,
    ) -> shapes.DescribeFleetInstancesResult:
        """
        Describes the running instances for the specified EC2 Fleet.
        """
        if _request is None:
            _params = {}
            if fleet_id is not ShapeBase.NOT_SET:
                _params['fleet_id'] = fleet_id
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            _request = shapes.DescribeFleetInstancesRequest(**_params)
        response = self._boto_client.describe_fleet_instances(
            **_request.to_boto()
        )

        return shapes.DescribeFleetInstancesResult.from_boto(response)

    def describe_fleets(
        self,
        _request: shapes.DescribeFleetsRequest = None,
        *,
        dry_run: bool = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        fleet_ids: typing.List[str] = ShapeBase.NOT_SET,
        filters: typing.List[shapes.Filter] = ShapeBase.NOT_SET,
    ) -> shapes.DescribeFleetsResult:
        """
        Describes one or more of your EC2 Fleet.
        """
        if _request is None:
            _params = {}
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if fleet_ids is not ShapeBase.NOT_SET:
                _params['fleet_ids'] = fleet_ids
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            _request = shapes.DescribeFleetsRequest(**_params)
        response = self._boto_client.describe_fleets(**_request.to_boto())

        return shapes.DescribeFleetsResult.from_boto(response)

    def describe_flow_logs(
        self,
        _request: shapes.DescribeFlowLogsRequest = None,
        *,
        dry_run: bool = ShapeBase.NOT_SET,
        filter: typing.List[shapes.Filter] = ShapeBase.NOT_SET,
        flow_log_ids: typing.List[str] = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeFlowLogsResult:
        """
        Describes one or more flow logs. To view the information in your flow logs (the
        log streams for the network interfaces), you must use the CloudWatch Logs
        console or the CloudWatch Logs API.
        """
        if _request is None:
            _params = {}
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            if filter is not ShapeBase.NOT_SET:
                _params['filter'] = filter
            if flow_log_ids is not ShapeBase.NOT_SET:
                _params['flow_log_ids'] = flow_log_ids
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.DescribeFlowLogsRequest(**_params)
        response = self._boto_client.describe_flow_logs(**_request.to_boto())

        return shapes.DescribeFlowLogsResult.from_boto(response)

    def describe_fpga_image_attribute(
        self,
        _request: shapes.DescribeFpgaImageAttributeRequest = None,
        *,
        fpga_image_id: str,
        attribute: typing.Union[str, shapes.FpgaImageAttributeName],
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> shapes.DescribeFpgaImageAttributeResult:
        """
        Describes the specified attribute of the specified Amazon FPGA Image (AFI).
        """
        if _request is None:
            _params = {}
            if fpga_image_id is not ShapeBase.NOT_SET:
                _params['fpga_image_id'] = fpga_image_id
            if attribute is not ShapeBase.NOT_SET:
                _params['attribute'] = attribute
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.DescribeFpgaImageAttributeRequest(**_params)
        response = self._boto_client.describe_fpga_image_attribute(
            **_request.to_boto()
        )

        return shapes.DescribeFpgaImageAttributeResult.from_boto(response)

    def describe_fpga_images(
        self,
        _request: shapes.DescribeFpgaImagesRequest = None,
        *,
        dry_run: bool = ShapeBase.NOT_SET,
        fpga_image_ids: typing.List[str] = ShapeBase.NOT_SET,
        owners: typing.List[str] = ShapeBase.NOT_SET,
        filters: typing.List[shapes.Filter] = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.DescribeFpgaImagesResult:
        """
        Describes one or more available Amazon FPGA Images (AFIs). These include public
        AFIs, private AFIs that you own, and AFIs owned by other AWS accounts for which
        you have load permissions.
        """
        if _request is None:
            _params = {}
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            if fpga_image_ids is not ShapeBase.NOT_SET:
                _params['fpga_image_ids'] = fpga_image_ids
            if owners is not ShapeBase.NOT_SET:
                _params['owners'] = owners
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.DescribeFpgaImagesRequest(**_params)
        response = self._boto_client.describe_fpga_images(**_request.to_boto())

        return shapes.DescribeFpgaImagesResult.from_boto(response)

    def describe_host_reservation_offerings(
        self,
        _request: shapes.DescribeHostReservationOfferingsRequest = None,
        *,
        filter: typing.List[shapes.Filter] = ShapeBase.NOT_SET,
        max_duration: int = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        min_duration: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        offering_id: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeHostReservationOfferingsResult:
        """
        Describes the Dedicated Host reservations that are available to purchase.

        The results describe all the Dedicated Host reservation offerings, including
        offerings that may not match the instance family and region of your Dedicated
        Hosts. When purchasing an offering, ensure that the instance family and Region
        of the offering matches that of the Dedicated Hosts with which it is to be
        associated. For more information about supported instance types, see [Dedicated
        Hosts Overview](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/dedicated-
        hosts-overview.html) in the _Amazon Elastic Compute Cloud User Guide_.
        """
        if _request is None:
            _params = {}
            if filter is not ShapeBase.NOT_SET:
                _params['filter'] = filter
            if max_duration is not ShapeBase.NOT_SET:
                _params['max_duration'] = max_duration
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if min_duration is not ShapeBase.NOT_SET:
                _params['min_duration'] = min_duration
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if offering_id is not ShapeBase.NOT_SET:
                _params['offering_id'] = offering_id
            _request = shapes.DescribeHostReservationOfferingsRequest(**_params)
        response = self._boto_client.describe_host_reservation_offerings(
            **_request.to_boto()
        )

        return shapes.DescribeHostReservationOfferingsResult.from_boto(response)

    def describe_host_reservations(
        self,
        _request: shapes.DescribeHostReservationsRequest = None,
        *,
        filter: typing.List[shapes.Filter] = ShapeBase.NOT_SET,
        host_reservation_id_set: typing.List[str] = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeHostReservationsResult:
        """
        Describes reservations that are associated with Dedicated Hosts in your account.
        """
        if _request is None:
            _params = {}
            if filter is not ShapeBase.NOT_SET:
                _params['filter'] = filter
            if host_reservation_id_set is not ShapeBase.NOT_SET:
                _params['host_reservation_id_set'] = host_reservation_id_set
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.DescribeHostReservationsRequest(**_params)
        response = self._boto_client.describe_host_reservations(
            **_request.to_boto()
        )

        return shapes.DescribeHostReservationsResult.from_boto(response)

    def describe_hosts(
        self,
        _request: shapes.DescribeHostsRequest = None,
        *,
        filter: typing.List[shapes.Filter] = ShapeBase.NOT_SET,
        host_ids: typing.List[str] = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeHostsResult:
        """
        Describes one or more of your Dedicated Hosts.

        The results describe only the Dedicated Hosts in the region you're currently
        using. All listed instances consume capacity on your Dedicated Host. Dedicated
        Hosts that have recently been released are listed with the state `released`.
        """
        if _request is None:
            _params = {}
            if filter is not ShapeBase.NOT_SET:
                _params['filter'] = filter
            if host_ids is not ShapeBase.NOT_SET:
                _params['host_ids'] = host_ids
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.DescribeHostsRequest(**_params)
        response = self._boto_client.describe_hosts(**_request.to_boto())

        return shapes.DescribeHostsResult.from_boto(response)

    def describe_iam_instance_profile_associations(
        self,
        _request: shapes.DescribeIamInstanceProfileAssociationsRequest = None,
        *,
        association_ids: typing.List[str] = ShapeBase.NOT_SET,
        filters: typing.List[shapes.Filter] = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeIamInstanceProfileAssociationsResult:
        """
        Describes your IAM instance profile associations.
        """
        if _request is None:
            _params = {}
            if association_ids is not ShapeBase.NOT_SET:
                _params['association_ids'] = association_ids
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.DescribeIamInstanceProfileAssociationsRequest(
                **_params
            )
        paginator = self.get_paginator(
            "describe_iam_instance_profile_associations"
        ).paginate(**_request.to_boto())
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.DescribeIamInstanceProfileAssociationsResult.from_boto(
            first_page
        )
        result._page_iterator = page_generator
        return result

        return shapes.DescribeIamInstanceProfileAssociationsResult.from_boto(
            response
        )

    def describe_id_format(
        self,
        _request: shapes.DescribeIdFormatRequest = None,
        *,
        resource: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeIdFormatResult:
        """
        Describes the ID format settings for your resources on a per-region basis, for
        example, to view which resource types are enabled for longer IDs. This request
        only returns information about resource types whose ID formats can be modified;
        it does not return information about other resource types.

        The following resource types support longer IDs: `bundle` | `conversion-task` |
        `customer-gateway` | `dhcp-options` | `elastic-ip-allocation` | `elastic-ip-
        association` | `export-task` | `flow-log` | `image` | `import-task` | `instance`
        | `internet-gateway` | `network-acl` | `network-acl-association` | `network-
        interface` | `network-interface-attachment` | `prefix-list` | `reservation` |
        `route-table` | `route-table-association` | `security-group` | `snapshot` |
        `subnet` | `subnet-cidr-block-association` | `volume` | `vpc` | `vpc-cidr-block-
        association` | `vpc-endpoint` | `vpc-peering-connection` | `vpn-connection` |
        `vpn-gateway`.

        These settings apply to the IAM user who makes the request; they do not apply to
        the entire AWS account. By default, an IAM user defaults to the same settings as
        the root user, unless they explicitly override the settings by running the
        ModifyIdFormat command. Resources created with longer IDs are visible to all IAM
        users, regardless of these settings and provided that they have permission to
        use the relevant `Describe` command for the resource type.
        """
        if _request is None:
            _params = {}
            if resource is not ShapeBase.NOT_SET:
                _params['resource'] = resource
            _request = shapes.DescribeIdFormatRequest(**_params)
        response = self._boto_client.describe_id_format(**_request.to_boto())

        return shapes.DescribeIdFormatResult.from_boto(response)

    def describe_identity_id_format(
        self,
        _request: shapes.DescribeIdentityIdFormatRequest = None,
        *,
        principal_arn: str,
        resource: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeIdentityIdFormatResult:
        """
        Describes the ID format settings for resources for the specified IAM user, IAM
        role, or root user. For example, you can view the resource types that are
        enabled for longer IDs. This request only returns information about resource
        types whose ID formats can be modified; it does not return information about
        other resource types. For more information, see [Resource
        IDs](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/resource-ids.html) in
        the _Amazon Elastic Compute Cloud User Guide_.

        The following resource types support longer IDs: `bundle` | `conversion-task` |
        `customer-gateway` | `dhcp-options` | `elastic-ip-allocation` | `elastic-ip-
        association` | `export-task` | `flow-log` | `image` | `import-task` | `instance`
        | `internet-gateway` | `network-acl` | `network-acl-association` | `network-
        interface` | `network-interface-attachment` | `prefix-list` | `reservation` |
        `route-table` | `route-table-association` | `security-group` | `snapshot` |
        `subnet` | `subnet-cidr-block-association` | `volume` | `vpc` | `vpc-cidr-block-
        association` | `vpc-endpoint` | `vpc-peering-connection` | `vpn-connection` |
        `vpn-gateway`.

        These settings apply to the principal specified in the request. They do not
        apply to the principal that makes the request.
        """
        if _request is None:
            _params = {}
            if principal_arn is not ShapeBase.NOT_SET:
                _params['principal_arn'] = principal_arn
            if resource is not ShapeBase.NOT_SET:
                _params['resource'] = resource
            _request = shapes.DescribeIdentityIdFormatRequest(**_params)
        response = self._boto_client.describe_identity_id_format(
            **_request.to_boto()
        )

        return shapes.DescribeIdentityIdFormatResult.from_boto(response)

    def describe_image_attribute(
        self,
        _request: shapes.DescribeImageAttributeRequest = None,
        *,
        attribute: typing.Union[str, shapes.ImageAttributeName],
        image_id: str,
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> shapes.ImageAttribute:
        """
        Describes the specified attribute of the specified AMI. You can specify only one
        attribute at a time.
        """
        if _request is None:
            _params = {}
            if attribute is not ShapeBase.NOT_SET:
                _params['attribute'] = attribute
            if image_id is not ShapeBase.NOT_SET:
                _params['image_id'] = image_id
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.DescribeImageAttributeRequest(**_params)
        response = self._boto_client.describe_image_attribute(
            **_request.to_boto()
        )

        return shapes.ImageAttribute.from_boto(response)

    def describe_images(
        self,
        _request: shapes.DescribeImagesRequest = None,
        *,
        executable_users: typing.List[str] = ShapeBase.NOT_SET,
        filters: typing.List[shapes.Filter] = ShapeBase.NOT_SET,
        image_ids: typing.List[str] = ShapeBase.NOT_SET,
        owners: typing.List[str] = ShapeBase.NOT_SET,
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> shapes.DescribeImagesResult:
        """
        Describes one or more of the images (AMIs, AKIs, and ARIs) available to you.
        Images available to you include public images, private images that you own, and
        private images owned by other AWS accounts but for which you have explicit
        launch permissions.

        Deregistered images are included in the returned results for an unspecified
        interval after deregistration.
        """
        if _request is None:
            _params = {}
            if executable_users is not ShapeBase.NOT_SET:
                _params['executable_users'] = executable_users
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if image_ids is not ShapeBase.NOT_SET:
                _params['image_ids'] = image_ids
            if owners is not ShapeBase.NOT_SET:
                _params['owners'] = owners
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.DescribeImagesRequest(**_params)
        response = self._boto_client.describe_images(**_request.to_boto())

        return shapes.DescribeImagesResult.from_boto(response)

    def describe_import_image_tasks(
        self,
        _request: shapes.DescribeImportImageTasksRequest = None,
        *,
        dry_run: bool = ShapeBase.NOT_SET,
        filters: typing.List[shapes.Filter] = ShapeBase.NOT_SET,
        import_task_ids: typing.List[str] = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeImportImageTasksResult:
        """
        Displays details about an import virtual machine or import snapshot tasks that
        are already created.
        """
        if _request is None:
            _params = {}
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if import_task_ids is not ShapeBase.NOT_SET:
                _params['import_task_ids'] = import_task_ids
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.DescribeImportImageTasksRequest(**_params)
        response = self._boto_client.describe_import_image_tasks(
            **_request.to_boto()
        )

        return shapes.DescribeImportImageTasksResult.from_boto(response)

    def describe_import_snapshot_tasks(
        self,
        _request: shapes.DescribeImportSnapshotTasksRequest = None,
        *,
        dry_run: bool = ShapeBase.NOT_SET,
        filters: typing.List[shapes.Filter] = ShapeBase.NOT_SET,
        import_task_ids: typing.List[str] = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeImportSnapshotTasksResult:
        """
        Describes your import snapshot tasks.
        """
        if _request is None:
            _params = {}
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if import_task_ids is not ShapeBase.NOT_SET:
                _params['import_task_ids'] = import_task_ids
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.DescribeImportSnapshotTasksRequest(**_params)
        response = self._boto_client.describe_import_snapshot_tasks(
            **_request.to_boto()
        )

        return shapes.DescribeImportSnapshotTasksResult.from_boto(response)

    def describe_instance_attribute(
        self,
        _request: shapes.DescribeInstanceAttributeRequest = None,
        *,
        attribute: typing.Union[str, shapes.InstanceAttributeName],
        instance_id: str,
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> shapes.InstanceAttribute:
        """
        Describes the specified attribute of the specified instance. You can specify
        only one attribute at a time. Valid attribute values are: `instanceType` |
        `kernel` | `ramdisk` | `userData` | `disableApiTermination` |
        `instanceInitiatedShutdownBehavior` | `rootDeviceName` | `blockDeviceMapping` |
        `productCodes` | `sourceDestCheck` | `groupSet` | `ebsOptimized` |
        `sriovNetSupport`
        """
        if _request is None:
            _params = {}
            if attribute is not ShapeBase.NOT_SET:
                _params['attribute'] = attribute
            if instance_id is not ShapeBase.NOT_SET:
                _params['instance_id'] = instance_id
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.DescribeInstanceAttributeRequest(**_params)
        response = self._boto_client.describe_instance_attribute(
            **_request.to_boto()
        )

        return shapes.InstanceAttribute.from_boto(response)

    def describe_instance_credit_specifications(
        self,
        _request: shapes.DescribeInstanceCreditSpecificationsRequest = None,
        *,
        dry_run: bool = ShapeBase.NOT_SET,
        filters: typing.List[shapes.Filter] = ShapeBase.NOT_SET,
        instance_ids: typing.List[str] = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeInstanceCreditSpecificationsResult:
        """
        Describes the credit option for CPU usage of one or more of your T2 or T3
        instances. The credit options are `standard` and `unlimited`.

        If you do not specify an instance ID, Amazon EC2 returns T2 and T3 instances
        with the `unlimited` credit option, as well as instances that were previously
        configured as T2 or T3 with the `unlimited` credit option. For example, if you
        resize a T2 instance, while it is configured as `unlimited`, to an M4 instance,
        Amazon EC2 returns the M4 instance.

        If you specify one or more instance IDs, Amazon EC2 returns the credit option
        (`standard` or `unlimited`) of those instances. If you specify an instance ID
        that is not valid, such as an instance that is not a T2 or T3 instance, an error
        is returned.

        Recently terminated instances might appear in the returned results. This
        interval is usually less than one hour.

        If an Availability Zone is experiencing a service disruption and you specify
        instance IDs in the affected zone, or do not specify any instance IDs at all,
        the call fails. If you specify only instance IDs in an unaffected zone, the call
        works normally.

        For more information, see [Burstable Performance
        Instances](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/burstable-
        performance-instances.html) in the _Amazon Elastic Compute Cloud User Guide_.
        """
        if _request is None:
            _params = {}
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if instance_ids is not ShapeBase.NOT_SET:
                _params['instance_ids'] = instance_ids
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.DescribeInstanceCreditSpecificationsRequest(
                **_params
            )
        response = self._boto_client.describe_instance_credit_specifications(
            **_request.to_boto()
        )

        return shapes.DescribeInstanceCreditSpecificationsResult.from_boto(
            response
        )

    def describe_instance_status(
        self,
        _request: shapes.DescribeInstanceStatusRequest = None,
        *,
        filters: typing.List[shapes.Filter] = ShapeBase.NOT_SET,
        instance_ids: typing.List[str] = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        dry_run: bool = ShapeBase.NOT_SET,
        include_all_instances: bool = ShapeBase.NOT_SET,
    ) -> shapes.DescribeInstanceStatusResult:
        """
        Describes the status of one or more instances. By default, only running
        instances are described, unless you specifically indicate to return the status
        of all instances.

        Instance status includes the following components:

          * **Status checks** \- Amazon EC2 performs status checks on running EC2 instances to identify hardware and software issues. For more information, see [Status Checks for Your Instances](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/monitoring-system-instance-status-check.html) and [Troubleshooting Instances with Failed Status Checks](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/TroubleshootingInstances.html) in the _Amazon Elastic Compute Cloud User Guide_.

          * **Scheduled events** \- Amazon EC2 can schedule events (such as reboot, stop, or terminate) for your instances related to hardware issues, software updates, or system maintenance. For more information, see [Scheduled Events for Your Instances](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/monitoring-instances-status-check_sched.html) in the _Amazon Elastic Compute Cloud User Guide_.

          * **Instance state** \- You can manage your instances from the moment you launch them through their termination. For more information, see [Instance Lifecycle](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-lifecycle.html) in the _Amazon Elastic Compute Cloud User Guide_.
        """
        if _request is None:
            _params = {}
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if instance_ids is not ShapeBase.NOT_SET:
                _params['instance_ids'] = instance_ids
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            if include_all_instances is not ShapeBase.NOT_SET:
                _params['include_all_instances'] = include_all_instances
            _request = shapes.DescribeInstanceStatusRequest(**_params)
        paginator = self.get_paginator("describe_instance_status").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.DescribeInstanceStatusResult.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.DescribeInstanceStatusResult.from_boto(response)

    def describe_instances(
        self,
        _request: shapes.DescribeInstancesRequest = None,
        *,
        filters: typing.List[shapes.Filter] = ShapeBase.NOT_SET,
        instance_ids: typing.List[str] = ShapeBase.NOT_SET,
        dry_run: bool = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeInstancesResult:
        """
        Describes one or more of your instances.

        If you specify one or more instance IDs, Amazon EC2 returns information for
        those instances. If you do not specify instance IDs, Amazon EC2 returns
        information for all relevant instances. If you specify an instance ID that is
        not valid, an error is returned. If you specify an instance that you do not own,
        it is not included in the returned results.

        Recently terminated instances might appear in the returned results. This
        interval is usually less than one hour.

        If you describe instances in the rare case where an Availability Zone is
        experiencing a service disruption and you specify instance IDs that are in the
        affected zone, or do not specify any instance IDs at all, the call fails. If you
        describe instances and specify only instance IDs that are in an unaffected zone,
        the call works normally.
        """
        if _request is None:
            _params = {}
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if instance_ids is not ShapeBase.NOT_SET:
                _params['instance_ids'] = instance_ids
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.DescribeInstancesRequest(**_params)
        paginator = self.get_paginator("describe_instances").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.DescribeInstancesResult.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.DescribeInstancesResult.from_boto(response)

    def describe_internet_gateways(
        self,
        _request: shapes.DescribeInternetGatewaysRequest = None,
        *,
        filters: typing.List[shapes.Filter] = ShapeBase.NOT_SET,
        dry_run: bool = ShapeBase.NOT_SET,
        internet_gateway_ids: typing.List[str] = ShapeBase.NOT_SET,
    ) -> shapes.DescribeInternetGatewaysResult:
        """
        Describes one or more of your internet gateways.
        """
        if _request is None:
            _params = {}
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            if internet_gateway_ids is not ShapeBase.NOT_SET:
                _params['internet_gateway_ids'] = internet_gateway_ids
            _request = shapes.DescribeInternetGatewaysRequest(**_params)
        response = self._boto_client.describe_internet_gateways(
            **_request.to_boto()
        )

        return shapes.DescribeInternetGatewaysResult.from_boto(response)

    def describe_key_pairs(
        self,
        _request: shapes.DescribeKeyPairsRequest = None,
        *,
        filters: typing.List[shapes.Filter] = ShapeBase.NOT_SET,
        key_names: typing.List[str] = ShapeBase.NOT_SET,
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> shapes.DescribeKeyPairsResult:
        """
        Describes one or more of your key pairs.

        For more information about key pairs, see [Key
        Pairs](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html) in
        the _Amazon Elastic Compute Cloud User Guide_.
        """
        if _request is None:
            _params = {}
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if key_names is not ShapeBase.NOT_SET:
                _params['key_names'] = key_names
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.DescribeKeyPairsRequest(**_params)
        response = self._boto_client.describe_key_pairs(**_request.to_boto())

        return shapes.DescribeKeyPairsResult.from_boto(response)

    def describe_launch_template_versions(
        self,
        _request: shapes.DescribeLaunchTemplateVersionsRequest = None,
        *,
        dry_run: bool = ShapeBase.NOT_SET,
        launch_template_id: str = ShapeBase.NOT_SET,
        launch_template_name: str = ShapeBase.NOT_SET,
        versions: typing.List[str] = ShapeBase.NOT_SET,
        min_version: str = ShapeBase.NOT_SET,
        max_version: str = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        filters: typing.List[shapes.Filter] = ShapeBase.NOT_SET,
    ) -> shapes.DescribeLaunchTemplateVersionsResult:
        """
        Describes one or more versions of a specified launch template. You can describe
        all versions, individual versions, or a range of versions.
        """
        if _request is None:
            _params = {}
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            if launch_template_id is not ShapeBase.NOT_SET:
                _params['launch_template_id'] = launch_template_id
            if launch_template_name is not ShapeBase.NOT_SET:
                _params['launch_template_name'] = launch_template_name
            if versions is not ShapeBase.NOT_SET:
                _params['versions'] = versions
            if min_version is not ShapeBase.NOT_SET:
                _params['min_version'] = min_version
            if max_version is not ShapeBase.NOT_SET:
                _params['max_version'] = max_version
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            _request = shapes.DescribeLaunchTemplateVersionsRequest(**_params)
        response = self._boto_client.describe_launch_template_versions(
            **_request.to_boto()
        )

        return shapes.DescribeLaunchTemplateVersionsResult.from_boto(response)

    def describe_launch_templates(
        self,
        _request: shapes.DescribeLaunchTemplatesRequest = None,
        *,
        dry_run: bool = ShapeBase.NOT_SET,
        launch_template_ids: typing.List[str] = ShapeBase.NOT_SET,
        launch_template_names: typing.List[str] = ShapeBase.NOT_SET,
        filters: typing.List[shapes.Filter] = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.DescribeLaunchTemplatesResult:
        """
        Describes one or more launch templates.
        """
        if _request is None:
            _params = {}
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            if launch_template_ids is not ShapeBase.NOT_SET:
                _params['launch_template_ids'] = launch_template_ids
            if launch_template_names is not ShapeBase.NOT_SET:
                _params['launch_template_names'] = launch_template_names
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.DescribeLaunchTemplatesRequest(**_params)
        response = self._boto_client.describe_launch_templates(
            **_request.to_boto()
        )

        return shapes.DescribeLaunchTemplatesResult.from_boto(response)

    def describe_moving_addresses(
        self,
        _request: shapes.DescribeMovingAddressesRequest = None,
        *,
        filters: typing.List[shapes.Filter] = ShapeBase.NOT_SET,
        dry_run: bool = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        public_ips: typing.List[str] = ShapeBase.NOT_SET,
    ) -> shapes.DescribeMovingAddressesResult:
        """
        Describes your Elastic IP addresses that are being moved to the EC2-VPC
        platform, or that are being restored to the EC2-Classic platform. This request
        does not return information about any other Elastic IP addresses in your
        account.
        """
        if _request is None:
            _params = {}
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if public_ips is not ShapeBase.NOT_SET:
                _params['public_ips'] = public_ips
            _request = shapes.DescribeMovingAddressesRequest(**_params)
        response = self._boto_client.describe_moving_addresses(
            **_request.to_boto()
        )

        return shapes.DescribeMovingAddressesResult.from_boto(response)

    def describe_nat_gateways(
        self,
        _request: shapes.DescribeNatGatewaysRequest = None,
        *,
        filter: typing.List[shapes.Filter] = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        nat_gateway_ids: typing.List[str] = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeNatGatewaysResult:
        """
        Describes one or more of your NAT gateways.
        """
        if _request is None:
            _params = {}
            if filter is not ShapeBase.NOT_SET:
                _params['filter'] = filter
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if nat_gateway_ids is not ShapeBase.NOT_SET:
                _params['nat_gateway_ids'] = nat_gateway_ids
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.DescribeNatGatewaysRequest(**_params)
        paginator = self.get_paginator("describe_nat_gateways").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.DescribeNatGatewaysResult.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.DescribeNatGatewaysResult.from_boto(response)

    def describe_network_acls(
        self,
        _request: shapes.DescribeNetworkAclsRequest = None,
        *,
        filters: typing.List[shapes.Filter] = ShapeBase.NOT_SET,
        dry_run: bool = ShapeBase.NOT_SET,
        network_acl_ids: typing.List[str] = ShapeBase.NOT_SET,
    ) -> shapes.DescribeNetworkAclsResult:
        """
        Describes one or more of your network ACLs.

        For more information, see [Network
        ACLs](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_ACLs.html) in
        the _Amazon Virtual Private Cloud User Guide_.
        """
        if _request is None:
            _params = {}
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            if network_acl_ids is not ShapeBase.NOT_SET:
                _params['network_acl_ids'] = network_acl_ids
            _request = shapes.DescribeNetworkAclsRequest(**_params)
        response = self._boto_client.describe_network_acls(**_request.to_boto())

        return shapes.DescribeNetworkAclsResult.from_boto(response)

    def describe_network_interface_attribute(
        self,
        _request: shapes.DescribeNetworkInterfaceAttributeRequest = None,
        *,
        network_interface_id: str,
        attribute: typing.Union[str, shapes.
                                NetworkInterfaceAttribute] = ShapeBase.NOT_SET,
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> shapes.DescribeNetworkInterfaceAttributeResult:
        """
        Describes a network interface attribute. You can specify only one attribute at a
        time.
        """
        if _request is None:
            _params = {}
            if network_interface_id is not ShapeBase.NOT_SET:
                _params['network_interface_id'] = network_interface_id
            if attribute is not ShapeBase.NOT_SET:
                _params['attribute'] = attribute
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.DescribeNetworkInterfaceAttributeRequest(
                **_params
            )
        response = self._boto_client.describe_network_interface_attribute(
            **_request.to_boto()
        )

        return shapes.DescribeNetworkInterfaceAttributeResult.from_boto(
            response
        )

    def describe_network_interface_permissions(
        self,
        _request: shapes.DescribeNetworkInterfacePermissionsRequest = None,
        *,
        network_interface_permission_ids: typing.List[str] = ShapeBase.NOT_SET,
        filters: typing.List[shapes.Filter] = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.DescribeNetworkInterfacePermissionsResult:
        """
        Describes the permissions for your network interfaces.
        """
        if _request is None:
            _params = {}
            if network_interface_permission_ids is not ShapeBase.NOT_SET:
                _params['network_interface_permission_ids'
                       ] = network_interface_permission_ids
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.DescribeNetworkInterfacePermissionsRequest(
                **_params
            )
        response = self._boto_client.describe_network_interface_permissions(
            **_request.to_boto()
        )

        return shapes.DescribeNetworkInterfacePermissionsResult.from_boto(
            response
        )

    def describe_network_interfaces(
        self,
        _request: shapes.DescribeNetworkInterfacesRequest = None,
        *,
        filters: typing.List[shapes.Filter] = ShapeBase.NOT_SET,
        dry_run: bool = ShapeBase.NOT_SET,
        network_interface_ids: typing.List[str] = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.DescribeNetworkInterfacesResult:
        """
        Describes one or more of your network interfaces.
        """
        if _request is None:
            _params = {}
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            if network_interface_ids is not ShapeBase.NOT_SET:
                _params['network_interface_ids'] = network_interface_ids
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.DescribeNetworkInterfacesRequest(**_params)
        paginator = self.get_paginator("describe_network_interfaces").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.DescribeNetworkInterfacesResult.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.DescribeNetworkInterfacesResult.from_boto(response)

    def describe_placement_groups(
        self,
        _request: shapes.DescribePlacementGroupsRequest = None,
        *,
        filters: typing.List[shapes.Filter] = ShapeBase.NOT_SET,
        dry_run: bool = ShapeBase.NOT_SET,
        group_names: typing.List[str] = ShapeBase.NOT_SET,
    ) -> shapes.DescribePlacementGroupsResult:
        """
        Describes one or more of your placement groups. For more information, see
        [Placement Groups](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-
        groups.html) in the _Amazon Elastic Compute Cloud User Guide_.
        """
        if _request is None:
            _params = {}
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            if group_names is not ShapeBase.NOT_SET:
                _params['group_names'] = group_names
            _request = shapes.DescribePlacementGroupsRequest(**_params)
        response = self._boto_client.describe_placement_groups(
            **_request.to_boto()
        )

        return shapes.DescribePlacementGroupsResult.from_boto(response)

    def describe_prefix_lists(
        self,
        _request: shapes.DescribePrefixListsRequest = None,
        *,
        dry_run: bool = ShapeBase.NOT_SET,
        filters: typing.List[shapes.Filter] = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        prefix_list_ids: typing.List[str] = ShapeBase.NOT_SET,
    ) -> shapes.DescribePrefixListsResult:
        """
        Describes available AWS services in a prefix list format, which includes the
        prefix list name and prefix list ID of the service and the IP address range for
        the service. A prefix list ID is required for creating an outbound security
        group rule that allows traffic from a VPC to access an AWS service through a
        gateway VPC endpoint. Currently, the services that support this action are
        Amazon S3 and Amazon DynamoDB.
        """
        if _request is None:
            _params = {}
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if prefix_list_ids is not ShapeBase.NOT_SET:
                _params['prefix_list_ids'] = prefix_list_ids
            _request = shapes.DescribePrefixListsRequest(**_params)
        response = self._boto_client.describe_prefix_lists(**_request.to_boto())

        return shapes.DescribePrefixListsResult.from_boto(response)

    def describe_principal_id_format(
        self,
        _request: shapes.DescribePrincipalIdFormatRequest = None,
        *,
        dry_run: bool = ShapeBase.NOT_SET,
        resources: typing.List[str] = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribePrincipalIdFormatResult:
        """
        Describes the ID format settings for the root user and all IAM roles and IAM
        users that have explicitly specified a longer ID (17-character ID) preference.

        By default, all IAM roles and IAM users default to the same ID settings as the
        root user, unless they explicitly override the settings. This request is useful
        for identifying those IAM users and IAM roles that have overridden the default
        ID settings.

        The following resource types support longer IDs: `bundle` | `conversion-task` |
        `customer-gateway` | `dhcp-options` | `elastic-ip-allocation` | `elastic-ip-
        association` | `export-task` | `flow-log` | `image` | `import-task` | `instance`
        | `internet-gateway` | `network-acl` | `network-acl-association` | `network-
        interface` | `network-interface-attachment` | `prefix-list` | `reservation` |
        `route-table` | `route-table-association` | `security-group` | `snapshot` |
        `subnet` | `subnet-cidr-block-association` | `volume` | `vpc` | `vpc-cidr-block-
        association` | `vpc-endpoint` | `vpc-peering-connection` | `vpn-connection` |
        `vpn-gateway`.
        """
        if _request is None:
            _params = {}
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            if resources is not ShapeBase.NOT_SET:
                _params['resources'] = resources
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.DescribePrincipalIdFormatRequest(**_params)
        response = self._boto_client.describe_principal_id_format(
            **_request.to_boto()
        )

        return shapes.DescribePrincipalIdFormatResult.from_boto(response)

    def describe_regions(
        self,
        _request: shapes.DescribeRegionsRequest = None,
        *,
        filters: typing.List[shapes.Filter] = ShapeBase.NOT_SET,
        region_names: typing.List[str] = ShapeBase.NOT_SET,
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> shapes.DescribeRegionsResult:
        """
        Describes one or more regions that are currently available to you.

        For a list of the regions supported by Amazon EC2, see [Regions and
        Endpoints](http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region).
        """
        if _request is None:
            _params = {}
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if region_names is not ShapeBase.NOT_SET:
                _params['region_names'] = region_names
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.DescribeRegionsRequest(**_params)
        response = self._boto_client.describe_regions(**_request.to_boto())

        return shapes.DescribeRegionsResult.from_boto(response)

    def describe_reserved_instances(
        self,
        _request: shapes.DescribeReservedInstancesRequest = None,
        *,
        filters: typing.List[shapes.Filter] = ShapeBase.NOT_SET,
        offering_class: typing.Union[str, shapes.
                                     OfferingClassType] = ShapeBase.NOT_SET,
        reserved_instances_ids: typing.List[str] = ShapeBase.NOT_SET,
        dry_run: bool = ShapeBase.NOT_SET,
        offering_type: typing.Union[str, shapes.OfferingTypeValues] = ShapeBase.
        NOT_SET,
    ) -> shapes.DescribeReservedInstancesResult:
        """
        Describes one or more of the Reserved Instances that you purchased.

        For more information about Reserved Instances, see [Reserved
        Instances](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts-on-
        demand-reserved-instances.html) in the _Amazon Elastic Compute Cloud User
        Guide_.
        """
        if _request is None:
            _params = {}
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if offering_class is not ShapeBase.NOT_SET:
                _params['offering_class'] = offering_class
            if reserved_instances_ids is not ShapeBase.NOT_SET:
                _params['reserved_instances_ids'] = reserved_instances_ids
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            if offering_type is not ShapeBase.NOT_SET:
                _params['offering_type'] = offering_type
            _request = shapes.DescribeReservedInstancesRequest(**_params)
        response = self._boto_client.describe_reserved_instances(
            **_request.to_boto()
        )

        return shapes.DescribeReservedInstancesResult.from_boto(response)

    def describe_reserved_instances_listings(
        self,
        _request: shapes.DescribeReservedInstancesListingsRequest = None,
        *,
        filters: typing.List[shapes.Filter] = ShapeBase.NOT_SET,
        reserved_instances_id: str = ShapeBase.NOT_SET,
        reserved_instances_listing_id: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeReservedInstancesListingsResult:
        """
        Describes your account's Reserved Instance listings in the Reserved Instance
        Marketplace.

        The Reserved Instance Marketplace matches sellers who want to resell Reserved
        Instance capacity that they no longer need with buyers who want to purchase
        additional capacity. Reserved Instances bought and sold through the Reserved
        Instance Marketplace work like any other Reserved Instances.

        As a seller, you choose to list some or all of your Reserved Instances, and you
        specify the upfront price to receive for them. Your Reserved Instances are then
        listed in the Reserved Instance Marketplace and are available for purchase.

        As a buyer, you specify the configuration of the Reserved Instance to purchase,
        and the Marketplace matches what you're searching for with what's available. The
        Marketplace first sells the lowest priced Reserved Instances to you, and
        continues to sell available Reserved Instance listings to you until your demand
        is met. You are charged based on the total price of all of the listings that you
        purchase.

        For more information, see [Reserved Instance
        Marketplace](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ri-market-
        general.html) in the _Amazon Elastic Compute Cloud User Guide_.
        """
        if _request is None:
            _params = {}
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if reserved_instances_id is not ShapeBase.NOT_SET:
                _params['reserved_instances_id'] = reserved_instances_id
            if reserved_instances_listing_id is not ShapeBase.NOT_SET:
                _params['reserved_instances_listing_id'
                       ] = reserved_instances_listing_id
            _request = shapes.DescribeReservedInstancesListingsRequest(
                **_params
            )
        response = self._boto_client.describe_reserved_instances_listings(
            **_request.to_boto()
        )

        return shapes.DescribeReservedInstancesListingsResult.from_boto(
            response
        )

    def describe_reserved_instances_modifications(
        self,
        _request: shapes.DescribeReservedInstancesModificationsRequest = None,
        *,
        filters: typing.List[shapes.Filter] = ShapeBase.NOT_SET,
        reserved_instances_modification_ids: typing.List[str] = ShapeBase.
        NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeReservedInstancesModificationsResult:
        """
        Describes the modifications made to your Reserved Instances. If no parameter is
        specified, information about all your Reserved Instances modification requests
        is returned. If a modification ID is specified, only information about the
        specific modification is returned.

        For more information, see [Modifying Reserved
        Instances](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ri-modifying.html)
        in the Amazon Elastic Compute Cloud User Guide.
        """
        if _request is None:
            _params = {}
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if reserved_instances_modification_ids is not ShapeBase.NOT_SET:
                _params['reserved_instances_modification_ids'
                       ] = reserved_instances_modification_ids
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.DescribeReservedInstancesModificationsRequest(
                **_params
            )
        paginator = self.get_paginator(
            "describe_reserved_instances_modifications"
        ).paginate(**_request.to_boto())
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.DescribeReservedInstancesModificationsResult.from_boto(
            first_page
        )
        result._page_iterator = page_generator
        return result

        return shapes.DescribeReservedInstancesModificationsResult.from_boto(
            response
        )

    def describe_reserved_instances_offerings(
        self,
        _request: shapes.DescribeReservedInstancesOfferingsRequest = None,
        *,
        availability_zone: str = ShapeBase.NOT_SET,
        filters: typing.List[shapes.Filter] = ShapeBase.NOT_SET,
        include_marketplace: bool = ShapeBase.NOT_SET,
        instance_type: typing.Union[str, shapes.
                                    InstanceType] = ShapeBase.NOT_SET,
        max_duration: int = ShapeBase.NOT_SET,
        max_instance_count: int = ShapeBase.NOT_SET,
        min_duration: int = ShapeBase.NOT_SET,
        offering_class: typing.Union[str, shapes.
                                     OfferingClassType] = ShapeBase.NOT_SET,
        product_description: typing.
        Union[str, shapes.RIProductDescription] = ShapeBase.NOT_SET,
        reserved_instances_offering_ids: typing.List[str] = ShapeBase.NOT_SET,
        dry_run: bool = ShapeBase.NOT_SET,
        instance_tenancy: typing.Union[str, shapes.Tenancy] = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        offering_type: typing.Union[str, shapes.
                                    OfferingTypeValues] = ShapeBase.NOT_SET,
    ) -> shapes.DescribeReservedInstancesOfferingsResult:
        """
        Describes Reserved Instance offerings that are available for purchase. With
        Reserved Instances, you purchase the right to launch instances for a period of
        time. During that time period, you do not receive insufficient capacity errors,
        and you pay a lower usage rate than the rate charged for On-Demand instances for
        the actual time used.

        If you have listed your own Reserved Instances for sale in the Reserved Instance
        Marketplace, they will be excluded from these results. This is to ensure that
        you do not purchase your own Reserved Instances.

        For more information, see [Reserved Instance
        Marketplace](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ri-market-
        general.html) in the _Amazon Elastic Compute Cloud User Guide_.
        """
        if _request is None:
            _params = {}
            if availability_zone is not ShapeBase.NOT_SET:
                _params['availability_zone'] = availability_zone
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if include_marketplace is not ShapeBase.NOT_SET:
                _params['include_marketplace'] = include_marketplace
            if instance_type is not ShapeBase.NOT_SET:
                _params['instance_type'] = instance_type
            if max_duration is not ShapeBase.NOT_SET:
                _params['max_duration'] = max_duration
            if max_instance_count is not ShapeBase.NOT_SET:
                _params['max_instance_count'] = max_instance_count
            if min_duration is not ShapeBase.NOT_SET:
                _params['min_duration'] = min_duration
            if offering_class is not ShapeBase.NOT_SET:
                _params['offering_class'] = offering_class
            if product_description is not ShapeBase.NOT_SET:
                _params['product_description'] = product_description
            if reserved_instances_offering_ids is not ShapeBase.NOT_SET:
                _params['reserved_instances_offering_ids'
                       ] = reserved_instances_offering_ids
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            if instance_tenancy is not ShapeBase.NOT_SET:
                _params['instance_tenancy'] = instance_tenancy
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if offering_type is not ShapeBase.NOT_SET:
                _params['offering_type'] = offering_type
            _request = shapes.DescribeReservedInstancesOfferingsRequest(
                **_params
            )
        paginator = self.get_paginator("describe_reserved_instances_offerings"
                                      ).paginate(**_request.to_boto())
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.DescribeReservedInstancesOfferingsResult.from_boto(
            first_page
        )
        result._page_iterator = page_generator
        return result

        return shapes.DescribeReservedInstancesOfferingsResult.from_boto(
            response
        )

    def describe_route_tables(
        self,
        _request: shapes.DescribeRouteTablesRequest = None,
        *,
        filters: typing.List[shapes.Filter] = ShapeBase.NOT_SET,
        dry_run: bool = ShapeBase.NOT_SET,
        route_table_ids: typing.List[str] = ShapeBase.NOT_SET,
    ) -> shapes.DescribeRouteTablesResult:
        """
        Describes one or more of your route tables.

        Each subnet in your VPC must be associated with a route table. If a subnet is
        not explicitly associated with any route table, it is implicitly associated with
        the main route table. This command does not return the subnet ID for implicit
        associations.

        For more information, see [Route
        Tables](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Route_Tables.html)
        in the _Amazon Virtual Private Cloud User Guide_.
        """
        if _request is None:
            _params = {}
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            if route_table_ids is not ShapeBase.NOT_SET:
                _params['route_table_ids'] = route_table_ids
            _request = shapes.DescribeRouteTablesRequest(**_params)
        response = self._boto_client.describe_route_tables(**_request.to_boto())

        return shapes.DescribeRouteTablesResult.from_boto(response)

    def describe_scheduled_instance_availability(
        self,
        _request: shapes.DescribeScheduledInstanceAvailabilityRequest = None,
        *,
        first_slot_start_time_range: shapes.SlotDateTimeRangeRequest,
        recurrence: shapes.ScheduledInstanceRecurrenceRequest,
        dry_run: bool = ShapeBase.NOT_SET,
        filters: typing.List[shapes.Filter] = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        max_slot_duration_in_hours: int = ShapeBase.NOT_SET,
        min_slot_duration_in_hours: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeScheduledInstanceAvailabilityResult:
        """
        Finds available schedules that meet the specified criteria.

        You can search for an available schedule no more than 3 months in advance. You
        must meet the minimum required duration of 1,200 hours per year. For example,
        the minimum daily schedule is 4 hours, the minimum weekly schedule is 24 hours,
        and the minimum monthly schedule is 100 hours.

        After you find a schedule that meets your needs, call PurchaseScheduledInstances
        to purchase Scheduled Instances with that schedule.
        """
        if _request is None:
            _params = {}
            if first_slot_start_time_range is not ShapeBase.NOT_SET:
                _params['first_slot_start_time_range'
                       ] = first_slot_start_time_range
            if recurrence is not ShapeBase.NOT_SET:
                _params['recurrence'] = recurrence
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if max_slot_duration_in_hours is not ShapeBase.NOT_SET:
                _params['max_slot_duration_in_hours'
                       ] = max_slot_duration_in_hours
            if min_slot_duration_in_hours is not ShapeBase.NOT_SET:
                _params['min_slot_duration_in_hours'
                       ] = min_slot_duration_in_hours
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.DescribeScheduledInstanceAvailabilityRequest(
                **_params
            )
        response = self._boto_client.describe_scheduled_instance_availability(
            **_request.to_boto()
        )

        return shapes.DescribeScheduledInstanceAvailabilityResult.from_boto(
            response
        )

    def describe_scheduled_instances(
        self,
        _request: shapes.DescribeScheduledInstancesRequest = None,
        *,
        dry_run: bool = ShapeBase.NOT_SET,
        filters: typing.List[shapes.Filter] = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        scheduled_instance_ids: typing.List[str] = ShapeBase.NOT_SET,
        slot_start_time_range: shapes.SlotStartTimeRangeRequest = ShapeBase.
        NOT_SET,
    ) -> shapes.DescribeScheduledInstancesResult:
        """
        Describes one or more of your Scheduled Instances.
        """
        if _request is None:
            _params = {}
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if scheduled_instance_ids is not ShapeBase.NOT_SET:
                _params['scheduled_instance_ids'] = scheduled_instance_ids
            if slot_start_time_range is not ShapeBase.NOT_SET:
                _params['slot_start_time_range'] = slot_start_time_range
            _request = shapes.DescribeScheduledInstancesRequest(**_params)
        response = self._boto_client.describe_scheduled_instances(
            **_request.to_boto()
        )

        return shapes.DescribeScheduledInstancesResult.from_boto(response)

    def describe_security_group_references(
        self,
        _request: shapes.DescribeSecurityGroupReferencesRequest = None,
        *,
        group_id: typing.List[str],
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> shapes.DescribeSecurityGroupReferencesResult:
        """
        [EC2-VPC only] Describes the VPCs on the other side of a VPC peering connection
        that are referencing the security groups you've specified in this request.
        """
        if _request is None:
            _params = {}
            if group_id is not ShapeBase.NOT_SET:
                _params['group_id'] = group_id
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.DescribeSecurityGroupReferencesRequest(**_params)
        response = self._boto_client.describe_security_group_references(
            **_request.to_boto()
        )

        return shapes.DescribeSecurityGroupReferencesResult.from_boto(response)

    def describe_security_groups(
        self,
        _request: shapes.DescribeSecurityGroupsRequest = None,
        *,
        filters: typing.List[shapes.Filter] = ShapeBase.NOT_SET,
        group_ids: typing.List[str] = ShapeBase.NOT_SET,
        group_names: typing.List[str] = ShapeBase.NOT_SET,
        dry_run: bool = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.DescribeSecurityGroupsResult:
        """
        Describes one or more of your security groups.

        A security group is for use with instances either in the EC2-Classic platform or
        in a specific VPC. For more information, see [Amazon EC2 Security
        Groups](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-network-
        security.html) in the _Amazon Elastic Compute Cloud User Guide_ and [Security
        Groups for Your
        VPC](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_SecurityGroups.html)
        in the _Amazon Virtual Private Cloud User Guide_.
        """
        if _request is None:
            _params = {}
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if group_ids is not ShapeBase.NOT_SET:
                _params['group_ids'] = group_ids
            if group_names is not ShapeBase.NOT_SET:
                _params['group_names'] = group_names
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.DescribeSecurityGroupsRequest(**_params)
        paginator = self.get_paginator("describe_security_groups").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.DescribeSecurityGroupsResult.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.DescribeSecurityGroupsResult.from_boto(response)

    def describe_snapshot_attribute(
        self,
        _request: shapes.DescribeSnapshotAttributeRequest = None,
        *,
        attribute: typing.Union[str, shapes.SnapshotAttributeName],
        snapshot_id: str,
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> shapes.DescribeSnapshotAttributeResult:
        """
        Describes the specified attribute of the specified snapshot. You can specify
        only one attribute at a time.

        For more information about EBS snapshots, see [Amazon EBS
        Snapshots](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSSnapshots.html)
        in the _Amazon Elastic Compute Cloud User Guide_.
        """
        if _request is None:
            _params = {}
            if attribute is not ShapeBase.NOT_SET:
                _params['attribute'] = attribute
            if snapshot_id is not ShapeBase.NOT_SET:
                _params['snapshot_id'] = snapshot_id
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.DescribeSnapshotAttributeRequest(**_params)
        response = self._boto_client.describe_snapshot_attribute(
            **_request.to_boto()
        )

        return shapes.DescribeSnapshotAttributeResult.from_boto(response)

    def describe_snapshots(
        self,
        _request: shapes.DescribeSnapshotsRequest = None,
        *,
        filters: typing.List[shapes.Filter] = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        owner_ids: typing.List[str] = ShapeBase.NOT_SET,
        restorable_by_user_ids: typing.List[str] = ShapeBase.NOT_SET,
        snapshot_ids: typing.List[str] = ShapeBase.NOT_SET,
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> shapes.DescribeSnapshotsResult:
        """
        Describes one or more of the EBS snapshots available to you. Available snapshots
        include public snapshots available for any AWS account to launch, private
        snapshots that you own, and private snapshots owned by another AWS account but
        for which you've been given explicit create volume permissions.

        The create volume permissions fall into the following categories:

          * _public_ : The owner of the snapshot granted create volume permissions for the snapshot to the `all` group. All AWS accounts have create volume permissions for these snapshots.

          * _explicit_ : The owner of the snapshot granted create volume permissions to a specific AWS account.

          * _implicit_ : An AWS account has implicit create volume permissions for all snapshots it owns.

        The list of snapshots returned can be modified by specifying snapshot IDs,
        snapshot owners, or AWS accounts with create volume permissions. If no options
        are specified, Amazon EC2 returns all snapshots for which you have create volume
        permissions.

        If you specify one or more snapshot IDs, only snapshots that have the specified
        IDs are returned. If you specify an invalid snapshot ID, an error is returned.
        If you specify a snapshot ID for which you do not have access, it is not
        included in the returned results.

        If you specify one or more snapshot owners using the `OwnerIds` option, only
        snapshots from the specified owners and for which you have access are returned.
        The results can include the AWS account IDs of the specified owners, `amazon`
        for snapshots owned by Amazon, or `self` for snapshots that you own.

        If you specify a list of restorable users, only snapshots with create snapshot
        permissions for those users are returned. You can specify AWS account IDs (if
        you own the snapshots), `self` for snapshots for which you own or have explicit
        permissions, or `all` for public snapshots.

        If you are describing a long list of snapshots, you can paginate the output to
        make the list more manageable. The `MaxResults` parameter sets the maximum
        number of results returned in a single page. If the list of results exceeds your
        `MaxResults` value, then that number of results is returned along with a
        `NextToken` value that can be passed to a subsequent `DescribeSnapshots` request
        to retrieve the remaining results.

        For more information about EBS snapshots, see [Amazon EBS
        Snapshots](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSSnapshots.html)
        in the _Amazon Elastic Compute Cloud User Guide_.
        """
        if _request is None:
            _params = {}
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if owner_ids is not ShapeBase.NOT_SET:
                _params['owner_ids'] = owner_ids
            if restorable_by_user_ids is not ShapeBase.NOT_SET:
                _params['restorable_by_user_ids'] = restorable_by_user_ids
            if snapshot_ids is not ShapeBase.NOT_SET:
                _params['snapshot_ids'] = snapshot_ids
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.DescribeSnapshotsRequest(**_params)
        paginator = self.get_paginator("describe_snapshots").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.DescribeSnapshotsResult.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.DescribeSnapshotsResult.from_boto(response)

    def describe_spot_datafeed_subscription(
        self,
        _request: shapes.DescribeSpotDatafeedSubscriptionRequest = None,
        *,
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> shapes.DescribeSpotDatafeedSubscriptionResult:
        """
        Describes the data feed for Spot Instances. For more information, see [Spot
        Instance Data Feed](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-
        data-feeds.html) in the _Amazon EC2 User Guide for Linux Instances_.
        """
        if _request is None:
            _params = {}
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.DescribeSpotDatafeedSubscriptionRequest(**_params)
        response = self._boto_client.describe_spot_datafeed_subscription(
            **_request.to_boto()
        )

        return shapes.DescribeSpotDatafeedSubscriptionResult.from_boto(response)

    def describe_spot_fleet_instances(
        self,
        _request: shapes.DescribeSpotFleetInstancesRequest = None,
        *,
        spot_fleet_request_id: str,
        dry_run: bool = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeSpotFleetInstancesResponse:
        """
        Describes the running instances for the specified Spot Fleet.
        """
        if _request is None:
            _params = {}
            if spot_fleet_request_id is not ShapeBase.NOT_SET:
                _params['spot_fleet_request_id'] = spot_fleet_request_id
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.DescribeSpotFleetInstancesRequest(**_params)
        paginator = self.get_paginator("describe_spot_fleet_instances"
                                      ).paginate(**_request.to_boto())
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.DescribeSpotFleetInstancesResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.DescribeSpotFleetInstancesResponse.from_boto(response)

    def describe_spot_fleet_request_history(
        self,
        _request: shapes.DescribeSpotFleetRequestHistoryRequest = None,
        *,
        spot_fleet_request_id: str,
        start_time: datetime.datetime,
        dry_run: bool = ShapeBase.NOT_SET,
        event_type: typing.Union[str, shapes.EventType] = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeSpotFleetRequestHistoryResponse:
        """
        Describes the events for the specified Spot Fleet request during the specified
        time.

        Spot Fleet events are delayed by up to 30 seconds before they can be described.
        This ensures that you can query by the last evaluated time and not miss a
        recorded event.
        """
        if _request is None:
            _params = {}
            if spot_fleet_request_id is not ShapeBase.NOT_SET:
                _params['spot_fleet_request_id'] = spot_fleet_request_id
            if start_time is not ShapeBase.NOT_SET:
                _params['start_time'] = start_time
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            if event_type is not ShapeBase.NOT_SET:
                _params['event_type'] = event_type
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.DescribeSpotFleetRequestHistoryRequest(**_params)
        response = self._boto_client.describe_spot_fleet_request_history(
            **_request.to_boto()
        )

        return shapes.DescribeSpotFleetRequestHistoryResponse.from_boto(
            response
        )

    def describe_spot_fleet_requests(
        self,
        _request: shapes.DescribeSpotFleetRequestsRequest = None,
        *,
        dry_run: bool = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        spot_fleet_request_ids: typing.List[str] = ShapeBase.NOT_SET,
    ) -> shapes.DescribeSpotFleetRequestsResponse:
        """
        Describes your Spot Fleet requests.

        Spot Fleet requests are deleted 48 hours after they are canceled and their
        instances are terminated.
        """
        if _request is None:
            _params = {}
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if spot_fleet_request_ids is not ShapeBase.NOT_SET:
                _params['spot_fleet_request_ids'] = spot_fleet_request_ids
            _request = shapes.DescribeSpotFleetRequestsRequest(**_params)
        paginator = self.get_paginator("describe_spot_fleet_requests").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.DescribeSpotFleetRequestsResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.DescribeSpotFleetRequestsResponse.from_boto(response)

    def describe_spot_instance_requests(
        self,
        _request: shapes.DescribeSpotInstanceRequestsRequest = None,
        *,
        filters: typing.List[shapes.Filter] = ShapeBase.NOT_SET,
        dry_run: bool = ShapeBase.NOT_SET,
        spot_instance_request_ids: typing.List[str] = ShapeBase.NOT_SET,
    ) -> shapes.DescribeSpotInstanceRequestsResult:
        """
        Describes the specified Spot Instance requests.

        You can use `DescribeSpotInstanceRequests` to find a running Spot Instance by
        examining the response. If the status of the Spot Instance is `fulfilled`, the
        instance ID appears in the response and contains the identifier of the instance.
        Alternatively, you can use DescribeInstances with a filter to look for instances
        where the instance lifecycle is `spot`.

        Spot Instance requests are deleted four hours after they are canceled and their
        instances are terminated.
        """
        if _request is None:
            _params = {}
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            if spot_instance_request_ids is not ShapeBase.NOT_SET:
                _params['spot_instance_request_ids'] = spot_instance_request_ids
            _request = shapes.DescribeSpotInstanceRequestsRequest(**_params)
        response = self._boto_client.describe_spot_instance_requests(
            **_request.to_boto()
        )

        return shapes.DescribeSpotInstanceRequestsResult.from_boto(response)

    def describe_spot_price_history(
        self,
        _request: shapes.DescribeSpotPriceHistoryRequest = None,
        *,
        filters: typing.List[shapes.Filter] = ShapeBase.NOT_SET,
        availability_zone: str = ShapeBase.NOT_SET,
        dry_run: bool = ShapeBase.NOT_SET,
        end_time: datetime.datetime = ShapeBase.NOT_SET,
        instance_types: typing.List[typing.Union[str, shapes.InstanceType]
                                   ] = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        product_descriptions: typing.List[str] = ShapeBase.NOT_SET,
        start_time: datetime.datetime = ShapeBase.NOT_SET,
    ) -> shapes.DescribeSpotPriceHistoryResult:
        """
        Describes the Spot price history. For more information, see [Spot Instance
        Pricing History](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-
        instances-history.html) in the _Amazon EC2 User Guide for Linux Instances_.

        When you specify a start and end time, this operation returns the prices of the
        instance types within the time range that you specified and the time when the
        price changed. The price is valid within the time period that you specified; the
        response merely indicates the last time that the price changed.
        """
        if _request is None:
            _params = {}
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if availability_zone is not ShapeBase.NOT_SET:
                _params['availability_zone'] = availability_zone
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            if end_time is not ShapeBase.NOT_SET:
                _params['end_time'] = end_time
            if instance_types is not ShapeBase.NOT_SET:
                _params['instance_types'] = instance_types
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if product_descriptions is not ShapeBase.NOT_SET:
                _params['product_descriptions'] = product_descriptions
            if start_time is not ShapeBase.NOT_SET:
                _params['start_time'] = start_time
            _request = shapes.DescribeSpotPriceHistoryRequest(**_params)
        paginator = self.get_paginator("describe_spot_price_history").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.DescribeSpotPriceHistoryResult.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.DescribeSpotPriceHistoryResult.from_boto(response)

    def describe_stale_security_groups(
        self,
        _request: shapes.DescribeStaleSecurityGroupsRequest = None,
        *,
        vpc_id: str,
        dry_run: bool = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeStaleSecurityGroupsResult:
        """
        [EC2-VPC only] Describes the stale security group rules for security groups in a
        specified VPC. Rules are stale when they reference a deleted security group in a
        peer VPC, or a security group in a peer VPC for which the VPC peering connection
        has been deleted.
        """
        if _request is None:
            _params = {}
            if vpc_id is not ShapeBase.NOT_SET:
                _params['vpc_id'] = vpc_id
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.DescribeStaleSecurityGroupsRequest(**_params)
        response = self._boto_client.describe_stale_security_groups(
            **_request.to_boto()
        )

        return shapes.DescribeStaleSecurityGroupsResult.from_boto(response)

    def describe_subnets(
        self,
        _request: shapes.DescribeSubnetsRequest = None,
        *,
        filters: typing.List[shapes.Filter] = ShapeBase.NOT_SET,
        subnet_ids: typing.List[str] = ShapeBase.NOT_SET,
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> shapes.DescribeSubnetsResult:
        """
        Describes one or more of your subnets.

        For more information, see [Your VPC and
        Subnets](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Subnets.html)
        in the _Amazon Virtual Private Cloud User Guide_.
        """
        if _request is None:
            _params = {}
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if subnet_ids is not ShapeBase.NOT_SET:
                _params['subnet_ids'] = subnet_ids
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.DescribeSubnetsRequest(**_params)
        response = self._boto_client.describe_subnets(**_request.to_boto())

        return shapes.DescribeSubnetsResult.from_boto(response)

    def describe_tags(
        self,
        _request: shapes.DescribeTagsRequest = None,
        *,
        dry_run: bool = ShapeBase.NOT_SET,
        filters: typing.List[shapes.Filter] = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeTagsResult:
        """
        Describes one or more of the tags for your EC2 resources.

        For more information about tags, see [Tagging Your
        Resources](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html)
        in the _Amazon Elastic Compute Cloud User Guide_.
        """
        if _request is None:
            _params = {}
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.DescribeTagsRequest(**_params)
        paginator = self.get_paginator("describe_tags").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.DescribeTagsResult.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.DescribeTagsResult.from_boto(response)

    def describe_volume_attribute(
        self,
        _request: shapes.DescribeVolumeAttributeRequest = None,
        *,
        attribute: typing.Union[str, shapes.VolumeAttributeName],
        volume_id: str,
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> shapes.DescribeVolumeAttributeResult:
        """
        Describes the specified attribute of the specified volume. You can specify only
        one attribute at a time.

        For more information about EBS volumes, see [Amazon EBS
        Volumes](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumes.html) in
        the _Amazon Elastic Compute Cloud User Guide_.
        """
        if _request is None:
            _params = {}
            if attribute is not ShapeBase.NOT_SET:
                _params['attribute'] = attribute
            if volume_id is not ShapeBase.NOT_SET:
                _params['volume_id'] = volume_id
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.DescribeVolumeAttributeRequest(**_params)
        response = self._boto_client.describe_volume_attribute(
            **_request.to_boto()
        )

        return shapes.DescribeVolumeAttributeResult.from_boto(response)

    def describe_volume_status(
        self,
        _request: shapes.DescribeVolumeStatusRequest = None,
        *,
        filters: typing.List[shapes.Filter] = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        volume_ids: typing.List[str] = ShapeBase.NOT_SET,
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> shapes.DescribeVolumeStatusResult:
        """
        Describes the status of the specified volumes. Volume status provides the result
        of the checks performed on your volumes to determine events that can impair the
        performance of your volumes. The performance of a volume can be affected if an
        issue occurs on the volume's underlying host. If the volume's underlying host
        experiences a power outage or system issue, after the system is restored, there
        could be data inconsistencies on the volume. Volume events notify you if this
        occurs. Volume actions notify you if any action needs to be taken in response to
        the event.

        The `DescribeVolumeStatus` operation provides the following information about
        the specified volumes:

        _Status_ : Reflects the current status of the volume. The possible values are
        `ok`, `impaired` , `warning`, or `insufficient-data`. If all checks pass, the
        overall status of the volume is `ok`. If the check fails, the overall status is
        `impaired`. If the status is `insufficient-data`, then the checks may still be
        taking place on your volume at the time. We recommend that you retry the
        request. For more information about volume status, see [Monitoring the Status of
        Your Volumes](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/monitoring-
        volume-status.html) in the _Amazon Elastic Compute Cloud User Guide_.

        _Events_ : Reflect the cause of a volume status and may require you to take
        action. For example, if your volume returns an `impaired` status, then the
        volume event might be `potential-data-inconsistency`. This means that your
        volume has been affected by an issue with the underlying host, has all I/O
        operations disabled, and may have inconsistent data.

        _Actions_ : Reflect the actions you may have to take in response to an event.
        For example, if the status of the volume is `impaired` and the volume event
        shows `potential-data-inconsistency`, then the action shows `enable-volume-io`.
        This means that you may want to enable the I/O operations for the volume by
        calling the EnableVolumeIO action and then check the volume for data
        consistency.

        Volume status is based on the volume status checks, and does not reflect the
        volume state. Therefore, volume status does not indicate volumes in the `error`
        state (for example, when a volume is incapable of accepting I/O.)
        """
        if _request is None:
            _params = {}
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if volume_ids is not ShapeBase.NOT_SET:
                _params['volume_ids'] = volume_ids
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.DescribeVolumeStatusRequest(**_params)
        paginator = self.get_paginator("describe_volume_status").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.DescribeVolumeStatusResult.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.DescribeVolumeStatusResult.from_boto(response)

    def describe_volumes(
        self,
        _request: shapes.DescribeVolumesRequest = None,
        *,
        filters: typing.List[shapes.Filter] = ShapeBase.NOT_SET,
        volume_ids: typing.List[str] = ShapeBase.NOT_SET,
        dry_run: bool = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeVolumesResult:
        """
        Describes the specified EBS volumes.

        If you are describing a long list of volumes, you can paginate the output to
        make the list more manageable. The `MaxResults` parameter sets the maximum
        number of results returned in a single page. If the list of results exceeds your
        `MaxResults` value, then that number of results is returned along with a
        `NextToken` value that can be passed to a subsequent `DescribeVolumes` request
        to retrieve the remaining results.

        For more information about EBS volumes, see [Amazon EBS
        Volumes](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumes.html) in
        the _Amazon Elastic Compute Cloud User Guide_.
        """
        if _request is None:
            _params = {}
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if volume_ids is not ShapeBase.NOT_SET:
                _params['volume_ids'] = volume_ids
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.DescribeVolumesRequest(**_params)
        paginator = self.get_paginator("describe_volumes").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.DescribeVolumesResult.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.DescribeVolumesResult.from_boto(response)

    def describe_volumes_modifications(
        self,
        _request: shapes.DescribeVolumesModificationsRequest = None,
        *,
        dry_run: bool = ShapeBase.NOT_SET,
        volume_ids: typing.List[str] = ShapeBase.NOT_SET,
        filters: typing.List[shapes.Filter] = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.DescribeVolumesModificationsResult:
        """
        Reports the current modification status of EBS volumes.

        Current-generation EBS volumes support modification of attributes including
        type, size, and (for `io1` volumes) IOPS provisioning while either attached to
        or detached from an instance. Following an action from the API or the console to
        modify a volume, the status of the modification may be `modifying`,
        `optimizing`, `completed`, or `failed`. If a volume has never been modified,
        then certain elements of the returned `VolumeModification` objects are null.

        You can also use CloudWatch Events to check the status of a modification to an
        EBS volume. For information about CloudWatch Events, see the [Amazon CloudWatch
        Events User Guide](http://docs.aws.amazon.com/AmazonCloudWatch/latest/events/).
        For more information, see [Monitoring Volume
        Modifications"](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-expand-
        volume.html#monitoring_mods) in the _Amazon Elastic Compute Cloud User Guide_.
        """
        if _request is None:
            _params = {}
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            if volume_ids is not ShapeBase.NOT_SET:
                _params['volume_ids'] = volume_ids
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.DescribeVolumesModificationsRequest(**_params)
        response = self._boto_client.describe_volumes_modifications(
            **_request.to_boto()
        )

        return shapes.DescribeVolumesModificationsResult.from_boto(response)

    def describe_vpc_attribute(
        self,
        _request: shapes.DescribeVpcAttributeRequest = None,
        *,
        attribute: typing.Union[str, shapes.VpcAttributeName],
        vpc_id: str,
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> shapes.DescribeVpcAttributeResult:
        """
        Describes the specified attribute of the specified VPC. You can specify only one
        attribute at a time.
        """
        if _request is None:
            _params = {}
            if attribute is not ShapeBase.NOT_SET:
                _params['attribute'] = attribute
            if vpc_id is not ShapeBase.NOT_SET:
                _params['vpc_id'] = vpc_id
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.DescribeVpcAttributeRequest(**_params)
        response = self._boto_client.describe_vpc_attribute(
            **_request.to_boto()
        )

        return shapes.DescribeVpcAttributeResult.from_boto(response)

    def describe_vpc_classic_link(
        self,
        _request: shapes.DescribeVpcClassicLinkRequest = None,
        *,
        filters: typing.List[shapes.Filter] = ShapeBase.NOT_SET,
        dry_run: bool = ShapeBase.NOT_SET,
        vpc_ids: typing.List[str] = ShapeBase.NOT_SET,
    ) -> shapes.DescribeVpcClassicLinkResult:
        """
        Describes the ClassicLink status of one or more VPCs.
        """
        if _request is None:
            _params = {}
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            if vpc_ids is not ShapeBase.NOT_SET:
                _params['vpc_ids'] = vpc_ids
            _request = shapes.DescribeVpcClassicLinkRequest(**_params)
        response = self._boto_client.describe_vpc_classic_link(
            **_request.to_boto()
        )

        return shapes.DescribeVpcClassicLinkResult.from_boto(response)

    def describe_vpc_classic_link_dns_support(
        self,
        _request: shapes.DescribeVpcClassicLinkDnsSupportRequest = None,
        *,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        vpc_ids: typing.List[str] = ShapeBase.NOT_SET,
    ) -> shapes.DescribeVpcClassicLinkDnsSupportResult:
        """
        Describes the ClassicLink DNS support status of one or more VPCs. If enabled,
        the DNS hostname of a linked EC2-Classic instance resolves to its private IP
        address when addressed from an instance in the VPC to which it's linked.
        Similarly, the DNS hostname of an instance in a VPC resolves to its private IP
        address when addressed from a linked EC2-Classic instance. For more information,
        see [ClassicLink](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/vpc-
        classiclink.html) in the _Amazon Elastic Compute Cloud User Guide_.
        """
        if _request is None:
            _params = {}
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if vpc_ids is not ShapeBase.NOT_SET:
                _params['vpc_ids'] = vpc_ids
            _request = shapes.DescribeVpcClassicLinkDnsSupportRequest(**_params)
        response = self._boto_client.describe_vpc_classic_link_dns_support(
            **_request.to_boto()
        )

        return shapes.DescribeVpcClassicLinkDnsSupportResult.from_boto(response)

    def describe_vpc_endpoint_connection_notifications(
        self,
        _request: shapes.
        DescribeVpcEndpointConnectionNotificationsRequest = None,
        *,
        dry_run: bool = ShapeBase.NOT_SET,
        connection_notification_id: str = ShapeBase.NOT_SET,
        filters: typing.List[shapes.Filter] = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeVpcEndpointConnectionNotificationsResult:
        """
        Describes the connection notifications for VPC endpoints and VPC endpoint
        services.
        """
        if _request is None:
            _params = {}
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            if connection_notification_id is not ShapeBase.NOT_SET:
                _params['connection_notification_id'
                       ] = connection_notification_id
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.DescribeVpcEndpointConnectionNotificationsRequest(
                **_params
            )
        response = self._boto_client.describe_vpc_endpoint_connection_notifications(
            **_request.to_boto()
        )

        return shapes.DescribeVpcEndpointConnectionNotificationsResult.from_boto(
            response
        )

    def describe_vpc_endpoint_connections(
        self,
        _request: shapes.DescribeVpcEndpointConnectionsRequest = None,
        *,
        dry_run: bool = ShapeBase.NOT_SET,
        filters: typing.List[shapes.Filter] = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeVpcEndpointConnectionsResult:
        """
        Describes the VPC endpoint connections to your VPC endpoint services, including
        any endpoints that are pending your acceptance.
        """
        if _request is None:
            _params = {}
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.DescribeVpcEndpointConnectionsRequest(**_params)
        response = self._boto_client.describe_vpc_endpoint_connections(
            **_request.to_boto()
        )

        return shapes.DescribeVpcEndpointConnectionsResult.from_boto(response)

    def describe_vpc_endpoint_service_configurations(
        self,
        _request: shapes.DescribeVpcEndpointServiceConfigurationsRequest = None,
        *,
        dry_run: bool = ShapeBase.NOT_SET,
        service_ids: typing.List[str] = ShapeBase.NOT_SET,
        filters: typing.List[shapes.Filter] = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeVpcEndpointServiceConfigurationsResult:
        """
        Describes the VPC endpoint service configurations in your account (your
        services).
        """
        if _request is None:
            _params = {}
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            if service_ids is not ShapeBase.NOT_SET:
                _params['service_ids'] = service_ids
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.DescribeVpcEndpointServiceConfigurationsRequest(
                **_params
            )
        response = self._boto_client.describe_vpc_endpoint_service_configurations(
            **_request.to_boto()
        )

        return shapes.DescribeVpcEndpointServiceConfigurationsResult.from_boto(
            response
        )

    def describe_vpc_endpoint_service_permissions(
        self,
        _request: shapes.DescribeVpcEndpointServicePermissionsRequest = None,
        *,
        service_id: str,
        dry_run: bool = ShapeBase.NOT_SET,
        filters: typing.List[shapes.Filter] = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeVpcEndpointServicePermissionsResult:
        """
        Describes the principals (service consumers) that are permitted to discover your
        VPC endpoint service.
        """
        if _request is None:
            _params = {}
            if service_id is not ShapeBase.NOT_SET:
                _params['service_id'] = service_id
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.DescribeVpcEndpointServicePermissionsRequest(
                **_params
            )
        response = self._boto_client.describe_vpc_endpoint_service_permissions(
            **_request.to_boto()
        )

        return shapes.DescribeVpcEndpointServicePermissionsResult.from_boto(
            response
        )

    def describe_vpc_endpoint_services(
        self,
        _request: shapes.DescribeVpcEndpointServicesRequest = None,
        *,
        dry_run: bool = ShapeBase.NOT_SET,
        service_names: typing.List[str] = ShapeBase.NOT_SET,
        filters: typing.List[shapes.Filter] = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeVpcEndpointServicesResult:
        """
        Describes available services to which you can create a VPC endpoint.
        """
        if _request is None:
            _params = {}
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            if service_names is not ShapeBase.NOT_SET:
                _params['service_names'] = service_names
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.DescribeVpcEndpointServicesRequest(**_params)
        response = self._boto_client.describe_vpc_endpoint_services(
            **_request.to_boto()
        )

        return shapes.DescribeVpcEndpointServicesResult.from_boto(response)

    def describe_vpc_endpoints(
        self,
        _request: shapes.DescribeVpcEndpointsRequest = None,
        *,
        dry_run: bool = ShapeBase.NOT_SET,
        vpc_endpoint_ids: typing.List[str] = ShapeBase.NOT_SET,
        filters: typing.List[shapes.Filter] = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeVpcEndpointsResult:
        """
        Describes one or more of your VPC endpoints.
        """
        if _request is None:
            _params = {}
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            if vpc_endpoint_ids is not ShapeBase.NOT_SET:
                _params['vpc_endpoint_ids'] = vpc_endpoint_ids
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.DescribeVpcEndpointsRequest(**_params)
        response = self._boto_client.describe_vpc_endpoints(
            **_request.to_boto()
        )

        return shapes.DescribeVpcEndpointsResult.from_boto(response)

    def describe_vpc_peering_connections(
        self,
        _request: shapes.DescribeVpcPeeringConnectionsRequest = None,
        *,
        filters: typing.List[shapes.Filter] = ShapeBase.NOT_SET,
        dry_run: bool = ShapeBase.NOT_SET,
        vpc_peering_connection_ids: typing.List[str] = ShapeBase.NOT_SET,
    ) -> shapes.DescribeVpcPeeringConnectionsResult:
        """
        Describes one or more of your VPC peering connections.
        """
        if _request is None:
            _params = {}
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            if vpc_peering_connection_ids is not ShapeBase.NOT_SET:
                _params['vpc_peering_connection_ids'
                       ] = vpc_peering_connection_ids
            _request = shapes.DescribeVpcPeeringConnectionsRequest(**_params)
        response = self._boto_client.describe_vpc_peering_connections(
            **_request.to_boto()
        )

        return shapes.DescribeVpcPeeringConnectionsResult.from_boto(response)

    def describe_vpcs(
        self,
        _request: shapes.DescribeVpcsRequest = None,
        *,
        filters: typing.List[shapes.Filter] = ShapeBase.NOT_SET,
        vpc_ids: typing.List[str] = ShapeBase.NOT_SET,
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> shapes.DescribeVpcsResult:
        """
        Describes one or more of your VPCs.
        """
        if _request is None:
            _params = {}
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if vpc_ids is not ShapeBase.NOT_SET:
                _params['vpc_ids'] = vpc_ids
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.DescribeVpcsRequest(**_params)
        response = self._boto_client.describe_vpcs(**_request.to_boto())

        return shapes.DescribeVpcsResult.from_boto(response)

    def describe_vpn_connections(
        self,
        _request: shapes.DescribeVpnConnectionsRequest = None,
        *,
        filters: typing.List[shapes.Filter] = ShapeBase.NOT_SET,
        vpn_connection_ids: typing.List[str] = ShapeBase.NOT_SET,
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> shapes.DescribeVpnConnectionsResult:
        """
        Describes one or more of your VPN connections.

        For more information about VPN connections, see [AWS Managed VPN
        Connections](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_VPN.html)
        in the _Amazon Virtual Private Cloud User Guide_.
        """
        if _request is None:
            _params = {}
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if vpn_connection_ids is not ShapeBase.NOT_SET:
                _params['vpn_connection_ids'] = vpn_connection_ids
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.DescribeVpnConnectionsRequest(**_params)
        response = self._boto_client.describe_vpn_connections(
            **_request.to_boto()
        )

        return shapes.DescribeVpnConnectionsResult.from_boto(response)

    def describe_vpn_gateways(
        self,
        _request: shapes.DescribeVpnGatewaysRequest = None,
        *,
        filters: typing.List[shapes.Filter] = ShapeBase.NOT_SET,
        vpn_gateway_ids: typing.List[str] = ShapeBase.NOT_SET,
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> shapes.DescribeVpnGatewaysResult:
        """
        Describes one or more of your virtual private gateways.

        For more information about virtual private gateways, see [AWS Managed VPN
        Connections](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_VPN.html)
        in the _Amazon Virtual Private Cloud User Guide_.
        """
        if _request is None:
            _params = {}
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if vpn_gateway_ids is not ShapeBase.NOT_SET:
                _params['vpn_gateway_ids'] = vpn_gateway_ids
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.DescribeVpnGatewaysRequest(**_params)
        response = self._boto_client.describe_vpn_gateways(**_request.to_boto())

        return shapes.DescribeVpnGatewaysResult.from_boto(response)

    def detach_classic_link_vpc(
        self,
        _request: shapes.DetachClassicLinkVpcRequest = None,
        *,
        instance_id: str,
        vpc_id: str,
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> shapes.DetachClassicLinkVpcResult:
        """
        Unlinks (detaches) a linked EC2-Classic instance from a VPC. After the instance
        has been unlinked, the VPC security groups are no longer associated with it. An
        instance is automatically unlinked from a VPC when it's stopped.
        """
        if _request is None:
            _params = {}
            if instance_id is not ShapeBase.NOT_SET:
                _params['instance_id'] = instance_id
            if vpc_id is not ShapeBase.NOT_SET:
                _params['vpc_id'] = vpc_id
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.DetachClassicLinkVpcRequest(**_params)
        response = self._boto_client.detach_classic_link_vpc(
            **_request.to_boto()
        )

        return shapes.DetachClassicLinkVpcResult.from_boto(response)

    def detach_internet_gateway(
        self,
        _request: shapes.DetachInternetGatewayRequest = None,
        *,
        internet_gateway_id: str,
        vpc_id: str,
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> None:
        """
        Detaches an internet gateway from a VPC, disabling connectivity between the
        internet and the VPC. The VPC must not contain any running instances with
        Elastic IP addresses or public IPv4 addresses.
        """
        if _request is None:
            _params = {}
            if internet_gateway_id is not ShapeBase.NOT_SET:
                _params['internet_gateway_id'] = internet_gateway_id
            if vpc_id is not ShapeBase.NOT_SET:
                _params['vpc_id'] = vpc_id
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.DetachInternetGatewayRequest(**_params)
        response = self._boto_client.detach_internet_gateway(
            **_request.to_boto()
        )

    def detach_network_interface(
        self,
        _request: shapes.DetachNetworkInterfaceRequest = None,
        *,
        attachment_id: str,
        dry_run: bool = ShapeBase.NOT_SET,
        force: bool = ShapeBase.NOT_SET,
    ) -> None:
        """
        Detaches a network interface from an instance.
        """
        if _request is None:
            _params = {}
            if attachment_id is not ShapeBase.NOT_SET:
                _params['attachment_id'] = attachment_id
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            if force is not ShapeBase.NOT_SET:
                _params['force'] = force
            _request = shapes.DetachNetworkInterfaceRequest(**_params)
        response = self._boto_client.detach_network_interface(
            **_request.to_boto()
        )

    def detach_volume(
        self,
        _request: shapes.DetachVolumeRequest = None,
        *,
        volume_id: str,
        device: str = ShapeBase.NOT_SET,
        force: bool = ShapeBase.NOT_SET,
        instance_id: str = ShapeBase.NOT_SET,
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> shapes.VolumeAttachment:
        """
        Detaches an EBS volume from an instance. Make sure to unmount any file systems
        on the device within your operating system before detaching the volume. Failure
        to do so can result in the volume becoming stuck in the `busy` state while
        detaching. If this happens, detachment can be delayed indefinitely until you
        unmount the volume, force detachment, reboot the instance, or all three. If an
        EBS volume is the root device of an instance, it can't be detached while the
        instance is running. To detach the root volume, stop the instance first.

        When a volume with an AWS Marketplace product code is detached from an instance,
        the product code is no longer associated with the instance.

        For more information, see [Detaching an Amazon EBS
        Volume](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-detaching-
        volume.html) in the _Amazon Elastic Compute Cloud User Guide_.
        """
        if _request is None:
            _params = {}
            if volume_id is not ShapeBase.NOT_SET:
                _params['volume_id'] = volume_id
            if device is not ShapeBase.NOT_SET:
                _params['device'] = device
            if force is not ShapeBase.NOT_SET:
                _params['force'] = force
            if instance_id is not ShapeBase.NOT_SET:
                _params['instance_id'] = instance_id
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.DetachVolumeRequest(**_params)
        response = self._boto_client.detach_volume(**_request.to_boto())

        return shapes.VolumeAttachment.from_boto(response)

    def detach_vpn_gateway(
        self,
        _request: shapes.DetachVpnGatewayRequest = None,
        *,
        vpc_id: str,
        vpn_gateway_id: str,
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> None:
        """
        Detaches a virtual private gateway from a VPC. You do this if you're planning to
        turn off the VPC and not use it anymore. You can confirm a virtual private
        gateway has been completely detached from a VPC by describing the virtual
        private gateway (any attachments to the virtual private gateway are also
        described).

        You must wait for the attachment's state to switch to `detached` before you can
        delete the VPC or attach a different VPC to the virtual private gateway.
        """
        if _request is None:
            _params = {}
            if vpc_id is not ShapeBase.NOT_SET:
                _params['vpc_id'] = vpc_id
            if vpn_gateway_id is not ShapeBase.NOT_SET:
                _params['vpn_gateway_id'] = vpn_gateway_id
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.DetachVpnGatewayRequest(**_params)
        response = self._boto_client.detach_vpn_gateway(**_request.to_boto())

    def disable_vgw_route_propagation(
        self,
        _request: shapes.DisableVgwRoutePropagationRequest = None,
        *,
        gateway_id: str,
        route_table_id: str,
    ) -> None:
        """
        Disables a virtual private gateway (VGW) from propagating routes to a specified
        route table of a VPC.
        """
        if _request is None:
            _params = {}
            if gateway_id is not ShapeBase.NOT_SET:
                _params['gateway_id'] = gateway_id
            if route_table_id is not ShapeBase.NOT_SET:
                _params['route_table_id'] = route_table_id
            _request = shapes.DisableVgwRoutePropagationRequest(**_params)
        response = self._boto_client.disable_vgw_route_propagation(
            **_request.to_boto()
        )

    def disable_vpc_classic_link(
        self,
        _request: shapes.DisableVpcClassicLinkRequest = None,
        *,
        vpc_id: str,
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> shapes.DisableVpcClassicLinkResult:
        """
        Disables ClassicLink for a VPC. You cannot disable ClassicLink for a VPC that
        has EC2-Classic instances linked to it.
        """
        if _request is None:
            _params = {}
            if vpc_id is not ShapeBase.NOT_SET:
                _params['vpc_id'] = vpc_id
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.DisableVpcClassicLinkRequest(**_params)
        response = self._boto_client.disable_vpc_classic_link(
            **_request.to_boto()
        )

        return shapes.DisableVpcClassicLinkResult.from_boto(response)

    def disable_vpc_classic_link_dns_support(
        self,
        _request: shapes.DisableVpcClassicLinkDnsSupportRequest = None,
        *,
        vpc_id: str = ShapeBase.NOT_SET,
    ) -> shapes.DisableVpcClassicLinkDnsSupportResult:
        """
        Disables ClassicLink DNS support for a VPC. If disabled, DNS hostnames resolve
        to public IP addresses when addressed between a linked EC2-Classic instance and
        instances in the VPC to which it's linked. For more information, see
        [ClassicLink](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/vpc-
        classiclink.html) in the _Amazon Elastic Compute Cloud User Guide_.
        """
        if _request is None:
            _params = {}
            if vpc_id is not ShapeBase.NOT_SET:
                _params['vpc_id'] = vpc_id
            _request = shapes.DisableVpcClassicLinkDnsSupportRequest(**_params)
        response = self._boto_client.disable_vpc_classic_link_dns_support(
            **_request.to_boto()
        )

        return shapes.DisableVpcClassicLinkDnsSupportResult.from_boto(response)

    def disassociate_address(
        self,
        _request: shapes.DisassociateAddressRequest = None,
        *,
        association_id: str = ShapeBase.NOT_SET,
        public_ip: str = ShapeBase.NOT_SET,
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> None:
        """
        Disassociates an Elastic IP address from the instance or network interface it's
        associated with.

        An Elastic IP address is for use in either the EC2-Classic platform or in a VPC.
        For more information, see [Elastic IP
        Addresses](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-
        addresses-eip.html) in the _Amazon Elastic Compute Cloud User Guide_.

        This is an idempotent operation. If you perform the operation more than once,
        Amazon EC2 doesn't return an error.
        """
        if _request is None:
            _params = {}
            if association_id is not ShapeBase.NOT_SET:
                _params['association_id'] = association_id
            if public_ip is not ShapeBase.NOT_SET:
                _params['public_ip'] = public_ip
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.DisassociateAddressRequest(**_params)
        response = self._boto_client.disassociate_address(**_request.to_boto())

    def disassociate_iam_instance_profile(
        self,
        _request: shapes.DisassociateIamInstanceProfileRequest = None,
        *,
        association_id: str,
    ) -> shapes.DisassociateIamInstanceProfileResult:
        """
        Disassociates an IAM instance profile from a running or stopped instance.

        Use DescribeIamInstanceProfileAssociations to get the association ID.
        """
        if _request is None:
            _params = {}
            if association_id is not ShapeBase.NOT_SET:
                _params['association_id'] = association_id
            _request = shapes.DisassociateIamInstanceProfileRequest(**_params)
        response = self._boto_client.disassociate_iam_instance_profile(
            **_request.to_boto()
        )

        return shapes.DisassociateIamInstanceProfileResult.from_boto(response)

    def disassociate_route_table(
        self,
        _request: shapes.DisassociateRouteTableRequest = None,
        *,
        association_id: str,
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> None:
        """
        Disassociates a subnet from a route table.

        After you perform this action, the subnet no longer uses the routes in the route
        table. Instead, it uses the routes in the VPC's main route table. For more
        information about route tables, see [Route
        Tables](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Route_Tables.html)
        in the _Amazon Virtual Private Cloud User Guide_.
        """
        if _request is None:
            _params = {}
            if association_id is not ShapeBase.NOT_SET:
                _params['association_id'] = association_id
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.DisassociateRouteTableRequest(**_params)
        response = self._boto_client.disassociate_route_table(
            **_request.to_boto()
        )

    def disassociate_subnet_cidr_block(
        self,
        _request: shapes.DisassociateSubnetCidrBlockRequest = None,
        *,
        association_id: str,
    ) -> shapes.DisassociateSubnetCidrBlockResult:
        """
        Disassociates a CIDR block from a subnet. Currently, you can disassociate an
        IPv6 CIDR block only. You must detach or delete all gateways and resources that
        are associated with the CIDR block before you can disassociate it.
        """
        if _request is None:
            _params = {}
            if association_id is not ShapeBase.NOT_SET:
                _params['association_id'] = association_id
            _request = shapes.DisassociateSubnetCidrBlockRequest(**_params)
        response = self._boto_client.disassociate_subnet_cidr_block(
            **_request.to_boto()
        )

        return shapes.DisassociateSubnetCidrBlockResult.from_boto(response)

    def disassociate_vpc_cidr_block(
        self,
        _request: shapes.DisassociateVpcCidrBlockRequest = None,
        *,
        association_id: str,
    ) -> shapes.DisassociateVpcCidrBlockResult:
        """
        Disassociates a CIDR block from a VPC. To disassociate the CIDR block, you must
        specify its association ID. You can get the association ID by using
        DescribeVpcs. You must detach or delete all gateways and resources that are
        associated with the CIDR block before you can disassociate it.

        You cannot disassociate the CIDR block with which you originally created the VPC
        (the primary CIDR block).
        """
        if _request is None:
            _params = {}
            if association_id is not ShapeBase.NOT_SET:
                _params['association_id'] = association_id
            _request = shapes.DisassociateVpcCidrBlockRequest(**_params)
        response = self._boto_client.disassociate_vpc_cidr_block(
            **_request.to_boto()
        )

        return shapes.DisassociateVpcCidrBlockResult.from_boto(response)

    def enable_vgw_route_propagation(
        self,
        _request: shapes.EnableVgwRoutePropagationRequest = None,
        *,
        gateway_id: str,
        route_table_id: str,
    ) -> None:
        """
        Enables a virtual private gateway (VGW) to propagate routes to the specified
        route table of a VPC.
        """
        if _request is None:
            _params = {}
            if gateway_id is not ShapeBase.NOT_SET:
                _params['gateway_id'] = gateway_id
            if route_table_id is not ShapeBase.NOT_SET:
                _params['route_table_id'] = route_table_id
            _request = shapes.EnableVgwRoutePropagationRequest(**_params)
        response = self._boto_client.enable_vgw_route_propagation(
            **_request.to_boto()
        )

    def enable_volume_io(
        self,
        _request: shapes.EnableVolumeIORequest = None,
        *,
        volume_id: str,
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> None:
        """
        Enables I/O operations for a volume that had I/O operations disabled because the
        data on the volume was potentially inconsistent.
        """
        if _request is None:
            _params = {}
            if volume_id is not ShapeBase.NOT_SET:
                _params['volume_id'] = volume_id
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.EnableVolumeIORequest(**_params)
        response = self._boto_client.enable_volume_io(**_request.to_boto())

    def enable_vpc_classic_link(
        self,
        _request: shapes.EnableVpcClassicLinkRequest = None,
        *,
        vpc_id: str,
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> shapes.EnableVpcClassicLinkResult:
        """
        Enables a VPC for ClassicLink. You can then link EC2-Classic instances to your
        ClassicLink-enabled VPC to allow communication over private IP addresses. You
        cannot enable your VPC for ClassicLink if any of your VPC route tables have
        existing routes for address ranges within the `10.0.0.0/8` IP address range,
        excluding local routes for VPCs in the `10.0.0.0/16` and `10.1.0.0/16` IP
        address ranges. For more information, see
        [ClassicLink](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/vpc-
        classiclink.html) in the _Amazon Elastic Compute Cloud User Guide_.
        """
        if _request is None:
            _params = {}
            if vpc_id is not ShapeBase.NOT_SET:
                _params['vpc_id'] = vpc_id
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.EnableVpcClassicLinkRequest(**_params)
        response = self._boto_client.enable_vpc_classic_link(
            **_request.to_boto()
        )

        return shapes.EnableVpcClassicLinkResult.from_boto(response)

    def enable_vpc_classic_link_dns_support(
        self,
        _request: shapes.EnableVpcClassicLinkDnsSupportRequest = None,
        *,
        vpc_id: str = ShapeBase.NOT_SET,
    ) -> shapes.EnableVpcClassicLinkDnsSupportResult:
        """
        Enables a VPC to support DNS hostname resolution for ClassicLink. If enabled,
        the DNS hostname of a linked EC2-Classic instance resolves to its private IP
        address when addressed from an instance in the VPC to which it's linked.
        Similarly, the DNS hostname of an instance in a VPC resolves to its private IP
        address when addressed from a linked EC2-Classic instance. For more information,
        see [ClassicLink](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/vpc-
        classiclink.html) in the _Amazon Elastic Compute Cloud User Guide_.
        """
        if _request is None:
            _params = {}
            if vpc_id is not ShapeBase.NOT_SET:
                _params['vpc_id'] = vpc_id
            _request = shapes.EnableVpcClassicLinkDnsSupportRequest(**_params)
        response = self._boto_client.enable_vpc_classic_link_dns_support(
            **_request.to_boto()
        )

        return shapes.EnableVpcClassicLinkDnsSupportResult.from_boto(response)

    def get_console_output(
        self,
        _request: shapes.GetConsoleOutputRequest = None,
        *,
        instance_id: str,
        dry_run: bool = ShapeBase.NOT_SET,
        latest: bool = ShapeBase.NOT_SET,
    ) -> shapes.GetConsoleOutputResult:
        """
        Gets the console output for the specified instance. For Linux instances, the
        instance console output displays the exact console output that would normally be
        displayed on a physical monitor attached to a computer. For Windows instances,
        the instance console output includes the last three system event log errors.

        By default, the console output returns buffered information that was posted
        shortly after an instance transition state (start, stop, reboot, or terminate).
        This information is available for at least one hour after the most recent post.
        Only the most recent 64 KB of console output is available.

        You can optionally retrieve the latest serial console output at any time during
        the instance lifecycle. This option is supported on instance types that use the
        Nitro hypervisor.

        For more information, see [Instance Console
        Output](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-
        console.html#instance-console-console-output) in the _Amazon Elastic Compute
        Cloud User Guide_.
        """
        if _request is None:
            _params = {}
            if instance_id is not ShapeBase.NOT_SET:
                _params['instance_id'] = instance_id
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            if latest is not ShapeBase.NOT_SET:
                _params['latest'] = latest
            _request = shapes.GetConsoleOutputRequest(**_params)
        response = self._boto_client.get_console_output(**_request.to_boto())

        return shapes.GetConsoleOutputResult.from_boto(response)

    def get_console_screenshot(
        self,
        _request: shapes.GetConsoleScreenshotRequest = None,
        *,
        instance_id: str,
        dry_run: bool = ShapeBase.NOT_SET,
        wake_up: bool = ShapeBase.NOT_SET,
    ) -> shapes.GetConsoleScreenshotResult:
        """
        Retrieve a JPG-format screenshot of a running instance to help with
        troubleshooting.

        The returned content is Base64-encoded.
        """
        if _request is None:
            _params = {}
            if instance_id is not ShapeBase.NOT_SET:
                _params['instance_id'] = instance_id
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            if wake_up is not ShapeBase.NOT_SET:
                _params['wake_up'] = wake_up
            _request = shapes.GetConsoleScreenshotRequest(**_params)
        response = self._boto_client.get_console_screenshot(
            **_request.to_boto()
        )

        return shapes.GetConsoleScreenshotResult.from_boto(response)

    def get_host_reservation_purchase_preview(
        self,
        _request: shapes.GetHostReservationPurchasePreviewRequest = None,
        *,
        host_id_set: typing.List[str],
        offering_id: str,
    ) -> shapes.GetHostReservationPurchasePreviewResult:
        """
        Preview a reservation purchase with configurations that match those of your
        Dedicated Host. You must have active Dedicated Hosts in your account before you
        purchase a reservation.

        This is a preview of the PurchaseHostReservation action and does not result in
        the offering being purchased.
        """
        if _request is None:
            _params = {}
            if host_id_set is not ShapeBase.NOT_SET:
                _params['host_id_set'] = host_id_set
            if offering_id is not ShapeBase.NOT_SET:
                _params['offering_id'] = offering_id
            _request = shapes.GetHostReservationPurchasePreviewRequest(
                **_params
            )
        response = self._boto_client.get_host_reservation_purchase_preview(
            **_request.to_boto()
        )

        return shapes.GetHostReservationPurchasePreviewResult.from_boto(
            response
        )

    def get_launch_template_data(
        self,
        _request: shapes.GetLaunchTemplateDataRequest = None,
        *,
        instance_id: str,
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> shapes.GetLaunchTemplateDataResult:
        """
        Retrieves the configuration data of the specified instance. You can use this
        data to create a launch template.
        """
        if _request is None:
            _params = {}
            if instance_id is not ShapeBase.NOT_SET:
                _params['instance_id'] = instance_id
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.GetLaunchTemplateDataRequest(**_params)
        response = self._boto_client.get_launch_template_data(
            **_request.to_boto()
        )

        return shapes.GetLaunchTemplateDataResult.from_boto(response)

    def get_password_data(
        self,
        _request: shapes.GetPasswordDataRequest = None,
        *,
        instance_id: str,
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> shapes.GetPasswordDataResult:
        """
        Retrieves the encrypted administrator password for a running Windows instance.

        The Windows password is generated at boot by the `EC2Config` service or
        `EC2Launch` scripts (Windows Server 2016 and later). This usually only happens
        the first time an instance is launched. For more information, see
        [EC2Config](http://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/UsingConfig_WinAMI.html)
        and
        [EC2Launch](http://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/ec2launch.html)
        in the Amazon Elastic Compute Cloud User Guide.

        For the `EC2Config` service, the password is not generated for rebundled AMIs
        unless `Ec2SetPassword` is enabled before bundling.

        The password is encrypted using the key pair that you specified when you
        launched the instance. You must provide the corresponding key pair file.

        When you launch an instance, password generation and encryption may take a few
        minutes. If you try to retrieve the password before it's available, the output
        returns an empty string. We recommend that you wait up to 15 minutes after
        launching an instance before trying to retrieve the generated password.
        """
        if _request is None:
            _params = {}
            if instance_id is not ShapeBase.NOT_SET:
                _params['instance_id'] = instance_id
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.GetPasswordDataRequest(**_params)
        response = self._boto_client.get_password_data(**_request.to_boto())

        return shapes.GetPasswordDataResult.from_boto(response)

    def get_reserved_instances_exchange_quote(
        self,
        _request: shapes.GetReservedInstancesExchangeQuoteRequest = None,
        *,
        reserved_instance_ids: typing.List[str],
        dry_run: bool = ShapeBase.NOT_SET,
        target_configurations: typing.List[shapes.TargetConfigurationRequest
                                          ] = ShapeBase.NOT_SET,
    ) -> shapes.GetReservedInstancesExchangeQuoteResult:
        """
        Returns a quote and exchange information for exchanging one or more specified
        Convertible Reserved Instances for a new Convertible Reserved Instance. If the
        exchange cannot be performed, the reason is returned in the response. Use
        AcceptReservedInstancesExchangeQuote to perform the exchange.
        """
        if _request is None:
            _params = {}
            if reserved_instance_ids is not ShapeBase.NOT_SET:
                _params['reserved_instance_ids'] = reserved_instance_ids
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            if target_configurations is not ShapeBase.NOT_SET:
                _params['target_configurations'] = target_configurations
            _request = shapes.GetReservedInstancesExchangeQuoteRequest(
                **_params
            )
        response = self._boto_client.get_reserved_instances_exchange_quote(
            **_request.to_boto()
        )

        return shapes.GetReservedInstancesExchangeQuoteResult.from_boto(
            response
        )

    def import_image(
        self,
        _request: shapes.ImportImageRequest = None,
        *,
        architecture: str = ShapeBase.NOT_SET,
        client_data: shapes.ClientData = ShapeBase.NOT_SET,
        client_token: str = ShapeBase.NOT_SET,
        description: str = ShapeBase.NOT_SET,
        disk_containers: typing.List[shapes.ImageDiskContainer
                                    ] = ShapeBase.NOT_SET,
        dry_run: bool = ShapeBase.NOT_SET,
        hypervisor: str = ShapeBase.NOT_SET,
        license_type: str = ShapeBase.NOT_SET,
        platform: str = ShapeBase.NOT_SET,
        role_name: str = ShapeBase.NOT_SET,
    ) -> shapes.ImportImageResult:
        """
        Import single or multi-volume disk images or EBS snapshots into an Amazon
        Machine Image (AMI). For more information, see [Importing a VM as an Image Using
        VM Import/Export](http://docs.aws.amazon.com/vm-
        import/latest/userguide/vmimport-image-import.html) in the _VM Import/Export
        User Guide_.
        """
        if _request is None:
            _params = {}
            if architecture is not ShapeBase.NOT_SET:
                _params['architecture'] = architecture
            if client_data is not ShapeBase.NOT_SET:
                _params['client_data'] = client_data
            if client_token is not ShapeBase.NOT_SET:
                _params['client_token'] = client_token
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if disk_containers is not ShapeBase.NOT_SET:
                _params['disk_containers'] = disk_containers
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            if hypervisor is not ShapeBase.NOT_SET:
                _params['hypervisor'] = hypervisor
            if license_type is not ShapeBase.NOT_SET:
                _params['license_type'] = license_type
            if platform is not ShapeBase.NOT_SET:
                _params['platform'] = platform
            if role_name is not ShapeBase.NOT_SET:
                _params['role_name'] = role_name
            _request = shapes.ImportImageRequest(**_params)
        response = self._boto_client.import_image(**_request.to_boto())

        return shapes.ImportImageResult.from_boto(response)

    def import_instance(
        self,
        _request: shapes.ImportInstanceRequest = None,
        *,
        platform: typing.Union[str, shapes.PlatformValues],
        description: str = ShapeBase.NOT_SET,
        disk_images: typing.List[shapes.DiskImage] = ShapeBase.NOT_SET,
        dry_run: bool = ShapeBase.NOT_SET,
        launch_specification: shapes.
        ImportInstanceLaunchSpecification = ShapeBase.NOT_SET,
    ) -> shapes.ImportInstanceResult:
        """
        Creates an import instance task using metadata from the specified disk image.
        `ImportInstance` only supports single-volume VMs. To import multi-volume VMs,
        use ImportImage. For more information, see [Importing a Virtual Machine Using
        the Amazon EC2
        CLI](http://docs.aws.amazon.com/AWSEC2/latest/CommandLineReference/ec2-cli-
        vmimport-export.html).

        For information about the import manifest referenced by this API action, see [VM
        Import
        Manifest](http://docs.aws.amazon.com/AWSEC2/latest/APIReference/manifest.html).
        """
        if _request is None:
            _params = {}
            if platform is not ShapeBase.NOT_SET:
                _params['platform'] = platform
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if disk_images is not ShapeBase.NOT_SET:
                _params['disk_images'] = disk_images
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            if launch_specification is not ShapeBase.NOT_SET:
                _params['launch_specification'] = launch_specification
            _request = shapes.ImportInstanceRequest(**_params)
        response = self._boto_client.import_instance(**_request.to_boto())

        return shapes.ImportInstanceResult.from_boto(response)

    def import_key_pair(
        self,
        _request: shapes.ImportKeyPairRequest = None,
        *,
        key_name: str,
        public_key_material: typing.Any,
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> shapes.ImportKeyPairResult:
        """
        Imports the public key from an RSA key pair that you created with a third-party
        tool. Compare this with CreateKeyPair, in which AWS creates the key pair and
        gives the keys to you (AWS keeps a copy of the public key). With ImportKeyPair,
        you create the key pair and give AWS just the public key. The private key is
        never transferred between you and AWS.

        For more information about key pairs, see [Key
        Pairs](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html) in
        the _Amazon Elastic Compute Cloud User Guide_.
        """
        if _request is None:
            _params = {}
            if key_name is not ShapeBase.NOT_SET:
                _params['key_name'] = key_name
            if public_key_material is not ShapeBase.NOT_SET:
                _params['public_key_material'] = public_key_material
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.ImportKeyPairRequest(**_params)
        response = self._boto_client.import_key_pair(**_request.to_boto())

        return shapes.ImportKeyPairResult.from_boto(response)

    def import_snapshot(
        self,
        _request: shapes.ImportSnapshotRequest = None,
        *,
        client_data: shapes.ClientData = ShapeBase.NOT_SET,
        client_token: str = ShapeBase.NOT_SET,
        description: str = ShapeBase.NOT_SET,
        disk_container: shapes.SnapshotDiskContainer = ShapeBase.NOT_SET,
        dry_run: bool = ShapeBase.NOT_SET,
        role_name: str = ShapeBase.NOT_SET,
    ) -> shapes.ImportSnapshotResult:
        """
        Imports a disk into an EBS snapshot.
        """
        if _request is None:
            _params = {}
            if client_data is not ShapeBase.NOT_SET:
                _params['client_data'] = client_data
            if client_token is not ShapeBase.NOT_SET:
                _params['client_token'] = client_token
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if disk_container is not ShapeBase.NOT_SET:
                _params['disk_container'] = disk_container
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            if role_name is not ShapeBase.NOT_SET:
                _params['role_name'] = role_name
            _request = shapes.ImportSnapshotRequest(**_params)
        response = self._boto_client.import_snapshot(**_request.to_boto())

        return shapes.ImportSnapshotResult.from_boto(response)

    def import_volume(
        self,
        _request: shapes.ImportVolumeRequest = None,
        *,
        availability_zone: str,
        image: shapes.DiskImageDetail,
        volume: shapes.VolumeDetail,
        description: str = ShapeBase.NOT_SET,
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> shapes.ImportVolumeResult:
        """
        Creates an import volume task using metadata from the specified disk image.For
        more information, see [Importing Disks to Amazon
        EBS](http://docs.aws.amazon.com/AWSEC2/latest/CommandLineReference/importing-
        your-volumes-into-amazon-ebs.html).

        For information about the import manifest referenced by this API action, see [VM
        Import
        Manifest](http://docs.aws.amazon.com/AWSEC2/latest/APIReference/manifest.html).
        """
        if _request is None:
            _params = {}
            if availability_zone is not ShapeBase.NOT_SET:
                _params['availability_zone'] = availability_zone
            if image is not ShapeBase.NOT_SET:
                _params['image'] = image
            if volume is not ShapeBase.NOT_SET:
                _params['volume'] = volume
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.ImportVolumeRequest(**_params)
        response = self._boto_client.import_volume(**_request.to_boto())

        return shapes.ImportVolumeResult.from_boto(response)

    def modify_fleet(
        self,
        _request: shapes.ModifyFleetRequest = None,
        *,
        fleet_id: str,
        target_capacity_specification: shapes.
        TargetCapacitySpecificationRequest,
        dry_run: bool = ShapeBase.NOT_SET,
        excess_capacity_termination_policy: typing.
        Union[str, shapes.
              FleetExcessCapacityTerminationPolicy] = ShapeBase.NOT_SET,
    ) -> shapes.ModifyFleetResult:
        """
        Modifies the specified EC2 Fleet.

        While the EC2 Fleet is being modified, it is in the `modifying` state.
        """
        if _request is None:
            _params = {}
            if fleet_id is not ShapeBase.NOT_SET:
                _params['fleet_id'] = fleet_id
            if target_capacity_specification is not ShapeBase.NOT_SET:
                _params['target_capacity_specification'
                       ] = target_capacity_specification
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            if excess_capacity_termination_policy is not ShapeBase.NOT_SET:
                _params['excess_capacity_termination_policy'
                       ] = excess_capacity_termination_policy
            _request = shapes.ModifyFleetRequest(**_params)
        response = self._boto_client.modify_fleet(**_request.to_boto())

        return shapes.ModifyFleetResult.from_boto(response)

    def modify_fpga_image_attribute(
        self,
        _request: shapes.ModifyFpgaImageAttributeRequest = None,
        *,
        fpga_image_id: str,
        dry_run: bool = ShapeBase.NOT_SET,
        attribute: typing.Union[str, shapes.
                                FpgaImageAttributeName] = ShapeBase.NOT_SET,
        operation_type: typing.Union[str, shapes.OperationType] = ShapeBase.
        NOT_SET,
        user_ids: typing.List[str] = ShapeBase.NOT_SET,
        user_groups: typing.List[str] = ShapeBase.NOT_SET,
        product_codes: typing.List[str] = ShapeBase.NOT_SET,
        load_permission: shapes.LoadPermissionModifications = ShapeBase.NOT_SET,
        description: str = ShapeBase.NOT_SET,
        name: str = ShapeBase.NOT_SET,
    ) -> shapes.ModifyFpgaImageAttributeResult:
        """
        Modifies the specified attribute of the specified Amazon FPGA Image (AFI).
        """
        if _request is None:
            _params = {}
            if fpga_image_id is not ShapeBase.NOT_SET:
                _params['fpga_image_id'] = fpga_image_id
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            if attribute is not ShapeBase.NOT_SET:
                _params['attribute'] = attribute
            if operation_type is not ShapeBase.NOT_SET:
                _params['operation_type'] = operation_type
            if user_ids is not ShapeBase.NOT_SET:
                _params['user_ids'] = user_ids
            if user_groups is not ShapeBase.NOT_SET:
                _params['user_groups'] = user_groups
            if product_codes is not ShapeBase.NOT_SET:
                _params['product_codes'] = product_codes
            if load_permission is not ShapeBase.NOT_SET:
                _params['load_permission'] = load_permission
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            _request = shapes.ModifyFpgaImageAttributeRequest(**_params)
        response = self._boto_client.modify_fpga_image_attribute(
            **_request.to_boto()
        )

        return shapes.ModifyFpgaImageAttributeResult.from_boto(response)

    def modify_hosts(
        self,
        _request: shapes.ModifyHostsRequest = None,
        *,
        auto_placement: typing.Union[str, shapes.AutoPlacement],
        host_ids: typing.List[str],
    ) -> shapes.ModifyHostsResult:
        """
        Modify the auto-placement setting of a Dedicated Host. When auto-placement is
        enabled, any instances that you launch with a tenancy of `host` but without a
        specific host ID are placed onto any available Dedicated Host in your account
        that has auto-placement enabled. When auto-placement is disabled, you need to
        provide a host ID to have the instance launch onto a specific host. If no host
        ID is provided, the instance is launched onto a suitable host with auto-
        placement enabled.
        """
        if _request is None:
            _params = {}
            if auto_placement is not ShapeBase.NOT_SET:
                _params['auto_placement'] = auto_placement
            if host_ids is not ShapeBase.NOT_SET:
                _params['host_ids'] = host_ids
            _request = shapes.ModifyHostsRequest(**_params)
        response = self._boto_client.modify_hosts(**_request.to_boto())

        return shapes.ModifyHostsResult.from_boto(response)

    def modify_id_format(
        self,
        _request: shapes.ModifyIdFormatRequest = None,
        *,
        resource: str,
        use_long_ids: bool,
    ) -> None:
        """
        Modifies the ID format for the specified resource on a per-region basis. You can
        specify that resources should receive longer IDs (17-character IDs) when they
        are created.

        This request can only be used to modify longer ID settings for resource types
        that are within the opt-in period. Resources currently in their opt-in period
        include: `bundle` | `conversion-task` | `customer-gateway` | `dhcp-options` |
        `elastic-ip-allocation` | `elastic-ip-association` | `export-task` | `flow-log`
        | `image` | `import-task` | `internet-gateway` | `network-acl` | `network-acl-
        association` | `network-interface` | `network-interface-attachment` | `prefix-
        list` | `route-table` | `route-table-association` | `security-group` | `subnet`
        | `subnet-cidr-block-association` | `vpc` | `vpc-cidr-block-association` | `vpc-
        endpoint` | `vpc-peering-connection` | `vpn-connection` | `vpn-gateway`.

        This setting applies to the IAM user who makes the request; it does not apply to
        the entire AWS account. By default, an IAM user defaults to the same settings as
        the root user. If you're using this action as the root user, then these settings
        apply to the entire account, unless an IAM user explicitly overrides these
        settings for themselves. For more information, see [Resource
        IDs](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/resource-ids.html) in
        the _Amazon Elastic Compute Cloud User Guide_.

        Resources created with longer IDs are visible to all IAM roles and users,
        regardless of these settings and provided that they have permission to use the
        relevant `Describe` command for the resource type.
        """
        if _request is None:
            _params = {}
            if resource is not ShapeBase.NOT_SET:
                _params['resource'] = resource
            if use_long_ids is not ShapeBase.NOT_SET:
                _params['use_long_ids'] = use_long_ids
            _request = shapes.ModifyIdFormatRequest(**_params)
        response = self._boto_client.modify_id_format(**_request.to_boto())

    def modify_identity_id_format(
        self,
        _request: shapes.ModifyIdentityIdFormatRequest = None,
        *,
        principal_arn: str,
        resource: str,
        use_long_ids: bool,
    ) -> None:
        """
        Modifies the ID format of a resource for a specified IAM user, IAM role, or the
        root user for an account; or all IAM users, IAM roles, and the root user for an
        account. You can specify that resources should receive longer IDs (17-character
        IDs) when they are created.

        This request can only be used to modify longer ID settings for resource types
        that are within the opt-in period. Resources currently in their opt-in period
        include: `bundle` | `conversion-task` | `customer-gateway` | `dhcp-options` |
        `elastic-ip-allocation` | `elastic-ip-association` | `export-task` | `flow-log`
        | `image` | `import-task` | `internet-gateway` | `network-acl` | `network-acl-
        association` | `network-interface` | `network-interface-attachment` | `prefix-
        list` | `route-table` | `route-table-association` | `security-group` | `subnet`
        | `subnet-cidr-block-association` | `vpc` | `vpc-cidr-block-association` | `vpc-
        endpoint` | `vpc-peering-connection` | `vpn-connection` | `vpn-gateway`.

        For more information, see [Resource
        IDs](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/resource-ids.html) in
        the _Amazon Elastic Compute Cloud User Guide_.

        This setting applies to the principal specified in the request; it does not
        apply to the principal that makes the request.

        Resources created with longer IDs are visible to all IAM roles and users,
        regardless of these settings and provided that they have permission to use the
        relevant `Describe` command for the resource type.
        """
        if _request is None:
            _params = {}
            if principal_arn is not ShapeBase.NOT_SET:
                _params['principal_arn'] = principal_arn
            if resource is not ShapeBase.NOT_SET:
                _params['resource'] = resource
            if use_long_ids is not ShapeBase.NOT_SET:
                _params['use_long_ids'] = use_long_ids
            _request = shapes.ModifyIdentityIdFormatRequest(**_params)
        response = self._boto_client.modify_identity_id_format(
            **_request.to_boto()
        )

    def modify_image_attribute(
        self,
        _request: shapes.ModifyImageAttributeRequest = None,
        *,
        image_id: str,
        attribute: str = ShapeBase.NOT_SET,
        description: shapes.AttributeValue = ShapeBase.NOT_SET,
        launch_permission: shapes.LaunchPermissionModifications = ShapeBase.
        NOT_SET,
        operation_type: typing.Union[str, shapes.
                                     OperationType] = ShapeBase.NOT_SET,
        product_codes: typing.List[str] = ShapeBase.NOT_SET,
        user_groups: typing.List[str] = ShapeBase.NOT_SET,
        user_ids: typing.List[str] = ShapeBase.NOT_SET,
        value: str = ShapeBase.NOT_SET,
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> None:
        """
        Modifies the specified attribute of the specified AMI. You can specify only one
        attribute at a time. You can use the `Attribute` parameter to specify the
        attribute or one of the following parameters: `Description`, `LaunchPermission`,
        or `ProductCode`.

        AWS Marketplace product codes cannot be modified. Images with an AWS Marketplace
        product code cannot be made public.

        To enable the SriovNetSupport enhanced networking attribute of an image, enable
        SriovNetSupport on an instance and create an AMI from the instance.
        """
        if _request is None:
            _params = {}
            if image_id is not ShapeBase.NOT_SET:
                _params['image_id'] = image_id
            if attribute is not ShapeBase.NOT_SET:
                _params['attribute'] = attribute
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if launch_permission is not ShapeBase.NOT_SET:
                _params['launch_permission'] = launch_permission
            if operation_type is not ShapeBase.NOT_SET:
                _params['operation_type'] = operation_type
            if product_codes is not ShapeBase.NOT_SET:
                _params['product_codes'] = product_codes
            if user_groups is not ShapeBase.NOT_SET:
                _params['user_groups'] = user_groups
            if user_ids is not ShapeBase.NOT_SET:
                _params['user_ids'] = user_ids
            if value is not ShapeBase.NOT_SET:
                _params['value'] = value
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.ModifyImageAttributeRequest(**_params)
        response = self._boto_client.modify_image_attribute(
            **_request.to_boto()
        )

    def modify_instance_attribute(
        self,
        _request: shapes.ModifyInstanceAttributeRequest = None,
        *,
        instance_id: str,
        source_dest_check: shapes.AttributeBooleanValue = ShapeBase.NOT_SET,
        attribute: typing.Union[str, shapes.
                                InstanceAttributeName] = ShapeBase.NOT_SET,
        block_device_mappings: typing.List[
            shapes.InstanceBlockDeviceMappingSpecification] = ShapeBase.NOT_SET,
        disable_api_termination: shapes.AttributeBooleanValue = ShapeBase.
        NOT_SET,
        dry_run: bool = ShapeBase.NOT_SET,
        ebs_optimized: shapes.AttributeBooleanValue = ShapeBase.NOT_SET,
        ena_support: shapes.AttributeBooleanValue = ShapeBase.NOT_SET,
        groups: typing.List[str] = ShapeBase.NOT_SET,
        instance_initiated_shutdown_behavior: shapes.AttributeValue = ShapeBase.
        NOT_SET,
        instance_type: shapes.AttributeValue = ShapeBase.NOT_SET,
        kernel: shapes.AttributeValue = ShapeBase.NOT_SET,
        ramdisk: shapes.AttributeValue = ShapeBase.NOT_SET,
        sriov_net_support: shapes.AttributeValue = ShapeBase.NOT_SET,
        user_data: shapes.BlobAttributeValue = ShapeBase.NOT_SET,
        value: str = ShapeBase.NOT_SET,
    ) -> None:
        """
        Modifies the specified attribute of the specified instance. You can specify only
        one attribute at a time.

        **Note:** Using this action to change the security groups associated with an
        elastic network interface (ENI) attached to an instance in a VPC can result in
        an error if the instance has more than one ENI. To change the security groups
        associated with an ENI attached to an instance that has multiple ENIs, we
        recommend that you use the ModifyNetworkInterfaceAttribute action.

        To modify some attributes, the instance must be stopped. For more information,
        see [Modifying Attributes of a Stopped
        Instance](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_ChangingAttributesWhileInstanceStopped.html)
        in the _Amazon Elastic Compute Cloud User Guide_.
        """
        if _request is None:
            _params = {}
            if instance_id is not ShapeBase.NOT_SET:
                _params['instance_id'] = instance_id
            if source_dest_check is not ShapeBase.NOT_SET:
                _params['source_dest_check'] = source_dest_check
            if attribute is not ShapeBase.NOT_SET:
                _params['attribute'] = attribute
            if block_device_mappings is not ShapeBase.NOT_SET:
                _params['block_device_mappings'] = block_device_mappings
            if disable_api_termination is not ShapeBase.NOT_SET:
                _params['disable_api_termination'] = disable_api_termination
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            if ebs_optimized is not ShapeBase.NOT_SET:
                _params['ebs_optimized'] = ebs_optimized
            if ena_support is not ShapeBase.NOT_SET:
                _params['ena_support'] = ena_support
            if groups is not ShapeBase.NOT_SET:
                _params['groups'] = groups
            if instance_initiated_shutdown_behavior is not ShapeBase.NOT_SET:
                _params['instance_initiated_shutdown_behavior'
                       ] = instance_initiated_shutdown_behavior
            if instance_type is not ShapeBase.NOT_SET:
                _params['instance_type'] = instance_type
            if kernel is not ShapeBase.NOT_SET:
                _params['kernel'] = kernel
            if ramdisk is not ShapeBase.NOT_SET:
                _params['ramdisk'] = ramdisk
            if sriov_net_support is not ShapeBase.NOT_SET:
                _params['sriov_net_support'] = sriov_net_support
            if user_data is not ShapeBase.NOT_SET:
                _params['user_data'] = user_data
            if value is not ShapeBase.NOT_SET:
                _params['value'] = value
            _request = shapes.ModifyInstanceAttributeRequest(**_params)
        response = self._boto_client.modify_instance_attribute(
            **_request.to_boto()
        )

    def modify_instance_credit_specification(
        self,
        _request: shapes.ModifyInstanceCreditSpecificationRequest = None,
        *,
        instance_credit_specifications: typing.List[
            shapes.InstanceCreditSpecificationRequest],
        dry_run: bool = ShapeBase.NOT_SET,
        client_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ModifyInstanceCreditSpecificationResult:
        """
        Modifies the credit option for CPU usage on a running or stopped T2 or T3
        instance. The credit options are `standard` and `unlimited`.

        For more information, see [Burstable Performance
        Instances](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/burstable-
        performance-instances.html) in the _Amazon Elastic Compute Cloud User Guide_.
        """
        if _request is None:
            _params = {}
            if instance_credit_specifications is not ShapeBase.NOT_SET:
                _params['instance_credit_specifications'
                       ] = instance_credit_specifications
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            if client_token is not ShapeBase.NOT_SET:
                _params['client_token'] = client_token
            _request = shapes.ModifyInstanceCreditSpecificationRequest(
                **_params
            )
        response = self._boto_client.modify_instance_credit_specification(
            **_request.to_boto()
        )

        return shapes.ModifyInstanceCreditSpecificationResult.from_boto(
            response
        )

    def modify_instance_placement(
        self,
        _request: shapes.ModifyInstancePlacementRequest = None,
        *,
        instance_id: str,
        affinity: typing.Union[str, shapes.Affinity] = ShapeBase.NOT_SET,
        group_name: str = ShapeBase.NOT_SET,
        host_id: str = ShapeBase.NOT_SET,
        tenancy: typing.Union[str, shapes.HostTenancy] = ShapeBase.NOT_SET,
    ) -> shapes.ModifyInstancePlacementResult:
        """
        Modifies the placement attributes for a specified instance. You can do the
        following:

          * Modify the affinity between an instance and a [Dedicated Host](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/dedicated-hosts-overview.html). When affinity is set to `host` and the instance is not associated with a specific Dedicated Host, the next time the instance is launched, it is automatically associated with the host on which it lands. If the instance is restarted or rebooted, this relationship persists.

          * Change the Dedicated Host with which an instance is associated.

          * Change the instance tenancy of an instance from `host` to `dedicated`, or from `dedicated` to `host`.

          * Move an instance to or from a [placement group](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html).

        At least one attribute for affinity, host ID, tenancy, or placement group name
        must be specified in the request. Affinity and tenancy can be modified in the
        same request.

        To modify the host ID, tenancy, or placement group for an instance, the instance
        must be in the `stopped` state.
        """
        if _request is None:
            _params = {}
            if instance_id is not ShapeBase.NOT_SET:
                _params['instance_id'] = instance_id
            if affinity is not ShapeBase.NOT_SET:
                _params['affinity'] = affinity
            if group_name is not ShapeBase.NOT_SET:
                _params['group_name'] = group_name
            if host_id is not ShapeBase.NOT_SET:
                _params['host_id'] = host_id
            if tenancy is not ShapeBase.NOT_SET:
                _params['tenancy'] = tenancy
            _request = shapes.ModifyInstancePlacementRequest(**_params)
        response = self._boto_client.modify_instance_placement(
            **_request.to_boto()
        )

        return shapes.ModifyInstancePlacementResult.from_boto(response)

    def modify_launch_template(
        self,
        _request: shapes.ModifyLaunchTemplateRequest = None,
        *,
        dry_run: bool = ShapeBase.NOT_SET,
        client_token: str = ShapeBase.NOT_SET,
        launch_template_id: str = ShapeBase.NOT_SET,
        launch_template_name: str = ShapeBase.NOT_SET,
        default_version: str = ShapeBase.NOT_SET,
    ) -> shapes.ModifyLaunchTemplateResult:
        """
        Modifies a launch template. You can specify which version of the launch template
        to set as the default version. When launching an instance, the default version
        applies when a launch template version is not specified.
        """
        if _request is None:
            _params = {}
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            if client_token is not ShapeBase.NOT_SET:
                _params['client_token'] = client_token
            if launch_template_id is not ShapeBase.NOT_SET:
                _params['launch_template_id'] = launch_template_id
            if launch_template_name is not ShapeBase.NOT_SET:
                _params['launch_template_name'] = launch_template_name
            if default_version is not ShapeBase.NOT_SET:
                _params['default_version'] = default_version
            _request = shapes.ModifyLaunchTemplateRequest(**_params)
        response = self._boto_client.modify_launch_template(
            **_request.to_boto()
        )

        return shapes.ModifyLaunchTemplateResult.from_boto(response)

    def modify_network_interface_attribute(
        self,
        _request: shapes.ModifyNetworkInterfaceAttributeRequest = None,
        *,
        network_interface_id: str,
        attachment: shapes.NetworkInterfaceAttachmentChanges = ShapeBase.
        NOT_SET,
        description: shapes.AttributeValue = ShapeBase.NOT_SET,
        dry_run: bool = ShapeBase.NOT_SET,
        groups: typing.List[str] = ShapeBase.NOT_SET,
        source_dest_check: shapes.AttributeBooleanValue = ShapeBase.NOT_SET,
    ) -> None:
        """
        Modifies the specified network interface attribute. You can specify only one
        attribute at a time.
        """
        if _request is None:
            _params = {}
            if network_interface_id is not ShapeBase.NOT_SET:
                _params['network_interface_id'] = network_interface_id
            if attachment is not ShapeBase.NOT_SET:
                _params['attachment'] = attachment
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            if groups is not ShapeBase.NOT_SET:
                _params['groups'] = groups
            if source_dest_check is not ShapeBase.NOT_SET:
                _params['source_dest_check'] = source_dest_check
            _request = shapes.ModifyNetworkInterfaceAttributeRequest(**_params)
        response = self._boto_client.modify_network_interface_attribute(
            **_request.to_boto()
        )

    def modify_reserved_instances(
        self,
        _request: shapes.ModifyReservedInstancesRequest = None,
        *,
        reserved_instances_ids: typing.List[str],
        target_configurations: typing.List[shapes.ReservedInstancesConfiguration
                                          ],
        client_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ModifyReservedInstancesResult:
        """
        Modifies the Availability Zone, instance count, instance type, or network
        platform (EC2-Classic or EC2-VPC) of your Reserved Instances. The Reserved
        Instances to be modified must be identical, except for Availability Zone,
        network platform, and instance type.

        For more information, see [Modifying Reserved
        Instances](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ri-modifying.html)
        in the Amazon Elastic Compute Cloud User Guide.
        """
        if _request is None:
            _params = {}
            if reserved_instances_ids is not ShapeBase.NOT_SET:
                _params['reserved_instances_ids'] = reserved_instances_ids
            if target_configurations is not ShapeBase.NOT_SET:
                _params['target_configurations'] = target_configurations
            if client_token is not ShapeBase.NOT_SET:
                _params['client_token'] = client_token
            _request = shapes.ModifyReservedInstancesRequest(**_params)
        response = self._boto_client.modify_reserved_instances(
            **_request.to_boto()
        )

        return shapes.ModifyReservedInstancesResult.from_boto(response)

    def modify_snapshot_attribute(
        self,
        _request: shapes.ModifySnapshotAttributeRequest = None,
        *,
        snapshot_id: str,
        attribute: typing.Union[str, shapes.
                                SnapshotAttributeName] = ShapeBase.NOT_SET,
        create_volume_permission: shapes.
        CreateVolumePermissionModifications = ShapeBase.NOT_SET,
        group_names: typing.List[str] = ShapeBase.NOT_SET,
        operation_type: typing.Union[str, shapes.
                                     OperationType] = ShapeBase.NOT_SET,
        user_ids: typing.List[str] = ShapeBase.NOT_SET,
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> None:
        """
        Adds or removes permission settings for the specified snapshot. You may add or
        remove specified AWS account IDs from a snapshot's list of create volume
        permissions, but you cannot do both in a single API call. If you need to both
        add and remove account IDs for a snapshot, you must use multiple API calls.

        Encrypted snapshots and snapshots with AWS Marketplace product codes cannot be
        made public. Snapshots encrypted with your default CMK cannot be shared with
        other accounts.

        For more information about modifying snapshot permissions, see [Sharing
        Snapshots](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-modifying-
        snapshot-permissions.html) in the _Amazon Elastic Compute Cloud User Guide_.
        """
        if _request is None:
            _params = {}
            if snapshot_id is not ShapeBase.NOT_SET:
                _params['snapshot_id'] = snapshot_id
            if attribute is not ShapeBase.NOT_SET:
                _params['attribute'] = attribute
            if create_volume_permission is not ShapeBase.NOT_SET:
                _params['create_volume_permission'] = create_volume_permission
            if group_names is not ShapeBase.NOT_SET:
                _params['group_names'] = group_names
            if operation_type is not ShapeBase.NOT_SET:
                _params['operation_type'] = operation_type
            if user_ids is not ShapeBase.NOT_SET:
                _params['user_ids'] = user_ids
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.ModifySnapshotAttributeRequest(**_params)
        response = self._boto_client.modify_snapshot_attribute(
            **_request.to_boto()
        )

    def modify_spot_fleet_request(
        self,
        _request: shapes.ModifySpotFleetRequestRequest = None,
        *,
        spot_fleet_request_id: str,
        excess_capacity_termination_policy: typing.
        Union[str, shapes.ExcessCapacityTerminationPolicy] = ShapeBase.NOT_SET,
        target_capacity: int = ShapeBase.NOT_SET,
    ) -> shapes.ModifySpotFleetRequestResponse:
        """
        Modifies the specified Spot Fleet request.

        While the Spot Fleet request is being modified, it is in the `modifying` state.

        To scale up your Spot Fleet, increase its target capacity. The Spot Fleet
        launches the additional Spot Instances according to the allocation strategy for
        the Spot Fleet request. If the allocation strategy is `lowestPrice`, the Spot
        Fleet launches instances using the Spot pool with the lowest price. If the
        allocation strategy is `diversified`, the Spot Fleet distributes the instances
        across the Spot pools.

        To scale down your Spot Fleet, decrease its target capacity. First, the Spot
        Fleet cancels any open requests that exceed the new target capacity. You can
        request that the Spot Fleet terminate Spot Instances until the size of the fleet
        no longer exceeds the new target capacity. If the allocation strategy is
        `lowestPrice`, the Spot Fleet terminates the instances with the highest price
        per unit. If the allocation strategy is `diversified`, the Spot Fleet terminates
        instances across the Spot pools. Alternatively, you can request that the Spot
        Fleet keep the fleet at its current size, but not replace any Spot Instances
        that are interrupted or that you terminate manually.

        If you are finished with your Spot Fleet for now, but will use it again later,
        you can set the target capacity to 0.
        """
        if _request is None:
            _params = {}
            if spot_fleet_request_id is not ShapeBase.NOT_SET:
                _params['spot_fleet_request_id'] = spot_fleet_request_id
            if excess_capacity_termination_policy is not ShapeBase.NOT_SET:
                _params['excess_capacity_termination_policy'
                       ] = excess_capacity_termination_policy
            if target_capacity is not ShapeBase.NOT_SET:
                _params['target_capacity'] = target_capacity
            _request = shapes.ModifySpotFleetRequestRequest(**_params)
        response = self._boto_client.modify_spot_fleet_request(
            **_request.to_boto()
        )

        return shapes.ModifySpotFleetRequestResponse.from_boto(response)

    def modify_subnet_attribute(
        self,
        _request: shapes.ModifySubnetAttributeRequest = None,
        *,
        subnet_id: str,
        assign_ipv6_address_on_creation: shapes.
        AttributeBooleanValue = ShapeBase.NOT_SET,
        map_public_ip_on_launch: shapes.AttributeBooleanValue = ShapeBase.
        NOT_SET,
    ) -> None:
        """
        Modifies a subnet attribute. You can only modify one attribute at a time.
        """
        if _request is None:
            _params = {}
            if subnet_id is not ShapeBase.NOT_SET:
                _params['subnet_id'] = subnet_id
            if assign_ipv6_address_on_creation is not ShapeBase.NOT_SET:
                _params['assign_ipv6_address_on_creation'
                       ] = assign_ipv6_address_on_creation
            if map_public_ip_on_launch is not ShapeBase.NOT_SET:
                _params['map_public_ip_on_launch'] = map_public_ip_on_launch
            _request = shapes.ModifySubnetAttributeRequest(**_params)
        response = self._boto_client.modify_subnet_attribute(
            **_request.to_boto()
        )

    def modify_volume(
        self,
        _request: shapes.ModifyVolumeRequest = None,
        *,
        volume_id: str,
        dry_run: bool = ShapeBase.NOT_SET,
        size: int = ShapeBase.NOT_SET,
        volume_type: typing.Union[str, shapes.VolumeType] = ShapeBase.NOT_SET,
        iops: int = ShapeBase.NOT_SET,
    ) -> shapes.ModifyVolumeResult:
        """
        You can modify several parameters of an existing EBS volume, including volume
        size, volume type, and IOPS capacity. If your EBS volume is attached to a
        current-generation EC2 instance type, you may be able to apply these changes
        without stopping the instance or detaching the volume from it. For more
        information about modifying an EBS volume running Linux, see [Modifying the
        Size, IOPS, or Type of an EBS Volume on
        Linux](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-expand-
        volume.html). For more information about modifying an EBS volume running
        Windows, see [Modifying the Size, IOPS, or Type of an EBS Volume on
        Windows](http://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/ebs-expand-
        volume.html).

        When you complete a resize operation on your volume, you need to extend the
        volume's file-system size to take advantage of the new storage capacity. For
        information about extending a Linux file system, see [Extending a Linux File
        System](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-expand-
        volume.html#recognize-expanded-volume-linux). For information about extending a
        Windows file system, see [Extending a Windows File
        System](http://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/ebs-expand-
        volume.html#recognize-expanded-volume-windows).

        You can use CloudWatch Events to check the status of a modification to an EBS
        volume. For information about CloudWatch Events, see the [Amazon CloudWatch
        Events User Guide](http://docs.aws.amazon.com/AmazonCloudWatch/latest/events/).
        You can also track the status of a modification using the
        DescribeVolumesModifications API. For information about tracking status changes
        using either method, see [Monitoring Volume
        Modifications](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-expand-
        volume.html#monitoring_mods).

        With previous-generation instance types, resizing an EBS volume may require
        detaching and reattaching the volume or stopping and restarting the instance.
        For more information, see [Modifying the Size, IOPS, or Type of an EBS Volume on
        Linux](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-expand-
        volume.html) and [Modifying the Size, IOPS, or Type of an EBS Volume on
        Windows](http://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/ebs-expand-
        volume.html).

        If you reach the maximum volume modification rate per volume limit, you will
        need to wait at least six hours before applying further modifications to the
        affected EBS volume.
        """
        if _request is None:
            _params = {}
            if volume_id is not ShapeBase.NOT_SET:
                _params['volume_id'] = volume_id
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            if size is not ShapeBase.NOT_SET:
                _params['size'] = size
            if volume_type is not ShapeBase.NOT_SET:
                _params['volume_type'] = volume_type
            if iops is not ShapeBase.NOT_SET:
                _params['iops'] = iops
            _request = shapes.ModifyVolumeRequest(**_params)
        response = self._boto_client.modify_volume(**_request.to_boto())

        return shapes.ModifyVolumeResult.from_boto(response)

    def modify_volume_attribute(
        self,
        _request: shapes.ModifyVolumeAttributeRequest = None,
        *,
        volume_id: str,
        auto_enable_io: shapes.AttributeBooleanValue = ShapeBase.NOT_SET,
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> None:
        """
        Modifies a volume attribute.

        By default, all I/O operations for the volume are suspended when the data on the
        volume is determined to be potentially inconsistent, to prevent undetectable,
        latent data corruption. The I/O access to the volume can be resumed by first
        enabling I/O access and then checking the data consistency on your volume.

        You can change the default behavior to resume I/O operations. We recommend that
        you change this only for boot volumes or for volumes that are stateless or
        disposable.
        """
        if _request is None:
            _params = {}
            if volume_id is not ShapeBase.NOT_SET:
                _params['volume_id'] = volume_id
            if auto_enable_io is not ShapeBase.NOT_SET:
                _params['auto_enable_io'] = auto_enable_io
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.ModifyVolumeAttributeRequest(**_params)
        response = self._boto_client.modify_volume_attribute(
            **_request.to_boto()
        )

    def modify_vpc_attribute(
        self,
        _request: shapes.ModifyVpcAttributeRequest = None,
        *,
        vpc_id: str,
        enable_dns_hostnames: shapes.AttributeBooleanValue = ShapeBase.NOT_SET,
        enable_dns_support: shapes.AttributeBooleanValue = ShapeBase.NOT_SET,
    ) -> None:
        """
        Modifies the specified attribute of the specified VPC.
        """
        if _request is None:
            _params = {}
            if vpc_id is not ShapeBase.NOT_SET:
                _params['vpc_id'] = vpc_id
            if enable_dns_hostnames is not ShapeBase.NOT_SET:
                _params['enable_dns_hostnames'] = enable_dns_hostnames
            if enable_dns_support is not ShapeBase.NOT_SET:
                _params['enable_dns_support'] = enable_dns_support
            _request = shapes.ModifyVpcAttributeRequest(**_params)
        response = self._boto_client.modify_vpc_attribute(**_request.to_boto())

    def modify_vpc_endpoint(
        self,
        _request: shapes.ModifyVpcEndpointRequest = None,
        *,
        vpc_endpoint_id: str,
        dry_run: bool = ShapeBase.NOT_SET,
        reset_policy: bool = ShapeBase.NOT_SET,
        policy_document: str = ShapeBase.NOT_SET,
        add_route_table_ids: typing.List[str] = ShapeBase.NOT_SET,
        remove_route_table_ids: typing.List[str] = ShapeBase.NOT_SET,
        add_subnet_ids: typing.List[str] = ShapeBase.NOT_SET,
        remove_subnet_ids: typing.List[str] = ShapeBase.NOT_SET,
        add_security_group_ids: typing.List[str] = ShapeBase.NOT_SET,
        remove_security_group_ids: typing.List[str] = ShapeBase.NOT_SET,
        private_dns_enabled: bool = ShapeBase.NOT_SET,
    ) -> shapes.ModifyVpcEndpointResult:
        """
        Modifies attributes of a specified VPC endpoint. The attributes that you can
        modify depend on the type of VPC endpoint (interface or gateway). For more
        information, see [VPC
        Endpoints](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/vpc-
        endpoints.html) in the _Amazon Virtual Private Cloud User Guide_.
        """
        if _request is None:
            _params = {}
            if vpc_endpoint_id is not ShapeBase.NOT_SET:
                _params['vpc_endpoint_id'] = vpc_endpoint_id
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            if reset_policy is not ShapeBase.NOT_SET:
                _params['reset_policy'] = reset_policy
            if policy_document is not ShapeBase.NOT_SET:
                _params['policy_document'] = policy_document
            if add_route_table_ids is not ShapeBase.NOT_SET:
                _params['add_route_table_ids'] = add_route_table_ids
            if remove_route_table_ids is not ShapeBase.NOT_SET:
                _params['remove_route_table_ids'] = remove_route_table_ids
            if add_subnet_ids is not ShapeBase.NOT_SET:
                _params['add_subnet_ids'] = add_subnet_ids
            if remove_subnet_ids is not ShapeBase.NOT_SET:
                _params['remove_subnet_ids'] = remove_subnet_ids
            if add_security_group_ids is not ShapeBase.NOT_SET:
                _params['add_security_group_ids'] = add_security_group_ids
            if remove_security_group_ids is not ShapeBase.NOT_SET:
                _params['remove_security_group_ids'] = remove_security_group_ids
            if private_dns_enabled is not ShapeBase.NOT_SET:
                _params['private_dns_enabled'] = private_dns_enabled
            _request = shapes.ModifyVpcEndpointRequest(**_params)
        response = self._boto_client.modify_vpc_endpoint(**_request.to_boto())

        return shapes.ModifyVpcEndpointResult.from_boto(response)

    def modify_vpc_endpoint_connection_notification(
        self,
        _request: shapes.ModifyVpcEndpointConnectionNotificationRequest = None,
        *,
        connection_notification_id: str,
        dry_run: bool = ShapeBase.NOT_SET,
        connection_notification_arn: str = ShapeBase.NOT_SET,
        connection_events: typing.List[str] = ShapeBase.NOT_SET,
    ) -> shapes.ModifyVpcEndpointConnectionNotificationResult:
        """
        Modifies a connection notification for VPC endpoint or VPC endpoint service. You
        can change the SNS topic for the notification, or the events for which to be
        notified.
        """
        if _request is None:
            _params = {}
            if connection_notification_id is not ShapeBase.NOT_SET:
                _params['connection_notification_id'
                       ] = connection_notification_id
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            if connection_notification_arn is not ShapeBase.NOT_SET:
                _params['connection_notification_arn'
                       ] = connection_notification_arn
            if connection_events is not ShapeBase.NOT_SET:
                _params['connection_events'] = connection_events
            _request = shapes.ModifyVpcEndpointConnectionNotificationRequest(
                **_params
            )
        response = self._boto_client.modify_vpc_endpoint_connection_notification(
            **_request.to_boto()
        )

        return shapes.ModifyVpcEndpointConnectionNotificationResult.from_boto(
            response
        )

    def modify_vpc_endpoint_service_configuration(
        self,
        _request: shapes.ModifyVpcEndpointServiceConfigurationRequest = None,
        *,
        service_id: str,
        dry_run: bool = ShapeBase.NOT_SET,
        acceptance_required: bool = ShapeBase.NOT_SET,
        add_network_load_balancer_arns: typing.List[str] = ShapeBase.NOT_SET,
        remove_network_load_balancer_arns: typing.List[str] = ShapeBase.NOT_SET,
    ) -> shapes.ModifyVpcEndpointServiceConfigurationResult:
        """
        Modifies the attributes of your VPC endpoint service configuration. You can
        change the Network Load Balancers for your service, and you can specify whether
        acceptance is required for requests to connect to your endpoint service through
        an interface VPC endpoint.
        """
        if _request is None:
            _params = {}
            if service_id is not ShapeBase.NOT_SET:
                _params['service_id'] = service_id
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            if acceptance_required is not ShapeBase.NOT_SET:
                _params['acceptance_required'] = acceptance_required
            if add_network_load_balancer_arns is not ShapeBase.NOT_SET:
                _params['add_network_load_balancer_arns'
                       ] = add_network_load_balancer_arns
            if remove_network_load_balancer_arns is not ShapeBase.NOT_SET:
                _params['remove_network_load_balancer_arns'
                       ] = remove_network_load_balancer_arns
            _request = shapes.ModifyVpcEndpointServiceConfigurationRequest(
                **_params
            )
        response = self._boto_client.modify_vpc_endpoint_service_configuration(
            **_request.to_boto()
        )

        return shapes.ModifyVpcEndpointServiceConfigurationResult.from_boto(
            response
        )

    def modify_vpc_endpoint_service_permissions(
        self,
        _request: shapes.ModifyVpcEndpointServicePermissionsRequest = None,
        *,
        service_id: str,
        dry_run: bool = ShapeBase.NOT_SET,
        add_allowed_principals: typing.List[str] = ShapeBase.NOT_SET,
        remove_allowed_principals: typing.List[str] = ShapeBase.NOT_SET,
    ) -> shapes.ModifyVpcEndpointServicePermissionsResult:
        """
        Modifies the permissions for your [VPC endpoint
        service](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/endpoint-
        service.html). You can add or remove permissions for service consumers (IAM
        users, IAM roles, and AWS accounts) to connect to your endpoint service.

        If you grant permissions to all principals, the service is public. Any users who
        know the name of a public service can send a request to attach an endpoint. If
        the service does not require manual approval, attachments are automatically
        approved.
        """
        if _request is None:
            _params = {}
            if service_id is not ShapeBase.NOT_SET:
                _params['service_id'] = service_id
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            if add_allowed_principals is not ShapeBase.NOT_SET:
                _params['add_allowed_principals'] = add_allowed_principals
            if remove_allowed_principals is not ShapeBase.NOT_SET:
                _params['remove_allowed_principals'] = remove_allowed_principals
            _request = shapes.ModifyVpcEndpointServicePermissionsRequest(
                **_params
            )
        response = self._boto_client.modify_vpc_endpoint_service_permissions(
            **_request.to_boto()
        )

        return shapes.ModifyVpcEndpointServicePermissionsResult.from_boto(
            response
        )

    def modify_vpc_peering_connection_options(
        self,
        _request: shapes.ModifyVpcPeeringConnectionOptionsRequest = None,
        *,
        vpc_peering_connection_id: str,
        accepter_peering_connection_options: shapes.
        PeeringConnectionOptionsRequest = ShapeBase.NOT_SET,
        dry_run: bool = ShapeBase.NOT_SET,
        requester_peering_connection_options: shapes.
        PeeringConnectionOptionsRequest = ShapeBase.NOT_SET,
    ) -> shapes.ModifyVpcPeeringConnectionOptionsResult:
        """
        Modifies the VPC peering connection options on one side of a VPC peering
        connection. You can do the following:

          * Enable/disable communication over the peering connection between an EC2-Classic instance that's linked to your VPC (using ClassicLink) and instances in the peer VPC.

          * Enable/disable communication over the peering connection between instances in your VPC and an EC2-Classic instance that's linked to the peer VPC.

          * Enable/disable the ability to resolve public DNS hostnames to private IP addresses when queried from instances in the peer VPC.

        If the peered VPCs are in different accounts, each owner must initiate a
        separate request to modify the peering connection options, depending on whether
        their VPC was the requester or accepter for the VPC peering connection. If the
        peered VPCs are in the same account, you can modify the requester and accepter
        options in the same request. To confirm which VPC is the accepter and requester
        for a VPC peering connection, use the DescribeVpcPeeringConnections command.
        """
        if _request is None:
            _params = {}
            if vpc_peering_connection_id is not ShapeBase.NOT_SET:
                _params['vpc_peering_connection_id'] = vpc_peering_connection_id
            if accepter_peering_connection_options is not ShapeBase.NOT_SET:
                _params['accepter_peering_connection_options'
                       ] = accepter_peering_connection_options
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            if requester_peering_connection_options is not ShapeBase.NOT_SET:
                _params['requester_peering_connection_options'
                       ] = requester_peering_connection_options
            _request = shapes.ModifyVpcPeeringConnectionOptionsRequest(
                **_params
            )
        response = self._boto_client.modify_vpc_peering_connection_options(
            **_request.to_boto()
        )

        return shapes.ModifyVpcPeeringConnectionOptionsResult.from_boto(
            response
        )

    def modify_vpc_tenancy(
        self,
        _request: shapes.ModifyVpcTenancyRequest = None,
        *,
        vpc_id: str,
        instance_tenancy: typing.Union[str, shapes.VpcTenancy],
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> shapes.ModifyVpcTenancyResult:
        """
        Modifies the instance tenancy attribute of the specified VPC. You can change the
        instance tenancy attribute of a VPC to `default` only. You cannot change the
        instance tenancy attribute to `dedicated`.

        After you modify the tenancy of the VPC, any new instances that you launch into
        the VPC have a tenancy of `default`, unless you specify otherwise during launch.
        The tenancy of any existing instances in the VPC is not affected.

        For more information, see [Dedicated
        Instances](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/dedicated-
        instance.html) in the _Amazon Elastic Compute Cloud User Guide_.
        """
        if _request is None:
            _params = {}
            if vpc_id is not ShapeBase.NOT_SET:
                _params['vpc_id'] = vpc_id
            if instance_tenancy is not ShapeBase.NOT_SET:
                _params['instance_tenancy'] = instance_tenancy
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.ModifyVpcTenancyRequest(**_params)
        response = self._boto_client.modify_vpc_tenancy(**_request.to_boto())

        return shapes.ModifyVpcTenancyResult.from_boto(response)

    def monitor_instances(
        self,
        _request: shapes.MonitorInstancesRequest = None,
        *,
        instance_ids: typing.List[str],
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> shapes.MonitorInstancesResult:
        """
        Enables detailed monitoring for a running instance. Otherwise, basic monitoring
        is enabled. For more information, see [Monitoring Your Instances and
        Volumes](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-
        cloudwatch.html) in the _Amazon Elastic Compute Cloud User Guide_.

        To disable detailed monitoring, see .
        """
        if _request is None:
            _params = {}
            if instance_ids is not ShapeBase.NOT_SET:
                _params['instance_ids'] = instance_ids
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.MonitorInstancesRequest(**_params)
        response = self._boto_client.monitor_instances(**_request.to_boto())

        return shapes.MonitorInstancesResult.from_boto(response)

    def move_address_to_vpc(
        self,
        _request: shapes.MoveAddressToVpcRequest = None,
        *,
        public_ip: str,
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> shapes.MoveAddressToVpcResult:
        """
        Moves an Elastic IP address from the EC2-Classic platform to the EC2-VPC
        platform. The Elastic IP address must be allocated to your account for more than
        24 hours, and it must not be associated with an instance. After the Elastic IP
        address is moved, it is no longer available for use in the EC2-Classic platform,
        unless you move it back using the RestoreAddressToClassic request. You cannot
        move an Elastic IP address that was originally allocated for use in the EC2-VPC
        platform to the EC2-Classic platform.
        """
        if _request is None:
            _params = {}
            if public_ip is not ShapeBase.NOT_SET:
                _params['public_ip'] = public_ip
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.MoveAddressToVpcRequest(**_params)
        response = self._boto_client.move_address_to_vpc(**_request.to_boto())

        return shapes.MoveAddressToVpcResult.from_boto(response)

    def purchase_host_reservation(
        self,
        _request: shapes.PurchaseHostReservationRequest = None,
        *,
        host_id_set: typing.List[str],
        offering_id: str,
        client_token: str = ShapeBase.NOT_SET,
        currency_code: typing.Union[str, shapes.CurrencyCodeValues] = ShapeBase.
        NOT_SET,
        limit_price: str = ShapeBase.NOT_SET,
    ) -> shapes.PurchaseHostReservationResult:
        """
        Purchase a reservation with configurations that match those of your Dedicated
        Host. You must have active Dedicated Hosts in your account before you purchase a
        reservation. This action results in the specified reservation being purchased
        and charged to your account.
        """
        if _request is None:
            _params = {}
            if host_id_set is not ShapeBase.NOT_SET:
                _params['host_id_set'] = host_id_set
            if offering_id is not ShapeBase.NOT_SET:
                _params['offering_id'] = offering_id
            if client_token is not ShapeBase.NOT_SET:
                _params['client_token'] = client_token
            if currency_code is not ShapeBase.NOT_SET:
                _params['currency_code'] = currency_code
            if limit_price is not ShapeBase.NOT_SET:
                _params['limit_price'] = limit_price
            _request = shapes.PurchaseHostReservationRequest(**_params)
        response = self._boto_client.purchase_host_reservation(
            **_request.to_boto()
        )

        return shapes.PurchaseHostReservationResult.from_boto(response)

    def purchase_reserved_instances_offering(
        self,
        _request: shapes.PurchaseReservedInstancesOfferingRequest = None,
        *,
        instance_count: int,
        reserved_instances_offering_id: str,
        dry_run: bool = ShapeBase.NOT_SET,
        limit_price: shapes.ReservedInstanceLimitPrice = ShapeBase.NOT_SET,
    ) -> shapes.PurchaseReservedInstancesOfferingResult:
        """
        Purchases a Reserved Instance for use with your account. With Reserved
        Instances, you pay a lower hourly rate compared to On-Demand instance pricing.

        Use DescribeReservedInstancesOfferings to get a list of Reserved Instance
        offerings that match your specifications. After you've purchased a Reserved
        Instance, you can check for your new Reserved Instance with
        DescribeReservedInstances.

        For more information, see [Reserved
        Instances](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts-on-
        demand-reserved-instances.html) and [Reserved Instance
        Marketplace](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ri-market-
        general.html) in the _Amazon Elastic Compute Cloud User Guide_.
        """
        if _request is None:
            _params = {}
            if instance_count is not ShapeBase.NOT_SET:
                _params['instance_count'] = instance_count
            if reserved_instances_offering_id is not ShapeBase.NOT_SET:
                _params['reserved_instances_offering_id'
                       ] = reserved_instances_offering_id
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            if limit_price is not ShapeBase.NOT_SET:
                _params['limit_price'] = limit_price
            _request = shapes.PurchaseReservedInstancesOfferingRequest(
                **_params
            )
        response = self._boto_client.purchase_reserved_instances_offering(
            **_request.to_boto()
        )

        return shapes.PurchaseReservedInstancesOfferingResult.from_boto(
            response
        )

    def purchase_scheduled_instances(
        self,
        _request: shapes.PurchaseScheduledInstancesRequest = None,
        *,
        purchase_requests: typing.List[shapes.PurchaseRequest],
        client_token: str = ShapeBase.NOT_SET,
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> shapes.PurchaseScheduledInstancesResult:
        """
        Purchases one or more Scheduled Instances with the specified schedule.

        Scheduled Instances enable you to purchase Amazon EC2 compute capacity by the
        hour for a one-year term. Before you can purchase a Scheduled Instance, you must
        call DescribeScheduledInstanceAvailability to check for available schedules and
        obtain a purchase token. After you purchase a Scheduled Instance, you must call
        RunScheduledInstances during each scheduled time period.

        After you purchase a Scheduled Instance, you can't cancel, modify, or resell
        your purchase.
        """
        if _request is None:
            _params = {}
            if purchase_requests is not ShapeBase.NOT_SET:
                _params['purchase_requests'] = purchase_requests
            if client_token is not ShapeBase.NOT_SET:
                _params['client_token'] = client_token
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.PurchaseScheduledInstancesRequest(**_params)
        response = self._boto_client.purchase_scheduled_instances(
            **_request.to_boto()
        )

        return shapes.PurchaseScheduledInstancesResult.from_boto(response)

    def reboot_instances(
        self,
        _request: shapes.RebootInstancesRequest = None,
        *,
        instance_ids: typing.List[str],
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> None:
        """
        Requests a reboot of one or more instances. This operation is asynchronous; it
        only queues a request to reboot the specified instances. The operation succeeds
        if the instances are valid and belong to you. Requests to reboot terminated
        instances are ignored.

        If an instance does not cleanly shut down within four minutes, Amazon EC2
        performs a hard reboot.

        For more information about troubleshooting, see [Getting Console Output and
        Rebooting
        Instances](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-
        console.html) in the _Amazon Elastic Compute Cloud User Guide_.
        """
        if _request is None:
            _params = {}
            if instance_ids is not ShapeBase.NOT_SET:
                _params['instance_ids'] = instance_ids
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.RebootInstancesRequest(**_params)
        response = self._boto_client.reboot_instances(**_request.to_boto())

    def register_image(
        self,
        _request: shapes.RegisterImageRequest = None,
        *,
        name: str,
        image_location: str = ShapeBase.NOT_SET,
        architecture: typing.Union[str, shapes.ArchitectureValues] = ShapeBase.
        NOT_SET,
        block_device_mappings: typing.List[shapes.BlockDeviceMapping
                                          ] = ShapeBase.NOT_SET,
        description: str = ShapeBase.NOT_SET,
        dry_run: bool = ShapeBase.NOT_SET,
        ena_support: bool = ShapeBase.NOT_SET,
        kernel_id: str = ShapeBase.NOT_SET,
        billing_products: typing.List[str] = ShapeBase.NOT_SET,
        ramdisk_id: str = ShapeBase.NOT_SET,
        root_device_name: str = ShapeBase.NOT_SET,
        sriov_net_support: str = ShapeBase.NOT_SET,
        virtualization_type: str = ShapeBase.NOT_SET,
    ) -> shapes.RegisterImageResult:
        """
        Registers an AMI. When you're creating an AMI, this is the final step you must
        complete before you can launch an instance from the AMI. For more information
        about creating AMIs, see [Creating Your Own
        AMIs](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/creating-an-ami.html)
        in the _Amazon Elastic Compute Cloud User Guide_.

        For Amazon EBS-backed instances, CreateImage creates and registers the AMI in a
        single request, so you don't have to register the AMI yourself.

        You can also use `RegisterImage` to create an Amazon EBS-backed Linux AMI from a
        snapshot of a root device volume. You specify the snapshot using the block
        device mapping. For more information, see [Launching a Linux Instance from a
        Backup](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-launch-
        snapshot.html) in the _Amazon Elastic Compute Cloud User Guide_.

        You can't register an image where a secondary (non-root) snapshot has AWS
        Marketplace product codes.

        Some Linux distributions, such as Red Hat Enterprise Linux (RHEL) and SUSE Linux
        Enterprise Server (SLES), use the EC2 billing product code associated with an
        AMI to verify the subscription status for package updates. Creating an AMI from
        an EBS snapshot does not maintain this billing code, and instances launched from
        such an AMI are not able to connect to package update infrastructure. If you
        purchase a Reserved Instance offering for one of these Linux distributions and
        launch instances using an AMI that does not contain the required billing code,
        your Reserved Instance is not applied to these instances.

        To create an AMI for operating systems that require a billing code, see
        CreateImage.

        If needed, you can deregister an AMI at any time. Any modifications you make to
        an AMI backed by an instance store volume invalidates its registration. If you
        make changes to an image, deregister the previous image and register the new
        image.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if image_location is not ShapeBase.NOT_SET:
                _params['image_location'] = image_location
            if architecture is not ShapeBase.NOT_SET:
                _params['architecture'] = architecture
            if block_device_mappings is not ShapeBase.NOT_SET:
                _params['block_device_mappings'] = block_device_mappings
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            if ena_support is not ShapeBase.NOT_SET:
                _params['ena_support'] = ena_support
            if kernel_id is not ShapeBase.NOT_SET:
                _params['kernel_id'] = kernel_id
            if billing_products is not ShapeBase.NOT_SET:
                _params['billing_products'] = billing_products
            if ramdisk_id is not ShapeBase.NOT_SET:
                _params['ramdisk_id'] = ramdisk_id
            if root_device_name is not ShapeBase.NOT_SET:
                _params['root_device_name'] = root_device_name
            if sriov_net_support is not ShapeBase.NOT_SET:
                _params['sriov_net_support'] = sriov_net_support
            if virtualization_type is not ShapeBase.NOT_SET:
                _params['virtualization_type'] = virtualization_type
            _request = shapes.RegisterImageRequest(**_params)
        response = self._boto_client.register_image(**_request.to_boto())

        return shapes.RegisterImageResult.from_boto(response)

    def reject_vpc_endpoint_connections(
        self,
        _request: shapes.RejectVpcEndpointConnectionsRequest = None,
        *,
        service_id: str,
        vpc_endpoint_ids: typing.List[str],
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> shapes.RejectVpcEndpointConnectionsResult:
        """
        Rejects one or more VPC endpoint connection requests to your VPC endpoint
        service.
        """
        if _request is None:
            _params = {}
            if service_id is not ShapeBase.NOT_SET:
                _params['service_id'] = service_id
            if vpc_endpoint_ids is not ShapeBase.NOT_SET:
                _params['vpc_endpoint_ids'] = vpc_endpoint_ids
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.RejectVpcEndpointConnectionsRequest(**_params)
        response = self._boto_client.reject_vpc_endpoint_connections(
            **_request.to_boto()
        )

        return shapes.RejectVpcEndpointConnectionsResult.from_boto(response)

    def reject_vpc_peering_connection(
        self,
        _request: shapes.RejectVpcPeeringConnectionRequest = None,
        *,
        vpc_peering_connection_id: str,
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> shapes.RejectVpcPeeringConnectionResult:
        """
        Rejects a VPC peering connection request. The VPC peering connection must be in
        the `pending-acceptance` state. Use the DescribeVpcPeeringConnections request to
        view your outstanding VPC peering connection requests. To delete an active VPC
        peering connection, or to delete a VPC peering connection request that you
        initiated, use DeleteVpcPeeringConnection.
        """
        if _request is None:
            _params = {}
            if vpc_peering_connection_id is not ShapeBase.NOT_SET:
                _params['vpc_peering_connection_id'] = vpc_peering_connection_id
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.RejectVpcPeeringConnectionRequest(**_params)
        response = self._boto_client.reject_vpc_peering_connection(
            **_request.to_boto()
        )

        return shapes.RejectVpcPeeringConnectionResult.from_boto(response)

    def release_address(
        self,
        _request: shapes.ReleaseAddressRequest = None,
        *,
        allocation_id: str = ShapeBase.NOT_SET,
        public_ip: str = ShapeBase.NOT_SET,
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> None:
        """
        Releases the specified Elastic IP address.

        [EC2-Classic, default VPC] Releasing an Elastic IP address automatically
        disassociates it from any instance that it's associated with. To disassociate an
        Elastic IP address without releasing it, use DisassociateAddress.

        [Nondefault VPC] You must use DisassociateAddress to disassociate the Elastic IP
        address before you can release it. Otherwise, Amazon EC2 returns an error
        (`InvalidIPAddress.InUse`).

        After releasing an Elastic IP address, it is released to the IP address pool. Be
        sure to update your DNS records and any servers or devices that communicate with
        the address. If you attempt to release an Elastic IP address that you already
        released, you'll get an `AuthFailure` error if the address is already allocated
        to another AWS account.

        [EC2-VPC] After you release an Elastic IP address for use in a VPC, you might be
        able to recover it. For more information, see AllocateAddress.
        """
        if _request is None:
            _params = {}
            if allocation_id is not ShapeBase.NOT_SET:
                _params['allocation_id'] = allocation_id
            if public_ip is not ShapeBase.NOT_SET:
                _params['public_ip'] = public_ip
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.ReleaseAddressRequest(**_params)
        response = self._boto_client.release_address(**_request.to_boto())

    def release_hosts(
        self,
        _request: shapes.ReleaseHostsRequest = None,
        *,
        host_ids: typing.List[str],
    ) -> shapes.ReleaseHostsResult:
        """
        When you no longer want to use an On-Demand Dedicated Host it can be released.
        On-Demand billing is stopped and the host goes into `released` state. The host
        ID of Dedicated Hosts that have been released can no longer be specified in
        another request, for example, to modify the host. You must stop or terminate all
        instances on a host before it can be released.

        When Dedicated Hosts are released, it may take some time for them to stop
        counting toward your limit and you may receive capacity errors when trying to
        allocate new Dedicated Hosts. Wait a few minutes and then try again.

        Released hosts still appear in a DescribeHosts response.
        """
        if _request is None:
            _params = {}
            if host_ids is not ShapeBase.NOT_SET:
                _params['host_ids'] = host_ids
            _request = shapes.ReleaseHostsRequest(**_params)
        response = self._boto_client.release_hosts(**_request.to_boto())

        return shapes.ReleaseHostsResult.from_boto(response)

    def replace_iam_instance_profile_association(
        self,
        _request: shapes.ReplaceIamInstanceProfileAssociationRequest = None,
        *,
        iam_instance_profile: shapes.IamInstanceProfileSpecification,
        association_id: str,
    ) -> shapes.ReplaceIamInstanceProfileAssociationResult:
        """
        Replaces an IAM instance profile for the specified running instance. You can use
        this action to change the IAM instance profile that's associated with an
        instance without having to disassociate the existing IAM instance profile first.

        Use DescribeIamInstanceProfileAssociations to get the association ID.
        """
        if _request is None:
            _params = {}
            if iam_instance_profile is not ShapeBase.NOT_SET:
                _params['iam_instance_profile'] = iam_instance_profile
            if association_id is not ShapeBase.NOT_SET:
                _params['association_id'] = association_id
            _request = shapes.ReplaceIamInstanceProfileAssociationRequest(
                **_params
            )
        response = self._boto_client.replace_iam_instance_profile_association(
            **_request.to_boto()
        )

        return shapes.ReplaceIamInstanceProfileAssociationResult.from_boto(
            response
        )

    def replace_network_acl_association(
        self,
        _request: shapes.ReplaceNetworkAclAssociationRequest = None,
        *,
        association_id: str,
        network_acl_id: str,
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> shapes.ReplaceNetworkAclAssociationResult:
        """
        Changes which network ACL a subnet is associated with. By default when you
        create a subnet, it's automatically associated with the default network ACL. For
        more information, see [Network
        ACLs](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_ACLs.html) in
        the _Amazon Virtual Private Cloud User Guide_.

        This is an idempotent operation.
        """
        if _request is None:
            _params = {}
            if association_id is not ShapeBase.NOT_SET:
                _params['association_id'] = association_id
            if network_acl_id is not ShapeBase.NOT_SET:
                _params['network_acl_id'] = network_acl_id
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.ReplaceNetworkAclAssociationRequest(**_params)
        response = self._boto_client.replace_network_acl_association(
            **_request.to_boto()
        )

        return shapes.ReplaceNetworkAclAssociationResult.from_boto(response)

    def replace_network_acl_entry(
        self,
        _request: shapes.ReplaceNetworkAclEntryRequest = None,
        *,
        egress: bool,
        network_acl_id: str,
        protocol: str,
        rule_action: typing.Union[str, shapes.RuleAction],
        rule_number: int,
        cidr_block: str = ShapeBase.NOT_SET,
        dry_run: bool = ShapeBase.NOT_SET,
        icmp_type_code: shapes.IcmpTypeCode = ShapeBase.NOT_SET,
        ipv6_cidr_block: str = ShapeBase.NOT_SET,
        port_range: shapes.PortRange = ShapeBase.NOT_SET,
    ) -> None:
        """
        Replaces an entry (rule) in a network ACL. For more information, see [Network
        ACLs](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_ACLs.html) in
        the _Amazon Virtual Private Cloud User Guide_.
        """
        if _request is None:
            _params = {}
            if egress is not ShapeBase.NOT_SET:
                _params['egress'] = egress
            if network_acl_id is not ShapeBase.NOT_SET:
                _params['network_acl_id'] = network_acl_id
            if protocol is not ShapeBase.NOT_SET:
                _params['protocol'] = protocol
            if rule_action is not ShapeBase.NOT_SET:
                _params['rule_action'] = rule_action
            if rule_number is not ShapeBase.NOT_SET:
                _params['rule_number'] = rule_number
            if cidr_block is not ShapeBase.NOT_SET:
                _params['cidr_block'] = cidr_block
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            if icmp_type_code is not ShapeBase.NOT_SET:
                _params['icmp_type_code'] = icmp_type_code
            if ipv6_cidr_block is not ShapeBase.NOT_SET:
                _params['ipv6_cidr_block'] = ipv6_cidr_block
            if port_range is not ShapeBase.NOT_SET:
                _params['port_range'] = port_range
            _request = shapes.ReplaceNetworkAclEntryRequest(**_params)
        response = self._boto_client.replace_network_acl_entry(
            **_request.to_boto()
        )

    def replace_route(
        self,
        _request: shapes.ReplaceRouteRequest = None,
        *,
        route_table_id: str,
        destination_cidr_block: str = ShapeBase.NOT_SET,
        destination_ipv6_cidr_block: str = ShapeBase.NOT_SET,
        dry_run: bool = ShapeBase.NOT_SET,
        egress_only_internet_gateway_id: str = ShapeBase.NOT_SET,
        gateway_id: str = ShapeBase.NOT_SET,
        instance_id: str = ShapeBase.NOT_SET,
        nat_gateway_id: str = ShapeBase.NOT_SET,
        network_interface_id: str = ShapeBase.NOT_SET,
        vpc_peering_connection_id: str = ShapeBase.NOT_SET,
    ) -> None:
        """
        Replaces an existing route within a route table in a VPC. You must provide only
        one of the following: internet gateway or virtual private gateway, NAT instance,
        NAT gateway, VPC peering connection, network interface, or egress-only internet
        gateway.

        For more information, see [Route
        Tables](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Route_Tables.html)
        in the _Amazon Virtual Private Cloud User Guide_.
        """
        if _request is None:
            _params = {}
            if route_table_id is not ShapeBase.NOT_SET:
                _params['route_table_id'] = route_table_id
            if destination_cidr_block is not ShapeBase.NOT_SET:
                _params['destination_cidr_block'] = destination_cidr_block
            if destination_ipv6_cidr_block is not ShapeBase.NOT_SET:
                _params['destination_ipv6_cidr_block'
                       ] = destination_ipv6_cidr_block
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            if egress_only_internet_gateway_id is not ShapeBase.NOT_SET:
                _params['egress_only_internet_gateway_id'
                       ] = egress_only_internet_gateway_id
            if gateway_id is not ShapeBase.NOT_SET:
                _params['gateway_id'] = gateway_id
            if instance_id is not ShapeBase.NOT_SET:
                _params['instance_id'] = instance_id
            if nat_gateway_id is not ShapeBase.NOT_SET:
                _params['nat_gateway_id'] = nat_gateway_id
            if network_interface_id is not ShapeBase.NOT_SET:
                _params['network_interface_id'] = network_interface_id
            if vpc_peering_connection_id is not ShapeBase.NOT_SET:
                _params['vpc_peering_connection_id'] = vpc_peering_connection_id
            _request = shapes.ReplaceRouteRequest(**_params)
        response = self._boto_client.replace_route(**_request.to_boto())

    def replace_route_table_association(
        self,
        _request: shapes.ReplaceRouteTableAssociationRequest = None,
        *,
        association_id: str,
        route_table_id: str,
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> shapes.ReplaceRouteTableAssociationResult:
        """
        Changes the route table associated with a given subnet in a VPC. After the
        operation completes, the subnet uses the routes in the new route table it's
        associated with. For more information about route tables, see [Route
        Tables](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Route_Tables.html)
        in the _Amazon Virtual Private Cloud User Guide_.

        You can also use ReplaceRouteTableAssociation to change which table is the main
        route table in the VPC. You just specify the main route table's association ID
        and the route table to be the new main route table.
        """
        if _request is None:
            _params = {}
            if association_id is not ShapeBase.NOT_SET:
                _params['association_id'] = association_id
            if route_table_id is not ShapeBase.NOT_SET:
                _params['route_table_id'] = route_table_id
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.ReplaceRouteTableAssociationRequest(**_params)
        response = self._boto_client.replace_route_table_association(
            **_request.to_boto()
        )

        return shapes.ReplaceRouteTableAssociationResult.from_boto(response)

    def report_instance_status(
        self,
        _request: shapes.ReportInstanceStatusRequest = None,
        *,
        instances: typing.List[str],
        reason_codes: typing.List[typing.Union[str, shapes.
                                               ReportInstanceReasonCodes]],
        status: typing.Union[str, shapes.ReportStatusType],
        description: str = ShapeBase.NOT_SET,
        dry_run: bool = ShapeBase.NOT_SET,
        end_time: datetime.datetime = ShapeBase.NOT_SET,
        start_time: datetime.datetime = ShapeBase.NOT_SET,
    ) -> None:
        """
        Submits feedback about the status of an instance. The instance must be in the
        `running` state. If your experience with the instance differs from the instance
        status returned by DescribeInstanceStatus, use ReportInstanceStatus to report
        your experience with the instance. Amazon EC2 collects this information to
        improve the accuracy of status checks.

        Use of this action does not change the value returned by DescribeInstanceStatus.
        """
        if _request is None:
            _params = {}
            if instances is not ShapeBase.NOT_SET:
                _params['instances'] = instances
            if reason_codes is not ShapeBase.NOT_SET:
                _params['reason_codes'] = reason_codes
            if status is not ShapeBase.NOT_SET:
                _params['status'] = status
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            if end_time is not ShapeBase.NOT_SET:
                _params['end_time'] = end_time
            if start_time is not ShapeBase.NOT_SET:
                _params['start_time'] = start_time
            _request = shapes.ReportInstanceStatusRequest(**_params)
        response = self._boto_client.report_instance_status(
            **_request.to_boto()
        )

    def request_spot_fleet(
        self,
        _request: shapes.RequestSpotFleetRequest = None,
        *,
        spot_fleet_request_config: shapes.SpotFleetRequestConfigData,
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> shapes.RequestSpotFleetResponse:
        """
        Creates a Spot Fleet request.

        The Spot Fleet request specifies the total target capacity and the On-Demand
        target capacity. Amazon EC2 calculates the difference between the total capacity
        and On-Demand capacity, and launches the difference as Spot capacity.

        You can submit a single request that includes multiple launch specifications
        that vary by instance type, AMI, Availability Zone, or subnet.

        By default, the Spot Fleet requests Spot Instances in the Spot pool where the
        price per unit is the lowest. Each launch specification can include its own
        instance weighting that reflects the value of the instance type to your
        application workload.

        Alternatively, you can specify that the Spot Fleet distribute the target
        capacity across the Spot pools included in its launch specifications. By
        ensuring that the Spot Instances in your Spot Fleet are in different Spot pools,
        you can improve the availability of your fleet.

        You can specify tags for the Spot Instances. You cannot tag other resource types
        in a Spot Fleet request because only the `instance` resource type is supported.

        For more information, see [Spot Fleet
        Requests](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-fleet-
        requests.html) in the _Amazon EC2 User Guide for Linux Instances_.
        """
        if _request is None:
            _params = {}
            if spot_fleet_request_config is not ShapeBase.NOT_SET:
                _params['spot_fleet_request_config'] = spot_fleet_request_config
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.RequestSpotFleetRequest(**_params)
        response = self._boto_client.request_spot_fleet(**_request.to_boto())

        return shapes.RequestSpotFleetResponse.from_boto(response)

    def request_spot_instances(
        self,
        _request: shapes.RequestSpotInstancesRequest = None,
        *,
        availability_zone_group: str = ShapeBase.NOT_SET,
        block_duration_minutes: int = ShapeBase.NOT_SET,
        client_token: str = ShapeBase.NOT_SET,
        dry_run: bool = ShapeBase.NOT_SET,
        instance_count: int = ShapeBase.NOT_SET,
        launch_group: str = ShapeBase.NOT_SET,
        launch_specification: shapes.RequestSpotLaunchSpecification = ShapeBase.
        NOT_SET,
        spot_price: str = ShapeBase.NOT_SET,
        type: typing.Union[str, shapes.SpotInstanceType] = ShapeBase.NOT_SET,
        valid_from: datetime.datetime = ShapeBase.NOT_SET,
        valid_until: datetime.datetime = ShapeBase.NOT_SET,
        instance_interruption_behavior: typing.
        Union[str, shapes.InstanceInterruptionBehavior] = ShapeBase.NOT_SET,
    ) -> shapes.RequestSpotInstancesResult:
        """
        Creates a Spot Instance request.

        For more information, see [Spot Instance
        Requests](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-requests.html)
        in the _Amazon EC2 User Guide for Linux Instances_.
        """
        if _request is None:
            _params = {}
            if availability_zone_group is not ShapeBase.NOT_SET:
                _params['availability_zone_group'] = availability_zone_group
            if block_duration_minutes is not ShapeBase.NOT_SET:
                _params['block_duration_minutes'] = block_duration_minutes
            if client_token is not ShapeBase.NOT_SET:
                _params['client_token'] = client_token
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            if instance_count is not ShapeBase.NOT_SET:
                _params['instance_count'] = instance_count
            if launch_group is not ShapeBase.NOT_SET:
                _params['launch_group'] = launch_group
            if launch_specification is not ShapeBase.NOT_SET:
                _params['launch_specification'] = launch_specification
            if spot_price is not ShapeBase.NOT_SET:
                _params['spot_price'] = spot_price
            if type is not ShapeBase.NOT_SET:
                _params['type'] = type
            if valid_from is not ShapeBase.NOT_SET:
                _params['valid_from'] = valid_from
            if valid_until is not ShapeBase.NOT_SET:
                _params['valid_until'] = valid_until
            if instance_interruption_behavior is not ShapeBase.NOT_SET:
                _params['instance_interruption_behavior'
                       ] = instance_interruption_behavior
            _request = shapes.RequestSpotInstancesRequest(**_params)
        response = self._boto_client.request_spot_instances(
            **_request.to_boto()
        )

        return shapes.RequestSpotInstancesResult.from_boto(response)

    def reset_fpga_image_attribute(
        self,
        _request: shapes.ResetFpgaImageAttributeRequest = None,
        *,
        fpga_image_id: str,
        dry_run: bool = ShapeBase.NOT_SET,
        attribute: typing.
        Union[str, shapes.ResetFpgaImageAttributeName] = ShapeBase.NOT_SET,
    ) -> shapes.ResetFpgaImageAttributeResult:
        """
        Resets the specified attribute of the specified Amazon FPGA Image (AFI) to its
        default value. You can only reset the load permission attribute.
        """
        if _request is None:
            _params = {}
            if fpga_image_id is not ShapeBase.NOT_SET:
                _params['fpga_image_id'] = fpga_image_id
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            if attribute is not ShapeBase.NOT_SET:
                _params['attribute'] = attribute
            _request = shapes.ResetFpgaImageAttributeRequest(**_params)
        response = self._boto_client.reset_fpga_image_attribute(
            **_request.to_boto()
        )

        return shapes.ResetFpgaImageAttributeResult.from_boto(response)

    def reset_image_attribute(
        self,
        _request: shapes.ResetImageAttributeRequest = None,
        *,
        attribute: typing.Union[str, shapes.ResetImageAttributeName],
        image_id: str,
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> None:
        """
        Resets an attribute of an AMI to its default value.

        The productCodes attribute can't be reset.
        """
        if _request is None:
            _params = {}
            if attribute is not ShapeBase.NOT_SET:
                _params['attribute'] = attribute
            if image_id is not ShapeBase.NOT_SET:
                _params['image_id'] = image_id
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.ResetImageAttributeRequest(**_params)
        response = self._boto_client.reset_image_attribute(**_request.to_boto())

    def reset_instance_attribute(
        self,
        _request: shapes.ResetInstanceAttributeRequest = None,
        *,
        attribute: typing.Union[str, shapes.InstanceAttributeName],
        instance_id: str,
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> None:
        """
        Resets an attribute of an instance to its default value. To reset the `kernel`
        or `ramdisk`, the instance must be in a stopped state. To reset the
        `sourceDestCheck`, the instance can be either running or stopped.

        The `sourceDestCheck` attribute controls whether source/destination checking is
        enabled. The default value is `true`, which means checking is enabled. This
        value must be `false` for a NAT instance to perform NAT. For more information,
        see [NAT
        Instances](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_NAT_Instance.html)
        in the _Amazon Virtual Private Cloud User Guide_.
        """
        if _request is None:
            _params = {}
            if attribute is not ShapeBase.NOT_SET:
                _params['attribute'] = attribute
            if instance_id is not ShapeBase.NOT_SET:
                _params['instance_id'] = instance_id
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.ResetInstanceAttributeRequest(**_params)
        response = self._boto_client.reset_instance_attribute(
            **_request.to_boto()
        )

    def reset_network_interface_attribute(
        self,
        _request: shapes.ResetNetworkInterfaceAttributeRequest = None,
        *,
        network_interface_id: str,
        dry_run: bool = ShapeBase.NOT_SET,
        source_dest_check: str = ShapeBase.NOT_SET,
    ) -> None:
        """
        Resets a network interface attribute. You can specify only one attribute at a
        time.
        """
        if _request is None:
            _params = {}
            if network_interface_id is not ShapeBase.NOT_SET:
                _params['network_interface_id'] = network_interface_id
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            if source_dest_check is not ShapeBase.NOT_SET:
                _params['source_dest_check'] = source_dest_check
            _request = shapes.ResetNetworkInterfaceAttributeRequest(**_params)
        response = self._boto_client.reset_network_interface_attribute(
            **_request.to_boto()
        )

    def reset_snapshot_attribute(
        self,
        _request: shapes.ResetSnapshotAttributeRequest = None,
        *,
        attribute: typing.Union[str, shapes.SnapshotAttributeName],
        snapshot_id: str,
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> None:
        """
        Resets permission settings for the specified snapshot.

        For more information about modifying snapshot permissions, see [Sharing
        Snapshots](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-modifying-
        snapshot-permissions.html) in the _Amazon Elastic Compute Cloud User Guide_.
        """
        if _request is None:
            _params = {}
            if attribute is not ShapeBase.NOT_SET:
                _params['attribute'] = attribute
            if snapshot_id is not ShapeBase.NOT_SET:
                _params['snapshot_id'] = snapshot_id
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.ResetSnapshotAttributeRequest(**_params)
        response = self._boto_client.reset_snapshot_attribute(
            **_request.to_boto()
        )

    def restore_address_to_classic(
        self,
        _request: shapes.RestoreAddressToClassicRequest = None,
        *,
        public_ip: str,
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> shapes.RestoreAddressToClassicResult:
        """
        Restores an Elastic IP address that was previously moved to the EC2-VPC platform
        back to the EC2-Classic platform. You cannot move an Elastic IP address that was
        originally allocated for use in EC2-VPC. The Elastic IP address must not be
        associated with an instance or network interface.
        """
        if _request is None:
            _params = {}
            if public_ip is not ShapeBase.NOT_SET:
                _params['public_ip'] = public_ip
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.RestoreAddressToClassicRequest(**_params)
        response = self._boto_client.restore_address_to_classic(
            **_request.to_boto()
        )

        return shapes.RestoreAddressToClassicResult.from_boto(response)

    def revoke_security_group_egress(
        self,
        _request: shapes.RevokeSecurityGroupEgressRequest = None,
        *,
        group_id: str,
        dry_run: bool = ShapeBase.NOT_SET,
        ip_permissions: typing.List[shapes.IpPermission] = ShapeBase.NOT_SET,
        cidr_ip: str = ShapeBase.NOT_SET,
        from_port: int = ShapeBase.NOT_SET,
        ip_protocol: str = ShapeBase.NOT_SET,
        to_port: int = ShapeBase.NOT_SET,
        source_security_group_name: str = ShapeBase.NOT_SET,
        source_security_group_owner_id: str = ShapeBase.NOT_SET,
    ) -> None:
        """
        [EC2-VPC only] Removes one or more egress rules from a security group for
        EC2-VPC. This action doesn't apply to security groups for use in EC2-Classic. To
        remove a rule, the values that you specify (for example, ports) must match the
        existing rule's values exactly.

        Each rule consists of the protocol and the IPv4 or IPv6 CIDR range or source
        security group. For the TCP and UDP protocols, you must also specify the
        destination port or range of ports. For the ICMP protocol, you must also specify
        the ICMP type and code. If the security group rule has a description, you do not
        have to specify the description to revoke the rule.

        Rule changes are propagated to instances within the security group as quickly as
        possible. However, a small delay might occur.
        """
        if _request is None:
            _params = {}
            if group_id is not ShapeBase.NOT_SET:
                _params['group_id'] = group_id
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            if ip_permissions is not ShapeBase.NOT_SET:
                _params['ip_permissions'] = ip_permissions
            if cidr_ip is not ShapeBase.NOT_SET:
                _params['cidr_ip'] = cidr_ip
            if from_port is not ShapeBase.NOT_SET:
                _params['from_port'] = from_port
            if ip_protocol is not ShapeBase.NOT_SET:
                _params['ip_protocol'] = ip_protocol
            if to_port is not ShapeBase.NOT_SET:
                _params['to_port'] = to_port
            if source_security_group_name is not ShapeBase.NOT_SET:
                _params['source_security_group_name'
                       ] = source_security_group_name
            if source_security_group_owner_id is not ShapeBase.NOT_SET:
                _params['source_security_group_owner_id'
                       ] = source_security_group_owner_id
            _request = shapes.RevokeSecurityGroupEgressRequest(**_params)
        response = self._boto_client.revoke_security_group_egress(
            **_request.to_boto()
        )

    def revoke_security_group_ingress(
        self,
        _request: shapes.RevokeSecurityGroupIngressRequest = None,
        *,
        cidr_ip: str = ShapeBase.NOT_SET,
        from_port: int = ShapeBase.NOT_SET,
        group_id: str = ShapeBase.NOT_SET,
        group_name: str = ShapeBase.NOT_SET,
        ip_permissions: typing.List[shapes.IpPermission] = ShapeBase.NOT_SET,
        ip_protocol: str = ShapeBase.NOT_SET,
        source_security_group_name: str = ShapeBase.NOT_SET,
        source_security_group_owner_id: str = ShapeBase.NOT_SET,
        to_port: int = ShapeBase.NOT_SET,
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> None:
        """
        Removes one or more ingress rules from a security group. To remove a rule, the
        values that you specify (for example, ports) must match the existing rule's
        values exactly.

        [EC2-Classic security groups only] If the values you specify do not match the
        existing rule's values, no error is returned. Use DescribeSecurityGroups to
        verify that the rule has been removed.

        Each rule consists of the protocol and the CIDR range or source security group.
        For the TCP and UDP protocols, you must also specify the destination port or
        range of ports. For the ICMP protocol, you must also specify the ICMP type and
        code. If the security group rule has a description, you do not have to specify
        the description to revoke the rule.

        Rule changes are propagated to instances within the security group as quickly as
        possible. However, a small delay might occur.
        """
        if _request is None:
            _params = {}
            if cidr_ip is not ShapeBase.NOT_SET:
                _params['cidr_ip'] = cidr_ip
            if from_port is not ShapeBase.NOT_SET:
                _params['from_port'] = from_port
            if group_id is not ShapeBase.NOT_SET:
                _params['group_id'] = group_id
            if group_name is not ShapeBase.NOT_SET:
                _params['group_name'] = group_name
            if ip_permissions is not ShapeBase.NOT_SET:
                _params['ip_permissions'] = ip_permissions
            if ip_protocol is not ShapeBase.NOT_SET:
                _params['ip_protocol'] = ip_protocol
            if source_security_group_name is not ShapeBase.NOT_SET:
                _params['source_security_group_name'
                       ] = source_security_group_name
            if source_security_group_owner_id is not ShapeBase.NOT_SET:
                _params['source_security_group_owner_id'
                       ] = source_security_group_owner_id
            if to_port is not ShapeBase.NOT_SET:
                _params['to_port'] = to_port
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.RevokeSecurityGroupIngressRequest(**_params)
        response = self._boto_client.revoke_security_group_ingress(
            **_request.to_boto()
        )

    def run_instances(
        self,
        _request: shapes.RunInstancesRequest = None,
        *,
        max_count: int,
        min_count: int,
        block_device_mappings: typing.List[shapes.BlockDeviceMapping
                                          ] = ShapeBase.NOT_SET,
        image_id: str = ShapeBase.NOT_SET,
        instance_type: typing.Union[str, shapes.
                                    InstanceType] = ShapeBase.NOT_SET,
        ipv6_address_count: int = ShapeBase.NOT_SET,
        ipv6_addresses: typing.List[shapes.InstanceIpv6Address
                                   ] = ShapeBase.NOT_SET,
        kernel_id: str = ShapeBase.NOT_SET,
        key_name: str = ShapeBase.NOT_SET,
        monitoring: shapes.RunInstancesMonitoringEnabled = ShapeBase.NOT_SET,
        placement: shapes.Placement = ShapeBase.NOT_SET,
        ramdisk_id: str = ShapeBase.NOT_SET,
        security_group_ids: typing.List[str] = ShapeBase.NOT_SET,
        security_groups: typing.List[str] = ShapeBase.NOT_SET,
        subnet_id: str = ShapeBase.NOT_SET,
        user_data: str = ShapeBase.NOT_SET,
        additional_info: str = ShapeBase.NOT_SET,
        client_token: str = ShapeBase.NOT_SET,
        disable_api_termination: bool = ShapeBase.NOT_SET,
        dry_run: bool = ShapeBase.NOT_SET,
        ebs_optimized: bool = ShapeBase.NOT_SET,
        iam_instance_profile: shapes.
        IamInstanceProfileSpecification = ShapeBase.NOT_SET,
        instance_initiated_shutdown_behavior: typing.
        Union[str, shapes.ShutdownBehavior] = ShapeBase.NOT_SET,
        network_interfaces: typing.List[
            shapes.InstanceNetworkInterfaceSpecification] = ShapeBase.NOT_SET,
        private_ip_address: str = ShapeBase.NOT_SET,
        elastic_gpu_specification: typing.List[shapes.ElasticGpuSpecification
                                              ] = ShapeBase.NOT_SET,
        tag_specifications: typing.List[shapes.TagSpecification
                                       ] = ShapeBase.NOT_SET,
        launch_template: shapes.LaunchTemplateSpecification = ShapeBase.NOT_SET,
        instance_market_options: shapes.
        InstanceMarketOptionsRequest = ShapeBase.NOT_SET,
        credit_specification: shapes.CreditSpecificationRequest = ShapeBase.
        NOT_SET,
        cpu_options: shapes.CpuOptionsRequest = ShapeBase.NOT_SET,
    ) -> shapes.Reservation:
        """
        Launches the specified number of instances using an AMI for which you have
        permissions.

        You can specify a number of options, or leave the default options. The following
        rules apply:

          * [EC2-VPC] If you don't specify a subnet ID, we choose a default subnet from your default VPC for you. If you don't have a default VPC, you must specify a subnet ID in the request.

          * [EC2-Classic] If don't specify an Availability Zone, we choose one for you.

          * Some instance types must be launched into a VPC. If you do not have a default VPC, or if you do not specify a subnet ID, the request fails. For more information, see [Instance Types Available Only in a VPC](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-vpc.html#vpc-only-instance-types).

          * [EC2-VPC] All instances have a network interface with a primary private IPv4 address. If you don't specify this address, we choose one from the IPv4 range of your subnet.

          * Not all instance types support IPv6 addresses. For more information, see [Instance Types](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html).

          * If you don't specify a security group ID, we use the default security group. For more information, see [Security Groups](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-network-security.html).

          * If any of the AMIs have a product code attached for which the user has not subscribed, the request fails.

        You can create a [launch
        template](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-launch-
        templates.html), which is a resource that contains the parameters to launch an
        instance. When you launch an instance using RunInstances, you can specify the
        launch template instead of specifying the launch parameters.

        To ensure faster instance launches, break up large requests into smaller
        batches. For example, create five separate launch requests for 100 instances
        each instead of one launch request for 500 instances.

        An instance is ready for you to use when it's in the `running` state. You can
        check the state of your instance using DescribeInstances. You can tag instances
        and EBS volumes during launch, after launch, or both. For more information, see
        CreateTags and [Tagging Your Amazon EC2
        Resources](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html).

        Linux instances have access to the public key of the key pair at boot. You can
        use this key to provide secure access to the instance. Amazon EC2 public images
        use this feature to provide secure access without passwords. For more
        information, see [Key
        Pairs](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html) in
        the _Amazon Elastic Compute Cloud User Guide_.

        For troubleshooting, see [What To Do If An Instance Immediately
        Terminates](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_InstanceStraightToTerminated.html),
        and [Troubleshooting Connecting to Your
        Instance](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/TroubleshootingInstancesConnecting.html)
        in the _Amazon Elastic Compute Cloud User Guide_.
        """
        if _request is None:
            _params = {}
            if max_count is not ShapeBase.NOT_SET:
                _params['max_count'] = max_count
            if min_count is not ShapeBase.NOT_SET:
                _params['min_count'] = min_count
            if block_device_mappings is not ShapeBase.NOT_SET:
                _params['block_device_mappings'] = block_device_mappings
            if image_id is not ShapeBase.NOT_SET:
                _params['image_id'] = image_id
            if instance_type is not ShapeBase.NOT_SET:
                _params['instance_type'] = instance_type
            if ipv6_address_count is not ShapeBase.NOT_SET:
                _params['ipv6_address_count'] = ipv6_address_count
            if ipv6_addresses is not ShapeBase.NOT_SET:
                _params['ipv6_addresses'] = ipv6_addresses
            if kernel_id is not ShapeBase.NOT_SET:
                _params['kernel_id'] = kernel_id
            if key_name is not ShapeBase.NOT_SET:
                _params['key_name'] = key_name
            if monitoring is not ShapeBase.NOT_SET:
                _params['monitoring'] = monitoring
            if placement is not ShapeBase.NOT_SET:
                _params['placement'] = placement
            if ramdisk_id is not ShapeBase.NOT_SET:
                _params['ramdisk_id'] = ramdisk_id
            if security_group_ids is not ShapeBase.NOT_SET:
                _params['security_group_ids'] = security_group_ids
            if security_groups is not ShapeBase.NOT_SET:
                _params['security_groups'] = security_groups
            if subnet_id is not ShapeBase.NOT_SET:
                _params['subnet_id'] = subnet_id
            if user_data is not ShapeBase.NOT_SET:
                _params['user_data'] = user_data
            if additional_info is not ShapeBase.NOT_SET:
                _params['additional_info'] = additional_info
            if client_token is not ShapeBase.NOT_SET:
                _params['client_token'] = client_token
            if disable_api_termination is not ShapeBase.NOT_SET:
                _params['disable_api_termination'] = disable_api_termination
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            if ebs_optimized is not ShapeBase.NOT_SET:
                _params['ebs_optimized'] = ebs_optimized
            if iam_instance_profile is not ShapeBase.NOT_SET:
                _params['iam_instance_profile'] = iam_instance_profile
            if instance_initiated_shutdown_behavior is not ShapeBase.NOT_SET:
                _params['instance_initiated_shutdown_behavior'
                       ] = instance_initiated_shutdown_behavior
            if network_interfaces is not ShapeBase.NOT_SET:
                _params['network_interfaces'] = network_interfaces
            if private_ip_address is not ShapeBase.NOT_SET:
                _params['private_ip_address'] = private_ip_address
            if elastic_gpu_specification is not ShapeBase.NOT_SET:
                _params['elastic_gpu_specification'] = elastic_gpu_specification
            if tag_specifications is not ShapeBase.NOT_SET:
                _params['tag_specifications'] = tag_specifications
            if launch_template is not ShapeBase.NOT_SET:
                _params['launch_template'] = launch_template
            if instance_market_options is not ShapeBase.NOT_SET:
                _params['instance_market_options'] = instance_market_options
            if credit_specification is not ShapeBase.NOT_SET:
                _params['credit_specification'] = credit_specification
            if cpu_options is not ShapeBase.NOT_SET:
                _params['cpu_options'] = cpu_options
            _request = shapes.RunInstancesRequest(**_params)
        response = self._boto_client.run_instances(**_request.to_boto())

        return shapes.Reservation.from_boto(response)

    def run_scheduled_instances(
        self,
        _request: shapes.RunScheduledInstancesRequest = None,
        *,
        launch_specification: shapes.ScheduledInstancesLaunchSpecification,
        scheduled_instance_id: str,
        client_token: str = ShapeBase.NOT_SET,
        dry_run: bool = ShapeBase.NOT_SET,
        instance_count: int = ShapeBase.NOT_SET,
    ) -> shapes.RunScheduledInstancesResult:
        """
        Launches the specified Scheduled Instances.

        Before you can launch a Scheduled Instance, you must purchase it and obtain an
        identifier using PurchaseScheduledInstances.

        You must launch a Scheduled Instance during its scheduled time period. You can't
        stop or reboot a Scheduled Instance, but you can terminate it as needed. If you
        terminate a Scheduled Instance before the current scheduled time period ends,
        you can launch it again after a few minutes. For more information, see
        [Scheduled
        Instances](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-scheduled-
        instances.html) in the _Amazon Elastic Compute Cloud User Guide_.
        """
        if _request is None:
            _params = {}
            if launch_specification is not ShapeBase.NOT_SET:
                _params['launch_specification'] = launch_specification
            if scheduled_instance_id is not ShapeBase.NOT_SET:
                _params['scheduled_instance_id'] = scheduled_instance_id
            if client_token is not ShapeBase.NOT_SET:
                _params['client_token'] = client_token
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            if instance_count is not ShapeBase.NOT_SET:
                _params['instance_count'] = instance_count
            _request = shapes.RunScheduledInstancesRequest(**_params)
        response = self._boto_client.run_scheduled_instances(
            **_request.to_boto()
        )

        return shapes.RunScheduledInstancesResult.from_boto(response)

    def start_instances(
        self,
        _request: shapes.StartInstancesRequest = None,
        *,
        instance_ids: typing.List[str],
        additional_info: str = ShapeBase.NOT_SET,
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> shapes.StartInstancesResult:
        """
        Starts an Amazon EBS-backed instance that you've previously stopped.

        Instances that use Amazon EBS volumes as their root devices can be quickly
        stopped and started. When an instance is stopped, the compute resources are
        released and you are not billed for instance usage. However, your root partition
        Amazon EBS volume remains and continues to persist your data, and you are
        charged for Amazon EBS volume usage. You can restart your instance at any time.
        Every time you start your Windows instance, Amazon EC2 charges you for a full
        instance hour. If you stop and restart your Windows instance, a new instance
        hour begins and Amazon EC2 charges you for another full instance hour even if
        you are still within the same 60-minute period when it was stopped. Every time
        you start your Linux instance, Amazon EC2 charges a one-minute minimum for
        instance usage, and thereafter charges per second for instance usage.

        Before stopping an instance, make sure it is in a state from which it can be
        restarted. Stopping an instance does not preserve data stored in RAM.

        Performing this operation on an instance that uses an instance store as its root
        device returns an error.

        For more information, see [Stopping
        Instances](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Stop_Start.html)
        in the _Amazon Elastic Compute Cloud User Guide_.
        """
        if _request is None:
            _params = {}
            if instance_ids is not ShapeBase.NOT_SET:
                _params['instance_ids'] = instance_ids
            if additional_info is not ShapeBase.NOT_SET:
                _params['additional_info'] = additional_info
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.StartInstancesRequest(**_params)
        response = self._boto_client.start_instances(**_request.to_boto())

        return shapes.StartInstancesResult.from_boto(response)

    def stop_instances(
        self,
        _request: shapes.StopInstancesRequest = None,
        *,
        instance_ids: typing.List[str],
        dry_run: bool = ShapeBase.NOT_SET,
        force: bool = ShapeBase.NOT_SET,
    ) -> shapes.StopInstancesResult:
        """
        Stops an Amazon EBS-backed instance.

        We don't charge usage for a stopped instance, or data transfer fees; however,
        your root partition Amazon EBS volume remains and continues to persist your
        data, and you are charged for Amazon EBS volume usage. Every time you start your
        Windows instance, Amazon EC2 charges you for a full instance hour. If you stop
        and restart your Windows instance, a new instance hour begins and Amazon EC2
        charges you for another full instance hour even if you are still within the same
        60-minute period when it was stopped. Every time you start your Linux instance,
        Amazon EC2 charges a one-minute minimum for instance usage, and thereafter
        charges per second for instance usage.

        You can't start or stop Spot Instances, and you can't stop instance store-backed
        instances.

        When you stop an instance, we shut it down. You can restart your instance at any
        time. Before stopping an instance, make sure it is in a state from which it can
        be restarted. Stopping an instance does not preserve data stored in RAM.

        Stopping an instance is different to rebooting or terminating it. For example,
        when you stop an instance, the root device and any other devices attached to the
        instance persist. When you terminate an instance, the root device and any other
        devices attached during the instance launch are automatically deleted. For more
        information about the differences between rebooting, stopping, and terminating
        instances, see [Instance
        Lifecycle](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-
        lifecycle.html) in the _Amazon Elastic Compute Cloud User Guide_.

        When you stop an instance, we attempt to shut it down forcibly after a short
        while. If your instance appears stuck in the stopping state after a period of
        time, there may be an issue with the underlying host computer. For more
        information, see [Troubleshooting Stopping Your
        Instance](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/TroubleshootingInstancesStopping.html)
        in the _Amazon Elastic Compute Cloud User Guide_.
        """
        if _request is None:
            _params = {}
            if instance_ids is not ShapeBase.NOT_SET:
                _params['instance_ids'] = instance_ids
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            if force is not ShapeBase.NOT_SET:
                _params['force'] = force
            _request = shapes.StopInstancesRequest(**_params)
        response = self._boto_client.stop_instances(**_request.to_boto())

        return shapes.StopInstancesResult.from_boto(response)

    def terminate_instances(
        self,
        _request: shapes.TerminateInstancesRequest = None,
        *,
        instance_ids: typing.List[str],
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> shapes.TerminateInstancesResult:
        """
        Shuts down one or more instances. This operation is idempotent; if you terminate
        an instance more than once, each call succeeds.

        If you specify multiple instances and the request fails (for example, because of
        a single incorrect instance ID), none of the instances are terminated.

        Terminated instances remain visible after termination (for approximately one
        hour).

        By default, Amazon EC2 deletes all EBS volumes that were attached when the
        instance launched. Volumes attached after instance launch continue running.

        You can stop, start, and terminate EBS-backed instances. You can only terminate
        instance store-backed instances. What happens to an instance differs if you stop
        it or terminate it. For example, when you stop an instance, the root device and
        any other devices attached to the instance persist. When you terminate an
        instance, any attached EBS volumes with the `DeleteOnTermination` block device
        mapping parameter set to `true` are automatically deleted. For more information
        about the differences between stopping and terminating instances, see [Instance
        Lifecycle](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-
        lifecycle.html) in the _Amazon Elastic Compute Cloud User Guide_.

        For more information about troubleshooting, see [Troubleshooting Terminating
        Your
        Instance](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/TroubleshootingInstancesShuttingDown.html)
        in the _Amazon Elastic Compute Cloud User Guide_.
        """
        if _request is None:
            _params = {}
            if instance_ids is not ShapeBase.NOT_SET:
                _params['instance_ids'] = instance_ids
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.TerminateInstancesRequest(**_params)
        response = self._boto_client.terminate_instances(**_request.to_boto())

        return shapes.TerminateInstancesResult.from_boto(response)

    def unassign_ipv6_addresses(
        self,
        _request: shapes.UnassignIpv6AddressesRequest = None,
        *,
        ipv6_addresses: typing.List[str],
        network_interface_id: str,
    ) -> shapes.UnassignIpv6AddressesResult:
        """
        Unassigns one or more IPv6 addresses from a network interface.
        """
        if _request is None:
            _params = {}
            if ipv6_addresses is not ShapeBase.NOT_SET:
                _params['ipv6_addresses'] = ipv6_addresses
            if network_interface_id is not ShapeBase.NOT_SET:
                _params['network_interface_id'] = network_interface_id
            _request = shapes.UnassignIpv6AddressesRequest(**_params)
        response = self._boto_client.unassign_ipv6_addresses(
            **_request.to_boto()
        )

        return shapes.UnassignIpv6AddressesResult.from_boto(response)

    def unassign_private_ip_addresses(
        self,
        _request: shapes.UnassignPrivateIpAddressesRequest = None,
        *,
        network_interface_id: str,
        private_ip_addresses: typing.List[str],
    ) -> None:
        """
        Unassigns one or more secondary private IP addresses from a network interface.
        """
        if _request is None:
            _params = {}
            if network_interface_id is not ShapeBase.NOT_SET:
                _params['network_interface_id'] = network_interface_id
            if private_ip_addresses is not ShapeBase.NOT_SET:
                _params['private_ip_addresses'] = private_ip_addresses
            _request = shapes.UnassignPrivateIpAddressesRequest(**_params)
        response = self._boto_client.unassign_private_ip_addresses(
            **_request.to_boto()
        )

    def unmonitor_instances(
        self,
        _request: shapes.UnmonitorInstancesRequest = None,
        *,
        instance_ids: typing.List[str],
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> shapes.UnmonitorInstancesResult:
        """
        Disables detailed monitoring for a running instance. For more information, see
        [Monitoring Your Instances and
        Volumes](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-
        cloudwatch.html) in the _Amazon Elastic Compute Cloud User Guide_.
        """
        if _request is None:
            _params = {}
            if instance_ids is not ShapeBase.NOT_SET:
                _params['instance_ids'] = instance_ids
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.UnmonitorInstancesRequest(**_params)
        response = self._boto_client.unmonitor_instances(**_request.to_boto())

        return shapes.UnmonitorInstancesResult.from_boto(response)

    def update_security_group_rule_descriptions_egress(
        self,
        _request: shapes.
        UpdateSecurityGroupRuleDescriptionsEgressRequest = None,
        *,
        ip_permissions: typing.List[shapes.IpPermission],
        dry_run: bool = ShapeBase.NOT_SET,
        group_id: str = ShapeBase.NOT_SET,
        group_name: str = ShapeBase.NOT_SET,
    ) -> shapes.UpdateSecurityGroupRuleDescriptionsEgressResult:
        """
        [EC2-VPC only] Updates the description of an egress (outbound) security group
        rule. You can replace an existing description, or add a description to a rule
        that did not have one previously.

        You specify the description as part of the IP permissions structure. You can
        remove a description for a security group rule by omitting the description
        parameter in the request.
        """
        if _request is None:
            _params = {}
            if ip_permissions is not ShapeBase.NOT_SET:
                _params['ip_permissions'] = ip_permissions
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            if group_id is not ShapeBase.NOT_SET:
                _params['group_id'] = group_id
            if group_name is not ShapeBase.NOT_SET:
                _params['group_name'] = group_name
            _request = shapes.UpdateSecurityGroupRuleDescriptionsEgressRequest(
                **_params
            )
        response = self._boto_client.update_security_group_rule_descriptions_egress(
            **_request.to_boto()
        )

        return shapes.UpdateSecurityGroupRuleDescriptionsEgressResult.from_boto(
            response
        )

    def update_security_group_rule_descriptions_ingress(
        self,
        _request: shapes.
        UpdateSecurityGroupRuleDescriptionsIngressRequest = None,
        *,
        ip_permissions: typing.List[shapes.IpPermission],
        dry_run: bool = ShapeBase.NOT_SET,
        group_id: str = ShapeBase.NOT_SET,
        group_name: str = ShapeBase.NOT_SET,
    ) -> shapes.UpdateSecurityGroupRuleDescriptionsIngressResult:
        """
        Updates the description of an ingress (inbound) security group rule. You can
        replace an existing description, or add a description to a rule that did not
        have one previously.

        You specify the description as part of the IP permissions structure. You can
        remove a description for a security group rule by omitting the description
        parameter in the request.
        """
        if _request is None:
            _params = {}
            if ip_permissions is not ShapeBase.NOT_SET:
                _params['ip_permissions'] = ip_permissions
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            if group_id is not ShapeBase.NOT_SET:
                _params['group_id'] = group_id
            if group_name is not ShapeBase.NOT_SET:
                _params['group_name'] = group_name
            _request = shapes.UpdateSecurityGroupRuleDescriptionsIngressRequest(
                **_params
            )
        response = self._boto_client.update_security_group_rule_descriptions_ingress(
            **_request.to_boto()
        )

        return shapes.UpdateSecurityGroupRuleDescriptionsIngressResult.from_boto(
            response
        )
