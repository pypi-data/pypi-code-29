import datetime
import typing
from autoboto import ShapeBase, OutputShapeBase, TypeInfo
import dataclasses


@dataclasses.dataclass
class AddIpRoutesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "directory_id",
                "DirectoryId",
                TypeInfo(str),
            ),
            (
                "ip_routes",
                "IpRoutes",
                TypeInfo(typing.List[IpRoute]),
            ),
            (
                "update_security_group_for_directory_controllers",
                "UpdateSecurityGroupForDirectoryControllers",
                TypeInfo(bool),
            ),
        ]

    # Identifier (ID) of the directory to which to add the address block.
    directory_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # IP address blocks, using CIDR format, of the traffic to route. This is
    # often the IP address block of the DNS server used for your on-premises
    # domain.
    ip_routes: typing.List["IpRoute"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If set to true, updates the inbound and outbound rules of the security
    # group that has the description: "AWS created security group for _directory
    # ID_ directory controllers." Following are the new rules:

    # Inbound:

    #   * Type: Custom UDP Rule, Protocol: UDP, Range: 88, Source: 0.0.0.0/0

    #   * Type: Custom UDP Rule, Protocol: UDP, Range: 123, Source: 0.0.0.0/0

    #   * Type: Custom UDP Rule, Protocol: UDP, Range: 138, Source: 0.0.0.0/0

    #   * Type: Custom UDP Rule, Protocol: UDP, Range: 389, Source: 0.0.0.0/0

    #   * Type: Custom UDP Rule, Protocol: UDP, Range: 464, Source: 0.0.0.0/0

    #   * Type: Custom UDP Rule, Protocol: UDP, Range: 445, Source: 0.0.0.0/0

    #   * Type: Custom TCP Rule, Protocol: TCP, Range: 88, Source: 0.0.0.0/0

    #   * Type: Custom TCP Rule, Protocol: TCP, Range: 135, Source: 0.0.0.0/0

    #   * Type: Custom TCP Rule, Protocol: TCP, Range: 445, Source: 0.0.0.0/0

    #   * Type: Custom TCP Rule, Protocol: TCP, Range: 464, Source: 0.0.0.0/0

    #   * Type: Custom TCP Rule, Protocol: TCP, Range: 636, Source: 0.0.0.0/0

    #   * Type: Custom TCP Rule, Protocol: TCP, Range: 1024-65535, Source: 0.0.0.0/0

    #   * Type: Custom TCP Rule, Protocol: TCP, Range: 3268-33269, Source: 0.0.0.0/0

    #   * Type: DNS (UDP), Protocol: UDP, Range: 53, Source: 0.0.0.0/0

    #   * Type: DNS (TCP), Protocol: TCP, Range: 53, Source: 0.0.0.0/0

    #   * Type: LDAP, Protocol: TCP, Range: 389, Source: 0.0.0.0/0

    #   * Type: All ICMP, Protocol: All, Range: N/A, Source: 0.0.0.0/0

    # Outbound:

    #   * Type: All traffic, Protocol: All, Range: All, Destination: 0.0.0.0/0

    # These security rules impact an internal network interface that is not
    # exposed publicly.
    update_security_group_for_directory_controllers: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AddIpRoutesResult(OutputShapeBase):
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
class AddTagsToResourceRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_id",
                "ResourceId",
                TypeInfo(str),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.List[Tag]),
            ),
        ]

    # Identifier (ID) for the directory to which to add the tag.
    resource_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The tags to be assigned to the directory.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AddTagsToResourceResult(OutputShapeBase):
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
class Attribute(ShapeBase):
    """
    Represents a named directory attribute.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "value",
                "Value",
                TypeInfo(str),
            ),
        ]

    # The name of the attribute.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The value of the attribute.
    value: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AuthenticationFailedException(ShapeBase):
    """
    An authentication error occurred.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
            (
                "request_id",
                "RequestId",
                TypeInfo(str),
            ),
        ]

    # The textual message for the exception.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identifier of the request that caused the exception.
    request_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CancelSchemaExtensionRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "directory_id",
                "DirectoryId",
                TypeInfo(str),
            ),
            (
                "schema_extension_id",
                "SchemaExtensionId",
                TypeInfo(str),
            ),
        ]

    # The identifier of the directory whose schema extension will be canceled.
    directory_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identifier of the schema extension that will be canceled.
    schema_extension_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CancelSchemaExtensionResult(OutputShapeBase):
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
class ClientException(ShapeBase):
    """
    A client exception has occurred.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
            (
                "request_id",
                "RequestId",
                TypeInfo(str),
            ),
        ]

    # The descriptive message for the exception.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The AWS request identifier.
    request_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Computer(ShapeBase):
    """
    Contains information about a computer account in a directory.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "computer_id",
                "ComputerId",
                TypeInfo(str),
            ),
            (
                "computer_name",
                "ComputerName",
                TypeInfo(str),
            ),
            (
                "computer_attributes",
                "ComputerAttributes",
                TypeInfo(typing.List[Attribute]),
            ),
        ]

    # The identifier of the computer.
    computer_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The computer name.
    computer_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An array of Attribute objects containing the LDAP attributes that belong to
    # the computer account.
    computer_attributes: typing.List["Attribute"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ConditionalForwarder(ShapeBase):
    """
    Points to a remote domain with which you are setting up a trust relationship.
    Conditional forwarders are required in order to set up a trust relationship with
    another domain.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "remote_domain_name",
                "RemoteDomainName",
                TypeInfo(str),
            ),
            (
                "dns_ip_addrs",
                "DnsIpAddrs",
                TypeInfo(typing.List[str]),
            ),
            (
                "replication_scope",
                "ReplicationScope",
                TypeInfo(typing.Union[str, ReplicationScope]),
            ),
        ]

    # The fully qualified domain name (FQDN) of the remote domains pointed to by
    # the conditional forwarder.
    remote_domain_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The IP addresses of the remote DNS server associated with RemoteDomainName.
    # This is the IP address of the DNS server that your conditional forwarder
    # points to.
    dns_ip_addrs: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The replication scope of the conditional forwarder. The only allowed value
    # is `Domain`, which will replicate the conditional forwarder to all of the
    # domain controllers for your AWS directory.
    replication_scope: typing.Union[str, "ReplicationScope"
                                   ] = dataclasses.field(
                                       default=ShapeBase.NOT_SET,
                                   )


@dataclasses.dataclass
class ConnectDirectoryRequest(ShapeBase):
    """
    Contains the inputs for the ConnectDirectory operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "password",
                "Password",
                TypeInfo(str),
            ),
            (
                "size",
                "Size",
                TypeInfo(typing.Union[str, DirectorySize]),
            ),
            (
                "connect_settings",
                "ConnectSettings",
                TypeInfo(DirectoryConnectSettings),
            ),
            (
                "short_name",
                "ShortName",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
        ]

    # The fully-qualified name of the on-premises directory, such as
    # `corp.example.com`.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The password for the on-premises user account.
    password: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The size of the directory.
    size: typing.Union[str, "DirectorySize"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A DirectoryConnectSettings object that contains additional information for
    # the operation.
    connect_settings: "DirectoryConnectSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The NetBIOS name of the on-premises directory, such as `CORP`.
    short_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A textual description for the directory.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ConnectDirectoryResult(OutputShapeBase):
    """
    Contains the results of the ConnectDirectory operation.
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
                "directory_id",
                "DirectoryId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The identifier of the new directory.
    directory_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateAliasRequest(ShapeBase):
    """
    Contains the inputs for the CreateAlias operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "directory_id",
                "DirectoryId",
                TypeInfo(str),
            ),
            (
                "alias",
                "Alias",
                TypeInfo(str),
            ),
        ]

    # The identifier of the directory for which to create the alias.
    directory_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The requested alias.

    # The alias must be unique amongst all aliases in AWS. This operation throws
    # an `EntityAlreadyExistsException` error if the alias already exists.
    alias: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateAliasResult(OutputShapeBase):
    """
    Contains the results of the CreateAlias operation.
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
                "directory_id",
                "DirectoryId",
                TypeInfo(str),
            ),
            (
                "alias",
                "Alias",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The identifier of the directory.
    directory_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The alias for the directory.
    alias: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateComputerRequest(ShapeBase):
    """
    Contains the inputs for the CreateComputer operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "directory_id",
                "DirectoryId",
                TypeInfo(str),
            ),
            (
                "computer_name",
                "ComputerName",
                TypeInfo(str),
            ),
            (
                "password",
                "Password",
                TypeInfo(str),
            ),
            (
                "organizational_unit_distinguished_name",
                "OrganizationalUnitDistinguishedName",
                TypeInfo(str),
            ),
            (
                "computer_attributes",
                "ComputerAttributes",
                TypeInfo(typing.List[Attribute]),
            ),
        ]

    # The identifier of the directory in which to create the computer account.
    directory_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the computer account.
    computer_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A one-time password that is used to join the computer to the directory. You
    # should generate a random, strong password to use for this parameter.
    password: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The fully-qualified distinguished name of the organizational unit to place
    # the computer account in.
    organizational_unit_distinguished_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An array of Attribute objects that contain any LDAP attributes to apply to
    # the computer account.
    computer_attributes: typing.List["Attribute"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateComputerResult(OutputShapeBase):
    """
    Contains the results for the CreateComputer operation.
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
                "computer",
                "Computer",
                TypeInfo(Computer),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A Computer object that represents the computer account.
    computer: "Computer" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateConditionalForwarderRequest(ShapeBase):
    """
    Initiates the creation of a conditional forwarder for your AWS Directory Service
    for Microsoft Active Directory. Conditional forwarders are required in order to
    set up a trust relationship with another domain.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "directory_id",
                "DirectoryId",
                TypeInfo(str),
            ),
            (
                "remote_domain_name",
                "RemoteDomainName",
                TypeInfo(str),
            ),
            (
                "dns_ip_addrs",
                "DnsIpAddrs",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The directory ID of the AWS directory for which you are creating the
    # conditional forwarder.
    directory_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The fully qualified domain name (FQDN) of the remote domain with which you
    # will set up a trust relationship.
    remote_domain_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The IP addresses of the remote DNS server associated with RemoteDomainName.
    dns_ip_addrs: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateConditionalForwarderResult(OutputShapeBase):
    """
    The result of a CreateConditinalForwarder request.
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
class CreateDirectoryRequest(ShapeBase):
    """
    Contains the inputs for the CreateDirectory operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "password",
                "Password",
                TypeInfo(str),
            ),
            (
                "size",
                "Size",
                TypeInfo(typing.Union[str, DirectorySize]),
            ),
            (
                "short_name",
                "ShortName",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "vpc_settings",
                "VpcSettings",
                TypeInfo(DirectoryVpcSettings),
            ),
        ]

    # The fully qualified name for the directory, such as `corp.example.com`.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The password for the directory administrator. The directory creation
    # process creates a directory administrator account with the username
    # `Administrator` and this password.
    password: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The size of the directory.
    size: typing.Union[str, "DirectorySize"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The short name of the directory, such as `CORP`.
    short_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A textual description for the directory.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A DirectoryVpcSettings object that contains additional information for the
    # operation.
    vpc_settings: "DirectoryVpcSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateDirectoryResult(OutputShapeBase):
    """
    Contains the results of the CreateDirectory operation.
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
                "directory_id",
                "DirectoryId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The identifier of the directory that was created.
    directory_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateMicrosoftADRequest(ShapeBase):
    """
    Creates a Microsoft AD in the AWS cloud.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "password",
                "Password",
                TypeInfo(str),
            ),
            (
                "vpc_settings",
                "VpcSettings",
                TypeInfo(DirectoryVpcSettings),
            ),
            (
                "short_name",
                "ShortName",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "edition",
                "Edition",
                TypeInfo(typing.Union[str, DirectoryEdition]),
            ),
        ]

    # The fully qualified domain name for the directory, such as
    # `corp.example.com`. This name will resolve inside your VPC only. It does
    # not need to be publicly resolvable.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The password for the default administrative user named `Admin`.
    password: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Contains VPC information for the CreateDirectory or CreateMicrosoftAD
    # operation.
    vpc_settings: "DirectoryVpcSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The NetBIOS name for your domain. A short identifier for your domain, such
    # as `CORP`. If you don't specify a NetBIOS name, it will default to the
    # first part of your directory DNS. For example, `CORP` for the directory DNS
    # `corp.example.com`.
    short_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A textual description for the directory. This label will appear on the AWS
    # console `Directory Details` page after the directory is created.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # AWS Microsoft AD is available in two editions: Standard and Enterprise.
    # Enterprise is the default.
    edition: typing.Union[str, "DirectoryEdition"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateMicrosoftADResult(OutputShapeBase):
    """
    Result of a CreateMicrosoftAD request.
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
                "directory_id",
                "DirectoryId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The identifier of the directory that was created.
    directory_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateSnapshotRequest(ShapeBase):
    """
    Contains the inputs for the CreateSnapshot operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "directory_id",
                "DirectoryId",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    # The identifier of the directory of which to take a snapshot.
    directory_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The descriptive name to apply to the snapshot.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateSnapshotResult(OutputShapeBase):
    """
    Contains the results of the CreateSnapshot operation.
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
                "snapshot_id",
                "SnapshotId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The identifier of the snapshot that was created.
    snapshot_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateTrustRequest(ShapeBase):
    """
    AWS Directory Service for Microsoft Active Directory allows you to configure
    trust relationships. For example, you can establish a trust between your
    Microsoft AD in the AWS cloud, and your existing on-premises Microsoft Active
    Directory. This would allow you to provide users and groups access to resources
    in either domain, with a single set of credentials.

    This action initiates the creation of the AWS side of a trust relationship
    between a Microsoft AD in the AWS cloud and an external domain.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "directory_id",
                "DirectoryId",
                TypeInfo(str),
            ),
            (
                "remote_domain_name",
                "RemoteDomainName",
                TypeInfo(str),
            ),
            (
                "trust_password",
                "TrustPassword",
                TypeInfo(str),
            ),
            (
                "trust_direction",
                "TrustDirection",
                TypeInfo(typing.Union[str, TrustDirection]),
            ),
            (
                "trust_type",
                "TrustType",
                TypeInfo(typing.Union[str, TrustType]),
            ),
            (
                "conditional_forwarder_ip_addrs",
                "ConditionalForwarderIpAddrs",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The Directory ID of the Microsoft AD in the AWS cloud for which to
    # establish the trust relationship.
    directory_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Fully Qualified Domain Name (FQDN) of the external domain for which to
    # create the trust relationship.
    remote_domain_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The trust password. The must be the same password that was used when
    # creating the trust relationship on the external domain.
    trust_password: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The direction of the trust relationship.
    trust_direction: typing.Union[str, "TrustDirection"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The trust relationship type.
    trust_type: typing.Union[str, "TrustType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The IP addresses of the remote DNS server associated with RemoteDomainName.
    conditional_forwarder_ip_addrs: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateTrustResult(OutputShapeBase):
    """
    The result of a CreateTrust request.
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
                "trust_id",
                "TrustId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A unique identifier for the trust relationship that was created.
    trust_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteConditionalForwarderRequest(ShapeBase):
    """
    Deletes a conditional forwarder.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "directory_id",
                "DirectoryId",
                TypeInfo(str),
            ),
            (
                "remote_domain_name",
                "RemoteDomainName",
                TypeInfo(str),
            ),
        ]

    # The directory ID for which you are deleting the conditional forwarder.
    directory_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The fully qualified domain name (FQDN) of the remote domain with which you
    # are deleting the conditional forwarder.
    remote_domain_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteConditionalForwarderResult(OutputShapeBase):
    """
    The result of a DeleteConditionalForwarder request.
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
class DeleteDirectoryRequest(ShapeBase):
    """
    Contains the inputs for the DeleteDirectory operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "directory_id",
                "DirectoryId",
                TypeInfo(str),
            ),
        ]

    # The identifier of the directory to delete.
    directory_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteDirectoryResult(OutputShapeBase):
    """
    Contains the results of the DeleteDirectory operation.
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
                "directory_id",
                "DirectoryId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The directory identifier.
    directory_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteSnapshotRequest(ShapeBase):
    """
    Contains the inputs for the DeleteSnapshot operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "snapshot_id",
                "SnapshotId",
                TypeInfo(str),
            ),
        ]

    # The identifier of the directory snapshot to be deleted.
    snapshot_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteSnapshotResult(OutputShapeBase):
    """
    Contains the results of the DeleteSnapshot operation.
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
                "snapshot_id",
                "SnapshotId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The identifier of the directory snapshot that was deleted.
    snapshot_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteTrustRequest(ShapeBase):
    """
    Deletes the local side of an existing trust relationship between the Microsoft
    AD in the AWS cloud and the external domain.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "trust_id",
                "TrustId",
                TypeInfo(str),
            ),
            (
                "delete_associated_conditional_forwarder",
                "DeleteAssociatedConditionalForwarder",
                TypeInfo(bool),
            ),
        ]

    # The Trust ID of the trust relationship to be deleted.
    trust_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Delete a conditional forwarder as part of a DeleteTrustRequest.
    delete_associated_conditional_forwarder: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteTrustResult(OutputShapeBase):
    """
    The result of a DeleteTrust request.
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
                "trust_id",
                "TrustId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Trust ID of the trust relationship that was deleted.
    trust_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeregisterEventTopicRequest(ShapeBase):
    """
    Removes the specified directory as a publisher to the specified SNS topic.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "directory_id",
                "DirectoryId",
                TypeInfo(str),
            ),
            (
                "topic_name",
                "TopicName",
                TypeInfo(str),
            ),
        ]

    # The Directory ID to remove as a publisher. This directory will no longer
    # send messages to the specified SNS topic.
    directory_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the SNS topic from which to remove the directory as a
    # publisher.
    topic_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeregisterEventTopicResult(OutputShapeBase):
    """
    The result of a DeregisterEventTopic request.
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
class DescribeConditionalForwardersRequest(ShapeBase):
    """
    Describes a conditional forwarder.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "directory_id",
                "DirectoryId",
                TypeInfo(str),
            ),
            (
                "remote_domain_names",
                "RemoteDomainNames",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The directory ID for which to get the list of associated conditional
    # forwarders.
    directory_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The fully qualified domain names (FQDN) of the remote domains for which to
    # get the list of associated conditional forwarders. If this member is null,
    # all conditional forwarders are returned.
    remote_domain_names: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeConditionalForwardersResult(OutputShapeBase):
    """
    The result of a DescribeConditionalForwarder request.
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
                "conditional_forwarders",
                "ConditionalForwarders",
                TypeInfo(typing.List[ConditionalForwarder]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The list of conditional forwarders that have been created.
    conditional_forwarders: typing.List["ConditionalForwarder"
                                       ] = dataclasses.field(
                                           default=ShapeBase.NOT_SET,
                                       )


@dataclasses.dataclass
class DescribeDirectoriesRequest(ShapeBase):
    """
    Contains the inputs for the DescribeDirectories operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "directory_ids",
                "DirectoryIds",
                TypeInfo(typing.List[str]),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
            (
                "limit",
                "Limit",
                TypeInfo(int),
            ),
        ]

    # A list of identifiers of the directories for which to obtain the
    # information. If this member is null, all directories that belong to the
    # current account are returned.

    # An empty list results in an `InvalidParameterException` being thrown.
    directory_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The _DescribeDirectoriesResult.NextToken_ value from a previous call to
    # DescribeDirectories. Pass null if this is the first call.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of items to return. If this value is zero, the maximum
    # number of items is specified by the limitations of the operation.
    limit: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeDirectoriesResult(OutputShapeBase):
    """
    Contains the results of the DescribeDirectories operation.
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
                "directory_descriptions",
                "DirectoryDescriptions",
                TypeInfo(typing.List[DirectoryDescription]),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The list of DirectoryDescription objects that were retrieved.

    # It is possible that this list contains less than the number of items
    # specified in the _Limit_ member of the request. This occurs if there are
    # less than the requested number of items left to retrieve, or if the
    # limitations of the operation have been exceeded.
    directory_descriptions: typing.List["DirectoryDescription"
                                       ] = dataclasses.field(
                                           default=ShapeBase.NOT_SET,
                                       )

    # If not null, more results are available. Pass this value for the
    # _NextToken_ parameter in a subsequent call to DescribeDirectories to
    # retrieve the next set of items.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeDomainControllersRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "directory_id",
                "DirectoryId",
                TypeInfo(str),
            ),
            (
                "domain_controller_ids",
                "DomainControllerIds",
                TypeInfo(typing.List[str]),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
            (
                "limit",
                "Limit",
                TypeInfo(int),
            ),
        ]

    # Identifier of the directory for which to retrieve the domain controller
    # information.
    directory_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of identifiers for the domain controllers whose information will be
    # provided.
    domain_controller_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The _DescribeDomainControllers.NextToken_ value from a previous call to
    # DescribeDomainControllers. Pass null if this is the first call.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of items to return.
    limit: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeDomainControllersResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "domain_controllers",
                "DomainControllers",
                TypeInfo(typing.List[DomainController]),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # List of the DomainController objects that were retrieved.
    domain_controllers: typing.List["DomainController"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If not null, more results are available. Pass this value for the
    # `NextToken` parameter in a subsequent call to DescribeDomainControllers
    # retrieve the next set of items.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(
        self,
    ) -> typing.Generator["DescribeDomainControllersResult", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class DescribeEventTopicsRequest(ShapeBase):
    """
    Describes event topics.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "directory_id",
                "DirectoryId",
                TypeInfo(str),
            ),
            (
                "topic_names",
                "TopicNames",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The Directory ID for which to get the list of associated SNS topics. If
    # this member is null, associations for all Directory IDs are returned.
    directory_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of SNS topic names for which to obtain the information. If this
    # member is null, all associations for the specified Directory ID are
    # returned.

    # An empty list results in an `InvalidParameterException` being thrown.
    topic_names: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeEventTopicsResult(OutputShapeBase):
    """
    The result of a DescribeEventTopic request.
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
                "event_topics",
                "EventTopics",
                TypeInfo(typing.List[EventTopic]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of SNS topic names that receive status messages from the specified
    # Directory ID.
    event_topics: typing.List["EventTopic"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeSnapshotsRequest(ShapeBase):
    """
    Contains the inputs for the DescribeSnapshots operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "directory_id",
                "DirectoryId",
                TypeInfo(str),
            ),
            (
                "snapshot_ids",
                "SnapshotIds",
                TypeInfo(typing.List[str]),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
            (
                "limit",
                "Limit",
                TypeInfo(int),
            ),
        ]

    # The identifier of the directory for which to retrieve snapshot information.
    directory_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of identifiers of the snapshots to obtain the information for. If
    # this member is null or empty, all snapshots are returned using the _Limit_
    # and _NextToken_ members.
    snapshot_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The _DescribeSnapshotsResult.NextToken_ value from a previous call to
    # DescribeSnapshots. Pass null if this is the first call.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of objects to return.
    limit: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeSnapshotsResult(OutputShapeBase):
    """
    Contains the results of the DescribeSnapshots operation.
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
                "snapshots",
                "Snapshots",
                TypeInfo(typing.List[Snapshot]),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The list of Snapshot objects that were retrieved.

    # It is possible that this list contains less than the number of items
    # specified in the _Limit_ member of the request. This occurs if there are
    # less than the requested number of items left to retrieve, or if the
    # limitations of the operation have been exceeded.
    snapshots: typing.List["Snapshot"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If not null, more results are available. Pass this value in the _NextToken_
    # member of a subsequent call to DescribeSnapshots.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeTrustsRequest(ShapeBase):
    """
    Describes the trust relationships for a particular Microsoft AD in the AWS
    cloud. If no input parameters are are provided, such as directory ID or trust
    ID, this request describes all the trust relationships.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "directory_id",
                "DirectoryId",
                TypeInfo(str),
            ),
            (
                "trust_ids",
                "TrustIds",
                TypeInfo(typing.List[str]),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
            (
                "limit",
                "Limit",
                TypeInfo(int),
            ),
        ]

    # The Directory ID of the AWS directory that is a part of the requested trust
    # relationship.
    directory_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of identifiers of the trust relationships for which to obtain the
    # information. If this member is null, all trust relationships that belong to
    # the current account are returned.

    # An empty list results in an `InvalidParameterException` being thrown.
    trust_ids: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The _DescribeTrustsResult.NextToken_ value from a previous call to
    # DescribeTrusts. Pass null if this is the first call.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of objects to return.
    limit: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeTrustsResult(OutputShapeBase):
    """
    The result of a DescribeTrust request.
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
                "trusts",
                "Trusts",
                TypeInfo(typing.List[Trust]),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The list of Trust objects that were retrieved.

    # It is possible that this list contains less than the number of items
    # specified in the _Limit_ member of the request. This occurs if there are
    # less than the requested number of items left to retrieve, or if the
    # limitations of the operation have been exceeded.
    trusts: typing.List["Trust"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If not null, more results are available. Pass this value for the
    # _NextToken_ parameter in a subsequent call to DescribeTrusts to retrieve
    # the next set of items.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DirectoryConnectSettings(ShapeBase):
    """
    Contains information for the ConnectDirectory operation when an AD Connector
    directory is being created.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "vpc_id",
                "VpcId",
                TypeInfo(str),
            ),
            (
                "subnet_ids",
                "SubnetIds",
                TypeInfo(typing.List[str]),
            ),
            (
                "customer_dns_ips",
                "CustomerDnsIps",
                TypeInfo(typing.List[str]),
            ),
            (
                "customer_user_name",
                "CustomerUserName",
                TypeInfo(str),
            ),
        ]

    # The identifier of the VPC in which the AD Connector is created.
    vpc_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of subnet identifiers in the VPC in which the AD Connector is
    # created.
    subnet_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of one or more IP addresses of DNS servers or domain controllers in
    # the on-premises directory.
    customer_dns_ips: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The username of an account in the on-premises directory that is used to
    # connect to the directory. This account must have the following privileges:

    #   * Read users and groups

    #   * Create computer objects

    #   * Join computers to the domain
    customer_user_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DirectoryConnectSettingsDescription(ShapeBase):
    """
    Contains information about an AD Connector directory.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "vpc_id",
                "VpcId",
                TypeInfo(str),
            ),
            (
                "subnet_ids",
                "SubnetIds",
                TypeInfo(typing.List[str]),
            ),
            (
                "customer_user_name",
                "CustomerUserName",
                TypeInfo(str),
            ),
            (
                "security_group_id",
                "SecurityGroupId",
                TypeInfo(str),
            ),
            (
                "availability_zones",
                "AvailabilityZones",
                TypeInfo(typing.List[str]),
            ),
            (
                "connect_ips",
                "ConnectIps",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The identifier of the VPC that the AD Connector is in.
    vpc_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of subnet identifiers in the VPC that the AD connector is in.
    subnet_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The username of the service account in the on-premises directory.
    customer_user_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The security group identifier for the AD Connector directory.
    security_group_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of the Availability Zones that the directory is in.
    availability_zones: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The IP addresses of the AD Connector servers.
    connect_ips: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DirectoryDescription(ShapeBase):
    """
    Contains information about an AWS Directory Service directory.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "directory_id",
                "DirectoryId",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "short_name",
                "ShortName",
                TypeInfo(str),
            ),
            (
                "size",
                "Size",
                TypeInfo(typing.Union[str, DirectorySize]),
            ),
            (
                "edition",
                "Edition",
                TypeInfo(typing.Union[str, DirectoryEdition]),
            ),
            (
                "alias",
                "Alias",
                TypeInfo(str),
            ),
            (
                "access_url",
                "AccessUrl",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "dns_ip_addrs",
                "DnsIpAddrs",
                TypeInfo(typing.List[str]),
            ),
            (
                "stage",
                "Stage",
                TypeInfo(typing.Union[str, DirectoryStage]),
            ),
            (
                "launch_time",
                "LaunchTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "stage_last_updated_date_time",
                "StageLastUpdatedDateTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "type",
                "Type",
                TypeInfo(typing.Union[str, DirectoryType]),
            ),
            (
                "vpc_settings",
                "VpcSettings",
                TypeInfo(DirectoryVpcSettingsDescription),
            ),
            (
                "connect_settings",
                "ConnectSettings",
                TypeInfo(DirectoryConnectSettingsDescription),
            ),
            (
                "radius_settings",
                "RadiusSettings",
                TypeInfo(RadiusSettings),
            ),
            (
                "radius_status",
                "RadiusStatus",
                TypeInfo(typing.Union[str, RadiusStatus]),
            ),
            (
                "stage_reason",
                "StageReason",
                TypeInfo(str),
            ),
            (
                "sso_enabled",
                "SsoEnabled",
                TypeInfo(bool),
            ),
            (
                "desired_number_of_domain_controllers",
                "DesiredNumberOfDomainControllers",
                TypeInfo(int),
            ),
        ]

    # The directory identifier.
    directory_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The fully-qualified name of the directory.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The short name of the directory.
    short_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The directory size.
    size: typing.Union[str, "DirectorySize"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The edition associated with this directory.
    edition: typing.Union[str, "DirectoryEdition"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The alias for the directory. If no alias has been created for the
    # directory, the alias is the directory identifier, such as `d-XXXXXXXXXX`.
    alias: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The access URL for the directory, such as `http://<alias>.awsapps.com`. If
    # no alias has been created for the directory, `<alias>` is the directory
    # identifier, such as `d-XXXXXXXXXX`.
    access_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The textual description for the directory.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The IP addresses of the DNS servers for the directory. For a Simple AD or
    # Microsoft AD directory, these are the IP addresses of the Simple AD or
    # Microsoft AD directory servers. For an AD Connector directory, these are
    # the IP addresses of the DNS servers or domain controllers in the on-
    # premises directory to which the AD Connector is connected.
    dns_ip_addrs: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The current stage of the directory.
    stage: typing.Union[str, "DirectoryStage"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies when the directory was created.
    launch_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date and time that the stage was last updated.
    stage_last_updated_date_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The directory size.
    type: typing.Union[str, "DirectoryType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A DirectoryVpcSettingsDescription object that contains additional
    # information about a directory. This member is only present if the directory
    # is a Simple AD or Managed AD directory.
    vpc_settings: "DirectoryVpcSettingsDescription" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A DirectoryConnectSettingsDescription object that contains additional
    # information about an AD Connector directory. This member is only present if
    # the directory is an AD Connector directory.
    connect_settings: "DirectoryConnectSettingsDescription" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A RadiusSettings object that contains information about the RADIUS server
    # configured for this directory.
    radius_settings: "RadiusSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The status of the RADIUS MFA server connection.
    radius_status: typing.Union[str, "RadiusStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Additional information about the directory stage.
    stage_reason: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates if single-sign on is enabled for the directory. For more
    # information, see EnableSso and DisableSso.
    sso_enabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The desired number of domain controllers in the directory if the directory
    # is Microsoft AD.
    desired_number_of_domain_controllers: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class DirectoryEdition(str):
    Enterprise = "Enterprise"
    Standard = "Standard"


@dataclasses.dataclass
class DirectoryLimitExceededException(ShapeBase):
    """
    The maximum number of directories in the region has been reached. You can use
    the GetDirectoryLimits operation to determine your directory limits in the
    region.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
            (
                "request_id",
                "RequestId",
                TypeInfo(str),
            ),
        ]

    # The descriptive message for the exception.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The AWS request identifier.
    request_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DirectoryLimits(ShapeBase):
    """
    Contains directory limit information for a region.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cloud_only_directories_limit",
                "CloudOnlyDirectoriesLimit",
                TypeInfo(int),
            ),
            (
                "cloud_only_directories_current_count",
                "CloudOnlyDirectoriesCurrentCount",
                TypeInfo(int),
            ),
            (
                "cloud_only_directories_limit_reached",
                "CloudOnlyDirectoriesLimitReached",
                TypeInfo(bool),
            ),
            (
                "cloud_only_microsoft_ad_limit",
                "CloudOnlyMicrosoftADLimit",
                TypeInfo(int),
            ),
            (
                "cloud_only_microsoft_ad_current_count",
                "CloudOnlyMicrosoftADCurrentCount",
                TypeInfo(int),
            ),
            (
                "cloud_only_microsoft_ad_limit_reached",
                "CloudOnlyMicrosoftADLimitReached",
                TypeInfo(bool),
            ),
            (
                "connected_directories_limit",
                "ConnectedDirectoriesLimit",
                TypeInfo(int),
            ),
            (
                "connected_directories_current_count",
                "ConnectedDirectoriesCurrentCount",
                TypeInfo(int),
            ),
            (
                "connected_directories_limit_reached",
                "ConnectedDirectoriesLimitReached",
                TypeInfo(bool),
            ),
        ]

    # The maximum number of cloud directories allowed in the region.
    cloud_only_directories_limit: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The current number of cloud directories in the region.
    cloud_only_directories_current_count: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Indicates if the cloud directory limit has been reached.
    cloud_only_directories_limit_reached: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The maximum number of Microsoft AD directories allowed in the region.
    cloud_only_microsoft_ad_limit: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The current number of Microsoft AD directories in the region.
    cloud_only_microsoft_ad_current_count: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Indicates if the Microsoft AD directory limit has been reached.
    cloud_only_microsoft_ad_limit_reached: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The maximum number of connected directories allowed in the region.
    connected_directories_limit: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The current number of connected directories in the region.
    connected_directories_current_count: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Indicates if the connected directory limit has been reached.
    connected_directories_limit_reached: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class DirectorySize(str):
    Small = "Small"
    Large = "Large"


class DirectoryStage(str):
    Requested = "Requested"
    Creating = "Creating"
    Created = "Created"
    Active = "Active"
    Inoperable = "Inoperable"
    Impaired = "Impaired"
    Restoring = "Restoring"
    RestoreFailed = "RestoreFailed"
    Deleting = "Deleting"
    Deleted = "Deleted"
    Failed = "Failed"


class DirectoryType(str):
    SimpleAD = "SimpleAD"
    ADConnector = "ADConnector"
    MicrosoftAD = "MicrosoftAD"


@dataclasses.dataclass
class DirectoryUnavailableException(ShapeBase):
    """
    The specified directory is unavailable or could not be found.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
            (
                "request_id",
                "RequestId",
                TypeInfo(str),
            ),
        ]

    # The descriptive message for the exception.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The AWS request identifier.
    request_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DirectoryVpcSettings(ShapeBase):
    """
    Contains VPC information for the CreateDirectory or CreateMicrosoftAD operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "vpc_id",
                "VpcId",
                TypeInfo(str),
            ),
            (
                "subnet_ids",
                "SubnetIds",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The identifier of the VPC in which to create the directory.
    vpc_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identifiers of the subnets for the directory servers. The two subnets
    # must be in different Availability Zones. AWS Directory Service creates a
    # directory server and a DNS server in each of these subnets.
    subnet_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DirectoryVpcSettingsDescription(ShapeBase):
    """
    Contains information about the directory.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "vpc_id",
                "VpcId",
                TypeInfo(str),
            ),
            (
                "subnet_ids",
                "SubnetIds",
                TypeInfo(typing.List[str]),
            ),
            (
                "security_group_id",
                "SecurityGroupId",
                TypeInfo(str),
            ),
            (
                "availability_zones",
                "AvailabilityZones",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The identifier of the VPC that the directory is in.
    vpc_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identifiers of the subnets for the directory servers.
    subnet_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The domain controller security group identifier for the directory.
    security_group_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The list of Availability Zones that the directory is in.
    availability_zones: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DisableRadiusRequest(ShapeBase):
    """
    Contains the inputs for the DisableRadius operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "directory_id",
                "DirectoryId",
                TypeInfo(str),
            ),
        ]

    # The identifier of the directory for which to disable MFA.
    directory_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DisableRadiusResult(OutputShapeBase):
    """
    Contains the results of the DisableRadius operation.
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
class DisableSsoRequest(ShapeBase):
    """
    Contains the inputs for the DisableSso operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "directory_id",
                "DirectoryId",
                TypeInfo(str),
            ),
            (
                "user_name",
                "UserName",
                TypeInfo(str),
            ),
            (
                "password",
                "Password",
                TypeInfo(str),
            ),
        ]

    # The identifier of the directory for which to disable single-sign on.
    directory_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The username of an alternate account to use to disable single-sign on. This
    # is only used for AD Connector directories. This account must have
    # privileges to remove a service principal name.

    # If the AD Connector service account does not have privileges to remove a
    # service principal name, you can specify an alternate account with the
    # _UserName_ and _Password_ parameters. These credentials are only used to
    # disable single sign-on and are not stored by the service. The AD Connector
    # service account is not changed.
    user_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The password of an alternate account to use to disable single-sign on. This
    # is only used for AD Connector directories. For more information, see the
    # _UserName_ parameter.
    password: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DisableSsoResult(OutputShapeBase):
    """
    Contains the results of the DisableSso operation.
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
class DomainController(ShapeBase):
    """
    Contains information about the domain controllers for a specified directory.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "directory_id",
                "DirectoryId",
                TypeInfo(str),
            ),
            (
                "domain_controller_id",
                "DomainControllerId",
                TypeInfo(str),
            ),
            (
                "dns_ip_addr",
                "DnsIpAddr",
                TypeInfo(str),
            ),
            (
                "vpc_id",
                "VpcId",
                TypeInfo(str),
            ),
            (
                "subnet_id",
                "SubnetId",
                TypeInfo(str),
            ),
            (
                "availability_zone",
                "AvailabilityZone",
                TypeInfo(str),
            ),
            (
                "status",
                "Status",
                TypeInfo(typing.Union[str, DomainControllerStatus]),
            ),
            (
                "status_reason",
                "StatusReason",
                TypeInfo(str),
            ),
            (
                "launch_time",
                "LaunchTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "status_last_updated_date_time",
                "StatusLastUpdatedDateTime",
                TypeInfo(datetime.datetime),
            ),
        ]

    # Identifier of the directory where the domain controller resides.
    directory_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Identifies a specific domain controller in the directory.
    domain_controller_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The IP address of the domain controller.
    dns_ip_addr: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identifier of the VPC that contains the domain controller.
    vpc_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Identifier of the subnet in the VPC that contains the domain controller.
    subnet_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Availability Zone where the domain controller is located.
    availability_zone: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the domain controller.
    status: typing.Union[str, "DomainControllerStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A description of the domain controller state.
    status_reason: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies when the domain controller was created.
    launch_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date and time that the status was last updated.
    status_last_updated_date_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DomainControllerLimitExceededException(ShapeBase):
    """
    The maximum allowed number of domain controllers per directory was exceeded. The
    default limit per directory is 20 domain controllers.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
            (
                "request_id",
                "RequestId",
                TypeInfo(str),
            ),
        ]

    # The descriptive message for the exception.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The AWS request identifier.
    request_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class DomainControllerStatus(str):
    Creating = "Creating"
    Active = "Active"
    Impaired = "Impaired"
    Restoring = "Restoring"
    Deleting = "Deleting"
    Deleted = "Deleted"
    Failed = "Failed"


@dataclasses.dataclass
class EnableRadiusRequest(ShapeBase):
    """
    Contains the inputs for the EnableRadius operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "directory_id",
                "DirectoryId",
                TypeInfo(str),
            ),
            (
                "radius_settings",
                "RadiusSettings",
                TypeInfo(RadiusSettings),
            ),
        ]

    # The identifier of the directory for which to enable MFA.
    directory_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A RadiusSettings object that contains information about the RADIUS server.
    radius_settings: "RadiusSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class EnableRadiusResult(OutputShapeBase):
    """
    Contains the results of the EnableRadius operation.
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
class EnableSsoRequest(ShapeBase):
    """
    Contains the inputs for the EnableSso operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "directory_id",
                "DirectoryId",
                TypeInfo(str),
            ),
            (
                "user_name",
                "UserName",
                TypeInfo(str),
            ),
            (
                "password",
                "Password",
                TypeInfo(str),
            ),
        ]

    # The identifier of the directory for which to enable single-sign on.
    directory_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The username of an alternate account to use to enable single-sign on. This
    # is only used for AD Connector directories. This account must have
    # privileges to add a service principal name.

    # If the AD Connector service account does not have privileges to add a
    # service principal name, you can specify an alternate account with the
    # _UserName_ and _Password_ parameters. These credentials are only used to
    # enable single sign-on and are not stored by the service. The AD Connector
    # service account is not changed.
    user_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The password of an alternate account to use to enable single-sign on. This
    # is only used for AD Connector directories. For more information, see the
    # _UserName_ parameter.
    password: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class EnableSsoResult(OutputShapeBase):
    """
    Contains the results of the EnableSso operation.
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
class EntityAlreadyExistsException(ShapeBase):
    """
    The specified entity already exists.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
            (
                "request_id",
                "RequestId",
                TypeInfo(str),
            ),
        ]

    # The descriptive message for the exception.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The AWS request identifier.
    request_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class EntityDoesNotExistException(ShapeBase):
    """
    The specified entity could not be found.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
            (
                "request_id",
                "RequestId",
                TypeInfo(str),
            ),
        ]

    # The descriptive message for the exception.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The AWS request identifier.
    request_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class EventTopic(ShapeBase):
    """
    Information about SNS topic and AWS Directory Service directory associations.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "directory_id",
                "DirectoryId",
                TypeInfo(str),
            ),
            (
                "topic_name",
                "TopicName",
                TypeInfo(str),
            ),
            (
                "topic_arn",
                "TopicArn",
                TypeInfo(str),
            ),
            (
                "created_date_time",
                "CreatedDateTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "status",
                "Status",
                TypeInfo(typing.Union[str, TopicStatus]),
            ),
        ]

    # The Directory ID of an AWS Directory Service directory that will publish
    # status messages to an SNS topic.
    directory_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of an AWS SNS topic the receives status messages from the
    # directory.
    topic_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The SNS topic ARN (Amazon Resource Name).
    topic_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date and time of when you associated your directory with the SNS topic.
    created_date_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The topic registration status.
    status: typing.Union[str, "TopicStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetDirectoryLimitsRequest(ShapeBase):
    """
    Contains the inputs for the GetDirectoryLimits operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class GetDirectoryLimitsResult(OutputShapeBase):
    """
    Contains the results of the GetDirectoryLimits operation.
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
                "directory_limits",
                "DirectoryLimits",
                TypeInfo(DirectoryLimits),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A DirectoryLimits object that contains the directory limits for the current
    # region.
    directory_limits: "DirectoryLimits" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetSnapshotLimitsRequest(ShapeBase):
    """
    Contains the inputs for the GetSnapshotLimits operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "directory_id",
                "DirectoryId",
                TypeInfo(str),
            ),
        ]

    # Contains the identifier of the directory to obtain the limits for.
    directory_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetSnapshotLimitsResult(OutputShapeBase):
    """
    Contains the results of the GetSnapshotLimits operation.
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
                "snapshot_limits",
                "SnapshotLimits",
                TypeInfo(SnapshotLimits),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A SnapshotLimits object that contains the manual snapshot limits for the
    # specified directory.
    snapshot_limits: "SnapshotLimits" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class InsufficientPermissionsException(ShapeBase):
    """
    The account does not have sufficient permission to perform the operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
            (
                "request_id",
                "RequestId",
                TypeInfo(str),
            ),
        ]

    # The descriptive message for the exception.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The AWS request identifier.
    request_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidNextTokenException(ShapeBase):
    """
    The _NextToken_ value is not valid.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
            (
                "request_id",
                "RequestId",
                TypeInfo(str),
            ),
        ]

    # The descriptive message for the exception.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The AWS request identifier.
    request_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidParameterException(ShapeBase):
    """
    One or more parameters are not valid.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
            (
                "request_id",
                "RequestId",
                TypeInfo(str),
            ),
        ]

    # The descriptive message for the exception.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The AWS request identifier.
    request_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidPasswordException(ShapeBase):
    """
    The new password provided by the user does not meet the password complexity
    requirements defined in your directory.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
            (
                "request_id",
                "RequestId",
                TypeInfo(str),
            ),
        ]

    # The descriptive message for the exception.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The AWS request identifier.
    request_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class IpRoute(ShapeBase):
    """
    IP address block. This is often the address block of the DNS server used for
    your on-premises domain.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cidr_ip",
                "CidrIp",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
        ]

    # IP address block using CIDR format, for example 10.0.0.0/24. This is often
    # the address block of the DNS server used for your on-premises domain. For a
    # single IP address use a CIDR address block with /32. For example
    # 10.0.0.0/32.
    cidr_ip: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Description of the address block.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class IpRouteInfo(ShapeBase):
    """
    Information about one or more IP address blocks.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "directory_id",
                "DirectoryId",
                TypeInfo(str),
            ),
            (
                "cidr_ip",
                "CidrIp",
                TypeInfo(str),
            ),
            (
                "ip_route_status_msg",
                "IpRouteStatusMsg",
                TypeInfo(typing.Union[str, IpRouteStatusMsg]),
            ),
            (
                "added_date_time",
                "AddedDateTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "ip_route_status_reason",
                "IpRouteStatusReason",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
        ]

    # Identifier (ID) of the directory associated with the IP addresses.
    directory_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # IP address block in the IpRoute.
    cidr_ip: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the IP address block.
    ip_route_status_msg: typing.Union[str, "IpRouteStatusMsg"
                                     ] = dataclasses.field(
                                         default=ShapeBase.NOT_SET,
                                     )

    # The date and time the address block was added to the directory.
    added_date_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The reason for the IpRouteStatusMsg.
    ip_route_status_reason: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Description of the IpRouteInfo.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class IpRouteLimitExceededException(ShapeBase):
    """
    The maximum allowed number of IP addresses was exceeded. The default limit is
    100 IP address blocks.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
            (
                "request_id",
                "RequestId",
                TypeInfo(str),
            ),
        ]

    # The descriptive message for the exception.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The AWS request identifier.
    request_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class IpRouteStatusMsg(str):
    Adding = "Adding"
    Added = "Added"
    Removing = "Removing"
    Removed = "Removed"
    AddFailed = "AddFailed"
    RemoveFailed = "RemoveFailed"


@dataclasses.dataclass
class ListIpRoutesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "directory_id",
                "DirectoryId",
                TypeInfo(str),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
            (
                "limit",
                "Limit",
                TypeInfo(int),
            ),
        ]

    # Identifier (ID) of the directory for which you want to retrieve the IP
    # addresses.
    directory_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The _ListIpRoutes.NextToken_ value from a previous call to ListIpRoutes.
    # Pass null if this is the first call.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Maximum number of items to return. If this value is zero, the maximum
    # number of items is specified by the limitations of the operation.
    limit: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListIpRoutesResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "ip_routes_info",
                "IpRoutesInfo",
                TypeInfo(typing.List[IpRouteInfo]),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of IpRoutes.
    ip_routes_info: typing.List["IpRouteInfo"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If not null, more results are available. Pass this value for the
    # _NextToken_ parameter in a subsequent call to ListIpRoutes to retrieve the
    # next set of items.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListSchemaExtensionsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "directory_id",
                "DirectoryId",
                TypeInfo(str),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
            (
                "limit",
                "Limit",
                TypeInfo(int),
            ),
        ]

    # The identifier of the directory from which to retrieve the schema extension
    # information.
    directory_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The `ListSchemaExtensions.NextToken` value from a previous call to
    # `ListSchemaExtensions`. Pass null if this is the first call.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of items to return.
    limit: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListSchemaExtensionsResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "schema_extensions_info",
                "SchemaExtensionsInfo",
                TypeInfo(typing.List[SchemaExtensionInfo]),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the schema extensions applied to the directory.
    schema_extensions_info: typing.List["SchemaExtensionInfo"
                                       ] = dataclasses.field(
                                           default=ShapeBase.NOT_SET,
                                       )

    # If not null, more results are available. Pass this value for the
    # `NextToken` parameter in a subsequent call to `ListSchemaExtensions` to
    # retrieve the next set of items.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListTagsForResourceRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_id",
                "ResourceId",
                TypeInfo(str),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
            (
                "limit",
                "Limit",
                TypeInfo(int),
            ),
        ]

    # Identifier (ID) of the directory for which you want to retrieve tags.
    resource_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Reserved for future use.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Reserved for future use.
    limit: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListTagsForResourceResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.List[Tag]),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # List of tags returned by the ListTagsForResource operation.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Reserved for future use.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class RadiusAuthenticationProtocol(str):
    PAP = "PAP"
    CHAP = "CHAP"
    MS_CHAPv1 = "MS-CHAPv1"
    MS_CHAPv2 = "MS-CHAPv2"


@dataclasses.dataclass
class RadiusSettings(ShapeBase):
    """
    Contains information about a Remote Authentication Dial In User Service (RADIUS)
    server.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "radius_servers",
                "RadiusServers",
                TypeInfo(typing.List[str]),
            ),
            (
                "radius_port",
                "RadiusPort",
                TypeInfo(int),
            ),
            (
                "radius_timeout",
                "RadiusTimeout",
                TypeInfo(int),
            ),
            (
                "radius_retries",
                "RadiusRetries",
                TypeInfo(int),
            ),
            (
                "shared_secret",
                "SharedSecret",
                TypeInfo(str),
            ),
            (
                "authentication_protocol",
                "AuthenticationProtocol",
                TypeInfo(typing.Union[str, RadiusAuthenticationProtocol]),
            ),
            (
                "display_label",
                "DisplayLabel",
                TypeInfo(str),
            ),
            (
                "use_same_username",
                "UseSameUsername",
                TypeInfo(bool),
            ),
        ]

    # An array of strings that contains the IP addresses of the RADIUS server
    # endpoints, or the IP addresses of your RADIUS server load balancer.
    radius_servers: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The port that your RADIUS server is using for communications. Your on-
    # premises network must allow inbound traffic over this port from the AWS
    # Directory Service servers.
    radius_port: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The amount of time, in seconds, to wait for the RADIUS server to respond.
    radius_timeout: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of times that communication with the RADIUS server is
    # attempted.
    radius_retries: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Not currently used.
    shared_secret: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The protocol specified for your RADIUS endpoints.
    authentication_protocol: typing.Union[str, "RadiusAuthenticationProtocol"
                                         ] = dataclasses.field(
                                             default=ShapeBase.NOT_SET,
                                         )

    # Not currently used.
    display_label: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Not currently used.
    use_same_username: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


