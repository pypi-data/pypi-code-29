import datetime
import typing
from autoboto import ShapeBase, OutputShapeBase, TypeInfo
import botocore.response
import dataclasses


class AddressFamily(str):
    """
    Indicates the address family for the BGP peer.

      * **ipv4** : IPv4 address family

      * **ipv6** : IPv6 address family
    """
    ipv4 = "ipv4"
    ipv6 = "ipv6"


@dataclasses.dataclass
class AllocateConnectionOnInterconnectRequest(ShapeBase):
    """
    Container for the parameters to the AllocateConnectionOnInterconnect operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bandwidth",
                "bandwidth",
                TypeInfo(str),
            ),
            (
                "connection_name",
                "connectionName",
                TypeInfo(str),
            ),
            (
                "owner_account",
                "ownerAccount",
                TypeInfo(str),
            ),
            (
                "interconnect_id",
                "interconnectId",
                TypeInfo(str),
            ),
            (
                "vlan",
                "vlan",
                TypeInfo(int),
            ),
        ]

    # Bandwidth of the connection.

    # Example: " _500Mbps_ "

    # Default: None

    # Values: 50Mbps, 100Mbps, 200Mbps, 300Mbps, 400Mbps, or 500Mbps
    bandwidth: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Name of the provisioned connection.

    # Example: " _500M Connection to AWS_ "

    # Default: None
    connection_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Numeric account Id of the customer for whom the connection will be
    # provisioned.

    # Example: 123443215678

    # Default: None
    owner_account: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # ID of the interconnect on which the connection will be provisioned.

    # Example: dxcon-456abc78

    # Default: None
    interconnect_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The dedicated VLAN provisioned to the connection.

    # Example: 101

    # Default: None
    vlan: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AllocateHostedConnectionRequest(ShapeBase):
    """
    Container for the parameters to theHostedConnection operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "connection_id",
                "connectionId",
                TypeInfo(str),
            ),
            (
                "owner_account",
                "ownerAccount",
                TypeInfo(str),
            ),
            (
                "bandwidth",
                "bandwidth",
                TypeInfo(str),
            ),
            (
                "connection_name",
                "connectionName",
                TypeInfo(str),
            ),
            (
                "vlan",
                "vlan",
                TypeInfo(int),
            ),
        ]

    # The ID of the interconnect or LAG on which the connection will be
    # provisioned.

    # Example: dxcon-456abc78 or dxlag-abc123

    # Default: None
    connection_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The numeric account ID of the customer for whom the connection will be
    # provisioned.

    # Example: 123443215678

    # Default: None
    owner_account: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The bandwidth of the connection.

    # Example: `500Mbps`

    # Default: None

    # Values: 50Mbps, 100Mbps, 200Mbps, 300Mbps, 400Mbps, or 500Mbps
    bandwidth: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the provisioned connection.

    # Example: "`500M Connection to AWS`"

    # Default: None
    connection_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The dedicated VLAN provisioned to the hosted connection.

    # Example: 101

    # Default: None
    vlan: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AllocatePrivateVirtualInterfaceRequest(ShapeBase):
    """
    Container for the parameters to the AllocatePrivateVirtualInterface operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "connection_id",
                "connectionId",
                TypeInfo(str),
            ),
            (
                "owner_account",
                "ownerAccount",
                TypeInfo(str),
            ),
            (
                "new_private_virtual_interface_allocation",
                "newPrivateVirtualInterfaceAllocation",
                TypeInfo(NewPrivateVirtualInterfaceAllocation),
            ),
        ]

    # The connection ID on which the private virtual interface is provisioned.

    # Default: None
    connection_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The AWS account that will own the new private virtual interface.

    # Default: None
    owner_account: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Detailed information for the private virtual interface to be provisioned.

    # Default: None
    new_private_virtual_interface_allocation: "NewPrivateVirtualInterfaceAllocation" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AllocatePublicVirtualInterfaceRequest(ShapeBase):
    """
    Container for the parameters to the AllocatePublicVirtualInterface operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "connection_id",
                "connectionId",
                TypeInfo(str),
            ),
            (
                "owner_account",
                "ownerAccount",
                TypeInfo(str),
            ),
            (
                "new_public_virtual_interface_allocation",
                "newPublicVirtualInterfaceAllocation",
                TypeInfo(NewPublicVirtualInterfaceAllocation),
            ),
        ]

    # The connection ID on which the public virtual interface is provisioned.

    # Default: None
    connection_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The AWS account that will own the new public virtual interface.

    # Default: None
    owner_account: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Detailed information for the public virtual interface to be provisioned.

    # Default: None
    new_public_virtual_interface_allocation: "NewPublicVirtualInterfaceAllocation" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AssociateConnectionWithLagRequest(ShapeBase):
    """
    Container for the parameters to the AssociateConnectionWithLag operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "connection_id",
                "connectionId",
                TypeInfo(str),
            ),
            (
                "lag_id",
                "lagId",
                TypeInfo(str),
            ),
        ]

    # The ID of the connection.

    # Example: dxcon-abc123

    # Default: None
    connection_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the LAG with which to associate the connection.

    # Example: dxlag-abc123

    # Default: None
    lag_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AssociateHostedConnectionRequest(ShapeBase):
    """
    Container for the parameters to the AssociateHostedConnection operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "connection_id",
                "connectionId",
                TypeInfo(str),
            ),
            (
                "parent_connection_id",
                "parentConnectionId",
                TypeInfo(str),
            ),
        ]

    # The ID of the hosted connection.

    # Example: dxcon-abc123

    # Default: None
    connection_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the interconnect or the LAG.

    # Example: dxcon-abc123 or dxlag-abc123

    # Default: None
    parent_connection_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AssociateVirtualInterfaceRequest(ShapeBase):
    """
    Container for the parameters to the AssociateVirtualInterface operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "virtual_interface_id",
                "virtualInterfaceId",
                TypeInfo(str),
            ),
            (
                "connection_id",
                "connectionId",
                TypeInfo(str),
            ),
        ]

    # The ID of the virtual interface.

    # Example: dxvif-123dfg56

    # Default: None
    virtual_interface_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the LAG or connection with which to associate the virtual
    # interface.

    # Example: dxlag-abc123 or dxcon-abc123

    # Default: None
    connection_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class BGPPeer(ShapeBase):
    """
    A structure containing information about a BGP peer.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "asn",
                "asn",
                TypeInfo(int),
            ),
            (
                "auth_key",
                "authKey",
                TypeInfo(str),
            ),
            (
                "address_family",
                "addressFamily",
                TypeInfo(typing.Union[str, AddressFamily]),
            ),
            (
                "amazon_address",
                "amazonAddress",
                TypeInfo(str),
            ),
            (
                "customer_address",
                "customerAddress",
                TypeInfo(str),
            ),
            (
                "bgp_peer_state",
                "bgpPeerState",
                TypeInfo(typing.Union[str, BGPPeerState]),
            ),
            (
                "bgp_status",
                "bgpStatus",
                TypeInfo(typing.Union[str, BGPStatus]),
            ),
            (
                "aws_device_v2",
                "awsDeviceV2",
                TypeInfo(str),
            ),
        ]

    # The autonomous system (AS) number for Border Gateway Protocol (BGP)
    # configuration.

    # Example: 65000
    asn: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The authentication key for BGP configuration.

    # Example: asdf34example
    auth_key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates the address family for the BGP peer.

    #   * **ipv4** : IPv4 address family

    #   * **ipv6** : IPv6 address family
    address_family: typing.Union[str, "AddressFamily"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # IP address assigned to the Amazon interface.

    # Example: 192.168.1.1/30 or 2001:db8::1/125
    amazon_address: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # IP address assigned to the customer interface.

    # Example: 192.168.1.2/30 or 2001:db8::2/125
    customer_address: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The state of the BGP peer.

    #   * **Verifying** : The BGP peering addresses or ASN require validation before the BGP peer can be created. This state only applies to BGP peers on a public virtual interface.

    #   * **Pending** : The BGP peer has been created, and is in this state until it is ready to be established.

    #   * **Available** : The BGP peer can be established.

    #   * **Deleting** : The BGP peer is in the process of being deleted.

    #   * **Deleted** : The BGP peer has been deleted and cannot be established.
    bgp_peer_state: typing.Union[str, "BGPPeerState"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Up/Down state of the BGP peer.

    #   * **Up** : The BGP peer is established.

    # A state of `up` does not indicate the state of the routing function. Ensure
    # that you are receiving routes over the BGP session.

    #   * **Down** : The BGP peer is down.
    bgp_status: typing.Union[str, "BGPStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Direct Connection endpoint which the BGP peer terminates on.
    aws_device_v2: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class BGPPeerState(str):
    """
    The state of the BGP peer.

      * **Verifying** : The BGP peering addresses or ASN require validation before the BGP peer can be created. This state only applies to BGP peers on a public virtual interface. 

      * **Pending** : The BGP peer has been created, and is in this state until it is ready to be established.

      * **Available** : The BGP peer can be established.

      * **Deleting** : The BGP peer is in the process of being deleted.

      * **Deleted** : The BGP peer has been deleted and cannot be established.
    """
    verifying = "verifying"
    pending = "pending"
    available = "available"
    deleting = "deleting"
    deleted = "deleted"


class BGPStatus(str):
    """
    The Up/Down state of the BGP peer.

      * **Up** : The BGP peer is established.

    A state of `up` does not indicate the state of the routing function. Ensure that
    you are receiving routes over the BGP session.

      * **Down** : The BGP peer is down.
    """
    up = "up"
    down = "down"


@dataclasses.dataclass
class ConfirmConnectionRequest(ShapeBase):
    """
    Container for the parameters to the ConfirmConnection operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "connection_id",
                "connectionId",
                TypeInfo(str),
            ),
        ]

    # The ID of the connection. This field is also used as the ID type for
    # operations that use multiple connection types (LAG, interconnect, and/or
    # connection).

    # Example: dxcon-fg5678gh

    # Default: None
    connection_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ConfirmConnectionResponse(OutputShapeBase):
    """
    The response received when ConfirmConnection is called.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "connection_state",
                "connectionState",
                TypeInfo(typing.Union[str, ConnectionState]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # State of the connection.

    #   * **Ordering** : The initial state of a hosted connection provisioned on an interconnect. The connection stays in the ordering state until the owner of the hosted connection confirms or declines the connection order.

    #   * **Requested** : The initial state of a standard connection. The connection stays in the requested state until the Letter of Authorization (LOA) is sent to the customer.

    #   * **Pending** : The connection has been approved, and is being initialized.

    #   * **Available** : The network link is up, and the connection is ready for use.

    #   * **Down** : The network link is down.

    #   * **Deleting** : The connection is in the process of being deleted.

    #   * **Deleted** : The connection has been deleted.

    #   * **Rejected** : A hosted connection in the 'Ordering' state will enter the 'Rejected' state if it is deleted by the end customer.
    connection_state: typing.Union[str, "ConnectionState"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ConfirmPrivateVirtualInterfaceRequest(ShapeBase):
    """
    Container for the parameters to the ConfirmPrivateVirtualInterface operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "virtual_interface_id",
                "virtualInterfaceId",
                TypeInfo(str),
            ),
            (
                "virtual_gateway_id",
                "virtualGatewayId",
                TypeInfo(str),
            ),
            (
                "direct_connect_gateway_id",
                "directConnectGatewayId",
                TypeInfo(str),
            ),
        ]

    # The ID of the virtual interface.

    # Example: dxvif-123dfg56

    # Default: None
    virtual_interface_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # ID of the virtual private gateway that will be attached to the virtual
    # interface.

    # A virtual private gateway can be managed via the Amazon Virtual Private
    # Cloud (VPC) console or the [EC2
    # CreateVpnGateway](http://docs.aws.amazon.com/AWSEC2/latest/APIReference/ApiReference-
    # query-CreateVpnGateway.html) action.

    # Default: None
    virtual_gateway_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # ID of the direct connect gateway that will be attached to the virtual
    # interface.

    # A direct connect gateway can be managed via the AWS Direct Connect console
    # or the CreateDirectConnectGateway action.

    # Default: None
    direct_connect_gateway_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ConfirmPrivateVirtualInterfaceResponse(OutputShapeBase):
    """
    The response received when ConfirmPrivateVirtualInterface is called.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "virtual_interface_state",
                "virtualInterfaceState",
                TypeInfo(typing.Union[str, VirtualInterfaceState]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # State of the virtual interface.

    #   * **Confirming** : The creation of the virtual interface is pending confirmation from the virtual interface owner. If the owner of the virtual interface is different from the owner of the connection on which it is provisioned, then the virtual interface will remain in this state until it is confirmed by the virtual interface owner.

    #   * **Verifying** : This state only applies to public virtual interfaces. Each public virtual interface needs validation before the virtual interface can be created.

    #   * **Pending** : A virtual interface is in this state from the time that it is created until the virtual interface is ready to forward traffic.

    #   * **Available** : A virtual interface that is able to forward traffic.

    #   * **Down** : A virtual interface that is BGP down.

    #   * **Deleting** : A virtual interface is in this state immediately after calling DeleteVirtualInterface until it can no longer forward traffic.

    #   * **Deleted** : A virtual interface that cannot forward traffic.

    #   * **Rejected** : The virtual interface owner has declined creation of the virtual interface. If a virtual interface in the 'Confirming' state is deleted by the virtual interface owner, the virtual interface will enter the 'Rejected' state.
    virtual_interface_state: typing.Union[str, "VirtualInterfaceState"
                                         ] = dataclasses.field(
                                             default=ShapeBase.NOT_SET,
                                         )


@dataclasses.dataclass
class ConfirmPublicVirtualInterfaceRequest(ShapeBase):
    """
    Container for the parameters to the ConfirmPublicVirtualInterface operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "virtual_interface_id",
                "virtualInterfaceId",
                TypeInfo(str),
            ),
        ]

    # The ID of the virtual interface.

    # Example: dxvif-123dfg56

    # Default: None
    virtual_interface_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ConfirmPublicVirtualInterfaceResponse(OutputShapeBase):
    """
    The response received when ConfirmPublicVirtualInterface is called.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "virtual_interface_state",
                "virtualInterfaceState",
                TypeInfo(typing.Union[str, VirtualInterfaceState]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # State of the virtual interface.

    #   * **Confirming** : The creation of the virtual interface is pending confirmation from the virtual interface owner. If the owner of the virtual interface is different from the owner of the connection on which it is provisioned, then the virtual interface will remain in this state until it is confirmed by the virtual interface owner.

    #   * **Verifying** : This state only applies to public virtual interfaces. Each public virtual interface needs validation before the virtual interface can be created.

    #   * **Pending** : A virtual interface is in this state from the time that it is created until the virtual interface is ready to forward traffic.

    #   * **Available** : A virtual interface that is able to forward traffic.

    #   * **Down** : A virtual interface that is BGP down.

    #   * **Deleting** : A virtual interface is in this state immediately after calling DeleteVirtualInterface until it can no longer forward traffic.

    #   * **Deleted** : A virtual interface that cannot forward traffic.

    #   * **Rejected** : The virtual interface owner has declined creation of the virtual interface. If a virtual interface in the 'Confirming' state is deleted by the virtual interface owner, the virtual interface will enter the 'Rejected' state.
    virtual_interface_state: typing.Union[str, "VirtualInterfaceState"
                                         ] = dataclasses.field(
                                             default=ShapeBase.NOT_SET,
                                         )


@dataclasses.dataclass
class Connection(OutputShapeBase):
    """
    A connection represents the physical network connection between the AWS Direct
    Connect location and the customer.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "owner_account",
                "ownerAccount",
                TypeInfo(str),
            ),
            (
                "connection_id",
                "connectionId",
                TypeInfo(str),
            ),
            (
                "connection_name",
                "connectionName",
                TypeInfo(str),
            ),
            (
                "connection_state",
                "connectionState",
                TypeInfo(typing.Union[str, ConnectionState]),
            ),
            (
                "region",
                "region",
                TypeInfo(str),
            ),
            (
                "location",
                "location",
                TypeInfo(str),
            ),
            (
                "bandwidth",
                "bandwidth",
                TypeInfo(str),
            ),
            (
                "vlan",
                "vlan",
                TypeInfo(int),
            ),
            (
                "partner_name",
                "partnerName",
                TypeInfo(str),
            ),
            (
                "loa_issue_time",
                "loaIssueTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "lag_id",
                "lagId",
                TypeInfo(str),
            ),
            (
                "aws_device",
                "awsDevice",
                TypeInfo(str),
            ),
            (
                "aws_device_v2",
                "awsDeviceV2",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The AWS account that will own the new connection.
    owner_account: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the connection. This field is also used as the ID type for
    # operations that use multiple connection types (LAG, interconnect, and/or
    # connection).

    # Example: dxcon-fg5678gh

    # Default: None
    connection_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the connection.

    # Example: " _My Connection to AWS_ "

    # Default: None
    connection_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # State of the connection.

    #   * **Ordering** : The initial state of a hosted connection provisioned on an interconnect. The connection stays in the ordering state until the owner of the hosted connection confirms or declines the connection order.

    #   * **Requested** : The initial state of a standard connection. The connection stays in the requested state until the Letter of Authorization (LOA) is sent to the customer.

    #   * **Pending** : The connection has been approved, and is being initialized.

    #   * **Available** : The network link is up, and the connection is ready for use.

    #   * **Down** : The network link is down.

    #   * **Deleting** : The connection is in the process of being deleted.

    #   * **Deleted** : The connection has been deleted.

    #   * **Rejected** : A hosted connection in the 'Ordering' state will enter the 'Rejected' state if it is deleted by the end customer.
    connection_state: typing.Union[str, "ConnectionState"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The AWS region where the connection is located.

    # Example: us-east-1

    # Default: None
    region: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Where the connection is located.

    # Example: EqSV5

    # Default: None
    location: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Bandwidth of the connection.

    # Example: 1Gbps (for regular connections), or 500Mbps (for hosted
    # connections)

    # Default: None
    bandwidth: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The VLAN ID.

    # Example: 101
    vlan: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the AWS Direct Connect service provider associated with the
    # connection.
    partner_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time of the most recent call to DescribeLoa for this connection.
    loa_issue_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID of the LAG.

    # Example: dxlag-fg5678gh
    lag_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Deprecated in favor of awsDeviceV2.

    # The Direct Connection endpoint which the physical connection terminates on.
    aws_device: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Direct Connection endpoint which the physical connection terminates on.
    aws_device_v2: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class ConnectionState(str):
    """
    State of the connection.

      * **Ordering** : The initial state of a hosted connection provisioned on an interconnect. The connection stays in the ordering state until the owner of the hosted connection confirms or declines the connection order.

      * **Requested** : The initial state of a standard connection. The connection stays in the requested state until the Letter of Authorization (LOA) is sent to the customer.

      * **Pending** : The connection has been approved, and is being initialized.

      * **Available** : The network link is up, and the connection is ready for use.

      * **Down** : The network link is down.

      * **Deleting** : The connection is in the process of being deleted.

      * **Deleted** : The connection has been deleted.

      * **Rejected** : A hosted connection in the 'Ordering' state will enter the 'Rejected' state if it is deleted by the end customer.
    """
    ordering = "ordering"
    requested = "requested"
    pending = "pending"
    available = "available"
    down = "down"
    deleting = "deleting"
    deleted = "deleted"
    rejected = "rejected"


@dataclasses.dataclass
class Connections(OutputShapeBase):
    """
    A structure containing a list of connections.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "connections",
                "connections",
                TypeInfo(typing.List[Connection]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of connections.
    connections: typing.List["Connection"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateBGPPeerRequest(ShapeBase):
    """
    Container for the parameters to the CreateBGPPeer operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "virtual_interface_id",
                "virtualInterfaceId",
                TypeInfo(str),
            ),
            (
                "new_bgp_peer",
                "newBGPPeer",
                TypeInfo(NewBGPPeer),
            ),
        ]

    # The ID of the virtual interface on which the BGP peer will be provisioned.

    # Example: dxvif-456abc78

    # Default: None
    virtual_interface_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Detailed information for the BGP peer to be created.

    # Default: None
    new_bgp_peer: "NewBGPPeer" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateBGPPeerResponse(OutputShapeBase):
    """
    The response received when CreateBGPPeer is called.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "virtual_interface",
                "virtualInterface",
                TypeInfo(VirtualInterface),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A virtual interface (VLAN) transmits the traffic between the AWS Direct
    # Connect location and the customer.
    virtual_interface: "VirtualInterface" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateConnectionRequest(ShapeBase):
    """
    Container for the parameters to the CreateConnection operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "location",
                "location",
                TypeInfo(str),
            ),
            (
                "bandwidth",
                "bandwidth",
                TypeInfo(str),
            ),
            (
                "connection_name",
                "connectionName",
                TypeInfo(str),
            ),
            (
                "lag_id",
                "lagId",
                TypeInfo(str),
            ),
        ]

    # Where the connection is located.

    # Example: EqSV5

    # Default: None
    location: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Bandwidth of the connection.

    # Example: 1Gbps

    # Default: None
    bandwidth: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the connection.

    # Example: " _My Connection to AWS_ "

    # Default: None
    connection_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the LAG.

    # Example: dxlag-fg5678gh
    lag_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateDirectConnectGatewayAssociationRequest(ShapeBase):
    """
    Container for the parameters to the CreateDirectConnectGatewayAssociation
    operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "direct_connect_gateway_id",
                "directConnectGatewayId",
                TypeInfo(str),
            ),
            (
                "virtual_gateway_id",
                "virtualGatewayId",
                TypeInfo(str),
            ),
        ]

    # The ID of the direct connect gateway.

    # Example: "abcd1234-dcba-5678-be23-cdef9876ab45"

    # Default: None
    direct_connect_gateway_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID of the virtual private gateway.

    # Example: "vgw-abc123ef"

    # Default: None
    virtual_gateway_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateDirectConnectGatewayAssociationResult(OutputShapeBase):
    """
    Container for the response from the CreateDirectConnectGatewayAssociation API
    call
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "direct_connect_gateway_association",
                "directConnectGatewayAssociation",
                TypeInfo(DirectConnectGatewayAssociation),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The direct connect gateway association to be created.
    direct_connect_gateway_association: "DirectConnectGatewayAssociation" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateDirectConnectGatewayRequest(ShapeBase):
    """
    Container for the parameters to the CreateDirectConnectGateway operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "direct_connect_gateway_name",
                "directConnectGatewayName",
                TypeInfo(str),
            ),
            (
                "amazon_side_asn",
                "amazonSideAsn",
                TypeInfo(int),
            ),
        ]

    # The name of the direct connect gateway.

    # Example: "My direct connect gateway"

    # Default: None
    direct_connect_gateway_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The autonomous system number (ASN) for Border Gateway Protocol (BGP) to be
    # configured on the Amazon side of the connection. The ASN must be in the
    # private range of 64,512 to 65,534 or 4,200,000,000 to 4,294,967,294

    # Example: 65200

    # Default: 64512
    amazon_side_asn: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateDirectConnectGatewayResult(OutputShapeBase):
    """
    Container for the response from the CreateDirectConnectGateway API call
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "direct_connect_gateway",
                "directConnectGateway",
                TypeInfo(DirectConnectGateway),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The direct connect gateway to be created.
    direct_connect_gateway: "DirectConnectGateway" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateInterconnectRequest(ShapeBase):
    """
    Container for the parameters to the CreateInterconnect operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "interconnect_name",
                "interconnectName",
                TypeInfo(str),
            ),
            (
                "bandwidth",
                "bandwidth",
                TypeInfo(str),
            ),
            (
                "location",
                "location",
                TypeInfo(str),
            ),
            (
                "lag_id",
                "lagId",
                TypeInfo(str),
            ),
        ]

    # The name of the interconnect.

    # Example: " _1G Interconnect to AWS_ "

    # Default: None
    interconnect_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The port bandwidth

    # Example: 1Gbps

    # Default: None

    # Available values: 1Gbps,10Gbps
    bandwidth: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Where the interconnect is located

    # Example: EqSV5

    # Default: None
    location: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the LAG.

    # Example: dxlag-fg5678gh
    lag_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateLagRequest(ShapeBase):
    """
    Container for the parameters to the CreateLag operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "number_of_connections",
                "numberOfConnections",
                TypeInfo(int),
            ),
            (
                "location",
                "location",
                TypeInfo(str),
            ),
            (
                "connections_bandwidth",
                "connectionsBandwidth",
                TypeInfo(str),
            ),
            (
                "lag_name",
                "lagName",
                TypeInfo(str),
            ),
            (
                "connection_id",
                "connectionId",
                TypeInfo(str),
            ),
        ]

    # The number of physical connections initially provisioned and bundled by the
    # LAG.

    # Default: None
    number_of_connections: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The AWS Direct Connect location in which the LAG should be allocated.

    # Example: EqSV5

    # Default: None
    location: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The bandwidth of the individual physical connections bundled by the LAG.

    # Default: None

    # Available values: 1Gbps, 10Gbps
    connections_bandwidth: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the LAG.

    # Example: "`3x10G LAG to AWS`"

    # Default: None
    lag_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of an existing connection to migrate to the LAG.

    # Default: None
    connection_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreatePrivateVirtualInterfaceRequest(ShapeBase):
    """
    Container for the parameters to the CreatePrivateVirtualInterface operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "connection_id",
                "connectionId",
                TypeInfo(str),
            ),
            (
                "new_private_virtual_interface",
                "newPrivateVirtualInterface",
                TypeInfo(NewPrivateVirtualInterface),
            ),
        ]

    # The ID of the connection. This field is also used as the ID type for
    # operations that use multiple connection types (LAG, interconnect, and/or
    # connection).

    # Example: dxcon-fg5678gh

    # Default: None
    connection_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Detailed information for the private virtual interface to be created.

    # Default: None
    new_private_virtual_interface: "NewPrivateVirtualInterface" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreatePublicVirtualInterfaceRequest(ShapeBase):
    """
    Container for the parameters to the CreatePublicVirtualInterface operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "connection_id",
                "connectionId",
                TypeInfo(str),
            ),
            (
                "new_public_virtual_interface",
                "newPublicVirtualInterface",
                TypeInfo(NewPublicVirtualInterface),
            ),
        ]

    # The ID of the connection. This field is also used as the ID type for
    # operations that use multiple connection types (LAG, interconnect, and/or
    # connection).

    # Example: dxcon-fg5678gh

    # Default: None
    connection_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Detailed information for the public virtual interface to be created.

    # Default: None
    new_public_virtual_interface: "NewPublicVirtualInterface" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteBGPPeerRequest(ShapeBase):
    """
    Container for the parameters to the DeleteBGPPeer operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "virtual_interface_id",
                "virtualInterfaceId",
                TypeInfo(str),
            ),
            (
                "asn",
                "asn",
                TypeInfo(int),
            ),
            (
                "customer_address",
                "customerAddress",
                TypeInfo(str),
            ),
        ]

    # The ID of the virtual interface from which the BGP peer will be deleted.

    # Example: dxvif-456abc78

    # Default: None
    virtual_interface_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The autonomous system (AS) number for Border Gateway Protocol (BGP)
    # configuration.

    # Example: 65000
    asn: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # IP address assigned to the customer interface.

    # Example: 192.168.1.2/30 or 2001:db8::2/125
    customer_address: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteBGPPeerResponse(OutputShapeBase):
    """
    The response received when DeleteBGPPeer is called.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "virtual_interface",
                "virtualInterface",
                TypeInfo(VirtualInterface),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A virtual interface (VLAN) transmits the traffic between the AWS Direct
    # Connect location and the customer.
    virtual_interface: "VirtualInterface" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteConnectionRequest(ShapeBase):
    """
    Container for the parameters to the DeleteConnection operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "connection_id",
                "connectionId",
                TypeInfo(str),
            ),
        ]

    # The ID of the connection. This field is also used as the ID type for
    # operations that use multiple connection types (LAG, interconnect, and/or
    # connection).

    # Example: dxcon-fg5678gh

    # Default: None
    connection_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteDirectConnectGatewayAssociationRequest(ShapeBase):
    """
    Container for the parameters to the DeleteDirectConnectGatewayAssociation
    operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "direct_connect_gateway_id",
                "directConnectGatewayId",
                TypeInfo(str),
            ),
            (
                "virtual_gateway_id",
                "virtualGatewayId",
                TypeInfo(str),
            ),
        ]

    # The ID of the direct connect gateway.

    # Example: "abcd1234-dcba-5678-be23-cdef9876ab45"

    # Default: None
    direct_connect_gateway_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID of the virtual private gateway.

    # Example: "vgw-abc123ef"

    # Default: None
    virtual_gateway_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteDirectConnectGatewayAssociationResult(OutputShapeBase):
    """
    Container for the response from the DeleteDirectConnectGatewayAssociation API
    call
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "direct_connect_gateway_association",
                "directConnectGatewayAssociation",
                TypeInfo(DirectConnectGatewayAssociation),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The direct connect gateway association to be deleted.
    direct_connect_gateway_association: "DirectConnectGatewayAssociation" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteDirectConnectGatewayRequest(ShapeBase):
    """
    Container for the parameters to the DeleteDirectConnectGateway operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "direct_connect_gateway_id",
                "directConnectGatewayId",
                TypeInfo(str),
            ),
        ]

    # The ID of the direct connect gateway.

    # Example: "abcd1234-dcba-5678-be23-cdef9876ab45"

    # Default: None
    direct_connect_gateway_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteDirectConnectGatewayResult(OutputShapeBase):
    """
    Container for the response from the DeleteDirectConnectGateway API call
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "direct_connect_gateway",
                "directConnectGateway",
                TypeInfo(DirectConnectGateway),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The direct connect gateway to be deleted.
    direct_connect_gateway: "DirectConnectGateway" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteInterconnectRequest(ShapeBase):
    """
    Container for the parameters to the DeleteInterconnect operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "interconnect_id",
                "interconnectId",
                TypeInfo(str),
            ),
        ]

    # The ID of the interconnect.

    # Example: dxcon-abc123
    interconnect_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteInterconnectResponse(OutputShapeBase):
    """
    The response received when DeleteInterconnect is called.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "interconnect_state",
                "interconnectState",
                TypeInfo(typing.Union[str, InterconnectState]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # State of the interconnect.

    #   * **Requested** : The initial state of an interconnect. The interconnect stays in the requested state until the Letter of Authorization (LOA) is sent to the customer.

    #   * **Pending** : The interconnect has been approved, and is being initialized.

    #   * **Available** : The network link is up, and the interconnect is ready for use.

    #   * **Down** : The network link is down.

    #   * **Deleting** : The interconnect is in the process of being deleted.

    #   * **Deleted** : The interconnect has been deleted.
    interconnect_state: typing.Union[str, "InterconnectState"
                                    ] = dataclasses.field(
                                        default=ShapeBase.NOT_SET,
                                    )


@dataclasses.dataclass
class DeleteLagRequest(ShapeBase):
    """
    Container for the parameters to the DeleteLag operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "lag_id",
                "lagId",
                TypeInfo(str),
            ),
        ]

    # The ID of the LAG to delete.

    # Example: dxlag-abc123

    # Default: None
    lag_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteVirtualInterfaceRequest(ShapeBase):
    """
    Container for the parameters to the DeleteVirtualInterface operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "virtual_interface_id",
                "virtualInterfaceId",
                TypeInfo(str),
            ),
        ]

    # The ID of the virtual interface.

    # Example: dxvif-123dfg56

    # Default: None
    virtual_interface_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteVirtualInterfaceResponse(OutputShapeBase):
    """
    The response received when DeleteVirtualInterface is called.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "virtual_interface_state",
                "virtualInterfaceState",
                TypeInfo(typing.Union[str, VirtualInterfaceState]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # State of the virtual interface.

    #   * **Confirming** : The creation of the virtual interface is pending confirmation from the virtual interface owner. If the owner of the virtual interface is different from the owner of the connection on which it is provisioned, then the virtual interface will remain in this state until it is confirmed by the virtual interface owner.

    #   * **Verifying** : This state only applies to public virtual interfaces. Each public virtual interface needs validation before the virtual interface can be created.

    #   * **Pending** : A virtual interface is in this state from the time that it is created until the virtual interface is ready to forward traffic.

    #   * **Available** : A virtual interface that is able to forward traffic.

    #   * **Down** : A virtual interface that is BGP down.

    #   * **Deleting** : A virtual interface is in this state immediately after calling DeleteVirtualInterface until it can no longer forward traffic.

    #   * **Deleted** : A virtual interface that cannot forward traffic.

    #   * **Rejected** : The virtual interface owner has declined creation of the virtual interface. If a virtual interface in the 'Confirming' state is deleted by the virtual interface owner, the virtual interface will enter the 'Rejected' state.
    virtual_interface_state: typing.Union[str, "VirtualInterfaceState"
                                         ] = dataclasses.field(
                                             default=ShapeBase.NOT_SET,
                                         )


@dataclasses.dataclass
class DescribeConnectionLoaRequest(ShapeBase):
    """
    Container for the parameters to the DescribeConnectionLoa operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "connection_id",
                "connectionId",
                TypeInfo(str),
            ),
            (
                "provider_name",
                "providerName",
                TypeInfo(str),
            ),
            (
                "loa_content_type",
                "loaContentType",
                TypeInfo(typing.Union[str, LoaContentType]),
            ),
        ]

    # The ID of the connection. This field is also used as the ID type for
    # operations that use multiple connection types (LAG, interconnect, and/or
    # connection).

    # Example: dxcon-fg5678gh

    # Default: None
    connection_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the APN partner or service provider who establishes
    # connectivity on your behalf. If you supply this parameter, the LOA-CFA
    # lists the provider name alongside your company name as the requester of the
    # cross connect.

    # Default: None
    provider_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A standard media type indicating the content type of the LOA-CFA document.
    # Currently, the only supported value is "application/pdf".

    # Default: application/pdf
    loa_content_type: typing.Union[str, "LoaContentType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeConnectionLoaResponse(OutputShapeBase):
    """
    The response received when DescribeConnectionLoa is called.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "loa",
                "loa",
                TypeInfo(Loa),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A structure containing the Letter of Authorization - Connecting Facility
    # Assignment (LOA-CFA) for a connection.
    loa: "Loa" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeConnectionsOnInterconnectRequest(ShapeBase):
    """
    Container for the parameters to the DescribeConnectionsOnInterconnect operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "interconnect_id",
                "interconnectId",
                TypeInfo(str),
            ),
        ]

    # ID of the interconnect on which a list of connection is provisioned.

    # Example: dxcon-abc123

    # Default: None
    interconnect_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeConnectionsRequest(ShapeBase):
    """
    Container for the parameters to the DescribeConnections operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "connection_id",
                "connectionId",
                TypeInfo(str),
            ),
        ]

    # The ID of the connection. This field is also used as the ID type for
    # operations that use multiple connection types (LAG, interconnect, and/or
    # connection).

    # Example: dxcon-fg5678gh

    # Default: None
    connection_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeDirectConnectGatewayAssociationsRequest(ShapeBase):
    """
    Container for the parameters to the DescribeDirectConnectGatewayAssociations
    operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "direct_connect_gateway_id",
                "directConnectGatewayId",
                TypeInfo(str),
            ),
            (
                "virtual_gateway_id",
                "virtualGatewayId",
                TypeInfo(str),
            ),
            (
                "max_results",
                "maxResults",
                TypeInfo(int),
            ),
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
        ]

    # The ID of the direct connect gateway.

    # Example: "abcd1234-dcba-5678-be23-cdef9876ab45"

    # Default: None
    direct_connect_gateway_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID of the virtual private gateway.

    # Example: "vgw-abc123ef"

    # Default: None
    virtual_gateway_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of direct connect gateway associations to return per
    # page.

    # Example: 15

    # Default: None
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The token provided in the previous describe result to retrieve the next
    # page of the result.

    # Default: None
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeDirectConnectGatewayAssociationsResult(OutputShapeBase):
    """
    Container for the response from the DescribeDirectConnectGatewayAssociations API
    call
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "direct_connect_gateway_associations",
                "directConnectGatewayAssociations",
                TypeInfo(typing.List[DirectConnectGatewayAssociation]),
            ),
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the direct connect gateway associations.
    direct_connect_gateway_associations: typing.List[
        "DirectConnectGatewayAssociation"] = dataclasses.field(
            default=ShapeBase.NOT_SET,
        )

    # Token to retrieve the next page of the result.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeDirectConnectGatewayAttachmentsRequest(ShapeBase):
    """
    Container for the parameters to the DescribeDirectConnectGatewayAttachments
    operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "direct_connect_gateway_id",
                "directConnectGatewayId",
                TypeInfo(str),
            ),
            (
                "virtual_interface_id",
                "virtualInterfaceId",
                TypeInfo(str),
            ),
            (
                "max_results",
                "maxResults",
                TypeInfo(int),
            ),
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
        ]

    # The ID of the direct connect gateway.

    # Example: "abcd1234-dcba-5678-be23-cdef9876ab45"

    # Default: None
    direct_connect_gateway_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID of the virtual interface.

    # Example: "dxvif-abc123ef"

    # Default: None
    virtual_interface_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of direct connect gateway attachments to return per
    # page.

    # Example: 15

    # Default: None
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The token provided in the previous describe result to retrieve the next
    # page of the result.

    # Default: None
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeDirectConnectGatewayAttachmentsResult(OutputShapeBase):
    """
    Container for the response from the DescribeDirectConnectGatewayAttachments API
    call
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "direct_connect_gateway_attachments",
                "directConnectGatewayAttachments",
                TypeInfo(typing.List[DirectConnectGatewayAttachment]),
            ),
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the direct connect gateway attachments.
    direct_connect_gateway_attachments: typing.List[
        "DirectConnectGatewayAttachment"] = dataclasses.field(
            default=ShapeBase.NOT_SET,
        )

    # Token to retrieve the next page of the result.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeDirectConnectGatewaysRequest(ShapeBase):
    """
    Container for the parameters to the DescribeDirectConnectGateways operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "direct_connect_gateway_id",
                "directConnectGatewayId",
                TypeInfo(str),
            ),
            (
                "max_results",
                "maxResults",
                TypeInfo(int),
            ),
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
        ]

    # The ID of the direct connect gateway.

    # Example: "abcd1234-dcba-5678-be23-cdef9876ab45"

    # Default: None
    direct_connect_gateway_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The maximum number of direct connect gateways to return per page.

    # Example: 15

    # Default: None
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The token provided in the previous describe result to retrieve the next
    # page of the result.

    # Default: None
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeDirectConnectGatewaysResult(OutputShapeBase):
    """
    Container for the response from the DescribeDirectConnectGateways API call
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "direct_connect_gateways",
                "directConnectGateways",
                TypeInfo(typing.List[DirectConnectGateway]),
            ),
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the direct connect gateways.
    direct_connect_gateways: typing.List["DirectConnectGateway"
                                        ] = dataclasses.field(
                                            default=ShapeBase.NOT_SET,
                                        )

    # Token to retrieve the next page of the result.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeHostedConnectionsRequest(ShapeBase):
    """
    Container for the parameters to the DescribeHostedConnections operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "connection_id",
                "connectionId",
                TypeInfo(str),
            ),
        ]

    # The ID of the interconnect or LAG on which the hosted connections are
    # provisioned.

    # Example: dxcon-abc123 or dxlag-abc123

    # Default: None
    connection_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeInterconnectLoaRequest(ShapeBase):
    """
    Container for the parameters to the DescribeInterconnectLoa operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "interconnect_id",
                "interconnectId",
                TypeInfo(str),
            ),
            (
                "provider_name",
                "providerName",
                TypeInfo(str),
            ),
            (
                "loa_content_type",
                "loaContentType",
                TypeInfo(typing.Union[str, LoaContentType]),
            ),
        ]

    # The ID of the interconnect.

    # Example: dxcon-abc123
    interconnect_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the service provider who establishes connectivity on your
    # behalf. If you supply this parameter, the LOA-CFA lists the provider name
    # alongside your company name as the requester of the cross connect.

    # Default: None
    provider_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A standard media type indicating the content type of the LOA-CFA document.
    # Currently, the only supported value is "application/pdf".

    # Default: application/pdf
    loa_content_type: typing.Union[str, "LoaContentType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeInterconnectLoaResponse(OutputShapeBase):
    """
    The response received when DescribeInterconnectLoa is called.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "loa",
                "loa",
                TypeInfo(Loa),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A structure containing the Letter of Authorization - Connecting Facility
    # Assignment (LOA-CFA) for a connection.
    loa: "Loa" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeInterconnectsRequest(ShapeBase):
    """
    Container for the parameters to the DescribeInterconnects operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "interconnect_id",
                "interconnectId",
                TypeInfo(str),
            ),
        ]

    # The ID of the interconnect.

    # Example: dxcon-abc123
    interconnect_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeLagsRequest(ShapeBase):
    """
    Container for the parameters to the DescribeLags operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "lag_id",
                "lagId",
                TypeInfo(str),
            ),
        ]

    # The ID of the LAG.

    # Example: dxlag-abc123

    # Default: None
    lag_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeLoaRequest(ShapeBase):
    """
    Container for the parameters to the DescribeLoa operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "connection_id",
                "connectionId",
                TypeInfo(str),
            ),
            (
                "provider_name",
                "providerName",
                TypeInfo(str),
            ),
            (
                "loa_content_type",
                "loaContentType",
                TypeInfo(typing.Union[str, LoaContentType]),
            ),
        ]

    # The ID of a connection, LAG, or interconnect for which to get the LOA-CFA
    # information.

    # Example: dxcon-abc123 or dxlag-abc123

    # Default: None
    connection_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the service provider who establishes connectivity on your
    # behalf. If you supply this parameter, the LOA-CFA lists the provider name
    # alongside your company name as the requester of the cross connect.

    # Default: None
    provider_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A standard media type indicating the content type of the LOA-CFA document.
    # Currently, the only supported value is "application/pdf".

    # Default: application/pdf
    loa_content_type: typing.Union[str, "LoaContentType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeTagsRequest(ShapeBase):
    """
    Container for the parameters to the DescribeTags operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_arns",
                "resourceArns",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The Amazon Resource Names (ARNs) of the Direct Connect resources.
    resource_arns: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeTagsResponse(OutputShapeBase):
    """
    The response received when DescribeTags is called.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "resource_tags",
                "resourceTags",
                TypeInfo(typing.List[ResourceTag]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the tags.
    resource_tags: typing.List["ResourceTag"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeVirtualInterfacesRequest(ShapeBase):
    """
    Container for the parameters to the DescribeVirtualInterfaces operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "connection_id",
                "connectionId",
                TypeInfo(str),
            ),
            (
                "virtual_interface_id",
                "virtualInterfaceId",
                TypeInfo(str),
            ),
        ]

    # The ID of the connection. This field is also used as the ID type for
    # operations that use multiple connection types (LAG, interconnect, and/or
    # connection).

    # Example: dxcon-fg5678gh

    # Default: None
    connection_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the virtual interface.

    # Example: dxvif-123dfg56

    # Default: None
    virtual_interface_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DirectConnectClientException(ShapeBase):
    """
    The API was called with invalid parameters. The error message will contain
    additional details about the cause.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    # This is an exception thrown when there is an issue with the input provided
    # by the API call. For example, the name provided for a connection contains a
    # pound sign (#). This can also occur when a valid value is provided, but is
    # otherwise constrained. For example, the valid VLAN tag range is 1-4096 but
    # each can only be used once per connection.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DirectConnectGateway(ShapeBase):
    """
    A direct connect gateway is an intermediate object that enables you to connect
    virtual interfaces and virtual private gateways.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "direct_connect_gateway_id",
                "directConnectGatewayId",
                TypeInfo(str),
            ),
            (
                "direct_connect_gateway_name",
                "directConnectGatewayName",
                TypeInfo(str),
            ),
            (
                "amazon_side_asn",
                "amazonSideAsn",
                TypeInfo(int),
            ),
            (
                "owner_account",
                "ownerAccount",
                TypeInfo(str),
            ),
            (
                "direct_connect_gateway_state",
                "directConnectGatewayState",
                TypeInfo(typing.Union[str, DirectConnectGatewayState]),
            ),
            (
                "state_change_error",
                "stateChangeError",
                TypeInfo(str),
            ),
        ]

    # The ID of the direct connect gateway.

    # Example: "abcd1234-dcba-5678-be23-cdef9876ab45"
    direct_connect_gateway_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the direct connect gateway.

    # Example: "My direct connect gateway"

    # Default: None
    direct_connect_gateway_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The autonomous system number (ASN) for the Amazon side of the connection.
    amazon_side_asn: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The AWS account ID of the owner of the direct connect gateway.
    owner_account: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # State of the direct connect gateway.

    #   * **Pending** : The initial state after calling CreateDirectConnectGateway.

    #   * **Available** : The direct connect gateway is ready for use.

    #   * **Deleting** : The initial state after calling DeleteDirectConnectGateway.

    #   * **Deleted** : The direct connect gateway is deleted and cannot pass traffic.
    direct_connect_gateway_state: typing.Union[str, "DirectConnectGatewayState"
                                              ] = dataclasses.field(
                                                  default=ShapeBase.NOT_SET,
                                              )

    # Error message when the state of an object fails to advance.
    state_change_error: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DirectConnectGatewayAssociation(ShapeBase):
    """
    The association between a direct connect gateway and virtual private gateway.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "direct_connect_gateway_id",
                "directConnectGatewayId",
                TypeInfo(str),
            ),
            (
                "virtual_gateway_id",
                "virtualGatewayId",
                TypeInfo(str),
            ),
            (
                "virtual_gateway_region",
                "virtualGatewayRegion",
                TypeInfo(str),
            ),
            (
                "virtual_gateway_owner_account",
                "virtualGatewayOwnerAccount",
                TypeInfo(str),
            ),
            (
                "association_state",
                "associationState",
                TypeInfo(
                    typing.Union[str, DirectConnectGatewayAssociationState]
                ),
            ),
            (
                "state_change_error",
                "stateChangeError",
                TypeInfo(str),
            ),
        ]

    # The ID of the direct connect gateway.

    # Example: "abcd1234-dcba-5678-be23-cdef9876ab45"
    direct_connect_gateway_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID of the virtual private gateway to a VPC. This only applies to
    # private virtual interfaces.

    # Example: vgw-123er56
    virtual_gateway_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The region in which the virtual private gateway is located.

    # Example: us-east-1
    virtual_gateway_region: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The AWS account ID of the owner of the virtual private gateway.
    virtual_gateway_owner_account: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # State of the direct connect gateway association.

    #   * **Associating** : The initial state after calling CreateDirectConnectGatewayAssociation.

    #   * **Associated** : The direct connect gateway and virtual private gateway are successfully associated and ready to pass traffic.

    #   * **Disassociating** : The initial state after calling DeleteDirectConnectGatewayAssociation.

    #   * **Disassociated** : The virtual private gateway is successfully disassociated from the direct connect gateway. Traffic flow between the direct connect gateway and virtual private gateway stops.
    association_state: typing.Union[str, "DirectConnectGatewayAssociationState"
                                   ] = dataclasses.field(
                                       default=ShapeBase.NOT_SET,
                                   )

    # Error message when the state of an object fails to advance.
    state_change_error: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class DirectConnectGatewayAssociationState(str):
    """
    State of the direct connect gateway association.

      * **Associating** : The initial state after calling CreateDirectConnectGatewayAssociation.

      * **Associated** : The direct connect gateway and virtual private gateway are successfully associated and ready to pass traffic.

      * **Disassociating** : The initial state after calling DeleteDirectConnectGatewayAssociation.

      * **Disassociated** : The virtual private gateway is successfully disassociated from the direct connect gateway. Traffic flow between the direct connect gateway and virtual private gateway stops.
    """
    associating = "associating"
    associated = "associated"
    disassociating = "disassociating"
    disassociated = "disassociated"


@dataclasses.dataclass
class DirectConnectGatewayAttachment(ShapeBase):
    """
    The association between a direct connect gateway and virtual interface.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "direct_connect_gateway_id",
                "directConnectGatewayId",
                TypeInfo(str),
            ),
            (
                "virtual_interface_id",
                "virtualInterfaceId",
                TypeInfo(str),
            ),
            (
                "virtual_interface_region",
                "virtualInterfaceRegion",
                TypeInfo(str),
            ),
            (
                "virtual_interface_owner_account",
                "virtualInterfaceOwnerAccount",
                TypeInfo(str),
            ),
            (
                "attachment_state",
                "attachmentState",
                TypeInfo(
                    typing.Union[str, DirectConnectGatewayAttachmentState]
                ),
            ),
            (
                "state_change_error",
                "stateChangeError",
                TypeInfo(str),
            ),
        ]

    # The ID of the direct connect gateway.

    # Example: "abcd1234-dcba-5678-be23-cdef9876ab45"
    direct_connect_gateway_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID of the virtual interface.

    # Example: dxvif-123dfg56

    # Default: None
    virtual_interface_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The region in which the virtual interface is located.

    # Example: us-east-1
    virtual_interface_region: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The AWS account ID of the owner of the virtual interface.
    virtual_interface_owner_account: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # State of the direct connect gateway attachment.

    #   * **Attaching** : The initial state after a virtual interface is created using the direct connect gateway.

    #   * **Attached** : The direct connect gateway and virtual interface are successfully attached and ready to pass traffic.

    #   * **Detaching** : The initial state after calling DeleteVirtualInterface on a virtual interface that is attached to a direct connect gateway.

    #   * **Detached** : The virtual interface is successfully detached from the direct connect gateway. Traffic flow between the direct connect gateway and virtual interface stops.
    attachment_state: typing.Union[str, "DirectConnectGatewayAttachmentState"
                                  ] = dataclasses.field(
                                      default=ShapeBase.NOT_SET,
                                  )

    # Error message when the state of an object fails to advance.
    state_change_error: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class DirectConnectGatewayAttachmentState(str):
    """
    State of the direct connect gateway attachment.

      * **Attaching** : The initial state after a virtual interface is created using the direct connect gateway.

      * **Attached** : The direct connect gateway and virtual interface are successfully attached and ready to pass traffic.

      * **Detaching** : The initial state after calling DeleteVirtualInterface on a virtual interface that is attached to a direct connect gateway.

      * **Detached** : The virtual interface is successfully detached from the direct connect gateway. Traffic flow between the direct connect gateway and virtual interface stops.
    """
    attaching = "attaching"
    attached = "attached"
    detaching = "detaching"
    detached = "detached"


