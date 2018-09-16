import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("directconnect", *args, **kwargs)

    def allocate_connection_on_interconnect(
        self,
        _request: shapes.AllocateConnectionOnInterconnectRequest = None,
        *,
        bandwidth: str,
        connection_name: str,
        owner_account: str,
        interconnect_id: str,
        vlan: int,
    ) -> shapes.Connection:
        """
        Deprecated in favor of AllocateHostedConnection.

        Creates a hosted connection on an interconnect.

        Allocates a VLAN number and a specified amount of bandwidth for use by a hosted
        connection on the given interconnect.

        This is intended for use by AWS Direct Connect partners only.
        """
        if _request is None:
            _params = {}
            if bandwidth is not ShapeBase.NOT_SET:
                _params['bandwidth'] = bandwidth
            if connection_name is not ShapeBase.NOT_SET:
                _params['connection_name'] = connection_name
            if owner_account is not ShapeBase.NOT_SET:
                _params['owner_account'] = owner_account
            if interconnect_id is not ShapeBase.NOT_SET:
                _params['interconnect_id'] = interconnect_id
            if vlan is not ShapeBase.NOT_SET:
                _params['vlan'] = vlan
            _request = shapes.AllocateConnectionOnInterconnectRequest(**_params)
        response = self._boto_client.allocate_connection_on_interconnect(
            **_request.to_boto()
        )

        return shapes.Connection.from_boto(response)

    def allocate_hosted_connection(
        self,
        _request: shapes.AllocateHostedConnectionRequest = None,
        *,
        connection_id: str,
        owner_account: str,
        bandwidth: str,
        connection_name: str,
        vlan: int,
    ) -> shapes.Connection:
        """
        Creates a hosted connection on an interconnect or a link aggregation group
        (LAG).

        Allocates a VLAN number and a specified amount of bandwidth for use by a hosted
        connection on the given interconnect or LAG.

        This is intended for use by AWS Direct Connect partners only.
        """
        if _request is None:
            _params = {}
            if connection_id is not ShapeBase.NOT_SET:
                _params['connection_id'] = connection_id
            if owner_account is not ShapeBase.NOT_SET:
                _params['owner_account'] = owner_account
            if bandwidth is not ShapeBase.NOT_SET:
                _params['bandwidth'] = bandwidth
            if connection_name is not ShapeBase.NOT_SET:
                _params['connection_name'] = connection_name
            if vlan is not ShapeBase.NOT_SET:
                _params['vlan'] = vlan
            _request = shapes.AllocateHostedConnectionRequest(**_params)
        response = self._boto_client.allocate_hosted_connection(
            **_request.to_boto()
        )

        return shapes.Connection.from_boto(response)

    def allocate_private_virtual_interface(
        self,
        _request: shapes.AllocatePrivateVirtualInterfaceRequest = None,
        *,
        connection_id: str,
        owner_account: str,
        new_private_virtual_interface_allocation: shapes.
        NewPrivateVirtualInterfaceAllocation,
    ) -> shapes.VirtualInterface:
        """
        Provisions a private virtual interface to be owned by another AWS customer.

        Virtual interfaces created using this action must be confirmed by the virtual
        interface owner by using the ConfirmPrivateVirtualInterface action. Until then,
        the virtual interface will be in 'Confirming' state, and will not be available
        for handling traffic.
        """
        if _request is None:
            _params = {}
            if connection_id is not ShapeBase.NOT_SET:
                _params['connection_id'] = connection_id
            if owner_account is not ShapeBase.NOT_SET:
                _params['owner_account'] = owner_account
            if new_private_virtual_interface_allocation is not ShapeBase.NOT_SET:
                _params['new_private_virtual_interface_allocation'
                       ] = new_private_virtual_interface_allocation
            _request = shapes.AllocatePrivateVirtualInterfaceRequest(**_params)
        response = self._boto_client.allocate_private_virtual_interface(
            **_request.to_boto()
        )

        return shapes.VirtualInterface.from_boto(response)

    def allocate_public_virtual_interface(
        self,
        _request: shapes.AllocatePublicVirtualInterfaceRequest = None,
        *,
        connection_id: str,
        owner_account: str,
        new_public_virtual_interface_allocation: shapes.
        NewPublicVirtualInterfaceAllocation,
    ) -> shapes.VirtualInterface:
        """
        Provisions a public virtual interface to be owned by a different customer.

        The owner of a connection calls this function to provision a public virtual
        interface which will be owned by another AWS customer.

        Virtual interfaces created using this function must be confirmed by the virtual
        interface owner by calling ConfirmPublicVirtualInterface. Until this step has
        been completed, the virtual interface will be in 'Confirming' state, and will
        not be available for handling traffic.

        When creating an IPv6 public virtual interface (addressFamily is 'ipv6'), the
        customer and amazon address fields should be left blank to use auto-assigned
        IPv6 space. Custom IPv6 Addresses are currently not supported.
        """
        if _request is None:
            _params = {}
            if connection_id is not ShapeBase.NOT_SET:
                _params['connection_id'] = connection_id
            if owner_account is not ShapeBase.NOT_SET:
                _params['owner_account'] = owner_account
            if new_public_virtual_interface_allocation is not ShapeBase.NOT_SET:
                _params['new_public_virtual_interface_allocation'
                       ] = new_public_virtual_interface_allocation
            _request = shapes.AllocatePublicVirtualInterfaceRequest(**_params)
        response = self._boto_client.allocate_public_virtual_interface(
            **_request.to_boto()
        )

        return shapes.VirtualInterface.from_boto(response)

    def associate_connection_with_lag(
        self,
        _request: shapes.AssociateConnectionWithLagRequest = None,
        *,
        connection_id: str,
        lag_id: str,
    ) -> shapes.Connection:
        """
        Associates an existing connection with a link aggregation group (LAG). The
        connection is interrupted and re-established as a member of the LAG
        (connectivity to AWS will be interrupted). The connection must be hosted on the
        same AWS Direct Connect endpoint as the LAG, and its bandwidth must match the
        bandwidth for the LAG. You can reassociate a connection that's currently
        associated with a different LAG; however, if removing the connection will cause
        the original LAG to fall below its setting for minimum number of operational
        connections, the request fails.

        Any virtual interfaces that are directly associated with the connection are
        automatically re-associated with the LAG. If the connection was originally
        associated with a different LAG, the virtual interfaces remain associated with
        the original LAG.

        For interconnects, any hosted connections are automatically re-associated with
        the LAG. If the interconnect was originally associated with a different LAG, the
        hosted connections remain associated with the original LAG.
        """
        if _request is None:
            _params = {}
            if connection_id is not ShapeBase.NOT_SET:
                _params['connection_id'] = connection_id
            if lag_id is not ShapeBase.NOT_SET:
                _params['lag_id'] = lag_id
            _request = shapes.AssociateConnectionWithLagRequest(**_params)
        response = self._boto_client.associate_connection_with_lag(
            **_request.to_boto()
        )

        return shapes.Connection.from_boto(response)

    def associate_hosted_connection(
        self,
        _request: shapes.AssociateHostedConnectionRequest = None,
        *,
        connection_id: str,
        parent_connection_id: str,
    ) -> shapes.Connection:
        """
        Associates a hosted connection and its virtual interfaces with a link
        aggregation group (LAG) or interconnect. If the target interconnect or LAG has
        an existing hosted connection with a conflicting VLAN number or IP address, the
        operation fails. This action temporarily interrupts the hosted connection's
        connectivity to AWS as it is being migrated.

        This is intended for use by AWS Direct Connect partners only.
        """
        if _request is None:
            _params = {}
            if connection_id is not ShapeBase.NOT_SET:
                _params['connection_id'] = connection_id
            if parent_connection_id is not ShapeBase.NOT_SET:
                _params['parent_connection_id'] = parent_connection_id
            _request = shapes.AssociateHostedConnectionRequest(**_params)
        response = self._boto_client.associate_hosted_connection(
            **_request.to_boto()
        )

        return shapes.Connection.from_boto(response)

    def associate_virtual_interface(
        self,
        _request: shapes.AssociateVirtualInterfaceRequest = None,
        *,
        virtual_interface_id: str,
        connection_id: str,
    ) -> shapes.VirtualInterface:
        """
        Associates a virtual interface with a specified link aggregation group (LAG) or
        connection. Connectivity to AWS is temporarily interrupted as the virtual
        interface is being migrated. If the target connection or LAG has an associated
        virtual interface with a conflicting VLAN number or a conflicting IP address,
        the operation fails.

        Virtual interfaces associated with a hosted connection cannot be associated with
        a LAG; hosted connections must be migrated along with their virtual interfaces
        using AssociateHostedConnection.

        In order to reassociate a virtual interface to a new connection or LAG, the
        requester must own either the virtual interface itself or the connection to
        which the virtual interface is currently associated. Additionally, the requester
        must own the connection or LAG to which the virtual interface will be newly
        associated.
        """
        if _request is None:
            _params = {}
            if virtual_interface_id is not ShapeBase.NOT_SET:
                _params['virtual_interface_id'] = virtual_interface_id
            if connection_id is not ShapeBase.NOT_SET:
                _params['connection_id'] = connection_id
            _request = shapes.AssociateVirtualInterfaceRequest(**_params)
        response = self._boto_client.associate_virtual_interface(
            **_request.to_boto()
        )

        return shapes.VirtualInterface.from_boto(response)

    def confirm_connection(
        self,
        _request: shapes.ConfirmConnectionRequest = None,
        *,
        connection_id: str,
    ) -> shapes.ConfirmConnectionResponse:
        """
        Confirm the creation of a hosted connection on an interconnect.

        Upon creation, the hosted connection is initially in the 'Ordering' state, and
        will remain in this state until the owner calls ConfirmConnection to confirm
        creation of the hosted connection.
        """
        if _request is None:
            _params = {}
            if connection_id is not ShapeBase.NOT_SET:
                _params['connection_id'] = connection_id
            _request = shapes.ConfirmConnectionRequest(**_params)
        response = self._boto_client.confirm_connection(**_request.to_boto())

        return shapes.ConfirmConnectionResponse.from_boto(response)

    def confirm_private_virtual_interface(
        self,
        _request: shapes.ConfirmPrivateVirtualInterfaceRequest = None,
        *,
        virtual_interface_id: str,
        virtual_gateway_id: str = ShapeBase.NOT_SET,
        direct_connect_gateway_id: str = ShapeBase.NOT_SET,
    ) -> shapes.ConfirmPrivateVirtualInterfaceResponse:
        """
        Accept ownership of a private virtual interface created by another customer.

        After the virtual interface owner calls this function, the virtual interface
        will be created and attached to the given virtual private gateway or direct
        connect gateway, and will be available for handling traffic.
        """
        if _request is None:
            _params = {}
            if virtual_interface_id is not ShapeBase.NOT_SET:
                _params['virtual_interface_id'] = virtual_interface_id
            if virtual_gateway_id is not ShapeBase.NOT_SET:
                _params['virtual_gateway_id'] = virtual_gateway_id
            if direct_connect_gateway_id is not ShapeBase.NOT_SET:
                _params['direct_connect_gateway_id'] = direct_connect_gateway_id
            _request = shapes.ConfirmPrivateVirtualInterfaceRequest(**_params)
        response = self._boto_client.confirm_private_virtual_interface(
            **_request.to_boto()
        )

        return shapes.ConfirmPrivateVirtualInterfaceResponse.from_boto(response)

    def confirm_public_virtual_interface(
        self,
        _request: shapes.ConfirmPublicVirtualInterfaceRequest = None,
        *,
        virtual_interface_id: str,
    ) -> shapes.ConfirmPublicVirtualInterfaceResponse:
        """
        Accept ownership of a public virtual interface created by another customer.

        After the virtual interface owner calls this function, the specified virtual
        interface will be created and made available for handling traffic.
        """
        if _request is None:
            _params = {}
            if virtual_interface_id is not ShapeBase.NOT_SET:
                _params['virtual_interface_id'] = virtual_interface_id
            _request = shapes.ConfirmPublicVirtualInterfaceRequest(**_params)
        response = self._boto_client.confirm_public_virtual_interface(
            **_request.to_boto()
        )

        return shapes.ConfirmPublicVirtualInterfaceResponse.from_boto(response)

    def create_bgp_peer(
        self,
        _request: shapes.CreateBGPPeerRequest = None,
        *,
        virtual_interface_id: str = ShapeBase.NOT_SET,
        new_bgp_peer: shapes.NewBGPPeer = ShapeBase.NOT_SET,
    ) -> shapes.CreateBGPPeerResponse:
        """
        Creates a new BGP peer on a specified virtual interface. The BGP peer cannot be
        in the same address family (IPv4/IPv6) of an existing BGP peer on the virtual
        interface.

        You must create a BGP peer for the corresponding address family in order to
        access AWS resources that also use that address family.

        When creating a IPv6 BGP peer, the Amazon address and customer address fields
        must be left blank. IPv6 addresses are automatically assigned from Amazon's pool
        of IPv6 addresses; you cannot specify custom IPv6 addresses.

        For a public virtual interface, the Autonomous System Number (ASN) must be
        private or already whitelisted for the virtual interface.
        """
        if _request is None:
            _params = {}
            if virtual_interface_id is not ShapeBase.NOT_SET:
                _params['virtual_interface_id'] = virtual_interface_id
            if new_bgp_peer is not ShapeBase.NOT_SET:
                _params['new_bgp_peer'] = new_bgp_peer
            _request = shapes.CreateBGPPeerRequest(**_params)
        response = self._boto_client.create_bgp_peer(**_request.to_boto())

        return shapes.CreateBGPPeerResponse.from_boto(response)

    def create_connection(
        self,
        _request: shapes.CreateConnectionRequest = None,
        *,
        location: str,
        bandwidth: str,
        connection_name: str,
        lag_id: str = ShapeBase.NOT_SET,
    ) -> shapes.Connection:
        """
        Creates a new connection between the customer network and a specific AWS Direct
        Connect location.

        A connection links your internal network to an AWS Direct Connect location over
        a standard 1 gigabit or 10 gigabit Ethernet fiber-optic cable. One end of the
        cable is connected to your router, the other to an AWS Direct Connect router. An
        AWS Direct Connect location provides access to Amazon Web Services in the region
        it is associated with. You can establish connections with AWS Direct Connect
        locations in multiple regions, but a connection in one region does not provide
        connectivity to other regions.

        To find the locations for your region, use DescribeLocations.

        You can automatically add the new connection to a link aggregation group (LAG)
        by specifying a LAG ID in the request. This ensures that the new connection is
        allocated on the same AWS Direct Connect endpoint that hosts the specified LAG.
        If there are no available ports on the endpoint, the request fails and no
        connection will be created.
        """
        if _request is None:
            _params = {}
            if location is not ShapeBase.NOT_SET:
                _params['location'] = location
            if bandwidth is not ShapeBase.NOT_SET:
                _params['bandwidth'] = bandwidth
            if connection_name is not ShapeBase.NOT_SET:
                _params['connection_name'] = connection_name
            if lag_id is not ShapeBase.NOT_SET:
                _params['lag_id'] = lag_id
            _request = shapes.CreateConnectionRequest(**_params)
        response = self._boto_client.create_connection(**_request.to_boto())

        return shapes.Connection.from_boto(response)

    def create_direct_connect_gateway(
        self,
        _request: shapes.CreateDirectConnectGatewayRequest = None,
        *,
        direct_connect_gateway_name: str,
        amazon_side_asn: int = ShapeBase.NOT_SET,
    ) -> shapes.CreateDirectConnectGatewayResult:
        """
        Creates a new direct connect gateway. A direct connect gateway is an
        intermediate object that enables you to connect a set of virtual interfaces and
        virtual private gateways. direct connect gateways are global and visible in any
        AWS region after they are created. The virtual interfaces and virtual private
        gateways that are connected through a direct connect gateway can be in different
        regions. This enables you to connect to a VPC in any region, regardless of the
        region in which the virtual interfaces are located, and pass traffic between
        them.
        """
        if _request is None:
            _params = {}
            if direct_connect_gateway_name is not ShapeBase.NOT_SET:
                _params['direct_connect_gateway_name'
                       ] = direct_connect_gateway_name
            if amazon_side_asn is not ShapeBase.NOT_SET:
                _params['amazon_side_asn'] = amazon_side_asn
            _request = shapes.CreateDirectConnectGatewayRequest(**_params)
        response = self._boto_client.create_direct_connect_gateway(
            **_request.to_boto()
        )

        return shapes.CreateDirectConnectGatewayResult.from_boto(response)

    def create_direct_connect_gateway_association(
        self,
        _request: shapes.CreateDirectConnectGatewayAssociationRequest = None,
        *,
        direct_connect_gateway_id: str,
        virtual_gateway_id: str,
    ) -> shapes.CreateDirectConnectGatewayAssociationResult:
        """
        Creates an association between a direct connect gateway and a virtual private
        gateway (VGW). The VGW must be attached to a VPC and must not be associated with
        another direct connect gateway.
        """
        if _request is None:
            _params = {}
            if direct_connect_gateway_id is not ShapeBase.NOT_SET:
                _params['direct_connect_gateway_id'] = direct_connect_gateway_id
            if virtual_gateway_id is not ShapeBase.NOT_SET:
                _params['virtual_gateway_id'] = virtual_gateway_id
            _request = shapes.CreateDirectConnectGatewayAssociationRequest(
                **_params
            )
        response = self._boto_client.create_direct_connect_gateway_association(
            **_request.to_boto()
        )

        return shapes.CreateDirectConnectGatewayAssociationResult.from_boto(
            response
        )

    def create_interconnect(
        self,
        _request: shapes.CreateInterconnectRequest = None,
        *,
        interconnect_name: str,
        bandwidth: str,
        location: str,
        lag_id: str = ShapeBase.NOT_SET,
    ) -> shapes.Interconnect:
        """
        Creates a new interconnect between a AWS Direct Connect partner's network and a
        specific AWS Direct Connect location.

        An interconnect is a connection which is capable of hosting other connections.
        The AWS Direct Connect partner can use an interconnect to provide sub-1Gbps AWS
        Direct Connect service to tier 2 customers who do not have their own
        connections. Like a standard connection, an interconnect links the AWS Direct
        Connect partner's network to an AWS Direct Connect location over a standard 1
        Gbps or 10 Gbps Ethernet fiber-optic cable. One end is connected to the
        partner's router, the other to an AWS Direct Connect router.

        You can automatically add the new interconnect to a link aggregation group (LAG)
        by specifying a LAG ID in the request. This ensures that the new interconnect is
        allocated on the same AWS Direct Connect endpoint that hosts the specified LAG.
        If there are no available ports on the endpoint, the request fails and no
        interconnect will be created.

        For each end customer, the AWS Direct Connect partner provisions a connection on
        their interconnect by calling AllocateConnectionOnInterconnect. The end customer
        can then connect to AWS resources by creating a virtual interface on their
        connection, using the VLAN assigned to them by the AWS Direct Connect partner.

        This is intended for use by AWS Direct Connect partners only.
        """
        if _request is None:
            _params = {}
            if interconnect_name is not ShapeBase.NOT_SET:
                _params['interconnect_name'] = interconnect_name
            if bandwidth is not ShapeBase.NOT_SET:
                _params['bandwidth'] = bandwidth
            if location is not ShapeBase.NOT_SET:
                _params['location'] = location
            if lag_id is not ShapeBase.NOT_SET:
                _params['lag_id'] = lag_id
            _request = shapes.CreateInterconnectRequest(**_params)
        response = self._boto_client.create_interconnect(**_request.to_boto())

        return shapes.Interconnect.from_boto(response)

    def create_lag(
        self,
        _request: shapes.CreateLagRequest = None,
        *,
        number_of_connections: int,
        location: str,
        connections_bandwidth: str,
        lag_name: str,
        connection_id: str = ShapeBase.NOT_SET,
    ) -> shapes.Lag:
        """
        Creates a new link aggregation group (LAG) with the specified number of bundled
        physical connections between the customer network and a specific AWS Direct
        Connect location. A LAG is a logical interface that uses the Link Aggregation
        Control Protocol (LACP) to aggregate multiple 1 gigabit or 10 gigabit
        interfaces, allowing you to treat them as a single interface.

        All connections in a LAG must use the same bandwidth (for example, 10 Gbps), and
        must terminate at the same AWS Direct Connect endpoint.

        You can have up to 10 connections per LAG. Regardless of this limit, if you
        request more connections for the LAG than AWS Direct Connect can allocate on a
        single endpoint, no LAG is created.

        You can specify an existing physical connection or interconnect to include in
        the LAG (which counts towards the total number of connections). Doing so
        interrupts the current physical connection or hosted connections, and re-
        establishes them as a member of the LAG. The LAG will be created on the same AWS
        Direct Connect endpoint to which the connection terminates. Any virtual
        interfaces associated with the connection are automatically disassociated and
        re-associated with the LAG. The connection ID does not change.

        If the AWS account used to create a LAG is a registered AWS Direct Connect
        partner, the LAG is automatically enabled to host sub-connections. For a LAG
        owned by a partner, any associated virtual interfaces cannot be directly
        configured.
        """
        if _request is None:
            _params = {}
            if number_of_connections is not ShapeBase.NOT_SET:
                _params['number_of_connections'] = number_of_connections
            if location is not ShapeBase.NOT_SET:
                _params['location'] = location
            if connections_bandwidth is not ShapeBase.NOT_SET:
                _params['connections_bandwidth'] = connections_bandwidth
            if lag_name is not ShapeBase.NOT_SET:
                _params['lag_name'] = lag_name
            if connection_id is not ShapeBase.NOT_SET:
                _params['connection_id'] = connection_id
            _request = shapes.CreateLagRequest(**_params)
        response = self._boto_client.create_lag(**_request.to_boto())

        return shapes.Lag.from_boto(response)

    def create_private_virtual_interface(
        self,
        _request: shapes.CreatePrivateVirtualInterfaceRequest = None,
        *,
        connection_id: str,
        new_private_virtual_interface: shapes.NewPrivateVirtualInterface,
    ) -> shapes.VirtualInterface:
        """
        Creates a new private virtual interface. A virtual interface is the VLAN that
        transports AWS Direct Connect traffic. A private virtual interface supports
        sending traffic to a single virtual private cloud (VPC).
        """
        if _request is None:
            _params = {}
            if connection_id is not ShapeBase.NOT_SET:
                _params['connection_id'] = connection_id
            if new_private_virtual_interface is not ShapeBase.NOT_SET:
                _params['new_private_virtual_interface'
                       ] = new_private_virtual_interface
            _request = shapes.CreatePrivateVirtualInterfaceRequest(**_params)
        response = self._boto_client.create_private_virtual_interface(
            **_request.to_boto()
        )

        return shapes.VirtualInterface.from_boto(response)

    def create_public_virtual_interface(
        self,
        _request: shapes.CreatePublicVirtualInterfaceRequest = None,
        *,
        connection_id: str,
        new_public_virtual_interface: shapes.NewPublicVirtualInterface,
    ) -> shapes.VirtualInterface:
        """
        Creates a new public virtual interface. A virtual interface is the VLAN that
        transports AWS Direct Connect traffic. A public virtual interface supports
        sending traffic to public services of AWS such as Amazon Simple Storage Service
        (Amazon S3).

        When creating an IPv6 public virtual interface (addressFamily is 'ipv6'), the
        customer and amazon address fields should be left blank to use auto-assigned
        IPv6 space. Custom IPv6 Addresses are currently not supported.
        """
        if _request is None:
            _params = {}
            if connection_id is not ShapeBase.NOT_SET:
                _params['connection_id'] = connection_id
            if new_public_virtual_interface is not ShapeBase.NOT_SET:
                _params['new_public_virtual_interface'
                       ] = new_public_virtual_interface
            _request = shapes.CreatePublicVirtualInterfaceRequest(**_params)
        response = self._boto_client.create_public_virtual_interface(
            **_request.to_boto()
        )

        return shapes.VirtualInterface.from_boto(response)

    def delete_bgp_peer(
        self,
        _request: shapes.DeleteBGPPeerRequest = None,
        *,
        virtual_interface_id: str = ShapeBase.NOT_SET,
        asn: int = ShapeBase.NOT_SET,
        customer_address: str = ShapeBase.NOT_SET,
    ) -> shapes.DeleteBGPPeerResponse:
        """
        Deletes a BGP peer on the specified virtual interface that matches the specified
        customer address and ASN. You cannot delete the last BGP peer from a virtual
        interface.
        """
        if _request is None:
            _params = {}
            if virtual_interface_id is not ShapeBase.NOT_SET:
                _params['virtual_interface_id'] = virtual_interface_id
            if asn is not ShapeBase.NOT_SET:
                _params['asn'] = asn
            if customer_address is not ShapeBase.NOT_SET:
                _params['customer_address'] = customer_address
            _request = shapes.DeleteBGPPeerRequest(**_params)
        response = self._boto_client.delete_bgp_peer(**_request.to_boto())

        return shapes.DeleteBGPPeerResponse.from_boto(response)

    def delete_connection(
        self,
        _request: shapes.DeleteConnectionRequest = None,
        *,
        connection_id: str,
    ) -> shapes.Connection:
        """
        Deletes the connection.

        Deleting a connection only stops the AWS Direct Connect port hour and data
        transfer charges. You need to cancel separately with the providers any services
        or charges for cross-connects or network circuits that connect you to the AWS
        Direct Connect location.
        """
        if _request is None:
            _params = {}
            if connection_id is not ShapeBase.NOT_SET:
                _params['connection_id'] = connection_id
            _request = shapes.DeleteConnectionRequest(**_params)
        response = self._boto_client.delete_connection(**_request.to_boto())

        return shapes.Connection.from_boto(response)

    def delete_direct_connect_gateway(
        self,
        _request: shapes.DeleteDirectConnectGatewayRequest = None,
        *,
        direct_connect_gateway_id: str,
    ) -> shapes.DeleteDirectConnectGatewayResult:
        """
        Deletes a direct connect gateway. You must first delete all virtual interfaces
        that are attached to the direct connect gateway and disassociate all virtual
        private gateways that are associated with the direct connect gateway.
        """
        if _request is None:
            _params = {}
            if direct_connect_gateway_id is not ShapeBase.NOT_SET:
                _params['direct_connect_gateway_id'] = direct_connect_gateway_id
            _request = shapes.DeleteDirectConnectGatewayRequest(**_params)
        response = self._boto_client.delete_direct_connect_gateway(
            **_request.to_boto()
        )

        return shapes.DeleteDirectConnectGatewayResult.from_boto(response)

    def delete_direct_connect_gateway_association(
        self,
        _request: shapes.DeleteDirectConnectGatewayAssociationRequest = None,
        *,
        direct_connect_gateway_id: str,
        virtual_gateway_id: str,
    ) -> shapes.DeleteDirectConnectGatewayAssociationResult:
        """
        Deletes the association between a direct connect gateway and a virtual private
        gateway.
        """
        if _request is None:
            _params = {}
            if direct_connect_gateway_id is not ShapeBase.NOT_SET:
                _params['direct_connect_gateway_id'] = direct_connect_gateway_id
            if virtual_gateway_id is not ShapeBase.NOT_SET:
                _params['virtual_gateway_id'] = virtual_gateway_id
            _request = shapes.DeleteDirectConnectGatewayAssociationRequest(
                **_params
            )
        response = self._boto_client.delete_direct_connect_gateway_association(
            **_request.to_boto()
        )

        return shapes.DeleteDirectConnectGatewayAssociationResult.from_boto(
            response
        )

    def delete_interconnect(
        self,
        _request: shapes.DeleteInterconnectRequest = None,
        *,
        interconnect_id: str,
    ) -> shapes.DeleteInterconnectResponse:
        """
        Deletes the specified interconnect.

        This is intended for use by AWS Direct Connect partners only.
        """
        if _request is None:
            _params = {}
            if interconnect_id is not ShapeBase.NOT_SET:
                _params['interconnect_id'] = interconnect_id
            _request = shapes.DeleteInterconnectRequest(**_params)
        response = self._boto_client.delete_interconnect(**_request.to_boto())

        return shapes.DeleteInterconnectResponse.from_boto(response)

    def delete_lag(
        self,
        _request: shapes.DeleteLagRequest = None,
        *,
        lag_id: str,
    ) -> shapes.Lag:
        """
        Deletes a link aggregation group (LAG). You cannot delete a LAG if it has active
        virtual interfaces or hosted connections.
        """
        if _request is None:
            _params = {}
            if lag_id is not ShapeBase.NOT_SET:
                _params['lag_id'] = lag_id
            _request = shapes.DeleteLagRequest(**_params)
        response = self._boto_client.delete_lag(**_request.to_boto())

        return shapes.Lag.from_boto(response)

    def delete_virtual_interface(
        self,
        _request: shapes.DeleteVirtualInterfaceRequest = None,
        *,
        virtual_interface_id: str,
    ) -> shapes.DeleteVirtualInterfaceResponse:
        """
        Deletes a virtual interface.
        """
        if _request is None:
            _params = {}
            if virtual_interface_id is not ShapeBase.NOT_SET:
                _params['virtual_interface_id'] = virtual_interface_id
            _request = shapes.DeleteVirtualInterfaceRequest(**_params)
        response = self._boto_client.delete_virtual_interface(
            **_request.to_boto()
        )

        return shapes.DeleteVirtualInterfaceResponse.from_boto(response)

    def describe_connection_loa(
        self,
        _request: shapes.DescribeConnectionLoaRequest = None,
        *,
        connection_id: str,
        provider_name: str = ShapeBase.NOT_SET,
        loa_content_type: typing.Union[str, shapes.LoaContentType] = ShapeBase.
        NOT_SET,
    ) -> shapes.DescribeConnectionLoaResponse:
        """
        Deprecated in favor of DescribeLoa.

        Returns the LOA-CFA for a Connection.

        The Letter of Authorization - Connecting Facility Assignment (LOA-CFA) is a
        document that your APN partner or service provider uses when establishing your
        cross connect to AWS at the colocation facility. For more information, see
        [Requesting Cross Connects at AWS Direct Connect
        Locations](http://docs.aws.amazon.com/directconnect/latest/UserGuide/Colocation.html)
        in the AWS Direct Connect user guide.
        """
        if _request is None:
            _params = {}
            if connection_id is not ShapeBase.NOT_SET:
                _params['connection_id'] = connection_id
            if provider_name is not ShapeBase.NOT_SET:
                _params['provider_name'] = provider_name
            if loa_content_type is not ShapeBase.NOT_SET:
                _params['loa_content_type'] = loa_content_type
            _request = shapes.DescribeConnectionLoaRequest(**_params)
        response = self._boto_client.describe_connection_loa(
            **_request.to_boto()
        )

        return shapes.DescribeConnectionLoaResponse.from_boto(response)

    def describe_connections(
        self,
        _request: shapes.DescribeConnectionsRequest = None,
        *,
        connection_id: str = ShapeBase.NOT_SET,
    ) -> shapes.Connections:
        """
        Displays all connections in this region.

        If a connection ID is provided, the call returns only that particular
        connection.
        """
        if _request is None:
            _params = {}
            if connection_id is not ShapeBase.NOT_SET:
                _params['connection_id'] = connection_id
            _request = shapes.DescribeConnectionsRequest(**_params)
        response = self._boto_client.describe_connections(**_request.to_boto())

        return shapes.Connections.from_boto(response)

    def describe_connections_on_interconnect(
        self,
        _request: shapes.DescribeConnectionsOnInterconnectRequest = None,
        *,
        interconnect_id: str,
    ) -> shapes.Connections:
        """
        Deprecated in favor of DescribeHostedConnections.

        Returns a list of connections that have been provisioned on the given
        interconnect.

        This is intended for use by AWS Direct Connect partners only.
        """
        if _request is None:
            _params = {}
            if interconnect_id is not ShapeBase.NOT_SET:
                _params['interconnect_id'] = interconnect_id
            _request = shapes.DescribeConnectionsOnInterconnectRequest(
                **_params
            )
        response = self._boto_client.describe_connections_on_interconnect(
            **_request.to_boto()
        )

        return shapes.Connections.from_boto(response)

    def describe_direct_connect_gateway_associations(
        self,
        _request: shapes.DescribeDirectConnectGatewayAssociationsRequest = None,
        *,
        direct_connect_gateway_id: str = ShapeBase.NOT_SET,
        virtual_gateway_id: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeDirectConnectGatewayAssociationsResult:
        """
        Returns a list of all direct connect gateway and virtual private gateway (VGW)
        associations. Either a direct connect gateway ID or a VGW ID must be provided in
        the request. If a direct connect gateway ID is provided, the response returns
        all VGWs associated with the direct connect gateway. If a VGW ID is provided,
        the response returns all direct connect gateways associated with the VGW. If
        both are provided, the response only returns the association that matches both
        the direct connect gateway and the VGW.
        """
        if _request is None:
            _params = {}
            if direct_connect_gateway_id is not ShapeBase.NOT_SET:
                _params['direct_connect_gateway_id'] = direct_connect_gateway_id
            if virtual_gateway_id is not ShapeBase.NOT_SET:
                _params['virtual_gateway_id'] = virtual_gateway_id
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.DescribeDirectConnectGatewayAssociationsRequest(
                **_params
            )
        response = self._boto_client.describe_direct_connect_gateway_associations(
            **_request.to_boto()
        )

        return shapes.DescribeDirectConnectGatewayAssociationsResult.from_boto(
            response
        )

    def describe_direct_connect_gateway_attachments(
        self,
        _request: shapes.DescribeDirectConnectGatewayAttachmentsRequest = None,
        *,
        direct_connect_gateway_id: str = ShapeBase.NOT_SET,
        virtual_interface_id: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeDirectConnectGatewayAttachmentsResult:
        """
        Returns a list of all direct connect gateway and virtual interface (VIF)
        attachments. Either a direct connect gateway ID or a VIF ID must be provided in
        the request. If a direct connect gateway ID is provided, the response returns
        all VIFs attached to the direct connect gateway. If a VIF ID is provided, the
        response returns all direct connect gateways attached to the VIF. If both are
        provided, the response only returns the attachment that matches both the direct
        connect gateway and the VIF.
        """
        if _request is None:
            _params = {}
            if direct_connect_gateway_id is not ShapeBase.NOT_SET:
                _params['direct_connect_gateway_id'] = direct_connect_gateway_id
            if virtual_interface_id is not ShapeBase.NOT_SET:
                _params['virtual_interface_id'] = virtual_interface_id
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.DescribeDirectConnectGatewayAttachmentsRequest(
                **_params
            )
        response = self._boto_client.describe_direct_connect_gateway_attachments(
            **_request.to_boto()
        )

        return shapes.DescribeDirectConnectGatewayAttachmentsResult.from_boto(
            response
        )

    def describe_direct_connect_gateways(
        self,
        _request: shapes.DescribeDirectConnectGatewaysRequest = None,
        *,
        direct_connect_gateway_id: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeDirectConnectGatewaysResult:
        """
        Returns a list of direct connect gateways in your account. Deleted direct
        connect gateways are not returned. You can provide a direct connect gateway ID
        in the request to return information about the specific direct connect gateway
        only. Otherwise, if a direct connect gateway ID is not provided, information
        about all of your direct connect gateways is returned.
        """
        if _request is None:
            _params = {}
            if direct_connect_gateway_id is not ShapeBase.NOT_SET:
                _params['direct_connect_gateway_id'] = direct_connect_gateway_id
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.DescribeDirectConnectGatewaysRequest(**_params)
        response = self._boto_client.describe_direct_connect_gateways(
            **_request.to_boto()
        )

        return shapes.DescribeDirectConnectGatewaysResult.from_boto(response)

    def describe_hosted_connections(
        self,
        _request: shapes.DescribeHostedConnectionsRequest = None,
        *,
        connection_id: str,
    ) -> shapes.Connections:
        """
        Returns a list of hosted connections that have been provisioned on the given
        interconnect or link aggregation group (LAG).

        This is intended for use by AWS Direct Connect partners only.
        """
        if _request is None:
            _params = {}
            if connection_id is not ShapeBase.NOT_SET:
                _params['connection_id'] = connection_id
            _request = shapes.DescribeHostedConnectionsRequest(**_params)
        response = self._boto_client.describe_hosted_connections(
            **_request.to_boto()
        )

        return shapes.Connections.from_boto(response)

    def describe_interconnect_loa(
        self,
        _request: shapes.DescribeInterconnectLoaRequest = None,
        *,
        interconnect_id: str,
        provider_name: str = ShapeBase.NOT_SET,
        loa_content_type: typing.Union[str, shapes.LoaContentType] = ShapeBase.
        NOT_SET,
    ) -> shapes.DescribeInterconnectLoaResponse:
        """
        Deprecated in favor of DescribeLoa.

        Returns the LOA-CFA for an Interconnect.

        The Letter of Authorization - Connecting Facility Assignment (LOA-CFA) is a
        document that is used when establishing your cross connect to AWS at the
        colocation facility. For more information, see [Requesting Cross Connects at AWS
        Direct Connect
        Locations](http://docs.aws.amazon.com/directconnect/latest/UserGuide/Colocation.html)
        in the AWS Direct Connect user guide.
        """
        if _request is None:
            _params = {}
            if interconnect_id is not ShapeBase.NOT_SET:
                _params['interconnect_id'] = interconnect_id
            if provider_name is not ShapeBase.NOT_SET:
                _params['provider_name'] = provider_name
            if loa_content_type is not ShapeBase.NOT_SET:
                _params['loa_content_type'] = loa_content_type
            _request = shapes.DescribeInterconnectLoaRequest(**_params)
        response = self._boto_client.describe_interconnect_loa(
            **_request.to_boto()
        )

        return shapes.DescribeInterconnectLoaResponse.from_boto(response)

    def describe_interconnects(
        self,
        _request: shapes.DescribeInterconnectsRequest = None,
        *,
        interconnect_id: str = ShapeBase.NOT_SET,
    ) -> shapes.Interconnects:
        """
        Returns a list of interconnects owned by the AWS account.

        If an interconnect ID is provided, it will only return this particular
        interconnect.
        """
        if _request is None:
            _params = {}
            if interconnect_id is not ShapeBase.NOT_SET:
                _params['interconnect_id'] = interconnect_id
            _request = shapes.DescribeInterconnectsRequest(**_params)
        response = self._boto_client.describe_interconnects(
            **_request.to_boto()
        )

        return shapes.Interconnects.from_boto(response)

    def describe_lags(
        self,
        _request: shapes.DescribeLagsRequest = None,
        *,
        lag_id: str = ShapeBase.NOT_SET,
    ) -> shapes.Lags:
        """
        Describes the link aggregation groups (LAGs) in your account.

        If a LAG ID is provided, only information about the specified LAG is returned.
        """
        if _request is None:
            _params = {}
            if lag_id is not ShapeBase.NOT_SET:
                _params['lag_id'] = lag_id
            _request = shapes.DescribeLagsRequest(**_params)
        response = self._boto_client.describe_lags(**_request.to_boto())

        return shapes.Lags.from_boto(response)

    def describe_loa(
        self,
        _request: shapes.DescribeLoaRequest = None,
        *,
        connection_id: str,
        provider_name: str = ShapeBase.NOT_SET,
        loa_content_type: typing.Union[str, shapes.LoaContentType] = ShapeBase.
        NOT_SET,
    ) -> shapes.Loa:
        """
        Returns the LOA-CFA for a connection, interconnect, or link aggregation group
        (LAG).

        The Letter of Authorization - Connecting Facility Assignment (LOA-CFA) is a
        document that is used when establishing your cross connect to AWS at the
        colocation facility. For more information, see [Requesting Cross Connects at AWS
        Direct Connect
        Locations](http://docs.aws.amazon.com/directconnect/latest/UserGuide/Colocation.html)
        in the AWS Direct Connect user guide.
        """
        if _request is None:
            _params = {}
            if connection_id is not ShapeBase.NOT_SET:
                _params['connection_id'] = connection_id
            if provider_name is not ShapeBase.NOT_SET:
                _params['provider_name'] = provider_name
            if loa_content_type is not ShapeBase.NOT_SET:
                _params['loa_content_type'] = loa_content_type
            _request = shapes.DescribeLoaRequest(**_params)
        response = self._boto_client.describe_loa(**_request.to_boto())

        return shapes.Loa.from_boto(response)

    def describe_locations(self) -> shapes.Locations:
        """
        Returns the list of AWS Direct Connect locations in the current AWS region.
        These are the locations that may be selected when calling CreateConnection or
        CreateInterconnect.
        """
        response = self._boto_client.describe_locations()

        return shapes.Locations.from_boto(response)

    def describe_tags(
        self,
        _request: shapes.DescribeTagsRequest = None,
        *,
        resource_arns: typing.List[str],
    ) -> shapes.DescribeTagsResponse:
        """
        Describes the tags associated with the specified Direct Connect resources.
        """
        if _request is None:
            _params = {}
            if resource_arns is not ShapeBase.NOT_SET:
                _params['resource_arns'] = resource_arns
            _request = shapes.DescribeTagsRequest(**_params)
        response = self._boto_client.describe_tags(**_request.to_boto())

        return shapes.DescribeTagsResponse.from_boto(response)

    def describe_virtual_gateways(self) -> shapes.VirtualGateways:
        """
        Returns a list of virtual private gateways owned by the AWS account.

        You can create one or more AWS Direct Connect private virtual interfaces linking
        to a virtual private gateway. A virtual private gateway can be managed via
        Amazon Virtual Private Cloud (VPC) console or the [EC2
        CreateVpnGateway](http://docs.aws.amazon.com/AWSEC2/latest/APIReference/ApiReference-
        query-CreateVpnGateway.html) action.
        """
        response = self._boto_client.describe_virtual_gateways()

        return shapes.VirtualGateways.from_boto(response)

    def describe_virtual_interfaces(
        self,
        _request: shapes.DescribeVirtualInterfacesRequest = None,
        *,
        connection_id: str = ShapeBase.NOT_SET,
        virtual_interface_id: str = ShapeBase.NOT_SET,
    ) -> shapes.VirtualInterfaces:
        """
        Displays all virtual interfaces for an AWS account. Virtual interfaces deleted
        fewer than 15 minutes before you make the request are also returned. If you
        specify a connection ID, only the virtual interfaces associated with the
        connection are returned. If you specify a virtual interface ID, then only a
        single virtual interface is returned.

        A virtual interface (VLAN) transmits the traffic between the AWS Direct Connect
        location and the customer.
        """
        if _request is None:
            _params = {}
            if connection_id is not ShapeBase.NOT_SET:
                _params['connection_id'] = connection_id
            if virtual_interface_id is not ShapeBase.NOT_SET:
                _params['virtual_interface_id'] = virtual_interface_id
            _request = shapes.DescribeVirtualInterfacesRequest(**_params)
        response = self._boto_client.describe_virtual_interfaces(
            **_request.to_boto()
        )

        return shapes.VirtualInterfaces.from_boto(response)

    def disassociate_connection_from_lag(
        self,
        _request: shapes.DisassociateConnectionFromLagRequest = None,
        *,
        connection_id: str,
        lag_id: str,
    ) -> shapes.Connection:
        """
        Disassociates a connection from a link aggregation group (LAG). The connection
        is interrupted and re-established as a standalone connection (the connection is
        not deleted; to delete the connection, use the DeleteConnection request). If the
        LAG has associated virtual interfaces or hosted connections, they remain
        associated with the LAG. A disassociated connection owned by an AWS Direct
        Connect partner is automatically converted to an interconnect.

        If disassociating the connection will cause the LAG to fall below its setting
        for minimum number of operational connections, the request fails, except when
        it's the last member of the LAG. If all connections are disassociated, the LAG
        continues to exist as an empty LAG with no physical connections.
        """
        if _request is None:
            _params = {}
            if connection_id is not ShapeBase.NOT_SET:
                _params['connection_id'] = connection_id
            if lag_id is not ShapeBase.NOT_SET:
                _params['lag_id'] = lag_id
            _request = shapes.DisassociateConnectionFromLagRequest(**_params)
        response = self._boto_client.disassociate_connection_from_lag(
            **_request.to_boto()
        )

        return shapes.Connection.from_boto(response)

    def tag_resource(
        self,
        _request: shapes.TagResourceRequest = None,
        *,
        resource_arn: str,
        tags: typing.List[shapes.Tag],
    ) -> shapes.TagResourceResponse:
        """
        Adds the specified tags to the specified Direct Connect resource. Each Direct
        Connect resource can have a maximum of 50 tags.

        Each tag consists of a key and an optional value. If a tag with the same key is
        already associated with the Direct Connect resource, this action updates its
        value.
        """
        if _request is None:
            _params = {}
            if resource_arn is not ShapeBase.NOT_SET:
                _params['resource_arn'] = resource_arn
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            _request = shapes.TagResourceRequest(**_params)
        response = self._boto_client.tag_resource(**_request.to_boto())

        return shapes.TagResourceResponse.from_boto(response)

    def untag_resource(
        self,
        _request: shapes.UntagResourceRequest = None,
        *,
        resource_arn: str,
        tag_keys: typing.List[str],
    ) -> shapes.UntagResourceResponse:
        """
        Removes one or more tags from the specified Direct Connect resource.
        """
        if _request is None:
            _params = {}
            if resource_arn is not ShapeBase.NOT_SET:
                _params['resource_arn'] = resource_arn
            if tag_keys is not ShapeBase.NOT_SET:
                _params['tag_keys'] = tag_keys
            _request = shapes.UntagResourceRequest(**_params)
        response = self._boto_client.untag_resource(**_request.to_boto())

        return shapes.UntagResourceResponse.from_boto(response)

    def update_lag(
        self,
        _request: shapes.UpdateLagRequest = None,
        *,
        lag_id: str,
        lag_name: str = ShapeBase.NOT_SET,
        minimum_links: int = ShapeBase.NOT_SET,
    ) -> shapes.Lag:
        """
        Updates the attributes of a link aggregation group (LAG).

        You can update the following attributes:

          * The name of the LAG.

          * The value for the minimum number of connections that must be operational for the LAG itself to be operational. 

        When you create a LAG, the default value for the minimum number of operational
        connections is zero (0). If you update this value, and the number of operational
        connections falls below the specified value, the LAG will automatically go down
        to avoid overutilization of the remaining connections. Adjusting this value
        should be done with care as it could force the LAG down if the value is set
        higher than the current number of operational connections.
        """
        if _request is None:
            _params = {}
            if lag_id is not ShapeBase.NOT_SET:
                _params['lag_id'] = lag_id
            if lag_name is not ShapeBase.NOT_SET:
                _params['lag_name'] = lag_name
            if minimum_links is not ShapeBase.NOT_SET:
                _params['minimum_links'] = minimum_links
            _request = shapes.UpdateLagRequest(**_params)
        response = self._boto_client.update_lag(**_request.to_boto())

        return shapes.Lag.from_boto(response)
