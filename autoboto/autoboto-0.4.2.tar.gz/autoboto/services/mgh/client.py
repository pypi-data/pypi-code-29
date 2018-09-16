import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("mgh", *args, **kwargs)

    def associate_created_artifact(
        self,
        _request: shapes.AssociateCreatedArtifactRequest = None,
        *,
        progress_update_stream: str,
        migration_task_name: str,
        created_artifact: shapes.CreatedArtifact,
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> shapes.AssociateCreatedArtifactResult:
        """
        Associates a created artifact of an AWS cloud resource, the target receiving the
        migration, with the migration task performed by a migration tool. This API has
        the following traits:

          * Migration tools can call the `AssociateCreatedArtifact` operation to indicate which AWS artifact is associated with a migration task.

          * The created artifact name must be provided in ARN (Amazon Resource Name) format which will contain information about type and region; for example: `arn:aws:ec2:us-east-1:488216288981:image/ami-6d0ba87b`.

          * Examples of the AWS resource behind the created artifact are, AMI's, EC2 instance, or DMS endpoint, etc.
        """
        if _request is None:
            _params = {}
            if progress_update_stream is not ShapeBase.NOT_SET:
                _params['progress_update_stream'] = progress_update_stream
            if migration_task_name is not ShapeBase.NOT_SET:
                _params['migration_task_name'] = migration_task_name
            if created_artifact is not ShapeBase.NOT_SET:
                _params['created_artifact'] = created_artifact
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.AssociateCreatedArtifactRequest(**_params)
        response = self._boto_client.associate_created_artifact(
            **_request.to_boto()
        )

        return shapes.AssociateCreatedArtifactResult.from_boto(response)

    def associate_discovered_resource(
        self,
        _request: shapes.AssociateDiscoveredResourceRequest = None,
        *,
        progress_update_stream: str,
        migration_task_name: str,
        discovered_resource: shapes.DiscoveredResource,
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> shapes.AssociateDiscoveredResourceResult:
        """
        Associates a discovered resource ID from Application Discovery Service (ADS)
        with a migration task.
        """
        if _request is None:
            _params = {}
            if progress_update_stream is not ShapeBase.NOT_SET:
                _params['progress_update_stream'] = progress_update_stream
            if migration_task_name is not ShapeBase.NOT_SET:
                _params['migration_task_name'] = migration_task_name
            if discovered_resource is not ShapeBase.NOT_SET:
                _params['discovered_resource'] = discovered_resource
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.AssociateDiscoveredResourceRequest(**_params)
        response = self._boto_client.associate_discovered_resource(
            **_request.to_boto()
        )

        return shapes.AssociateDiscoveredResourceResult.from_boto(response)

    def create_progress_update_stream(
        self,
        _request: shapes.CreateProgressUpdateStreamRequest = None,
        *,
        progress_update_stream_name: str,
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> shapes.CreateProgressUpdateStreamResult:
        """
        Creates a progress update stream which is an AWS resource used for access
        control as well as a namespace for migration task names that is implicitly
        linked to your AWS account. It must uniquely identify the migration tool as it
        is used for all updates made by the tool; however, it does not need to be unique
        for each AWS account because it is scoped to the AWS account.
        """
        if _request is None:
            _params = {}
            if progress_update_stream_name is not ShapeBase.NOT_SET:
                _params['progress_update_stream_name'
                       ] = progress_update_stream_name
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.CreateProgressUpdateStreamRequest(**_params)
        response = self._boto_client.create_progress_update_stream(
            **_request.to_boto()
        )

        return shapes.CreateProgressUpdateStreamResult.from_boto(response)

    def delete_progress_update_stream(
        self,
        _request: shapes.DeleteProgressUpdateStreamRequest = None,
        *,
        progress_update_stream_name: str,
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> shapes.DeleteProgressUpdateStreamResult:
        """
        Deletes a progress update stream, including all of its tasks, which was
        previously created as an AWS resource used for access control. This API has the
        following traits:

          * The only parameter needed for `DeleteProgressUpdateStream` is the stream name (same as a `CreateProgressUpdateStream` call).

          * The call will return, and a background process will asynchronously delete the stream and all of its resources (tasks, associated resources, resource attributes, created artifacts).

          * If the stream takes time to be deleted, it might still show up on a `ListProgressUpdateStreams` call.

          * `CreateProgressUpdateStream`, `ImportMigrationTask`, `NotifyMigrationTaskState`, and all Associate[*] APIs realted to the tasks belonging to the stream will throw "InvalidInputException" if the stream of the same name is in the process of being deleted.

          * Once the stream and all of its resources are deleted, `CreateProgressUpdateStream` for a stream of the same name will succeed, and that stream will be an entirely new logical resource (without any resources associated with the old stream).
        """
        if _request is None:
            _params = {}
            if progress_update_stream_name is not ShapeBase.NOT_SET:
                _params['progress_update_stream_name'
                       ] = progress_update_stream_name
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.DeleteProgressUpdateStreamRequest(**_params)
        response = self._boto_client.delete_progress_update_stream(
            **_request.to_boto()
        )

        return shapes.DeleteProgressUpdateStreamResult.from_boto(response)

    def describe_application_state(
        self,
        _request: shapes.DescribeApplicationStateRequest = None,
        *,
        application_id: str,
    ) -> shapes.DescribeApplicationStateResult:
        """
        Gets the migration status of an application.
        """
        if _request is None:
            _params = {}
            if application_id is not ShapeBase.NOT_SET:
                _params['application_id'] = application_id
            _request = shapes.DescribeApplicationStateRequest(**_params)
        response = self._boto_client.describe_application_state(
            **_request.to_boto()
        )

        return shapes.DescribeApplicationStateResult.from_boto(response)

    def describe_migration_task(
        self,
        _request: shapes.DescribeMigrationTaskRequest = None,
        *,
        progress_update_stream: str,
        migration_task_name: str,
    ) -> shapes.DescribeMigrationTaskResult:
        """
        Retrieves a list of all attributes associated with a specific migration task.
        """
        if _request is None:
            _params = {}
            if progress_update_stream is not ShapeBase.NOT_SET:
                _params['progress_update_stream'] = progress_update_stream
            if migration_task_name is not ShapeBase.NOT_SET:
                _params['migration_task_name'] = migration_task_name
            _request = shapes.DescribeMigrationTaskRequest(**_params)
        response = self._boto_client.describe_migration_task(
            **_request.to_boto()
        )

        return shapes.DescribeMigrationTaskResult.from_boto(response)

    def disassociate_created_artifact(
        self,
        _request: shapes.DisassociateCreatedArtifactRequest = None,
        *,
        progress_update_stream: str,
        migration_task_name: str,
        created_artifact_name: str,
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> shapes.DisassociateCreatedArtifactResult:
        """
        Disassociates a created artifact of an AWS resource with a migration task
        performed by a migration tool that was previously associated. This API has the
        following traits:

          * A migration user can call the `DisassociateCreatedArtifacts` operation to disassociate a created AWS Artifact from a migration task.

          * The created artifact name must be provided in ARN (Amazon Resource Name) format which will contain information about type and region; for example: `arn:aws:ec2:us-east-1:488216288981:image/ami-6d0ba87b`.

          * Examples of the AWS resource behind the created artifact are, AMI's, EC2 instance, or RDS instance, etc.
        """
        if _request is None:
            _params = {}
            if progress_update_stream is not ShapeBase.NOT_SET:
                _params['progress_update_stream'] = progress_update_stream
            if migration_task_name is not ShapeBase.NOT_SET:
                _params['migration_task_name'] = migration_task_name
            if created_artifact_name is not ShapeBase.NOT_SET:
                _params['created_artifact_name'] = created_artifact_name
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.DisassociateCreatedArtifactRequest(**_params)
        response = self._boto_client.disassociate_created_artifact(
            **_request.to_boto()
        )

        return shapes.DisassociateCreatedArtifactResult.from_boto(response)

    def disassociate_discovered_resource(
        self,
        _request: shapes.DisassociateDiscoveredResourceRequest = None,
        *,
        progress_update_stream: str,
        migration_task_name: str,
        configuration_id: str,
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> shapes.DisassociateDiscoveredResourceResult:
        """
        Disassociate an Application Discovery Service (ADS) discovered resource from a
        migration task.
        """
        if _request is None:
            _params = {}
            if progress_update_stream is not ShapeBase.NOT_SET:
                _params['progress_update_stream'] = progress_update_stream
            if migration_task_name is not ShapeBase.NOT_SET:
                _params['migration_task_name'] = migration_task_name
            if configuration_id is not ShapeBase.NOT_SET:
                _params['configuration_id'] = configuration_id
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.DisassociateDiscoveredResourceRequest(**_params)
        response = self._boto_client.disassociate_discovered_resource(
            **_request.to_boto()
        )

        return shapes.DisassociateDiscoveredResourceResult.from_boto(response)

    def import_migration_task(
        self,
        _request: shapes.ImportMigrationTaskRequest = None,
        *,
        progress_update_stream: str,
        migration_task_name: str,
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> shapes.ImportMigrationTaskResult:
        """
        Registers a new migration task which represents a server, database, etc., being
        migrated to AWS by a migration tool.

        This API is a prerequisite to calling the `NotifyMigrationTaskState` API as the
        migration tool must first register the migration task with Migration Hub.
        """
        if _request is None:
            _params = {}
            if progress_update_stream is not ShapeBase.NOT_SET:
                _params['progress_update_stream'] = progress_update_stream
            if migration_task_name is not ShapeBase.NOT_SET:
                _params['migration_task_name'] = migration_task_name
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.ImportMigrationTaskRequest(**_params)
        response = self._boto_client.import_migration_task(**_request.to_boto())

        return shapes.ImportMigrationTaskResult.from_boto(response)

    def list_created_artifacts(
        self,
        _request: shapes.ListCreatedArtifactsRequest = None,
        *,
        progress_update_stream: str,
        migration_task_name: str,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.ListCreatedArtifactsResult:
        """
        Lists the created artifacts attached to a given migration task in an update
        stream. This API has the following traits:

          * Gets the list of the created artifacts while migration is taking place.

          * Shows the artifacts created by the migration tool that was associated by the `AssociateCreatedArtifact` API. 

          * Lists created artifacts in a paginated interface.
        """
        if _request is None:
            _params = {}
            if progress_update_stream is not ShapeBase.NOT_SET:
                _params['progress_update_stream'] = progress_update_stream
            if migration_task_name is not ShapeBase.NOT_SET:
                _params['migration_task_name'] = migration_task_name
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.ListCreatedArtifactsRequest(**_params)
        response = self._boto_client.list_created_artifacts(
            **_request.to_boto()
        )

        return shapes.ListCreatedArtifactsResult.from_boto(response)

    def list_discovered_resources(
        self,
        _request: shapes.ListDiscoveredResourcesRequest = None,
        *,
        progress_update_stream: str,
        migration_task_name: str,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.ListDiscoveredResourcesResult:
        """
        Lists discovered resources associated with the given `MigrationTask`.
        """
        if _request is None:
            _params = {}
            if progress_update_stream is not ShapeBase.NOT_SET:
                _params['progress_update_stream'] = progress_update_stream
            if migration_task_name is not ShapeBase.NOT_SET:
                _params['migration_task_name'] = migration_task_name
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.ListDiscoveredResourcesRequest(**_params)
        response = self._boto_client.list_discovered_resources(
            **_request.to_boto()
        )

        return shapes.ListDiscoveredResourcesResult.from_boto(response)

    def list_migration_tasks(
        self,
        _request: shapes.ListMigrationTasksRequest = None,
        *,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        resource_name: str = ShapeBase.NOT_SET,
    ) -> shapes.ListMigrationTasksResult:
        """
        Lists all, or filtered by resource name, migration tasks associated with the
        user account making this call. This API has the following traits:

          * Can show a summary list of the most recent migration tasks.

          * Can show a summary list of migration tasks associated with a given discovered resource.

          * Lists migration tasks in a paginated interface.
        """
        if _request is None:
            _params = {}
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if resource_name is not ShapeBase.NOT_SET:
                _params['resource_name'] = resource_name
            _request = shapes.ListMigrationTasksRequest(**_params)
        response = self._boto_client.list_migration_tasks(**_request.to_boto())

        return shapes.ListMigrationTasksResult.from_boto(response)

    def list_progress_update_streams(
        self,
        _request: shapes.ListProgressUpdateStreamsRequest = None,
        *,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.ListProgressUpdateStreamsResult:
        """
        Lists progress update streams associated with the user account making this call.
        """
        if _request is None:
            _params = {}
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.ListProgressUpdateStreamsRequest(**_params)
        response = self._boto_client.list_progress_update_streams(
            **_request.to_boto()
        )

        return shapes.ListProgressUpdateStreamsResult.from_boto(response)

    def notify_application_state(
        self,
        _request: shapes.NotifyApplicationStateRequest = None,
        *,
        application_id: str,
        status: typing.Union[str, shapes.ApplicationStatus],
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> shapes.NotifyApplicationStateResult:
        """
        Sets the migration state of an application. For a given application identified
        by the value passed to `ApplicationId`, its status is set or updated by passing
        one of three values to `Status`: `NOT_STARTED | IN_PROGRESS | COMPLETED`.
        """
        if _request is None:
            _params = {}
            if application_id is not ShapeBase.NOT_SET:
                _params['application_id'] = application_id
            if status is not ShapeBase.NOT_SET:
                _params['status'] = status
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.NotifyApplicationStateRequest(**_params)
        response = self._boto_client.notify_application_state(
            **_request.to_boto()
        )

        return shapes.NotifyApplicationStateResult.from_boto(response)

    def notify_migration_task_state(
        self,
        _request: shapes.NotifyMigrationTaskStateRequest = None,
        *,
        progress_update_stream: str,
        migration_task_name: str,
        task: shapes.Task,
        update_date_time: datetime.datetime,
        next_update_seconds: int,
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> shapes.NotifyMigrationTaskStateResult:
        """
        Notifies Migration Hub of the current status, progress, or other detail
        regarding a migration task. This API has the following traits:

          * Migration tools will call the `NotifyMigrationTaskState` API to share the latest progress and status.

          * `MigrationTaskName` is used for addressing updates to the correct target.

          * `ProgressUpdateStream` is used for access control and to provide a namespace for each migration tool.
        """
        if _request is None:
            _params = {}
            if progress_update_stream is not ShapeBase.NOT_SET:
                _params['progress_update_stream'] = progress_update_stream
            if migration_task_name is not ShapeBase.NOT_SET:
                _params['migration_task_name'] = migration_task_name
            if task is not ShapeBase.NOT_SET:
                _params['task'] = task
            if update_date_time is not ShapeBase.NOT_SET:
                _params['update_date_time'] = update_date_time
            if next_update_seconds is not ShapeBase.NOT_SET:
                _params['next_update_seconds'] = next_update_seconds
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.NotifyMigrationTaskStateRequest(**_params)
        response = self._boto_client.notify_migration_task_state(
            **_request.to_boto()
        )

        return shapes.NotifyMigrationTaskStateResult.from_boto(response)

    def put_resource_attributes(
        self,
        _request: shapes.PutResourceAttributesRequest = None,
        *,
        progress_update_stream: str,
        migration_task_name: str,
        resource_attribute_list: typing.List[shapes.ResourceAttribute],
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> shapes.PutResourceAttributesResult:
        """
        Provides identifying details of the resource being migrated so that it can be
        associated in the Application Discovery Service (ADS)'s repository. This
        association occurs asynchronously after `PutResourceAttributes` returns.

          * Keep in mind that subsequent calls to PutResourceAttributes will override previously stored attributes. For example, if it is first called with a MAC address, but later, it is desired to _add_ an IP address, it will then be required to call it with _both_ the IP and MAC addresses to prevent overiding the MAC address.

          * Note the instructions regarding the special use case of the [ `ResourceAttributeList` ](https://docs.aws.amazon.com/migrationhub/latest/ug/API_PutResourceAttributes.html#migrationhub-PutResourceAttributes-request-ResourceAttributeList) parameter when specifying any "VM" related value. 

        Because this is an asynchronous call, it will always return 200, whether an
        association occurs or not. To confirm if an association was found based on the
        provided details, call `ListDiscoveredResources`.
        """
        if _request is None:
            _params = {}
            if progress_update_stream is not ShapeBase.NOT_SET:
                _params['progress_update_stream'] = progress_update_stream
            if migration_task_name is not ShapeBase.NOT_SET:
                _params['migration_task_name'] = migration_task_name
            if resource_attribute_list is not ShapeBase.NOT_SET:
                _params['resource_attribute_list'] = resource_attribute_list
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.PutResourceAttributesRequest(**_params)
        response = self._boto_client.put_resource_attributes(
            **_request.to_boto()
        )

        return shapes.PutResourceAttributesResult.from_boto(response)