class DirectConnectGatewayState(str):
    """
    State of the direct connect gateway.

      * **Pending** : The initial state after calling CreateDirectConnectGateway.

      * **Available** : The direct connect gateway is ready for use.

      * **Deleting** : The initial state after calling DeleteDirectConnectGateway.

      * **Deleted** : The direct connect gateway is deleted and cannot pass traffic.
    """
    pending = "pending"
    available = "available"
    deleting = "deleting"
    deleted = "deleted"


@dataclasses.dataclass
class DirectConnectServerException(ShapeBase):
    """
    A server-side error occurred during the API call. The error message will contain
    additional details about the cause.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    # This is an exception thrown when there is a backend issue on the server
    # side.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DisassociateConnectionFromLagRequest(ShapeBase):
    """
    Container for the parameters to the DisassociateConnectionFromLag operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "connection_id",
                "connectionId",
                TypeInfo(str),
            ),
            (
                "lag_id",
                "lagId",
                TypeInfo(str),
            ),
        ]

    # The ID of the connection to disassociate from the LAG.

    # Example: dxcon-abc123

    # Default: None
    connection_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the LAG.

    # Example: dxlag-abc123

    # Default: None
    lag_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DuplicateTagKeysException(ShapeBase):
    """
    A tag key was specified more than once.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class Interconnect(OutputShapeBase):
    """
    An interconnect is a connection that can host other connections.

    Like a standard AWS Direct Connect connection, an interconnect represents the
    physical connection between an AWS Direct Connect partner's network and a
    specific Direct Connect location. An AWS Direct Connect partner who owns an
    interconnect can provision hosted connections on the interconnect for their end
    customers, thereby providing the end customers with connectivity to AWS
    services.

    The resources of the interconnect, including bandwidth and VLAN numbers, are
    shared by all of the hosted connections on the interconnect, and the owner of
    the interconnect determines how these resources are assigned.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "interconnect_id",
                "interconnectId",
                TypeInfo(str),
            ),
            (
                "interconnect_name",
                "interconnectName",
                TypeInfo(str),
            ),
            (
                "interconnect_state",
                "interconnectState",
                TypeInfo(typing.Union[str, InterconnectState]),
            ),
            (
                "region",
                "region",
                TypeInfo(str),
            ),
            (
                "location",
                "location",
                TypeInfo(str),
            ),
            (
                "bandwidth",
                "bandwidth",
                TypeInfo(str),
            ),
            (
                "loa_issue_time",
                "loaIssueTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "lag_id",
                "lagId",
                TypeInfo(str),
            ),
            (
                "aws_device",
                "awsDevice",
                TypeInfo(str),
            ),
            (
                "aws_device_v2",
                "awsDeviceV2",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID of the interconnect.

    # Example: dxcon-abc123
    interconnect_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the interconnect.

    # Example: " _1G Interconnect to AWS_ "
    interconnect_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # State of the interconnect.

    #   * **Requested** : The initial state of an interconnect. The interconnect stays in the requested state until the Letter of Authorization (LOA) is sent to the customer.

    #   * **Pending** : The interconnect has been approved, and is being initialized.

    #   * **Available** : The network link is up, and the interconnect is ready for use.

    #   * **Down** : The network link is down.

    #   * **Deleting** : The interconnect is in the process of being deleted.

    #   * **Deleted** : The interconnect has been deleted.
    interconnect_state: typing.Union[str, "InterconnectState"
                                    ] = dataclasses.field(
                                        default=ShapeBase.NOT_SET,
                                    )

    # The AWS region where the connection is located.

    # Example: us-east-1

    # Default: None
    region: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Where the connection is located.

    # Example: EqSV5

    # Default: None
    location: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Bandwidth of the connection.

    # Example: 1Gbps

    # Default: None
    bandwidth: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time of the most recent call to DescribeInterconnectLoa for this
    # Interconnect.
    loa_issue_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID of the LAG.

    # Example: dxlag-fg5678gh
    lag_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Deprecated in favor of awsDeviceV2.

    # The Direct Connection endpoint which the physical connection terminates on.
    aws_device: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Direct Connection endpoint which the physical connection terminates on.
    aws_device_v2: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class InterconnectState(str):
    """
    State of the interconnect.

      * **Requested** : The initial state of an interconnect. The interconnect stays in the requested state until the Letter of Authorization (LOA) is sent to the customer.

      * **Pending** : The interconnect has been approved, and is being initialized.

      * **Available** : The network link is up, and the interconnect is ready for use.

      * **Down** : The network link is down.

      * **Deleting** : The interconnect is in the process of being deleted.

      * **Deleted** : The interconnect has been deleted.
    """
    requested = "requested"
    pending = "pending"
    available = "available"
    down = "down"
    deleting = "deleting"
    deleted = "deleted"


@dataclasses.dataclass
class Interconnects(OutputShapeBase):
    """
    A structure containing a list of interconnects.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "interconnects",
                "interconnects",
                TypeInfo(typing.List[Interconnect]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of interconnects.
    interconnects: typing.List["Interconnect"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class Lag(OutputShapeBase):
    """
    Describes a link aggregation group (LAG). A LAG is a connection that uses the
    Link Aggregation Control Protocol (LACP) to logically aggregate a bundle of
    physical connections. Like an interconnect, it can host other connections. All
    connections in a LAG must terminate on the same physical AWS Direct Connect
    endpoint, and must be the same bandwidth.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "connections_bandwidth",
                "connectionsBandwidth",
                TypeInfo(str),
            ),
            (
                "number_of_connections",
                "numberOfConnections",
                TypeInfo(int),
            ),
            (
                "lag_id",
                "lagId",
                TypeInfo(str),
            ),
            (
                "owner_account",
                "ownerAccount",
                TypeInfo(str),
            ),
            (
                "lag_name",
                "lagName",
                TypeInfo(str),
            ),
            (
                "lag_state",
                "lagState",
                TypeInfo(typing.Union[str, LagState]),
            ),
            (
                "location",
                "location",
                TypeInfo(str),
            ),
            (
                "region",
                "region",
                TypeInfo(str),
            ),
            (
                "minimum_links",
                "minimumLinks",
                TypeInfo(int),
            ),
            (
                "aws_device",
                "awsDevice",
                TypeInfo(str),
            ),
            (
                "aws_device_v2",
                "awsDeviceV2",
                TypeInfo(str),
            ),
            (
                "connections",
                "connections",
                TypeInfo(typing.List[Connection]),
            ),
            (
                "allows_hosted_connections",
                "allowsHostedConnections",
                TypeInfo(bool),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The individual bandwidth of the physical connections bundled by the LAG.

    # Available values: 1Gbps, 10Gbps
    connections_bandwidth: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of physical connections bundled by the LAG, up to a maximum of
    # 10.
    number_of_connections: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the LAG.

    # Example: dxlag-fg5678gh
    lag_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The owner of the LAG.
    owner_account: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the LAG.
    lag_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The state of the LAG.

    #   * **Requested** : The initial state of a LAG. The LAG stays in the requested state until the Letter of Authorization (LOA) is available.

    #   * **Pending** : The LAG has been approved, and is being initialized.

    #   * **Available** : The network link is established, and the LAG is ready for use.

    #   * **Down** : The network link is down.

    #   * **Deleting** : The LAG is in the process of being deleted.

    #   * **Deleted** : The LAG has been deleted.
    lag_state: typing.Union[str, "LagState"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Where the connection is located.

    # Example: EqSV5

    # Default: None
    location: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The AWS region where the connection is located.

    # Example: us-east-1

    # Default: None
    region: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The minimum number of physical connections that must be operational for the
    # LAG itself to be operational. If the number of operational connections
    # drops below this setting, the LAG state changes to `down`. This value can
    # help to ensure that a LAG is not overutilized if a significant number of
    # its bundled connections go down.
    minimum_links: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Deprecated in favor of awsDeviceV2.

    # The AWS Direct Connection endpoint that hosts the LAG.
    aws_device: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The AWS Direct Connection endpoint that hosts the LAG.
    aws_device_v2: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of connections bundled by this LAG.
    connections: typing.List["Connection"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Indicates whether the LAG can host other connections.

    # This is intended for use by AWS Direct Connect partners only.
    allows_hosted_connections: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class LagState(str):
    """
    The state of the LAG.

      * **Requested** : The initial state of a LAG. The LAG stays in the requested state until the Letter of Authorization (LOA) is available.

      * **Pending** : The LAG has been approved, and is being initialized.

      * **Available** : The network link is established, and the LAG is ready for use.

      * **Down** : The network link is down.

      * **Deleting** : The LAG is in the process of being deleted.

      * **Deleted** : The LAG has been deleted.
    """
    requested = "requested"
    pending = "pending"
    available = "available"
    down = "down"
    deleting = "deleting"
    deleted = "deleted"


@dataclasses.dataclass
class Lags(OutputShapeBase):
    """
    A structure containing a list of LAGs.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "lags",
                "lags",
                TypeInfo(typing.List[Lag]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of LAGs.
    lags: typing.List["Lag"] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Loa(OutputShapeBase):
    """
    A structure containing the Letter of Authorization - Connecting Facility
    Assignment (LOA-CFA) for a connection.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "loa_content",
                "loaContent",
                TypeInfo(typing.Any),
            ),
            (
                "loa_content_type",
                "loaContentType",
                TypeInfo(typing.Union[str, LoaContentType]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The binary contents of the LOA-CFA document.
    loa_content: typing.Any = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A standard media type indicating the content type of the LOA-CFA document.
    # Currently, the only supported value is "application/pdf".

    # Default: application/pdf
    loa_content_type: typing.Union[str, "LoaContentType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class LoaContent(botocore.response.StreamingBody):
    """
    The binary contents of the LOA-CFA document.
    """
    pass


class LoaContentType(str):
    """
    A standard media type indicating the content type of the LOA-CFA document.
    Currently, the only supported value is "application/pdf".

    Default: application/pdf
    """
    application_pdf = "application/pdf"


@dataclasses.dataclass
class Location(ShapeBase):
    """
    An AWS Direct Connect location where connections and interconnects can be
    requested.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "location_code",
                "locationCode",
                TypeInfo(str),
            ),
            (
                "location_name",
                "locationName",
                TypeInfo(str),
            ),
            (
                "region",
                "region",
                TypeInfo(str),
            ),
        ]

    # The code used to indicate the AWS Direct Connect location.
    location_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the AWS Direct Connect location. The name includes the
    # colocation partner name and the physical site of the lit building.
    location_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The AWS region where the AWS Direct connect location is located.

    # Example: us-east-1

    # Default: None
    region: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Locations(OutputShapeBase):
    """
    A location is a network facility where AWS Direct Connect routers are available
    to be connected. Generally, these are colocation hubs where many network
    providers have equipment, and where cross connects can be delivered. Locations
    include a name and facility code, and must be provided when creating a
    connection.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "locations",
                "locations",
                TypeInfo(typing.List[Location]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of colocation hubs where network providers have equipment. Most
    # regions have multiple locations available.
    locations: typing.List["Location"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class NewBGPPeer(ShapeBase):
    """
    A structure containing information about a new BGP peer.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "asn",
                "asn",
                TypeInfo(int),
            ),
            (
                "auth_key",
                "authKey",
                TypeInfo(str),
            ),
            (
                "address_family",
                "addressFamily",
                TypeInfo(typing.Union[str, AddressFamily]),
            ),
            (
                "amazon_address",
                "amazonAddress",
                TypeInfo(str),
            ),
            (
                "customer_address",
                "customerAddress",
                TypeInfo(str),
            ),
        ]

    # The autonomous system (AS) number for Border Gateway Protocol (BGP)
    # configuration.

    # Example: 65000
    asn: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The authentication key for BGP configuration.

    # Example: asdf34example
    auth_key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates the address family for the BGP peer.

    #   * **ipv4** : IPv4 address family

    #   * **ipv6** : IPv6 address family
    address_family: typing.Union[str, "AddressFamily"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # IP address assigned to the Amazon interface.

    # Example: 192.168.1.1/30 or 2001:db8::1/125
    amazon_address: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # IP address assigned to the customer interface.

    # Example: 192.168.1.2/30 or 2001:db8::2/125
    customer_address: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class NewPrivateVirtualInterface(ShapeBase):
    """
    A structure containing information about a new private virtual interface.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "virtual_interface_name",
                "virtualInterfaceName",
                TypeInfo(str),
            ),
            (
                "vlan",
                "vlan",
                TypeInfo(int),
            ),
            (
                "asn",
                "asn",
                TypeInfo(int),
            ),
            (
                "auth_key",
                "authKey",
                TypeInfo(str),
            ),
            (
                "amazon_address",
                "amazonAddress",
                TypeInfo(str),
            ),
            (
                "customer_address",
                "customerAddress",
                TypeInfo(str),
            ),
            (
                "address_family",
                "addressFamily",
                TypeInfo(typing.Union[str, AddressFamily]),
            ),
            (
                "virtual_gateway_id",
                "virtualGatewayId",
                TypeInfo(str),
            ),
            (
                "direct_connect_gateway_id",
                "directConnectGatewayId",
                TypeInfo(str),
            ),
        ]

    # The name of the virtual interface assigned by the customer.

    # Example: "My VPC"
    virtual_interface_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The VLAN ID.

    # Example: 101
    vlan: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The autonomous system (AS) number for Border Gateway Protocol (BGP)
    # configuration.

    # Example: 65000
    asn: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The authentication key for BGP configuration.

    # Example: asdf34example
    auth_key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # IP address assigned to the Amazon interface.

    # Example: 192.168.1.1/30 or 2001:db8::1/125
    amazon_address: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # IP address assigned to the customer interface.

    # Example: 192.168.1.2/30 or 2001:db8::2/125
    customer_address: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates the address family for the BGP peer.

    #   * **ipv4** : IPv4 address family

    #   * **ipv6** : IPv6 address family
    address_family: typing.Union[str, "AddressFamily"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID of the virtual private gateway to a VPC. This only applies to
    # private virtual interfaces.

    # Example: vgw-123er56
    virtual_gateway_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the direct connect gateway.

    # Example: "abcd1234-dcba-5678-be23-cdef9876ab45"
    direct_connect_gateway_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class NewPrivateVirtualInterfaceAllocation(ShapeBase):
    """
    A structure containing information about a private virtual interface that will
    be provisioned on a connection.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "virtual_interface_name",
                "virtualInterfaceName",
                TypeInfo(str),
            ),
            (
                "vlan",
                "vlan",
                TypeInfo(int),
            ),
            (
                "asn",
                "asn",
                TypeInfo(int),
            ),
            (
                "auth_key",
                "authKey",
                TypeInfo(str),
            ),
            (
                "amazon_address",
                "amazonAddress",
                TypeInfo(str),
            ),
            (
                "address_family",
                "addressFamily",
                TypeInfo(typing.Union[str, AddressFamily]),
            ),
            (
                "customer_address",
                "customerAddress",
                TypeInfo(str),
            ),
        ]

    # The name of the virtual interface assigned by the customer.

    # Example: "My VPC"
    virtual_interface_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The VLAN ID.

    # Example: 101
    vlan: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The autonomous system (AS) number for Border Gateway Protocol (BGP)
    # configuration.

    # Example: 65000
    asn: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The authentication key for BGP configuration.

    # Example: asdf34example
    auth_key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # IP address assigned to the Amazon interface.

    # Example: 192.168.1.1/30 or 2001:db8::1/125
    amazon_address: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates the address family for the BGP peer.

    #   * **ipv4** : IPv4 address family

    #   * **ipv6** : IPv6 address family
    address_family: typing.Union[str, "AddressFamily"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # IP address assigned to the customer interface.

    # Example: 192.168.1.2/30 or 2001:db8::2/125
    customer_address: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class NewPublicVirtualInterface(ShapeBase):
    """
    A structure containing information about a new public virtual interface.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "virtual_interface_name",
                "virtualInterfaceName",
                TypeInfo(str),
            ),
            (
                "vlan",
                "vlan",
                TypeInfo(int),
            ),
            (
                "asn",
                "asn",
                TypeInfo(int),
            ),
            (
                "auth_key",
                "authKey",
                TypeInfo(str),
            ),
            (
                "amazon_address",
                "amazonAddress",
                TypeInfo(str),
            ),
            (
                "customer_address",
                "customerAddress",
                TypeInfo(str),
            ),
            (
                "address_family",
                "addressFamily",
                TypeInfo(typing.Union[str, AddressFamily]),
            ),
            (
                "route_filter_prefixes",
                "routeFilterPrefixes",
                TypeInfo(typing.List[RouteFilterPrefix]),
            ),
        ]

    # The name of the virtual interface assigned by the customer.

    # Example: "My VPC"
    virtual_interface_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The VLAN ID.

    # Example: 101
    vlan: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The autonomous system (AS) number for Border Gateway Protocol (BGP)
    # configuration.

    # Example: 65000
    asn: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The authentication key for BGP configuration.

    # Example: asdf34example
    auth_key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # IP address assigned to the Amazon interface.

    # Example: 192.168.1.1/30 or 2001:db8::1/125
    amazon_address: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # IP address assigned to the customer interface.

    # Example: 192.168.1.2/30 or 2001:db8::2/125
    customer_address: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates the address family for the BGP peer.

    #   * **ipv4** : IPv4 address family

    #   * **ipv6** : IPv6 address family
    address_family: typing.Union[str, "AddressFamily"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of routes to be advertised to the AWS network in this region (public
    # virtual interface).
    route_filter_prefixes: typing.List["RouteFilterPrefix"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class NewPublicVirtualInterfaceAllocation(ShapeBase):
    """
    A structure containing information about a public virtual interface that will be
    provisioned on a connection.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "virtual_interface_name",
                "virtualInterfaceName",
                TypeInfo(str),
            ),
            (
                "vlan",
                "vlan",
                TypeInfo(int),
            ),
            (
                "asn",
                "asn",
                TypeInfo(int),
            ),
            (
                "auth_key",
                "authKey",
                TypeInfo(str),
            ),
            (
                "amazon_address",
                "amazonAddress",
                TypeInfo(str),
            ),
            (
                "customer_address",
                "customerAddress",
                TypeInfo(str),
            ),
            (
                "address_family",
                "addressFamily",
                TypeInfo(typing.Union[str, AddressFamily]),
            ),
            (
                "route_filter_prefixes",
                "routeFilterPrefixes",
                TypeInfo(typing.List[RouteFilterPrefix]),
            ),
        ]

    # The name of the virtual interface assigned by the customer.

    # Example: "My VPC"
    virtual_interface_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The VLAN ID.

    # Example: 101
    vlan: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The autonomous system (AS) number for Border Gateway Protocol (BGP)
    # configuration.

    # Example: 65000
    asn: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The authentication key for BGP configuration.

    # Example: asdf34example
    auth_key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # IP address assigned to the Amazon interface.

    # Example: 192.168.1.1/30 or 2001:db8::1/125
    amazon_address: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # IP address assigned to the customer interface.

    # Example: 192.168.1.2/30 or 2001:db8::2/125
    customer_address: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates the address family for the BGP peer.

    #   * **ipv4** : IPv4 address family

    #   * **ipv6** : IPv6 address family
    address_family: typing.Union[str, "AddressFamily"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of routes to be advertised to the AWS network in this region (public
    # virtual interface).
    route_filter_prefixes: typing.List["RouteFilterPrefix"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ResourceTag(ShapeBase):
    """
    The tags associated with a Direct Connect resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_arn",
                "resourceArn",
                TypeInfo(str),
            ),
            (
                "tags",
                "tags",
                TypeInfo(typing.List[Tag]),
            ),
        ]

    # The Amazon Resource Name (ARN) of the Direct Connect resource.
    resource_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The tags.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RouteFilterPrefix(ShapeBase):
    """
    A route filter prefix that the customer can advertise through Border Gateway
    Protocol (BGP) over a public virtual interface.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cidr",
                "cidr",
                TypeInfo(str),
            ),
        ]

    # CIDR notation for the advertised route. Multiple routes are separated by
    # commas.

    # IPv6 CIDRs must be at least a /64 or shorter

    # Example: 10.10.10.0/24,10.10.11.0/24,2001:db8::/64
    cidr: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Tag(ShapeBase):
    """
    Information about a tag.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "key",
                "key",
                TypeInfo(str),
            ),
            (
                "value",
                "value",
                TypeInfo(str),
            ),
        ]

    # The key of the tag.
    key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The value of the tag.
    value: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TagResourceRequest(ShapeBase):
    """
    Container for the parameters to the TagResource operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_arn",
                "resourceArn",
                TypeInfo(str),
            ),
            (
                "tags",
                "tags",
                TypeInfo(typing.List[Tag]),
            ),
        ]

    # The Amazon Resource Name (ARN) of the Direct Connect resource.

    # Example: arn:aws:directconnect:us-east-1:123456789012:dxcon/dxcon-fg5678gh
    resource_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The list of tags to add.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TagResourceResponse(OutputShapeBase):
    """
    The response received when TagResource is called.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class TooManyTagsException(ShapeBase):
    """
    You have reached the limit on the number of tags that can be assigned to a
    Direct Connect resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class UntagResourceRequest(ShapeBase):
    """
    Container for the parameters to the UntagResource operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_arn",
                "resourceArn",
                TypeInfo(str),
            ),
            (
                "tag_keys",
                "tagKeys",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The Amazon Resource Name (ARN) of the Direct Connect resource.
    resource_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The list of tag keys to remove.
    tag_keys: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UntagResourceResponse(OutputShapeBase):
    """
    The response received when UntagResource is called.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateLagRequest(ShapeBase):
    """
    Container for the parameters to the UpdateLag operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "lag_id",
                "lagId",
                TypeInfo(str),
            ),
            (
                "lag_name",
                "lagName",
                TypeInfo(str),
            ),
            (
                "minimum_links",
                "minimumLinks",
                TypeInfo(int),
            ),
        ]

    # The ID of the LAG to update.

    # Example: dxlag-abc123

    # Default: None
    lag_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name for the LAG.

    # Example: "`3x10G LAG to AWS`"

    # Default: None
    lag_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The minimum number of physical connections that must be operational for the
    # LAG itself to be operational.

    # Default: None
    minimum_links: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class VirtualGateway(ShapeBase):
    """
    You can create one or more AWS Direct Connect private virtual interfaces linking
    to your virtual private gateway.

    Virtual private gateways can be managed using the Amazon Virtual Private Cloud
    (Amazon VPC) console or the [Amazon EC2 CreateVpnGateway
    action](http://docs.aws.amazon.com/AWSEC2/latest/APIReference/ApiReference-
    query-CreateVpnGateway.html).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "virtual_gateway_id",
                "virtualGatewayId",
                TypeInfo(str),
            ),
            (
                "virtual_gateway_state",
                "virtualGatewayState",
                TypeInfo(str),
            ),
        ]

    # The ID of the virtual private gateway to a VPC. This only applies to
    # private virtual interfaces.

    # Example: vgw-123er56
    virtual_gateway_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # State of the virtual private gateway.

    #   * **Pending** : This is the initial state after calling _CreateVpnGateway_.

    #   * **Available** : Ready for use by a private virtual interface.

    #   * **Deleting** : This is the initial state after calling _DeleteVpnGateway_.

    #   * **Deleted** : In this state, a private virtual interface is unable to send traffic over this gateway.
    virtual_gateway_state: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class VirtualGateways(OutputShapeBase):
    """
    A structure containing a list of virtual private gateways.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "virtual_gateways",
                "virtualGateways",
                TypeInfo(typing.List[VirtualGateway]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of virtual private gateways.
    virtual_gateways: typing.List["VirtualGateway"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class VirtualInterface(OutputShapeBase):
    """
    A virtual interface (VLAN) transmits the traffic between the AWS Direct Connect
    location and the customer.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "owner_account",
                "ownerAccount",
                TypeInfo(str),
            ),
            (
                "virtual_interface_id",
                "virtualInterfaceId",
                TypeInfo(str),
            ),
            (
                "location",
                "location",
                TypeInfo(str),
            ),
            (
                "connection_id",
                "connectionId",
                TypeInfo(str),
            ),
            (
                "virtual_interface_type",
                "virtualInterfaceType",
                TypeInfo(str),
            ),
            (
                "virtual_interface_name",
                "virtualInterfaceName",
                TypeInfo(str),
            ),
            (
                "vlan",
                "vlan",
                TypeInfo(int),
            ),
            (
                "asn",
                "asn",
                TypeInfo(int),
            ),
            (
                "amazon_side_asn",
                "amazonSideAsn",
                TypeInfo(int),
            ),
            (
                "auth_key",
                "authKey",
                TypeInfo(str),
            ),
            (
                "amazon_address",
                "amazonAddress",
                TypeInfo(str),
            ),
            (
                "customer_address",
                "customerAddress",
                TypeInfo(str),
            ),
            (
                "address_family",
                "addressFamily",
                TypeInfo(typing.Union[str, AddressFamily]),
            ),
            (
                "virtual_interface_state",
                "virtualInterfaceState",
                TypeInfo(typing.Union[str, VirtualInterfaceState]),
            ),
            (
                "customer_router_config",
                "customerRouterConfig",
                TypeInfo(str),
            ),
            (
                "virtual_gateway_id",
                "virtualGatewayId",
                TypeInfo(str),
            ),
            (
                "direct_connect_gateway_id",
                "directConnectGatewayId",
                TypeInfo(str),
            ),
            (
                "route_filter_prefixes",
                "routeFilterPrefixes",
                TypeInfo(typing.List[RouteFilterPrefix]),
            ),
            (
                "bgp_peers",
                "bgpPeers",
                TypeInfo(typing.List[BGPPeer]),
            ),
            (
                "region",
                "region",
                TypeInfo(str),
            ),
            (
                "aws_device_v2",
                "awsDeviceV2",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The AWS account that will own the new virtual interface.
    owner_account: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the virtual interface.

    # Example: dxvif-123dfg56

    # Default: None
    virtual_interface_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Where the connection is located.

    # Example: EqSV5

    # Default: None
    location: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the connection. This field is also used as the ID type for
    # operations that use multiple connection types (LAG, interconnect, and/or
    # connection).

    # Example: dxcon-fg5678gh

    # Default: None
    connection_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of virtual interface.

    # Example: private (Amazon VPC) or public (Amazon S3, Amazon DynamoDB, and so
    # on.)
    virtual_interface_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the virtual interface assigned by the customer.

    # Example: "My VPC"
    virtual_interface_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The VLAN ID.

    # Example: 101
    vlan: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The autonomous system (AS) number for Border Gateway Protocol (BGP)
    # configuration.

    # Example: 65000
    asn: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The autonomous system number (ASN) for the Amazon side of the connection.
    amazon_side_asn: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The authentication key for BGP configuration.

    # Example: asdf34example
    auth_key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # IP address assigned to the Amazon interface.

    # Example: 192.168.1.1/30 or 2001:db8::1/125
    amazon_address: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # IP address assigned to the customer interface.

    # Example: 192.168.1.2/30 or 2001:db8::2/125
    customer_address: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates the address family for the BGP peer.

    #   * **ipv4** : IPv4 address family

    #   * **ipv6** : IPv6 address family
    address_family: typing.Union[str, "AddressFamily"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # State of the virtual interface.

    #   * **Confirming** : The creation of the virtual interface is pending confirmation from the virtual interface owner. If the owner of the virtual interface is different from the owner of the connection on which it is provisioned, then the virtual interface will remain in this state until it is confirmed by the virtual interface owner.

    #   * **Verifying** : This state only applies to public virtual interfaces. Each public virtual interface needs validation before the virtual interface can be created.

    #   * **Pending** : A virtual interface is in this state from the time that it is created until the virtual interface is ready to forward traffic.

    #   * **Available** : A virtual interface that is able to forward traffic.

    #   * **Down** : A virtual interface that is BGP down.

    #   * **Deleting** : A virtual interface is in this state immediately after calling DeleteVirtualInterface until it can no longer forward traffic.

    #   * **Deleted** : A virtual interface that cannot forward traffic.

    #   * **Rejected** : The virtual interface owner has declined creation of the virtual interface. If a virtual interface in the 'Confirming' state is deleted by the virtual interface owner, the virtual interface will enter the 'Rejected' state.
    virtual_interface_state: typing.Union[str, "VirtualInterfaceState"
                                         ] = dataclasses.field(
                                             default=ShapeBase.NOT_SET,
                                         )

    # Information for generating the customer router configuration.
    customer_router_config: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the virtual private gateway to a VPC. This only applies to
    # private virtual interfaces.

    # Example: vgw-123er56
    virtual_gateway_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the direct connect gateway.

    # Example: "abcd1234-dcba-5678-be23-cdef9876ab45"
    direct_connect_gateway_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of routes to be advertised to the AWS network in this region (public
    # virtual interface).
    route_filter_prefixes: typing.List["RouteFilterPrefix"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of the BGP peers configured on this virtual interface.
    bgp_peers: typing.List["BGPPeer"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The AWS region where the virtual interface is located.

    # Example: us-east-1

    # Default: None
    region: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Direct Connection endpoint which the virtual interface terminates on.
    aws_device_v2: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class VirtualInterfaceState(str):
    """
    State of the virtual interface.

      * **Confirming** : The creation of the virtual interface is pending confirmation from the virtual interface owner. If the owner of the virtual interface is different from the owner of the connection on which it is provisioned, then the virtual interface will remain in this state until it is confirmed by the virtual interface owner.

      * **Verifying** : This state only applies to public virtual interfaces. Each public virtual interface needs validation before the virtual interface can be created.

      * **Pending** : A virtual interface is in this state from the time that it is created until the virtual interface is ready to forward traffic.

      * **Available** : A virtual interface that is able to forward traffic.

      * **Down** : A virtual interface that is BGP down.

      * **Deleting** : A virtual interface is in this state immediately after calling DeleteVirtualInterface until it can no longer forward traffic.

      * **Deleted** : A virtual interface that cannot forward traffic.

      * **Rejected** : The virtual interface owner has declined creation of the virtual interface. If a virtual interface in the 'Confirming' state is deleted by the virtual interface owner, the virtual interface will enter the 'Rejected' state.
    """
    confirming = "confirming"
    verifying = "verifying"
    pending = "pending"
    available = "available"
    down = "down"
    deleting = "deleting"
    deleted = "deleted"
    rejected = "rejected"


@dataclasses.dataclass
class VirtualInterfaces(OutputShapeBase):
    """
    A structure containing a list of virtual interfaces.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "virtual_interfaces",
                "virtualInterfaces",
                TypeInfo(typing.List[VirtualInterface]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of virtual interfaces.
    virtual_interfaces: typing.List["VirtualInterface"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )
