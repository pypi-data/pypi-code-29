import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("lightsail", *args, **kwargs)

    def allocate_static_ip(
        self,
        _request: shapes.AllocateStaticIpRequest = None,
        *,
        static_ip_name: str,
    ) -> shapes.AllocateStaticIpResult:
        """
        Allocates a static IP address.
        """
        if _request is None:
            _params = {}
            if static_ip_name is not ShapeBase.NOT_SET:
                _params['static_ip_name'] = static_ip_name
            _request = shapes.AllocateStaticIpRequest(**_params)
        response = self._boto_client.allocate_static_ip(**_request.to_boto())

        return shapes.AllocateStaticIpResult.from_boto(response)

    def attach_disk(
        self,
        _request: shapes.AttachDiskRequest = None,
        *,
        disk_name: str,
        instance_name: str,
        disk_path: str,
    ) -> shapes.AttachDiskResult:
        """
        Attaches a block storage disk to a running or stopped Lightsail instance and
        exposes it to the instance with the specified disk name.
        """
        if _request is None:
            _params = {}
            if disk_name is not ShapeBase.NOT_SET:
                _params['disk_name'] = disk_name
            if instance_name is not ShapeBase.NOT_SET:
                _params['instance_name'] = instance_name
            if disk_path is not ShapeBase.NOT_SET:
                _params['disk_path'] = disk_path
            _request = shapes.AttachDiskRequest(**_params)
        response = self._boto_client.attach_disk(**_request.to_boto())

        return shapes.AttachDiskResult.from_boto(response)

    def attach_instances_to_load_balancer(
        self,
        _request: shapes.AttachInstancesToLoadBalancerRequest = None,
        *,
        load_balancer_name: str,
        instance_names: typing.List[str],
    ) -> shapes.AttachInstancesToLoadBalancerResult:
        """
        Attaches one or more Lightsail instances to a load balancer.

        After some time, the instances are attached to the load balancer and the health
        check status is available.
        """
        if _request is None:
            _params = {}
            if load_balancer_name is not ShapeBase.NOT_SET:
                _params['load_balancer_name'] = load_balancer_name
            if instance_names is not ShapeBase.NOT_SET:
                _params['instance_names'] = instance_names
            _request = shapes.AttachInstancesToLoadBalancerRequest(**_params)
        response = self._boto_client.attach_instances_to_load_balancer(
            **_request.to_boto()
        )

        return shapes.AttachInstancesToLoadBalancerResult.from_boto(response)

    def attach_load_balancer_tls_certificate(
        self,
        _request: shapes.AttachLoadBalancerTlsCertificateRequest = None,
        *,
        load_balancer_name: str,
        certificate_name: str,
    ) -> shapes.AttachLoadBalancerTlsCertificateResult:
        """
        Attaches a Transport Layer Security (TLS) certificate to your load balancer. TLS
        is just an updated, more secure version of Secure Socket Layer (SSL).

        Once you create and validate your certificate, you can attach it to your load
        balancer. You can also use this API to rotate the certificates on your account.
        Use the `AttachLoadBalancerTlsCertificate` operation with the non-attached
        certificate, and it will replace the existing one and become the attached
        certificate.
        """
        if _request is None:
            _params = {}
            if load_balancer_name is not ShapeBase.NOT_SET:
                _params['load_balancer_name'] = load_balancer_name
            if certificate_name is not ShapeBase.NOT_SET:
                _params['certificate_name'] = certificate_name
            _request = shapes.AttachLoadBalancerTlsCertificateRequest(**_params)
        response = self._boto_client.attach_load_balancer_tls_certificate(
            **_request.to_boto()
        )

        return shapes.AttachLoadBalancerTlsCertificateResult.from_boto(response)

    def attach_static_ip(
        self,
        _request: shapes.AttachStaticIpRequest = None,
        *,
        static_ip_name: str,
        instance_name: str,
    ) -> shapes.AttachStaticIpResult:
        """
        Attaches a static IP address to a specific Amazon Lightsail instance.
        """
        if _request is None:
            _params = {}
            if static_ip_name is not ShapeBase.NOT_SET:
                _params['static_ip_name'] = static_ip_name
            if instance_name is not ShapeBase.NOT_SET:
                _params['instance_name'] = instance_name
            _request = shapes.AttachStaticIpRequest(**_params)
        response = self._boto_client.attach_static_ip(**_request.to_boto())

        return shapes.AttachStaticIpResult.from_boto(response)

    def close_instance_public_ports(
        self,
        _request: shapes.CloseInstancePublicPortsRequest = None,
        *,
        port_info: shapes.PortInfo,
        instance_name: str,
    ) -> shapes.CloseInstancePublicPortsResult:
        """
        Closes the public ports on a specific Amazon Lightsail instance.
        """
        if _request is None:
            _params = {}
            if port_info is not ShapeBase.NOT_SET:
                _params['port_info'] = port_info
            if instance_name is not ShapeBase.NOT_SET:
                _params['instance_name'] = instance_name
            _request = shapes.CloseInstancePublicPortsRequest(**_params)
        response = self._boto_client.close_instance_public_ports(
            **_request.to_boto()
        )

        return shapes.CloseInstancePublicPortsResult.from_boto(response)

    def create_disk(
        self,
        _request: shapes.CreateDiskRequest = None,
        *,
        disk_name: str,
        availability_zone: str,
        size_in_gb: int,
    ) -> shapes.CreateDiskResult:
        """
        Creates a block storage disk that can be attached to a Lightsail instance in the
        same Availability Zone (e.g., `us-east-2a`). The disk is created in the regional
        endpoint that you send the HTTP request to. For more information, see [Regions
        and Availability Zones in
        Lightsail](https://lightsail.aws.amazon.com/ls/docs/overview/article/understanding-
        regions-and-availability-zones-in-amazon-lightsail).
        """
        if _request is None:
            _params = {}
            if disk_name is not ShapeBase.NOT_SET:
                _params['disk_name'] = disk_name
            if availability_zone is not ShapeBase.NOT_SET:
                _params['availability_zone'] = availability_zone
            if size_in_gb is not ShapeBase.NOT_SET:
                _params['size_in_gb'] = size_in_gb
            _request = shapes.CreateDiskRequest(**_params)
        response = self._boto_client.create_disk(**_request.to_boto())

        return shapes.CreateDiskResult.from_boto(response)

    def create_disk_from_snapshot(
        self,
        _request: shapes.CreateDiskFromSnapshotRequest = None,
        *,
        disk_name: str,
        disk_snapshot_name: str,
        availability_zone: str,
        size_in_gb: int,
    ) -> shapes.CreateDiskFromSnapshotResult:
        """
        Creates a block storage disk from a disk snapshot that can be attached to a
        Lightsail instance in the same Availability Zone (e.g., `us-east-2a`). The disk
        is created in the regional endpoint that you send the HTTP request to. For more
        information, see [Regions and Availability Zones in
        Lightsail](https://lightsail.aws.amazon.com/ls/docs/overview/article/understanding-
        regions-and-availability-zones-in-amazon-lightsail).
        """
        if _request is None:
            _params = {}
            if disk_name is not ShapeBase.NOT_SET:
                _params['disk_name'] = disk_name
            if disk_snapshot_name is not ShapeBase.NOT_SET:
                _params['disk_snapshot_name'] = disk_snapshot_name
            if availability_zone is not ShapeBase.NOT_SET:
                _params['availability_zone'] = availability_zone
            if size_in_gb is not ShapeBase.NOT_SET:
                _params['size_in_gb'] = size_in_gb
            _request = shapes.CreateDiskFromSnapshotRequest(**_params)
        response = self._boto_client.create_disk_from_snapshot(
            **_request.to_boto()
        )

        return shapes.CreateDiskFromSnapshotResult.from_boto(response)

    def create_disk_snapshot(
        self,
        _request: shapes.CreateDiskSnapshotRequest = None,
        *,
        disk_name: str,
        disk_snapshot_name: str,
    ) -> shapes.CreateDiskSnapshotResult:
        """
        Creates a snapshot of a block storage disk. You can use snapshots for backups,
        to make copies of disks, and to save data before shutting down a Lightsail
        instance.

        You can take a snapshot of an attached disk that is in use; however, snapshots
        only capture data that has been written to your disk at the time the snapshot
        command is issued. This may exclude any data that has been cached by any
        applications or the operating system. If you can pause any file systems on the
        disk long enough to take a snapshot, your snapshot should be complete.
        Nevertheless, if you cannot pause all file writes to the disk, you should
        unmount the disk from within the Lightsail instance, issue the create disk
        snapshot command, and then remount the disk to ensure a consistent and complete
        snapshot. You may remount and use your disk while the snapshot status is
        pending.
        """
        if _request is None:
            _params = {}
            if disk_name is not ShapeBase.NOT_SET:
                _params['disk_name'] = disk_name
            if disk_snapshot_name is not ShapeBase.NOT_SET:
                _params['disk_snapshot_name'] = disk_snapshot_name
            _request = shapes.CreateDiskSnapshotRequest(**_params)
        response = self._boto_client.create_disk_snapshot(**_request.to_boto())

        return shapes.CreateDiskSnapshotResult.from_boto(response)

    def create_domain(
        self,
        _request: shapes.CreateDomainRequest = None,
        *,
        domain_name: str,
    ) -> shapes.CreateDomainResult:
        """
        Creates a domain resource for the specified domain (e.g., example.com).
        """
        if _request is None:
            _params = {}
            if domain_name is not ShapeBase.NOT_SET:
                _params['domain_name'] = domain_name
            _request = shapes.CreateDomainRequest(**_params)
        response = self._boto_client.create_domain(**_request.to_boto())

        return shapes.CreateDomainResult.from_boto(response)

    def create_domain_entry(
        self,
        _request: shapes.CreateDomainEntryRequest = None,
        *,
        domain_name: str,
        domain_entry: shapes.DomainEntry,
    ) -> shapes.CreateDomainEntryResult:
        """
        Creates one of the following entry records associated with the domain: A record,
        CNAME record, TXT record, or MX record.
        """
        if _request is None:
            _params = {}
            if domain_name is not ShapeBase.NOT_SET:
                _params['domain_name'] = domain_name
            if domain_entry is not ShapeBase.NOT_SET:
                _params['domain_entry'] = domain_entry
            _request = shapes.CreateDomainEntryRequest(**_params)
        response = self._boto_client.create_domain_entry(**_request.to_boto())

        return shapes.CreateDomainEntryResult.from_boto(response)

    def create_instance_snapshot(
        self,
        _request: shapes.CreateInstanceSnapshotRequest = None,
        *,
        instance_snapshot_name: str,
        instance_name: str,
    ) -> shapes.CreateInstanceSnapshotResult:
        """
        Creates a snapshot of a specific virtual private server, or _instance_. You can
        use a snapshot to create a new instance that is based on that snapshot.
        """
        if _request is None:
            _params = {}
            if instance_snapshot_name is not ShapeBase.NOT_SET:
                _params['instance_snapshot_name'] = instance_snapshot_name
            if instance_name is not ShapeBase.NOT_SET:
                _params['instance_name'] = instance_name
            _request = shapes.CreateInstanceSnapshotRequest(**_params)
        response = self._boto_client.create_instance_snapshot(
            **_request.to_boto()
        )

        return shapes.CreateInstanceSnapshotResult.from_boto(response)

    def create_instances(
        self,
        _request: shapes.CreateInstancesRequest = None,
        *,
        instance_names: typing.List[str],
        availability_zone: str,
        blueprint_id: str,
        bundle_id: str,
        custom_image_name: str = ShapeBase.NOT_SET,
        user_data: str = ShapeBase.NOT_SET,
        key_pair_name: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateInstancesResult:
        """
        Creates one or more Amazon Lightsail virtual private servers, or _instances_.
        """
        if _request is None:
            _params = {}
            if instance_names is not ShapeBase.NOT_SET:
                _params['instance_names'] = instance_names
            if availability_zone is not ShapeBase.NOT_SET:
                _params['availability_zone'] = availability_zone
            if blueprint_id is not ShapeBase.NOT_SET:
                _params['blueprint_id'] = blueprint_id
            if bundle_id is not ShapeBase.NOT_SET:
                _params['bundle_id'] = bundle_id
            if custom_image_name is not ShapeBase.NOT_SET:
                _params['custom_image_name'] = custom_image_name
            if user_data is not ShapeBase.NOT_SET:
                _params['user_data'] = user_data
            if key_pair_name is not ShapeBase.NOT_SET:
                _params['key_pair_name'] = key_pair_name
            _request = shapes.CreateInstancesRequest(**_params)
        response = self._boto_client.create_instances(**_request.to_boto())

        return shapes.CreateInstancesResult.from_boto(response)

    def create_instances_from_snapshot(
        self,
        _request: shapes.CreateInstancesFromSnapshotRequest = None,
        *,
        instance_names: typing.List[str],
        availability_zone: str,
        instance_snapshot_name: str,
        bundle_id: str,
        attached_disk_mapping: typing.
        Dict[str, typing.List[shapes.DiskMap]] = ShapeBase.NOT_SET,
        user_data: str = ShapeBase.NOT_SET,
        key_pair_name: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateInstancesFromSnapshotResult:
        """
        Uses a specific snapshot as a blueprint for creating one or more new instances
        that are based on that identical configuration.
        """
        if _request is None:
            _params = {}
            if instance_names is not ShapeBase.NOT_SET:
                _params['instance_names'] = instance_names
            if availability_zone is not ShapeBase.NOT_SET:
                _params['availability_zone'] = availability_zone
            if instance_snapshot_name is not ShapeBase.NOT_SET:
                _params['instance_snapshot_name'] = instance_snapshot_name
            if bundle_id is not ShapeBase.NOT_SET:
                _params['bundle_id'] = bundle_id
            if attached_disk_mapping is not ShapeBase.NOT_SET:
                _params['attached_disk_mapping'] = attached_disk_mapping
            if user_data is not ShapeBase.NOT_SET:
                _params['user_data'] = user_data
            if key_pair_name is not ShapeBase.NOT_SET:
                _params['key_pair_name'] = key_pair_name
            _request = shapes.CreateInstancesFromSnapshotRequest(**_params)
        response = self._boto_client.create_instances_from_snapshot(
            **_request.to_boto()
        )

        return shapes.CreateInstancesFromSnapshotResult.from_boto(response)

    def create_key_pair(
        self,
        _request: shapes.CreateKeyPairRequest = None,
        *,
        key_pair_name: str,
    ) -> shapes.CreateKeyPairResult:
        """
        Creates sn SSH key pair.
        """
        if _request is None:
            _params = {}
            if key_pair_name is not ShapeBase.NOT_SET:
                _params['key_pair_name'] = key_pair_name
            _request = shapes.CreateKeyPairRequest(**_params)
        response = self._boto_client.create_key_pair(**_request.to_boto())

        return shapes.CreateKeyPairResult.from_boto(response)

    def create_load_balancer(
        self,
        _request: shapes.CreateLoadBalancerRequest = None,
        *,
        load_balancer_name: str,
        instance_port: int,
        health_check_path: str = ShapeBase.NOT_SET,
        certificate_name: str = ShapeBase.NOT_SET,
        certificate_domain_name: str = ShapeBase.NOT_SET,
        certificate_alternative_names: typing.List[str] = ShapeBase.NOT_SET,
    ) -> shapes.CreateLoadBalancerResult:
        """
        Creates a Lightsail load balancer. To learn more about deciding whether to load
        balance your application, see [Configure your Lightsail instances for load
        balancing](https://lightsail.aws.amazon.com/ls/docs/how-to/article/configure-
        lightsail-instances-for-load-balancing). You can create up to 5 load balancers
        per AWS Region in your account.

        When you create a load balancer, you can specify a unique name and port
        settings. To change additional load balancer settings, use the
        `UpdateLoadBalancerAttribute` operation.
        """
        if _request is None:
            _params = {}
            if load_balancer_name is not ShapeBase.NOT_SET:
                _params['load_balancer_name'] = load_balancer_name
            if instance_port is not ShapeBase.NOT_SET:
                _params['instance_port'] = instance_port
            if health_check_path is not ShapeBase.NOT_SET:
                _params['health_check_path'] = health_check_path
            if certificate_name is not ShapeBase.NOT_SET:
                _params['certificate_name'] = certificate_name
            if certificate_domain_name is not ShapeBase.NOT_SET:
                _params['certificate_domain_name'] = certificate_domain_name
            if certificate_alternative_names is not ShapeBase.NOT_SET:
                _params['certificate_alternative_names'
                       ] = certificate_alternative_names
            _request = shapes.CreateLoadBalancerRequest(**_params)
        response = self._boto_client.create_load_balancer(**_request.to_boto())

        return shapes.CreateLoadBalancerResult.from_boto(response)

    def create_load_balancer_tls_certificate(
        self,
        _request: shapes.CreateLoadBalancerTlsCertificateRequest = None,
        *,
        load_balancer_name: str,
        certificate_name: str,
        certificate_domain_name: str,
        certificate_alternative_names: typing.List[str] = ShapeBase.NOT_SET,
    ) -> shapes.CreateLoadBalancerTlsCertificateResult:
        """
        Creates a Lightsail load balancer TLS certificate.

        TLS is just an updated, more secure version of Secure Socket Layer (SSL).
        """
        if _request is None:
            _params = {}
            if load_balancer_name is not ShapeBase.NOT_SET:
                _params['load_balancer_name'] = load_balancer_name
            if certificate_name is not ShapeBase.NOT_SET:
                _params['certificate_name'] = certificate_name
            if certificate_domain_name is not ShapeBase.NOT_SET:
                _params['certificate_domain_name'] = certificate_domain_name
            if certificate_alternative_names is not ShapeBase.NOT_SET:
                _params['certificate_alternative_names'
                       ] = certificate_alternative_names
            _request = shapes.CreateLoadBalancerTlsCertificateRequest(**_params)
        response = self._boto_client.create_load_balancer_tls_certificate(
            **_request.to_boto()
        )

        return shapes.CreateLoadBalancerTlsCertificateResult.from_boto(response)

    def delete_disk(
        self,
        _request: shapes.DeleteDiskRequest = None,
        *,
        disk_name: str,
    ) -> shapes.DeleteDiskResult:
        """
        Deletes the specified block storage disk. The disk must be in the `available`
        state (not attached to a Lightsail instance).

        The disk may remain in the `deleting` state for several minutes.
        """
        if _request is None:
            _params = {}
            if disk_name is not ShapeBase.NOT_SET:
                _params['disk_name'] = disk_name
            _request = shapes.DeleteDiskRequest(**_params)
        response = self._boto_client.delete_disk(**_request.to_boto())

        return shapes.DeleteDiskResult.from_boto(response)

    def delete_disk_snapshot(
        self,
        _request: shapes.DeleteDiskSnapshotRequest = None,
        *,
        disk_snapshot_name: str,
    ) -> shapes.DeleteDiskSnapshotResult:
        """
        Deletes the specified disk snapshot.

        When you make periodic snapshots of a disk, the snapshots are incremental, and
        only the blocks on the device that have changed since your last snapshot are
        saved in the new snapshot. When you delete a snapshot, only the data not needed
        for any other snapshot is removed. So regardless of which prior snapshots have
        been deleted, all active snapshots will have access to all the information
        needed to restore the disk.
        """
        if _request is None:
            _params = {}
            if disk_snapshot_name is not ShapeBase.NOT_SET:
                _params['disk_snapshot_name'] = disk_snapshot_name
            _request = shapes.DeleteDiskSnapshotRequest(**_params)
        response = self._boto_client.delete_disk_snapshot(**_request.to_boto())

        return shapes.DeleteDiskSnapshotResult.from_boto(response)

    def delete_domain(
        self,
        _request: shapes.DeleteDomainRequest = None,
        *,
        domain_name: str,
    ) -> shapes.DeleteDomainResult:
        """
        Deletes the specified domain recordset and all of its domain records.
        """
        if _request is None:
            _params = {}
            if domain_name is not ShapeBase.NOT_SET:
                _params['domain_name'] = domain_name
            _request = shapes.DeleteDomainRequest(**_params)
        response = self._boto_client.delete_domain(**_request.to_boto())

        return shapes.DeleteDomainResult.from_boto(response)

    def delete_domain_entry(
        self,
        _request: shapes.DeleteDomainEntryRequest = None,
        *,
        domain_name: str,
        domain_entry: shapes.DomainEntry,
    ) -> shapes.DeleteDomainEntryResult:
        """
        Deletes a specific domain entry.
        """
        if _request is None:
            _params = {}
            if domain_name is not ShapeBase.NOT_SET:
                _params['domain_name'] = domain_name
            if domain_entry is not ShapeBase.NOT_SET:
                _params['domain_entry'] = domain_entry
            _request = shapes.DeleteDomainEntryRequest(**_params)
        response = self._boto_client.delete_domain_entry(**_request.to_boto())

        return shapes.DeleteDomainEntryResult.from_boto(response)

    def delete_instance(
        self,
        _request: shapes.DeleteInstanceRequest = None,
        *,
        instance_name: str,
    ) -> shapes.DeleteInstanceResult:
        """
        Deletes a specific Amazon Lightsail virtual private server, or _instance_.
        """
        if _request is None:
            _params = {}
            if instance_name is not ShapeBase.NOT_SET:
                _params['instance_name'] = instance_name
            _request = shapes.DeleteInstanceRequest(**_params)
        response = self._boto_client.delete_instance(**_request.to_boto())

        return shapes.DeleteInstanceResult.from_boto(response)

    def delete_instance_snapshot(
        self,
        _request: shapes.DeleteInstanceSnapshotRequest = None,
        *,
        instance_snapshot_name: str,
    ) -> shapes.DeleteInstanceSnapshotResult:
        """
        Deletes a specific snapshot of a virtual private server (or _instance_ ).
        """
        if _request is None:
            _params = {}
            if instance_snapshot_name is not ShapeBase.NOT_SET:
                _params['instance_snapshot_name'] = instance_snapshot_name
            _request = shapes.DeleteInstanceSnapshotRequest(**_params)
        response = self._boto_client.delete_instance_snapshot(
            **_request.to_boto()
        )

        return shapes.DeleteInstanceSnapshotResult.from_boto(response)

    def delete_key_pair(
        self,
        _request: shapes.DeleteKeyPairRequest = None,
        *,
        key_pair_name: str,
    ) -> shapes.DeleteKeyPairResult:
        """
        Deletes a specific SSH key pair.
        """
        if _request is None:
            _params = {}
            if key_pair_name is not ShapeBase.NOT_SET:
                _params['key_pair_name'] = key_pair_name
            _request = shapes.DeleteKeyPairRequest(**_params)
        response = self._boto_client.delete_key_pair(**_request.to_boto())

        return shapes.DeleteKeyPairResult.from_boto(response)

    def delete_load_balancer(
        self,
        _request: shapes.DeleteLoadBalancerRequest = None,
        *,
        load_balancer_name: str,
    ) -> shapes.DeleteLoadBalancerResult:
        """
        Deletes a Lightsail load balancer and all its associated SSL/TLS certificates.
        Once the load balancer is deleted, you will need to create a new load balancer,
        create a new certificate, and verify domain ownership again.
        """
        if _request is None:
            _params = {}
            if load_balancer_name is not ShapeBase.NOT_SET:
                _params['load_balancer_name'] = load_balancer_name
            _request = shapes.DeleteLoadBalancerRequest(**_params)
        response = self._boto_client.delete_load_balancer(**_request.to_boto())

        return shapes.DeleteLoadBalancerResult.from_boto(response)

    def delete_load_balancer_tls_certificate(
        self,
        _request: shapes.DeleteLoadBalancerTlsCertificateRequest = None,
        *,
        load_balancer_name: str,
        certificate_name: str,
        force: bool = ShapeBase.NOT_SET,
    ) -> shapes.DeleteLoadBalancerTlsCertificateResult:
        """
        Deletes an SSL/TLS certificate associated with a Lightsail load balancer.
        """
        if _request is None:
            _params = {}
            if load_balancer_name is not ShapeBase.NOT_SET:
                _params['load_balancer_name'] = load_balancer_name
            if certificate_name is not ShapeBase.NOT_SET:
                _params['certificate_name'] = certificate_name
            if force is not ShapeBase.NOT_SET:
                _params['force'] = force
            _request = shapes.DeleteLoadBalancerTlsCertificateRequest(**_params)
        response = self._boto_client.delete_load_balancer_tls_certificate(
            **_request.to_boto()
        )

        return shapes.DeleteLoadBalancerTlsCertificateResult.from_boto(response)

    def detach_disk(
        self,
        _request: shapes.DetachDiskRequest = None,
        *,
        disk_name: str,
    ) -> shapes.DetachDiskResult:
        """
        Detaches a stopped block storage disk from a Lightsail instance. Make sure to
        unmount any file systems on the device within your operating system before
        stopping the instance and detaching the disk.
        """
        if _request is None:
            _params = {}
            if disk_name is not ShapeBase.NOT_SET:
                _params['disk_name'] = disk_name
            _request = shapes.DetachDiskRequest(**_params)
        response = self._boto_client.detach_disk(**_request.to_boto())

        return shapes.DetachDiskResult.from_boto(response)

    def detach_instances_from_load_balancer(
        self,
        _request: shapes.DetachInstancesFromLoadBalancerRequest = None,
        *,
        load_balancer_name: str,
        instance_names: typing.List[str],
    ) -> shapes.DetachInstancesFromLoadBalancerResult:
        """
        Detaches the specified instances from a Lightsail load balancer.

        This operation waits until the instances are no longer needed before they are
        detached from the load balancer.
        """
        if _request is None:
            _params = {}
            if load_balancer_name is not ShapeBase.NOT_SET:
                _params['load_balancer_name'] = load_balancer_name
            if instance_names is not ShapeBase.NOT_SET:
                _params['instance_names'] = instance_names
            _request = shapes.DetachInstancesFromLoadBalancerRequest(**_params)
        response = self._boto_client.detach_instances_from_load_balancer(
            **_request.to_boto()
        )

        return shapes.DetachInstancesFromLoadBalancerResult.from_boto(response)

    def detach_static_ip(
        self,
        _request: shapes.DetachStaticIpRequest = None,
        *,
        static_ip_name: str,
    ) -> shapes.DetachStaticIpResult:
        """
        Detaches a static IP from the Amazon Lightsail instance to which it is attached.
        """
        if _request is None:
            _params = {}
            if static_ip_name is not ShapeBase.NOT_SET:
                _params['static_ip_name'] = static_ip_name
            _request = shapes.DetachStaticIpRequest(**_params)
        response = self._boto_client.detach_static_ip(**_request.to_boto())

        return shapes.DetachStaticIpResult.from_boto(response)

    def download_default_key_pair(
        self,
        _request: shapes.DownloadDefaultKeyPairRequest = None,
    ) -> shapes.DownloadDefaultKeyPairResult:
        """
        Downloads the default SSH key pair from the user's account.
        """
        if _request is None:
            _params = {}
            _request = shapes.DownloadDefaultKeyPairRequest(**_params)
        response = self._boto_client.download_default_key_pair(
            **_request.to_boto()
        )

        return shapes.DownloadDefaultKeyPairResult.from_boto(response)

    def get_active_names(
        self,
        _request: shapes.GetActiveNamesRequest = None,
        *,
        page_token: str = ShapeBase.NOT_SET,
    ) -> shapes.GetActiveNamesResult:
        """
        Returns the names of all active (not deleted) resources.
        """
        if _request is None:
            _params = {}
            if page_token is not ShapeBase.NOT_SET:
                _params['page_token'] = page_token
            _request = shapes.GetActiveNamesRequest(**_params)
        paginator = self.get_paginator("get_active_names").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.GetActiveNamesResult.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.GetActiveNamesResult.from_boto(response)

    def get_blueprints(
        self,
        _request: shapes.GetBlueprintsRequest = None,
        *,
        include_inactive: bool = ShapeBase.NOT_SET,
        page_token: str = ShapeBase.NOT_SET,
    ) -> shapes.GetBlueprintsResult:
        """
        Returns the list of available instance images, or _blueprints_. You can use a
        blueprint to create a new virtual private server already running a specific
        operating system, as well as a preinstalled app or development stack. The
        software each instance is running depends on the blueprint image you choose.
        """
        if _request is None:
            _params = {}
            if include_inactive is not ShapeBase.NOT_SET:
                _params['include_inactive'] = include_inactive
            if page_token is not ShapeBase.NOT_SET:
                _params['page_token'] = page_token
            _request = shapes.GetBlueprintsRequest(**_params)
        paginator = self.get_paginator("get_blueprints").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.GetBlueprintsResult.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.GetBlueprintsResult.from_boto(response)

    def get_bundles(
        self,
        _request: shapes.GetBundlesRequest = None,
        *,
        include_inactive: bool = ShapeBase.NOT_SET,
        page_token: str = ShapeBase.NOT_SET,
    ) -> shapes.GetBundlesResult:
        """
        Returns the list of bundles that are available for purchase. A bundle describes
        the specs for your virtual private server (or _instance_ ).
        """
        if _request is None:
            _params = {}
            if include_inactive is not ShapeBase.NOT_SET:
                _params['include_inactive'] = include_inactive
            if page_token is not ShapeBase.NOT_SET:
                _params['page_token'] = page_token
            _request = shapes.GetBundlesRequest(**_params)
        paginator = self.get_paginator("get_bundles").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.GetBundlesResult.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.GetBundlesResult.from_boto(response)

    def get_disk(
        self,
        _request: shapes.GetDiskRequest = None,
        *,
        disk_name: str,
    ) -> shapes.GetDiskResult:
        """
        Returns information about a specific block storage disk.
        """
        if _request is None:
            _params = {}
            if disk_name is not ShapeBase.NOT_SET:
                _params['disk_name'] = disk_name
            _request = shapes.GetDiskRequest(**_params)
        response = self._boto_client.get_disk(**_request.to_boto())

        return shapes.GetDiskResult.from_boto(response)

    def get_disk_snapshot(
        self,
        _request: shapes.GetDiskSnapshotRequest = None,
        *,
        disk_snapshot_name: str,
    ) -> shapes.GetDiskSnapshotResult:
        """
        Returns information about a specific block storage disk snapshot.
        """
        if _request is None:
            _params = {}
            if disk_snapshot_name is not ShapeBase.NOT_SET:
                _params['disk_snapshot_name'] = disk_snapshot_name
            _request = shapes.GetDiskSnapshotRequest(**_params)
        response = self._boto_client.get_disk_snapshot(**_request.to_boto())

        return shapes.GetDiskSnapshotResult.from_boto(response)

    def get_disk_snapshots(
        self,
        _request: shapes.GetDiskSnapshotsRequest = None,
        *,
        page_token: str = ShapeBase.NOT_SET,
    ) -> shapes.GetDiskSnapshotsResult:
        """
        Returns information about all block storage disk snapshots in your AWS account
        and region.

        If you are describing a long list of disk snapshots, you can paginate the output
        to make the list more manageable. You can use the pageToken and nextPageToken
        values to retrieve the next items in the list.
        """
        if _request is None:
            _params = {}
            if page_token is not ShapeBase.NOT_SET:
                _params['page_token'] = page_token
            _request = shapes.GetDiskSnapshotsRequest(**_params)
        response = self._boto_client.get_disk_snapshots(**_request.to_boto())

        return shapes.GetDiskSnapshotsResult.from_boto(response)

    def get_disks(
        self,
        _request: shapes.GetDisksRequest = None,
        *,
        page_token: str = ShapeBase.NOT_SET,
    ) -> shapes.GetDisksResult:
        """
        Returns information about all block storage disks in your AWS account and
        region.

        If you are describing a long list of disks, you can paginate the output to make
        the list more manageable. You can use the pageToken and nextPageToken values to
        retrieve the next items in the list.
        """
        if _request is None:
            _params = {}
            if page_token is not ShapeBase.NOT_SET:
                _params['page_token'] = page_token
            _request = shapes.GetDisksRequest(**_params)
        response = self._boto_client.get_disks(**_request.to_boto())

        return shapes.GetDisksResult.from_boto(response)

    def get_domain(
        self,
        _request: shapes.GetDomainRequest = None,
        *,
        domain_name: str,
    ) -> shapes.GetDomainResult:
        """
        Returns information about a specific domain recordset.
        """
        if _request is None:
            _params = {}
            if domain_name is not ShapeBase.NOT_SET:
                _params['domain_name'] = domain_name
            _request = shapes.GetDomainRequest(**_params)
        response = self._boto_client.get_domain(**_request.to_boto())

        return shapes.GetDomainResult.from_boto(response)

    def get_domains(
        self,
        _request: shapes.GetDomainsRequest = None,
        *,
        page_token: str = ShapeBase.NOT_SET,
    ) -> shapes.GetDomainsResult:
        """
        Returns a list of all domains in the user's account.
        """
        if _request is None:
            _params = {}
            if page_token is not ShapeBase.NOT_SET:
                _params['page_token'] = page_token
            _request = shapes.GetDomainsRequest(**_params)
        paginator = self.get_paginator("get_domains").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.GetDomainsResult.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.GetDomainsResult.from_boto(response)

    def get_instance(
        self,
        _request: shapes.GetInstanceRequest = None,
        *,
        instance_name: str,
    ) -> shapes.GetInstanceResult:
        """
        Returns information about a specific Amazon Lightsail instance, which is a
        virtual private server.
        """
        if _request is None:
            _params = {}
            if instance_name is not ShapeBase.NOT_SET:
                _params['instance_name'] = instance_name
            _request = shapes.GetInstanceRequest(**_params)
        response = self._boto_client.get_instance(**_request.to_boto())

        return shapes.GetInstanceResult.from_boto(response)

    def get_instance_access_details(
        self,
        _request: shapes.GetInstanceAccessDetailsRequest = None,
        *,
        instance_name: str,
        protocol: typing.Union[str, shapes.InstanceAccessProtocol] = ShapeBase.
        NOT_SET,
    ) -> shapes.GetInstanceAccessDetailsResult:
        """
        Returns temporary SSH keys you can use to connect to a specific virtual private
        server, or _instance_.
        """
        if _request is None:
            _params = {}
            if instance_name is not ShapeBase.NOT_SET:
                _params['instance_name'] = instance_name
            if protocol is not ShapeBase.NOT_SET:
                _params['protocol'] = protocol
            _request = shapes.GetInstanceAccessDetailsRequest(**_params)
        response = self._boto_client.get_instance_access_details(
            **_request.to_boto()
        )

        return shapes.GetInstanceAccessDetailsResult.from_boto(response)

    def get_instance_metric_data(
        self,
        _request: shapes.GetInstanceMetricDataRequest = None,
        *,
        instance_name: str,
        metric_name: typing.Union[str, shapes.InstanceMetricName],
        period: int,
        start_time: datetime.datetime,
        end_time: datetime.datetime,
        unit: typing.Union[str, shapes.MetricUnit],
        statistics: typing.List[typing.Union[str, shapes.MetricStatistic]],
    ) -> shapes.GetInstanceMetricDataResult:
        """
        Returns the data points for the specified Amazon Lightsail instance metric,
        given an instance name.
        """
        if _request is None:
            _params = {}
            if instance_name is not ShapeBase.NOT_SET:
                _params['instance_name'] = instance_name
            if metric_name is not ShapeBase.NOT_SET:
                _params['metric_name'] = metric_name
            if period is not ShapeBase.NOT_SET:
                _params['period'] = period
            if start_time is not ShapeBase.NOT_SET:
                _params['start_time'] = start_time
            if end_time is not ShapeBase.NOT_SET:
                _params['end_time'] = end_time
            if unit is not ShapeBase.NOT_SET:
                _params['unit'] = unit
            if statistics is not ShapeBase.NOT_SET:
                _params['statistics'] = statistics
            _request = shapes.GetInstanceMetricDataRequest(**_params)
        response = self._boto_client.get_instance_metric_data(
            **_request.to_boto()
        )

        return shapes.GetInstanceMetricDataResult.from_boto(response)

    def get_instance_port_states(
        self,
        _request: shapes.GetInstancePortStatesRequest = None,
        *,
        instance_name: str,
    ) -> shapes.GetInstancePortStatesResult:
        """
        Returns the port states for a specific virtual private server, or _instance_.
        """
        if _request is None:
            _params = {}
            if instance_name is not ShapeBase.NOT_SET:
                _params['instance_name'] = instance_name
            _request = shapes.GetInstancePortStatesRequest(**_params)
        response = self._boto_client.get_instance_port_states(
            **_request.to_boto()
        )

        return shapes.GetInstancePortStatesResult.from_boto(response)

    def get_instance_snapshot(
        self,
        _request: shapes.GetInstanceSnapshotRequest = None,
        *,
        instance_snapshot_name: str,
    ) -> shapes.GetInstanceSnapshotResult:
        """
        Returns information about a specific instance snapshot.
        """
        if _request is None:
            _params = {}
            if instance_snapshot_name is not ShapeBase.NOT_SET:
                _params['instance_snapshot_name'] = instance_snapshot_name
            _request = shapes.GetInstanceSnapshotRequest(**_params)
        response = self._boto_client.get_instance_snapshot(**_request.to_boto())

        return shapes.GetInstanceSnapshotResult.from_boto(response)

    def get_instance_snapshots(
        self,
        _request: shapes.GetInstanceSnapshotsRequest = None,
        *,
        page_token: str = ShapeBase.NOT_SET,
    ) -> shapes.GetInstanceSnapshotsResult:
        """
        Returns all instance snapshots for the user's account.
        """
        if _request is None:
            _params = {}
            if page_token is not ShapeBase.NOT_SET:
                _params['page_token'] = page_token
            _request = shapes.GetInstanceSnapshotsRequest(**_params)
        paginator = self.get_paginator("get_instance_snapshots").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.GetInstanceSnapshotsResult.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.GetInstanceSnapshotsResult.from_boto(response)

    def get_instance_state(
        self,
        _request: shapes.GetInstanceStateRequest = None,
        *,
        instance_name: str,
    ) -> shapes.GetInstanceStateResult:
        """
        Returns the state of a specific instance. Works on one instance at a time.
        """
        if _request is None:
            _params = {}
            if instance_name is not ShapeBase.NOT_SET:
                _params['instance_name'] = instance_name
            _request = shapes.GetInstanceStateRequest(**_params)
        response = self._boto_client.get_instance_state(**_request.to_boto())

        return shapes.GetInstanceStateResult.from_boto(response)

    def get_instances(
        self,
        _request: shapes.GetInstancesRequest = None,
        *,
        page_token: str = ShapeBase.NOT_SET,
    ) -> shapes.GetInstancesResult:
        """
        Returns information about all Amazon Lightsail virtual private servers, or
        _instances_.
        """
        if _request is None:
            _params = {}
            if page_token is not ShapeBase.NOT_SET:
                _params['page_token'] = page_token
            _request = shapes.GetInstancesRequest(**_params)
        paginator = self.get_paginator("get_instances").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.GetInstancesResult.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.GetInstancesResult.from_boto(response)

    def get_key_pair(
        self,
        _request: shapes.GetKeyPairRequest = None,
        *,
        key_pair_name: str,
    ) -> shapes.GetKeyPairResult:
        """
        Returns information about a specific key pair.
        """
        if _request is None:
            _params = {}
            if key_pair_name is not ShapeBase.NOT_SET:
                _params['key_pair_name'] = key_pair_name
            _request = shapes.GetKeyPairRequest(**_params)
        response = self._boto_client.get_key_pair(**_request.to_boto())

        return shapes.GetKeyPairResult.from_boto(response)

    def get_key_pairs(
        self,
        _request: shapes.GetKeyPairsRequest = None,
        *,
        page_token: str = ShapeBase.NOT_SET,
    ) -> shapes.GetKeyPairsResult:
        """
        Returns information about all key pairs in the user's account.
        """
        if _request is None:
            _params = {}
            if page_token is not ShapeBase.NOT_SET:
                _params['page_token'] = page_token
            _request = shapes.GetKeyPairsRequest(**_params)
        paginator = self.get_paginator("get_key_pairs").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.GetKeyPairsResult.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.GetKeyPairsResult.from_boto(response)

    def get_load_balancer(
        self,
        _request: shapes.GetLoadBalancerRequest = None,
        *,
        load_balancer_name: str,
    ) -> shapes.GetLoadBalancerResult:
        """
        Returns information about the specified Lightsail load balancer.
        """
        if _request is None:
            _params = {}
            if load_balancer_name is not ShapeBase.NOT_SET:
                _params['load_balancer_name'] = load_balancer_name
            _request = shapes.GetLoadBalancerRequest(**_params)
        response = self._boto_client.get_load_balancer(**_request.to_boto())

        return shapes.GetLoadBalancerResult.from_boto(response)

    def get_load_balancer_metric_data(
        self,
        _request: shapes.GetLoadBalancerMetricDataRequest = None,
        *,
        load_balancer_name: str,
        metric_name: typing.Union[str, shapes.LoadBalancerMetricName],
        period: int,
        start_time: datetime.datetime,
        end_time: datetime.datetime,
        unit: typing.Union[str, shapes.MetricUnit],
        statistics: typing.List[typing.Union[str, shapes.MetricStatistic]],
    ) -> shapes.GetLoadBalancerMetricDataResult:
        """
        Returns information about health metrics for your Lightsail load balancer.
        """
        if _request is None:
            _params = {}
            if load_balancer_name is not ShapeBase.NOT_SET:
                _params['load_balancer_name'] = load_balancer_name
            if metric_name is not ShapeBase.NOT_SET:
                _params['metric_name'] = metric_name
            if period is not ShapeBase.NOT_SET:
                _params['period'] = period
            if start_time is not ShapeBase.NOT_SET:
                _params['start_time'] = start_time
            if end_time is not ShapeBase.NOT_SET:
                _params['end_time'] = end_time
            if unit is not ShapeBase.NOT_SET:
                _params['unit'] = unit
            if statistics is not ShapeBase.NOT_SET:
                _params['statistics'] = statistics
            _request = shapes.GetLoadBalancerMetricDataRequest(**_params)
        response = self._boto_client.get_load_balancer_metric_data(
            **_request.to_boto()
        )

        return shapes.GetLoadBalancerMetricDataResult.from_boto(response)

    def get_load_balancer_tls_certificates(
        self,
        _request: shapes.GetLoadBalancerTlsCertificatesRequest = None,
        *,
        load_balancer_name: str,
    ) -> shapes.GetLoadBalancerTlsCertificatesResult:
        """
        Returns information about the TLS certificates that are associated with the
        specified Lightsail load balancer.

        TLS is just an updated, more secure version of Secure Socket Layer (SSL).

        You can have a maximum of 2 certificates associated with a Lightsail load
        balancer. One is active and the other is inactive.
        """
        if _request is None:
            _params = {}
            if load_balancer_name is not ShapeBase.NOT_SET:
                _params['load_balancer_name'] = load_balancer_name
            _request = shapes.GetLoadBalancerTlsCertificatesRequest(**_params)
        response = self._boto_client.get_load_balancer_tls_certificates(
            **_request.to_boto()
        )

        return shapes.GetLoadBalancerTlsCertificatesResult.from_boto(response)

    def get_load_balancers(
        self,
        _request: shapes.GetLoadBalancersRequest = None,
        *,
        page_token: str = ShapeBase.NOT_SET,
    ) -> shapes.GetLoadBalancersResult:
        """
        Returns information about all load balancers in an account.

        If you are describing a long list of load balancers, you can paginate the output
        to make the list more manageable. You can use the pageToken and nextPageToken
        values to retrieve the next items in the list.
        """
        if _request is None:
            _params = {}
            if page_token is not ShapeBase.NOT_SET:
                _params['page_token'] = page_token
            _request = shapes.GetLoadBalancersRequest(**_params)
        response = self._boto_client.get_load_balancers(**_request.to_boto())

        return shapes.GetLoadBalancersResult.from_boto(response)

    def get_operation(
        self,
        _request: shapes.GetOperationRequest = None,
        *,
        operation_id: str,
    ) -> shapes.GetOperationResult:
        """
        Returns information about a specific operation. Operations include events such
        as when you create an instance, allocate a static IP, attach a static IP, and so
        on.
        """
        if _request is None:
            _params = {}
            if operation_id is not ShapeBase.NOT_SET:
                _params['operation_id'] = operation_id
            _request = shapes.GetOperationRequest(**_params)
        response = self._boto_client.get_operation(**_request.to_boto())

        return shapes.GetOperationResult.from_boto(response)

    def get_operations(
        self,
        _request: shapes.GetOperationsRequest = None,
        *,
        page_token: str = ShapeBase.NOT_SET,
    ) -> shapes.GetOperationsResult:
        """
        Returns information about all operations.

        Results are returned from oldest to newest, up to a maximum of 200. Results can
        be paged by making each subsequent call to `GetOperations` use the maximum
        (last) `statusChangedAt` value from the previous request.
        """
        if _request is None:
            _params = {}
            if page_token is not ShapeBase.NOT_SET:
                _params['page_token'] = page_token
            _request = shapes.GetOperationsRequest(**_params)
        paginator = self.get_paginator("get_operations").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.GetOperationsResult.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.GetOperationsResult.from_boto(response)

    def get_operations_for_resource(
        self,
        _request: shapes.GetOperationsForResourceRequest = None,
        *,
        resource_name: str,
        page_token: str = ShapeBase.NOT_SET,
    ) -> shapes.GetOperationsForResourceResult:
        """
        Gets operations for a specific resource (e.g., an instance or a static IP).
        """
        if _request is None:
            _params = {}
            if resource_name is not ShapeBase.NOT_SET:
                _params['resource_name'] = resource_name
            if page_token is not ShapeBase.NOT_SET:
                _params['page_token'] = page_token
            _request = shapes.GetOperationsForResourceRequest(**_params)
        response = self._boto_client.get_operations_for_resource(
            **_request.to_boto()
        )

        return shapes.GetOperationsForResourceResult.from_boto(response)

    def get_regions(
        self,
        _request: shapes.GetRegionsRequest = None,
        *,
        include_availability_zones: bool = ShapeBase.NOT_SET,
    ) -> shapes.GetRegionsResult:
        """
        Returns a list of all valid regions for Amazon Lightsail. Use the `include
        availability zones` parameter to also return the availability zones in a region.
        """
        if _request is None:
            _params = {}
            if include_availability_zones is not ShapeBase.NOT_SET:
                _params['include_availability_zones'
                       ] = include_availability_zones
            _request = shapes.GetRegionsRequest(**_params)
        response = self._boto_client.get_regions(**_request.to_boto())

        return shapes.GetRegionsResult.from_boto(response)

    def get_static_ip(
        self,
        _request: shapes.GetStaticIpRequest = None,
        *,
        static_ip_name: str,
    ) -> shapes.GetStaticIpResult:
        """
        Returns information about a specific static IP.
        """
        if _request is None:
            _params = {}
            if static_ip_name is not ShapeBase.NOT_SET:
                _params['static_ip_name'] = static_ip_name
            _request = shapes.GetStaticIpRequest(**_params)
        response = self._boto_client.get_static_ip(**_request.to_boto())

        return shapes.GetStaticIpResult.from_boto(response)

    def get_static_ips(
        self,
        _request: shapes.GetStaticIpsRequest = None,
        *,
        page_token: str = ShapeBase.NOT_SET,
    ) -> shapes.GetStaticIpsResult:
        """
        Returns information about all static IPs in the user's account.
        """
        if _request is None:
            _params = {}
            if page_token is not ShapeBase.NOT_SET:
                _params['page_token'] = page_token
            _request = shapes.GetStaticIpsRequest(**_params)
        paginator = self.get_paginator("get_static_ips").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.GetStaticIpsResult.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.GetStaticIpsResult.from_boto(response)

    def import_key_pair(
        self,
        _request: shapes.ImportKeyPairRequest = None,
        *,
        key_pair_name: str,
        public_key_base64: str,
    ) -> shapes.ImportKeyPairResult:
        """
        Imports a public SSH key from a specific key pair.
        """
        if _request is None:
            _params = {}
            if key_pair_name is not ShapeBase.NOT_SET:
                _params['key_pair_name'] = key_pair_name
            if public_key_base64 is not ShapeBase.NOT_SET:
                _params['public_key_base64'] = public_key_base64
            _request = shapes.ImportKeyPairRequest(**_params)
        response = self._boto_client.import_key_pair(**_request.to_boto())

        return shapes.ImportKeyPairResult.from_boto(response)

    def is_vpc_peered(
        self,
        _request: shapes.IsVpcPeeredRequest = None,
    ) -> shapes.IsVpcPeeredResult:
        """
        Returns a Boolean value indicating whether your Lightsail VPC is peered.
        """
        if _request is None:
            _params = {}
            _request = shapes.IsVpcPeeredRequest(**_params)
        response = self._boto_client.is_vpc_peered(**_request.to_boto())

        return shapes.IsVpcPeeredResult.from_boto(response)

    def open_instance_public_ports(
        self,
        _request: shapes.OpenInstancePublicPortsRequest = None,
        *,
        port_info: shapes.PortInfo,
        instance_name: str,
    ) -> shapes.OpenInstancePublicPortsResult:
        """
        Adds public ports to an Amazon Lightsail instance.
        """
        if _request is None:
            _params = {}
            if port_info is not ShapeBase.NOT_SET:
                _params['port_info'] = port_info
            if instance_name is not ShapeBase.NOT_SET:
                _params['instance_name'] = instance_name
            _request = shapes.OpenInstancePublicPortsRequest(**_params)
        response = self._boto_client.open_instance_public_ports(
            **_request.to_boto()
        )

        return shapes.OpenInstancePublicPortsResult.from_boto(response)

    def peer_vpc(
        self,
        _request: shapes.PeerVpcRequest = None,
    ) -> shapes.PeerVpcResult:
        """
        Tries to peer the Lightsail VPC with the user's default VPC.
        """
        if _request is None:
            _params = {}
            _request = shapes.PeerVpcRequest(**_params)
        response = self._boto_client.peer_vpc(**_request.to_boto())

        return shapes.PeerVpcResult.from_boto(response)

    def put_instance_public_ports(
        self,
        _request: shapes.PutInstancePublicPortsRequest = None,
        *,
        port_infos: typing.List[shapes.PortInfo],
        instance_name: str,
    ) -> shapes.PutInstancePublicPortsResult:
        """
        Sets the specified open ports for an Amazon Lightsail instance, and closes all
        ports for every protocol not included in the current request.
        """
        if _request is None:
            _params = {}
            if port_infos is not ShapeBase.NOT_SET:
                _params['port_infos'] = port_infos
            if instance_name is not ShapeBase.NOT_SET:
                _params['instance_name'] = instance_name
            _request = shapes.PutInstancePublicPortsRequest(**_params)
        response = self._boto_client.put_instance_public_ports(
            **_request.to_boto()
        )

        return shapes.PutInstancePublicPortsResult.from_boto(response)

    def reboot_instance(
        self,
        _request: shapes.RebootInstanceRequest = None,
        *,
        instance_name: str,
    ) -> shapes.RebootInstanceResult:
        """
        Restarts a specific instance. When your Amazon Lightsail instance is finished
        rebooting, Lightsail assigns a new public IP address. To use the same IP address
        after restarting, create a static IP address and attach it to the instance.
        """
        if _request is None:
            _params = {}
            if instance_name is not ShapeBase.NOT_SET:
                _params['instance_name'] = instance_name
            _request = shapes.RebootInstanceRequest(**_params)
        response = self._boto_client.reboot_instance(**_request.to_boto())

        return shapes.RebootInstanceResult.from_boto(response)

    def release_static_ip(
        self,
        _request: shapes.ReleaseStaticIpRequest = None,
        *,
        static_ip_name: str,
    ) -> shapes.ReleaseStaticIpResult:
        """
        Deletes a specific static IP from your account.
        """
        if _request is None:
            _params = {}
            if static_ip_name is not ShapeBase.NOT_SET:
                _params['static_ip_name'] = static_ip_name
            _request = shapes.ReleaseStaticIpRequest(**_params)
        response = self._boto_client.release_static_ip(**_request.to_boto())

        return shapes.ReleaseStaticIpResult.from_boto(response)

    def start_instance(
        self,
        _request: shapes.StartInstanceRequest = None,
        *,
        instance_name: str,
    ) -> shapes.StartInstanceResult:
        """
        Starts a specific Amazon Lightsail instance from a stopped state. To restart an
        instance, use the reboot instance operation.
        """
        if _request is None:
            _params = {}
            if instance_name is not ShapeBase.NOT_SET:
                _params['instance_name'] = instance_name
            _request = shapes.StartInstanceRequest(**_params)
        response = self._boto_client.start_instance(**_request.to_boto())

        return shapes.StartInstanceResult.from_boto(response)

    def stop_instance(
        self,
        _request: shapes.StopInstanceRequest = None,
        *,
        instance_name: str,
        force: bool = ShapeBase.NOT_SET,
    ) -> shapes.StopInstanceResult:
        """
        Stops a specific Amazon Lightsail instance that is currently running.
        """
        if _request is None:
            _params = {}
            if instance_name is not ShapeBase.NOT_SET:
                _params['instance_name'] = instance_name
            if force is not ShapeBase.NOT_SET:
                _params['force'] = force
            _request = shapes.StopInstanceRequest(**_params)
        response = self._boto_client.stop_instance(**_request.to_boto())

        return shapes.StopInstanceResult.from_boto(response)

    def unpeer_vpc(
        self,
        _request: shapes.UnpeerVpcRequest = None,
    ) -> shapes.UnpeerVpcResult:
        """
        Attempts to unpeer the Lightsail VPC from the user's default VPC.
        """
        if _request is None:
            _params = {}
            _request = shapes.UnpeerVpcRequest(**_params)
        response = self._boto_client.unpeer_vpc(**_request.to_boto())

        return shapes.UnpeerVpcResult.from_boto(response)

    def update_domain_entry(
        self,
        _request: shapes.UpdateDomainEntryRequest = None,
        *,
        domain_name: str,
        domain_entry: shapes.DomainEntry,
    ) -> shapes.UpdateDomainEntryResult:
        """
        Updates a domain recordset after it is created.
        """
        if _request is None:
            _params = {}
            if domain_name is not ShapeBase.NOT_SET:
                _params['domain_name'] = domain_name
            if domain_entry is not ShapeBase.NOT_SET:
                _params['domain_entry'] = domain_entry
            _request = shapes.UpdateDomainEntryRequest(**_params)
        response = self._boto_client.update_domain_entry(**_request.to_boto())

        return shapes.UpdateDomainEntryResult.from_boto(response)

    def update_load_balancer_attribute(
        self,
        _request: shapes.UpdateLoadBalancerAttributeRequest = None,
        *,
        load_balancer_name: str,
        attribute_name: typing.Union[str, shapes.LoadBalancerAttributeName],
        attribute_value: str,
    ) -> shapes.UpdateLoadBalancerAttributeResult:
        """
        Updates the specified attribute for a load balancer. You can only update one
        attribute at a time.
        """
        if _request is None:
            _params = {}
            if load_balancer_name is not ShapeBase.NOT_SET:
                _params['load_balancer_name'] = load_balancer_name
            if attribute_name is not ShapeBase.NOT_SET:
                _params['attribute_name'] = attribute_name
            if attribute_value is not ShapeBase.NOT_SET:
                _params['attribute_value'] = attribute_value
            _request = shapes.UpdateLoadBalancerAttributeRequest(**_params)
        response = self._boto_client.update_load_balancer_attribute(
            **_request.to_boto()
        )

        return shapes.UpdateLoadBalancerAttributeResult.from_boto(response)
