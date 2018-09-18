import datetime
import typing
from autoboto import ShapeBase, OutputShapeBase, TypeInfo
import dataclasses


@dataclasses.dataclass
class AccessDeniedException(ShapeBase):
    """
    Lightsail throws this exception when the user cannot be authenticated or uses
    invalid credentials to access a resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "code",
                "code",
                TypeInfo(str),
            ),
            (
                "docs",
                "docs",
                TypeInfo(str),
            ),
            (
                "message",
                "message",
                TypeInfo(str),
            ),
            (
                "tip",
                "tip",
                TypeInfo(str),
            ),
        ]

    code: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    docs: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    tip: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class AccessDirection(str):
    inbound = "inbound"
    outbound = "outbound"


@dataclasses.dataclass
class AccountSetupInProgressException(ShapeBase):
    """
    Lightsail throws this exception when an account is still in the setup in
    progress state.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "code",
                "code",
                TypeInfo(str),
            ),
            (
                "docs",
                "docs",
                TypeInfo(str),
            ),
            (
                "message",
                "message",
                TypeInfo(str),
            ),
            (
                "tip",
                "tip",
                TypeInfo(str),
            ),
        ]

    code: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    docs: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    tip: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AllocateStaticIpRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "static_ip_name",
                "staticIpName",
                TypeInfo(str),
            ),
        ]

    # The name of the static IP address.
    static_ip_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AllocateStaticIpResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "operations",
                "operations",
                TypeInfo(typing.List[Operation]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An array of key-value pairs containing information about the static IP
    # address you allocated.
    operations: typing.List["Operation"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AttachDiskRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "disk_name",
                "diskName",
                TypeInfo(str),
            ),
            (
                "instance_name",
                "instanceName",
                TypeInfo(str),
            ),
            (
                "disk_path",
                "diskPath",
                TypeInfo(str),
            ),
        ]

    # The unique Lightsail disk name (e.g., `my-disk`).
    disk_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the Lightsail instance where you want to utilize the storage
    # disk.
    instance_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The disk path to expose to the instance (e.g., `/dev/xvdf`).
    disk_path: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AttachDiskResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "operations",
                "operations",
                TypeInfo(typing.List[Operation]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An object describing the API operations.
    operations: typing.List["Operation"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AttachInstancesToLoadBalancerRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "load_balancer_name",
                "loadBalancerName",
                TypeInfo(str),
            ),
            (
                "instance_names",
                "instanceNames",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The name of the load balancer.
    load_balancer_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An array of strings representing the instance name(s) you want to attach to
    # your load balancer.

    # An instance must be `running` before you can attach it to your load
    # balancer.

    # There are no additional limits on the number of instances you can attach to
    # your load balancer, aside from the limit of Lightsail instances you can
    # create in your account (20).
    instance_names: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AttachInstancesToLoadBalancerResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "operations",
                "operations",
                TypeInfo(typing.List[Operation]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An object representing the API operations.
    operations: typing.List["Operation"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AttachLoadBalancerTlsCertificateRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "load_balancer_name",
                "loadBalancerName",
                TypeInfo(str),
            ),
            (
                "certificate_name",
                "certificateName",
                TypeInfo(str),
            ),
        ]

    # The name of the load balancer to which you want to associate the SSL/TLS
    # certificate.
    load_balancer_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of your SSL/TLS certificate.
    certificate_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AttachLoadBalancerTlsCertificateResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "operations",
                "operations",
                TypeInfo(typing.List[Operation]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An object representing the API operations.

    # These SSL/TLS certificates are only usable by Lightsail load balancers. You
    # can't get the certificate and use it for another purpose.
    operations: typing.List["Operation"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AttachStaticIpRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "static_ip_name",
                "staticIpName",
                TypeInfo(str),
            ),
            (
                "instance_name",
                "instanceName",
                TypeInfo(str),
            ),
        ]

    # The name of the static IP.
    static_ip_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The instance name to which you want to attach the static IP address.
    instance_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AttachStaticIpResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "operations",
                "operations",
                TypeInfo(typing.List[Operation]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An array of key-value pairs containing information about your API
    # operations.
    operations: typing.List["Operation"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AvailabilityZone(ShapeBase):
    """
    Describes an Availability Zone.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "zone_name",
                "zoneName",
                TypeInfo(str),
            ),
            (
                "state",
                "state",
                TypeInfo(str),
            ),
        ]

    # The name of the Availability Zone. The format is `us-east-2a` (case-
    # sensitive).
    zone_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The state of the Availability Zone.
    state: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Blueprint(ShapeBase):
    """
    Describes a blueprint (a virtual private server image).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "blueprint_id",
                "blueprintId",
                TypeInfo(str),
            ),
            (
                "name",
                "name",
                TypeInfo(str),
            ),
            (
                "group",
                "group",
                TypeInfo(str),
            ),
            (
                "type",
                "type",
                TypeInfo(typing.Union[str, BlueprintType]),
            ),
            (
                "description",
                "description",
                TypeInfo(str),
            ),
            (
                "is_active",
                "isActive",
                TypeInfo(bool),
            ),
            (
                "min_power",
                "minPower",
                TypeInfo(int),
            ),
            (
                "version",
                "version",
                TypeInfo(str),
            ),
            (
                "version_code",
                "versionCode",
                TypeInfo(str),
            ),
            (
                "product_url",
                "productUrl",
                TypeInfo(str),
            ),
            (
                "license_url",
                "licenseUrl",
                TypeInfo(str),
            ),
            (
                "platform",
                "platform",
                TypeInfo(typing.Union[str, InstancePlatform]),
            ),
        ]

    # The ID for the virtual private server image (e.g., `app_wordpress_4_4` or
    # `app_lamp_7_0`).
    blueprint_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The friendly name of the blueprint (e.g., `Amazon Linux`).
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The group name of the blueprint (e.g., `amazon-linux`).
    group: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of the blueprint (e.g., `os` or `app`).
    type: typing.Union[str, "BlueprintType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The description of the blueprint.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A Boolean value indicating whether the blueprint is active. When you update
    # your blueprints, you will inactivate old blueprints and keep the most
    # recent versions active.
    is_active: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The minimum bundle power required to run this blueprint. For example, you
    # need a bundle with a power value of 500 or more to create an instance that
    # uses a blueprint with a minimum power value of 500. `0` indicates that the
    # blueprint runs on all instance sizes.
    min_power: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The version number of the operating system, application, or stack (e.g.,
    # `2016.03.0`).
    version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The version code.
    version_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The product URL to learn more about the image or blueprint.
    product_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The end-user license agreement URL for the image or blueprint.
    license_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The operating system platform (either Linux/Unix-based or Windows Server-
    # based) of the blueprint.
    platform: typing.Union[str, "InstancePlatform"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class BlueprintType(str):
    os = "os"
    app = "app"


@dataclasses.dataclass
class Bundle(ShapeBase):
    """
    Describes a bundle, which is a set of specs describing your virtual private
    server (or _instance_ ).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "price",
                "price",
                TypeInfo(float),
            ),
            (
                "cpu_count",
                "cpuCount",
                TypeInfo(int),
            ),
            (
                "disk_size_in_gb",
                "diskSizeInGb",
                TypeInfo(int),
            ),
            (
                "bundle_id",
                "bundleId",
                TypeInfo(str),
            ),
            (
                "instance_type",
                "instanceType",
                TypeInfo(str),
            ),
            (
                "is_active",
                "isActive",
                TypeInfo(bool),
            ),
            (
                "name",
                "name",
                TypeInfo(str),
            ),
            (
                "power",
                "power",
                TypeInfo(int),
            ),
            (
                "ram_size_in_gb",
                "ramSizeInGb",
                TypeInfo(float),
            ),
            (
                "transfer_per_month_in_gb",
                "transferPerMonthInGb",
                TypeInfo(int),
            ),
            (
                "supported_platforms",
                "supportedPlatforms",
                TypeInfo(typing.List[typing.Union[str, InstancePlatform]]),
            ),
        ]

    # The price in US dollars (e.g., `5.0`).
    price: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of vCPUs included in the bundle (e.g., `2`).
    cpu_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The size of the SSD (e.g., `30`).
    disk_size_in_gb: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The bundle ID (e.g., `micro_1_0`).
    bundle_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon EC2 instance type (e.g., `t2.micro`).
    instance_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A Boolean value indicating whether the bundle is active.
    is_active: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A friendly name for the bundle (e.g., `Micro`).
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A numeric value that represents the power of the bundle (e.g., `500`). You
    # can use the bundle's power value in conjunction with a blueprint's minimum
    # power value to determine whether the blueprint will run on the bundle. For
    # example, you need a bundle with a power value of 500 or more to create an
    # instance that uses a blueprint with a minimum power value of 500.
    power: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The amount of RAM in GB (e.g., `2.0`).
    ram_size_in_gb: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The data transfer rate per month in GB (e.g., `2000`).
    transfer_per_month_in_gb: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The operating system platform (Linux/Unix-based or Windows Server-based)
    # that the bundle supports. You can only launch a `WINDOWS` bundle on a
    # blueprint that supports the `WINDOWS` platform. `LINUX_UNIX` blueprints
    # require a `LINUX_UNIX` bundle.
    supported_platforms: typing.List[typing.Union[str, "InstancePlatform"]
                                    ] = dataclasses.field(
                                        default=ShapeBase.NOT_SET,
                                    )


@dataclasses.dataclass
class CloseInstancePublicPortsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "port_info",
                "portInfo",
                TypeInfo(PortInfo),
            ),
            (
                "instance_name",
                "instanceName",
                TypeInfo(str),
            ),
        ]

    # Information about the public port you are trying to close.
    port_info: "PortInfo" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the instance on which you're attempting to close the public
    # ports.
    instance_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CloseInstancePublicPortsResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "operation",
                "operation",
                TypeInfo(Operation),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An array of key-value pairs that contains information about the operation.
    operation: "Operation" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateDiskFromSnapshotRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "disk_name",
                "diskName",
                TypeInfo(str),
            ),
            (
                "disk_snapshot_name",
                "diskSnapshotName",
                TypeInfo(str),
            ),
            (
                "availability_zone",
                "availabilityZone",
                TypeInfo(str),
            ),
            (
                "size_in_gb",
                "sizeInGb",
                TypeInfo(int),
            ),
        ]

    # The unique Lightsail disk name (e.g., `my-disk`).
    disk_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the disk snapshot (e.g., `my-snapshot`) from which to create
    # the new storage disk.
    disk_snapshot_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Availability Zone where you want to create the disk (e.g., `us-
    # east-2a`). Choose the same Availability Zone as the Lightsail instance
    # where you want to create the disk.

    # Use the GetRegions operation to list the Availability Zones where Lightsail
    # is currently available.
    availability_zone: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The size of the disk in GB (e.g., `32`).
    size_in_gb: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateDiskFromSnapshotResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "operations",
                "operations",
                TypeInfo(typing.List[Operation]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An object describing the API operations.
    operations: typing.List["Operation"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateDiskRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "disk_name",
                "diskName",
                TypeInfo(str),
            ),
            (
                "availability_zone",
                "availabilityZone",
                TypeInfo(str),
            ),
            (
                "size_in_gb",
                "sizeInGb",
                TypeInfo(int),
            ),
        ]

    # The unique Lightsail disk name (e.g., `my-disk`).
    disk_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Availability Zone where you want to create the disk (e.g., `us-
    # east-2a`). Choose the same Availability Zone as the Lightsail instance
    # where you want to create the disk.

    # Use the GetRegions operation to list the Availability Zones where Lightsail
    # is currently available.
    availability_zone: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The size of the disk in GB (e.g., `32`).
    size_in_gb: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateDiskResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "operations",
                "operations",
                TypeInfo(typing.List[Operation]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An object describing the API operations.
    operations: typing.List["Operation"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateDiskSnapshotRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "disk_name",
                "diskName",
                TypeInfo(str),
            ),
            (
                "disk_snapshot_name",
                "diskSnapshotName",
                TypeInfo(str),
            ),
        ]

    # The unique name of the source disk (e.g., `my-source-disk`).
    disk_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the destination disk snapshot (e.g., `my-disk-snapshot`) based
    # on the source disk.
    disk_snapshot_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateDiskSnapshotResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "operations",
                "operations",
                TypeInfo(typing.List[Operation]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An object describing the API operations.
    operations: typing.List["Operation"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateDomainEntryRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain_name",
                "domainName",
                TypeInfo(str),
            ),
            (
                "domain_entry",
                "domainEntry",
                TypeInfo(DomainEntry),
            ),
        ]

    # The domain name (e.g., `example.com`) for which you want to create the
    # domain entry.
    domain_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An array of key-value pairs containing information about the domain entry
    # request.
    domain_entry: "DomainEntry" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateDomainEntryResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "operation",
                "operation",
                TypeInfo(Operation),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An array of key-value pairs containing information about the operation.
    operation: "Operation" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateDomainRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain_name",
                "domainName",
                TypeInfo(str),
            ),
        ]

    # The domain name to manage (e.g., `example.com`).

    # You cannot register a new domain name using Lightsail. You must register a
    # domain name using Amazon Route 53 or another domain name registrar. If you
    # have already registered your domain, you can enter its name in this
    # parameter to manage the DNS records for that domain.
    domain_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateDomainResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "operation",
                "operation",
                TypeInfo(Operation),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An array of key-value pairs containing information about the domain
    # resource you created.
    operation: "Operation" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateInstanceSnapshotRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "instance_snapshot_name",
                "instanceSnapshotName",
                TypeInfo(str),
            ),
            (
                "instance_name",
                "instanceName",
                TypeInfo(str),
            ),
        ]

    # The name for your new snapshot.
    instance_snapshot_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Lightsail instance on which to base your snapshot.
    instance_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateInstanceSnapshotResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "operations",
                "operations",
                TypeInfo(typing.List[Operation]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An array of key-value pairs containing information about the results of
    # your create instances snapshot request.
    operations: typing.List["Operation"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateInstancesFromSnapshotRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "instance_names",
                "instanceNames",
                TypeInfo(typing.List[str]),
            ),
            (
                "availability_zone",
                "availabilityZone",
                TypeInfo(str),
            ),
            (
                "instance_snapshot_name",
                "instanceSnapshotName",
                TypeInfo(str),
            ),
            (
                "bundle_id",
                "bundleId",
                TypeInfo(str),
            ),
            (
                "attached_disk_mapping",
                "attachedDiskMapping",
                TypeInfo(typing.Dict[str, typing.List[DiskMap]]),
            ),
            (
                "user_data",
                "userData",
                TypeInfo(str),
            ),
            (
                "key_pair_name",
                "keyPairName",
                TypeInfo(str),
            ),
        ]

    # The names for your new instances.
    instance_names: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Availability Zone where you want to create your instances. Use the
    # following formatting: `us-east-2a` (case sensitive). You can get a list of
    # availability zones by using the [get
    # regions](http://docs.aws.amazon.com/lightsail/2016-11-28/api-
    # reference/API_GetRegions.html) operation. Be sure to add the `include
    # availability zones` parameter to your request.
    availability_zone: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the instance snapshot on which you are basing your new
    # instances. Use the get instance snapshots operation to return information
    # about your existing snapshots.
    instance_snapshot_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The bundle of specification information for your virtual private server (or
    # _instance_ ), including the pricing plan (e.g., `micro_1_0`).
    bundle_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An object containing information about one or more disk mappings.
    attached_disk_mapping: typing.Dict[str, typing.
                                       List["DiskMap"]] = dataclasses.field(
                                           default=ShapeBase.NOT_SET,
                                       )

    # You can create a launch script that configures a server with additional
    # user data. For example, `apt-get -y update`.

    # Depending on the machine image you choose, the command to get software on
    # your instance varies. Amazon Linux and CentOS use `yum`, Debian and Ubuntu
    # use `apt-get`, and FreeBSD uses `pkg`. For a complete list, see the [Dev
    # Guide](http://lightsail.aws.amazon.com/ls/docs/getting-
    # started/articles/pre-installed-apps).
    user_data: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name for your key pair.
    key_pair_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateInstancesFromSnapshotResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "operations",
                "operations",
                TypeInfo(typing.List[Operation]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An array of key-value pairs containing information about the results of
    # your create instances from snapshot request.
    operations: typing.List["Operation"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateInstancesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "instance_names",
                "instanceNames",
                TypeInfo(typing.List[str]),
            ),
            (
                "availability_zone",
                "availabilityZone",
                TypeInfo(str),
            ),
            (
                "blueprint_id",
                "blueprintId",
                TypeInfo(str),
            ),
            (
                "bundle_id",
                "bundleId",
                TypeInfo(str),
            ),
            (
                "custom_image_name",
                "customImageName",
                TypeInfo(str),
            ),
            (
                "user_data",
                "userData",
                TypeInfo(str),
            ),
            (
                "key_pair_name",
                "keyPairName",
                TypeInfo(str),
            ),
        ]

    # The names to use for your new Lightsail instances. Separate multiple values
    # using quotation marks and commas, for example:
    # `["MyFirstInstance","MySecondInstance"]`
    instance_names: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Availability Zone in which to create your instance. Use the following
    # format: `us-east-2a` (case sensitive). You can get a list of availability
    # zones by using the [get
    # regions](http://docs.aws.amazon.com/lightsail/2016-11-28/api-
    # reference/API_GetRegions.html) operation. Be sure to add the `include
    # availability zones` parameter to your request.
    availability_zone: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID for a virtual private server image (e.g., `app_wordpress_4_4` or
    # `app_lamp_7_0`). Use the get blueprints operation to return a list of
    # available images (or _blueprints_ ).
    blueprint_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The bundle of specification information for your virtual private server (or
    # _instance_ ), including the pricing plan (e.g., `micro_1_0`).
    bundle_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # (Deprecated) The name for your custom image.

    # In releases prior to June 12, 2017, this parameter was ignored by the API.
    # It is now deprecated.
    custom_image_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A launch script you can create that configures a server with additional
    # user data. For example, you might want to run `apt-get -y update`.

    # Depending on the machine image you choose, the command to get software on
    # your instance varies. Amazon Linux and CentOS use `yum`, Debian and Ubuntu
    # use `apt-get`, and FreeBSD uses `pkg`. For a complete list, see the [Dev
    # Guide](https://lightsail.aws.amazon.com/ls/docs/getting-
    # started/article/compare-options-choose-lightsail-instance-image).
    user_data: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of your key pair.
    key_pair_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateInstancesResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "operations",
                "operations",
                TypeInfo(typing.List[Operation]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An array of key-value pairs containing information about the results of
    # your create instances request.
    operations: typing.List["Operation"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateKeyPairRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "key_pair_name",
                "keyPairName",
                TypeInfo(str),
            ),
        ]

    # The name for your new key pair.
    key_pair_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateKeyPairResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "key_pair",
                "keyPair",
                TypeInfo(KeyPair),
            ),
            (
                "public_key_base64",
                "publicKeyBase64",
                TypeInfo(str),
            ),
            (
                "private_key_base64",
                "privateKeyBase64",
                TypeInfo(str),
            ),
            (
                "operation",
                "operation",
                TypeInfo(Operation),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An array of key-value pairs containing information about the new key pair
    # you just created.
    key_pair: "KeyPair" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A base64-encoded public key of the `ssh-rsa` type.
    public_key_base64: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A base64-encoded RSA private key.
    private_key_base64: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An array of key-value pairs containing information about the results of
    # your create key pair request.
    operation: "Operation" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateLoadBalancerRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "load_balancer_name",
                "loadBalancerName",
                TypeInfo(str),
            ),
            (
                "instance_port",
                "instancePort",
                TypeInfo(int),
            ),
            (
                "health_check_path",
                "healthCheckPath",
                TypeInfo(str),
            ),
            (
                "certificate_name",
                "certificateName",
                TypeInfo(str),
            ),
            (
                "certificate_domain_name",
                "certificateDomainName",
                TypeInfo(str),
            ),
            (
                "certificate_alternative_names",
                "certificateAlternativeNames",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The name of your load balancer.
    load_balancer_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The instance port where you're creating your load balancer.
    instance_port: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The path you provided to perform the load balancer health check. If you
    # didn't specify a health check path, Lightsail uses the root path of your
    # website (e.g., `"/"`).

    # You may want to specify a custom health check path other than the root of
    # your application if your home page loads slowly or has a lot of media or
    # scripting on it.
    health_check_path: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the SSL/TLS certificate.

    # If you specify `certificateName`, then `certificateDomainName` is required
    # (and vice-versa).
    certificate_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The domain name with which your certificate is associated (e.g.,
    # `example.com`).

    # If you specify `certificateDomainName`, then `certificateName` is required
    # (and vice-versa).
    certificate_domain_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The optional alternative domains and subdomains to use with your SSL/TLS
    # certificate (e.g., `www.example.com`, `example.com`, `m.example.com`,
    # `blog.example.com`).
    certificate_alternative_names: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateLoadBalancerResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "operations",
                "operations",
                TypeInfo(typing.List[Operation]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An object containing information about the API operations.
    operations: typing.List["Operation"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateLoadBalancerTlsCertificateRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "load_balancer_name",
                "loadBalancerName",
                TypeInfo(str),
            ),
            (
                "certificate_name",
                "certificateName",
                TypeInfo(str),
            ),
            (
                "certificate_domain_name",
                "certificateDomainName",
                TypeInfo(str),
            ),
            (
                "certificate_alternative_names",
                "certificateAlternativeNames",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The load balancer name where you want to create the SSL/TLS certificate.
    load_balancer_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The SSL/TLS certificate name.

    # You can have up to 10 certificates in your account at one time. Each
    # Lightsail load balancer can have up to 2 certificates associated with it at
    # one time. There is also an overall limit to the number of certificates that
    # can be issue in a 365-day period. For more information, see
    # [Limits](http://docs.aws.amazon.com/acm/latest/userguide/acm-limits.html).
    certificate_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The domain name (e.g., `example.com`) for your SSL/TLS certificate.
    certificate_domain_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An array of strings listing alternative domains and subdomains for your
    # SSL/TLS certificate. Lightsail will de-dupe the names for you. You can have
    # a maximum of 9 alternative names (in addition to the 1 primary domain). We
    # do not support wildcards (e.g., `*.example.com`).
    certificate_alternative_names: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateLoadBalancerTlsCertificateResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "operations",
                "operations",
                TypeInfo(typing.List[Operation]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An object containing information about the API operations.
    operations: typing.List["Operation"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteDiskRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "disk_name",
                "diskName",
                TypeInfo(str),
            ),
        ]

    # The unique name of the disk you want to delete (e.g., `my-disk`).
    disk_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteDiskResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "operations",
                "operations",
                TypeInfo(typing.List[Operation]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An object describing the API operations.
    operations: typing.List["Operation"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteDiskSnapshotRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "disk_snapshot_name",
                "diskSnapshotName",
                TypeInfo(str),
            ),
        ]

    # The name of the disk snapshot you want to delete (e.g., `my-disk-
    # snapshot`).
    disk_snapshot_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteDiskSnapshotResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "operations",
                "operations",
                TypeInfo(typing.List[Operation]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An object describing the API operations.
    operations: typing.List["Operation"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteDomainEntryRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain_name",
                "domainName",
                TypeInfo(str),
            ),
            (
                "domain_entry",
                "domainEntry",
                TypeInfo(DomainEntry),
            ),
        ]

    # The name of the domain entry to delete.
    domain_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An array of key-value pairs containing information about your domain
    # entries.
    domain_entry: "DomainEntry" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteDomainEntryResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "operation",
                "operation",
                TypeInfo(Operation),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An array of key-value pairs containing information about the results of
    # your delete domain entry request.
    operation: "Operation" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteDomainRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain_name",
                "domainName",
                TypeInfo(str),
            ),
        ]

    # The specific domain name to delete.
    domain_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteDomainResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "operation",
                "operation",
                TypeInfo(Operation),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An array of key-value pairs containing information about the results of
    # your delete domain request.
    operation: "Operation" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteInstanceRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "instance_name",
                "instanceName",
                TypeInfo(str),
            ),
        ]

    # The name of the instance to delete.
    instance_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteInstanceResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "operations",
                "operations",
                TypeInfo(typing.List[Operation]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An array of key-value pairs containing information about the results of
    # your delete instance request.
    operations: typing.List["Operation"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteInstanceSnapshotRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "instance_snapshot_name",
                "instanceSnapshotName",
                TypeInfo(str),
            ),
        ]

    # The name of the snapshot to delete.
    instance_snapshot_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteInstanceSnapshotResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "operations",
                "operations",
                TypeInfo(typing.List[Operation]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An array of key-value pairs containing information about the results of
    # your delete instance snapshot request.
    operations: typing.List["Operation"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteKeyPairRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "key_pair_name",
                "keyPairName",
                TypeInfo(str),
            ),
        ]

    # The name of the key pair to delete.
    key_pair_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteKeyPairResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "operation",
                "operation",
                TypeInfo(Operation),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An array of key-value pairs containing information about the results of
    # your delete key pair request.
    operation: "Operation" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteLoadBalancerRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "load_balancer_name",
                "loadBalancerName",
                TypeInfo(str),
            ),
        ]

    # The name of the load balancer you want to delete.
    load_balancer_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteLoadBalancerResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "operations",
                "operations",
                TypeInfo(typing.List[Operation]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An object describing the API operations.
    operations: typing.List["Operation"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteLoadBalancerTlsCertificateRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "load_balancer_name",
                "loadBalancerName",
                TypeInfo(str),
            ),
            (
                "certificate_name",
                "certificateName",
                TypeInfo(str),
            ),
            (
                "force",
                "force",
                TypeInfo(bool),
            ),
        ]

    # The load balancer name.
    load_balancer_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The SSL/TLS certificate name.
    certificate_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # When `true`, forces the deletion of an SSL/TLS certificate.

    # There can be two certificates associated with a Lightsail load balancer:
    # the primary and the backup. The force parameter is required when the
    # primary SSL/TLS certificate is in use by an instance attached to the load
    # balancer.
    force: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteLoadBalancerTlsCertificateResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "operations",
                "operations",
                TypeInfo(typing.List[Operation]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An object describing the API operations.
    operations: typing.List["Operation"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DetachDiskRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "disk_name",
                "diskName",
                TypeInfo(str),
            ),
        ]

    # The unique name of the disk you want to detach from your instance (e.g.,
    # `my-disk`).
    disk_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DetachDiskResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "operations",
                "operations",
                TypeInfo(typing.List[Operation]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An object describing the API operations.
    operations: typing.List["Operation"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DetachInstancesFromLoadBalancerRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "load_balancer_name",
                "loadBalancerName",
                TypeInfo(str),
            ),
            (
                "instance_names",
                "instanceNames",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The name of the Lightsail load balancer.
    load_balancer_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An array of strings containing the names of the instances you want to
    # detach from the load balancer.
    instance_names: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DetachInstancesFromLoadBalancerResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "operations",
                "operations",
                TypeInfo(typing.List[Operation]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An object describing the API operations.
    operations: typing.List["Operation"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DetachStaticIpRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "static_ip_name",
                "staticIpName",
                TypeInfo(str),
            ),
        ]

    # The name of the static IP to detach from the instance.
    static_ip_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DetachStaticIpResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "operations",
                "operations",
                TypeInfo(typing.List[Operation]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An array of key-value pairs containing information about the results of
    # your detach static IP request.
    operations: typing.List["Operation"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class Disk(ShapeBase):
    """
    Describes a system disk or an block storage disk.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "name",
                TypeInfo(str),
            ),
            (
                "arn",
                "arn",
                TypeInfo(str),
            ),
            (
                "support_code",
                "supportCode",
                TypeInfo(str),
            ),
            (
                "created_at",
                "createdAt",
                TypeInfo(datetime.datetime),
            ),
            (
                "location",
                "location",
                TypeInfo(ResourceLocation),
            ),
            (
                "resource_type",
                "resourceType",
                TypeInfo(typing.Union[str, ResourceType]),
            ),
            (
                "size_in_gb",
                "sizeInGb",
                TypeInfo(int),
            ),
            (
                "is_system_disk",
                "isSystemDisk",
                TypeInfo(bool),
            ),
            (
                "iops",
                "iops",
                TypeInfo(int),
            ),
            (
                "path",
                "path",
                TypeInfo(str),
            ),
            (
                "state",
                "state",
                TypeInfo(typing.Union[str, DiskState]),
            ),
            (
                "attached_to",
                "attachedTo",
                TypeInfo(str),
            ),
            (
                "is_attached",
                "isAttached",
                TypeInfo(bool),
            ),
            (
                "attachment_state",
                "attachmentState",
                TypeInfo(str),
            ),
            (
                "gb_in_use",
                "gbInUse",
                TypeInfo(int),
            ),
        ]

    # The unique name of the disk.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the disk.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The support code. Include this code in your email to support when you have
    # questions about an instance or another resource in Lightsail. This code
    # enables our support team to look up your Lightsail information more easily.
    support_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date when the disk was created.
    created_at: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The AWS Region and Availability Zone where the disk is located.
    location: "ResourceLocation" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Lightsail resource type (e.g., `Disk`).
    resource_type: typing.Union[str, "ResourceType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The size of the disk in GB.
    size_in_gb: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A Boolean value indicating whether this disk is a system disk (has an
    # operating system loaded on it).
    is_system_disk: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The input/output operations per second (IOPS) of the disk.
    iops: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The disk path.
    path: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Describes the status of the disk.
    state: typing.Union[str, "DiskState"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The resources to which the disk is attached.
    attached_to: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A Boolean value indicating whether the disk is attached.
    is_attached: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # (Deprecated) The attachment state of the disk.

    # In releases prior to November 14, 2017, this parameter returned `attached`
    # for system disks in the API response. It is now deprecated, but still
    # included in the response. Use `isAttached` instead.
    attachment_state: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # (Deprecated) The number of GB in use by the disk.

    # In releases prior to November 14, 2017, this parameter was not included in
    # the API response. It is now deprecated.
    gb_in_use: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DiskMap(ShapeBase):
    """
    Describes a block storage disk mapping.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "original_disk_path",
                "originalDiskPath",
                TypeInfo(str),
            ),
            (
                "new_disk_name",
                "newDiskName",
                TypeInfo(str),
            ),
        ]

    # The original disk path exposed to the instance (for example, `/dev/sdh`).
    original_disk_path: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The new disk name (e.g., `my-new-disk`).
    new_disk_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DiskSnapshot(ShapeBase):
    """
    Describes a block storage disk snapshot.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "name",
                TypeInfo(str),
            ),
            (
                "arn",
                "arn",
                TypeInfo(str),
            ),
            (
                "support_code",
                "supportCode",
                TypeInfo(str),
            ),
            (
                "created_at",
                "createdAt",
                TypeInfo(datetime.datetime),
            ),
            (
                "location",
                "location",
                TypeInfo(ResourceLocation),
            ),
            (
                "resource_type",
                "resourceType",
                TypeInfo(typing.Union[str, ResourceType]),
            ),
            (
                "size_in_gb",
                "sizeInGb",
                TypeInfo(int),
            ),
            (
                "state",
                "state",
                TypeInfo(typing.Union[str, DiskSnapshotState]),
            ),
            (
                "progress",
                "progress",
                TypeInfo(str),
            ),
            (
                "from_disk_name",
                "fromDiskName",
                TypeInfo(str),
            ),
            (
                "from_disk_arn",
                "fromDiskArn",
                TypeInfo(str),
            ),
        ]

    # The name of the disk snapshot (e.g., `my-disk-snapshot`).
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the disk snapshot.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The support code. Include this code in your email to support when you have
    # questions about an instance or another resource in Lightsail. This code
    # enables our support team to look up your Lightsail information more easily.
    support_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date when the disk snapshot was created.
    created_at: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The AWS Region and Availability Zone where the disk snapshot was created.
    location: "ResourceLocation" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Lightsail resource type (e.g., `DiskSnapshot`).
    resource_type: typing.Union[str, "ResourceType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The size of the disk in GB.
    size_in_gb: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the disk snapshot operation.
    state: typing.Union[str, "DiskSnapshotState"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The progress of the disk snapshot operation.
    progress: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique name of the source disk from which you are creating the disk
    # snapshot.
    from_disk_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the source disk from which you are
    # creating the disk snapshot.
    from_disk_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class DiskSnapshotState(str):
    pending = "pending"
    completed = "completed"
    error = "error"
    unknown = "unknown"


class DiskState(str):
    pending = "pending"
    error = "error"
    available = "available"
    in_use = "in-use"
    unknown = "unknown"


@dataclasses.dataclass
class Domain(ShapeBase):
    """
    Describes a domain where you are storing recordsets in Lightsail.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "name",
                TypeInfo(str),
            ),
            (
                "arn",
                "arn",
                TypeInfo(str),
            ),
            (
                "support_code",
                "supportCode",
                TypeInfo(str),
            ),
            (
                "created_at",
                "createdAt",
                TypeInfo(datetime.datetime),
            ),
            (
                "location",
                "location",
                TypeInfo(ResourceLocation),
            ),
            (
                "resource_type",
                "resourceType",
                TypeInfo(typing.Union[str, ResourceType]),
            ),
            (
                "domain_entries",
                "domainEntries",
                TypeInfo(typing.List[DomainEntry]),
            ),
        ]

    # The name of the domain.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the domain recordset (e.g.,
    # `arn:aws:lightsail:global:123456789101:Domain/824cede0-abc7-4f84-8dbc-12345EXAMPLE`).
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The support code. Include this code in your email to support when you have
    # questions about an instance or another resource in Lightsail. This code
    # enables our support team to look up your Lightsail information more easily.
    support_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date when the domain recordset was created.
    created_at: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The AWS Region and Availability Zones where the domain recordset was
    # created.
    location: "ResourceLocation" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The resource type.
    resource_type: typing.Union[str, "ResourceType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An array of key-value pairs containing information about the domain
    # entries.
    domain_entries: typing.List["DomainEntry"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DomainEntry(ShapeBase):
    """
    Describes a domain recordset entry.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "id",
                TypeInfo(str),
            ),
            (
                "name",
                "name",
                TypeInfo(str),
            ),
            (
                "target",
                "target",
                TypeInfo(str),
            ),
            (
                "is_alias",
                "isAlias",
                TypeInfo(bool),
            ),
            (
                "type",
                "type",
                TypeInfo(str),
            ),
            (
                "options",
                "options",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # The ID of the domain recordset entry.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the domain.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The target AWS name server (e.g., `ns-111.awsdns-22.com.`).

    # For Lightsail load balancers, the value looks like
    # `ab1234c56789c6b86aba6fb203d443bc-123456789.us-east-2.elb.amazonaws.com`.
    # Be sure to also set `isAlias` to `true` when setting up an A record for a
    # load balancer.
    target: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # When `true`, specifies whether the domain entry is an alias used by the
    # Lightsail load balancer. You can include an alias (A type) record in your
    # request, which points to a load balancer DNS name and routes traffic to
    # your load balancer
    is_alias: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of domain entry (e.g., `SOA` or `NS`).
    type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # (Deprecated) The options for the domain entry.

    # In releases prior to November 29, 2017, this parameter was not included in
    # the API response. It is now deprecated.
    options: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DownloadDefaultKeyPairRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DownloadDefaultKeyPairResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "public_key_base64",
                "publicKeyBase64",
                TypeInfo(str),
            ),
            (
                "private_key_base64",
                "privateKeyBase64",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A base64-encoded public key of the `ssh-rsa` type.
    public_key_base64: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A base64-encoded RSA private key.
    private_key_base64: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetActiveNamesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "page_token",
                "pageToken",
                TypeInfo(str),
            ),
        ]

    # A token used for paginating results from your get active names request.
    page_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetActiveNamesResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "active_names",
                "activeNames",
                TypeInfo(typing.List[str]),
            ),
            (
                "next_page_token",
                "nextPageToken",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The list of active names returned by the get active names request.
    active_names: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A token used for advancing to the next page of results from your get active
    # names request.
    next_page_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["GetActiveNamesResult", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class GetBlueprintsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "include_inactive",
                "includeInactive",
                TypeInfo(bool),
            ),
            (
                "page_token",
                "pageToken",
                TypeInfo(str),
            ),
        ]

    # A Boolean value indicating whether to include inactive results in your
    # request.
    include_inactive: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A token used for advancing to the next page of results from your get
    # blueprints request.
    page_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetBlueprintsResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "blueprints",
                "blueprints",
                TypeInfo(typing.List[Blueprint]),
            ),
            (
                "next_page_token",
                "nextPageToken",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An array of key-value pairs that contains information about the available
    # blueprints.
    blueprints: typing.List["Blueprint"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A token used for advancing to the next page of results from your get
    # blueprints request.
    next_page_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self, ) -> typing.Generator["GetBlueprintsResult", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class GetBundlesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "include_inactive",
                "includeInactive",
                TypeInfo(bool),
            ),
            (
                "page_token",
                "pageToken",
                TypeInfo(str),
            ),
        ]

    # A Boolean value that indicates whether to include inactive bundle results
    # in your request.
    include_inactive: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A token used for advancing to the next page of results from your get
    # bundles request.
    page_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetBundlesResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "bundles",
                "bundles",
                TypeInfo(typing.List[Bundle]),
            ),
            (
                "next_page_token",
                "nextPageToken",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An array of key-value pairs that contains information about the available
    # bundles.
    bundles: typing.List["Bundle"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A token used for advancing to the next page of results from your get active
    # names request.
    next_page_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self, ) -> typing.Generator["GetBundlesResult", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class GetDiskRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "disk_name",
                "diskName",
                TypeInfo(str),
            ),
        ]

    # The name of the disk (e.g., `my-disk`).
    disk_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetDiskResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "disk",
                "disk",
                TypeInfo(Disk),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An object containing information about the disk.
    disk: "Disk" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetDiskSnapshotRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "disk_snapshot_name",
                "diskSnapshotName",
                TypeInfo(str),
            ),
        ]

    # The name of the disk snapshot (e.g., `my-disk-snapshot`).
    disk_snapshot_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetDiskSnapshotResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "disk_snapshot",
                "diskSnapshot",
                TypeInfo(DiskSnapshot),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An object containing information about the disk snapshot.
    disk_snapshot: "DiskSnapshot" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetDiskSnapshotsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "page_token",
                "pageToken",
                TypeInfo(str),
            ),
        ]

    # A token used for advancing to the next page of results from your
    # GetDiskSnapshots request.
    page_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetDiskSnapshotsResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "disk_snapshots",
                "diskSnapshots",
                TypeInfo(typing.List[DiskSnapshot]),
            ),
            (
                "next_page_token",
                "nextPageToken",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An array of objects containing information about all block storage disk
    # snapshots.
    disk_snapshots: typing.List["DiskSnapshot"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A token used for advancing to the next page of results from your
    # GetDiskSnapshots request.
    next_page_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetDisksRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "page_token",
                "pageToken",
                TypeInfo(str),
            ),
        ]

    # A token used for advancing to the next page of results from your GetDisks
    # request.
    page_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetDisksResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "disks",
                "disks",
                TypeInfo(typing.List[Disk]),
            ),
            (
                "next_page_token",
                "nextPageToken",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An array of objects containing information about all block storage disks.
    disks: typing.List["Disk"] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A token used for advancing to the next page of results from your GetDisks
    # request.
    next_page_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetDomainRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain_name",
                "domainName",
                TypeInfo(str),
            ),
        ]

    # The domain name for which your want to return information about.
    domain_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetDomainResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "domain",
                "domain",
                TypeInfo(Domain),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An array of key-value pairs containing information about your get domain
    # request.
    domain: "Domain" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetDomainsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "page_token",
                "pageToken",
                TypeInfo(str),
            ),
        ]

    # A token used for advancing to the next page of results from your get
    # domains request.
    page_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetDomainsResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "domains",
                "domains",
                TypeInfo(typing.List[Domain]),
            ),
            (
                "next_page_token",
                "nextPageToken",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An array of key-value pairs containing information about each of the domain
    # entries in the user's account.
    domains: typing.List["Domain"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A token used for advancing to the next page of results from your get active
    # names request.
    next_page_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self, ) -> typing.Generator["GetDomainsResult", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class GetInstanceAccessDetailsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "instance_name",
                "instanceName",
                TypeInfo(str),
            ),
            (
                "protocol",
                "protocol",
                TypeInfo(typing.Union[str, InstanceAccessProtocol]),
            ),
        ]

    # The name of the instance to access.
    instance_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The protocol to use to connect to your instance. Defaults to `ssh`.
    protocol: typing.Union[str, "InstanceAccessProtocol"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetInstanceAccessDetailsResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "access_details",
                "accessDetails",
                TypeInfo(InstanceAccessDetails),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An array of key-value pairs containing information about a get instance
    # access request.
    access_details: "InstanceAccessDetails" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetInstanceMetricDataRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "instance_name",
                "instanceName",
                TypeInfo(str),
            ),
            (
                "metric_name",
                "metricName",
                TypeInfo(typing.Union[str, InstanceMetricName]),
            ),
            (
                "period",
                "period",
                TypeInfo(int),
            ),
            (
                "start_time",
                "startTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "end_time",
                "endTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "unit",
                "unit",
                TypeInfo(typing.Union[str, MetricUnit]),
            ),
            (
                "statistics",
                "statistics",
                TypeInfo(typing.List[typing.Union[str, MetricStatistic]]),
            ),
        ]

    # The name of the instance for which you want to get metrics data.
    instance_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The metric name to get data about.
    metric_name: typing.Union[str, "InstanceMetricName"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The time period for which you are requesting data.
    period: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The start time of the time period.
    start_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The end time of the time period.
    end_time: datetime.datetime = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unit. The list of valid values is below.
    unit: typing.Union[str, "MetricUnit"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The instance statistics.
    statistics: typing.List[typing.Union[str, "MetricStatistic"]
                           ] = dataclasses.field(
                               default=ShapeBase.NOT_SET,
                           )


@dataclasses.dataclass
class GetInstanceMetricDataResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "metric_name",
                "metricName",
                TypeInfo(typing.Union[str, InstanceMetricName]),
            ),
            (
                "metric_data",
                "metricData",
                TypeInfo(typing.List[MetricDatapoint]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The metric name to return data for.
    metric_name: typing.Union[str, "InstanceMetricName"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An array of key-value pairs containing information about the results of
    # your get instance metric data request.
    metric_data: typing.List["MetricDatapoint"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetInstancePortStatesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "instance_name",
                "instanceName",
                TypeInfo(str),
            ),
        ]

    # The name of the instance.
    instance_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetInstancePortStatesResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "port_states",
                "portStates",
                TypeInfo(typing.List[InstancePortState]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the port states resulting from your request.
    port_states: typing.List["InstancePortState"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetInstanceRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "instance_name",
                "instanceName",
                TypeInfo(str),
            ),
        ]

    # The name of the instance.
    instance_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetInstanceResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "instance",
                "instance",
                TypeInfo(Instance),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An array of key-value pairs containing information about the specified
    # instance.
    instance: "Instance" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetInstanceSnapshotRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "instance_snapshot_name",
                "instanceSnapshotName",
                TypeInfo(str),
            ),
        ]

    # The name of the snapshot for which you are requesting information.
    instance_snapshot_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetInstanceSnapshotResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "instance_snapshot",
                "instanceSnapshot",
                TypeInfo(InstanceSnapshot),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An array of key-value pairs containing information about the results of
    # your get instance snapshot request.
    instance_snapshot: "InstanceSnapshot" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetInstanceSnapshotsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "page_token",
                "pageToken",
                TypeInfo(str),
            ),
        ]

    # A token used for advancing to the next page of results from your get
    # instance snapshots request.
    page_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetInstanceSnapshotsResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "instance_snapshots",
                "instanceSnapshots",
                TypeInfo(typing.List[InstanceSnapshot]),
            ),
            (
                "next_page_token",
                "nextPageToken",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An array of key-value pairs containing information about the results of
    # your get instance snapshots request.
    instance_snapshots: typing.List["InstanceSnapshot"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A token used for advancing to the next page of results from your get
    # instance snapshots request.
    next_page_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["GetInstanceSnapshotsResult", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class GetInstanceStateRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "instance_name",
                "instanceName",
                TypeInfo(str),
            ),
        ]

    # The name of the instance to get state information about.
    instance_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetInstanceStateResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "state",
                "state",
                TypeInfo(InstanceState),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The state of the instance.
    state: "InstanceState" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetInstancesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "page_token",
                "pageToken",
                TypeInfo(str),
            ),
        ]

    # A token used for advancing to the next page of results from your get
    # instances request.
    page_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetInstancesResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "instances",
                "instances",
                TypeInfo(typing.List[Instance]),
            ),
            (
                "next_page_token",
                "nextPageToken",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An array of key-value pairs containing information about your instances.
    instances: typing.List["Instance"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A token used for advancing to the next page of results from your get
    # instances request.
    next_page_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self, ) -> typing.Generator["GetInstancesResult", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class GetKeyPairRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "key_pair_name",
                "keyPairName",
                TypeInfo(str),
            ),
        ]

    # The name of the key pair for which you are requesting information.
    key_pair_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetKeyPairResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "key_pair",
                "keyPair",
                TypeInfo(KeyPair),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An array of key-value pairs containing information about the key pair.
    key_pair: "KeyPair" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetKeyPairsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "page_token",
                "pageToken",
                TypeInfo(str),
            ),
        ]

    # A token used for advancing to the next page of results from your get key
    # pairs request.
    page_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetKeyPairsResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "key_pairs",
                "keyPairs",
                TypeInfo(typing.List[KeyPair]),
            ),
            (
                "next_page_token",
                "nextPageToken",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An array of key-value pairs containing information about the key pairs.
    key_pairs: typing.List["KeyPair"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A token used for advancing to the next page of results from your get key
    # pairs request.
    next_page_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self, ) -> typing.Generator["GetKeyPairsResult", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class GetLoadBalancerMetricDataRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "load_balancer_name",
                "loadBalancerName",
                TypeInfo(str),
            ),
            (
                "metric_name",
                "metricName",
                TypeInfo(typing.Union[str, LoadBalancerMetricName]),
            ),
            (
                "period",
                "period",
                TypeInfo(int),
            ),
            (
                "start_time",
                "startTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "end_time",
                "endTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "unit",
                "unit",
                TypeInfo(typing.Union[str, MetricUnit]),
            ),
            (
                "statistics",
                "statistics",
                TypeInfo(typing.List[typing.Union[str, MetricStatistic]]),
            ),
        ]

    # The name of the load balancer.
    load_balancer_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The metric about which you want to return information. Valid values are
    # listed below, along with the most useful `statistics` to include in your
    # request.

    #   * **`ClientTLSNegotiationErrorCount` ** \- The number of TLS connections initiated by the client that did not establish a session with the load balancer. Possible causes include a mismatch of ciphers or protocols.

    # `Statistics`: The most useful statistic is `Sum`.

    #   * **`HealthyHostCount` ** \- The number of target instances that are considered healthy.

    # `Statistics`: The most useful statistic are `Average`, `Minimum`, and
    # `Maximum`.

    #   * **`UnhealthyHostCount` ** \- The number of target instances that are considered unhealthy.

    # `Statistics`: The most useful statistic are `Average`, `Minimum`, and
    # `Maximum`.

    #   * **`HTTPCode_LB_4XX_Count` ** \- The number of HTTP 4XX client error codes that originate from the load balancer. Client errors are generated when requests are malformed or incomplete. These requests have not been received by the target instance. This count does not include any response codes generated by the target instances.

    # `Statistics`: The most useful statistic is `Sum`. Note that `Minimum`,
    # `Maximum`, and `Average` all return `1`.

    #   * **`HTTPCode_LB_5XX_Count` ** \- The number of HTTP 5XX server error codes that originate from the load balancer. This count does not include any response codes generated by the target instances.

    # `Statistics`: The most useful statistic is `Sum`. Note that `Minimum`,
    # `Maximum`, and `Average` all return `1`. Note that `Minimum`, `Maximum`,
    # and `Average` all return `1`.

    #   * **`HTTPCode_Instance_2XX_Count` ** \- The number of HTTP response codes generated by the target instances. This does not include any response codes generated by the load balancer.

    # `Statistics`: The most useful statistic is `Sum`. Note that `Minimum`,
    # `Maximum`, and `Average` all return `1`.

    #   * **`HTTPCode_Instance_3XX_Count` ** \- The number of HTTP response codes generated by the target instances. This does not include any response codes generated by the load balancer.

    # `Statistics`: The most useful statistic is `Sum`. Note that `Minimum`,
    # `Maximum`, and `Average` all return `1`.

    #   * **`HTTPCode_Instance_4XX_Count` ** \- The number of HTTP response codes generated by the target instances. This does not include any response codes generated by the load balancer.

    # `Statistics`: The most useful statistic is `Sum`. Note that `Minimum`,
    # `Maximum`, and `Average` all return `1`.

    #   * **`HTTPCode_Instance_5XX_Count` ** \- The number of HTTP response codes generated by the target instances. This does not include any response codes generated by the load balancer.

    # `Statistics`: The most useful statistic is `Sum`. Note that `Minimum`,
    # `Maximum`, and `Average` all return `1`.

    #   * **`InstanceResponseTime` ** \- The time elapsed, in seconds, after the request leaves the load balancer until a response from the target instance is received.

    # `Statistics`: The most useful statistic is `Average`.

    #   * **`RejectedConnectionCount` ** \- The number of connections that were rejected because the load balancer had reached its maximum number of connections.

    # `Statistics`: The most useful statistic is `Sum`.

    #   * **`RequestCount` ** \- The number of requests processed over IPv4. This count includes only the requests with a response generated by a target instance of the load balancer.

    # `Statistics`: The most useful statistic is `Sum`. Note that `Minimum`,
    # `Maximum`, and `Average` all return `1`.
    metric_name: typing.Union[str, "LoadBalancerMetricName"
                             ] = dataclasses.field(
                                 default=ShapeBase.NOT_SET,
                             )

    # The time period duration for your health data request.
    period: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The start time of the period.
    start_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The end time of the period.
    end_time: datetime.datetime = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unit for the time period request. Valid values are listed below.
    unit: typing.Union[str, "MetricUnit"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An array of statistics that you want to request metrics for. Valid values
    # are listed below.

    #   * **`SampleCount` ** \- The count (number) of data points used for the statistical calculation.

    #   * **`Average` ** \- The value of Sum / SampleCount during the specified period. By comparing this statistic with the Minimum and Maximum, you can determine the full scope of a metric and how close the average use is to the Minimum and Maximum. This comparison helps you to know when to increase or decrease your resources as needed.

    #   * **`Sum` ** \- All values submitted for the matching metric added together. This statistic can be useful for determining the total volume of a metric.

    #   * **`Minimum` ** \- The lowest value observed during the specified period. You can use this value to determine low volumes of activity for your application.

    #   * **`Maximum` ** \- The highest value observed during the specified period. You can use this value to determine high volumes of activity for your application.
    statistics: typing.List[typing.Union[str, "MetricStatistic"]
                           ] = dataclasses.field(
                               default=ShapeBase.NOT_SET,
                           )


@dataclasses.dataclass
class GetLoadBalancerMetricDataResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "metric_name",
                "metricName",
                TypeInfo(typing.Union[str, LoadBalancerMetricName]),
            ),
            (
                "metric_data",
                "metricData",
                TypeInfo(typing.List[MetricDatapoint]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The metric about which you are receiving information. Valid values are
    # listed below, along with the most useful `statistics` to include in your
    # request.

    #   * **`ClientTLSNegotiationErrorCount` ** \- The number of TLS connections initiated by the client that did not establish a session with the load balancer. Possible causes include a mismatch of ciphers or protocols.

    # `Statistics`: The most useful statistic is `Sum`.

    #   * **`HealthyHostCount` ** \- The number of target instances that are considered healthy.

    # `Statistics`: The most useful statistic are `Average`, `Minimum`, and
    # `Maximum`.

    #   * **`UnhealthyHostCount` ** \- The number of target instances that are considered unhealthy.

    # `Statistics`: The most useful statistic are `Average`, `Minimum`, and
    # `Maximum`.

    #   * **`HTTPCode_LB_4XX_Count` ** \- The number of HTTP 4XX client error codes that originate from the load balancer. Client errors are generated when requests are malformed or incomplete. These requests have not been received by the target instance. This count does not include any response codes generated by the target instances.

    # `Statistics`: The most useful statistic is `Sum`. Note that `Minimum`,
    # `Maximum`, and `Average` all return `1`.

    #   * **`HTTPCode_LB_5XX_Count` ** \- The number of HTTP 5XX server error codes that originate from the load balancer. This count does not include any response codes generated by the target instances.

    # `Statistics`: The most useful statistic is `Sum`. Note that `Minimum`,
    # `Maximum`, and `Average` all return `1`. Note that `Minimum`, `Maximum`,
    # and `Average` all return `1`.

    #   * **`HTTPCode_Instance_2XX_Count` ** \- The number of HTTP response codes generated by the target instances. This does not include any response codes generated by the load balancer.

    # `Statistics`: The most useful statistic is `Sum`. Note that `Minimum`,
    # `Maximum`, and `Average` all return `1`.

    #   * **`HTTPCode_Instance_3XX_Count` ** \- The number of HTTP response codes generated by the target instances. This does not include any response codes generated by the load balancer.

    # `Statistics`: The most useful statistic is `Sum`. Note that `Minimum`,
    # `Maximum`, and `Average` all return `1`.

    #   * **`HTTPCode_Instance_4XX_Count` ** \- The number of HTTP response codes generated by the target instances. This does not include any response codes generated by the load balancer.

    # `Statistics`: The most useful statistic is `Sum`. Note that `Minimum`,
    # `Maximum`, and `Average` all return `1`.

    #   * **`HTTPCode_Instance_5XX_Count` ** \- The number of HTTP response codes generated by the target instances. This does not include any response codes generated by the load balancer.

    # `Statistics`: The most useful statistic is `Sum`. Note that `Minimum`,
    # `Maximum`, and `Average` all return `1`.

    #   * **`InstanceResponseTime` ** \- The time elapsed, in seconds, after the request leaves the load balancer until a response from the target instance is received.

    # `Statistics`: The most useful statistic is `Average`.

    #   * **`RejectedConnectionCount` ** \- The number of connections that were rejected because the load balancer had reached its maximum number of connections.

    # `Statistics`: The most useful statistic is `Sum`.

    #   * **`RequestCount` ** \- The number of requests processed over IPv4. This count includes only the requests with a response generated by a target instance of the load balancer.

    # `Statistics`: The most useful statistic is `Sum`. Note that `Minimum`,
    # `Maximum`, and `Average` all return `1`.
    metric_name: typing.Union[str, "LoadBalancerMetricName"
                             ] = dataclasses.field(
                                 default=ShapeBase.NOT_SET,
                             )

    # An array of metric datapoint objects.
    metric_data: typing.List["MetricDatapoint"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetLoadBalancerRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "load_balancer_name",
                "loadBalancerName",
                TypeInfo(str),
            ),
        ]

    # The name of the load balancer.
    load_balancer_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetLoadBalancerResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "load_balancer",
                "loadBalancer",
                TypeInfo(LoadBalancer),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An object containing information about your load balancer.
    load_balancer: "LoadBalancer" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetLoadBalancerTlsCertificatesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "load_balancer_name",
                "loadBalancerName",
                TypeInfo(str),
            ),
        ]

    # The name of the load balancer you associated with your SSL/TLS certificate.
    load_balancer_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetLoadBalancerTlsCertificatesResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "tls_certificates",
                "tlsCertificates",
                TypeInfo(typing.List[LoadBalancerTlsCertificate]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An array of LoadBalancerTlsCertificate objects describing your SSL/TLS
    # certificates.
    tls_certificates: typing.List["LoadBalancerTlsCertificate"
                                 ] = dataclasses.field(
                                     default=ShapeBase.NOT_SET,
                                 )


@dataclasses.dataclass
class GetLoadBalancersRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "page_token",
                "pageToken",
                TypeInfo(str),
            ),
        ]

    # A token used for paginating the results from your GetLoadBalancers request.
    page_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetLoadBalancersResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "load_balancers",
                "loadBalancers",
                TypeInfo(typing.List[LoadBalancer]),
            ),
            (
                "next_page_token",
                "nextPageToken",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An array of LoadBalancer objects describing your load balancers.
    load_balancers: typing.List["LoadBalancer"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A token used for advancing to the next page of results from your
    # GetLoadBalancers request.
    next_page_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetOperationRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "operation_id",
                "operationId",
                TypeInfo(str),
            ),
        ]

    # A GUID used to identify the operation.
    operation_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetOperationResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "operation",
                "operation",
                TypeInfo(Operation),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An array of key-value pairs containing information about the results of
    # your get operation request.
    operation: "Operation" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetOperationsForResourceRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_name",
                "resourceName",
                TypeInfo(str),
            ),
            (
                "page_token",
                "pageToken",
                TypeInfo(str),
            ),
        ]

    # The name of the resource for which you are requesting information.
    resource_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A token used for advancing to the next page of results from your get
    # operations for resource request.
    page_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetOperationsForResourceResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "operations",
                "operations",
                TypeInfo(typing.List[Operation]),
            ),
            (
                "next_page_count",
                "nextPageCount",
                TypeInfo(str),
            ),
            (
                "next_page_token",
                "nextPageToken",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An array of key-value pairs containing information about the results of
    # your get operations for resource request.
    operations: typing.List["Operation"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # (Deprecated) Returns the number of pages of results that remain.

    # In releases prior to June 12, 2017, this parameter returned `null` by the
    # API. It is now deprecated, and the API returns the `nextPageToken`
    # parameter instead.
    next_page_count: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An identifier that was returned from the previous call to this operation,
    # which can be used to return the next set of items in the list.
    next_page_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetOperationsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "page_token",
                "pageToken",
                TypeInfo(str),
            ),
        ]

    # A token used for advancing to the next page of results from your get
    # operations request.
    page_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetOperationsResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "operations",
                "operations",
                TypeInfo(typing.List[Operation]),
            ),
            (
                "next_page_token",
                "nextPageToken",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An array of key-value pairs containing information about the results of
    # your get operations request.
    operations: typing.List["Operation"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A token used for advancing to the next page of results from your get
    # operations request.
    next_page_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self, ) -> typing.Generator["GetOperationsResult", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class GetRegionsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "include_availability_zones",
                "includeAvailabilityZones",
                TypeInfo(bool),
            ),
        ]

    # A Boolean value indicating whether to also include Availability Zones in
    # your get regions request. Availability Zones are indicated with a letter:
    # e.g., `us-east-2a`.
    include_availability_zones: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetRegionsResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "regions",
                "regions",
                TypeInfo(typing.List[Region]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An array of key-value pairs containing information about your get regions
    # request.
    regions: typing.List["Region"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetStaticIpRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "static_ip_name",
                "staticIpName",
                TypeInfo(str),
            ),
        ]

    # The name of the static IP in Lightsail.
    static_ip_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetStaticIpResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "static_ip",
                "staticIp",
                TypeInfo(StaticIp),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An array of key-value pairs containing information about the requested
    # static IP.
    static_ip: "StaticIp" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetStaticIpsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "page_token",
                "pageToken",
                TypeInfo(str),
            ),
        ]

    # A token used for advancing to the next page of results from your get static
    # IPs request.
    page_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetStaticIpsResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "static_ips",
                "staticIps",
                TypeInfo(typing.List[StaticIp]),
            ),
            (
                "next_page_token",
                "nextPageToken",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An array of key-value pairs containing information about your get static
    # IPs request.
    static_ips: typing.List["StaticIp"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A token used for advancing to the next page of results from your get static
    # IPs request.
    next_page_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self, ) -> typing.Generator["GetStaticIpsResult", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ImportKeyPairRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "key_pair_name",
                "keyPairName",
                TypeInfo(str),
            ),
            (
                "public_key_base64",
                "publicKeyBase64",
                TypeInfo(str),
            ),
        ]

    # The name of the key pair for which you want to import the public key.
    key_pair_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A base64-encoded public key of the `ssh-rsa` type.
    public_key_base64: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ImportKeyPairResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "operation",
                "operation",
                TypeInfo(Operation),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An array of key-value pairs containing information about the request
    # operation.
    operation: "Operation" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Instance(ShapeBase):
    """
    Describes an instance (a virtual private server).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "name",
                TypeInfo(str),
            ),
            (
                "arn",
                "arn",
                TypeInfo(str),
            ),
            (
                "support_code",
                "supportCode",
                TypeInfo(str),
            ),
            (
                "created_at",
                "createdAt",
                TypeInfo(datetime.datetime),
            ),
            (
                "location",
                "location",
                TypeInfo(ResourceLocation),
            ),
            (
                "resource_type",
                "resourceType",
                TypeInfo(typing.Union[str, ResourceType]),
            ),
            (
                "blueprint_id",
                "blueprintId",
                TypeInfo(str),
            ),
            (
                "blueprint_name",
                "blueprintName",
                TypeInfo(str),
            ),
            (
                "bundle_id",
                "bundleId",
                TypeInfo(str),
            ),
            (
                "is_static_ip",
                "isStaticIp",
                TypeInfo(bool),
            ),
            (
                "private_ip_address",
                "privateIpAddress",
                TypeInfo(str),
            ),
            (
                "public_ip_address",
                "publicIpAddress",
                TypeInfo(str),
            ),
            (
                "ipv6_address",
                "ipv6Address",
                TypeInfo(str),
            ),
            (
                "hardware",
                "hardware",
                TypeInfo(InstanceHardware),
            ),
            (
                "networking",
                "networking",
                TypeInfo(InstanceNetworking),
            ),
            (
                "state",
                "state",
                TypeInfo(InstanceState),
            ),
            (
                "username",
                "username",
                TypeInfo(str),
            ),
            (
                "ssh_key_name",
                "sshKeyName",
                TypeInfo(str),
            ),
        ]

    # The name the user gave the instance (e.g., `Amazon_Linux-1GB-Ohio-1`).
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the instance (e.g.,
    # `arn:aws:lightsail:us-
    # east-2:123456789101:Instance/244ad76f-8aad-4741-809f-12345EXAMPLE`).
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The support code. Include this code in your email to support when you have
    # questions about an instance or another resource in Lightsail. This code
    # enables our support team to look up your Lightsail information more easily.
    support_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The timestamp when the instance was created (e.g., `1479734909.17`).
    created_at: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The region name and availability zone where the instance is located.
    location: "ResourceLocation" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The type of resource (usually `Instance`).
    resource_type: typing.Union[str, "ResourceType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The blueprint ID (e.g., `os_amlinux_2016_03`).
    blueprint_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The friendly name of the blueprint (e.g., `Amazon Linux`).
    blueprint_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The bundle for the instance (e.g., `micro_1_0`).
    bundle_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A Boolean value indicating whether this instance has a static IP assigned
    # to it.
    is_static_ip: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The private IP address of the instance.
    private_ip_address: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The public IP address of the instance.
    public_ip_address: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The IPv6 address of the instance.
    ipv6_address: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The size of the vCPU and the amount of RAM for the instance.
    hardware: "InstanceHardware" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the public ports and monthly data transfer rates for the
    # instance.
    networking: "InstanceNetworking" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The status code and the state (e.g., `running`) for the instance.
    state: "InstanceState" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The user name for connecting to the instance (e.g., `ec2-user`).
    username: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the SSH key being used to connect to the instance (e.g.,
    # `LightsailDefaultKeyPair`).
    ssh_key_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InstanceAccessDetails(ShapeBase):
    """
    The parameters for gaining temporary access to one of your Amazon Lightsail
    instances.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cert_key",
                "certKey",
                TypeInfo(str),
            ),
            (
                "expires_at",
                "expiresAt",
                TypeInfo(datetime.datetime),
            ),
            (
                "ip_address",
                "ipAddress",
                TypeInfo(str),
            ),
            (
                "password",
                "password",
                TypeInfo(str),
            ),
            (
                "password_data",
                "passwordData",
                TypeInfo(PasswordData),
            ),
            (
                "private_key",
                "privateKey",
                TypeInfo(str),
            ),
            (
                "protocol",
                "protocol",
                TypeInfo(typing.Union[str, InstanceAccessProtocol]),
            ),
            (
                "instance_name",
                "instanceName",
                TypeInfo(str),
            ),
            (
                "username",
                "username",
                TypeInfo(str),
            ),
        ]

    # For SSH access, the public key to use when accessing your instance For
    # OpenSSH clients (e.g., command line SSH), you should save this value to
    # `tempkey-cert.pub`.
    cert_key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # For SSH access, the date on which the temporary keys expire.
    expires_at: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The public IP address of the Amazon Lightsail instance.
    ip_address: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # For RDP access, the password for your Amazon Lightsail instance. Password
    # will be an empty string if the password for your new instance is not ready
    # yet. When you create an instance, it can take up to 15 minutes for the
    # instance to be ready.

    # If you create an instance using any key pair other than the default
    # (`LightsailDefaultKeyPair`), `password` will always be an empty string.

    # If you change the Administrator password on the instance, Lightsail will
    # continue to return the original password value. When accessing the instance
    # using RDP, you need to manually enter the Administrator password after
    # changing it from the default.
    password: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # For a Windows Server-based instance, an object with the data you can use to
    # retrieve your password. This is only needed if `password` is empty and the
    # instance is not new (and therefore the password is not ready yet). When you
    # create an instance, it can take up to 15 minutes for the instance to be
    # ready.
    password_data: "PasswordData" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # For SSH access, the temporary private key. For OpenSSH clients (e.g.,
    # command line SSH), you should save this value to `tempkey`).
    private_key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The protocol for these Amazon Lightsail instance access details.
    protocol: typing.Union[str, "InstanceAccessProtocol"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of this Amazon Lightsail instance.
    instance_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The user name to use when logging in to the Amazon Lightsail instance.
    username: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class InstanceAccessProtocol(str):
    ssh = "ssh"
    rdp = "rdp"


@dataclasses.dataclass
class InstanceHardware(ShapeBase):
    """
    Describes the hardware for the instance.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cpu_count",
                "cpuCount",
                TypeInfo(int),
            ),
            (
                "disks",
                "disks",
                TypeInfo(typing.List[Disk]),
            ),
            (
                "ram_size_in_gb",
                "ramSizeInGb",
                TypeInfo(float),
            ),
        ]

    # The number of vCPUs the instance has.
    cpu_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The disks attached to the instance.
    disks: typing.List["Disk"] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The amount of RAM in GB on the instance (e.g., `1.0`).
    ram_size_in_gb: float = dataclasses.field(default=ShapeBase.NOT_SET, )


class InstanceHealthReason(str):
    Lb_RegistrationInProgress = "Lb.RegistrationInProgress"
    Lb_InitialHealthChecking = "Lb.InitialHealthChecking"
    Lb_InternalError = "Lb.InternalError"
    Instance_ResponseCodeMismatch = "Instance.ResponseCodeMismatch"
    Instance_Timeout = "Instance.Timeout"
    Instance_FailedHealthChecks = "Instance.FailedHealthChecks"
    Instance_NotRegistered = "Instance.NotRegistered"
    Instance_NotInUse = "Instance.NotInUse"
    Instance_DeregistrationInProgress = "Instance.DeregistrationInProgress"
    Instance_InvalidState = "Instance.InvalidState"
    Instance_IpUnusable = "Instance.IpUnusable"


class InstanceHealthState(str):
    initial = "initial"
    healthy = "healthy"
    unhealthy = "unhealthy"
    unused = "unused"
    draining = "draining"
    unavailable = "unavailable"


@dataclasses.dataclass
class InstanceHealthSummary(ShapeBase):
    """
    Describes information about the health of the instance.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "instance_name",
                "instanceName",
                TypeInfo(str),
            ),
            (
                "instance_health",
                "instanceHealth",
                TypeInfo(typing.Union[str, InstanceHealthState]),
            ),
            (
                "instance_health_reason",
                "instanceHealthReason",
                TypeInfo(typing.Union[str, InstanceHealthReason]),
            ),
        ]

    # The name of the Lightsail instance for which you are requesting health
    # check data.
    instance_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Describes the overall instance health. Valid values are below.
    instance_health: typing.Union[str, "InstanceHealthState"
                                 ] = dataclasses.field(
                                     default=ShapeBase.NOT_SET,
                                 )

    # More information about the instance health. If the `instanceHealth` is
    # `healthy`, then an `instanceHealthReason` value is not provided.

    # If **`instanceHealth` ** is `initial`, the **`instanceHealthReason` **
    # value can be one of the following:

    #   * **`Lb.RegistrationInProgress` ** \- The target instance is in the process of being registered with the load balancer.

    #   * **`Lb.InitialHealthChecking` ** \- The Lightsail load balancer is still sending the target instance the minimum number of health checks required to determine its health status.

    # If **`instanceHealth` ** is `unhealthy`, the **`instanceHealthReason` **
    # value can be one of the following:

    #   * **`Instance.ResponseCodeMismatch` ** \- The health checks did not return an expected HTTP code.

    #   * **`Instance.Timeout` ** \- The health check requests timed out.

    #   * **`Instance.FailedHealthChecks` ** \- The health checks failed because the connection to the target instance timed out, the target instance response was malformed, or the target instance failed the health check for an unknown reason.

    #   * **`Lb.InternalError` ** \- The health checks failed due to an internal error.

    # If **`instanceHealth` ** is `unused`, the **`instanceHealthReason` ** value
    # can be one of the following:

    #   * **`Instance.NotRegistered` ** \- The target instance is not registered with the target group.

    #   * **`Instance.NotInUse` ** \- The target group is not used by any load balancer, or the target instance is in an Availability Zone that is not enabled for its load balancer.

    #   * **`Instance.IpUnusable` ** \- The target IP address is reserved for use by a Lightsail load balancer.

    #   * **`Instance.InvalidState` ** \- The target is in the stopped or terminated state.

    # If **`instanceHealth` ** is `draining`, the **`instanceHealthReason` **
    # value can be one of the following:

    #   * **`Instance.DeregistrationInProgress` ** \- The target instance is in the process of being deregistered and the deregistration delay period has not expired.
    instance_health_reason: typing.Union[str, "InstanceHealthReason"
                                        ] = dataclasses.field(
                                            default=ShapeBase.NOT_SET,
                                        )