class RadiusStatus(str):
    Creating = "Creating"
    Completed = "Completed"
    Failed = "Failed"


@dataclasses.dataclass
class RegisterEventTopicRequest(ShapeBase):
    """
    Registers a new event topic.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "directory_id",
                "DirectoryId",
                TypeInfo(str),
            ),
            (
                "topic_name",
                "TopicName",
                TypeInfo(str),
            ),
        ]

    # The Directory ID that will publish status messages to the SNS topic.
    directory_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The SNS topic name to which the directory will publish status messages.
    # This SNS topic must be in the same region as the specified Directory ID.
    topic_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RegisterEventTopicResult(OutputShapeBase):
    """
    The result of a RegisterEventTopic request.
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
class RemoveIpRoutesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "directory_id",
                "DirectoryId",
                TypeInfo(str),
            ),
            (
                "cidr_ips",
                "CidrIps",
                TypeInfo(typing.List[str]),
            ),
        ]

    # Identifier (ID) of the directory from which you want to remove the IP
    # addresses.
    directory_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # IP address blocks that you want to remove.
    cidr_ips: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RemoveIpRoutesResult(OutputShapeBase):
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
class RemoveTagsFromResourceRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_id",
                "ResourceId",
                TypeInfo(str),
            ),
            (
                "tag_keys",
                "TagKeys",
                TypeInfo(typing.List[str]),
            ),
        ]

    # Identifier (ID) of the directory from which to remove the tag.
    resource_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The tag key (name) of the tag to be removed.
    tag_keys: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RemoveTagsFromResourceResult(OutputShapeBase):
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


