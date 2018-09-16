import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("sms", *args, **kwargs)

    def create_replication_job(
        self,
        _request: shapes.CreateReplicationJobRequest = None,
        *,
        server_id: str,
        seed_replication_time: datetime.datetime,
        frequency: int,
        license_type: typing.Union[str, shapes.LicenseType] = ShapeBase.NOT_SET,
        role_name: str = ShapeBase.NOT_SET,
        description: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateReplicationJobResponse:
        """
        The CreateReplicationJob API is used to create a ReplicationJob to replicate a
        server on AWS. Call this API to first create a ReplicationJob, which will then
        schedule periodic ReplicationRuns to replicate your server to AWS. Each
        ReplicationRun will result in the creation of an AWS AMI.
        """
        if _request is None:
            _params = {}
            if server_id is not ShapeBase.NOT_SET:
                _params['server_id'] = server_id
            if seed_replication_time is not ShapeBase.NOT_SET:
                _params['seed_replication_time'] = seed_replication_time
            if frequency is not ShapeBase.NOT_SET:
                _params['frequency'] = frequency
            if license_type is not ShapeBase.NOT_SET:
                _params['license_type'] = license_type
            if role_name is not ShapeBase.NOT_SET:
                _params['role_name'] = role_name
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            _request = shapes.CreateReplicationJobRequest(**_params)
        response = self._boto_client.create_replication_job(
            **_request.to_boto()
        )

        return shapes.CreateReplicationJobResponse.from_boto(response)

    def delete_replication_job(
        self,
        _request: shapes.DeleteReplicationJobRequest = None,
        *,
        replication_job_id: str,
    ) -> shapes.DeleteReplicationJobResponse:
        """
        The DeleteReplicationJob API is used to delete a ReplicationJob, resulting in no
        further ReplicationRuns. This will delete the contents of the S3 bucket used to
        store SMS artifacts, but will not delete any AMIs created by the SMS service.
        """
        if _request is None:
            _params = {}
            if replication_job_id is not ShapeBase.NOT_SET:
                _params['replication_job_id'] = replication_job_id
            _request = shapes.DeleteReplicationJobRequest(**_params)
        response = self._boto_client.delete_replication_job(
            **_request.to_boto()
        )

        return shapes.DeleteReplicationJobResponse.from_boto(response)

    def delete_server_catalog(
        self,
        _request: shapes.DeleteServerCatalogRequest = None,
    ) -> shapes.DeleteServerCatalogResponse:
        """
        The DeleteServerCatalog API clears all servers from your server catalog. This
        means that these servers will no longer be accessible to the Server Migration
        Service.
        """
        if _request is None:
            _params = {}
            _request = shapes.DeleteServerCatalogRequest(**_params)
        response = self._boto_client.delete_server_catalog(**_request.to_boto())

        return shapes.DeleteServerCatalogResponse.from_boto(response)

    def disassociate_connector(
        self,
        _request: shapes.DisassociateConnectorRequest = None,
        *,
        connector_id: str,
    ) -> shapes.DisassociateConnectorResponse:
        """
        The DisassociateConnector API will disassociate a connector from the Server
        Migration Service, rendering it unavailable to support replication jobs.
        """
        if _request is None:
            _params = {}
            if connector_id is not ShapeBase.NOT_SET:
                _params['connector_id'] = connector_id
            _request = shapes.DisassociateConnectorRequest(**_params)
        response = self._boto_client.disassociate_connector(
            **_request.to_boto()
        )

        return shapes.DisassociateConnectorResponse.from_boto(response)

    def get_connectors(
        self,
        _request: shapes.GetConnectorsRequest = None,
        *,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.GetConnectorsResponse:
        """
        The GetConnectors API returns a list of connectors that are registered with the
        Server Migration Service.
        """
        if _request is None:
            _params = {}
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.GetConnectorsRequest(**_params)
        paginator = self.get_paginator("get_connectors").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.GetConnectorsResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.GetConnectorsResponse.from_boto(response)

    def get_replication_jobs(
        self,
        _request: shapes.GetReplicationJobsRequest = None,
        *,
        replication_job_id: str = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.GetReplicationJobsResponse:
        """
        The GetReplicationJobs API will return all of your ReplicationJobs and their
        details. This API returns a paginated list, that may be consecutively called
        with nextToken to retrieve all ReplicationJobs.
        """
        if _request is None:
            _params = {}
            if replication_job_id is not ShapeBase.NOT_SET:
                _params['replication_job_id'] = replication_job_id
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.GetReplicationJobsRequest(**_params)
        paginator = self.get_paginator("get_replication_jobs").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.GetReplicationJobsResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.GetReplicationJobsResponse.from_boto(response)

    def get_replication_runs(
        self,
        _request: shapes.GetReplicationRunsRequest = None,
        *,
        replication_job_id: str,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.GetReplicationRunsResponse:
        """
        The GetReplicationRuns API will return all ReplicationRuns for a given
        ReplicationJob. This API returns a paginated list, that may be consecutively
        called with nextToken to retrieve all ReplicationRuns for a ReplicationJob.
        """
        if _request is None:
            _params = {}
            if replication_job_id is not ShapeBase.NOT_SET:
                _params['replication_job_id'] = replication_job_id
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.GetReplicationRunsRequest(**_params)
        paginator = self.get_paginator("get_replication_runs").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.GetReplicationRunsResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.GetReplicationRunsResponse.from_boto(response)

    def get_servers(
        self,
        _request: shapes.GetServersRequest = None,
        *,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.GetServersResponse:
        """
        The GetServers API returns a list of all servers in your server catalog. For
        this call to succeed, you must previously have called ImportServerCatalog.
        """
        if _request is None:
            _params = {}
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.GetServersRequest(**_params)
        paginator = self.get_paginator("get_servers").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.GetServersResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.GetServersResponse.from_boto(response)

    def import_server_catalog(
        self,
        _request: shapes.ImportServerCatalogRequest = None,
    ) -> shapes.ImportServerCatalogResponse:
        """
        The ImportServerCatalog API is used to gather the complete list of on-premises
        servers on your premises. This API call requires connectors to be installed and
        monitoring all servers you would like imported. This API call returns
        immediately, but may take some time to retrieve all of the servers.
        """
        if _request is None:
            _params = {}
            _request = shapes.ImportServerCatalogRequest(**_params)
        response = self._boto_client.import_server_catalog(**_request.to_boto())

        return shapes.ImportServerCatalogResponse.from_boto(response)

    def start_on_demand_replication_run(
        self,
        _request: shapes.StartOnDemandReplicationRunRequest = None,
        *,
        replication_job_id: str,
        description: str = ShapeBase.NOT_SET,
    ) -> shapes.StartOnDemandReplicationRunResponse:
        """
        The StartOnDemandReplicationRun API is used to start a ReplicationRun on demand
        (in addition to those that are scheduled based on your frequency). This
        ReplicationRun will start immediately. StartOnDemandReplicationRun is subject to
        limits on how many on demand ReplicationRuns you may call per 24-hour period.
        """
        if _request is None:
            _params = {}
            if replication_job_id is not ShapeBase.NOT_SET:
                _params['replication_job_id'] = replication_job_id
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            _request = shapes.StartOnDemandReplicationRunRequest(**_params)
        response = self._boto_client.start_on_demand_replication_run(
            **_request.to_boto()
        )

        return shapes.StartOnDemandReplicationRunResponse.from_boto(response)

    def update_replication_job(
        self,
        _request: shapes.UpdateReplicationJobRequest = None,
        *,
        replication_job_id: str,
        frequency: int = ShapeBase.NOT_SET,
        next_replication_run_start_time: datetime.datetime = ShapeBase.NOT_SET,
        license_type: typing.Union[str, shapes.LicenseType] = ShapeBase.NOT_SET,
        role_name: str = ShapeBase.NOT_SET,
        description: str = ShapeBase.NOT_SET,
    ) -> shapes.UpdateReplicationJobResponse:
        """
        The UpdateReplicationJob API is used to change the settings of your existing
        ReplicationJob created using CreateReplicationJob. Calling this API will affect
        the next scheduled ReplicationRun.
        """
        if _request is None:
            _params = {}
            if replication_job_id is not ShapeBase.NOT_SET:
                _params['replication_job_id'] = replication_job_id
            if frequency is not ShapeBase.NOT_SET:
                _params['frequency'] = frequency
            if next_replication_run_start_time is not ShapeBase.NOT_SET:
                _params['next_replication_run_start_time'
                       ] = next_replication_run_start_time
            if license_type is not ShapeBase.NOT_SET:
                _params['license_type'] = license_type
            if role_name is not ShapeBase.NOT_SET:
                _params['role_name'] = role_name
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            _request = shapes.UpdateReplicationJobRequest(**_params)
        response = self._boto_client.update_replication_job(
            **_request.to_boto()
        )

        return shapes.UpdateReplicationJobResponse.from_boto(response)
