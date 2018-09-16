import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("ssm", *args, **kwargs)

    def add_tags_to_resource(
        self,
        _request: shapes.AddTagsToResourceRequest = None,
        *,
        resource_type: typing.Union[str, shapes.ResourceTypeForTagging],
        resource_id: str,
        tags: typing.List[shapes.Tag],
    ) -> shapes.AddTagsToResourceResult:
        """
        Adds or overwrites one or more tags for the specified resource. Tags are
        metadata that you can assign to your documents, managed instances, Maintenance
        Windows, Parameter Store parameters, and patch baselines. Tags enable you to
        categorize your resources in different ways, for example, by purpose, owner, or
        environment. Each tag consists of a key and an optional value, both of which you
        define. For example, you could define a set of tags for your account's managed
        instances that helps you track each instance's owner and stack level. For
        example: Key=Owner and Value=DbAdmin, SysAdmin, or Dev. Or Key=Stack and
        Value=Production, Pre-Production, or Test.

        Each resource can have a maximum of 50 tags.

        We recommend that you devise a set of tag keys that meets your needs for each
        resource type. Using a consistent set of tag keys makes it easier for you to
        manage your resources. You can search and filter the resources based on the tags
        you add. Tags don't have any semantic meaning to Amazon EC2 and are interpreted
        strictly as a string of characters.

        For more information about tags, see [Tagging Your Amazon EC2
        Resources](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html)
        in the _Amazon EC2 User Guide_.
        """
        if _request is None:
            _params = {}
            if resource_type is not ShapeBase.NOT_SET:
                _params['resource_type'] = resource_type
            if resource_id is not ShapeBase.NOT_SET:
                _params['resource_id'] = resource_id
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            _request = shapes.AddTagsToResourceRequest(**_params)
        response = self._boto_client.add_tags_to_resource(**_request.to_boto())

        return shapes.AddTagsToResourceResult.from_boto(response)

    def cancel_command(
        self,
        _request: shapes.CancelCommandRequest = None,
        *,
        command_id: str,
        instance_ids: typing.List[str] = ShapeBase.NOT_SET,
    ) -> shapes.CancelCommandResult:
        """
        Attempts to cancel the command specified by the Command ID. There is no
        guarantee that the command will be terminated and the underlying process
        stopped.
        """
        if _request is None:
            _params = {}
            if command_id is not ShapeBase.NOT_SET:
                _params['command_id'] = command_id
            if instance_ids is not ShapeBase.NOT_SET:
                _params['instance_ids'] = instance_ids
            _request = shapes.CancelCommandRequest(**_params)
        response = self._boto_client.cancel_command(**_request.to_boto())

        return shapes.CancelCommandResult.from_boto(response)

    def create_activation(
        self,
        _request: shapes.CreateActivationRequest = None,
        *,
        iam_role: str,
        description: str = ShapeBase.NOT_SET,
        default_instance_name: str = ShapeBase.NOT_SET,
        registration_limit: int = ShapeBase.NOT_SET,
        expiration_date: datetime.datetime = ShapeBase.NOT_SET,
    ) -> shapes.CreateActivationResult:
        """
        Registers your on-premises server or virtual machine with Amazon EC2 so that you
        can manage these resources using Run Command. An on-premises server or virtual
        machine that has been registered with EC2 is called a managed instance. For more
        information about activations, see [Setting Up Systems Manager in Hybrid
        Environments](http://docs.aws.amazon.com/systems-
        manager/latest/userguide/systems-manager-managedinstances.html).
        """
        if _request is None:
            _params = {}
            if iam_role is not ShapeBase.NOT_SET:
                _params['iam_role'] = iam_role
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if default_instance_name is not ShapeBase.NOT_SET:
                _params['default_instance_name'] = default_instance_name
            if registration_limit is not ShapeBase.NOT_SET:
                _params['registration_limit'] = registration_limit
            if expiration_date is not ShapeBase.NOT_SET:
                _params['expiration_date'] = expiration_date
            _request = shapes.CreateActivationRequest(**_params)
        response = self._boto_client.create_activation(**_request.to_boto())

        return shapes.CreateActivationResult.from_boto(response)

    def create_association(
        self,
        _request: shapes.CreateAssociationRequest = None,
        *,
        name: str,
        document_version: str = ShapeBase.NOT_SET,
        instance_id: str = ShapeBase.NOT_SET,
        parameters: typing.Dict[str, typing.List[str]] = ShapeBase.NOT_SET,
        targets: typing.List[shapes.Target] = ShapeBase.NOT_SET,
        schedule_expression: str = ShapeBase.NOT_SET,
        output_location: shapes.InstanceAssociationOutputLocation = ShapeBase.
        NOT_SET,
        association_name: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateAssociationResult:
        """
        Associates the specified Systems Manager document with the specified instances
        or targets.

        When you associate a document with one or more instances using instance IDs or
        tags, SSM Agent running on the instance processes the document and configures
        the instance as specified.

        If you associate a document with an instance that already has an associated
        document, the system throws the AssociationAlreadyExists exception.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if document_version is not ShapeBase.NOT_SET:
                _params['document_version'] = document_version
            if instance_id is not ShapeBase.NOT_SET:
                _params['instance_id'] = instance_id
            if parameters is not ShapeBase.NOT_SET:
                _params['parameters'] = parameters
            if targets is not ShapeBase.NOT_SET:
                _params['targets'] = targets
            if schedule_expression is not ShapeBase.NOT_SET:
                _params['schedule_expression'] = schedule_expression
            if output_location is not ShapeBase.NOT_SET:
                _params['output_location'] = output_location
            if association_name is not ShapeBase.NOT_SET:
                _params['association_name'] = association_name
            _request = shapes.CreateAssociationRequest(**_params)
        response = self._boto_client.create_association(**_request.to_boto())

        return shapes.CreateAssociationResult.from_boto(response)

    def create_association_batch(
        self,
        _request: shapes.CreateAssociationBatchRequest = None,
        *,
        entries: typing.List[shapes.CreateAssociationBatchRequestEntry],
    ) -> shapes.CreateAssociationBatchResult:
        """
        Associates the specified Systems Manager document with the specified instances
        or targets.

        When you associate a document with one or more instances using instance IDs or
        tags, SSM Agent running on the instance processes the document and configures
        the instance as specified.

        If you associate a document with an instance that already has an associated
        document, the system throws the AssociationAlreadyExists exception.
        """
        if _request is None:
            _params = {}
            if entries is not ShapeBase.NOT_SET:
                _params['entries'] = entries
            _request = shapes.CreateAssociationBatchRequest(**_params)
        response = self._boto_client.create_association_batch(
            **_request.to_boto()
        )

        return shapes.CreateAssociationBatchResult.from_boto(response)

    def create_document(
        self,
        _request: shapes.CreateDocumentRequest = None,
        *,
        content: str,
        name: str,
        document_type: typing.Union[str, shapes.
                                    DocumentType] = ShapeBase.NOT_SET,
        document_format: typing.Union[str, shapes.DocumentFormat] = ShapeBase.
        NOT_SET,
        target_type: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateDocumentResult:
        """
        Creates a Systems Manager document.

        After you create a document, you can use CreateAssociation to associate it with
        one or more running instances.
        """
        if _request is None:
            _params = {}
            if content is not ShapeBase.NOT_SET:
                _params['content'] = content
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if document_type is not ShapeBase.NOT_SET:
                _params['document_type'] = document_type
            if document_format is not ShapeBase.NOT_SET:
                _params['document_format'] = document_format
            if target_type is not ShapeBase.NOT_SET:
                _params['target_type'] = target_type
            _request = shapes.CreateDocumentRequest(**_params)
        response = self._boto_client.create_document(**_request.to_boto())

        return shapes.CreateDocumentResult.from_boto(response)

    def create_maintenance_window(
        self,
        _request: shapes.CreateMaintenanceWindowRequest = None,
        *,
        name: str,
        schedule: str,
        duration: int,
        cutoff: int,
        allow_unassociated_targets: bool,
        description: str = ShapeBase.NOT_SET,
        client_token: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateMaintenanceWindowResult:
        """
        Creates a new Maintenance Window.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if schedule is not ShapeBase.NOT_SET:
                _params['schedule'] = schedule
            if duration is not ShapeBase.NOT_SET:
                _params['duration'] = duration
            if cutoff is not ShapeBase.NOT_SET:
                _params['cutoff'] = cutoff
            if allow_unassociated_targets is not ShapeBase.NOT_SET:
                _params['allow_unassociated_targets'
                       ] = allow_unassociated_targets
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if client_token is not ShapeBase.NOT_SET:
                _params['client_token'] = client_token
            _request = shapes.CreateMaintenanceWindowRequest(**_params)
        response = self._boto_client.create_maintenance_window(
            **_request.to_boto()
        )

        return shapes.CreateMaintenanceWindowResult.from_boto(response)

    def create_patch_baseline(
        self,
        _request: shapes.CreatePatchBaselineRequest = None,
        *,
        name: str,
        operating_system: typing.Union[str, shapes.
                                       OperatingSystem] = ShapeBase.NOT_SET,
        global_filters: shapes.PatchFilterGroup = ShapeBase.NOT_SET,
        approval_rules: shapes.PatchRuleGroup = ShapeBase.NOT_SET,
        approved_patches: typing.List[str] = ShapeBase.NOT_SET,
        approved_patches_compliance_level: typing.
        Union[str, shapes.PatchComplianceLevel] = ShapeBase.NOT_SET,
        approved_patches_enable_non_security: bool = ShapeBase.NOT_SET,
        rejected_patches: typing.List[str] = ShapeBase.NOT_SET,
        description: str = ShapeBase.NOT_SET,
        sources: typing.List[shapes.PatchSource] = ShapeBase.NOT_SET,
        client_token: str = ShapeBase.NOT_SET,
    ) -> shapes.CreatePatchBaselineResult:
        """
        Creates a patch baseline.

        For information about valid key and value pairs in `PatchFilters` for each
        supported operating system type, see
        [PatchFilter](http://docs.aws.amazon.com/systems-
        manager/latest/APIReference/API_PatchFilter.html).
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if operating_system is not ShapeBase.NOT_SET:
                _params['operating_system'] = operating_system
            if global_filters is not ShapeBase.NOT_SET:
                _params['global_filters'] = global_filters
            if approval_rules is not ShapeBase.NOT_SET:
                _params['approval_rules'] = approval_rules
            if approved_patches is not ShapeBase.NOT_SET:
                _params['approved_patches'] = approved_patches
            if approved_patches_compliance_level is not ShapeBase.NOT_SET:
                _params['approved_patches_compliance_level'
                       ] = approved_patches_compliance_level
            if approved_patches_enable_non_security is not ShapeBase.NOT_SET:
                _params['approved_patches_enable_non_security'
                       ] = approved_patches_enable_non_security
            if rejected_patches is not ShapeBase.NOT_SET:
                _params['rejected_patches'] = rejected_patches
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if sources is not ShapeBase.NOT_SET:
                _params['sources'] = sources
            if client_token is not ShapeBase.NOT_SET:
                _params['client_token'] = client_token
            _request = shapes.CreatePatchBaselineRequest(**_params)
        response = self._boto_client.create_patch_baseline(**_request.to_boto())

        return shapes.CreatePatchBaselineResult.from_boto(response)

    def create_resource_data_sync(
        self,
        _request: shapes.CreateResourceDataSyncRequest = None,
        *,
        sync_name: str,
        s3_destination: shapes.ResourceDataSyncS3Destination,
    ) -> shapes.CreateResourceDataSyncResult:
        """
        Creates a resource data sync configuration to a single bucket in Amazon S3. This
        is an asynchronous operation that returns immediately. After a successful
        initial sync is completed, the system continuously syncs data to the Amazon S3
        bucket. To check the status of the sync, use the ListResourceDataSync.

        By default, data is not encrypted in Amazon S3. We strongly recommend that you
        enable encryption in Amazon S3 to ensure secure data storage. We also recommend
        that you secure access to the Amazon S3 bucket by creating a restrictive bucket
        policy. To view an example of a restrictive Amazon S3 bucket policy for Resource
        Data Sync, see [Create a Resource Data Sync for
        Inventory](http://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-
        inventory-datasync-create.html) in the _AWS Systems Manager User Guide_.
        """
        if _request is None:
            _params = {}
            if sync_name is not ShapeBase.NOT_SET:
                _params['sync_name'] = sync_name
            if s3_destination is not ShapeBase.NOT_SET:
                _params['s3_destination'] = s3_destination
            _request = shapes.CreateResourceDataSyncRequest(**_params)
        response = self._boto_client.create_resource_data_sync(
            **_request.to_boto()
        )

        return shapes.CreateResourceDataSyncResult.from_boto(response)

    def delete_activation(
        self,
        _request: shapes.DeleteActivationRequest = None,
        *,
        activation_id: str,
    ) -> shapes.DeleteActivationResult:
        """
        Deletes an activation. You are not required to delete an activation. If you
        delete an activation, you can no longer use it to register additional managed
        instances. Deleting an activation does not de-register managed instances. You
        must manually de-register managed instances.
        """
        if _request is None:
            _params = {}
            if activation_id is not ShapeBase.NOT_SET:
                _params['activation_id'] = activation_id
            _request = shapes.DeleteActivationRequest(**_params)
        response = self._boto_client.delete_activation(**_request.to_boto())

        return shapes.DeleteActivationResult.from_boto(response)

    def delete_association(
        self,
        _request: shapes.DeleteAssociationRequest = None,
        *,
        name: str = ShapeBase.NOT_SET,
        instance_id: str = ShapeBase.NOT_SET,
        association_id: str = ShapeBase.NOT_SET,
    ) -> shapes.DeleteAssociationResult:
        """
        Disassociates the specified Systems Manager document from the specified
        instance.

        When you disassociate a document from an instance, it does not change the
        configuration of the instance. To change the configuration state of an instance
        after you disassociate a document, you must create a new document with the
        desired configuration and associate it with the instance.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if instance_id is not ShapeBase.NOT_SET:
                _params['instance_id'] = instance_id
            if association_id is not ShapeBase.NOT_SET:
                _params['association_id'] = association_id
            _request = shapes.DeleteAssociationRequest(**_params)
        response = self._boto_client.delete_association(**_request.to_boto())

        return shapes.DeleteAssociationResult.from_boto(response)

    def delete_document(
        self,
        _request: shapes.DeleteDocumentRequest = None,
        *,
        name: str,
    ) -> shapes.DeleteDocumentResult:
        """
        Deletes the Systems Manager document and all instance associations to the
        document.

        Before you delete the document, we recommend that you use DeleteAssociation to
        disassociate all instances that are associated with the document.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            _request = shapes.DeleteDocumentRequest(**_params)
        response = self._boto_client.delete_document(**_request.to_boto())

        return shapes.DeleteDocumentResult.from_boto(response)

    def delete_inventory(
        self,
        _request: shapes.DeleteInventoryRequest = None,
        *,
        type_name: str,
        schema_delete_option: typing.
        Union[str, shapes.InventorySchemaDeleteOption] = ShapeBase.NOT_SET,
        dry_run: bool = ShapeBase.NOT_SET,
        client_token: str = ShapeBase.NOT_SET,
    ) -> shapes.DeleteInventoryResult:
        """
        Delete a custom inventory type, or the data associated with a custom Inventory
        type. Deleting a custom inventory type is also referred to as deleting a custom
        inventory schema.
        """
        if _request is None:
            _params = {}
            if type_name is not ShapeBase.NOT_SET:
                _params['type_name'] = type_name
            if schema_delete_option is not ShapeBase.NOT_SET:
                _params['schema_delete_option'] = schema_delete_option
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            if client_token is not ShapeBase.NOT_SET:
                _params['client_token'] = client_token
            _request = shapes.DeleteInventoryRequest(**_params)
        response = self._boto_client.delete_inventory(**_request.to_boto())

        return shapes.DeleteInventoryResult.from_boto(response)

    def delete_maintenance_window(
        self,
        _request: shapes.DeleteMaintenanceWindowRequest = None,
        *,
        window_id: str,
    ) -> shapes.DeleteMaintenanceWindowResult:
        """
        Deletes a Maintenance Window.
        """
        if _request is None:
            _params = {}
            if window_id is not ShapeBase.NOT_SET:
                _params['window_id'] = window_id
            _request = shapes.DeleteMaintenanceWindowRequest(**_params)
        response = self._boto_client.delete_maintenance_window(
            **_request.to_boto()
        )

        return shapes.DeleteMaintenanceWindowResult.from_boto(response)

    def delete_parameter(
        self,
        _request: shapes.DeleteParameterRequest = None,
        *,
        name: str,
    ) -> shapes.DeleteParameterResult:
        """
        Delete a parameter from the system.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            _request = shapes.DeleteParameterRequest(**_params)
        response = self._boto_client.delete_parameter(**_request.to_boto())

        return shapes.DeleteParameterResult.from_boto(response)

    def delete_parameters(
        self,
        _request: shapes.DeleteParametersRequest = None,
        *,
        names: typing.List[str],
    ) -> shapes.DeleteParametersResult:
        """
        Delete a list of parameters. This API is used to delete parameters by using the
        Amazon EC2 console.
        """
        if _request is None:
            _params = {}
            if names is not ShapeBase.NOT_SET:
                _params['names'] = names
            _request = shapes.DeleteParametersRequest(**_params)
        response = self._boto_client.delete_parameters(**_request.to_boto())

        return shapes.DeleteParametersResult.from_boto(response)

    def delete_patch_baseline(
        self,
        _request: shapes.DeletePatchBaselineRequest = None,
        *,
        baseline_id: str,
    ) -> shapes.DeletePatchBaselineResult:
        """
        Deletes a patch baseline.
        """
        if _request is None:
            _params = {}
            if baseline_id is not ShapeBase.NOT_SET:
                _params['baseline_id'] = baseline_id
            _request = shapes.DeletePatchBaselineRequest(**_params)
        response = self._boto_client.delete_patch_baseline(**_request.to_boto())

        return shapes.DeletePatchBaselineResult.from_boto(response)

    def delete_resource_data_sync(
        self,
        _request: shapes.DeleteResourceDataSyncRequest = None,
        *,
        sync_name: str,
    ) -> shapes.DeleteResourceDataSyncResult:
        """
        Deletes a Resource Data Sync configuration. After the configuration is deleted,
        changes to inventory data on managed instances are no longer synced with the
        target Amazon S3 bucket. Deleting a sync configuration does not delete data in
        the target Amazon S3 bucket.
        """
        if _request is None:
            _params = {}
            if sync_name is not ShapeBase.NOT_SET:
                _params['sync_name'] = sync_name
            _request = shapes.DeleteResourceDataSyncRequest(**_params)
        response = self._boto_client.delete_resource_data_sync(
            **_request.to_boto()
        )

        return shapes.DeleteResourceDataSyncResult.from_boto(response)

    def deregister_managed_instance(
        self,
        _request: shapes.DeregisterManagedInstanceRequest = None,
        *,
        instance_id: str,
    ) -> shapes.DeregisterManagedInstanceResult:
        """
        Removes the server or virtual machine from the list of registered servers. You
        can reregister the instance again at any time. If you don't plan to use Run
        Command on the server, we suggest uninstalling SSM Agent first.
        """
        if _request is None:
            _params = {}
            if instance_id is not ShapeBase.NOT_SET:
                _params['instance_id'] = instance_id
            _request = shapes.DeregisterManagedInstanceRequest(**_params)
        response = self._boto_client.deregister_managed_instance(
            **_request.to_boto()
        )

        return shapes.DeregisterManagedInstanceResult.from_boto(response)

    def deregister_patch_baseline_for_patch_group(
        self,
        _request: shapes.DeregisterPatchBaselineForPatchGroupRequest = None,
        *,
        baseline_id: str,
        patch_group: str,
    ) -> shapes.DeregisterPatchBaselineForPatchGroupResult:
        """
        Removes a patch group from a patch baseline.
        """
        if _request is None:
            _params = {}
            if baseline_id is not ShapeBase.NOT_SET:
                _params['baseline_id'] = baseline_id
            if patch_group is not ShapeBase.NOT_SET:
                _params['patch_group'] = patch_group
            _request = shapes.DeregisterPatchBaselineForPatchGroupRequest(
                **_params
            )
        response = self._boto_client.deregister_patch_baseline_for_patch_group(
            **_request.to_boto()
        )

        return shapes.DeregisterPatchBaselineForPatchGroupResult.from_boto(
            response
        )

    def deregister_target_from_maintenance_window(
        self,
        _request: shapes.DeregisterTargetFromMaintenanceWindowRequest = None,
        *,
        window_id: str,
        window_target_id: str,
        safe: bool = ShapeBase.NOT_SET,
    ) -> shapes.DeregisterTargetFromMaintenanceWindowResult:
        """
        Removes a target from a Maintenance Window.
        """
        if _request is None:
            _params = {}
            if window_id is not ShapeBase.NOT_SET:
                _params['window_id'] = window_id
            if window_target_id is not ShapeBase.NOT_SET:
                _params['window_target_id'] = window_target_id
            if safe is not ShapeBase.NOT_SET:
                _params['safe'] = safe
            _request = shapes.DeregisterTargetFromMaintenanceWindowRequest(
                **_params
            )
        response = self._boto_client.deregister_target_from_maintenance_window(
            **_request.to_boto()
        )

        return shapes.DeregisterTargetFromMaintenanceWindowResult.from_boto(
            response
        )

    def deregister_task_from_maintenance_window(
        self,
        _request: shapes.DeregisterTaskFromMaintenanceWindowRequest = None,
        *,
        window_id: str,
        window_task_id: str,
    ) -> shapes.DeregisterTaskFromMaintenanceWindowResult:
        """
        Removes a task from a Maintenance Window.
        """
        if _request is None:
            _params = {}
            if window_id is not ShapeBase.NOT_SET:
                _params['window_id'] = window_id
            if window_task_id is not ShapeBase.NOT_SET:
                _params['window_task_id'] = window_task_id
            _request = shapes.DeregisterTaskFromMaintenanceWindowRequest(
                **_params
            )
        response = self._boto_client.deregister_task_from_maintenance_window(
            **_request.to_boto()
        )

        return shapes.DeregisterTaskFromMaintenanceWindowResult.from_boto(
            response
        )

    def describe_activations(
        self,
        _request: shapes.DescribeActivationsRequest = None,
        *,
        filters: typing.List[shapes.DescribeActivationsFilter
                            ] = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeActivationsResult:
        """
        Details about the activation, including: the date and time the activation was
        created, the expiration date, the IAM role assigned to the instances in the
        activation, and the number of instances activated by this registration.
        """
        if _request is None:
            _params = {}
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.DescribeActivationsRequest(**_params)
        paginator = self.get_paginator("describe_activations").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.DescribeActivationsResult.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.DescribeActivationsResult.from_boto(response)

    def describe_association(
        self,
        _request: shapes.DescribeAssociationRequest = None,
        *,
        name: str = ShapeBase.NOT_SET,
        instance_id: str = ShapeBase.NOT_SET,
        association_id: str = ShapeBase.NOT_SET,
        association_version: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeAssociationResult:
        """
        Describes the association for the specified target or instance. If you created
        the association by using the `Targets` parameter, then you must retrieve the
        association by using the association ID. If you created the association by
        specifying an instance ID and a Systems Manager document, then you retrieve the
        association by specifying the document name and the instance ID.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if instance_id is not ShapeBase.NOT_SET:
                _params['instance_id'] = instance_id
            if association_id is not ShapeBase.NOT_SET:
                _params['association_id'] = association_id
            if association_version is not ShapeBase.NOT_SET:
                _params['association_version'] = association_version
            _request = shapes.DescribeAssociationRequest(**_params)
        response = self._boto_client.describe_association(**_request.to_boto())

        return shapes.DescribeAssociationResult.from_boto(response)

    def describe_association_execution_targets(
        self,
        _request: shapes.DescribeAssociationExecutionTargetsRequest = None,
        *,
        association_id: str,
        execution_id: str,
        filters: typing.List[shapes.AssociationExecutionTargetsFilter
                            ] = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeAssociationExecutionTargetsResult:
        """
        Use this API action to view information about a specific execution of a specific
        association.
        """
        if _request is None:
            _params = {}
            if association_id is not ShapeBase.NOT_SET:
                _params['association_id'] = association_id
            if execution_id is not ShapeBase.NOT_SET:
                _params['execution_id'] = execution_id
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.DescribeAssociationExecutionTargetsRequest(
                **_params
            )
        response = self._boto_client.describe_association_execution_targets(
            **_request.to_boto()
        )

        return shapes.DescribeAssociationExecutionTargetsResult.from_boto(
            response
        )

    def describe_association_executions(
        self,
        _request: shapes.DescribeAssociationExecutionsRequest = None,
        *,
        association_id: str,
        filters: typing.List[shapes.AssociationExecutionFilter
                            ] = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeAssociationExecutionsResult:
        """
        Use this API action to view all executions for a specific association ID.
        """
        if _request is None:
            _params = {}
            if association_id is not ShapeBase.NOT_SET:
                _params['association_id'] = association_id
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.DescribeAssociationExecutionsRequest(**_params)
        response = self._boto_client.describe_association_executions(
            **_request.to_boto()
        )

        return shapes.DescribeAssociationExecutionsResult.from_boto(response)

    def describe_automation_executions(
        self,
        _request: shapes.DescribeAutomationExecutionsRequest = None,
        *,
        filters: typing.List[shapes.AutomationExecutionFilter
                            ] = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeAutomationExecutionsResult:
        """
        Provides details about all active and terminated Automation executions.
        """
        if _request is None:
            _params = {}
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.DescribeAutomationExecutionsRequest(**_params)
        response = self._boto_client.describe_automation_executions(
            **_request.to_boto()
        )

        return shapes.DescribeAutomationExecutionsResult.from_boto(response)

    def describe_automation_step_executions(
        self,
        _request: shapes.DescribeAutomationStepExecutionsRequest = None,
        *,
        automation_execution_id: str,
        filters: typing.List[shapes.StepExecutionFilter] = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        reverse_order: bool = ShapeBase.NOT_SET,
    ) -> shapes.DescribeAutomationStepExecutionsResult:
        """
        Information about all active and terminated step executions in an Automation
        workflow.
        """
        if _request is None:
            _params = {}
            if automation_execution_id is not ShapeBase.NOT_SET:
                _params['automation_execution_id'] = automation_execution_id
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if reverse_order is not ShapeBase.NOT_SET:
                _params['reverse_order'] = reverse_order
            _request = shapes.DescribeAutomationStepExecutionsRequest(**_params)
        response = self._boto_client.describe_automation_step_executions(
            **_request.to_boto()
        )

        return shapes.DescribeAutomationStepExecutionsResult.from_boto(response)

    def describe_available_patches(
        self,
        _request: shapes.DescribeAvailablePatchesRequest = None,
        *,
        filters: typing.List[shapes.PatchOrchestratorFilter
                            ] = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeAvailablePatchesResult:
        """
        Lists all patches that could possibly be included in a patch baseline.
        """
        if _request is None:
            _params = {}
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.DescribeAvailablePatchesRequest(**_params)
        response = self._boto_client.describe_available_patches(
            **_request.to_boto()
        )

        return shapes.DescribeAvailablePatchesResult.from_boto(response)

    def describe_document(
        self,
        _request: shapes.DescribeDocumentRequest = None,
        *,
        name: str,
        document_version: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeDocumentResult:
        """
        Describes the specified Systems Manager document.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if document_version is not ShapeBase.NOT_SET:
                _params['document_version'] = document_version
            _request = shapes.DescribeDocumentRequest(**_params)
        response = self._boto_client.describe_document(**_request.to_boto())

        return shapes.DescribeDocumentResult.from_boto(response)

    def describe_document_permission(
        self,
        _request: shapes.DescribeDocumentPermissionRequest = None,
        *,
        name: str,
        permission_type: typing.Union[str, shapes.DocumentPermissionType],
    ) -> shapes.DescribeDocumentPermissionResponse:
        """
        Describes the permissions for a Systems Manager document. If you created the
        document, you are the owner. If a document is shared, it can either be shared
        privately (by specifying a user's AWS account ID) or publicly ( _All_ ).
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if permission_type is not ShapeBase.NOT_SET:
                _params['permission_type'] = permission_type
            _request = shapes.DescribeDocumentPermissionRequest(**_params)
        response = self._boto_client.describe_document_permission(
            **_request.to_boto()
        )

        return shapes.DescribeDocumentPermissionResponse.from_boto(response)

    def describe_effective_instance_associations(
        self,
        _request: shapes.DescribeEffectiveInstanceAssociationsRequest = None,
        *,
        instance_id: str,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeEffectiveInstanceAssociationsResult:
        """
        All associations for the instance(s).
        """
        if _request is None:
            _params = {}
            if instance_id is not ShapeBase.NOT_SET:
                _params['instance_id'] = instance_id
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.DescribeEffectiveInstanceAssociationsRequest(
                **_params
            )
        response = self._boto_client.describe_effective_instance_associations(
            **_request.to_boto()
        )

        return shapes.DescribeEffectiveInstanceAssociationsResult.from_boto(
            response
        )

    def describe_effective_patches_for_patch_baseline(
        self,
        _request: shapes.DescribeEffectivePatchesForPatchBaselineRequest = None,
        *,
        baseline_id: str,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeEffectivePatchesForPatchBaselineResult:
        """
        Retrieves the current effective patches (the patch and the approval state) for
        the specified patch baseline. Note that this API applies only to Windows patch
        baselines.
        """
        if _request is None:
            _params = {}
            if baseline_id is not ShapeBase.NOT_SET:
                _params['baseline_id'] = baseline_id
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.DescribeEffectivePatchesForPatchBaselineRequest(
                **_params
            )
        response = self._boto_client.describe_effective_patches_for_patch_baseline(
            **_request.to_boto()
        )

        return shapes.DescribeEffectivePatchesForPatchBaselineResult.from_boto(
            response
        )

    def describe_instance_associations_status(
        self,
        _request: shapes.DescribeInstanceAssociationsStatusRequest = None,
        *,
        instance_id: str,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeInstanceAssociationsStatusResult:
        """
        The status of the associations for the instance(s).
        """
        if _request is None:
            _params = {}
            if instance_id is not ShapeBase.NOT_SET:
                _params['instance_id'] = instance_id
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.DescribeInstanceAssociationsStatusRequest(
                **_params
            )
        response = self._boto_client.describe_instance_associations_status(
            **_request.to_boto()
        )

        return shapes.DescribeInstanceAssociationsStatusResult.from_boto(
            response
        )

    def describe_instance_information(
        self,
        _request: shapes.DescribeInstanceInformationRequest = None,
        *,
        instance_information_filter_list: typing.List[
            shapes.InstanceInformationFilter] = ShapeBase.NOT_SET,
        filters: typing.List[shapes.InstanceInformationStringFilter
                            ] = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeInstanceInformationResult:
        """
        Describes one or more of your instances. You can use this to get information
        about instances like the operating system platform, the SSM Agent version
        (Linux), status etc. If you specify one or more instance IDs, it returns
        information for those instances. If you do not specify instance IDs, it returns
        information for all your instances. If you specify an instance ID that is not
        valid or an instance that you do not own, you receive an error.

        The IamRole field for this API action is the Amazon Identity and Access
        Management (IAM) role assigned to on-premises instances. This call does not
        return the IAM role for Amazon EC2 instances.
        """
        if _request is None:
            _params = {}
            if instance_information_filter_list is not ShapeBase.NOT_SET:
                _params['instance_information_filter_list'
                       ] = instance_information_filter_list
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.DescribeInstanceInformationRequest(**_params)
        paginator = self.get_paginator("describe_instance_information"
                                      ).paginate(**_request.to_boto())
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.DescribeInstanceInformationResult.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.DescribeInstanceInformationResult.from_boto(response)

    def describe_instance_patch_states(
        self,
        _request: shapes.DescribeInstancePatchStatesRequest = None,
        *,
        instance_ids: typing.List[str],
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.DescribeInstancePatchStatesResult:
        """
        Retrieves the high-level patch state of one or more instances.
        """
        if _request is None:
            _params = {}
            if instance_ids is not ShapeBase.NOT_SET:
                _params['instance_ids'] = instance_ids
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.DescribeInstancePatchStatesRequest(**_params)
        response = self._boto_client.describe_instance_patch_states(
            **_request.to_boto()
        )

        return shapes.DescribeInstancePatchStatesResult.from_boto(response)

    def describe_instance_patch_states_for_patch_group(
        self,
        _request: shapes.DescribeInstancePatchStatesForPatchGroupRequest = None,
        *,
        patch_group: str,
        filters: typing.List[shapes.InstancePatchStateFilter
                            ] = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.DescribeInstancePatchStatesForPatchGroupResult:
        """
        Retrieves the high-level patch state for the instances in the specified patch
        group.
        """
        if _request is None:
            _params = {}
            if patch_group is not ShapeBase.NOT_SET:
                _params['patch_group'] = patch_group
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.DescribeInstancePatchStatesForPatchGroupRequest(
                **_params
            )
        response = self._boto_client.describe_instance_patch_states_for_patch_group(
            **_request.to_boto()
        )

        return shapes.DescribeInstancePatchStatesForPatchGroupResult.from_boto(
            response
        )

    def describe_instance_patches(
        self,
        _request: shapes.DescribeInstancePatchesRequest = None,
        *,
        instance_id: str,
        filters: typing.List[shapes.PatchOrchestratorFilter
                            ] = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.DescribeInstancePatchesResult:
        """
        Retrieves information about the patches on the specified instance and their
        state relative to the patch baseline being used for the instance.
        """
        if _request is None:
            _params = {}
            if instance_id is not ShapeBase.NOT_SET:
                _params['instance_id'] = instance_id
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.DescribeInstancePatchesRequest(**_params)
        response = self._boto_client.describe_instance_patches(
            **_request.to_boto()
        )

        return shapes.DescribeInstancePatchesResult.from_boto(response)

    def describe_inventory_deletions(
        self,
        _request: shapes.DescribeInventoryDeletionsRequest = None,
        *,
        deletion_id: str = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.DescribeInventoryDeletionsResult:
        """
        Describes a specific delete inventory operation.
        """
        if _request is None:
            _params = {}
            if deletion_id is not ShapeBase.NOT_SET:
                _params['deletion_id'] = deletion_id
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.DescribeInventoryDeletionsRequest(**_params)
        response = self._boto_client.describe_inventory_deletions(
            **_request.to_boto()
        )

        return shapes.DescribeInventoryDeletionsResult.from_boto(response)

    def describe_maintenance_window_execution_task_invocations(
        self,
        _request: shapes.
        DescribeMaintenanceWindowExecutionTaskInvocationsRequest = None,
        *,
        window_execution_id: str,
        task_id: str,
        filters: typing.List[shapes.MaintenanceWindowFilter
                            ] = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeMaintenanceWindowExecutionTaskInvocationsResult:
        """
        Retrieves the individual task executions (one per target) for a particular task
        executed as part of a Maintenance Window execution.
        """
        if _request is None:
            _params = {}
            if window_execution_id is not ShapeBase.NOT_SET:
                _params['window_execution_id'] = window_execution_id
            if task_id is not ShapeBase.NOT_SET:
                _params['task_id'] = task_id
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.DescribeMaintenanceWindowExecutionTaskInvocationsRequest(
                **_params
            )
        response = self._boto_client.describe_maintenance_window_execution_task_invocations(
            **_request.to_boto()
        )

        return shapes.DescribeMaintenanceWindowExecutionTaskInvocationsResult.from_boto(
            response
        )

    def describe_maintenance_window_execution_tasks(
        self,
        _request: shapes.DescribeMaintenanceWindowExecutionTasksRequest = None,
        *,
        window_execution_id: str,
        filters: typing.List[shapes.MaintenanceWindowFilter
                            ] = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeMaintenanceWindowExecutionTasksResult:
        """
        For a given Maintenance Window execution, lists the tasks that were executed.
        """
        if _request is None:
            _params = {}
            if window_execution_id is not ShapeBase.NOT_SET:
                _params['window_execution_id'] = window_execution_id
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.DescribeMaintenanceWindowExecutionTasksRequest(
                **_params
            )
        response = self._boto_client.describe_maintenance_window_execution_tasks(
            **_request.to_boto()
        )

        return shapes.DescribeMaintenanceWindowExecutionTasksResult.from_boto(
            response
        )

    def describe_maintenance_window_executions(
        self,
        _request: shapes.DescribeMaintenanceWindowExecutionsRequest = None,
        *,
        window_id: str,
        filters: typing.List[shapes.MaintenanceWindowFilter
                            ] = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeMaintenanceWindowExecutionsResult:
        """
        Lists the executions of a Maintenance Window. This includes information about
        when the Maintenance Window was scheduled to be active, and information about
        tasks registered and run with the Maintenance Window.
        """
        if _request is None:
            _params = {}
            if window_id is not ShapeBase.NOT_SET:
                _params['window_id'] = window_id
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.DescribeMaintenanceWindowExecutionsRequest(
                **_params
            )
        response = self._boto_client.describe_maintenance_window_executions(
            **_request.to_boto()
        )

        return shapes.DescribeMaintenanceWindowExecutionsResult.from_boto(
            response
        )

    def describe_maintenance_window_targets(
        self,
        _request: shapes.DescribeMaintenanceWindowTargetsRequest = None,
        *,
        window_id: str,
        filters: typing.List[shapes.MaintenanceWindowFilter
                            ] = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeMaintenanceWindowTargetsResult:
        """
        Lists the targets registered with the Maintenance Window.
        """
        if _request is None:
            _params = {}
            if window_id is not ShapeBase.NOT_SET:
                _params['window_id'] = window_id
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.DescribeMaintenanceWindowTargetsRequest(**_params)
        response = self._boto_client.describe_maintenance_window_targets(
            **_request.to_boto()
        )

        return shapes.DescribeMaintenanceWindowTargetsResult.from_boto(response)

    def describe_maintenance_window_tasks(
        self,
        _request: shapes.DescribeMaintenanceWindowTasksRequest = None,
        *,
        window_id: str,
        filters: typing.List[shapes.MaintenanceWindowFilter
                            ] = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeMaintenanceWindowTasksResult:
        """
        Lists the tasks in a Maintenance Window.
        """
        if _request is None:
            _params = {}
            if window_id is not ShapeBase.NOT_SET:
                _params['window_id'] = window_id
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.DescribeMaintenanceWindowTasksRequest(**_params)
        response = self._boto_client.describe_maintenance_window_tasks(
            **_request.to_boto()
        )

        return shapes.DescribeMaintenanceWindowTasksResult.from_boto(response)

    def describe_maintenance_windows(
        self,
        _request: shapes.DescribeMaintenanceWindowsRequest = None,
        *,
        filters: typing.List[shapes.MaintenanceWindowFilter
                            ] = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeMaintenanceWindowsResult:
        """
        Retrieves the Maintenance Windows in an AWS account.
        """
        if _request is None:
            _params = {}
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.DescribeMaintenanceWindowsRequest(**_params)
        response = self._boto_client.describe_maintenance_windows(
            **_request.to_boto()
        )

        return shapes.DescribeMaintenanceWindowsResult.from_boto(response)

    def describe_parameters(
        self,
        _request: shapes.DescribeParametersRequest = None,
        *,
        filters: typing.List[shapes.ParametersFilter] = ShapeBase.NOT_SET,
        parameter_filters: typing.List[shapes.ParameterStringFilter
                                      ] = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeParametersResult:
        """
        Get information about a parameter.

        Request results are returned on a best-effort basis. If you specify `MaxResults`
        in the request, the response includes information up to the limit specified. The
        number of items returned, however, can be between zero and the value of
        `MaxResults`. If the service reaches an internal limit while processing the
        results, it stops the operation and returns the matching values up to that point
        and a `NextToken`. You can specify the `NextToken` in a subsequent call to get
        the next set of results.
        """
        if _request is None:
            _params = {}
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if parameter_filters is not ShapeBase.NOT_SET:
                _params['parameter_filters'] = parameter_filters
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.DescribeParametersRequest(**_params)
        paginator = self.get_paginator("describe_parameters").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.DescribeParametersResult.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.DescribeParametersResult.from_boto(response)

    def describe_patch_baselines(
        self,
        _request: shapes.DescribePatchBaselinesRequest = None,
        *,
        filters: typing.List[shapes.PatchOrchestratorFilter
                            ] = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribePatchBaselinesResult:
        """
        Lists the patch baselines in your AWS account.
        """
        if _request is None:
            _params = {}
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.DescribePatchBaselinesRequest(**_params)
        response = self._boto_client.describe_patch_baselines(
            **_request.to_boto()
        )

        return shapes.DescribePatchBaselinesResult.from_boto(response)

    def describe_patch_group_state(
        self,
        _request: shapes.DescribePatchGroupStateRequest = None,
        *,
        patch_group: str,
    ) -> shapes.DescribePatchGroupStateResult:
        """
        Returns high-level aggregated patch compliance state for a patch group.
        """
        if _request is None:
            _params = {}
            if patch_group is not ShapeBase.NOT_SET:
                _params['patch_group'] = patch_group
            _request = shapes.DescribePatchGroupStateRequest(**_params)
        response = self._boto_client.describe_patch_group_state(
            **_request.to_boto()
        )

        return shapes.DescribePatchGroupStateResult.from_boto(response)

    def describe_patch_groups(
        self,
        _request: shapes.DescribePatchGroupsRequest = None,
        *,
        max_results: int = ShapeBase.NOT_SET,
        filters: typing.List[shapes.PatchOrchestratorFilter
                            ] = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribePatchGroupsResult:
        """
        Lists all patch groups that have been registered with patch baselines.
        """
        if _request is None:
            _params = {}
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.DescribePatchGroupsRequest(**_params)
        response = self._boto_client.describe_patch_groups(**_request.to_boto())

        return shapes.DescribePatchGroupsResult.from_boto(response)

    def describe_sessions(
        self,
        _request: shapes.DescribeSessionsRequest = None,
        *,
        state: typing.Union[str, shapes.SessionState],
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        filters: typing.List[shapes.SessionFilter] = ShapeBase.NOT_SET,
    ) -> shapes.DescribeSessionsResponse:
        """
        Retrieves a list of all active sessions (both connected and disconnected) or
        terminated sessions from the past 30 days.
        """
        if _request is None:
            _params = {}
            if state is not ShapeBase.NOT_SET:
                _params['state'] = state
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            _request = shapes.DescribeSessionsRequest(**_params)
        response = self._boto_client.describe_sessions(**_request.to_boto())

        return shapes.DescribeSessionsResponse.from_boto(response)

    def get_automation_execution(
        self,
        _request: shapes.GetAutomationExecutionRequest = None,
        *,
        automation_execution_id: str,
    ) -> shapes.GetAutomationExecutionResult:
        """
        Get detailed information about a particular Automation execution.
        """
        if _request is None:
            _params = {}
            if automation_execution_id is not ShapeBase.NOT_SET:
                _params['automation_execution_id'] = automation_execution_id
            _request = shapes.GetAutomationExecutionRequest(**_params)
        response = self._boto_client.get_automation_execution(
            **_request.to_boto()
        )

        return shapes.GetAutomationExecutionResult.from_boto(response)

    def get_command_invocation(
        self,
        _request: shapes.GetCommandInvocationRequest = None,
        *,
        command_id: str,
        instance_id: str,
        plugin_name: str = ShapeBase.NOT_SET,
    ) -> shapes.GetCommandInvocationResult:
        """
        Returns detailed information about command execution for an invocation or
        plugin.
        """
        if _request is None:
            _params = {}
            if command_id is not ShapeBase.NOT_SET:
                _params['command_id'] = command_id
            if instance_id is not ShapeBase.NOT_SET:
                _params['instance_id'] = instance_id
            if plugin_name is not ShapeBase.NOT_SET:
                _params['plugin_name'] = plugin_name
            _request = shapes.GetCommandInvocationRequest(**_params)
        response = self._boto_client.get_command_invocation(
            **_request.to_boto()
        )

        return shapes.GetCommandInvocationResult.from_boto(response)

    def get_connection_status(
        self,
        _request: shapes.GetConnectionStatusRequest = None,
        *,
        target: str,
    ) -> shapes.GetConnectionStatusResponse:
        """
        Retrieves the Session Manager connection status for an instance to determine
        whether it is connected and ready to receive Session Manager connections.
        """
        if _request is None:
            _params = {}
            if target is not ShapeBase.NOT_SET:
                _params['target'] = target
            _request = shapes.GetConnectionStatusRequest(**_params)
        response = self._boto_client.get_connection_status(**_request.to_boto())

        return shapes.GetConnectionStatusResponse.from_boto(response)

    def get_default_patch_baseline(
        self,
        _request: shapes.GetDefaultPatchBaselineRequest = None,
        *,
        operating_system: typing.Union[str, shapes.OperatingSystem] = ShapeBase.
        NOT_SET,
    ) -> shapes.GetDefaultPatchBaselineResult:
        """
        Retrieves the default patch baseline. Note that Systems Manager supports
        creating multiple default patch baselines. For example, you can create a default
        patch baseline for each operating system.

        If you do not specify an operating system value, the default patch baseline for
        Windows is returned.
        """
        if _request is None:
            _params = {}
            if operating_system is not ShapeBase.NOT_SET:
                _params['operating_system'] = operating_system
            _request = shapes.GetDefaultPatchBaselineRequest(**_params)
        response = self._boto_client.get_default_patch_baseline(
            **_request.to_boto()
        )

        return shapes.GetDefaultPatchBaselineResult.from_boto(response)

    def get_deployable_patch_snapshot_for_instance(
        self,
        _request: shapes.GetDeployablePatchSnapshotForInstanceRequest = None,
        *,
        instance_id: str,
        snapshot_id: str,
    ) -> shapes.GetDeployablePatchSnapshotForInstanceResult:
        """
        Retrieves the current snapshot for the patch baseline the instance uses. This
        API is primarily used by the AWS-RunPatchBaseline Systems Manager document.
        """
        if _request is None:
            _params = {}
            if instance_id is not ShapeBase.NOT_SET:
                _params['instance_id'] = instance_id
            if snapshot_id is not ShapeBase.NOT_SET:
                _params['snapshot_id'] = snapshot_id
            _request = shapes.GetDeployablePatchSnapshotForInstanceRequest(
                **_params
            )
        response = self._boto_client.get_deployable_patch_snapshot_for_instance(
            **_request.to_boto()
        )

        return shapes.GetDeployablePatchSnapshotForInstanceResult.from_boto(
            response
        )

    def get_document(
        self,
        _request: shapes.GetDocumentRequest = None,
        *,
        name: str,
        document_version: str = ShapeBase.NOT_SET,
        document_format: typing.Union[str, shapes.DocumentFormat] = ShapeBase.
        NOT_SET,
    ) -> shapes.GetDocumentResult:
        """
        Gets the contents of the specified Systems Manager document.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if document_version is not ShapeBase.NOT_SET:
                _params['document_version'] = document_version
            if document_format is not ShapeBase.NOT_SET:
                _params['document_format'] = document_format
            _request = shapes.GetDocumentRequest(**_params)
        response = self._boto_client.get_document(**_request.to_boto())

        return shapes.GetDocumentResult.from_boto(response)

    def get_inventory(
        self,
        _request: shapes.GetInventoryRequest = None,
        *,
        filters: typing.List[shapes.InventoryFilter] = ShapeBase.NOT_SET,
        aggregators: typing.List[shapes.InventoryAggregator
                                ] = ShapeBase.NOT_SET,
        result_attributes: typing.List[shapes.ResultAttribute
                                      ] = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.GetInventoryResult:
        """
        Query inventory information.
        """
        if _request is None:
            _params = {}
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if aggregators is not ShapeBase.NOT_SET:
                _params['aggregators'] = aggregators
            if result_attributes is not ShapeBase.NOT_SET:
                _params['result_attributes'] = result_attributes
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.GetInventoryRequest(**_params)
        response = self._boto_client.get_inventory(**_request.to_boto())

        return shapes.GetInventoryResult.from_boto(response)

    def get_inventory_schema(
        self,
        _request: shapes.GetInventorySchemaRequest = None,
        *,
        type_name: str = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        aggregator: bool = ShapeBase.NOT_SET,
        sub_type: bool = ShapeBase.NOT_SET,
    ) -> shapes.GetInventorySchemaResult:
        """
        Return a list of inventory type names for the account, or return a list of
        attribute names for a specific Inventory item type.
        """
        if _request is None:
            _params = {}
            if type_name is not ShapeBase.NOT_SET:
                _params['type_name'] = type_name
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if aggregator is not ShapeBase.NOT_SET:
                _params['aggregator'] = aggregator
            if sub_type is not ShapeBase.NOT_SET:
                _params['sub_type'] = sub_type
            _request = shapes.GetInventorySchemaRequest(**_params)
        response = self._boto_client.get_inventory_schema(**_request.to_boto())

        return shapes.GetInventorySchemaResult.from_boto(response)

    def get_maintenance_window(
        self,
        _request: shapes.GetMaintenanceWindowRequest = None,
        *,
        window_id: str,
    ) -> shapes.GetMaintenanceWindowResult:
        """
        Retrieves a Maintenance Window.
        """
        if _request is None:
            _params = {}
            if window_id is not ShapeBase.NOT_SET:
                _params['window_id'] = window_id
            _request = shapes.GetMaintenanceWindowRequest(**_params)
        response = self._boto_client.get_maintenance_window(
            **_request.to_boto()
        )

        return shapes.GetMaintenanceWindowResult.from_boto(response)

    def get_maintenance_window_execution(
        self,
        _request: shapes.GetMaintenanceWindowExecutionRequest = None,
        *,
        window_execution_id: str,
    ) -> shapes.GetMaintenanceWindowExecutionResult:
        """
        Retrieves details about a specific task executed as part of a Maintenance Window
        execution.
        """
        if _request is None:
            _params = {}
            if window_execution_id is not ShapeBase.NOT_SET:
                _params['window_execution_id'] = window_execution_id
            _request = shapes.GetMaintenanceWindowExecutionRequest(**_params)
        response = self._boto_client.get_maintenance_window_execution(
            **_request.to_boto()
        )

        return shapes.GetMaintenanceWindowExecutionResult.from_boto(response)

    def get_maintenance_window_execution_task(
        self,
        _request: shapes.GetMaintenanceWindowExecutionTaskRequest = None,
        *,
        window_execution_id: str,
        task_id: str,
    ) -> shapes.GetMaintenanceWindowExecutionTaskResult:
        """
        Retrieves the details about a specific task executed as part of a Maintenance
        Window execution.
        """
        if _request is None:
            _params = {}
            if window_execution_id is not ShapeBase.NOT_SET:
                _params['window_execution_id'] = window_execution_id
            if task_id is not ShapeBase.NOT_SET:
                _params['task_id'] = task_id
            _request = shapes.GetMaintenanceWindowExecutionTaskRequest(
                **_params
            )
        response = self._boto_client.get_maintenance_window_execution_task(
            **_request.to_boto()
        )

        return shapes.GetMaintenanceWindowExecutionTaskResult.from_boto(
            response
        )

    def get_maintenance_window_execution_task_invocation(
        self,
        _request: shapes.
        GetMaintenanceWindowExecutionTaskInvocationRequest = None,
        *,
        window_execution_id: str,
        task_id: str,
        invocation_id: str,
    ) -> shapes.GetMaintenanceWindowExecutionTaskInvocationResult:
        """
        Retrieves a task invocation. A task invocation is a specific task executing on a
        specific target. Maintenance Windows report status for all invocations.
        """
        if _request is None:
            _params = {}
            if window_execution_id is not ShapeBase.NOT_SET:
                _params['window_execution_id'] = window_execution_id
            if task_id is not ShapeBase.NOT_SET:
                _params['task_id'] = task_id
            if invocation_id is not ShapeBase.NOT_SET:
                _params['invocation_id'] = invocation_id
            _request = shapes.GetMaintenanceWindowExecutionTaskInvocationRequest(
                **_params
            )
        response = self._boto_client.get_maintenance_window_execution_task_invocation(
            **_request.to_boto()
        )

        return shapes.GetMaintenanceWindowExecutionTaskInvocationResult.from_boto(
            response
        )

    def get_maintenance_window_task(
        self,
        _request: shapes.GetMaintenanceWindowTaskRequest = None,
        *,
        window_id: str,
        window_task_id: str,
    ) -> shapes.GetMaintenanceWindowTaskResult:
        """
        Lists the tasks in a Maintenance Window.
        """
        if _request is None:
            _params = {}
            if window_id is not ShapeBase.NOT_SET:
                _params['window_id'] = window_id
            if window_task_id is not ShapeBase.NOT_SET:
                _params['window_task_id'] = window_task_id
            _request = shapes.GetMaintenanceWindowTaskRequest(**_params)
        response = self._boto_client.get_maintenance_window_task(
            **_request.to_boto()
        )

        return shapes.GetMaintenanceWindowTaskResult.from_boto(response)

    def get_parameter(
        self,
        _request: shapes.GetParameterRequest = None,
        *,
        name: str,
        with_decryption: bool = ShapeBase.NOT_SET,
    ) -> shapes.GetParameterResult:
        """
        Get information about a parameter by using the parameter name. Don't confuse
        this API action with the GetParameters API action.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if with_decryption is not ShapeBase.NOT_SET:
                _params['with_decryption'] = with_decryption
            _request = shapes.GetParameterRequest(**_params)
        response = self._boto_client.get_parameter(**_request.to_boto())

        return shapes.GetParameterResult.from_boto(response)

    def get_parameter_history(
        self,
        _request: shapes.GetParameterHistoryRequest = None,
        *,
        name: str,
        with_decryption: bool = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.GetParameterHistoryResult:
        """
        Query a list of all parameters used by the AWS account.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if with_decryption is not ShapeBase.NOT_SET:
                _params['with_decryption'] = with_decryption
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.GetParameterHistoryRequest(**_params)
        paginator = self.get_paginator("get_parameter_history").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.GetParameterHistoryResult.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.GetParameterHistoryResult.from_boto(response)

    def get_parameters(
        self,
        _request: shapes.GetParametersRequest = None,
        *,
        names: typing.List[str],
        with_decryption: bool = ShapeBase.NOT_SET,
    ) -> shapes.GetParametersResult:
        """
        Get details of a parameter. Don't confuse this API action with the GetParameter
        API action.
        """
        if _request is None:
            _params = {}
            if names is not ShapeBase.NOT_SET:
                _params['names'] = names
            if with_decryption is not ShapeBase.NOT_SET:
                _params['with_decryption'] = with_decryption
            _request = shapes.GetParametersRequest(**_params)
        response = self._boto_client.get_parameters(**_request.to_boto())

        return shapes.GetParametersResult.from_boto(response)

    def get_parameters_by_path(
        self,
        _request: shapes.GetParametersByPathRequest = None,
        *,
        path: str,
        recursive: bool = ShapeBase.NOT_SET,
        parameter_filters: typing.List[shapes.ParameterStringFilter
                                      ] = ShapeBase.NOT_SET,
        with_decryption: bool = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.GetParametersByPathResult:
        """
        Retrieve parameters in a specific hierarchy. For more information, see [Working
        with Systems Manager Parameters](http://docs.aws.amazon.com/systems-
        manager/latest/userguide/sysman-paramstore-working.html) in the _AWS Systems
        Manager User Guide_.

        Request results are returned on a best-effort basis. If you specify `MaxResults`
        in the request, the response includes information up to the limit specified. The
        number of items returned, however, can be between zero and the value of
        `MaxResults`. If the service reaches an internal limit while processing the
        results, it stops the operation and returns the matching values up to that point
        and a `NextToken`. You can specify the `NextToken` in a subsequent call to get
        the next set of results.

        This API action doesn't support filtering by tags.
        """
        if _request is None:
            _params = {}
            if path is not ShapeBase.NOT_SET:
                _params['path'] = path
            if recursive is not ShapeBase.NOT_SET:
                _params['recursive'] = recursive
            if parameter_filters is not ShapeBase.NOT_SET:
                _params['parameter_filters'] = parameter_filters
            if with_decryption is not ShapeBase.NOT_SET:
                _params['with_decryption'] = with_decryption
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.GetParametersByPathRequest(**_params)
        paginator = self.get_paginator("get_parameters_by_path").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.GetParametersByPathResult.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.GetParametersByPathResult.from_boto(response)

    def get_patch_baseline(
        self,
        _request: shapes.GetPatchBaselineRequest = None,
        *,
        baseline_id: str,
    ) -> shapes.GetPatchBaselineResult:
        """
        Retrieves information about a patch baseline.
        """
        if _request is None:
            _params = {}
            if baseline_id is not ShapeBase.NOT_SET:
                _params['baseline_id'] = baseline_id
            _request = shapes.GetPatchBaselineRequest(**_params)
        response = self._boto_client.get_patch_baseline(**_request.to_boto())

        return shapes.GetPatchBaselineResult.from_boto(response)

    def get_patch_baseline_for_patch_group(
        self,
        _request: shapes.GetPatchBaselineForPatchGroupRequest = None,
        *,
        patch_group: str,
        operating_system: typing.Union[str, shapes.OperatingSystem] = ShapeBase.
        NOT_SET,
    ) -> shapes.GetPatchBaselineForPatchGroupResult:
        """
        Retrieves the patch baseline that should be used for the specified patch group.
        """
        if _request is None:
            _params = {}
            if patch_group is not ShapeBase.NOT_SET:
                _params['patch_group'] = patch_group
            if operating_system is not ShapeBase.NOT_SET:
                _params['operating_system'] = operating_system
            _request = shapes.GetPatchBaselineForPatchGroupRequest(**_params)
        response = self._boto_client.get_patch_baseline_for_patch_group(
            **_request.to_boto()
        )

        return shapes.GetPatchBaselineForPatchGroupResult.from_boto(response)

    def label_parameter_version(
        self,
        _request: shapes.LabelParameterVersionRequest = None,
        *,
        name: str,
        labels: typing.List[str],
        parameter_version: int = ShapeBase.NOT_SET,
    ) -> shapes.LabelParameterVersionResult:
        """
        A parameter label is a user-defined alias to help you manage different versions
        of a parameter. When you modify a parameter, Systems Manager automatically saves
        a new version and increments the version number by one. A label can help you
        remember the purpose of a parameter when there are multiple versions.

        Parameter labels have the following requirements and restrictions.

          * A version of a parameter can have a maximum of 10 labels.

          * You can't attach the same label to different versions of the same parameter. For example, if version 1 has the label Production, then you can't attach Production to version 2.

          * You can move a label from one version of a parameter to another.

          * You can't create a label when you create a new parameter. You must attach a label to a specific version of a parameter.

          * You can't delete a parameter label. If you no longer want to use a parameter label, then you must move it to a different version of a parameter.

          * A label can have a maximum of 100 characters.

          * Labels can contain letters (case sensitive), numbers, periods (.), hyphens (-), or underscores (_).

          * Labels can't begin with a number, "aws," or "ssm" (not case sensitive). If a label fails to meet these requirements, then the label is not associated with a parameter and the system displays it in the list of InvalidLabels.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if labels is not ShapeBase.NOT_SET:
                _params['labels'] = labels
            if parameter_version is not ShapeBase.NOT_SET:
                _params['parameter_version'] = parameter_version
            _request = shapes.LabelParameterVersionRequest(**_params)
        response = self._boto_client.label_parameter_version(
            **_request.to_boto()
        )

        return shapes.LabelParameterVersionResult.from_boto(response)

    def list_association_versions(
        self,
        _request: shapes.ListAssociationVersionsRequest = None,
        *,
        association_id: str,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListAssociationVersionsResult:
        """
        Retrieves all versions of an association for a specific association ID.
        """
        if _request is None:
            _params = {}
            if association_id is not ShapeBase.NOT_SET:
                _params['association_id'] = association_id
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListAssociationVersionsRequest(**_params)
        response = self._boto_client.list_association_versions(
            **_request.to_boto()
        )

        return shapes.ListAssociationVersionsResult.from_boto(response)

    def list_associations(
        self,
        _request: shapes.ListAssociationsRequest = None,
        *,
        association_filter_list: typing.List[shapes.AssociationFilter
                                            ] = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListAssociationsResult:
        """
        Lists the associations for the specified Systems Manager document or instance.
        """
        if _request is None:
            _params = {}
            if association_filter_list is not ShapeBase.NOT_SET:
                _params['association_filter_list'] = association_filter_list
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListAssociationsRequest(**_params)
        paginator = self.get_paginator("list_associations").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListAssociationsResult.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListAssociationsResult.from_boto(response)

    def list_command_invocations(
        self,
        _request: shapes.ListCommandInvocationsRequest = None,
        *,
        command_id: str = ShapeBase.NOT_SET,
        instance_id: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        filters: typing.List[shapes.CommandFilter] = ShapeBase.NOT_SET,
        details: bool = ShapeBase.NOT_SET,
    ) -> shapes.ListCommandInvocationsResult:
        """
        An invocation is copy of a command sent to a specific instance. A command can
        apply to one or more instances. A command invocation applies to one instance.
        For example, if a user executes SendCommand against three instances, then a
        command invocation is created for each requested instance ID.
        ListCommandInvocations provide status about command execution.
        """
        if _request is None:
            _params = {}
            if command_id is not ShapeBase.NOT_SET:
                _params['command_id'] = command_id
            if instance_id is not ShapeBase.NOT_SET:
                _params['instance_id'] = instance_id
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if details is not ShapeBase.NOT_SET:
                _params['details'] = details
            _request = shapes.ListCommandInvocationsRequest(**_params)
        paginator = self.get_paginator("list_command_invocations").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListCommandInvocationsResult.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListCommandInvocationsResult.from_boto(response)

    def list_commands(
        self,
        _request: shapes.ListCommandsRequest = None,
        *,
        command_id: str = ShapeBase.NOT_SET,
        instance_id: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        filters: typing.List[shapes.CommandFilter] = ShapeBase.NOT_SET,
    ) -> shapes.ListCommandsResult:
        """
        Lists the commands requested by users of the AWS account.
        """
        if _request is None:
            _params = {}
            if command_id is not ShapeBase.NOT_SET:
                _params['command_id'] = command_id
            if instance_id is not ShapeBase.NOT_SET:
                _params['instance_id'] = instance_id
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            _request = shapes.ListCommandsRequest(**_params)
        paginator = self.get_paginator("list_commands").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListCommandsResult.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListCommandsResult.from_boto(response)

    def list_compliance_items(
        self,
        _request: shapes.ListComplianceItemsRequest = None,
        *,
        filters: typing.List[shapes.ComplianceStringFilter] = ShapeBase.NOT_SET,
        resource_ids: typing.List[str] = ShapeBase.NOT_SET,
        resource_types: typing.List[str] = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.ListComplianceItemsResult:
        """
        For a specified resource ID, this API action returns a list of compliance
        statuses for different resource types. Currently, you can only specify one
        resource ID per call. List results depend on the criteria specified in the
        filter.
        """
        if _request is None:
            _params = {}
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if resource_ids is not ShapeBase.NOT_SET:
                _params['resource_ids'] = resource_ids
            if resource_types is not ShapeBase.NOT_SET:
                _params['resource_types'] = resource_types
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.ListComplianceItemsRequest(**_params)
        response = self._boto_client.list_compliance_items(**_request.to_boto())

        return shapes.ListComplianceItemsResult.from_boto(response)

    def list_compliance_summaries(
        self,
        _request: shapes.ListComplianceSummariesRequest = None,
        *,
        filters: typing.List[shapes.ComplianceStringFilter] = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.ListComplianceSummariesResult:
        """
        Returns a summary count of compliant and non-compliant resources for a
        compliance type. For example, this call can return State Manager associations,
        patches, or custom compliance types according to the filter criteria that you
        specify.
        """
        if _request is None:
            _params = {}
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.ListComplianceSummariesRequest(**_params)
        response = self._boto_client.list_compliance_summaries(
            **_request.to_boto()
        )

        return shapes.ListComplianceSummariesResult.from_boto(response)

    def list_document_versions(
        self,
        _request: shapes.ListDocumentVersionsRequest = None,
        *,
        name: str,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListDocumentVersionsResult:
        """
        List all versions for a document.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListDocumentVersionsRequest(**_params)
        response = self._boto_client.list_document_versions(
            **_request.to_boto()
        )

        return shapes.ListDocumentVersionsResult.from_boto(response)

    def list_documents(
        self,
        _request: shapes.ListDocumentsRequest = None,
        *,
        document_filter_list: typing.List[shapes.DocumentFilter
                                         ] = ShapeBase.NOT_SET,
        filters: typing.List[shapes.DocumentKeyValuesFilter
                            ] = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListDocumentsResult:
        """
        Describes one or more of your Systems Manager documents.
        """
        if _request is None:
            _params = {}
            if document_filter_list is not ShapeBase.NOT_SET:
                _params['document_filter_list'] = document_filter_list
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListDocumentsRequest(**_params)
        paginator = self.get_paginator("list_documents").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListDocumentsResult.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListDocumentsResult.from_boto(response)

    def list_inventory_entries(
        self,
        _request: shapes.ListInventoryEntriesRequest = None,
        *,
        instance_id: str,
        type_name: str,
        filters: typing.List[shapes.InventoryFilter] = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.ListInventoryEntriesResult:
        """
        A list of inventory items returned by the request.
        """
        if _request is None:
            _params = {}
            if instance_id is not ShapeBase.NOT_SET:
                _params['instance_id'] = instance_id
            if type_name is not ShapeBase.NOT_SET:
                _params['type_name'] = type_name
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.ListInventoryEntriesRequest(**_params)
        response = self._boto_client.list_inventory_entries(
            **_request.to_boto()
        )

        return shapes.ListInventoryEntriesResult.from_boto(response)

    def list_resource_compliance_summaries(
        self,
        _request: shapes.ListResourceComplianceSummariesRequest = None,
        *,
        filters: typing.List[shapes.ComplianceStringFilter] = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.ListResourceComplianceSummariesResult:
        """
        Returns a resource-level summary count. The summary includes information about
        compliant and non-compliant statuses and detailed compliance-item severity
        counts, according to the filter criteria you specify.
        """
        if _request is None:
            _params = {}
            if filters is not ShapeBase.NOT_SET:
                _params['filters'] = filters
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.ListResourceComplianceSummariesRequest(**_params)
        response = self._boto_client.list_resource_compliance_summaries(
            **_request.to_boto()
        )

        return shapes.ListResourceComplianceSummariesResult.from_boto(response)

    def list_resource_data_sync(
        self,
        _request: shapes.ListResourceDataSyncRequest = None,
        *,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.ListResourceDataSyncResult:
        """
        Lists your resource data sync configurations. Includes information about the
        last time a sync attempted to start, the last sync status, and the last time a
        sync successfully completed.

        The number of sync configurations might be too large to return using a single
        call to `ListResourceDataSync`. You can limit the number of sync configurations
        returned by using the `MaxResults` parameter. To determine whether there are
        more sync configurations to list, check the value of `NextToken` in the output.
        If there are more sync configurations to list, you can request them by
        specifying the `NextToken` returned in the call to the parameter of a subsequent
        call.
        """
        if _request is None:
            _params = {}
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.ListResourceDataSyncRequest(**_params)
        response = self._boto_client.list_resource_data_sync(
            **_request.to_boto()
        )

        return shapes.ListResourceDataSyncResult.from_boto(response)

    def list_tags_for_resource(
        self,
        _request: shapes.ListTagsForResourceRequest = None,
        *,
        resource_type: typing.Union[str, shapes.ResourceTypeForTagging],
        resource_id: str,
    ) -> shapes.ListTagsForResourceResult:
        """
        Returns a list of the tags assigned to the specified resource.
        """
        if _request is None:
            _params = {}
            if resource_type is not ShapeBase.NOT_SET:
                _params['resource_type'] = resource_type
            if resource_id is not ShapeBase.NOT_SET:
                _params['resource_id'] = resource_id
            _request = shapes.ListTagsForResourceRequest(**_params)
        response = self._boto_client.list_tags_for_resource(
            **_request.to_boto()
        )

        return shapes.ListTagsForResourceResult.from_boto(response)

    def modify_document_permission(
        self,
        _request: shapes.ModifyDocumentPermissionRequest = None,
        *,
        name: str,
        permission_type: typing.Union[str, shapes.DocumentPermissionType],
        account_ids_to_add: typing.List[str] = ShapeBase.NOT_SET,
        account_ids_to_remove: typing.List[str] = ShapeBase.NOT_SET,
    ) -> shapes.ModifyDocumentPermissionResponse:
        """
        Shares a Systems Manager document publicly or privately. If you share a document
        privately, you must specify the AWS user account IDs for those people who can
        use the document. If you share a document publicly, you must specify _All_ as
        the account ID.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if permission_type is not ShapeBase.NOT_SET:
                _params['permission_type'] = permission_type
            if account_ids_to_add is not ShapeBase.NOT_SET:
                _params['account_ids_to_add'] = account_ids_to_add
            if account_ids_to_remove is not ShapeBase.NOT_SET:
                _params['account_ids_to_remove'] = account_ids_to_remove
            _request = shapes.ModifyDocumentPermissionRequest(**_params)
        response = self._boto_client.modify_document_permission(
            **_request.to_boto()
        )

        return shapes.ModifyDocumentPermissionResponse.from_boto(response)

    def put_compliance_items(
        self,
        _request: shapes.PutComplianceItemsRequest = None,
        *,
        resource_id: str,
        resource_type: str,
        compliance_type: str,
        execution_summary: shapes.ComplianceExecutionSummary,
        items: typing.List[shapes.ComplianceItemEntry],
        item_content_hash: str = ShapeBase.NOT_SET,
    ) -> shapes.PutComplianceItemsResult:
        """
        Registers a compliance type and other compliance details on a designated
        resource. This action lets you register custom compliance details with a
        resource. This call overwrites existing compliance information on the resource,
        so you must provide a full list of compliance items each time that you send the
        request.

        ComplianceType can be one of the following:

          * ExecutionId: The execution ID when the patch, association, or custom compliance item was applied.

          * ExecutionType: Specify patch, association, or Custom:`string`.

          * ExecutionTime. The time the patch, association, or custom compliance item was applied to the instance.

          * Id: The patch, association, or custom compliance ID.

          * Title: A title.

          * Status: The status of the compliance item. For example, `approved` for patches, or `Failed` for associations.

          * Severity: A patch severity. For example, `critical`.

          * DocumentName: A SSM document name. For example, AWS-RunPatchBaseline.

          * DocumentVersion: An SSM document version number. For example, 4.

          * Classification: A patch classification. For example, `security updates`.

          * PatchBaselineId: A patch baseline ID.

          * PatchSeverity: A patch severity. For example, `Critical`.

          * PatchState: A patch state. For example, `InstancesWithFailedPatches`.

          * PatchGroup: The name of a patch group.

          * InstalledTime: The time the association, patch, or custom compliance item was applied to the resource. Specify the time by using the following format: yyyy-MM-dd'T'HH:mm:ss'Z'
        """
        if _request is None:
            _params = {}
            if resource_id is not ShapeBase.NOT_SET:
                _params['resource_id'] = resource_id
            if resource_type is not ShapeBase.NOT_SET:
                _params['resource_type'] = resource_type
            if compliance_type is not ShapeBase.NOT_SET:
                _params['compliance_type'] = compliance_type
            if execution_summary is not ShapeBase.NOT_SET:
                _params['execution_summary'] = execution_summary
            if items is not ShapeBase.NOT_SET:
                _params['items'] = items
            if item_content_hash is not ShapeBase.NOT_SET:
                _params['item_content_hash'] = item_content_hash
            _request = shapes.PutComplianceItemsRequest(**_params)
        response = self._boto_client.put_compliance_items(**_request.to_boto())

        return shapes.PutComplianceItemsResult.from_boto(response)

    def put_inventory(
        self,
        _request: shapes.PutInventoryRequest = None,
        *,
        instance_id: str,
        items: typing.List[shapes.InventoryItem],
    ) -> shapes.PutInventoryResult:
        """
        Bulk update custom inventory items on one more instance. The request adds an
        inventory item, if it doesn't already exist, or updates an inventory item, if it
        does exist.
        """
        if _request is None:
            _params = {}
            if instance_id is not ShapeBase.NOT_SET:
                _params['instance_id'] = instance_id
            if items is not ShapeBase.NOT_SET:
                _params['items'] = items
            _request = shapes.PutInventoryRequest(**_params)
        response = self._boto_client.put_inventory(**_request.to_boto())

        return shapes.PutInventoryResult.from_boto(response)

    def put_parameter(
        self,
        _request: shapes.PutParameterRequest = None,
        *,
        name: str,
        value: str,
        type: typing.Union[str, shapes.ParameterType],
        description: str = ShapeBase.NOT_SET,
        key_id: str = ShapeBase.NOT_SET,
        overwrite: bool = ShapeBase.NOT_SET,
        allowed_pattern: str = ShapeBase.NOT_SET,
    ) -> shapes.PutParameterResult:
        """
        Add a parameter to the system.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if value is not ShapeBase.NOT_SET:
                _params['value'] = value
            if type is not ShapeBase.NOT_SET:
                _params['type'] = type
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if key_id is not ShapeBase.NOT_SET:
                _params['key_id'] = key_id
            if overwrite is not ShapeBase.NOT_SET:
                _params['overwrite'] = overwrite
            if allowed_pattern is not ShapeBase.NOT_SET:
                _params['allowed_pattern'] = allowed_pattern
            _request = shapes.PutParameterRequest(**_params)
        response = self._boto_client.put_parameter(**_request.to_boto())

        return shapes.PutParameterResult.from_boto(response)

    def register_default_patch_baseline(
        self,
        _request: shapes.RegisterDefaultPatchBaselineRequest = None,
        *,
        baseline_id: str,
    ) -> shapes.RegisterDefaultPatchBaselineResult:
        """
        Defines the default patch baseline.
        """
        if _request is None:
            _params = {}
            if baseline_id is not ShapeBase.NOT_SET:
                _params['baseline_id'] = baseline_id
            _request = shapes.RegisterDefaultPatchBaselineRequest(**_params)
        response = self._boto_client.register_default_patch_baseline(
            **_request.to_boto()
        )

        return shapes.RegisterDefaultPatchBaselineResult.from_boto(response)

    def register_patch_baseline_for_patch_group(
        self,
        _request: shapes.RegisterPatchBaselineForPatchGroupRequest = None,
        *,
        baseline_id: str,
        patch_group: str,
    ) -> shapes.RegisterPatchBaselineForPatchGroupResult:
        """
        Registers a patch baseline for a patch group.
        """
        if _request is None:
            _params = {}
            if baseline_id is not ShapeBase.NOT_SET:
                _params['baseline_id'] = baseline_id
            if patch_group is not ShapeBase.NOT_SET:
                _params['patch_group'] = patch_group
            _request = shapes.RegisterPatchBaselineForPatchGroupRequest(
                **_params
            )
        response = self._boto_client.register_patch_baseline_for_patch_group(
            **_request.to_boto()
        )

        return shapes.RegisterPatchBaselineForPatchGroupResult.from_boto(
            response
        )

    def register_target_with_maintenance_window(
        self,
        _request: shapes.RegisterTargetWithMaintenanceWindowRequest = None,
        *,
        window_id: str,
        resource_type: typing.Union[str, shapes.MaintenanceWindowResourceType],
        targets: typing.List[shapes.Target],
        owner_information: str = ShapeBase.NOT_SET,
        name: str = ShapeBase.NOT_SET,
        description: str = ShapeBase.NOT_SET,
        client_token: str = ShapeBase.NOT_SET,
    ) -> shapes.RegisterTargetWithMaintenanceWindowResult:
        """
        Registers a target with a Maintenance Window.
        """
        if _request is None:
            _params = {}
            if window_id is not ShapeBase.NOT_SET:
                _params['window_id'] = window_id
            if resource_type is not ShapeBase.NOT_SET:
                _params['resource_type'] = resource_type
            if targets is not ShapeBase.NOT_SET:
                _params['targets'] = targets
            if owner_information is not ShapeBase.NOT_SET:
                _params['owner_information'] = owner_information
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if client_token is not ShapeBase.NOT_SET:
                _params['client_token'] = client_token
            _request = shapes.RegisterTargetWithMaintenanceWindowRequest(
                **_params
            )
        response = self._boto_client.register_target_with_maintenance_window(
            **_request.to_boto()
        )

        return shapes.RegisterTargetWithMaintenanceWindowResult.from_boto(
            response
        )

    def register_task_with_maintenance_window(
        self,
        _request: shapes.RegisterTaskWithMaintenanceWindowRequest = None,
        *,
        window_id: str,
        targets: typing.List[shapes.Target],
        task_arn: str,
        task_type: typing.Union[str, shapes.MaintenanceWindowTaskType],
        max_concurrency: str,
        max_errors: str,
        service_role_arn: str = ShapeBase.NOT_SET,
        task_parameters: typing.
        Dict[str, shapes.
             MaintenanceWindowTaskParameterValueExpression] = ShapeBase.NOT_SET,
        task_invocation_parameters: shapes.
        MaintenanceWindowTaskInvocationParameters = ShapeBase.NOT_SET,
        priority: int = ShapeBase.NOT_SET,
        logging_info: shapes.LoggingInfo = ShapeBase.NOT_SET,
        name: str = ShapeBase.NOT_SET,
        description: str = ShapeBase.NOT_SET,
        client_token: str = ShapeBase.NOT_SET,
    ) -> shapes.RegisterTaskWithMaintenanceWindowResult:
        """
        Adds a new task to a Maintenance Window.
        """
        if _request is None:
            _params = {}
            if window_id is not ShapeBase.NOT_SET:
                _params['window_id'] = window_id
            if targets is not ShapeBase.NOT_SET:
                _params['targets'] = targets
            if task_arn is not ShapeBase.NOT_SET:
                _params['task_arn'] = task_arn
            if task_type is not ShapeBase.NOT_SET:
                _params['task_type'] = task_type
            if max_concurrency is not ShapeBase.NOT_SET:
                _params['max_concurrency'] = max_concurrency
            if max_errors is not ShapeBase.NOT_SET:
                _params['max_errors'] = max_errors
            if service_role_arn is not ShapeBase.NOT_SET:
                _params['service_role_arn'] = service_role_arn
            if task_parameters is not ShapeBase.NOT_SET:
                _params['task_parameters'] = task_parameters
            if task_invocation_parameters is not ShapeBase.NOT_SET:
                _params['task_invocation_parameters'
                       ] = task_invocation_parameters
            if priority is not ShapeBase.NOT_SET:
                _params['priority'] = priority
            if logging_info is not ShapeBase.NOT_SET:
                _params['logging_info'] = logging_info
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if client_token is not ShapeBase.NOT_SET:
                _params['client_token'] = client_token
            _request = shapes.RegisterTaskWithMaintenanceWindowRequest(
                **_params
            )
        response = self._boto_client.register_task_with_maintenance_window(
            **_request.to_boto()
        )

        return shapes.RegisterTaskWithMaintenanceWindowResult.from_boto(
            response
        )

    def remove_tags_from_resource(
        self,
        _request: shapes.RemoveTagsFromResourceRequest = None,
        *,
        resource_type: typing.Union[str, shapes.ResourceTypeForTagging],
        resource_id: str,
        tag_keys: typing.List[str],
    ) -> shapes.RemoveTagsFromResourceResult:
        """
        Removes all tags from the specified resource.
        """
        if _request is None:
            _params = {}
            if resource_type is not ShapeBase.NOT_SET:
                _params['resource_type'] = resource_type
            if resource_id is not ShapeBase.NOT_SET:
                _params['resource_id'] = resource_id
            if tag_keys is not ShapeBase.NOT_SET:
                _params['tag_keys'] = tag_keys
            _request = shapes.RemoveTagsFromResourceRequest(**_params)
        response = self._boto_client.remove_tags_from_resource(
            **_request.to_boto()
        )

        return shapes.RemoveTagsFromResourceResult.from_boto(response)

    def resume_session(
        self,
        _request: shapes.ResumeSessionRequest = None,
        *,
        session_id: str,
    ) -> shapes.ResumeSessionResponse:
        """
        Reconnects a session to an instance after it has been disconnected. Connections
        can be resumed for disconnected sessions, but not terminated sessions.

        This command is primarily for use by client machines to automatically reconnect
        during intermittent network issues. It is not intended for any other use.
        """
        if _request is None:
            _params = {}
            if session_id is not ShapeBase.NOT_SET:
                _params['session_id'] = session_id
            _request = shapes.ResumeSessionRequest(**_params)
        response = self._boto_client.resume_session(**_request.to_boto())

        return shapes.ResumeSessionResponse.from_boto(response)

    def send_automation_signal(
        self,
        _request: shapes.SendAutomationSignalRequest = None,
        *,
        automation_execution_id: str,
        signal_type: typing.Union[str, shapes.SignalType],
        payload: typing.Dict[str, typing.List[str]] = ShapeBase.NOT_SET,
    ) -> shapes.SendAutomationSignalResult:
        """
        Sends a signal to an Automation execution to change the current behavior or
        status of the execution.
        """
        if _request is None:
            _params = {}
            if automation_execution_id is not ShapeBase.NOT_SET:
                _params['automation_execution_id'] = automation_execution_id
            if signal_type is not ShapeBase.NOT_SET:
                _params['signal_type'] = signal_type
            if payload is not ShapeBase.NOT_SET:
                _params['payload'] = payload
            _request = shapes.SendAutomationSignalRequest(**_params)
        response = self._boto_client.send_automation_signal(
            **_request.to_boto()
        )

        return shapes.SendAutomationSignalResult.from_boto(response)

    def send_command(
        self,
        _request: shapes.SendCommandRequest = None,
        *,
        document_name: str,
        instance_ids: typing.List[str] = ShapeBase.NOT_SET,
        targets: typing.List[shapes.Target] = ShapeBase.NOT_SET,
        document_version: str = ShapeBase.NOT_SET,
        document_hash: str = ShapeBase.NOT_SET,
        document_hash_type: typing.Union[str, shapes.
                                         DocumentHashType] = ShapeBase.NOT_SET,
        timeout_seconds: int = ShapeBase.NOT_SET,
        comment: str = ShapeBase.NOT_SET,
        parameters: typing.Dict[str, typing.List[str]] = ShapeBase.NOT_SET,
        output_s3_region: str = ShapeBase.NOT_SET,
        output_s3_bucket_name: str = ShapeBase.NOT_SET,
        output_s3_key_prefix: str = ShapeBase.NOT_SET,
        max_concurrency: str = ShapeBase.NOT_SET,
        max_errors: str = ShapeBase.NOT_SET,
        service_role_arn: str = ShapeBase.NOT_SET,
        notification_config: shapes.NotificationConfig = ShapeBase.NOT_SET,
        cloud_watch_output_config: shapes.CloudWatchOutputConfig = ShapeBase.
        NOT_SET,
    ) -> shapes.SendCommandResult:
        """
        Executes commands on one or more managed instances.
        """
        if _request is None:
            _params = {}
            if document_name is not ShapeBase.NOT_SET:
                _params['document_name'] = document_name
            if instance_ids is not ShapeBase.NOT_SET:
                _params['instance_ids'] = instance_ids
            if targets is not ShapeBase.NOT_SET:
                _params['targets'] = targets
            if document_version is not ShapeBase.NOT_SET:
                _params['document_version'] = document_version
            if document_hash is not ShapeBase.NOT_SET:
                _params['document_hash'] = document_hash
            if document_hash_type is not ShapeBase.NOT_SET:
                _params['document_hash_type'] = document_hash_type
            if timeout_seconds is not ShapeBase.NOT_SET:
                _params['timeout_seconds'] = timeout_seconds
            if comment is not ShapeBase.NOT_SET:
                _params['comment'] = comment
            if parameters is not ShapeBase.NOT_SET:
                _params['parameters'] = parameters
            if output_s3_region is not ShapeBase.NOT_SET:
                _params['output_s3_region'] = output_s3_region
            if output_s3_bucket_name is not ShapeBase.NOT_SET:
                _params['output_s3_bucket_name'] = output_s3_bucket_name
            if output_s3_key_prefix is not ShapeBase.NOT_SET:
                _params['output_s3_key_prefix'] = output_s3_key_prefix
            if max_concurrency is not ShapeBase.NOT_SET:
                _params['max_concurrency'] = max_concurrency
            if max_errors is not ShapeBase.NOT_SET:
                _params['max_errors'] = max_errors
            if service_role_arn is not ShapeBase.NOT_SET:
                _params['service_role_arn'] = service_role_arn
            if notification_config is not ShapeBase.NOT_SET:
                _params['notification_config'] = notification_config
            if cloud_watch_output_config is not ShapeBase.NOT_SET:
                _params['cloud_watch_output_config'] = cloud_watch_output_config
            _request = shapes.SendCommandRequest(**_params)
        response = self._boto_client.send_command(**_request.to_boto())

        return shapes.SendCommandResult.from_boto(response)

    def start_associations_once(
        self,
        _request: shapes.StartAssociationsOnceRequest = None,
        *,
        association_ids: typing.List[str],
    ) -> shapes.StartAssociationsOnceResult:
        """
        Use this API action to execute an association immediately and only one time.
        This action can be helpful when troubleshooting associations.
        """
        if _request is None:
            _params = {}
            if association_ids is not ShapeBase.NOT_SET:
                _params['association_ids'] = association_ids
            _request = shapes.StartAssociationsOnceRequest(**_params)
        response = self._boto_client.start_associations_once(
            **_request.to_boto()
        )

        return shapes.StartAssociationsOnceResult.from_boto(response)

    def start_automation_execution(
        self,
        _request: shapes.StartAutomationExecutionRequest = None,
        *,
        document_name: str,
        document_version: str = ShapeBase.NOT_SET,
        parameters: typing.Dict[str, typing.List[str]] = ShapeBase.NOT_SET,
        client_token: str = ShapeBase.NOT_SET,
        mode: typing.Union[str, shapes.ExecutionMode] = ShapeBase.NOT_SET,
        target_parameter_name: str = ShapeBase.NOT_SET,
        targets: typing.List[shapes.Target] = ShapeBase.NOT_SET,
        target_maps: typing.List[typing.Dict[str, typing.List[str]]
                                ] = ShapeBase.NOT_SET,
        max_concurrency: str = ShapeBase.NOT_SET,
        max_errors: str = ShapeBase.NOT_SET,
    ) -> shapes.StartAutomationExecutionResult:
        """
        Initiates execution of an Automation document.
        """
        if _request is None:
            _params = {}
            if document_name is not ShapeBase.NOT_SET:
                _params['document_name'] = document_name
            if document_version is not ShapeBase.NOT_SET:
                _params['document_version'] = document_version
            if parameters is not ShapeBase.NOT_SET:
                _params['parameters'] = parameters
            if client_token is not ShapeBase.NOT_SET:
                _params['client_token'] = client_token
            if mode is not ShapeBase.NOT_SET:
                _params['mode'] = mode
            if target_parameter_name is not ShapeBase.NOT_SET:
                _params['target_parameter_name'] = target_parameter_name
            if targets is not ShapeBase.NOT_SET:
                _params['targets'] = targets
            if target_maps is not ShapeBase.NOT_SET:
                _params['target_maps'] = target_maps
            if max_concurrency is not ShapeBase.NOT_SET:
                _params['max_concurrency'] = max_concurrency
            if max_errors is not ShapeBase.NOT_SET:
                _params['max_errors'] = max_errors
            _request = shapes.StartAutomationExecutionRequest(**_params)
        response = self._boto_client.start_automation_execution(
            **_request.to_boto()
        )

        return shapes.StartAutomationExecutionResult.from_boto(response)

    def start_session(
        self,
        _request: shapes.StartSessionRequest = None,
        *,
        target: str,
        document_name: str = ShapeBase.NOT_SET,
        parameters: typing.Dict[str, typing.List[str]] = ShapeBase.NOT_SET,
    ) -> shapes.StartSessionResponse:
        """
        Initiates a connection to a target (for example, an instance) for a Session
        Manager session. Returns a URL and token that can be used to open a WebSocket
        connection for sending input and receiving outputs.

        AWS CLI usage: `start-session` is an interactive command that requires the
        Session Manager plugin to be installed on the client machine making the call.
        For information, see [ Install the Session Manager Plugin for the AWS
        CLI](http://docs.aws.amazon.com/systems-manager/latest/userguide/session-
        manager-working-with-install-plugin.html) in the _AWS Systems Manager User
        Guide_.
        """
        if _request is None:
            _params = {}
            if target is not ShapeBase.NOT_SET:
                _params['target'] = target
            if document_name is not ShapeBase.NOT_SET:
                _params['document_name'] = document_name
            if parameters is not ShapeBase.NOT_SET:
                _params['parameters'] = parameters
            _request = shapes.StartSessionRequest(**_params)
        response = self._boto_client.start_session(**_request.to_boto())

        return shapes.StartSessionResponse.from_boto(response)

    def stop_automation_execution(
        self,
        _request: shapes.StopAutomationExecutionRequest = None,
        *,
        automation_execution_id: str,
        type: typing.Union[str, shapes.StopType] = ShapeBase.NOT_SET,
    ) -> shapes.StopAutomationExecutionResult:
        """
        Stop an Automation that is currently executing.
        """
        if _request is None:
            _params = {}
            if automation_execution_id is not ShapeBase.NOT_SET:
                _params['automation_execution_id'] = automation_execution_id
            if type is not ShapeBase.NOT_SET:
                _params['type'] = type
            _request = shapes.StopAutomationExecutionRequest(**_params)
        response = self._boto_client.stop_automation_execution(
            **_request.to_boto()
        )

        return shapes.StopAutomationExecutionResult.from_boto(response)

    def terminate_session(
        self,
        _request: shapes.TerminateSessionRequest = None,
        *,
        session_id: str,
    ) -> shapes.TerminateSessionResponse:
        """
        Permanently ends a session and closes the data connection between the Session
        Manager client and SSM Agent on the instance. A terminated session cannot be
        resumed.
        """
        if _request is None:
            _params = {}
            if session_id is not ShapeBase.NOT_SET:
                _params['session_id'] = session_id
            _request = shapes.TerminateSessionRequest(**_params)
        response = self._boto_client.terminate_session(**_request.to_boto())

        return shapes.TerminateSessionResponse.from_boto(response)

    def update_association(
        self,
        _request: shapes.UpdateAssociationRequest = None,
        *,
        association_id: str,
        parameters: typing.Dict[str, typing.List[str]] = ShapeBase.NOT_SET,
        document_version: str = ShapeBase.NOT_SET,
        schedule_expression: str = ShapeBase.NOT_SET,
        output_location: shapes.InstanceAssociationOutputLocation = ShapeBase.
        NOT_SET,
        name: str = ShapeBase.NOT_SET,
        targets: typing.List[shapes.Target] = ShapeBase.NOT_SET,
        association_name: str = ShapeBase.NOT_SET,
        association_version: str = ShapeBase.NOT_SET,
    ) -> shapes.UpdateAssociationResult:
        """
        Updates an association. You can update the association name and version, the
        document version, schedule, parameters, and Amazon S3 output.
        """
        if _request is None:
            _params = {}
            if association_id is not ShapeBase.NOT_SET:
                _params['association_id'] = association_id
            if parameters is not ShapeBase.NOT_SET:
                _params['parameters'] = parameters
            if document_version is not ShapeBase.NOT_SET:
                _params['document_version'] = document_version
            if schedule_expression is not ShapeBase.NOT_SET:
                _params['schedule_expression'] = schedule_expression
            if output_location is not ShapeBase.NOT_SET:
                _params['output_location'] = output_location
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if targets is not ShapeBase.NOT_SET:
                _params['targets'] = targets
            if association_name is not ShapeBase.NOT_SET:
                _params['association_name'] = association_name
            if association_version is not ShapeBase.NOT_SET:
                _params['association_version'] = association_version
            _request = shapes.UpdateAssociationRequest(**_params)
        response = self._boto_client.update_association(**_request.to_boto())

        return shapes.UpdateAssociationResult.from_boto(response)

    def update_association_status(
        self,
        _request: shapes.UpdateAssociationStatusRequest = None,
        *,
        name: str,
        instance_id: str,
        association_status: shapes.AssociationStatus,
    ) -> shapes.UpdateAssociationStatusResult:
        """
        Updates the status of the Systems Manager document associated with the specified
        instance.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if instance_id is not ShapeBase.NOT_SET:
                _params['instance_id'] = instance_id
            if association_status is not ShapeBase.NOT_SET:
                _params['association_status'] = association_status
            _request = shapes.UpdateAssociationStatusRequest(**_params)
        response = self._boto_client.update_association_status(
            **_request.to_boto()
        )

        return shapes.UpdateAssociationStatusResult.from_boto(response)

    def update_document(
        self,
        _request: shapes.UpdateDocumentRequest = None,
        *,
        content: str,
        name: str,
        document_version: str = ShapeBase.NOT_SET,
        document_format: typing.Union[str, shapes.DocumentFormat] = ShapeBase.
        NOT_SET,
        target_type: str = ShapeBase.NOT_SET,
    ) -> shapes.UpdateDocumentResult:
        """
        The document you want to update.
        """
        if _request is None:
            _params = {}
            if content is not ShapeBase.NOT_SET:
                _params['content'] = content
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if document_version is not ShapeBase.NOT_SET:
                _params['document_version'] = document_version
            if document_format is not ShapeBase.NOT_SET:
                _params['document_format'] = document_format
            if target_type is not ShapeBase.NOT_SET:
                _params['target_type'] = target_type
            _request = shapes.UpdateDocumentRequest(**_params)
        response = self._boto_client.update_document(**_request.to_boto())

        return shapes.UpdateDocumentResult.from_boto(response)

    def update_document_default_version(
        self,
        _request: shapes.UpdateDocumentDefaultVersionRequest = None,
        *,
        name: str,
        document_version: str,
    ) -> shapes.UpdateDocumentDefaultVersionResult:
        """
        Set the default version of a document.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if document_version is not ShapeBase.NOT_SET:
                _params['document_version'] = document_version
            _request = shapes.UpdateDocumentDefaultVersionRequest(**_params)
        response = self._boto_client.update_document_default_version(
            **_request.to_boto()
        )

        return shapes.UpdateDocumentDefaultVersionResult.from_boto(response)

    def update_maintenance_window(
        self,
        _request: shapes.UpdateMaintenanceWindowRequest = None,
        *,
        window_id: str,
        name: str = ShapeBase.NOT_SET,
        description: str = ShapeBase.NOT_SET,
        schedule: str = ShapeBase.NOT_SET,
        duration: int = ShapeBase.NOT_SET,
        cutoff: int = ShapeBase.NOT_SET,
        allow_unassociated_targets: bool = ShapeBase.NOT_SET,
        enabled: bool = ShapeBase.NOT_SET,
        replace: bool = ShapeBase.NOT_SET,
    ) -> shapes.UpdateMaintenanceWindowResult:
        """
        Updates an existing Maintenance Window. Only specified parameters are modified.
        """
        if _request is None:
            _params = {}
            if window_id is not ShapeBase.NOT_SET:
                _params['window_id'] = window_id
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if schedule is not ShapeBase.NOT_SET:
                _params['schedule'] = schedule
            if duration is not ShapeBase.NOT_SET:
                _params['duration'] = duration
            if cutoff is not ShapeBase.NOT_SET:
                _params['cutoff'] = cutoff
            if allow_unassociated_targets is not ShapeBase.NOT_SET:
                _params['allow_unassociated_targets'
                       ] = allow_unassociated_targets
            if enabled is not ShapeBase.NOT_SET:
                _params['enabled'] = enabled
            if replace is not ShapeBase.NOT_SET:
                _params['replace'] = replace
            _request = shapes.UpdateMaintenanceWindowRequest(**_params)
        response = self._boto_client.update_maintenance_window(
            **_request.to_boto()
        )

        return shapes.UpdateMaintenanceWindowResult.from_boto(response)

    def update_maintenance_window_target(
        self,
        _request: shapes.UpdateMaintenanceWindowTargetRequest = None,
        *,
        window_id: str,
        window_target_id: str,
        targets: typing.List[shapes.Target] = ShapeBase.NOT_SET,
        owner_information: str = ShapeBase.NOT_SET,
        name: str = ShapeBase.NOT_SET,
        description: str = ShapeBase.NOT_SET,
        replace: bool = ShapeBase.NOT_SET,
    ) -> shapes.UpdateMaintenanceWindowTargetResult:
        """
        Modifies the target of an existing Maintenance Window. You can't change the
        target type, but you can change the following:

        The target from being an ID target to a Tag target, or a Tag target to an ID
        target.

        IDs for an ID target.

        Tags for a Tag target.

        Owner.

        Name.

        Description.

        If a parameter is null, then the corresponding field is not modified.
        """
        if _request is None:
            _params = {}
            if window_id is not ShapeBase.NOT_SET:
                _params['window_id'] = window_id
            if window_target_id is not ShapeBase.NOT_SET:
                _params['window_target_id'] = window_target_id
            if targets is not ShapeBase.NOT_SET:
                _params['targets'] = targets
            if owner_information is not ShapeBase.NOT_SET:
                _params['owner_information'] = owner_information
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if replace is not ShapeBase.NOT_SET:
                _params['replace'] = replace
            _request = shapes.UpdateMaintenanceWindowTargetRequest(**_params)
        response = self._boto_client.update_maintenance_window_target(
            **_request.to_boto()
        )

        return shapes.UpdateMaintenanceWindowTargetResult.from_boto(response)

    def update_maintenance_window_task(
        self,
        _request: shapes.UpdateMaintenanceWindowTaskRequest = None,
        *,
        window_id: str,
        window_task_id: str,
        targets: typing.List[shapes.Target] = ShapeBase.NOT_SET,
        task_arn: str = ShapeBase.NOT_SET,
        service_role_arn: str = ShapeBase.NOT_SET,
        task_parameters: typing.
        Dict[str, shapes.
             MaintenanceWindowTaskParameterValueExpression] = ShapeBase.NOT_SET,
        task_invocation_parameters: shapes.
        MaintenanceWindowTaskInvocationParameters = ShapeBase.NOT_SET,
        priority: int = ShapeBase.NOT_SET,
        max_concurrency: str = ShapeBase.NOT_SET,
        max_errors: str = ShapeBase.NOT_SET,
        logging_info: shapes.LoggingInfo = ShapeBase.NOT_SET,
        name: str = ShapeBase.NOT_SET,
        description: str = ShapeBase.NOT_SET,
        replace: bool = ShapeBase.NOT_SET,
    ) -> shapes.UpdateMaintenanceWindowTaskResult:
        """
        Modifies a task assigned to a Maintenance Window. You can't change the task
        type, but you can change the following values:

          * TaskARN. For example, you can change a RUN_COMMAND task from AWS-RunPowerShellScript to AWS-RunShellScript.

          * ServiceRoleArn

          * TaskInvocationParameters

          * Priority

          * MaxConcurrency

          * MaxErrors

        If a parameter is null, then the corresponding field is not modified. Also, if
        you set Replace to true, then all fields required by the
        RegisterTaskWithMaintenanceWindow action are required for this request. Optional
        fields that aren't specified are set to null.
        """
        if _request is None:
            _params = {}
            if window_id is not ShapeBase.NOT_SET:
                _params['window_id'] = window_id
            if window_task_id is not ShapeBase.NOT_SET:
                _params['window_task_id'] = window_task_id
            if targets is not ShapeBase.NOT_SET:
                _params['targets'] = targets
            if task_arn is not ShapeBase.NOT_SET:
                _params['task_arn'] = task_arn
            if service_role_arn is not ShapeBase.NOT_SET:
                _params['service_role_arn'] = service_role_arn
            if task_parameters is not ShapeBase.NOT_SET:
                _params['task_parameters'] = task_parameters
            if task_invocation_parameters is not ShapeBase.NOT_SET:
                _params['task_invocation_parameters'
                       ] = task_invocation_parameters
            if priority is not ShapeBase.NOT_SET:
                _params['priority'] = priority
            if max_concurrency is not ShapeBase.NOT_SET:
                _params['max_concurrency'] = max_concurrency
            if max_errors is not ShapeBase.NOT_SET:
                _params['max_errors'] = max_errors
            if logging_info is not ShapeBase.NOT_SET:
                _params['logging_info'] = logging_info
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if replace is not ShapeBase.NOT_SET:
                _params['replace'] = replace
            _request = shapes.UpdateMaintenanceWindowTaskRequest(**_params)
        response = self._boto_client.update_maintenance_window_task(
            **_request.to_boto()
        )

        return shapes.UpdateMaintenanceWindowTaskResult.from_boto(response)

    def update_managed_instance_role(
        self,
        _request: shapes.UpdateManagedInstanceRoleRequest = None,
        *,
        instance_id: str,
        iam_role: str,
    ) -> shapes.UpdateManagedInstanceRoleResult:
        """
        Assigns or changes an Amazon Identity and Access Management (IAM) role to the
        managed instance.
        """
        if _request is None:
            _params = {}
            if instance_id is not ShapeBase.NOT_SET:
                _params['instance_id'] = instance_id
            if iam_role is not ShapeBase.NOT_SET:
                _params['iam_role'] = iam_role
            _request = shapes.UpdateManagedInstanceRoleRequest(**_params)
        response = self._boto_client.update_managed_instance_role(
            **_request.to_boto()
        )

        return shapes.UpdateManagedInstanceRoleResult.from_boto(response)

    def update_patch_baseline(
        self,
        _request: shapes.UpdatePatchBaselineRequest = None,
        *,
        baseline_id: str,
        name: str = ShapeBase.NOT_SET,
        global_filters: shapes.PatchFilterGroup = ShapeBase.NOT_SET,
        approval_rules: shapes.PatchRuleGroup = ShapeBase.NOT_SET,
        approved_patches: typing.List[str] = ShapeBase.NOT_SET,
        approved_patches_compliance_level: typing.
        Union[str, shapes.PatchComplianceLevel] = ShapeBase.NOT_SET,
        approved_patches_enable_non_security: bool = ShapeBase.NOT_SET,
        rejected_patches: typing.List[str] = ShapeBase.NOT_SET,
        description: str = ShapeBase.NOT_SET,
        sources: typing.List[shapes.PatchSource] = ShapeBase.NOT_SET,
        replace: bool = ShapeBase.NOT_SET,
    ) -> shapes.UpdatePatchBaselineResult:
        """
        Modifies an existing patch baseline. Fields not specified in the request are
        left unchanged.

        For information about valid key and value pairs in `PatchFilters` for each
        supported operating system type, see
        [PatchFilter](http://docs.aws.amazon.com/systems-
        manager/latest/APIReference/API_PatchFilter.html).
        """
        if _request is None:
            _params = {}
            if baseline_id is not ShapeBase.NOT_SET:
                _params['baseline_id'] = baseline_id
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if global_filters is not ShapeBase.NOT_SET:
                _params['global_filters'] = global_filters
            if approval_rules is not ShapeBase.NOT_SET:
                _params['approval_rules'] = approval_rules
            if approved_patches is not ShapeBase.NOT_SET:
                _params['approved_patches'] = approved_patches
            if approved_patches_compliance_level is not ShapeBase.NOT_SET:
                _params['approved_patches_compliance_level'
                       ] = approved_patches_compliance_level
            if approved_patches_enable_non_security is not ShapeBase.NOT_SET:
                _params['approved_patches_enable_non_security'
                       ] = approved_patches_enable_non_security
            if rejected_patches is not ShapeBase.NOT_SET:
                _params['rejected_patches'] = rejected_patches
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if sources is not ShapeBase.NOT_SET:
                _params['sources'] = sources
            if replace is not ShapeBase.NOT_SET:
                _params['replace'] = replace
            _request = shapes.UpdatePatchBaselineRequest(**_params)
        response = self._boto_client.update_patch_baseline(**_request.to_boto())

        return shapes.UpdatePatchBaselineResult.from_boto(response)