class InstanceMetricName(str):
    CPUUtilization = "CPUUtilization"
    NetworkIn = "NetworkIn"
    NetworkOut = "NetworkOut"
    StatusCheckFailed = "StatusCheckFailed"
    StatusCheckFailed_Instance = "StatusCheckFailed_Instance"
    StatusCheckFailed_System = "StatusCheckFailed_System"


@dataclasses.dataclass
class InstanceNetworking(ShapeBase):
    """
    Describes monthly data transfer rates and port information for an instance.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "monthly_transfer",
                "monthlyTransfer",
                TypeInfo(MonthlyTransfer),
            ),
            (
                "ports",
                "ports",
                TypeInfo(typing.List[InstancePortInfo]),
            ),
        ]

    # The amount of data in GB allocated for monthly data transfers.
    monthly_transfer: "MonthlyTransfer" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An array of key-value pairs containing information about the ports on the
    # instance.
    ports: typing.List["InstancePortInfo"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class InstancePlatform(str):
    LINUX_UNIX = "LINUX_UNIX"
    WINDOWS = "WINDOWS"


@dataclasses.dataclass
class InstancePortInfo(ShapeBase):
    """
    Describes information about the instance ports.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "from_port",
                "fromPort",
                TypeInfo(int),
            ),
            (
                "to_port",
                "toPort",
                TypeInfo(int),
            ),
            (
                "protocol",
                "protocol",
                TypeInfo(typing.Union[str, NetworkProtocol]),
            ),
            (
                "access_from",
                "accessFrom",
                TypeInfo(str),
            ),
            (
                "access_type",
                "accessType",
                TypeInfo(typing.Union[str, PortAccessType]),
            ),
            (
                "common_name",
                "commonName",
                TypeInfo(str),
            ),
            (
                "access_direction",
                "accessDirection",
                TypeInfo(typing.Union[str, AccessDirection]),
            ),
        ]

    # The first port in the range.
    from_port: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The last port in the range.
    to_port: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The protocol being used. Can be one of the following.

    #   * `tcp` \- Transmission Control Protocol (TCP) provides reliable, ordered, and error-checked delivery of streamed data between applications running on hosts communicating by an IP network. If you have an application that doesn't require reliable data stream service, use UDP instead.

    #   * `all` \- All transport layer protocol types. For more general information, see [Transport layer](https://en.wikipedia.org/wiki/Transport_layer) on Wikipedia.

    #   * `udp` \- With User Datagram Protocol (UDP), computer applications can send messages (or datagrams) to other hosts on an Internet Protocol (IP) network. Prior communications are not required to set up transmission channels or data paths. Applications that don't require reliable data stream service can use UDP, which provides a connectionless datagram service that emphasizes reduced latency over reliability. If you do require reliable data stream service, use TCP instead.
    protocol: typing.Union[str, "NetworkProtocol"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The location from which access is allowed (e.g., `Anywhere (0.0.0.0/0)`).
    access_from: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of access (`Public` or `Private`).
    access_type: typing.Union[str, "PortAccessType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The common name.
    common_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The access direction (`inbound` or `outbound`).
    access_direction: typing.Union[str, "AccessDirection"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class InstancePortState(ShapeBase):
    """
    Describes the port state.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "from_port",
                "fromPort",
                TypeInfo(int),
            ),
            (
                "to_port",
                "toPort",
                TypeInfo(int),
            ),
            (
                "protocol",
                "protocol",
                TypeInfo(typing.Union[str, NetworkProtocol]),
            ),
            (
                "state",
                "state",
                TypeInfo(typing.Union[str, PortState]),
            ),
        ]

    # The first port in the range.
    from_port: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The last port in the range.
    to_port: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The protocol being used. Can be one of the following.

    #   * `tcp` \- Transmission Control Protocol (TCP) provides reliable, ordered, and error-checked delivery of streamed data between applications running on hosts communicating by an IP network. If you have an application that doesn't require reliable data stream service, use UDP instead.

    #   * `all` \- All transport layer protocol types. For more general information, see [Transport layer](https://en.wikipedia.org/wiki/Transport_layer) on Wikipedia.

    #   * `udp` \- With User Datagram Protocol (UDP), computer applications can send messages (or datagrams) to other hosts on an Internet Protocol (IP) network. Prior communications are not required to set up transmission channels or data paths. Applications that don't require reliable data stream service can use UDP, which provides a connectionless datagram service that emphasizes reduced latency over reliability. If you do require reliable data stream service, use TCP instead.
    protocol: typing.Union[str, "NetworkProtocol"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies whether the instance port is `open` or `closed`.
    state: typing.Union[str, "PortState"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class InstanceSnapshot(ShapeBase):
    """
    Describes the snapshot of the virtual private server, or _instance_.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "name",
                TypeInfo(str),
            ),
            (
                "arn",
                "arn",
                TypeInfo(str),
            ),
            (
                "support_code",
                "supportCode",
                TypeInfo(str),
            ),
            (
                "created_at",
                "createdAt",
                TypeInfo(datetime.datetime),
            ),
            (
                "location",
                "location",
                TypeInfo(ResourceLocation),
            ),
            (
                "resource_type",
                "resourceType",
                TypeInfo(typing.Union[str, ResourceType]),
            ),
            (
                "state",
                "state",
                TypeInfo(typing.Union[str, InstanceSnapshotState]),
            ),
            (
                "progress",
                "progress",
                TypeInfo(str),
            ),
            (
                "from_attached_disks",
                "fromAttachedDisks",
                TypeInfo(typing.List[Disk]),
            ),
            (
                "from_instance_name",
                "fromInstanceName",
                TypeInfo(str),
            ),
            (
                "from_instance_arn",
                "fromInstanceArn",
                TypeInfo(str),
            ),
            (
                "from_blueprint_id",
                "fromBlueprintId",
                TypeInfo(str),
            ),
            (
                "from_bundle_id",
                "fromBundleId",
                TypeInfo(str),
            ),
            (
                "size_in_gb",
                "sizeInGb",
                TypeInfo(int),
            ),
        ]

    # The name of the snapshot.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the snapshot (e.g.,
    # `arn:aws:lightsail:us-
    # east-2:123456789101:InstanceSnapshot/d23b5706-3322-4d83-81e5-12345EXAMPLE`).
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The support code. Include this code in your email to support when you have
    # questions about an instance or another resource in Lightsail. This code
    # enables our support team to look up your Lightsail information more easily.
    support_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The timestamp when the snapshot was created (e.g., `1479907467.024`).
    created_at: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The region name and availability zone where you created the snapshot.
    location: "ResourceLocation" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The type of resource (usually `InstanceSnapshot`).
    resource_type: typing.Union[str, "ResourceType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The state the snapshot is in.
    state: typing.Union[str, "InstanceSnapshotState"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The progress of the snapshot.
    progress: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An array of disk objects containing information about all block storage
    # disks.
    from_attached_disks: typing.List["Disk"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The instance from which the snapshot was created.
    from_instance_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the instance from which the snapshot was
    # created (e.g., `arn:aws:lightsail:us-
    # east-2:123456789101:Instance/64b8404c-ccb1-430b-8daf-12345EXAMPLE`).
    from_instance_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The blueprint ID from which you created the snapshot (e.g.,
    # `os_debian_8_3`). A blueprint is a virtual private server (or _instance_ )
    # image used to create instances quickly.
    from_blueprint_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The bundle ID from which you created the snapshot (e.g., `micro_1_0`).
    from_bundle_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The size in GB of the SSD.
    size_in_gb: int = dataclasses.field(default=ShapeBase.NOT_SET, )


class InstanceSnapshotState(str):
    pending = "pending"
    error = "error"
    available = "available"


@dataclasses.dataclass
class InstanceState(ShapeBase):
    """
    Describes the virtual private server (or _instance_ ) status.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "code",
                "code",
                TypeInfo(int),
            ),
            (
                "name",
                "name",
                TypeInfo(str),
            ),
        ]

    # The status code for the instance.
    code: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The state of the instance (e.g., `running` or `pending`).
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidInputException(ShapeBase):
    """
    Lightsail throws this exception when user input does not conform to the
    validation rules of an input field.

    Domain-related APIs are only available in the N. Virginia (us-east-1) Region.
    Please set your AWS Region configuration to us-east-1 to create, view, or edit
    these resources.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "code",
                "code",
                TypeInfo(str),
            ),
            (
                "docs",
                "docs",
                TypeInfo(str),
            ),
            (
                "message",
                "message",
                TypeInfo(str),
            ),
            (
                "tip",
                "tip",
                TypeInfo(str),
            ),
        ]

    code: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    docs: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    tip: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class IsVpcPeeredRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class IsVpcPeeredResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "is_peered",
                "isPeered",
                TypeInfo(bool),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Returns `true` if the Lightsail VPC is peered; otherwise, `false`.
    is_peered: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class KeyPair(ShapeBase):
    """
    Describes the SSH key pair.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "name",
                TypeInfo(str),
            ),
            (
                "arn",
                "arn",
                TypeInfo(str),
            ),
            (
                "support_code",
                "supportCode",
                TypeInfo(str),
            ),
            (
                "created_at",
                "createdAt",
                TypeInfo(datetime.datetime),
            ),
            (
                "location",
                "location",
                TypeInfo(ResourceLocation),
            ),
            (
                "resource_type",
                "resourceType",
                TypeInfo(typing.Union[str, ResourceType]),
            ),
            (
                "fingerprint",
                "fingerprint",
                TypeInfo(str),
            ),
        ]

    # The friendly name of the SSH key pair.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the key pair (e.g.,
    # `arn:aws:lightsail:us-
    # east-2:123456789101:KeyPair/05859e3d-331d-48ba-9034-12345EXAMPLE`).
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The support code. Include this code in your email to support when you have
    # questions about an instance or another resource in Lightsail. This code
    # enables our support team to look up your Lightsail information more easily.
    support_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The timestamp when the key pair was created (e.g., `1479816991.349`).
    created_at: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The region name and Availability Zone where the key pair was created.
    location: "ResourceLocation" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The resource type (usually `KeyPair`).
    resource_type: typing.Union[str, "ResourceType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The RSA fingerprint of the key pair.
    fingerprint: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class LoadBalancer(ShapeBase):
    """
    Describes the Lightsail load balancer.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "name",
                TypeInfo(str),
            ),
            (
                "arn",
                "arn",
                TypeInfo(str),
            ),
            (
                "support_code",
                "supportCode",
                TypeInfo(str),
            ),
            (
                "created_at",
                "createdAt",
                TypeInfo(datetime.datetime),
            ),
            (
                "location",
                "location",
                TypeInfo(ResourceLocation),
            ),
            (
                "resource_type",
                "resourceType",
                TypeInfo(typing.Union[str, ResourceType]),
            ),
            (
                "dns_name",
                "dnsName",
                TypeInfo(str),
            ),
            (
                "state",
                "state",
                TypeInfo(typing.Union[str, LoadBalancerState]),
            ),
            (
                "protocol",
                "protocol",
                TypeInfo(typing.Union[str, LoadBalancerProtocol]),
            ),
            (
                "public_ports",
                "publicPorts",
                TypeInfo(typing.List[int]),
            ),
            (
                "health_check_path",
                "healthCheckPath",
                TypeInfo(str),
            ),
            (
                "instance_port",
                "instancePort",
                TypeInfo(int),
            ),
            (
                "instance_health_summary",
                "instanceHealthSummary",
                TypeInfo(typing.List[InstanceHealthSummary]),
            ),
            (
                "tls_certificate_summaries",
                "tlsCertificateSummaries",
                TypeInfo(typing.List[LoadBalancerTlsCertificateSummary]),
            ),
            (
                "configuration_options",
                "configurationOptions",
                TypeInfo(
                    typing.Dict[typing.
                                Union[str, LoadBalancerAttributeName], str]
                ),
            ),
        ]

    # The name of the load balancer (e.g., `my-load-balancer`).
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the load balancer.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The support code. Include this code in your email to support when you have
    # questions about your Lightsail load balancer. This code enables our support
    # team to look up your Lightsail information more easily.
    support_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date when your load balancer was created.
    created_at: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The AWS Region where your load balancer was created (e.g., `us-east-2a`).
    # Lightsail automatically creates your load balancer across Availability
    # Zones.
    location: "ResourceLocation" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The resource type (e.g., `LoadBalancer`.
    resource_type: typing.Union[str, "ResourceType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The DNS name of your Lightsail load balancer.
    dns_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of your load balancer. Valid values are below.
    state: typing.Union[str, "LoadBalancerState"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The protocol you have enabled for your load balancer. Valid values are
    # below.

    # You can't just have `HTTP_HTTPS`, but you can have just `HTTP`.
    protocol: typing.Union[str, "LoadBalancerProtocol"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An array of public port settings for your load balancer. For HTTP, use port
    # 80. For HTTPS, use port 443.
    public_ports: typing.List[int] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The path you specified to perform your health checks. If no path is
    # specified, the load balancer tries to make a request to the default (root)
    # page.
    health_check_path: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The port where the load balancer will direct traffic to your Lightsail
    # instances. For HTTP traffic, it's port 80. For HTTPS traffic, it's port
    # 443.
    instance_port: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An array of InstanceHealthSummary objects describing the health of the load
    # balancer.
    instance_health_summary: typing.List["InstanceHealthSummary"
                                        ] = dataclasses.field(
                                            default=ShapeBase.NOT_SET,
                                        )

    # An array of LoadBalancerTlsCertificateSummary objects that provide
    # additional information about the SSL/TLS certificates. For example, if
    # `true`, the certificate is attached to the load balancer.
    tls_certificate_summaries: typing.List["LoadBalancerTlsCertificateSummary"
                                          ] = dataclasses.field(
                                              default=ShapeBase.NOT_SET,
                                          )

    # A string to string map of the configuration options for your load balancer.
    # Valid values are listed below.
    configuration_options: typing.Dict[typing.
                                       Union[str, "LoadBalancerAttributeName"],
                                       str] = dataclasses.field(
                                           default=ShapeBase.NOT_SET,
                                       )


class LoadBalancerAttributeName(str):
    HealthCheckPath = "HealthCheckPath"
    SessionStickinessEnabled = "SessionStickinessEnabled"
    SessionStickiness_LB_CookieDurationSeconds = "SessionStickiness_LB_CookieDurationSeconds"


class LoadBalancerMetricName(str):
    ClientTLSNegotiationErrorCount = "ClientTLSNegotiationErrorCount"
    HealthyHostCount = "HealthyHostCount"
    UnhealthyHostCount = "UnhealthyHostCount"
    HTTPCode_LB_4XX_Count = "HTTPCode_LB_4XX_Count"
    HTTPCode_LB_5XX_Count = "HTTPCode_LB_5XX_Count"
    HTTPCode_Instance_2XX_Count = "HTTPCode_Instance_2XX_Count"
    HTTPCode_Instance_3XX_Count = "HTTPCode_Instance_3XX_Count"
    HTTPCode_Instance_4XX_Count = "HTTPCode_Instance_4XX_Count"
    HTTPCode_Instance_5XX_Count = "HTTPCode_Instance_5XX_Count"
    InstanceResponseTime = "InstanceResponseTime"
    RejectedConnectionCount = "RejectedConnectionCount"
    RequestCount = "RequestCount"


class LoadBalancerProtocol(str):
    HTTP_HTTPS = "HTTP_HTTPS"
    HTTP = "HTTP"


class LoadBalancerState(str):
    active = "active"
    provisioning = "provisioning"
    active_impaired = "active_impaired"
    failed = "failed"
    unknown = "unknown"


@dataclasses.dataclass
class LoadBalancerTlsCertificate(ShapeBase):
    """
    Describes a load balancer SSL/TLS certificate.

    TLS is just an updated, more secure version of Secure Socket Layer (SSL).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "name",
                TypeInfo(str),
            ),
            (
                "arn",
                "arn",
                TypeInfo(str),
            ),
            (
                "support_code",
                "supportCode",
                TypeInfo(str),
            ),
            (
                "created_at",
                "createdAt",
                TypeInfo(datetime.datetime),
            ),
            (
                "location",
                "location",
                TypeInfo(ResourceLocation),
            ),
            (
                "resource_type",
                "resourceType",
                TypeInfo(typing.Union[str, ResourceType]),
            ),
            (
                "load_balancer_name",
                "loadBalancerName",
                TypeInfo(str),
            ),
            (
                "is_attached",
                "isAttached",
                TypeInfo(bool),
            ),
            (
                "status",
                "status",
                TypeInfo(typing.Union[str, LoadBalancerTlsCertificateStatus]),
            ),
            (
                "domain_name",
                "domainName",
                TypeInfo(str),
            ),
            (
                "domain_validation_records",
                "domainValidationRecords",
                TypeInfo(
                    typing.
                    List[LoadBalancerTlsCertificateDomainValidationRecord]
                ),
            ),
            (
                "failure_reason",
                "failureReason",
                TypeInfo(
                    typing.Union[str, LoadBalancerTlsCertificateFailureReason]
                ),
            ),
            (
                "issued_at",
                "issuedAt",
                TypeInfo(datetime.datetime),
            ),
            (
                "issuer",
                "issuer",
                TypeInfo(str),
            ),
            (
                "key_algorithm",
                "keyAlgorithm",
                TypeInfo(str),
            ),
            (
                "not_after",
                "notAfter",
                TypeInfo(datetime.datetime),
            ),
            (
                "not_before",
                "notBefore",
                TypeInfo(datetime.datetime),
            ),
            (
                "renewal_summary",
                "renewalSummary",
                TypeInfo(LoadBalancerTlsCertificateRenewalSummary),
            ),
            (
                "revocation_reason",
                "revocationReason",
                TypeInfo(
                    typing.
                    Union[str, LoadBalancerTlsCertificateRevocationReason]
                ),
            ),
            (
                "revoked_at",
                "revokedAt",
                TypeInfo(datetime.datetime),
            ),
            (
                "serial",
                "serial",
                TypeInfo(str),
            ),
            (
                "signature_algorithm",
                "signatureAlgorithm",
                TypeInfo(str),
            ),
            (
                "subject",
                "subject",
                TypeInfo(str),
            ),
            (
                "subject_alternative_names",
                "subjectAlternativeNames",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The name of the SSL/TLS certificate (e.g., `my-certificate`).
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the SSL/TLS certificate.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The support code. Include this code in your email to support when you have
    # questions about your Lightsail load balancer or SSL/TLS certificate. This
    # code enables our support team to look up your Lightsail information more
    # easily.
    support_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time when you created your SSL/TLS certificate.
    created_at: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The AWS Region and Availability Zone where you created your certificate.
    location: "ResourceLocation" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The resource type (e.g., `LoadBalancerTlsCertificate`).

    #   * **`Instance` ** \- A Lightsail instance (a virtual private server)

    #   * **`StaticIp` ** \- A static IP address

    #   * **`KeyPair` ** \- The key pair used to connect to a Lightsail instance

    #   * **`InstanceSnapshot` ** \- A Lightsail instance snapshot

    #   * **`Domain` ** \- A DNS zone

    #   * **`PeeredVpc` ** \- A peered VPC

    #   * **`LoadBalancer` ** \- A Lightsail load balancer

    #   * **`LoadBalancerTlsCertificate` ** \- An SSL/TLS certificate associated with a Lightsail load balancer

    #   * **`Disk` ** \- A Lightsail block storage disk

    #   * **`DiskSnapshot` ** \- A block storage disk snapshot
    resource_type: typing.Union[str, "ResourceType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The load balancer name where your SSL/TLS certificate is attached.
    load_balancer_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # When `true`, the SSL/TLS certificate is attached to the Lightsail load
    # balancer.
    is_attached: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the SSL/TLS certificate. Valid values are below.
    status: typing.Union[str, "LoadBalancerTlsCertificateStatus"
                        ] = dataclasses.field(
                            default=ShapeBase.NOT_SET,
                        )

    # The domain name for your SSL/TLS certificate.
    domain_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An array of LoadBalancerTlsCertificateDomainValidationRecord objects
    # describing the records.
    domain_validation_records: typing.List[
        "LoadBalancerTlsCertificateDomainValidationRecord"] = dataclasses.field(
            default=ShapeBase.NOT_SET,
        )

    # The reason for the SSL/TLS certificate validation failure.
    failure_reason: typing.Union[str, "LoadBalancerTlsCertificateFailureReason"
                                ] = dataclasses.field(
                                    default=ShapeBase.NOT_SET,
                                )

    # The time when the SSL/TLS certificate was issued.
    issued_at: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The issuer of the certificate.
    issuer: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The algorithm that was used to generate the key pair (the public and
    # private key).
    key_algorithm: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The timestamp when the SSL/TLS certificate expires.
    not_after: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The timestamp when the SSL/TLS certificate is first valid.
    not_before: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An object containing information about the status of Lightsail's managed
    # renewal for the certificate.
    renewal_summary: "LoadBalancerTlsCertificateRenewalSummary" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The reason the certificate was revoked. Valid values are below.
    revocation_reason: typing.Union[
        str, "LoadBalancerTlsCertificateRevocationReason"] = dataclasses.field(
            default=ShapeBase.NOT_SET,
        )

    # The timestamp when the SSL/TLS certificate was revoked.
    revoked_at: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The serial number of the certificate.
    serial: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The algorithm that was used to sign the certificate.
    signature_algorithm: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the entity that is associated with the public key contained in
    # the certificate.
    subject: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # One or more domains or subdomains included in the certificate. This list
    # contains the domain names that are bound to the public key that is
    # contained in the certificate. The subject alternative names include the
    # canonical domain name (CNAME) of the certificate and additional domain
    # names that can be used to connect to the website, such as `example.com`,
    # `www.example.com`, or `m.example.com`.
    subject_alternative_names: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class LoadBalancerTlsCertificateDomainStatus(str):
    PENDING_VALIDATION = "PENDING_VALIDATION"
    FAILED = "FAILED"
    SUCCESS = "SUCCESS"


@dataclasses.dataclass
class LoadBalancerTlsCertificateDomainValidationOption(ShapeBase):
    """
    Contains information about the domain names on an SSL/TLS certificate that you
    will use to validate domain ownership.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain_name",
                "domainName",
                TypeInfo(str),
            ),
            (
                "validation_status",
                "validationStatus",
                TypeInfo(
                    typing.Union[str, LoadBalancerTlsCertificateDomainStatus]
                ),
            ),
        ]

    # The fully qualified domain name in the certificate request.
    domain_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the domain validation. Valid values are listed below.
    validation_status: typing.Union[
        str, "LoadBalancerTlsCertificateDomainStatus"] = dataclasses.field(
            default=ShapeBase.NOT_SET,
        )


@dataclasses.dataclass
class LoadBalancerTlsCertificateDomainValidationRecord(ShapeBase):
    """
    Describes the validation record of each domain name in the SSL/TLS certificate.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "name",
                TypeInfo(str),
            ),
            (
                "type",
                "type",
                TypeInfo(str),
            ),
            (
                "value",
                "value",
                TypeInfo(str),
            ),
            (
                "validation_status",
                "validationStatus",
                TypeInfo(
                    typing.Union[str, LoadBalancerTlsCertificateDomainStatus]
                ),
            ),
            (
                "domain_name",
                "domainName",
                TypeInfo(str),
            ),
        ]

    # A fully qualified domain name in the certificate. For example,
    # `example.com`.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of validation record. For example, `CNAME` for domain validation.
    type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The value for that type.
    value: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The validation status. Valid values are listed below.
    validation_status: typing.Union[
        str, "LoadBalancerTlsCertificateDomainStatus"] = dataclasses.field(
            default=ShapeBase.NOT_SET,
        )

    # The domain name against which your SSL/TLS certificate was validated.
    domain_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class LoadBalancerTlsCertificateFailureReason(str):
    NO_AVAILABLE_CONTACTS = "NO_AVAILABLE_CONTACTS"
    ADDITIONAL_VERIFICATION_REQUIRED = "ADDITIONAL_VERIFICATION_REQUIRED"
    DOMAIN_NOT_ALLOWED = "DOMAIN_NOT_ALLOWED"
    INVALID_PUBLIC_DOMAIN = "INVALID_PUBLIC_DOMAIN"
    OTHER = "OTHER"


class LoadBalancerTlsCertificateRenewalStatus(str):
    PENDING_AUTO_RENEWAL = "PENDING_AUTO_RENEWAL"
    PENDING_VALIDATION = "PENDING_VALIDATION"
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"


@dataclasses.dataclass
class LoadBalancerTlsCertificateRenewalSummary(ShapeBase):
    """
    Contains information about the status of Lightsail's managed renewal for the
    certificate.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "renewal_status",
                "renewalStatus",
                TypeInfo(
                    typing.Union[str, LoadBalancerTlsCertificateRenewalStatus]
                ),
            ),
            (
                "domain_validation_options",
                "domainValidationOptions",
                TypeInfo(
                    typing.
                    List[LoadBalancerTlsCertificateDomainValidationOption]
                ),
            ),
        ]

    # The status of Lightsail's managed renewal of the certificate. Valid values
    # are listed below.
    renewal_status: typing.Union[str, "LoadBalancerTlsCertificateRenewalStatus"
                                ] = dataclasses.field(
                                    default=ShapeBase.NOT_SET,
                                )

    # Contains information about the validation of each domain name in the
    # certificate, as it pertains to Lightsail's managed renewal. This is
    # different from the initial validation that occurs as a result of the
    # RequestCertificate request.
    domain_validation_options: typing.List[
        "LoadBalancerTlsCertificateDomainValidationOption"] = dataclasses.field(
            default=ShapeBase.NOT_SET,
        )


class LoadBalancerTlsCertificateRevocationReason(str):
    UNSPECIFIED = "UNSPECIFIED"
    KEY_COMPROMISE = "KEY_COMPROMISE"
    CA_COMPROMISE = "CA_COMPROMISE"
    AFFILIATION_CHANGED = "AFFILIATION_CHANGED"
    SUPERCEDED = "SUPERCEDED"
    CESSATION_OF_OPERATION = "CESSATION_OF_OPERATION"
    CERTIFICATE_HOLD = "CERTIFICATE_HOLD"
    REMOVE_FROM_CRL = "REMOVE_FROM_CRL"
    PRIVILEGE_WITHDRAWN = "PRIVILEGE_WITHDRAWN"
    A_A_COMPROMISE = "A_A_COMPROMISE"


class LoadBalancerTlsCertificateStatus(str):
    PENDING_VALIDATION = "PENDING_VALIDATION"
    ISSUED = "ISSUED"
    INACTIVE = "INACTIVE"
    EXPIRED = "EXPIRED"
    VALIDATION_TIMED_OUT = "VALIDATION_TIMED_OUT"
    REVOKED = "REVOKED"
    FAILED = "FAILED"
    UNKNOWN = "UNKNOWN"


@dataclasses.dataclass
class LoadBalancerTlsCertificateSummary(ShapeBase):
    """
    Provides a summary of SSL/TLS certificate metadata.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "name",
                TypeInfo(str),
            ),
            (
                "is_attached",
                "isAttached",
                TypeInfo(bool),
            ),
        ]

    # The name of the SSL/TLS certificate.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # When `true`, the SSL/TLS certificate is attached to the Lightsail load
    # balancer.
    is_attached: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class MetricDatapoint(ShapeBase):
    """
    Describes the metric data point.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "average",
                "average",
                TypeInfo(float),
            ),
            (
                "maximum",
                "maximum",
                TypeInfo(float),
            ),
            (
                "minimum",
                "minimum",
                TypeInfo(float),
            ),
            (
                "sample_count",
                "sampleCount",
                TypeInfo(float),
            ),
            (
                "sum",
                "sum",
                TypeInfo(float),
            ),
            (
                "timestamp",
                "timestamp",
                TypeInfo(datetime.datetime),
            ),
            (
                "unit",
                "unit",
                TypeInfo(typing.Union[str, MetricUnit]),
            ),
        ]

    # The average.
    average: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum.
    maximum: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The minimum.
    minimum: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The sample count.
    sample_count: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The sum.
    sum: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The timestamp (e.g., `1479816991.349`).
    timestamp: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The unit.
    unit: typing.Union[str, "MetricUnit"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class MetricStatistic(str):
    Minimum = "Minimum"
    Maximum = "Maximum"
    Sum = "Sum"
    Average = "Average"
    SampleCount = "SampleCount"


class MetricUnit(str):
    SECONDS = "Seconds"
    MICROSECONDS = "Microseconds"
    MILLISECONDS = "Milliseconds"
    BYTES = "Bytes"
    KILOBYTES = "Kilobytes"
    MEGABYTES = "Megabytes"
    GIGABYTES = "Gigabytes"
    TERABYTES = "Terabytes"
    BITS = "Bits"
    KILOBITS = "Kilobits"
    MEGABITS = "Megabits"
    GIGABITS = "Gigabits"
    TERABITS = "Terabits"
    PERCENT = "Percent"
    COUNT = "Count"
    BYTES_SECOND = "Bytes/Second"
    KILOBYTES_SECOND = "Kilobytes/Second"
    MEGABYTES_SECOND = "Megabytes/Second"
    GIGABYTES_SECOND = "Gigabytes/Second"
    TERABYTES_SECOND = "Terabytes/Second"
    BITS_SECOND = "Bits/Second"
    KILOBITS_SECOND = "Kilobits/Second"
    MEGABITS_SECOND = "Megabits/Second"
    GIGABITS_SECOND = "Gigabits/Second"
    TERABITS_SECOND = "Terabits/Second"
    COUNT_SECOND = "Count/Second"
    NONE = "None"


@dataclasses.dataclass
class MonthlyTransfer(ShapeBase):
    """
    Describes the monthly data transfer in and out of your virtual private server
    (or _instance_ ).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "gb_per_month_allocated",
                "gbPerMonthAllocated",
                TypeInfo(int),
            ),
        ]

    # The amount allocated per month (in GB).
    gb_per_month_allocated: int = dataclasses.field(default=ShapeBase.NOT_SET, )


class NetworkProtocol(str):
    tcp = "tcp"
    all = "all"
    udp = "udp"


@dataclasses.dataclass
class NotFoundException(ShapeBase):
    """
    Lightsail throws this exception when it cannot find a resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "code",
                "code",
                TypeInfo(str),
            ),
            (
                "docs",
                "docs",
                TypeInfo(str),
            ),
            (
                "message",
                "message",
                TypeInfo(str),
            ),
            (
                "tip",
                "tip",
                TypeInfo(str),
            ),
        ]

    code: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    docs: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    tip: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class OpenInstancePublicPortsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "port_info",
                "portInfo",
                TypeInfo(PortInfo),
            ),
            (
                "instance_name",
                "instanceName",
                TypeInfo(str),
            ),
        ]

    # An array of key-value pairs containing information about the port mappings.
    port_info: "PortInfo" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the instance for which you want to open the public ports.
    instance_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class OpenInstancePublicPortsResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "operation",
                "operation",
                TypeInfo(Operation),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An array of key-value pairs containing information about the request
    # operation.
    operation: "Operation" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Operation(ShapeBase):
    """
    Describes the API operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "id",
                TypeInfo(str),
            ),
            (
                "resource_name",
                "resourceName",
                TypeInfo(str),
            ),
            (
                "resource_type",
                "resourceType",
                TypeInfo(typing.Union[str, ResourceType]),
            ),
            (
                "created_at",
                "createdAt",
                TypeInfo(datetime.datetime),
            ),
            (
                "location",
                "location",
                TypeInfo(ResourceLocation),
            ),
            (
                "is_terminal",
                "isTerminal",
                TypeInfo(bool),
            ),
            (
                "operation_details",
                "operationDetails",
                TypeInfo(str),
            ),
            (
                "operation_type",
                "operationType",
                TypeInfo(typing.Union[str, OperationType]),
            ),
            (
                "status",
                "status",
                TypeInfo(typing.Union[str, OperationStatus]),
            ),
            (
                "status_changed_at",
                "statusChangedAt",
                TypeInfo(datetime.datetime),
            ),
            (
                "error_code",
                "errorCode",
                TypeInfo(str),
            ),
            (
                "error_details",
                "errorDetails",
                TypeInfo(str),
            ),
        ]

    # The ID of the operation.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The resource name.
    resource_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The resource type.
    resource_type: typing.Union[str, "ResourceType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The timestamp when the operation was initialized (e.g., `1479816991.349`).
    created_at: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The region and Availability Zone.
    location: "ResourceLocation" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A Boolean value indicating whether the operation is terminal.
    is_terminal: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Details about the operation (e.g., `Debian-1GB-Ohio-1`).
    operation_details: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of operation.
    operation_type: typing.Union[str, "OperationType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The status of the operation.
    status: typing.Union[str, "OperationStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The timestamp when the status was changed (e.g., `1479816991.349`).
    status_changed_at: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The error code.
    error_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The error details.
    error_details: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class OperationFailureException(ShapeBase):
    """
    Lightsail throws this exception when an operation fails to execute.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "code",
                "code",
                TypeInfo(str),
            ),
            (
                "docs",
                "docs",
                TypeInfo(str),
            ),
            (
                "message",
                "message",
                TypeInfo(str),
            ),
            (
                "tip",
                "tip",
                TypeInfo(str),
            ),
        ]

    code: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    docs: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    tip: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class OperationStatus(str):
    NotStarted = "NotStarted"
    Started = "Started"
    Failed = "Failed"
    Completed = "Completed"
    Succeeded = "Succeeded"


class OperationType(str):
    DeleteInstance = "DeleteInstance"
    CreateInstance = "CreateInstance"
    StopInstance = "StopInstance"
    StartInstance = "StartInstance"
    RebootInstance = "RebootInstance"
    OpenInstancePublicPorts = "OpenInstancePublicPorts"
    PutInstancePublicPorts = "PutInstancePublicPorts"
    CloseInstancePublicPorts = "CloseInstancePublicPorts"
    AllocateStaticIp = "AllocateStaticIp"
    ReleaseStaticIp = "ReleaseStaticIp"
    AttachStaticIp = "AttachStaticIp"
    DetachStaticIp = "DetachStaticIp"
    UpdateDomainEntry = "UpdateDomainEntry"
    DeleteDomainEntry = "DeleteDomainEntry"
    CreateDomain = "CreateDomain"
    DeleteDomain = "DeleteDomain"
    CreateInstanceSnapshot = "CreateInstanceSnapshot"
    DeleteInstanceSnapshot = "DeleteInstanceSnapshot"
    CreateInstancesFromSnapshot = "CreateInstancesFromSnapshot"
    CreateLoadBalancer = "CreateLoadBalancer"
    DeleteLoadBalancer = "DeleteLoadBalancer"
    AttachInstancesToLoadBalancer = "AttachInstancesToLoadBalancer"
    DetachInstancesFromLoadBalancer = "DetachInstancesFromLoadBalancer"
    UpdateLoadBalancerAttribute = "UpdateLoadBalancerAttribute"
    CreateLoadBalancerTlsCertificate = "CreateLoadBalancerTlsCertificate"
    DeleteLoadBalancerTlsCertificate = "DeleteLoadBalancerTlsCertificate"
    AttachLoadBalancerTlsCertificate = "AttachLoadBalancerTlsCertificate"
    CreateDisk = "CreateDisk"
    DeleteDisk = "DeleteDisk"
    AttachDisk = "AttachDisk"
    DetachDisk = "DetachDisk"
    CreateDiskSnapshot = "CreateDiskSnapshot"
    DeleteDiskSnapshot = "DeleteDiskSnapshot"
    CreateDiskFromSnapshot = "CreateDiskFromSnapshot"