class ReplicationScope(str):
    Domain = "Domain"


@dataclasses.dataclass
class ResetUserPasswordRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "directory_id",
                "DirectoryId",
                TypeInfo(str),
            ),
            (
                "user_name",
                "UserName",
                TypeInfo(str),
            ),
            (
                "new_password",
                "NewPassword",
                TypeInfo(str),
            ),
        ]

    # Identifier of the AWS Managed Microsoft AD or Simple AD directory in which
    # the user resides.
    directory_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The username of the user whose password will be reset.
    user_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The new password that will be reset.
    new_password: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ResetUserPasswordResult(OutputShapeBase):
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
class RestoreFromSnapshotRequest(ShapeBase):
    """
    An object representing the inputs for the RestoreFromSnapshot operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "snapshot_id",
                "SnapshotId",
                TypeInfo(str),
            ),
        ]

    # The identifier of the snapshot to restore from.
    snapshot_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RestoreFromSnapshotResult(OutputShapeBase):
    """
    Contains the results of the RestoreFromSnapshot operation.
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
class SchemaExtensionInfo(ShapeBase):
    """
    Information about a schema extension.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "directory_id",
                "DirectoryId",
                TypeInfo(str),
            ),
            (
                "schema_extension_id",
                "SchemaExtensionId",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "schema_extension_status",
                "SchemaExtensionStatus",
                TypeInfo(typing.Union[str, SchemaExtensionStatus]),
            ),
            (
                "schema_extension_status_reason",
                "SchemaExtensionStatusReason",
                TypeInfo(str),
            ),
            (
                "start_date_time",
                "StartDateTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "end_date_time",
                "EndDateTime",
                TypeInfo(datetime.datetime),
            ),
        ]

    # The identifier of the directory to which the schema extension is applied.
    directory_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identifier of the schema extension.
    schema_extension_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A description of the schema extension.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The current status of the schema extension.
    schema_extension_status: typing.Union[str, "SchemaExtensionStatus"
                                         ] = dataclasses.field(
                                             default=ShapeBase.NOT_SET,
                                         )

    # The reason for the `SchemaExtensionStatus`.
    schema_extension_status_reason: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date and time that the schema extension started being applied to the
    # directory.
    start_date_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date and time that the schema extension was completed.
    end_date_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class SchemaExtensionStatus(str):
    Initializing = "Initializing"
    CreatingSnapshot = "CreatingSnapshot"
    UpdatingSchema = "UpdatingSchema"
    Replicating = "Replicating"
    CancelInProgress = "CancelInProgress"
    RollbackInProgress = "RollbackInProgress"
    Cancelled = "Cancelled"
    Failed = "Failed"
    Completed = "Completed"


@dataclasses.dataclass
class ServiceException(ShapeBase):
    """
    An exception has occurred in AWS Directory Service.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
            (
                "request_id",
                "RequestId",
                TypeInfo(str),
            ),
        ]

    # The descriptive message for the exception.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The AWS request identifier.
    request_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Snapshot(ShapeBase):
    """
    Describes a directory snapshot.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "directory_id",
                "DirectoryId",
                TypeInfo(str),
            ),
            (
                "snapshot_id",
                "SnapshotId",
                TypeInfo(str),
            ),
            (
                "type",
                "Type",
                TypeInfo(typing.Union[str, SnapshotType]),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "status",
                "Status",
                TypeInfo(typing.Union[str, SnapshotStatus]),
            ),
            (
                "start_time",
                "StartTime",
                TypeInfo(datetime.datetime),
            ),
        ]

    # The directory identifier.
    directory_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The snapshot identifier.
    snapshot_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The snapshot type.
    type: typing.Union[str, "SnapshotType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The descriptive name of the snapshot.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The snapshot status.
    status: typing.Union[str, "SnapshotStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date and time that the snapshot was taken.
    start_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class SnapshotLimitExceededException(ShapeBase):
    """
    The maximum number of manual snapshots for the directory has been reached. You
    can use the GetSnapshotLimits operation to determine the snapshot limits for a
    directory.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
            (
                "request_id",
                "RequestId",
                TypeInfo(str),
            ),
        ]

    # The descriptive message for the exception.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The AWS request identifier.
    request_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SnapshotLimits(ShapeBase):
    """
    Contains manual snapshot limit information for a directory.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "manual_snapshots_limit",
                "ManualSnapshotsLimit",
                TypeInfo(int),
            ),
            (
                "manual_snapshots_current_count",
                "ManualSnapshotsCurrentCount",
                TypeInfo(int),
            ),
            (
                "manual_snapshots_limit_reached",
                "ManualSnapshotsLimitReached",
                TypeInfo(bool),
            ),
        ]

    # The maximum number of manual snapshots allowed.
    manual_snapshots_limit: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The current number of manual snapshots of the directory.
    manual_snapshots_current_count: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Indicates if the manual snapshot limit has been reached.
    manual_snapshots_limit_reached: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class SnapshotStatus(str):
    Creating = "Creating"
    Completed = "Completed"
    Failed = "Failed"


class SnapshotType(str):
    Auto = "Auto"
    Manual = "Manual"


@dataclasses.dataclass
class StartSchemaExtensionRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "directory_id",
                "DirectoryId",
                TypeInfo(str),
            ),
            (
                "create_snapshot_before_schema_extension",
                "CreateSnapshotBeforeSchemaExtension",
                TypeInfo(bool),
            ),
            (
                "ldif_content",
                "LdifContent",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
        ]

    # The identifier of the directory for which the schema extension will be
    # applied to.
    directory_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If true, creates a snapshot of the directory before applying the schema
    # extension.
    create_snapshot_before_schema_extension: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The LDIF file represented as a string. To construct the LdifContent string,
    # precede each line as it would be formatted in an ldif file with \n. See the
    # example request below for more details. The file size can be no larger than
    # 1MB.
    ldif_content: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A description of the schema extension.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StartSchemaExtensionResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "schema_extension_id",
                "SchemaExtensionId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The identifier of the schema extension that will be applied.
    schema_extension_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Tag(ShapeBase):
    """
    Metadata assigned to a directory consisting of a key-value pair.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "key",
                "Key",
                TypeInfo(str),
            ),
            (
                "value",
                "Value",
                TypeInfo(str),
            ),
        ]

    # Required name of the tag. The string value can be Unicode characters and
    # cannot be prefixed with "aws:". The string can contain only the set of
    # Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java
    # regex: "^([\\\p{L}\\\p{Z}\\\p{N}_.:/=+\\\\-]*)$").
    key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The optional value of the tag. The string value can be Unicode characters.
    # The string can contain only the set of Unicode letters, digits, white-
    # space, '_', '.', '/', '=', '+', '-' (Java regex:
    # "^([\\\p{L}\\\p{Z}\\\p{N}_.:/=+\\\\-]*)$").
    value: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TagLimitExceededException(ShapeBase):
    """
    The maximum allowed number of tags was exceeded.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
            (
                "request_id",
                "RequestId",
                TypeInfo(str),
            ),
        ]

    # The descriptive message for the exception.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The AWS request identifier.
    request_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class TopicStatus(str):
    Registered = "Registered"
    Topic_not_found = "Topic not found"
    Failed = "Failed"
    Deleted = "Deleted"


@dataclasses.dataclass
class Trust(ShapeBase):
    """
    Describes a trust relationship between an Microsoft AD in the AWS cloud and an
    external domain.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "directory_id",
                "DirectoryId",
                TypeInfo(str),
            ),
            (
                "trust_id",
                "TrustId",
                TypeInfo(str),
            ),
            (
                "remote_domain_name",
                "RemoteDomainName",
                TypeInfo(str),
            ),
            (
                "trust_type",
                "TrustType",
                TypeInfo(typing.Union[str, TrustType]),
            ),
            (
                "trust_direction",
                "TrustDirection",
                TypeInfo(typing.Union[str, TrustDirection]),
            ),
            (
                "trust_state",
                "TrustState",
                TypeInfo(typing.Union[str, TrustState]),
            ),
            (
                "created_date_time",
                "CreatedDateTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "last_updated_date_time",
                "LastUpdatedDateTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "state_last_updated_date_time",
                "StateLastUpdatedDateTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "trust_state_reason",
                "TrustStateReason",
                TypeInfo(str),
            ),
        ]

    # The Directory ID of the AWS directory involved in the trust relationship.
    directory_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique ID of the trust relationship.
    trust_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Fully Qualified Domain Name (FQDN) of the external domain involved in
    # the trust relationship.
    remote_domain_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The trust relationship type.
    trust_type: typing.Union[str, "TrustType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The trust relationship direction.
    trust_direction: typing.Union[str, "TrustDirection"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The trust relationship state.
    trust_state: typing.Union[str, "TrustState"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date and time that the trust relationship was created.
    created_date_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date and time that the trust relationship was last updated.
    last_updated_date_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date and time that the TrustState was last updated.
    state_last_updated_date_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The reason for the TrustState.
    trust_state_reason: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class TrustDirection(str):
    One_Way__Outgoing = "One-Way: Outgoing"
    One_Way__Incoming = "One-Way: Incoming"
    Two_Way = "Two-Way"


class TrustState(str):
    Creating = "Creating"
    Created = "Created"
    Verifying = "Verifying"
    VerifyFailed = "VerifyFailed"
    Verified = "Verified"
    Deleting = "Deleting"
    Deleted = "Deleted"
    Failed = "Failed"


class TrustType(str):
    Forest = "Forest"


@dataclasses.dataclass
class UnsupportedOperationException(ShapeBase):
    """
    The operation is not supported.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
            (
                "request_id",
                "RequestId",
                TypeInfo(str),
            ),
        ]

    # The descriptive message for the exception.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The AWS request identifier.
    request_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateConditionalForwarderRequest(ShapeBase):
    """
    Updates a conditional forwarder.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "directory_id",
                "DirectoryId",
                TypeInfo(str),
            ),
            (
                "remote_domain_name",
                "RemoteDomainName",
                TypeInfo(str),
            ),
            (
                "dns_ip_addrs",
                "DnsIpAddrs",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The directory ID of the AWS directory for which to update the conditional
    # forwarder.
    directory_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The fully qualified domain name (FQDN) of the remote domain with which you
    # will set up a trust relationship.
    remote_domain_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The updated IP addresses of the remote DNS server associated with the
    # conditional forwarder.
    dns_ip_addrs: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateConditionalForwarderResult(OutputShapeBase):
    """
    The result of an UpdateConditionalForwarder request.
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
class UpdateNumberOfDomainControllersRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "directory_id",
                "DirectoryId",
                TypeInfo(str),
            ),
            (
                "desired_number",
                "DesiredNumber",
                TypeInfo(int),
            ),
        ]

    # Identifier of the directory to which the domain controllers will be added
    # or removed.
    directory_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of domain controllers desired in the directory.
    desired_number: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateNumberOfDomainControllersResult(OutputShapeBase):
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
class UpdateRadiusRequest(ShapeBase):
    """
    Contains the inputs for the UpdateRadius operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "directory_id",
                "DirectoryId",
                TypeInfo(str),
            ),
            (
                "radius_settings",
                "RadiusSettings",
                TypeInfo(RadiusSettings),
            ),
        ]

    # The identifier of the directory for which to update the RADIUS server
    # information.
    directory_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A RadiusSettings object that contains information about the RADIUS server.
    radius_settings: "RadiusSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateRadiusResult(OutputShapeBase):
    """
    Contains the results of the UpdateRadius operation.
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
class UserDoesNotExistException(ShapeBase):
    """
    The user provided a username that does not exist in your directory.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
            (
                "request_id",
                "RequestId",
                TypeInfo(str),
            ),
        ]

    # The descriptive message for the exception.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The AWS request identifier.
    request_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class VerifyTrustRequest(ShapeBase):
    """
    Initiates the verification of an existing trust relationship between a Microsoft
    AD in the AWS cloud and an external domain.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "trust_id",
                "TrustId",
                TypeInfo(str),
            ),
        ]

    # The unique Trust ID of the trust relationship to verify.
    trust_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class VerifyTrustResult(OutputShapeBase):
    """
    Result of a VerifyTrust request.
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
                "trust_id",
                "TrustId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The unique Trust ID of the trust relationship that was verified.
    trust_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )
