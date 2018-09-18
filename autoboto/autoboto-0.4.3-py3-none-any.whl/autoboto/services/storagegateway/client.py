import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("storagegateway", *args, **kwargs)

    def activate_gateway(
        self,
        _request: shapes.ActivateGatewayInput = None,
        *,
        activation_key: str,
        gateway_name: str,
        gateway_timezone: str,
        gateway_region: str,
        gateway_type: str = ShapeBase.NOT_SET,
        tape_drive_type: str = ShapeBase.NOT_SET,
        medium_changer_type: str = ShapeBase.NOT_SET,
    ) -> shapes.ActivateGatewayOutput:
        """
        Activates the gateway you previously deployed on your host. In the activation
        process, you specify information such as the region you want to use for storing
        snapshots or tapes, the time zone for scheduled snapshots the gateway snapshot
        schedule window, an activation key, and a name for your gateway. The activation
        process also associates your gateway with your account; for more information,
        see UpdateGatewayInformation.

        You must turn on the gateway VM before you can activate your gateway.
        """
        if _request is None:
            _params = {}
            if activation_key is not ShapeBase.NOT_SET:
                _params['activation_key'] = activation_key
            if gateway_name is not ShapeBase.NOT_SET:
                _params['gateway_name'] = gateway_name
            if gateway_timezone is not ShapeBase.NOT_SET:
                _params['gateway_timezone'] = gateway_timezone
            if gateway_region is not ShapeBase.NOT_SET:
                _params['gateway_region'] = gateway_region
            if gateway_type is not ShapeBase.NOT_SET:
                _params['gateway_type'] = gateway_type
            if tape_drive_type is not ShapeBase.NOT_SET:
                _params['tape_drive_type'] = tape_drive_type
            if medium_changer_type is not ShapeBase.NOT_SET:
                _params['medium_changer_type'] = medium_changer_type
            _request = shapes.ActivateGatewayInput(**_params)
        response = self._boto_client.activate_gateway(**_request.to_boto())

        return shapes.ActivateGatewayOutput.from_boto(response)

    def add_cache(
        self,
        _request: shapes.AddCacheInput = None,
        *,
        gateway_arn: str,
        disk_ids: typing.List[str],
    ) -> shapes.AddCacheOutput:
        """
        Configures one or more gateway local disks as cache for a gateway. This
        operation is only supported in the cached volume, tape and file gateway type
        (see [Storage Gateway
        Concepts](http://docs.aws.amazon.com/storagegateway/latest/userguide/StorageGatewayConcepts.html)).

        In the request, you specify the gateway Amazon Resource Name (ARN) to which you
        want to add cache, and one or more disk IDs that you want to configure as cache.
        """
        if _request is None:
            _params = {}
            if gateway_arn is not ShapeBase.NOT_SET:
                _params['gateway_arn'] = gateway_arn
            if disk_ids is not ShapeBase.NOT_SET:
                _params['disk_ids'] = disk_ids
            _request = shapes.AddCacheInput(**_params)
        response = self._boto_client.add_cache(**_request.to_boto())

        return shapes.AddCacheOutput.from_boto(response)

    def add_tags_to_resource(
        self,
        _request: shapes.AddTagsToResourceInput = None,
        *,
        resource_arn: str,
        tags: typing.List[shapes.Tag],
    ) -> shapes.AddTagsToResourceOutput:
        """
        Adds one or more tags to the specified resource. You use tags to add metadata to
        resources, which you can use to categorize these resources. For example, you can
        categorize resources by purpose, owner, environment, or team. Each tag consists
        of a key and a value, which you define. You can add tags to the following AWS
        Storage Gateway resources:

          * Storage gateways of all types

          * Storage Volumes

          * Virtual Tapes

        You can create a maximum of 10 tags for each resource. Virtual tapes and storage
        volumes that are recovered to a new gateway maintain their tags.
        """
        if _request is None:
            _params = {}
            if resource_arn is not ShapeBase.NOT_SET:
                _params['resource_arn'] = resource_arn
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            _request = shapes.AddTagsToResourceInput(**_params)
        response = self._boto_client.add_tags_to_resource(**_request.to_boto())

        return shapes.AddTagsToResourceOutput.from_boto(response)

    def add_upload_buffer(
        self,
        _request: shapes.AddUploadBufferInput = None,
        *,
        gateway_arn: str,
        disk_ids: typing.List[str],
    ) -> shapes.AddUploadBufferOutput:
        """
        Configures one or more gateway local disks as upload buffer for a specified
        gateway. This operation is supported for the stored volume, cached volume and
        tape gateway types.

        In the request, you specify the gateway Amazon Resource Name (ARN) to which you
        want to add upload buffer, and one or more disk IDs that you want to configure
        as upload buffer.
        """
        if _request is None:
            _params = {}
            if gateway_arn is not ShapeBase.NOT_SET:
                _params['gateway_arn'] = gateway_arn
            if disk_ids is not ShapeBase.NOT_SET:
                _params['disk_ids'] = disk_ids
            _request = shapes.AddUploadBufferInput(**_params)
        response = self._boto_client.add_upload_buffer(**_request.to_boto())

        return shapes.AddUploadBufferOutput.from_boto(response)

    def add_working_storage(
        self,
        _request: shapes.AddWorkingStorageInput = None,
        *,
        gateway_arn: str,
        disk_ids: typing.List[str],
    ) -> shapes.AddWorkingStorageOutput:
        """
        Configures one or more gateway local disks as working storage for a gateway.
        This operation is only supported in the stored volume gateway type. This
        operation is deprecated in cached volume API version 20120630. Use
        AddUploadBuffer instead.

        Working storage is also referred to as upload buffer. You can also use the
        AddUploadBuffer operation to add upload buffer to a stored volume gateway.

        In the request, you specify the gateway Amazon Resource Name (ARN) to which you
        want to add working storage, and one or more disk IDs that you want to configure
        as working storage.
        """
        if _request is None:
            _params = {}
            if gateway_arn is not ShapeBase.NOT_SET:
                _params['gateway_arn'] = gateway_arn
            if disk_ids is not ShapeBase.NOT_SET:
                _params['disk_ids'] = disk_ids
            _request = shapes.AddWorkingStorageInput(**_params)
        response = self._boto_client.add_working_storage(**_request.to_boto())

        return shapes.AddWorkingStorageOutput.from_boto(response)

    def cancel_archival(
        self,
        _request: shapes.CancelArchivalInput = None,
        *,
        gateway_arn: str,
        tape_arn: str,
    ) -> shapes.CancelArchivalOutput:
        """
        Cancels archiving of a virtual tape to the virtual tape shelf (VTS) after the
        archiving process is initiated. This operation is only supported in the tape
        gateway type.
        """
        if _request is None:
            _params = {}
            if gateway_arn is not ShapeBase.NOT_SET:
                _params['gateway_arn'] = gateway_arn
            if tape_arn is not ShapeBase.NOT_SET:
                _params['tape_arn'] = tape_arn
            _request = shapes.CancelArchivalInput(**_params)
        response = self._boto_client.cancel_archival(**_request.to_boto())

        return shapes.CancelArchivalOutput.from_boto(response)

    def cancel_retrieval(
        self,
        _request: shapes.CancelRetrievalInput = None,
        *,
        gateway_arn: str,
        tape_arn: str,
    ) -> shapes.CancelRetrievalOutput:
        """
        Cancels retrieval of a virtual tape from the virtual tape shelf (VTS) to a
        gateway after the retrieval process is initiated. The virtual tape is returned
        to the VTS. This operation is only supported in the tape gateway type.
        """
        if _request is None:
            _params = {}
            if gateway_arn is not ShapeBase.NOT_SET:
                _params['gateway_arn'] = gateway_arn
            if tape_arn is not ShapeBase.NOT_SET:
                _params['tape_arn'] = tape_arn
            _request = shapes.CancelRetrievalInput(**_params)
        response = self._boto_client.cancel_retrieval(**_request.to_boto())

        return shapes.CancelRetrievalOutput.from_boto(response)

    def create_cached_iscsi_volume(
        self,
        _request: shapes.CreateCachediSCSIVolumeInput = None,
        *,
        gateway_arn: str,
        volume_size_in_bytes: int,
        target_name: str,
        network_interface_id: str,
        client_token: str,
        snapshot_id: str = ShapeBase.NOT_SET,
        source_volume_arn: str = ShapeBase.NOT_SET,
        kms_encrypted: bool = ShapeBase.NOT_SET,
        kms_key: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateCachediSCSIVolumeOutput:
        """
        Creates a cached volume on a specified cached volume gateway. This operation is
        only supported in the cached volume gateway type.

        Cache storage must be allocated to the gateway before you can create a cached
        volume. Use the AddCache operation to add cache storage to a gateway.

        In the request, you must specify the gateway, size of the volume in bytes, the
        iSCSI target name, an IP address on which to expose the target, and a unique
        client token. In response, the gateway creates the volume and returns
        information about it. This information includes the volume Amazon Resource Name
        (ARN), its size, and the iSCSI target ARN that initiators can use to connect to
        the volume target.

        Optionally, you can provide the ARN for an existing volume as the
        `SourceVolumeARN` for this cached volume, which creates an exact copy of the
        existing volume’s latest recovery point. The `VolumeSizeInBytes` value must be
        equal to or larger than the size of the copied volume, in bytes.
        """
        if _request is None:
            _params = {}
            if gateway_arn is not ShapeBase.NOT_SET:
                _params['gateway_arn'] = gateway_arn
            if volume_size_in_bytes is not ShapeBase.NOT_SET:
                _params['volume_size_in_bytes'] = volume_size_in_bytes
            if target_name is not ShapeBase.NOT_SET:
                _params['target_name'] = target_name
            if network_interface_id is not ShapeBase.NOT_SET:
                _params['network_interface_id'] = network_interface_id
            if client_token is not ShapeBase.NOT_SET:
                _params['client_token'] = client_token
            if snapshot_id is not ShapeBase.NOT_SET:
                _params['snapshot_id'] = snapshot_id
            if source_volume_arn is not ShapeBase.NOT_SET:
                _params['source_volume_arn'] = source_volume_arn
            if kms_encrypted is not ShapeBase.NOT_SET:
                _params['kms_encrypted'] = kms_encrypted
            if kms_key is not ShapeBase.NOT_SET:
                _params['kms_key'] = kms_key
            _request = shapes.CreateCachediSCSIVolumeInput(**_params)
        response = self._boto_client.create_cached_iscsi_volume(
            **_request.to_boto()
        )

        return shapes.CreateCachediSCSIVolumeOutput.from_boto(response)

    def create_nfs_file_share(
        self,
        _request: shapes.CreateNFSFileShareInput = None,
        *,
        client_token: str,
        gateway_arn: str,
        role: str,
        location_arn: str,
        nfs_file_share_defaults: shapes.NFSFileShareDefaults = ShapeBase.
        NOT_SET,
        kms_encrypted: bool = ShapeBase.NOT_SET,
        kms_key: str = ShapeBase.NOT_SET,
        default_storage_class: str = ShapeBase.NOT_SET,
        object_acl: typing.Union[str, shapes.ObjectACL] = ShapeBase.NOT_SET,
        client_list: typing.List[str] = ShapeBase.NOT_SET,
        squash: str = ShapeBase.NOT_SET,
        read_only: bool = ShapeBase.NOT_SET,
        guess_mime_type_enabled: bool = ShapeBase.NOT_SET,
        requester_pays: bool = ShapeBase.NOT_SET,
    ) -> shapes.CreateNFSFileShareOutput:
        """
        Creates a Network File System (NFS) file share on an existing file gateway. In
        Storage Gateway, a file share is a file system mount point backed by Amazon S3
        cloud storage. Storage Gateway exposes file shares using a NFS interface. This
        operation is only supported for file gateways.

        File gateway requires AWS Security Token Service (AWS STS) to be activated to
        enable you create a file share. Make sure AWS STS is activated in the region you
        are creating your file gateway in. If AWS STS is not activated in the region,
        activate it. For information about how to activate AWS STS, see Activating and
        Deactivating AWS STS in an AWS Region in the AWS Identity and Access Management
        User Guide.

        File gateway does not support creating hard or symbolic links on a file share.
        """
        if _request is None:
            _params = {}
            if client_token is not ShapeBase.NOT_SET:
                _params['client_token'] = client_token
            if gateway_arn is not ShapeBase.NOT_SET:
                _params['gateway_arn'] = gateway_arn
            if role is not ShapeBase.NOT_SET:
                _params['role'] = role
            if location_arn is not ShapeBase.NOT_SET:
                _params['location_arn'] = location_arn
            if nfs_file_share_defaults is not ShapeBase.NOT_SET:
                _params['nfs_file_share_defaults'] = nfs_file_share_defaults
            if kms_encrypted is not ShapeBase.NOT_SET:
                _params['kms_encrypted'] = kms_encrypted
            if kms_key is not ShapeBase.NOT_SET:
                _params['kms_key'] = kms_key
            if default_storage_class is not ShapeBase.NOT_SET:
                _params['default_storage_class'] = default_storage_class
            if object_acl is not ShapeBase.NOT_SET:
                _params['object_acl'] = object_acl
            if client_list is not ShapeBase.NOT_SET:
                _params['client_list'] = client_list
            if squash is not ShapeBase.NOT_SET:
                _params['squash'] = squash
            if read_only is not ShapeBase.NOT_SET:
                _params['read_only'] = read_only
            if guess_mime_type_enabled is not ShapeBase.NOT_SET:
                _params['guess_mime_type_enabled'] = guess_mime_type_enabled
            if requester_pays is not ShapeBase.NOT_SET:
                _params['requester_pays'] = requester_pays
            _request = shapes.CreateNFSFileShareInput(**_params)
        response = self._boto_client.create_nfs_file_share(**_request.to_boto())

        return shapes.CreateNFSFileShareOutput.from_boto(response)

    def create_smb_file_share(
        self,
        _request: shapes.CreateSMBFileShareInput = None,
        *,
        client_token: str,
        gateway_arn: str,
        role: str,
        location_arn: str,
        kms_encrypted: bool = ShapeBase.NOT_SET,
        kms_key: str = ShapeBase.NOT_SET,
        default_storage_class: str = ShapeBase.NOT_SET,
        object_acl: typing.Union[str, shapes.ObjectACL] = ShapeBase.NOT_SET,
        read_only: bool = ShapeBase.NOT_SET,
        guess_mime_type_enabled: bool = ShapeBase.NOT_SET,
        requester_pays: bool = ShapeBase.NOT_SET,
        valid_user_list: typing.List[str] = ShapeBase.NOT_SET,
        invalid_user_list: typing.List[str] = ShapeBase.NOT_SET,
        authentication: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateSMBFileShareOutput:
        """
        Creates a Server Message Block (SMB) file share on an existing file gateway. In
        Storage Gateway, a file share is a file system mount point backed by Amazon S3
        cloud storage. Storage Gateway expose file shares using a SMB interface. This
        operation is only supported for file gateways.

        File gateways require AWS Security Token Service (AWS STS) to be activated to
        enable you to create a file share. Make sure that AWS STS is activated in the
        AWS Region you are creating your file gateway in. If AWS STS is not activated in
        this AWS Region, activate it. For information about how to activate AWS STS, see
        [Activating and Deactivating AWS STS in an AWS
        Region](http://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_enable-
        regions.html) in the _AWS Identity and Access Management User Guide._

        File gateways don't support creating hard or symbolic links on a file share.
        """
        if _request is None:
            _params = {}
            if client_token is not ShapeBase.NOT_SET:
                _params['client_token'] = client_token
            if gateway_arn is not ShapeBase.NOT_SET:
                _params['gateway_arn'] = gateway_arn
            if role is not ShapeBase.NOT_SET:
                _params['role'] = role
            if location_arn is not ShapeBase.NOT_SET:
                _params['location_arn'] = location_arn
            if kms_encrypted is not ShapeBase.NOT_SET:
                _params['kms_encrypted'] = kms_encrypted
            if kms_key is not ShapeBase.NOT_SET:
                _params['kms_key'] = kms_key
            if default_storage_class is not ShapeBase.NOT_SET:
                _params['default_storage_class'] = default_storage_class
            if object_acl is not ShapeBase.NOT_SET:
                _params['object_acl'] = object_acl
            if read_only is not ShapeBase.NOT_SET:
                _params['read_only'] = read_only
            if guess_mime_type_enabled is not ShapeBase.NOT_SET:
                _params['guess_mime_type_enabled'] = guess_mime_type_enabled
            if requester_pays is not ShapeBase.NOT_SET:
                _params['requester_pays'] = requester_pays
            if valid_user_list is not ShapeBase.NOT_SET:
                _params['valid_user_list'] = valid_user_list
            if invalid_user_list is not ShapeBase.NOT_SET:
                _params['invalid_user_list'] = invalid_user_list
            if authentication is not ShapeBase.NOT_SET:
                _params['authentication'] = authentication
            _request = shapes.CreateSMBFileShareInput(**_params)
        response = self._boto_client.create_smb_file_share(**_request.to_boto())

        return shapes.CreateSMBFileShareOutput.from_boto(response)

    def create_snapshot(
        self,
        _request: shapes.CreateSnapshotInput = None,
        *,
        volume_arn: str,
        snapshot_description: str,
    ) -> shapes.CreateSnapshotOutput:
        """
        Initiates a snapshot of a volume.

        AWS Storage Gateway provides the ability to back up point-in-time snapshots of
        your data to Amazon Simple Storage (S3) for durable off-site recovery, as well
        as import the data to an Amazon Elastic Block Store (EBS) volume in Amazon
        Elastic Compute Cloud (EC2). You can take snapshots of your gateway volume on a
        scheduled or ad-hoc basis. This API enables you to take ad-hoc snapshot. For
        more information, see [Editing a Snapshot
        Schedule](http://docs.aws.amazon.com/storagegateway/latest/userguide/managing-
        volumes.html#SchedulingSnapshot).

        In the CreateSnapshot request you identify the volume by providing its Amazon
        Resource Name (ARN). You must also provide description for the snapshot. When
        AWS Storage Gateway takes the snapshot of specified volume, the snapshot and
        description appears in the AWS Storage Gateway Console. In response, AWS Storage
        Gateway returns you a snapshot ID. You can use this snapshot ID to check the
        snapshot progress or later use it when you want to create a volume from a
        snapshot. This operation is only supported in stored and cached volume gateway
        type.

        To list or delete a snapshot, you must use the Amazon EC2 API. For more
        information, see DescribeSnapshots or DeleteSnapshot in the [EC2 API
        reference](http://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_Operations.html).

        Volume and snapshot IDs are changing to a longer length ID format. For more
        information, see the important note on the
        [Welcome](http://docs.aws.amazon.com/storagegateway/latest/APIReference/Welcome.html)
        page.
        """
        if _request is None:
            _params = {}
            if volume_arn is not ShapeBase.NOT_SET:
                _params['volume_arn'] = volume_arn
            if snapshot_description is not ShapeBase.NOT_SET:
                _params['snapshot_description'] = snapshot_description
            _request = shapes.CreateSnapshotInput(**_params)
        response = self._boto_client.create_snapshot(**_request.to_boto())

        return shapes.CreateSnapshotOutput.from_boto(response)

    def create_snapshot_from_volume_recovery_point(
        self,
        _request: shapes.CreateSnapshotFromVolumeRecoveryPointInput = None,
        *,
        volume_arn: str,
        snapshot_description: str,
    ) -> shapes.CreateSnapshotFromVolumeRecoveryPointOutput:
        """
        Initiates a snapshot of a gateway from a volume recovery point. This operation
        is only supported in the cached volume gateway type.

        A volume recovery point is a point in time at which all data of the volume is
        consistent and from which you can create a snapshot. To get a list of volume
        recovery point for cached volume gateway, use ListVolumeRecoveryPoints.

        In the `CreateSnapshotFromVolumeRecoveryPoint` request, you identify the volume
        by providing its Amazon Resource Name (ARN). You must also provide a description
        for the snapshot. When the gateway takes a snapshot of the specified volume, the
        snapshot and its description appear in the AWS Storage Gateway console. In
        response, the gateway returns you a snapshot ID. You can use this snapshot ID to
        check the snapshot progress or later use it when you want to create a volume
        from a snapshot.

        To list or delete a snapshot, you must use the Amazon EC2 API. For more
        information, in _Amazon Elastic Compute Cloud API Reference_.
        """
        if _request is None:
            _params = {}
            if volume_arn is not ShapeBase.NOT_SET:
                _params['volume_arn'] = volume_arn
            if snapshot_description is not ShapeBase.NOT_SET:
                _params['snapshot_description'] = snapshot_description
            _request = shapes.CreateSnapshotFromVolumeRecoveryPointInput(
                **_params
            )
        response = self._boto_client.create_snapshot_from_volume_recovery_point(
            **_request.to_boto()
        )

        return shapes.CreateSnapshotFromVolumeRecoveryPointOutput.from_boto(
            response
        )

    def create_stored_iscsi_volume(
        self,
        _request: shapes.CreateStorediSCSIVolumeInput = None,
        *,
        gateway_arn: str,
        disk_id: str,
        preserve_existing_data: bool,
        target_name: str,
        network_interface_id: str,
        snapshot_id: str = ShapeBase.NOT_SET,
        kms_encrypted: bool = ShapeBase.NOT_SET,
        kms_key: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateStorediSCSIVolumeOutput:
        """
        Creates a volume on a specified gateway. This operation is only supported in the
        stored volume gateway type.

        The size of the volume to create is inferred from the disk size. You can choose
        to preserve existing data on the disk, create volume from an existing snapshot,
        or create an empty volume. If you choose to create an empty gateway volume, then
        any existing data on the disk is erased.

        In the request you must specify the gateway and the disk information on which
        you are creating the volume. In response, the gateway creates the volume and
        returns volume information such as the volume Amazon Resource Name (ARN), its
        size, and the iSCSI target ARN that initiators can use to connect to the volume
        target.
        """
        if _request is None:
            _params = {}
            if gateway_arn is not ShapeBase.NOT_SET:
                _params['gateway_arn'] = gateway_arn
            if disk_id is not ShapeBase.NOT_SET:
                _params['disk_id'] = disk_id
            if preserve_existing_data is not ShapeBase.NOT_SET:
                _params['preserve_existing_data'] = preserve_existing_data
            if target_name is not ShapeBase.NOT_SET:
                _params['target_name'] = target_name
            if network_interface_id is not ShapeBase.NOT_SET:
                _params['network_interface_id'] = network_interface_id
            if snapshot_id is not ShapeBase.NOT_SET:
                _params['snapshot_id'] = snapshot_id
            if kms_encrypted is not ShapeBase.NOT_SET:
                _params['kms_encrypted'] = kms_encrypted
            if kms_key is not ShapeBase.NOT_SET:
                _params['kms_key'] = kms_key
            _request = shapes.CreateStorediSCSIVolumeInput(**_params)
        response = self._boto_client.create_stored_iscsi_volume(
            **_request.to_boto()
        )

        return shapes.CreateStorediSCSIVolumeOutput.from_boto(response)

    def create_tape_with_barcode(
        self,
        _request: shapes.CreateTapeWithBarcodeInput = None,
        *,
        gateway_arn: str,
        tape_size_in_bytes: int,
        tape_barcode: str,
        kms_encrypted: bool = ShapeBase.NOT_SET,
        kms_key: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateTapeWithBarcodeOutput:
        """
        Creates a virtual tape by using your own barcode. You write data to the virtual
        tape and then archive the tape. A barcode is unique and can not be reused if it
        has already been used on a tape . This applies to barcodes used on deleted
        tapes. This operation is only supported in the tape gateway type.

        Cache storage must be allocated to the gateway before you can create a virtual
        tape. Use the AddCache operation to add cache storage to a gateway.
        """
        if _request is None:
            _params = {}
            if gateway_arn is not ShapeBase.NOT_SET:
                _params['gateway_arn'] = gateway_arn
            if tape_size_in_bytes is not ShapeBase.NOT_SET:
                _params['tape_size_in_bytes'] = tape_size_in_bytes
            if tape_barcode is not ShapeBase.NOT_SET:
                _params['tape_barcode'] = tape_barcode
            if kms_encrypted is not ShapeBase.NOT_SET:
                _params['kms_encrypted'] = kms_encrypted
            if kms_key is not ShapeBase.NOT_SET:
                _params['kms_key'] = kms_key
            _request = shapes.CreateTapeWithBarcodeInput(**_params)
        response = self._boto_client.create_tape_with_barcode(
            **_request.to_boto()
        )

        return shapes.CreateTapeWithBarcodeOutput.from_boto(response)

    def create_tapes(
        self,
        _request: shapes.CreateTapesInput = None,
        *,
        gateway_arn: str,
        tape_size_in_bytes: int,
        client_token: str,
        num_tapes_to_create: int,
        tape_barcode_prefix: str,
        kms_encrypted: bool = ShapeBase.NOT_SET,
        kms_key: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateTapesOutput:
        """
        Creates one or more virtual tapes. You write data to the virtual tapes and then
        archive the tapes. This operation is only supported in the tape gateway type.

        Cache storage must be allocated to the gateway before you can create virtual
        tapes. Use the AddCache operation to add cache storage to a gateway.
        """
        if _request is None:
            _params = {}
            if gateway_arn is not ShapeBase.NOT_SET:
                _params['gateway_arn'] = gateway_arn
            if tape_size_in_bytes is not ShapeBase.NOT_SET:
                _params['tape_size_in_bytes'] = tape_size_in_bytes
            if client_token is not ShapeBase.NOT_SET:
                _params['client_token'] = client_token
            if num_tapes_to_create is not ShapeBase.NOT_SET:
                _params['num_tapes_to_create'] = num_tapes_to_create
            if tape_barcode_prefix is not ShapeBase.NOT_SET:
                _params['tape_barcode_prefix'] = tape_barcode_prefix
            if kms_encrypted is not ShapeBase.NOT_SET:
                _params['kms_encrypted'] = kms_encrypted
            if kms_key is not ShapeBase.NOT_SET:
                _params['kms_key'] = kms_key
            _request = shapes.CreateTapesInput(**_params)
        response = self._boto_client.create_tapes(**_request.to_boto())

        return shapes.CreateTapesOutput.from_boto(response)

    def delete_bandwidth_rate_limit(
        self,
        _request: shapes.DeleteBandwidthRateLimitInput = None,
        *,
        gateway_arn: str,
        bandwidth_type: str,
    ) -> shapes.DeleteBandwidthRateLimitOutput:
        """
        Deletes the bandwidth rate limits of a gateway. You can delete either the upload
        and download bandwidth rate limit, or you can delete both. If you delete only
        one of the limits, the other limit remains unchanged. To specify which gateway
        to work with, use the Amazon Resource Name (ARN) of the gateway in your request.
        """
        if _request is None:
            _params = {}
            if gateway_arn is not ShapeBase.NOT_SET:
                _params['gateway_arn'] = gateway_arn
            if bandwidth_type is not ShapeBase.NOT_SET:
                _params['bandwidth_type'] = bandwidth_type
            _request = shapes.DeleteBandwidthRateLimitInput(**_params)
        response = self._boto_client.delete_bandwidth_rate_limit(
            **_request.to_boto()
        )

        return shapes.DeleteBandwidthRateLimitOutput.from_boto(response)

    def delete_chap_credentials(
        self,
        _request: shapes.DeleteChapCredentialsInput = None,
        *,
        target_arn: str,
        initiator_name: str,
    ) -> shapes.DeleteChapCredentialsOutput:
        """
        Deletes Challenge-Handshake Authentication Protocol (CHAP) credentials for a
        specified iSCSI target and initiator pair.
        """
        if _request is None:
            _params = {}
            if target_arn is not ShapeBase.NOT_SET:
                _params['target_arn'] = target_arn
            if initiator_name is not ShapeBase.NOT_SET:
                _params['initiator_name'] = initiator_name
            _request = shapes.DeleteChapCredentialsInput(**_params)
        response = self._boto_client.delete_chap_credentials(
            **_request.to_boto()
        )

        return shapes.DeleteChapCredentialsOutput.from_boto(response)

    def delete_file_share(
        self,
        _request: shapes.DeleteFileShareInput = None,
        *,
        file_share_arn: str,
        force_delete: bool = ShapeBase.NOT_SET,
    ) -> shapes.DeleteFileShareOutput:
        """
        Deletes a file share from a file gateway. This operation is only supported for
        file gateways.
        """
        if _request is None:
            _params = {}
            if file_share_arn is not ShapeBase.NOT_SET:
                _params['file_share_arn'] = file_share_arn
            if force_delete is not ShapeBase.NOT_SET:
                _params['force_delete'] = force_delete
            _request = shapes.DeleteFileShareInput(**_params)
        response = self._boto_client.delete_file_share(**_request.to_boto())

        return shapes.DeleteFileShareOutput.from_boto(response)

    def delete_gateway(
        self,
        _request: shapes.DeleteGatewayInput = None,
        *,
        gateway_arn: str,
    ) -> shapes.DeleteGatewayOutput:
        """
        Deletes a gateway. To specify which gateway to delete, use the Amazon Resource
        Name (ARN) of the gateway in your request. The operation deletes the gateway;
        however, it does not delete the gateway virtual machine (VM) from your host
        computer.

        After you delete a gateway, you cannot reactivate it. Completed snapshots of the
        gateway volumes are not deleted upon deleting the gateway, however, pending
        snapshots will not complete. After you delete a gateway, your next step is to
        remove it from your environment.

        You no longer pay software charges after the gateway is deleted; however, your
        existing Amazon EBS snapshots persist and you will continue to be billed for
        these snapshots. You can choose to remove all remaining Amazon EBS snapshots by
        canceling your Amazon EC2 subscription. If you prefer not to cancel your Amazon
        EC2 subscription, you can delete your snapshots using the Amazon EC2 console.
        For more information, see the [ AWS Storage Gateway Detail
        Page](http://aws.amazon.com/storagegateway).
        """
        if _request is None:
            _params = {}
            if gateway_arn is not ShapeBase.NOT_SET:
                _params['gateway_arn'] = gateway_arn
            _request = shapes.DeleteGatewayInput(**_params)
        response = self._boto_client.delete_gateway(**_request.to_boto())

        return shapes.DeleteGatewayOutput.from_boto(response)

    def delete_snapshot_schedule(
        self,
        _request: shapes.DeleteSnapshotScheduleInput = None,
        *,
        volume_arn: str,
    ) -> shapes.DeleteSnapshotScheduleOutput:
        """
        Deletes a snapshot of a volume.

        You can take snapshots of your gateway volumes on a scheduled or ad hoc basis.
        This API action enables you to delete a snapshot schedule for a volume. For more
        information, see [Working with
        Snapshots](http://docs.aws.amazon.com/storagegateway/latest/userguide/WorkingWithSnapshots.html).
        In the `DeleteSnapshotSchedule` request, you identify the volume by providing
        its Amazon Resource Name (ARN). This operation is only supported in stored and
        cached volume gateway types.

        To list or delete a snapshot, you must use the Amazon EC2 API. in _Amazon
        Elastic Compute Cloud API Reference_.
        """
        if _request is None:
            _params = {}
            if volume_arn is not ShapeBase.NOT_SET:
                _params['volume_arn'] = volume_arn
            _request = shapes.DeleteSnapshotScheduleInput(**_params)
        response = self._boto_client.delete_snapshot_schedule(
            **_request.to_boto()
        )

        return shapes.DeleteSnapshotScheduleOutput.from_boto(response)

    def delete_tape(
        self,
        _request: shapes.DeleteTapeInput = None,
        *,
        gateway_arn: str,
        tape_arn: str,
    ) -> shapes.DeleteTapeOutput:
        """
        Deletes the specified virtual tape. This operation is only supported in the tape
        gateway type.
        """
        if _request is None:
            _params = {}
            if gateway_arn is not ShapeBase.NOT_SET:
                _params['gateway_arn'] = gateway_arn
            if tape_arn is not ShapeBase.NOT_SET:
                _params['tape_arn'] = tape_arn
            _request = shapes.DeleteTapeInput(**_params)
        response = self._boto_client.delete_tape(**_request.to_boto())

        return shapes.DeleteTapeOutput.from_boto(response)

    def delete_tape_archive(
        self,
        _request: shapes.DeleteTapeArchiveInput = None,
        *,
        tape_arn: str,
    ) -> shapes.DeleteTapeArchiveOutput:
        """
        Deletes the specified virtual tape from the virtual tape shelf (VTS). This
        operation is only supported in the tape gateway type.
        """
        if _request is None:
            _params = {}
            if tape_arn is not ShapeBase.NOT_SET:
                _params['tape_arn'] = tape_arn
            _request = shapes.DeleteTapeArchiveInput(**_params)
        response = self._boto_client.delete_tape_archive(**_request.to_boto())

        return shapes.DeleteTapeArchiveOutput.from_boto(response)

    def delete_volume(
        self,
        _request: shapes.DeleteVolumeInput = None,
        *,
        volume_arn: str,
    ) -> shapes.DeleteVolumeOutput:
        """
        Deletes the specified storage volume that you previously created using the
        CreateCachediSCSIVolume or CreateStorediSCSIVolume API. This operation is only
        supported in the cached volume and stored volume types. For stored volume
        gateways, the local disk that was configured as the storage volume is not
        deleted. You can reuse the local disk to create another storage volume.

        Before you delete a volume, make sure there are no iSCSI connections to the
        volume you are deleting. You should also make sure there is no snapshot in
        progress. You can use the Amazon Elastic Compute Cloud (Amazon EC2) API to query
        snapshots on the volume you are deleting and check the snapshot status. For more
        information, go to
        [DescribeSnapshots](http://docs.aws.amazon.com/AWSEC2/latest/APIReference/ApiReference-
        query-DescribeSnapshots.html) in the _Amazon Elastic Compute Cloud API
        Reference_.

        In the request, you must provide the Amazon Resource Name (ARN) of the storage
        volume you want to delete.
        """
        if _request is None:
            _params = {}
            if volume_arn is not ShapeBase.NOT_SET:
                _params['volume_arn'] = volume_arn
            _request = shapes.DeleteVolumeInput(**_params)
        response = self._boto_client.delete_volume(**_request.to_boto())

        return shapes.DeleteVolumeOutput.from_boto(response)

    def describe_bandwidth_rate_limit(
        self,
        _request: shapes.DescribeBandwidthRateLimitInput = None,
        *,
        gateway_arn: str,
    ) -> shapes.DescribeBandwidthRateLimitOutput:
        """
        Returns the bandwidth rate limits of a gateway. By default, these limits are not
        set, which means no bandwidth rate limiting is in effect.

        This operation only returns a value for a bandwidth rate limit only if the limit
        is set. If no limits are set for the gateway, then this operation returns only
        the gateway ARN in the response body. To specify which gateway to describe, use
        the Amazon Resource Name (ARN) of the gateway in your request.
        """
        if _request is None:
            _params = {}
            if gateway_arn is not ShapeBase.NOT_SET:
                _params['gateway_arn'] = gateway_arn
            _request = shapes.DescribeBandwidthRateLimitInput(**_params)
        response = self._boto_client.describe_bandwidth_rate_limit(
            **_request.to_boto()
        )

        return shapes.DescribeBandwidthRateLimitOutput.from_boto(response)

    def describe_cache(
        self,
        _request: shapes.DescribeCacheInput = None,
        *,
        gateway_arn: str,
    ) -> shapes.DescribeCacheOutput:
        """
        Returns information about the cache of a gateway. This operation is only
        supported in the cached volume, tape and file gateway types.

        The response includes disk IDs that are configured as cache, and it includes the
        amount of cache allocated and used.
        """
        if _request is None:
            _params = {}
            if gateway_arn is not ShapeBase.NOT_SET:
                _params['gateway_arn'] = gateway_arn
            _request = shapes.DescribeCacheInput(**_params)
        response = self._boto_client.describe_cache(**_request.to_boto())

        return shapes.DescribeCacheOutput.from_boto(response)

    def describe_cached_iscsi_volumes(
        self,
        _request: shapes.DescribeCachediSCSIVolumesInput = None,
        *,
        volume_arns: typing.List[str],
    ) -> shapes.DescribeCachediSCSIVolumesOutput:
        """
        Returns a description of the gateway volumes specified in the request. This
        operation is only supported in the cached volume gateway types.

        The list of gateway volumes in the request must be from one gateway. In the
        response Amazon Storage Gateway returns volume information sorted by volume
        Amazon Resource Name (ARN).
        """
        if _request is None:
            _params = {}
            if volume_arns is not ShapeBase.NOT_SET:
                _params['volume_arns'] = volume_arns
            _request = shapes.DescribeCachediSCSIVolumesInput(**_params)
        response = self._boto_client.describe_cached_iscsi_volumes(
            **_request.to_boto()
        )

        return shapes.DescribeCachediSCSIVolumesOutput.from_boto(response)

    def describe_chap_credentials(
        self,
        _request: shapes.DescribeChapCredentialsInput = None,
        *,
        target_arn: str,
    ) -> shapes.DescribeChapCredentialsOutput:
        """
        Returns an array of Challenge-Handshake Authentication Protocol (CHAP)
        credentials information for a specified iSCSI target, one for each target-
        initiator pair.
        """
        if _request is None:
            _params = {}
            if target_arn is not ShapeBase.NOT_SET:
                _params['target_arn'] = target_arn
            _request = shapes.DescribeChapCredentialsInput(**_params)
        response = self._boto_client.describe_chap_credentials(
            **_request.to_boto()
        )

        return shapes.DescribeChapCredentialsOutput.from_boto(response)

    def describe_gateway_information(
        self,
        _request: shapes.DescribeGatewayInformationInput = None,
        *,
        gateway_arn: str,
    ) -> shapes.DescribeGatewayInformationOutput:
        """
        Returns metadata about a gateway such as its name, network interfaces,
        configured time zone, and the state (whether the gateway is running or not). To
        specify which gateway to describe, use the Amazon Resource Name (ARN) of the
        gateway in your request.
        """
        if _request is None:
            _params = {}
            if gateway_arn is not ShapeBase.NOT_SET:
                _params['gateway_arn'] = gateway_arn
            _request = shapes.DescribeGatewayInformationInput(**_params)
        response = self._boto_client.describe_gateway_information(
            **_request.to_boto()
        )

        return shapes.DescribeGatewayInformationOutput.from_boto(response)

    def describe_maintenance_start_time(
        self,
        _request: shapes.DescribeMaintenanceStartTimeInput = None,
        *,
        gateway_arn: str,
    ) -> shapes.DescribeMaintenanceStartTimeOutput:
        """
        Returns your gateway's weekly maintenance start time including the day and time
        of the week. Note that values are in terms of the gateway's time zone.
        """
        if _request is None:
            _params = {}
            if gateway_arn is not ShapeBase.NOT_SET:
                _params['gateway_arn'] = gateway_arn
            _request = shapes.DescribeMaintenanceStartTimeInput(**_params)
        response = self._boto_client.describe_maintenance_start_time(
            **_request.to_boto()
        )

        return shapes.DescribeMaintenanceStartTimeOutput.from_boto(response)

    def describe_nfs_file_shares(
        self,
        _request: shapes.DescribeNFSFileSharesInput = None,
        *,
        file_share_arn_list: typing.List[str],
    ) -> shapes.DescribeNFSFileSharesOutput:
        """
        Gets a description for one or more Network File System (NFS) file shares from a
        file gateway. This operation is only supported for file gateways.
        """
        if _request is None:
            _params = {}
            if file_share_arn_list is not ShapeBase.NOT_SET:
                _params['file_share_arn_list'] = file_share_arn_list
            _request = shapes.DescribeNFSFileSharesInput(**_params)
        response = self._boto_client.describe_nfs_file_shares(
            **_request.to_boto()
        )

        return shapes.DescribeNFSFileSharesOutput.from_boto(response)

    def describe_smb_file_shares(
        self,
        _request: shapes.DescribeSMBFileSharesInput = None,
        *,
        file_share_arn_list: typing.List[str],
    ) -> shapes.DescribeSMBFileSharesOutput:
        """
        Gets a description for one or more Server Message Block (SMB) file shares from a
        file gateway. This operation is only supported for file gateways.
        """
        if _request is None:
            _params = {}
            if file_share_arn_list is not ShapeBase.NOT_SET:
                _params['file_share_arn_list'] = file_share_arn_list
            _request = shapes.DescribeSMBFileSharesInput(**_params)
        response = self._boto_client.describe_smb_file_shares(
            **_request.to_boto()
        )

        return shapes.DescribeSMBFileSharesOutput.from_boto(response)

    def describe_smb_settings(
        self,
        _request: shapes.DescribeSMBSettingsInput = None,
        *,
        gateway_arn: str,
    ) -> shapes.DescribeSMBSettingsOutput:
        """
        Gets a description of a Server Message Block (SMB) file share settings from a
        file gateway. This operation is only supported for file gateways.
        """
        if _request is None:
            _params = {}
            if gateway_arn is not ShapeBase.NOT_SET:
                _params['gateway_arn'] = gateway_arn
            _request = shapes.DescribeSMBSettingsInput(**_params)
        response = self._boto_client.describe_smb_settings(**_request.to_boto())

        return shapes.DescribeSMBSettingsOutput.from_boto(response)

    def describe_snapshot_schedule(
        self,
        _request: shapes.DescribeSnapshotScheduleInput = None,
        *,
        volume_arn: str,
    ) -> shapes.DescribeSnapshotScheduleOutput:
        """
        Describes the snapshot schedule for the specified gateway volume. The snapshot
        schedule information includes intervals at which snapshots are automatically
        initiated on the volume. This operation is only supported in the cached volume
        and stored volume types.
        """
        if _request is None:
            _params = {}
            if volume_arn is not ShapeBase.NOT_SET:
                _params['volume_arn'] = volume_arn
            _request = shapes.DescribeSnapshotScheduleInput(**_params)
        response = self._boto_client.describe_snapshot_schedule(
            **_request.to_boto()
        )

        return shapes.DescribeSnapshotScheduleOutput.from_boto(response)

    def describe_stored_iscsi_volumes(
        self,
        _request: shapes.DescribeStorediSCSIVolumesInput = None,
        *,
        volume_arns: typing.List[str],
    ) -> shapes.DescribeStorediSCSIVolumesOutput:
        """
        Returns the description of the gateway volumes specified in the request. The
        list of gateway volumes in the request must be from one gateway. In the response
        Amazon Storage Gateway returns volume information sorted by volume ARNs. This
        operation is only supported in stored volume gateway type.
        """
        if _request is None:
            _params = {}
            if volume_arns is not ShapeBase.NOT_SET:
                _params['volume_arns'] = volume_arns
            _request = shapes.DescribeStorediSCSIVolumesInput(**_params)
        response = self._boto_client.describe_stored_iscsi_volumes(
            **_request.to_boto()
        )

        return shapes.DescribeStorediSCSIVolumesOutput.from_boto(response)

    def describe_tape_archives(
        self,
        _request: shapes.DescribeTapeArchivesInput = None,
        *,
        tape_arns: typing.List[str] = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
        limit: int = ShapeBase.NOT_SET,
    ) -> shapes.DescribeTapeArchivesOutput:
        """
        Returns a description of specified virtual tapes in the virtual tape shelf
        (VTS). This operation is only supported in the tape gateway type.

        If a specific `TapeARN` is not specified, AWS Storage Gateway returns a
        description of all virtual tapes found in the VTS associated with your account.
        """
        if _request is None:
            _params = {}
            if tape_arns is not ShapeBase.NOT_SET:
                _params['tape_arns'] = tape_arns
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            _request = shapes.DescribeTapeArchivesInput(**_params)
        paginator = self.get_paginator("describe_tape_archives").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.DescribeTapeArchivesOutput.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.DescribeTapeArchivesOutput.from_boto(response)

    def describe_tape_recovery_points(
        self,
        _request: shapes.DescribeTapeRecoveryPointsInput = None,
        *,
        gateway_arn: str,
        marker: str = ShapeBase.NOT_SET,
        limit: int = ShapeBase.NOT_SET,
    ) -> shapes.DescribeTapeRecoveryPointsOutput:
        """
        Returns a list of virtual tape recovery points that are available for the
        specified tape gateway.

        A recovery point is a point-in-time view of a virtual tape at which all the data
        on the virtual tape is consistent. If your gateway crashes, virtual tapes that
        have recovery points can be recovered to a new gateway. This operation is only
        supported in the tape gateway type.
        """
        if _request is None:
            _params = {}
            if gateway_arn is not ShapeBase.NOT_SET:
                _params['gateway_arn'] = gateway_arn
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            _request = shapes.DescribeTapeRecoveryPointsInput(**_params)
        paginator = self.get_paginator("describe_tape_recovery_points"
                                      ).paginate(**_request.to_boto())
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.DescribeTapeRecoveryPointsOutput.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.DescribeTapeRecoveryPointsOutput.from_boto(response)

    def describe_tapes(
        self,
        _request: shapes.DescribeTapesInput = None,
        *,
        gateway_arn: str,
        tape_arns: typing.List[str] = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
        limit: int = ShapeBase.NOT_SET,
    ) -> shapes.DescribeTapesOutput:
        """
        Returns a description of the specified Amazon Resource Name (ARN) of virtual
        tapes. If a `TapeARN` is not specified, returns a description of all virtual
        tapes associated with the specified gateway. This operation is only supported in
        the tape gateway type.
        """
        if _request is None:
            _params = {}
            if gateway_arn is not ShapeBase.NOT_SET:
                _params['gateway_arn'] = gateway_arn
            if tape_arns is not ShapeBase.NOT_SET:
                _params['tape_arns'] = tape_arns
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            _request = shapes.DescribeTapesInput(**_params)
        paginator = self.get_paginator("describe_tapes").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.DescribeTapesOutput.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.DescribeTapesOutput.from_boto(response)

    def describe_upload_buffer(
        self,
        _request: shapes.DescribeUploadBufferInput = None,
        *,
        gateway_arn: str,
    ) -> shapes.DescribeUploadBufferOutput:
        """
        Returns information about the upload buffer of a gateway. This operation is
        supported for the stored volume, cached volume and tape gateway types.

        The response includes disk IDs that are configured as upload buffer space, and
        it includes the amount of upload buffer space allocated and used.
        """
        if _request is None:
            _params = {}
            if gateway_arn is not ShapeBase.NOT_SET:
                _params['gateway_arn'] = gateway_arn
            _request = shapes.DescribeUploadBufferInput(**_params)
        response = self._boto_client.describe_upload_buffer(
            **_request.to_boto()
        )

        return shapes.DescribeUploadBufferOutput.from_boto(response)

    def describe_vtl_devices(
        self,
        _request: shapes.DescribeVTLDevicesInput = None,
        *,
        gateway_arn: str,
        vtl_device_arns: typing.List[str] = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
        limit: int = ShapeBase.NOT_SET,
    ) -> shapes.DescribeVTLDevicesOutput:
        """
        Returns a description of virtual tape library (VTL) devices for the specified
        tape gateway. In the response, AWS Storage Gateway returns VTL device
        information.

        This operation is only supported in the tape gateway type.
        """
        if _request is None:
            _params = {}
            if gateway_arn is not ShapeBase.NOT_SET:
                _params['gateway_arn'] = gateway_arn
            if vtl_device_arns is not ShapeBase.NOT_SET:
                _params['vtl_device_arns'] = vtl_device_arns
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            _request = shapes.DescribeVTLDevicesInput(**_params)
        paginator = self.get_paginator("describe_vtl_devices").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.DescribeVTLDevicesOutput.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.DescribeVTLDevicesOutput.from_boto(response)

    def describe_working_storage(
        self,
        _request: shapes.DescribeWorkingStorageInput = None,
        *,
        gateway_arn: str,
    ) -> shapes.DescribeWorkingStorageOutput:
        """
        Returns information about the working storage of a gateway. This operation is
        only supported in the stored volumes gateway type. This operation is deprecated
        in cached volumes API version (20120630). Use DescribeUploadBuffer instead.

        Working storage is also referred to as upload buffer. You can also use the
        DescribeUploadBuffer operation to add upload buffer to a stored volume gateway.

        The response includes disk IDs that are configured as working storage, and it
        includes the amount of working storage allocated and used.
        """
        if _request is None:
            _params = {}
            if gateway_arn is not ShapeBase.NOT_SET:
                _params['gateway_arn'] = gateway_arn
            _request = shapes.DescribeWorkingStorageInput(**_params)
        response = self._boto_client.describe_working_storage(
            **_request.to_boto()
        )

        return shapes.DescribeWorkingStorageOutput.from_boto(response)

    def disable_gateway(
        self,
        _request: shapes.DisableGatewayInput = None,
        *,
        gateway_arn: str,
    ) -> shapes.DisableGatewayOutput:
        """
        Disables a tape gateway when the gateway is no longer functioning. For example,
        if your gateway VM is damaged, you can disable the gateway so you can recover
        virtual tapes.

        Use this operation for a tape gateway that is not reachable or not functioning.
        This operation is only supported in the tape gateway type.

        Once a gateway is disabled it cannot be enabled.
        """
        if _request is None:
            _params = {}
            if gateway_arn is not ShapeBase.NOT_SET:
                _params['gateway_arn'] = gateway_arn
            _request = shapes.DisableGatewayInput(**_params)
        response = self._boto_client.disable_gateway(**_request.to_boto())

        return shapes.DisableGatewayOutput.from_boto(response)

    def join_domain(
        self,
        _request: shapes.JoinDomainInput = None,
        *,
        gateway_arn: str,
        domain_name: str,
        user_name: str,
        password: str,
    ) -> shapes.JoinDomainOutput:
        """
        Adds a file gateway to an Active Directory domain. This operation is only
        supported for file gateways that support the SMB file protocol.
        """
        if _request is None:
            _params = {}
            if gateway_arn is not ShapeBase.NOT_SET:
                _params['gateway_arn'] = gateway_arn
            if domain_name is not ShapeBase.NOT_SET:
                _params['domain_name'] = domain_name
            if user_name is not ShapeBase.NOT_SET:
                _params['user_name'] = user_name
            if password is not ShapeBase.NOT_SET:
                _params['password'] = password
            _request = shapes.JoinDomainInput(**_params)
        response = self._boto_client.join_domain(**_request.to_boto())

        return shapes.JoinDomainOutput.from_boto(response)

    def list_file_shares(
        self,
        _request: shapes.ListFileSharesInput = None,
        *,
        gateway_arn: str = ShapeBase.NOT_SET,
        limit: int = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
    ) -> shapes.ListFileSharesOutput:
        """
        Gets a list of the file shares for a specific file gateway, or the list of file
        shares that belong to the calling user account. This operation is only supported
        for file gateways.
        """
        if _request is None:
            _params = {}
            if gateway_arn is not ShapeBase.NOT_SET:
                _params['gateway_arn'] = gateway_arn
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            _request = shapes.ListFileSharesInput(**_params)
        response = self._boto_client.list_file_shares(**_request.to_boto())

        return shapes.ListFileSharesOutput.from_boto(response)

    def list_gateways(
        self,
        _request: shapes.ListGatewaysInput = None,
        *,
        marker: str = ShapeBase.NOT_SET,
        limit: int = ShapeBase.NOT_SET,
    ) -> shapes.ListGatewaysOutput:
        """
        Lists gateways owned by an AWS account in a region specified in the request. The
        returned list is ordered by gateway Amazon Resource Name (ARN).

        By default, the operation returns a maximum of 100 gateways. This operation
        supports pagination that allows you to optionally reduce the number of gateways
        returned in a response.

        If you have more gateways than are returned in a response (that is, the response
        returns only a truncated list of your gateways), the response contains a marker
        that you can specify in your next request to fetch the next page of gateways.
        """
        if _request is None:
            _params = {}
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            _request = shapes.ListGatewaysInput(**_params)
        paginator = self.get_paginator("list_gateways").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListGatewaysOutput.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListGatewaysOutput.from_boto(response)

    def list_local_disks(
        self,
        _request: shapes.ListLocalDisksInput = None,
        *,
        gateway_arn: str,
    ) -> shapes.ListLocalDisksOutput:
        """
        Returns a list of the gateway's local disks. To specify which gateway to
        describe, you use the Amazon Resource Name (ARN) of the gateway in the body of
        the request.

        The request returns a list of all disks, specifying which are configured as
        working storage, cache storage, or stored volume or not configured at all. The
        response includes a `DiskStatus` field. This field can have a value of present
        (the disk is available to use), missing (the disk is no longer connected to the
        gateway), or mismatch (the disk node is occupied by a disk that has incorrect
        metadata or the disk content is corrupted).
        """
        if _request is None:
            _params = {}
            if gateway_arn is not ShapeBase.NOT_SET:
                _params['gateway_arn'] = gateway_arn
            _request = shapes.ListLocalDisksInput(**_params)
        response = self._boto_client.list_local_disks(**_request.to_boto())

        return shapes.ListLocalDisksOutput.from_boto(response)

    def list_tags_for_resource(
        self,
        _request: shapes.ListTagsForResourceInput = None,
        *,
        resource_arn: str,
        marker: str = ShapeBase.NOT_SET,
        limit: int = ShapeBase.NOT_SET,
    ) -> shapes.ListTagsForResourceOutput:
        """
        Lists the tags that have been added to the specified resource. This operation is
        only supported in the cached volume, stored volume and tape gateway type.
        """
        if _request is None:
            _params = {}
            if resource_arn is not ShapeBase.NOT_SET:
                _params['resource_arn'] = resource_arn
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            _request = shapes.ListTagsForResourceInput(**_params)
        response = self._boto_client.list_tags_for_resource(
            **_request.to_boto()
        )

        return shapes.ListTagsForResourceOutput.from_boto(response)

    def list_tapes(
        self,
        _request: shapes.ListTapesInput = None,
        *,
        tape_arns: typing.List[str] = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
        limit: int = ShapeBase.NOT_SET,
    ) -> shapes.ListTapesOutput:
        """
        Lists virtual tapes in your virtual tape library (VTL) and your virtual tape
        shelf (VTS). You specify the tapes to list by specifying one or more tape Amazon
        Resource Names (ARNs). If you don't specify a tape ARN, the operation lists all
        virtual tapes in both your VTL and VTS.

        This operation supports pagination. By default, the operation returns a maximum
        of up to 100 tapes. You can optionally specify the `Limit` parameter in the body
        to limit the number of tapes in the response. If the number of tapes returned in
        the response is truncated, the response includes a `Marker` element that you can
        use in your subsequent request to retrieve the next set of tapes. This operation
        is only supported in the tape gateway type.
        """
        if _request is None:
            _params = {}
            if tape_arns is not ShapeBase.NOT_SET:
                _params['tape_arns'] = tape_arns
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            _request = shapes.ListTapesInput(**_params)
        response = self._boto_client.list_tapes(**_request.to_boto())

        return shapes.ListTapesOutput.from_boto(response)

    def list_volume_initiators(
        self,
        _request: shapes.ListVolumeInitiatorsInput = None,
        *,
        volume_arn: str,
    ) -> shapes.ListVolumeInitiatorsOutput:
        """
        Lists iSCSI initiators that are connected to a volume. You can use this
        operation to determine whether a volume is being used or not. This operation is
        only supported in the cached volume and stored volume gateway types.
        """
        if _request is None:
            _params = {}
            if volume_arn is not ShapeBase.NOT_SET:
                _params['volume_arn'] = volume_arn
            _request = shapes.ListVolumeInitiatorsInput(**_params)
        response = self._boto_client.list_volume_initiators(
            **_request.to_boto()
        )

        return shapes.ListVolumeInitiatorsOutput.from_boto(response)

    def list_volume_recovery_points(
        self,
        _request: shapes.ListVolumeRecoveryPointsInput = None,
        *,
        gateway_arn: str,
    ) -> shapes.ListVolumeRecoveryPointsOutput:
        """
        Lists the recovery points for a specified gateway. This operation is only
        supported in the cached volume gateway type.

        Each cache volume has one recovery point. A volume recovery point is a point in
        time at which all data of the volume is consistent and from which you can create
        a snapshot or clone a new cached volume from a source volume. To create a
        snapshot from a volume recovery point use the
        CreateSnapshotFromVolumeRecoveryPoint operation.
        """
        if _request is None:
            _params = {}
            if gateway_arn is not ShapeBase.NOT_SET:
                _params['gateway_arn'] = gateway_arn
            _request = shapes.ListVolumeRecoveryPointsInput(**_params)
        response = self._boto_client.list_volume_recovery_points(
            **_request.to_boto()
        )

        return shapes.ListVolumeRecoveryPointsOutput.from_boto(response)

    def list_volumes(
        self,
        _request: shapes.ListVolumesInput = None,
        *,
        gateway_arn: str = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
        limit: int = ShapeBase.NOT_SET,
    ) -> shapes.ListVolumesOutput:
        """
        Lists the iSCSI stored volumes of a gateway. Results are sorted by volume ARN.
        The response includes only the volume ARNs. If you want additional volume
        information, use the DescribeStorediSCSIVolumes or the
        DescribeCachediSCSIVolumes API.

        The operation supports pagination. By default, the operation returns a maximum
        of up to 100 volumes. You can optionally specify the `Limit` field in the body
        to limit the number of volumes in the response. If the number of volumes
        returned in the response is truncated, the response includes a Marker field. You
        can use this Marker value in your subsequent request to retrieve the next set of
        volumes. This operation is only supported in the cached volume and stored volume
        gateway types.
        """
        if _request is None:
            _params = {}
            if gateway_arn is not ShapeBase.NOT_SET:
                _params['gateway_arn'] = gateway_arn
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            _request = shapes.ListVolumesInput(**_params)
        paginator = self.get_paginator("list_volumes").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListVolumesOutput.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListVolumesOutput.from_boto(response)

    def notify_when_uploaded(
        self,
        _request: shapes.NotifyWhenUploadedInput = None,
        *,
        file_share_arn: str,
    ) -> shapes.NotifyWhenUploadedOutput:
        """
        Sends you notification through CloudWatch Events when all files written to your
        NFS file share have been uploaded to Amazon S3.

        AWS Storage Gateway can send a notification through Amazon CloudWatch Events
        when all files written to your file share up to that point in time have been
        uploaded to Amazon S3. These files include files written to the NFS file share
        up to the time that you make a request for notification. When the upload is
        done, Storage Gateway sends you notification through an Amazon CloudWatch Event.
        You can configure CloudWatch Events to send the notification through event
        targets such as Amazon SNS or AWS Lambda function. This operation is only
        supported for file gateways.

        For more information, see Getting File Upload Notification in the Storage
        Gateway User Guide
        (https://docs.aws.amazon.com/storagegateway/latest/userguide/monitoring-file-
        gateway.html#get-upload-notification).
        """
        if _request is None:
            _params = {}
            if file_share_arn is not ShapeBase.NOT_SET:
                _params['file_share_arn'] = file_share_arn
            _request = shapes.NotifyWhenUploadedInput(**_params)
        response = self._boto_client.notify_when_uploaded(**_request.to_boto())

        return shapes.NotifyWhenUploadedOutput.from_boto(response)

    def refresh_cache(
        self,
        _request: shapes.RefreshCacheInput = None,
        *,
        file_share_arn: str,
    ) -> shapes.RefreshCacheOutput:
        """
        Refreshes the cache for the specified file share. This operation finds objects
        in the Amazon S3 bucket that were added, removed or replaced since the gateway
        last listed the bucket's contents and cached the results. This operation is only
        supported in the file gateway type.
        """
        if _request is None:
            _params = {}
            if file_share_arn is not ShapeBase.NOT_SET:
                _params['file_share_arn'] = file_share_arn
            _request = shapes.RefreshCacheInput(**_params)
        response = self._boto_client.refresh_cache(**_request.to_boto())

        return shapes.RefreshCacheOutput.from_boto(response)

    def remove_tags_from_resource(
        self,
        _request: shapes.RemoveTagsFromResourceInput = None,
        *,
        resource_arn: str,
        tag_keys: typing.List[str],
    ) -> shapes.RemoveTagsFromResourceOutput:
        """
        Removes one or more tags from the specified resource. This operation is only
        supported in the cached volume, stored volume and tape gateway types.
        """
        if _request is None:
            _params = {}
            if resource_arn is not ShapeBase.NOT_SET:
                _params['resource_arn'] = resource_arn
            if tag_keys is not ShapeBase.NOT_SET:
                _params['tag_keys'] = tag_keys
            _request = shapes.RemoveTagsFromResourceInput(**_params)
        response = self._boto_client.remove_tags_from_resource(
            **_request.to_boto()
        )

        return shapes.RemoveTagsFromResourceOutput.from_boto(response)

    def reset_cache(
        self,
        _request: shapes.ResetCacheInput = None,
        *,
        gateway_arn: str,
    ) -> shapes.ResetCacheOutput:
        """
        Resets all cache disks that have encountered a error and makes the disks
        available for reconfiguration as cache storage. If your cache disk encounters a
        error, the gateway prevents read and write operations on virtual tapes in the
        gateway. For example, an error can occur when a disk is corrupted or removed
        from the gateway. When a cache is reset, the gateway loses its cache storage. At
        this point you can reconfigure the disks as cache disks. This operation is only
        supported in the cached volume and tape types.

        If the cache disk you are resetting contains data that has not been uploaded to
        Amazon S3 yet, that data can be lost. After you reset cache disks, there will be
        no configured cache disks left in the gateway, so you must configure at least
        one new cache disk for your gateway to function properly.
        """
        if _request is None:
            _params = {}
            if gateway_arn is not ShapeBase.NOT_SET:
                _params['gateway_arn'] = gateway_arn
            _request = shapes.ResetCacheInput(**_params)
        response = self._boto_client.reset_cache(**_request.to_boto())

        return shapes.ResetCacheOutput.from_boto(response)

    def retrieve_tape_archive(
        self,
        _request: shapes.RetrieveTapeArchiveInput = None,
        *,
        tape_arn: str,
        gateway_arn: str,
    ) -> shapes.RetrieveTapeArchiveOutput:
        """
        Retrieves an archived virtual tape from the virtual tape shelf (VTS) to a tape
        gateway. Virtual tapes archived in the VTS are not associated with any gateway.
        However after a tape is retrieved, it is associated with a gateway, even though
        it is also listed in the VTS, that is, archive. This operation is only supported
        in the tape gateway type.

        Once a tape is successfully retrieved to a gateway, it cannot be retrieved again
        to another gateway. You must archive the tape again before you can retrieve it
        to another gateway. This operation is only supported in the tape gateway type.
        """
        if _request is None:
            _params = {}
            if tape_arn is not ShapeBase.NOT_SET:
                _params['tape_arn'] = tape_arn
            if gateway_arn is not ShapeBase.NOT_SET:
                _params['gateway_arn'] = gateway_arn
            _request = shapes.RetrieveTapeArchiveInput(**_params)
        response = self._boto_client.retrieve_tape_archive(**_request.to_boto())

        return shapes.RetrieveTapeArchiveOutput.from_boto(response)

    def retrieve_tape_recovery_point(
        self,
        _request: shapes.RetrieveTapeRecoveryPointInput = None,
        *,
        tape_arn: str,
        gateway_arn: str,
    ) -> shapes.RetrieveTapeRecoveryPointOutput:
        """
        Retrieves the recovery point for the specified virtual tape. This operation is
        only supported in the tape gateway type.

        A recovery point is a point in time view of a virtual tape at which all the data
        on the tape is consistent. If your gateway crashes, virtual tapes that have
        recovery points can be recovered to a new gateway.

        The virtual tape can be retrieved to only one gateway. The retrieved tape is
        read-only. The virtual tape can be retrieved to only a tape gateway. There is no
        charge for retrieving recovery points.
        """
        if _request is None:
            _params = {}
            if tape_arn is not ShapeBase.NOT_SET:
                _params['tape_arn'] = tape_arn
            if gateway_arn is not ShapeBase.NOT_SET:
                _params['gateway_arn'] = gateway_arn
            _request = shapes.RetrieveTapeRecoveryPointInput(**_params)
        response = self._boto_client.retrieve_tape_recovery_point(
            **_request.to_boto()
        )

        return shapes.RetrieveTapeRecoveryPointOutput.from_boto(response)

    def set_local_console_password(
        self,
        _request: shapes.SetLocalConsolePasswordInput = None,
        *,
        gateway_arn: str,
        local_console_password: str,
    ) -> shapes.SetLocalConsolePasswordOutput:
        """
        Sets the password for your VM local console. When you log in to the local
        console for the first time, you log in to the VM with the default credentials.
        We recommend that you set a new password. You don't need to know the default
        password to set a new password.
        """
        if _request is None:
            _params = {}
            if gateway_arn is not ShapeBase.NOT_SET:
                _params['gateway_arn'] = gateway_arn
            if local_console_password is not ShapeBase.NOT_SET:
                _params['local_console_password'] = local_console_password
            _request = shapes.SetLocalConsolePasswordInput(**_params)
        response = self._boto_client.set_local_console_password(
            **_request.to_boto()
        )

        return shapes.SetLocalConsolePasswordOutput.from_boto(response)

    def set_smb_guest_password(
        self,
        _request: shapes.SetSMBGuestPasswordInput = None,
        *,
        gateway_arn: str,
        password: str,
    ) -> shapes.SetSMBGuestPasswordOutput:
        """
        Sets the password for the guest user `smbguest`. The `smbguest` user is the user
        when the authentication method for the file share is set to `GuestAccess`.
        """
        if _request is None:
            _params = {}
            if gateway_arn is not ShapeBase.NOT_SET:
                _params['gateway_arn'] = gateway_arn
            if password is not ShapeBase.NOT_SET:
                _params['password'] = password
            _request = shapes.SetSMBGuestPasswordInput(**_params)
        response = self._boto_client.set_smb_guest_password(
            **_request.to_boto()
        )

        return shapes.SetSMBGuestPasswordOutput.from_boto(response)

    def shutdown_gateway(
        self,
        _request: shapes.ShutdownGatewayInput = None,
        *,
        gateway_arn: str,
    ) -> shapes.ShutdownGatewayOutput:
        """
        Shuts down a gateway. To specify which gateway to shut down, use the Amazon
        Resource Name (ARN) of the gateway in the body of your request.

        The operation shuts down the gateway service component running in the gateway's
        virtual machine (VM) and not the host VM.

        If you want to shut down the VM, it is recommended that you first shut down the
        gateway component in the VM to avoid unpredictable conditions.

        After the gateway is shutdown, you cannot call any other API except
        StartGateway, DescribeGatewayInformation, and ListGateways. For more
        information, see ActivateGateway. Your applications cannot read from or write to
        the gateway's storage volumes, and there are no snapshots taken.

        When you make a shutdown request, you will get a `200 OK` success response
        immediately. However, it might take some time for the gateway to shut down. You
        can call the DescribeGatewayInformation API to check the status. For more
        information, see ActivateGateway.

        If do not intend to use the gateway again, you must delete the gateway (using
        DeleteGateway) to no longer pay software charges associated with the gateway.
        """
        if _request is None:
            _params = {}
            if gateway_arn is not ShapeBase.NOT_SET:
                _params['gateway_arn'] = gateway_arn
            _request = shapes.ShutdownGatewayInput(**_params)
        response = self._boto_client.shutdown_gateway(**_request.to_boto())

        return shapes.ShutdownGatewayOutput.from_boto(response)

    def start_gateway(
        self,
        _request: shapes.StartGatewayInput = None,
        *,
        gateway_arn: str,
    ) -> shapes.StartGatewayOutput:
        """
        Starts a gateway that you previously shut down (see ShutdownGateway). After the
        gateway starts, you can then make other API calls, your applications can read
        from or write to the gateway's storage volumes and you will be able to take
        snapshot backups.

        When you make a request, you will get a 200 OK success response immediately.
        However, it might take some time for the gateway to be ready. You should call
        DescribeGatewayInformation and check the status before making any additional API
        calls. For more information, see ActivateGateway.

        To specify which gateway to start, use the Amazon Resource Name (ARN) of the
        gateway in your request.
        """
        if _request is None:
            _params = {}
            if gateway_arn is not ShapeBase.NOT_SET:
                _params['gateway_arn'] = gateway_arn
            _request = shapes.StartGatewayInput(**_params)
        response = self._boto_client.start_gateway(**_request.to_boto())

        return shapes.StartGatewayOutput.from_boto(response)

    def update_bandwidth_rate_limit(
        self,
        _request: shapes.UpdateBandwidthRateLimitInput = None,
        *,
        gateway_arn: str,
        average_upload_rate_limit_in_bits_per_sec: int = ShapeBase.NOT_SET,
        average_download_rate_limit_in_bits_per_sec: int = ShapeBase.NOT_SET,
    ) -> shapes.UpdateBandwidthRateLimitOutput:
        """
        Updates the bandwidth rate limits of a gateway. You can update both the upload
        and download bandwidth rate limit or specify only one of the two. If you don't
        set a bandwidth rate limit, the existing rate limit remains.

        By default, a gateway's bandwidth rate limits are not set. If you don't set any
        limit, the gateway does not have any limitations on its bandwidth usage and
        could potentially use the maximum available bandwidth.

        To specify which gateway to update, use the Amazon Resource Name (ARN) of the
        gateway in your request.
        """
        if _request is None:
            _params = {}
            if gateway_arn is not ShapeBase.NOT_SET:
                _params['gateway_arn'] = gateway_arn
            if average_upload_rate_limit_in_bits_per_sec is not ShapeBase.NOT_SET:
                _params['average_upload_rate_limit_in_bits_per_sec'
                       ] = average_upload_rate_limit_in_bits_per_sec
            if average_download_rate_limit_in_bits_per_sec is not ShapeBase.NOT_SET:
                _params['average_download_rate_limit_in_bits_per_sec'
                       ] = average_download_rate_limit_in_bits_per_sec
            _request = shapes.UpdateBandwidthRateLimitInput(**_params)
        response = self._boto_client.update_bandwidth_rate_limit(
            **_request.to_boto()
        )

        return shapes.UpdateBandwidthRateLimitOutput.from_boto(response)

    def update_chap_credentials(
        self,
        _request: shapes.UpdateChapCredentialsInput = None,
        *,
        target_arn: str,
        secret_to_authenticate_initiator: str,
        initiator_name: str,
        secret_to_authenticate_target: str = ShapeBase.NOT_SET,
    ) -> shapes.UpdateChapCredentialsOutput:
        """
        Updates the Challenge-Handshake Authentication Protocol (CHAP) credentials for a
        specified iSCSI target. By default, a gateway does not have CHAP enabled;
        however, for added security, you might use it.

        When you update CHAP credentials, all existing connections on the target are
        closed and initiators must reconnect with the new credentials.
        """
        if _request is None:
            _params = {}
            if target_arn is not ShapeBase.NOT_SET:
                _params['target_arn'] = target_arn
            if secret_to_authenticate_initiator is not ShapeBase.NOT_SET:
                _params['secret_to_authenticate_initiator'
                       ] = secret_to_authenticate_initiator
            if initiator_name is not ShapeBase.NOT_SET:
                _params['initiator_name'] = initiator_name
            if secret_to_authenticate_target is not ShapeBase.NOT_SET:
                _params['secret_to_authenticate_target'
                       ] = secret_to_authenticate_target
            _request = shapes.UpdateChapCredentialsInput(**_params)
        response = self._boto_client.update_chap_credentials(
            **_request.to_boto()
        )

        return shapes.UpdateChapCredentialsOutput.from_boto(response)

    def update_gateway_information(
        self,
        _request: shapes.UpdateGatewayInformationInput = None,
        *,
        gateway_arn: str,
        gateway_name: str = ShapeBase.NOT_SET,
        gateway_timezone: str = ShapeBase.NOT_SET,
    ) -> shapes.UpdateGatewayInformationOutput:
        """
        Updates a gateway's metadata, which includes the gateway's name and time zone.
        To specify which gateway to update, use the Amazon Resource Name (ARN) of the
        gateway in your request.

        For Gateways activated after September 2, 2015, the gateway's ARN contains the
        gateway ID rather than the gateway name. However, changing the name of the
        gateway has no effect on the gateway's ARN.
        """
        if _request is None:
            _params = {}
            if gateway_arn is not ShapeBase.NOT_SET:
                _params['gateway_arn'] = gateway_arn
            if gateway_name is not ShapeBase.NOT_SET:
                _params['gateway_name'] = gateway_name
            if gateway_timezone is not ShapeBase.NOT_SET:
                _params['gateway_timezone'] = gateway_timezone
            _request = shapes.UpdateGatewayInformationInput(**_params)
        response = self._boto_client.update_gateway_information(
            **_request.to_boto()
        )

        return shapes.UpdateGatewayInformationOutput.from_boto(response)

    def update_gateway_software_now(
        self,
        _request: shapes.UpdateGatewaySoftwareNowInput = None,
        *,
        gateway_arn: str,
    ) -> shapes.UpdateGatewaySoftwareNowOutput:
        """
        Updates the gateway virtual machine (VM) software. The request immediately
        triggers the software update.

        When you make this request, you get a `200 OK` success response immediately.
        However, it might take some time for the update to complete. You can call
        DescribeGatewayInformation to verify the gateway is in the `STATE_RUNNING`
        state.

        A software update forces a system restart of your gateway. You can minimize the
        chance of any disruption to your applications by increasing your iSCSI
        Initiators' timeouts. For more information about increasing iSCSI Initiator
        timeouts for Windows and Linux, see [Customizing Your Windows iSCSI
        Settings](http://docs.aws.amazon.com/storagegateway/latest/userguide/ConfiguringiSCSIClientInitiatorWindowsClient.html#CustomizeWindowsiSCSISettings)
        and [Customizing Your Linux iSCSI
        Settings](http://docs.aws.amazon.com/storagegateway/latest/userguide/ConfiguringiSCSIClientInitiatorRedHatClient.html#CustomizeLinuxiSCSISettings),
        respectively.
        """
        if _request is None:
            _params = {}
            if gateway_arn is not ShapeBase.NOT_SET:
                _params['gateway_arn'] = gateway_arn
            _request = shapes.UpdateGatewaySoftwareNowInput(**_params)
        response = self._boto_client.update_gateway_software_now(
            **_request.to_boto()
        )

        return shapes.UpdateGatewaySoftwareNowOutput.from_boto(response)

    def update_maintenance_start_time(
        self,
        _request: shapes.UpdateMaintenanceStartTimeInput = None,
        *,
        gateway_arn: str,
        hour_of_day: int,
        minute_of_hour: int,
        day_of_week: int,
    ) -> shapes.UpdateMaintenanceStartTimeOutput:
        """
        Updates a gateway's weekly maintenance start time information, including day and
        time of the week. The maintenance time is the time in your gateway's time zone.
        """
        if _request is None:
            _params = {}
            if gateway_arn is not ShapeBase.NOT_SET:
                _params['gateway_arn'] = gateway_arn
            if hour_of_day is not ShapeBase.NOT_SET:
                _params['hour_of_day'] = hour_of_day
            if minute_of_hour is not ShapeBase.NOT_SET:
                _params['minute_of_hour'] = minute_of_hour
            if day_of_week is not ShapeBase.NOT_SET:
                _params['day_of_week'] = day_of_week
            _request = shapes.UpdateMaintenanceStartTimeInput(**_params)
        response = self._boto_client.update_maintenance_start_time(
            **_request.to_boto()
        )

        return shapes.UpdateMaintenanceStartTimeOutput.from_boto(response)

    def update_nfs_file_share(
        self,
        _request: shapes.UpdateNFSFileShareInput = None,
        *,
        file_share_arn: str,
        kms_encrypted: bool = ShapeBase.NOT_SET,
        kms_key: str = ShapeBase.NOT_SET,
        nfs_file_share_defaults: shapes.NFSFileShareDefaults = ShapeBase.
        NOT_SET,
        default_storage_class: str = ShapeBase.NOT_SET,
        object_acl: typing.Union[str, shapes.ObjectACL] = ShapeBase.NOT_SET,
        client_list: typing.List[str] = ShapeBase.NOT_SET,
        squash: str = ShapeBase.NOT_SET,
        read_only: bool = ShapeBase.NOT_SET,
        guess_mime_type_enabled: bool = ShapeBase.NOT_SET,
        requester_pays: bool = ShapeBase.NOT_SET,
    ) -> shapes.UpdateNFSFileShareOutput:
        """
        Updates a Network File System (NFS) file share. This operation is only supported
        in the file gateway type.

        To leave a file share field unchanged, set the corresponding input field to
        null.

        Updates the following file share setting:

          * Default storage class for your S3 bucket

          * Metadata defaults for your S3 bucket

          * Allowed NFS clients for your file share

          * Squash settings

          * Write status of your file share

        To leave a file share field unchanged, set the corresponding input field to
        null. This operation is only supported in file gateways.
        """
        if _request is None:
            _params = {}
            if file_share_arn is not ShapeBase.NOT_SET:
                _params['file_share_arn'] = file_share_arn
            if kms_encrypted is not ShapeBase.NOT_SET:
                _params['kms_encrypted'] = kms_encrypted
            if kms_key is not ShapeBase.NOT_SET:
                _params['kms_key'] = kms_key
            if nfs_file_share_defaults is not ShapeBase.NOT_SET:
                _params['nfs_file_share_defaults'] = nfs_file_share_defaults
            if default_storage_class is not ShapeBase.NOT_SET:
                _params['default_storage_class'] = default_storage_class
            if object_acl is not ShapeBase.NOT_SET:
                _params['object_acl'] = object_acl
            if client_list is not ShapeBase.NOT_SET:
                _params['client_list'] = client_list
            if squash is not ShapeBase.NOT_SET:
                _params['squash'] = squash
            if read_only is not ShapeBase.NOT_SET:
                _params['read_only'] = read_only
            if guess_mime_type_enabled is not ShapeBase.NOT_SET:
                _params['guess_mime_type_enabled'] = guess_mime_type_enabled
            if requester_pays is not ShapeBase.NOT_SET:
                _params['requester_pays'] = requester_pays
            _request = shapes.UpdateNFSFileShareInput(**_params)
        response = self._boto_client.update_nfs_file_share(**_request.to_boto())

        return shapes.UpdateNFSFileShareOutput.from_boto(response)

    def update_smb_file_share(
        self,
        _request: shapes.UpdateSMBFileShareInput = None,
        *,
        file_share_arn: str,
        kms_encrypted: bool = ShapeBase.NOT_SET,
        kms_key: str = ShapeBase.NOT_SET,
        default_storage_class: str = ShapeBase.NOT_SET,
        object_acl: typing.Union[str, shapes.ObjectACL] = ShapeBase.NOT_SET,
        read_only: bool = ShapeBase.NOT_SET,
        guess_mime_type_enabled: bool = ShapeBase.NOT_SET,
        requester_pays: bool = ShapeBase.NOT_SET,
        valid_user_list: typing.List[str] = ShapeBase.NOT_SET,
        invalid_user_list: typing.List[str] = ShapeBase.NOT_SET,
    ) -> shapes.UpdateSMBFileShareOutput:
        """
        Updates a Server Message Block (SMB) file share.

        To leave a file share field unchanged, set the corresponding input field to
        null. This operation is only supported for file gateways.

        File gateways require AWS Security Token Service (AWS STS) to be activated to
        enable you to create a file share. Make sure that AWS STS is activated in the
        AWS Region you are creating your file gateway in. If AWS STS is not activated in
        this AWS Region, activate it. For information about how to activate AWS STS, see
        [Activating and Deactivating AWS STS in an AWS
        Region](http://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_enable-
        regions.html) in the _AWS Identity and Access Management User Guide._

        File gateways don't support creating hard or symbolic links on a file share.
        """
        if _request is None:
            _params = {}
            if file_share_arn is not ShapeBase.NOT_SET:
                _params['file_share_arn'] = file_share_arn
            if kms_encrypted is not ShapeBase.NOT_SET:
                _params['kms_encrypted'] = kms_encrypted
            if kms_key is not ShapeBase.NOT_SET:
                _params['kms_key'] = kms_key
            if default_storage_class is not ShapeBase.NOT_SET:
                _params['default_storage_class'] = default_storage_class
            if object_acl is not ShapeBase.NOT_SET:
                _params['object_acl'] = object_acl
            if read_only is not ShapeBase.NOT_SET:
                _params['read_only'] = read_only
            if guess_mime_type_enabled is not ShapeBase.NOT_SET:
                _params['guess_mime_type_enabled'] = guess_mime_type_enabled
            if requester_pays is not ShapeBase.NOT_SET:
                _params['requester_pays'] = requester_pays
            if valid_user_list is not ShapeBase.NOT_SET:
                _params['valid_user_list'] = valid_user_list
            if invalid_user_list is not ShapeBase.NOT_SET:
                _params['invalid_user_list'] = invalid_user_list
            _request = shapes.UpdateSMBFileShareInput(**_params)
        response = self._boto_client.update_smb_file_share(**_request.to_boto())

        return shapes.UpdateSMBFileShareOutput.from_boto(response)

    def update_snapshot_schedule(
        self,
        _request: shapes.UpdateSnapshotScheduleInput = None,
        *,
        volume_arn: str,
        start_at: int,
        recurrence_in_hours: int,
        description: str = ShapeBase.NOT_SET,
    ) -> shapes.UpdateSnapshotScheduleOutput:
        """
        Updates a snapshot schedule configured for a gateway volume. This operation is
        only supported in the cached volume and stored volume gateway types.

        The default snapshot schedule for volume is once every 24 hours, starting at the
        creation time of the volume. You can use this API to change the snapshot
        schedule configured for the volume.

        In the request you must identify the gateway volume whose snapshot schedule you
        want to update, and the schedule information, including when you want the
        snapshot to begin on a day and the frequency (in hours) of snapshots.
        """
        if _request is None:
            _params = {}
            if volume_arn is not ShapeBase.NOT_SET:
                _params['volume_arn'] = volume_arn
            if start_at is not ShapeBase.NOT_SET:
                _params['start_at'] = start_at
            if recurrence_in_hours is not ShapeBase.NOT_SET:
                _params['recurrence_in_hours'] = recurrence_in_hours
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            _request = shapes.UpdateSnapshotScheduleInput(**_params)
        response = self._boto_client.update_snapshot_schedule(
            **_request.to_boto()
        )

        return shapes.UpdateSnapshotScheduleOutput.from_boto(response)

    def update_vtl_device_type(
        self,
        _request: shapes.UpdateVTLDeviceTypeInput = None,
        *,
        vtl_device_arn: str,
        device_type: str,
    ) -> shapes.UpdateVTLDeviceTypeOutput:
        """
        Updates the type of medium changer in a tape gateway. When you activate a tape
        gateway, you select a medium changer type for the tape gateway. This operation
        enables you to select a different type of medium changer after a tape gateway is
        activated. This operation is only supported in the tape gateway type.
        """
        if _request is None:
            _params = {}
            if vtl_device_arn is not ShapeBase.NOT_SET:
                _params['vtl_device_arn'] = vtl_device_arn
            if device_type is not ShapeBase.NOT_SET:
                _params['device_type'] = device_type
            _request = shapes.UpdateVTLDeviceTypeInput(**_params)
        response = self._boto_client.update_vtl_device_type(
            **_request.to_boto()
        )

        return shapes.UpdateVTLDeviceTypeOutput.from_boto(response)