@dataclasses.dataclass
class PasswordData(ShapeBase):
    """
    The password data for the Windows Server-based instance, including the
    ciphertext and the key pair name.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "ciphertext",
                "ciphertext",
                TypeInfo(str),
            ),
            (
                "key_pair_name",
                "keyPairName",
                TypeInfo(str),
            ),
        ]

    # The encrypted password. Ciphertext will be an empty string if access to
    # your new instance is not ready yet. When you create an instance, it can
    # take up to 15 minutes for the instance to be ready.

    # If you use the default key pair (`LightsailDefaultKeyPair`), the decrypted
    # password will be available in the password field.

    # If you are using a custom key pair, you need to use your own means of
    # decryption.

    # If you change the Administrator password on the instance, Lightsail will
    # continue to return the original ciphertext value. When accessing the
    # instance using RDP, you need to manually enter the Administrator password
    # after changing it from the default.
    ciphertext: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the key pair that you used when creating your instance. If no
    # key pair name was specified when creating the instance, Lightsail uses the
    # default key pair (`LightsailDefaultKeyPair`).

    # If you are using a custom key pair, you need to use your own means of
    # decrypting your password using the `ciphertext`. Lightsail creates the
    # ciphertext by encrypting your password with the public key part of this key
    # pair.
    key_pair_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PeerVpcRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class PeerVpcResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "operation",
                "operation",
                TypeInfo(Operation),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An array of key-value pairs containing information about the request
    # operation.
    operation: "Operation" = dataclasses.field(default=ShapeBase.NOT_SET, )


class PortAccessType(str):
    Public = "Public"
    Private = "Private"


@dataclasses.dataclass
class PortInfo(ShapeBase):
    """
    Describes information about the ports on your virtual private server (or
    _instance_ ).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "from_port",
                "fromPort",
                TypeInfo(int),
            ),
            (
                "to_port",
                "toPort",
                TypeInfo(int),
            ),
            (
                "protocol",
                "protocol",
                TypeInfo(typing.Union[str, NetworkProtocol]),
            ),
        ]

    # The first port in the range.
    from_port: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The last port in the range.
    to_port: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The protocol.
    protocol: typing.Union[str, "NetworkProtocol"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class PortState(str):
    open = "open"
    closed = "closed"


@dataclasses.dataclass
class PutInstancePublicPortsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "port_infos",
                "portInfos",
                TypeInfo(typing.List[PortInfo]),
            ),
            (
                "instance_name",
                "instanceName",
                TypeInfo(str),
            ),
        ]

    # Specifies information about the public port(s).
    port_infos: typing.List["PortInfo"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Lightsail instance name of the public port(s) you are setting.
    instance_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PutInstancePublicPortsResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "operation",
                "operation",
                TypeInfo(Operation),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Describes metadata about the operation you just executed.
    operation: "Operation" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RebootInstanceRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "instance_name",
                "instanceName",
                TypeInfo(str),
            ),
        ]

    # The name of the instance to reboot.
    instance_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RebootInstanceResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "operations",
                "operations",
                TypeInfo(typing.List[Operation]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An array of key-value pairs containing information about the request
    # operations.
    operations: typing.List["Operation"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class Region(ShapeBase):
    """
    Describes the AWS Region.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "continent_code",
                "continentCode",
                TypeInfo(str),
            ),
            (
                "description",
                "description",
                TypeInfo(str),
            ),
            (
                "display_name",
                "displayName",
                TypeInfo(str),
            ),
            (
                "name",
                "name",
                TypeInfo(typing.Union[str, RegionName]),
            ),
            (
                "availability_zones",
                "availabilityZones",
                TypeInfo(typing.List[AvailabilityZone]),
            ),
        ]

    # The continent code (e.g., `NA`, meaning North America).
    continent_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The description of the AWS Region (e.g., `This region is recommended to
    # serve users in the eastern United States and eastern Canada`).
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The display name (e.g., `Ohio`).
    display_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The region name (e.g., `us-east-2`).
    name: typing.Union[str, "RegionName"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Availability Zones. Follows the format `us-east-2a` (case-sensitive).
    availability_zones: typing.List["AvailabilityZone"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class RegionName(str):
    us_east_1 = "us-east-1"
    us_east_2 = "us-east-2"
    us_west_1 = "us-west-1"
    us_west_2 = "us-west-2"
    eu_central_1 = "eu-central-1"
    eu_west_1 = "eu-west-1"
    eu_west_2 = "eu-west-2"
    ap_south_1 = "ap-south-1"
    ap_southeast_1 = "ap-southeast-1"
    ap_southeast_2 = "ap-southeast-2"
    ap_northeast_1 = "ap-northeast-1"
    ap_northeast_2 = "ap-northeast-2"


@dataclasses.dataclass
class ReleaseStaticIpRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "static_ip_name",
                "staticIpName",
                TypeInfo(str),
            ),
        ]

    # The name of the static IP to delete.
    static_ip_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ReleaseStaticIpResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "operations",
                "operations",
                TypeInfo(typing.List[Operation]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An array of key-value pairs containing information about the request
    # operation.
    operations: typing.List["Operation"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ResourceLocation(ShapeBase):
    """
    Describes the resource location.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "availability_zone",
                "availabilityZone",
                TypeInfo(str),
            ),
            (
                "region_name",
                "regionName",
                TypeInfo(typing.Union[str, RegionName]),
            ),
        ]

    # The Availability Zone. Follows the format `us-east-2a` (case-sensitive).
    availability_zone: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The AWS Region name.
    region_name: typing.Union[str, "RegionName"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class ResourceType(str):
    Instance = "Instance"
    StaticIp = "StaticIp"
    KeyPair = "KeyPair"
    InstanceSnapshot = "InstanceSnapshot"
    Domain = "Domain"
    PeeredVpc = "PeeredVpc"
    LoadBalancer = "LoadBalancer"
    LoadBalancerTlsCertificate = "LoadBalancerTlsCertificate"
    Disk = "Disk"
    DiskSnapshot = "DiskSnapshot"


@dataclasses.dataclass
class ServiceException(ShapeBase):
    """
    A general service exception.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "code",
                "code",
                TypeInfo(str),
            ),
            (
                "docs",
                "docs",
                TypeInfo(str),
            ),
            (
                "message",
                "message",
                TypeInfo(str),
            ),
            (
                "tip",
                "tip",
                TypeInfo(str),
            ),
        ]

    code: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    docs: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    tip: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StartInstanceRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "instance_name",
                "instanceName",
                TypeInfo(str),
            ),
        ]

    # The name of the instance (a virtual private server) to start.
    instance_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StartInstanceResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "operations",
                "operations",
                TypeInfo(typing.List[Operation]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An array of key-value pairs containing information about the request
    # operation.
    operations: typing.List["Operation"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class StaticIp(ShapeBase):
    """
    Describes the static IP.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "name",
                TypeInfo(str),
            ),
            (
                "arn",
                "arn",
                TypeInfo(str),
            ),
            (
                "support_code",
                "supportCode",
                TypeInfo(str),
            ),
            (
                "created_at",
                "createdAt",
                TypeInfo(datetime.datetime),
            ),
            (
                "location",
                "location",
                TypeInfo(ResourceLocation),
            ),
            (
                "resource_type",
                "resourceType",
                TypeInfo(typing.Union[str, ResourceType]),
            ),
            (
                "ip_address",
                "ipAddress",
                TypeInfo(str),
            ),
            (
                "attached_to",
                "attachedTo",
                TypeInfo(str),
            ),
            (
                "is_attached",
                "isAttached",
                TypeInfo(bool),
            ),
        ]

    # The name of the static IP (e.g., `StaticIP-Ohio-EXAMPLE`).
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the static IP (e.g.,
    # `arn:aws:lightsail:us-
    # east-2:123456789101:StaticIp/9cbb4a9e-f8e3-4dfe-b57e-12345EXAMPLE`).
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The support code. Include this code in your email to support when you have
    # questions about an instance or another resource in Lightsail. This code
    # enables our support team to look up your Lightsail information more easily.
    support_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The timestamp when the static IP was created (e.g., `1479735304.222`).
    created_at: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The region and Availability Zone where the static IP was created.
    location: "ResourceLocation" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The resource type (usually `StaticIp`).
    resource_type: typing.Union[str, "ResourceType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The static IP address.
    ip_address: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The instance where the static IP is attached (e.g., `Amazon_Linux-1GB-
    # Ohio-1`).
    attached_to: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A Boolean value indicating whether the static IP is attached.
    is_attached: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StopInstanceRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "instance_name",
                "instanceName",
                TypeInfo(str),
            ),
            (
                "force",
                "force",
                TypeInfo(bool),
            ),
        ]

    # The name of the instance (a virtual private server) to stop.
    instance_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # When set to `True`, forces a Lightsail instance that is stuck in a
    # `stopping` state to stop.

    # Only use the `force` parameter if your instance is stuck in the `stopping`
    # state. In any other state, your instance should stop normally without
    # adding this parameter to your API request.
    force: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StopInstanceResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "operations",
                "operations",
                TypeInfo(typing.List[Operation]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An array of key-value pairs containing information about the request
    # operation.
    operations: typing.List["Operation"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UnauthenticatedException(ShapeBase):
    """
    Lightsail throws this exception when the user has not been authenticated.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "code",
                "code",
                TypeInfo(str),
            ),
            (
                "docs",
                "docs",
                TypeInfo(str),
            ),
            (
                "message",
                "message",
                TypeInfo(str),
            ),
            (
                "tip",
                "tip",
                TypeInfo(str),
            ),
        ]

    code: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    docs: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    tip: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UnpeerVpcRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class UnpeerVpcResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "operation",
                "operation",
                TypeInfo(Operation),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An array of key-value pairs containing information about the request
    # operation.
    operation: "Operation" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateDomainEntryRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain_name",
                "domainName",
                TypeInfo(str),
            ),
            (
                "domain_entry",
                "domainEntry",
                TypeInfo(DomainEntry),
            ),
        ]

    # The name of the domain recordset to update.
    domain_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An array of key-value pairs containing information about the domain entry.
    domain_entry: "DomainEntry" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateDomainEntryResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "operations",
                "operations",
                TypeInfo(typing.List[Operation]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An array of key-value pairs containing information about the request
    # operation.
    operations: typing.List["Operation"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateLoadBalancerAttributeRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "load_balancer_name",
                "loadBalancerName",
                TypeInfo(str),
            ),
            (
                "attribute_name",
                "attributeName",
                TypeInfo(typing.Union[str, LoadBalancerAttributeName]),
            ),
            (
                "attribute_value",
                "attributeValue",
                TypeInfo(str),
            ),
        ]

    # The name of the load balancer that you want to modify (e.g., `my-load-
    # balancer`.
    load_balancer_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the attribute you want to update. Valid values are below.
    attribute_name: typing.Union[str, "LoadBalancerAttributeName"
                                ] = dataclasses.field(
                                    default=ShapeBase.NOT_SET,
                                )

    # The value that you want to specify for the attribute name.
    attribute_value: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateLoadBalancerAttributeResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "operations",
                "operations",
                TypeInfo(typing.List[Operation]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An object describing the API operations.
    operations: typing.List["Operation"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )
