import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("pinpoint", *args, **kwargs)

    def create_app(
        self,
        _request: shapes.CreateAppRequest = None,
        *,
        create_application_request: shapes.CreateApplicationRequest,
    ) -> shapes.CreateAppResponse:
        """
        Creates or updates an app.
        """
        if _request is None:
            _params = {}
            if create_application_request is not ShapeBase.NOT_SET:
                _params['create_application_request'
                       ] = create_application_request
            _request = shapes.CreateAppRequest(**_params)
        response = self._boto_client.create_app(**_request.to_boto())

        return shapes.CreateAppResponse.from_boto(response)

    def create_campaign(
        self,
        _request: shapes.CreateCampaignRequest = None,
        *,
        application_id: str,
        write_campaign_request: shapes.WriteCampaignRequest,
    ) -> shapes.CreateCampaignResponse:
        """
        Creates or updates a campaign.
        """
        if _request is None:
            _params = {}
            if application_id is not ShapeBase.NOT_SET:
                _params['application_id'] = application_id
            if write_campaign_request is not ShapeBase.NOT_SET:
                _params['write_campaign_request'] = write_campaign_request
            _request = shapes.CreateCampaignRequest(**_params)
        response = self._boto_client.create_campaign(**_request.to_boto())

        return shapes.CreateCampaignResponse.from_boto(response)

    def create_export_job(
        self,
        _request: shapes.CreateExportJobRequest = None,
        *,
        application_id: str,
        export_job_request: shapes.ExportJobRequest,
    ) -> shapes.CreateExportJobResponse:
        """
        Creates an export job.
        """
        if _request is None:
            _params = {}
            if application_id is not ShapeBase.NOT_SET:
                _params['application_id'] = application_id
            if export_job_request is not ShapeBase.NOT_SET:
                _params['export_job_request'] = export_job_request
            _request = shapes.CreateExportJobRequest(**_params)
        response = self._boto_client.create_export_job(**_request.to_boto())

        return shapes.CreateExportJobResponse.from_boto(response)

    def create_import_job(
        self,
        _request: shapes.CreateImportJobRequest = None,
        *,
        application_id: str,
        import_job_request: shapes.ImportJobRequest,
    ) -> shapes.CreateImportJobResponse:
        """
        Creates or updates an import job.
        """
        if _request is None:
            _params = {}
            if application_id is not ShapeBase.NOT_SET:
                _params['application_id'] = application_id
            if import_job_request is not ShapeBase.NOT_SET:
                _params['import_job_request'] = import_job_request
            _request = shapes.CreateImportJobRequest(**_params)
        response = self._boto_client.create_import_job(**_request.to_boto())

        return shapes.CreateImportJobResponse.from_boto(response)

    def create_segment(
        self,
        _request: shapes.CreateSegmentRequest = None,
        *,
        application_id: str,
        write_segment_request: shapes.WriteSegmentRequest,
    ) -> shapes.CreateSegmentResponse:
        """
        Used to create or update a segment.
        """
        if _request is None:
            _params = {}
            if application_id is not ShapeBase.NOT_SET:
                _params['application_id'] = application_id
            if write_segment_request is not ShapeBase.NOT_SET:
                _params['write_segment_request'] = write_segment_request
            _request = shapes.CreateSegmentRequest(**_params)
        response = self._boto_client.create_segment(**_request.to_boto())

        return shapes.CreateSegmentResponse.from_boto(response)

    def delete_adm_channel(
        self,
        _request: shapes.DeleteAdmChannelRequest = None,
        *,
        application_id: str,
    ) -> shapes.DeleteAdmChannelResponse:
        """
        Delete an ADM channel.
        """
        if _request is None:
            _params = {}
            if application_id is not ShapeBase.NOT_SET:
                _params['application_id'] = application_id
            _request = shapes.DeleteAdmChannelRequest(**_params)
        response = self._boto_client.delete_adm_channel(**_request.to_boto())

        return shapes.DeleteAdmChannelResponse.from_boto(response)

    def delete_apns_channel(
        self,
        _request: shapes.DeleteApnsChannelRequest = None,
        *,
        application_id: str,
    ) -> shapes.DeleteApnsChannelResponse:
        """
        Deletes the APNs channel for an app.
        """
        if _request is None:
            _params = {}
            if application_id is not ShapeBase.NOT_SET:
                _params['application_id'] = application_id
            _request = shapes.DeleteApnsChannelRequest(**_params)
        response = self._boto_client.delete_apns_channel(**_request.to_boto())

        return shapes.DeleteApnsChannelResponse.from_boto(response)

    def delete_apns_sandbox_channel(
        self,
        _request: shapes.DeleteApnsSandboxChannelRequest = None,
        *,
        application_id: str,
    ) -> shapes.DeleteApnsSandboxChannelResponse:
        """
        Delete an APNS sandbox channel.
        """
        if _request is None:
            _params = {}
            if application_id is not ShapeBase.NOT_SET:
                _params['application_id'] = application_id
            _request = shapes.DeleteApnsSandboxChannelRequest(**_params)
        response = self._boto_client.delete_apns_sandbox_channel(
            **_request.to_boto()
        )

        return shapes.DeleteApnsSandboxChannelResponse.from_boto(response)

    def delete_apns_voip_channel(
        self,
        _request: shapes.DeleteApnsVoipChannelRequest = None,
        *,
        application_id: str,
    ) -> shapes.DeleteApnsVoipChannelResponse:
        """
        Delete an APNS VoIP channel
        """
        if _request is None:
            _params = {}
            if application_id is not ShapeBase.NOT_SET:
                _params['application_id'] = application_id
            _request = shapes.DeleteApnsVoipChannelRequest(**_params)
        response = self._boto_client.delete_apns_voip_channel(
            **_request.to_boto()
        )

        return shapes.DeleteApnsVoipChannelResponse.from_boto(response)

    def delete_apns_voip_sandbox_channel(
        self,
        _request: shapes.DeleteApnsVoipSandboxChannelRequest = None,
        *,
        application_id: str,
    ) -> shapes.DeleteApnsVoipSandboxChannelResponse:
        """
        Delete an APNS VoIP sandbox channel
        """
        if _request is None:
            _params = {}
            if application_id is not ShapeBase.NOT_SET:
                _params['application_id'] = application_id
            _request = shapes.DeleteApnsVoipSandboxChannelRequest(**_params)
        response = self._boto_client.delete_apns_voip_sandbox_channel(
            **_request.to_boto()
        )

        return shapes.DeleteApnsVoipSandboxChannelResponse.from_boto(response)

    def delete_app(
        self,
        _request: shapes.DeleteAppRequest = None,
        *,
        application_id: str,
    ) -> shapes.DeleteAppResponse:
        """
        Deletes an app.
        """
        if _request is None:
            _params = {}
            if application_id is not ShapeBase.NOT_SET:
                _params['application_id'] = application_id
            _request = shapes.DeleteAppRequest(**_params)
        response = self._boto_client.delete_app(**_request.to_boto())

        return shapes.DeleteAppResponse.from_boto(response)

    def delete_baidu_channel(
        self,
        _request: shapes.DeleteBaiduChannelRequest = None,
        *,
        application_id: str,
    ) -> shapes.DeleteBaiduChannelResponse:
        """
        Delete a BAIDU GCM channel
        """
        if _request is None:
            _params = {}
            if application_id is not ShapeBase.NOT_SET:
                _params['application_id'] = application_id
            _request = shapes.DeleteBaiduChannelRequest(**_params)
        response = self._boto_client.delete_baidu_channel(**_request.to_boto())

        return shapes.DeleteBaiduChannelResponse.from_boto(response)

    def delete_campaign(
        self,
        _request: shapes.DeleteCampaignRequest = None,
        *,
        application_id: str,
        campaign_id: str,
    ) -> shapes.DeleteCampaignResponse:
        """
        Deletes a campaign.
        """
        if _request is None:
            _params = {}
            if application_id is not ShapeBase.NOT_SET:
                _params['application_id'] = application_id
            if campaign_id is not ShapeBase.NOT_SET:
                _params['campaign_id'] = campaign_id
            _request = shapes.DeleteCampaignRequest(**_params)
        response = self._boto_client.delete_campaign(**_request.to_boto())

        return shapes.DeleteCampaignResponse.from_boto(response)

    def delete_email_channel(
        self,
        _request: shapes.DeleteEmailChannelRequest = None,
        *,
        application_id: str,
    ) -> shapes.DeleteEmailChannelResponse:
        """
        Delete an email channel.
        """
        if _request is None:
            _params = {}
            if application_id is not ShapeBase.NOT_SET:
                _params['application_id'] = application_id
            _request = shapes.DeleteEmailChannelRequest(**_params)
        response = self._boto_client.delete_email_channel(**_request.to_boto())

        return shapes.DeleteEmailChannelResponse.from_boto(response)

    def delete_endpoint(
        self,
        _request: shapes.DeleteEndpointRequest = None,
        *,
        application_id: str,
        endpoint_id: str,
    ) -> shapes.DeleteEndpointResponse:
        """
        Deletes an endpoint.
        """
        if _request is None:
            _params = {}
            if application_id is not ShapeBase.NOT_SET:
                _params['application_id'] = application_id
            if endpoint_id is not ShapeBase.NOT_SET:
                _params['endpoint_id'] = endpoint_id
            _request = shapes.DeleteEndpointRequest(**_params)
        response = self._boto_client.delete_endpoint(**_request.to_boto())

        return shapes.DeleteEndpointResponse.from_boto(response)

    def delete_event_stream(
        self,
        _request: shapes.DeleteEventStreamRequest = None,
        *,
        application_id: str,
    ) -> shapes.DeleteEventStreamResponse:
        """
        Deletes the event stream for an app.
        """
        if _request is None:
            _params = {}
            if application_id is not ShapeBase.NOT_SET:
                _params['application_id'] = application_id
            _request = shapes.DeleteEventStreamRequest(**_params)
        response = self._boto_client.delete_event_stream(**_request.to_boto())

        return shapes.DeleteEventStreamResponse.from_boto(response)

    def delete_gcm_channel(
        self,
        _request: shapes.DeleteGcmChannelRequest = None,
        *,
        application_id: str,
    ) -> shapes.DeleteGcmChannelResponse:
        """
        Deletes the GCM channel for an app.
        """
        if _request is None:
            _params = {}
            if application_id is not ShapeBase.NOT_SET:
                _params['application_id'] = application_id
            _request = shapes.DeleteGcmChannelRequest(**_params)
        response = self._boto_client.delete_gcm_channel(**_request.to_boto())

        return shapes.DeleteGcmChannelResponse.from_boto(response)

    def delete_segment(
        self,
        _request: shapes.DeleteSegmentRequest = None,
        *,
        application_id: str,
        segment_id: str,
    ) -> shapes.DeleteSegmentResponse:
        """
        Deletes a segment.
        """
        if _request is None:
            _params = {}
            if application_id is not ShapeBase.NOT_SET:
                _params['application_id'] = application_id
            if segment_id is not ShapeBase.NOT_SET:
                _params['segment_id'] = segment_id
            _request = shapes.DeleteSegmentRequest(**_params)
        response = self._boto_client.delete_segment(**_request.to_boto())

        return shapes.DeleteSegmentResponse.from_boto(response)

    def delete_sms_channel(
        self,
        _request: shapes.DeleteSmsChannelRequest = None,
        *,
        application_id: str,
    ) -> shapes.DeleteSmsChannelResponse:
        """
        Delete an SMS channel.
        """
        if _request is None:
            _params = {}
            if application_id is not ShapeBase.NOT_SET:
                _params['application_id'] = application_id
            _request = shapes.DeleteSmsChannelRequest(**_params)
        response = self._boto_client.delete_sms_channel(**_request.to_boto())

        return shapes.DeleteSmsChannelResponse.from_boto(response)

    def delete_user_endpoints(
        self,
        _request: shapes.DeleteUserEndpointsRequest = None,
        *,
        application_id: str,
        user_id: str,
    ) -> shapes.DeleteUserEndpointsResponse:
        """
        Deletes endpoints that are associated with a User ID.
        """
        if _request is None:
            _params = {}
            if application_id is not ShapeBase.NOT_SET:
                _params['application_id'] = application_id
            if user_id is not ShapeBase.NOT_SET:
                _params['user_id'] = user_id
            _request = shapes.DeleteUserEndpointsRequest(**_params)
        response = self._boto_client.delete_user_endpoints(**_request.to_boto())

        return shapes.DeleteUserEndpointsResponse.from_boto(response)

    def get_adm_channel(
        self,
        _request: shapes.GetAdmChannelRequest = None,
        *,
        application_id: str,
    ) -> shapes.GetAdmChannelResponse:
        """
        Get an ADM channel.
        """
        if _request is None:
            _params = {}
            if application_id is not ShapeBase.NOT_SET:
                _params['application_id'] = application_id
            _request = shapes.GetAdmChannelRequest(**_params)
        response = self._boto_client.get_adm_channel(**_request.to_boto())

        return shapes.GetAdmChannelResponse.from_boto(response)

    def get_apns_channel(
        self,
        _request: shapes.GetApnsChannelRequest = None,
        *,
        application_id: str,
    ) -> shapes.GetApnsChannelResponse:
        """
        Returns information about the APNs channel for an app.
        """
        if _request is None:
            _params = {}
            if application_id is not ShapeBase.NOT_SET:
                _params['application_id'] = application_id
            _request = shapes.GetApnsChannelRequest(**_params)
        response = self._boto_client.get_apns_channel(**_request.to_boto())

        return shapes.GetApnsChannelResponse.from_boto(response)

    def get_apns_sandbox_channel(
        self,
        _request: shapes.GetApnsSandboxChannelRequest = None,
        *,
        application_id: str,
    ) -> shapes.GetApnsSandboxChannelResponse:
        """
        Get an APNS sandbox channel.
        """
        if _request is None:
            _params = {}
            if application_id is not ShapeBase.NOT_SET:
                _params['application_id'] = application_id
            _request = shapes.GetApnsSandboxChannelRequest(**_params)
        response = self._boto_client.get_apns_sandbox_channel(
            **_request.to_boto()
        )

        return shapes.GetApnsSandboxChannelResponse.from_boto(response)

    def get_apns_voip_channel(
        self,
        _request: shapes.GetApnsVoipChannelRequest = None,
        *,
        application_id: str,
    ) -> shapes.GetApnsVoipChannelResponse:
        """
        Get an APNS VoIP channel
        """
        if _request is None:
            _params = {}
            if application_id is not ShapeBase.NOT_SET:
                _params['application_id'] = application_id
            _request = shapes.GetApnsVoipChannelRequest(**_params)
        response = self._boto_client.get_apns_voip_channel(**_request.to_boto())

        return shapes.GetApnsVoipChannelResponse.from_boto(response)

    def get_apns_voip_sandbox_channel(
        self,
        _request: shapes.GetApnsVoipSandboxChannelRequest = None,
        *,
        application_id: str,
    ) -> shapes.GetApnsVoipSandboxChannelResponse:
        """
        Get an APNS VoIPSandbox channel
        """
        if _request is None:
            _params = {}
            if application_id is not ShapeBase.NOT_SET:
                _params['application_id'] = application_id
            _request = shapes.GetApnsVoipSandboxChannelRequest(**_params)
        response = self._boto_client.get_apns_voip_sandbox_channel(
            **_request.to_boto()
        )

        return shapes.GetApnsVoipSandboxChannelResponse.from_boto(response)

    def get_app(
        self,
        _request: shapes.GetAppRequest = None,
        *,
        application_id: str,
    ) -> shapes.GetAppResponse:
        """
        Returns information about an app.
        """
        if _request is None:
            _params = {}
            if application_id is not ShapeBase.NOT_SET:
                _params['application_id'] = application_id
            _request = shapes.GetAppRequest(**_params)
        response = self._boto_client.get_app(**_request.to_boto())

        return shapes.GetAppResponse.from_boto(response)

    def get_application_settings(
        self,
        _request: shapes.GetApplicationSettingsRequest = None,
        *,
        application_id: str,
    ) -> shapes.GetApplicationSettingsResponse:
        """
        Used to request the settings for an app.
        """
        if _request is None:
            _params = {}
            if application_id is not ShapeBase.NOT_SET:
                _params['application_id'] = application_id
            _request = shapes.GetApplicationSettingsRequest(**_params)
        response = self._boto_client.get_application_settings(
            **_request.to_boto()
        )

        return shapes.GetApplicationSettingsResponse.from_boto(response)

    def get_apps(
        self,
        _request: shapes.GetAppsRequest = None,
        *,
        page_size: str = ShapeBase.NOT_SET,
        token: str = ShapeBase.NOT_SET,
    ) -> shapes.GetAppsResponse:
        """
        Returns information about your apps.
        """
        if _request is None:
            _params = {}
            if page_size is not ShapeBase.NOT_SET:
                _params['page_size'] = page_size
            if token is not ShapeBase.NOT_SET:
                _params['token'] = token
            _request = shapes.GetAppsRequest(**_params)
        response = self._boto_client.get_apps(**_request.to_boto())

        return shapes.GetAppsResponse.from_boto(response)

    def get_baidu_channel(
        self,
        _request: shapes.GetBaiduChannelRequest = None,
        *,
        application_id: str,
    ) -> shapes.GetBaiduChannelResponse:
        """
        Get a BAIDU GCM channel
        """
        if _request is None:
            _params = {}
            if application_id is not ShapeBase.NOT_SET:
                _params['application_id'] = application_id
            _request = shapes.GetBaiduChannelRequest(**_params)
        response = self._boto_client.get_baidu_channel(**_request.to_boto())

        return shapes.GetBaiduChannelResponse.from_boto(response)

    def get_campaign(
        self,
        _request: shapes.GetCampaignRequest = None,
        *,
        application_id: str,
        campaign_id: str,
    ) -> shapes.GetCampaignResponse:
        """
        Returns information about a campaign.
        """
        if _request is None:
            _params = {}
            if application_id is not ShapeBase.NOT_SET:
                _params['application_id'] = application_id
            if campaign_id is not ShapeBase.NOT_SET:
                _params['campaign_id'] = campaign_id
            _request = shapes.GetCampaignRequest(**_params)
        response = self._boto_client.get_campaign(**_request.to_boto())

        return shapes.GetCampaignResponse.from_boto(response)

    def get_campaign_activities(
        self,
        _request: shapes.GetCampaignActivitiesRequest = None,
        *,
        application_id: str,
        campaign_id: str,
        page_size: str = ShapeBase.NOT_SET,
        token: str = ShapeBase.NOT_SET,
    ) -> shapes.GetCampaignActivitiesResponse:
        """
        Returns information about the activity performed by a campaign.
        """
        if _request is None:
            _params = {}
            if application_id is not ShapeBase.NOT_SET:
                _params['application_id'] = application_id
            if campaign_id is not ShapeBase.NOT_SET:
                _params['campaign_id'] = campaign_id
            if page_size is not ShapeBase.NOT_SET:
                _params['page_size'] = page_size
            if token is not ShapeBase.NOT_SET:
                _params['token'] = token
            _request = shapes.GetCampaignActivitiesRequest(**_params)
        response = self._boto_client.get_campaign_activities(
            **_request.to_boto()
        )

        return shapes.GetCampaignActivitiesResponse.from_boto(response)

    def get_campaign_version(
        self,
        _request: shapes.GetCampaignVersionRequest = None,
        *,
        application_id: str,
        campaign_id: str,
        version: str,
    ) -> shapes.GetCampaignVersionResponse:
        """
        Returns information about a specific version of a campaign.
        """
        if _request is None:
            _params = {}
            if application_id is not ShapeBase.NOT_SET:
                _params['application_id'] = application_id
            if campaign_id is not ShapeBase.NOT_SET:
                _params['campaign_id'] = campaign_id
            if version is not ShapeBase.NOT_SET:
                _params['version'] = version
            _request = shapes.GetCampaignVersionRequest(**_params)
        response = self._boto_client.get_campaign_version(**_request.to_boto())

        return shapes.GetCampaignVersionResponse.from_boto(response)

    def get_campaign_versions(
        self,
        _request: shapes.GetCampaignVersionsRequest = None,
        *,
        application_id: str,
        campaign_id: str,
        page_size: str = ShapeBase.NOT_SET,
        token: str = ShapeBase.NOT_SET,
    ) -> shapes.GetCampaignVersionsResponse:
        """
        Returns information about your campaign versions.
        """
        if _request is None:
            _params = {}
            if application_id is not ShapeBase.NOT_SET:
                _params['application_id'] = application_id
            if campaign_id is not ShapeBase.NOT_SET:
                _params['campaign_id'] = campaign_id
            if page_size is not ShapeBase.NOT_SET:
                _params['page_size'] = page_size
            if token is not ShapeBase.NOT_SET:
                _params['token'] = token
            _request = shapes.GetCampaignVersionsRequest(**_params)
        response = self._boto_client.get_campaign_versions(**_request.to_boto())

        return shapes.GetCampaignVersionsResponse.from_boto(response)

    def get_campaigns(
        self,
        _request: shapes.GetCampaignsRequest = None,
        *,
        application_id: str,
        page_size: str = ShapeBase.NOT_SET,
        token: str = ShapeBase.NOT_SET,
    ) -> shapes.GetCampaignsResponse:
        """
        Returns information about your campaigns.
        """
        if _request is None:
            _params = {}
            if application_id is not ShapeBase.NOT_SET:
                _params['application_id'] = application_id
            if page_size is not ShapeBase.NOT_SET:
                _params['page_size'] = page_size
            if token is not ShapeBase.NOT_SET:
                _params['token'] = token
            _request = shapes.GetCampaignsRequest(**_params)
        response = self._boto_client.get_campaigns(**_request.to_boto())

        return shapes.GetCampaignsResponse.from_boto(response)

    def get_channels(
        self,
        _request: shapes.GetChannelsRequest = None,
        *,
        application_id: str,
    ) -> shapes.GetChannelsResponse:
        """
        Get all channels.
        """
        if _request is None:
            _params = {}
            if application_id is not ShapeBase.NOT_SET:
                _params['application_id'] = application_id
            _request = shapes.GetChannelsRequest(**_params)
        response = self._boto_client.get_channels(**_request.to_boto())

        return shapes.GetChannelsResponse.from_boto(response)

    def get_email_channel(
        self,
        _request: shapes.GetEmailChannelRequest = None,
        *,
        application_id: str,
    ) -> shapes.GetEmailChannelResponse:
        """
        Get an email channel.
        """
        if _request is None:
            _params = {}
            if application_id is not ShapeBase.NOT_SET:
                _params['application_id'] = application_id
            _request = shapes.GetEmailChannelRequest(**_params)
        response = self._boto_client.get_email_channel(**_request.to_boto())

        return shapes.GetEmailChannelResponse.from_boto(response)

    def get_endpoint(
        self,
        _request: shapes.GetEndpointRequest = None,
        *,
        application_id: str,
        endpoint_id: str,
    ) -> shapes.GetEndpointResponse:
        """
        Returns information about an endpoint.
        """
        if _request is None:
            _params = {}
            if application_id is not ShapeBase.NOT_SET:
                _params['application_id'] = application_id
            if endpoint_id is not ShapeBase.NOT_SET:
                _params['endpoint_id'] = endpoint_id
            _request = shapes.GetEndpointRequest(**_params)
        response = self._boto_client.get_endpoint(**_request.to_boto())

        return shapes.GetEndpointResponse.from_boto(response)

    def get_event_stream(
        self,
        _request: shapes.GetEventStreamRequest = None,
        *,
        application_id: str,
    ) -> shapes.GetEventStreamResponse:
        """
        Returns the event stream for an app.
        """
        if _request is None:
            _params = {}
            if application_id is not ShapeBase.NOT_SET:
                _params['application_id'] = application_id
            _request = shapes.GetEventStreamRequest(**_params)
        response = self._boto_client.get_event_stream(**_request.to_boto())

        return shapes.GetEventStreamResponse.from_boto(response)

    def get_export_job(
        self,
        _request: shapes.GetExportJobRequest = None,
        *,
        application_id: str,
        job_id: str,
    ) -> shapes.GetExportJobResponse:
        """
        Returns information about an export job.
        """
        if _request is None:
            _params = {}
            if application_id is not ShapeBase.NOT_SET:
                _params['application_id'] = application_id
            if job_id is not ShapeBase.NOT_SET:
                _params['job_id'] = job_id
            _request = shapes.GetExportJobRequest(**_params)
        response = self._boto_client.get_export_job(**_request.to_boto())

        return shapes.GetExportJobResponse.from_boto(response)

    def get_export_jobs(
        self,
        _request: shapes.GetExportJobsRequest = None,
        *,
        application_id: str,
        page_size: str = ShapeBase.NOT_SET,
        token: str = ShapeBase.NOT_SET,
    ) -> shapes.GetExportJobsResponse:
        """
        Returns information about your export jobs.
        """
        if _request is None:
            _params = {}
            if application_id is not ShapeBase.NOT_SET:
                _params['application_id'] = application_id
            if page_size is not ShapeBase.NOT_SET:
                _params['page_size'] = page_size
            if token is not ShapeBase.NOT_SET:
                _params['token'] = token
            _request = shapes.GetExportJobsRequest(**_params)
        response = self._boto_client.get_export_jobs(**_request.to_boto())

        return shapes.GetExportJobsResponse.from_boto(response)

    def get_gcm_channel(
        self,
        _request: shapes.GetGcmChannelRequest = None,
        *,
        application_id: str,
    ) -> shapes.GetGcmChannelResponse:
        """
        Returns information about the GCM channel for an app.
        """
        if _request is None:
            _params = {}
            if application_id is not ShapeBase.NOT_SET:
                _params['application_id'] = application_id
            _request = shapes.GetGcmChannelRequest(**_params)
        response = self._boto_client.get_gcm_channel(**_request.to_boto())

        return shapes.GetGcmChannelResponse.from_boto(response)

    def get_import_job(
        self,
        _request: shapes.GetImportJobRequest = None,
        *,
        application_id: str,
        job_id: str,
    ) -> shapes.GetImportJobResponse:
        """
        Returns information about an import job.
        """
        if _request is None:
            _params = {}
            if application_id is not ShapeBase.NOT_SET:
                _params['application_id'] = application_id
            if job_id is not ShapeBase.NOT_SET:
                _params['job_id'] = job_id
            _request = shapes.GetImportJobRequest(**_params)
        response = self._boto_client.get_import_job(**_request.to_boto())

        return shapes.GetImportJobResponse.from_boto(response)

    def get_import_jobs(
        self,
        _request: shapes.GetImportJobsRequest = None,
        *,
        application_id: str,
        page_size: str = ShapeBase.NOT_SET,
        token: str = ShapeBase.NOT_SET,
    ) -> shapes.GetImportJobsResponse:
        """
        Returns information about your import jobs.
        """
        if _request is None:
            _params = {}
            if application_id is not ShapeBase.NOT_SET:
                _params['application_id'] = application_id
            if page_size is not ShapeBase.NOT_SET:
                _params['page_size'] = page_size
            if token is not ShapeBase.NOT_SET:
                _params['token'] = token
            _request = shapes.GetImportJobsRequest(**_params)
        response = self._boto_client.get_import_jobs(**_request.to_boto())

        return shapes.GetImportJobsResponse.from_boto(response)

    def get_segment(
        self,
        _request: shapes.GetSegmentRequest = None,
        *,
        application_id: str,
        segment_id: str,
    ) -> shapes.GetSegmentResponse:
        """
        Returns information about a segment.
        """
        if _request is None:
            _params = {}
            if application_id is not ShapeBase.NOT_SET:
                _params['application_id'] = application_id
            if segment_id is not ShapeBase.NOT_SET:
                _params['segment_id'] = segment_id
            _request = shapes.GetSegmentRequest(**_params)
        response = self._boto_client.get_segment(**_request.to_boto())

        return shapes.GetSegmentResponse.from_boto(response)

    def get_segment_export_jobs(
        self,
        _request: shapes.GetSegmentExportJobsRequest = None,
        *,
        application_id: str,
        segment_id: str,
        page_size: str = ShapeBase.NOT_SET,
        token: str = ShapeBase.NOT_SET,
    ) -> shapes.GetSegmentExportJobsResponse:
        """
        Returns a list of export jobs for a specific segment.
        """
        if _request is None:
            _params = {}
            if application_id is not ShapeBase.NOT_SET:
                _params['application_id'] = application_id
            if segment_id is not ShapeBase.NOT_SET:
                _params['segment_id'] = segment_id
            if page_size is not ShapeBase.NOT_SET:
                _params['page_size'] = page_size
            if token is not ShapeBase.NOT_SET:
                _params['token'] = token
            _request = shapes.GetSegmentExportJobsRequest(**_params)
        response = self._boto_client.get_segment_export_jobs(
            **_request.to_boto()
        )

        return shapes.GetSegmentExportJobsResponse.from_boto(response)

    def get_segment_import_jobs(
        self,
        _request: shapes.GetSegmentImportJobsRequest = None,
        *,
        application_id: str,
        segment_id: str,
        page_size: str = ShapeBase.NOT_SET,
        token: str = ShapeBase.NOT_SET,
    ) -> shapes.GetSegmentImportJobsResponse:
        """
        Returns a list of import jobs for a specific segment.
        """
        if _request is None:
            _params = {}
            if application_id is not ShapeBase.NOT_SET:
                _params['application_id'] = application_id
            if segment_id is not ShapeBase.NOT_SET:
                _params['segment_id'] = segment_id
            if page_size is not ShapeBase.NOT_SET:
                _params['page_size'] = page_size
            if token is not ShapeBase.NOT_SET:
                _params['token'] = token
            _request = shapes.GetSegmentImportJobsRequest(**_params)
        response = self._boto_client.get_segment_import_jobs(
            **_request.to_boto()
        )

        return shapes.GetSegmentImportJobsResponse.from_boto(response)

    def get_segment_version(
        self,
        _request: shapes.GetSegmentVersionRequest = None,
        *,
        application_id: str,
        segment_id: str,
        version: str,
    ) -> shapes.GetSegmentVersionResponse:
        """
        Returns information about a segment version.
        """
        if _request is None:
            _params = {}
            if application_id is not ShapeBase.NOT_SET:
                _params['application_id'] = application_id
            if segment_id is not ShapeBase.NOT_SET:
                _params['segment_id'] = segment_id
            if version is not ShapeBase.NOT_SET:
                _params['version'] = version
            _request = shapes.GetSegmentVersionRequest(**_params)
        response = self._boto_client.get_segment_version(**_request.to_boto())

        return shapes.GetSegmentVersionResponse.from_boto(response)

    def get_segment_versions(
        self,
        _request: shapes.GetSegmentVersionsRequest = None,
        *,
        application_id: str,
        segment_id: str,
        page_size: str = ShapeBase.NOT_SET,
        token: str = ShapeBase.NOT_SET,
    ) -> shapes.GetSegmentVersionsResponse:
        """
        Returns information about your segment versions.
        """
        if _request is None:
            _params = {}
            if application_id is not ShapeBase.NOT_SET:
                _params['application_id'] = application_id
            if segment_id is not ShapeBase.NOT_SET:
                _params['segment_id'] = segment_id
            if page_size is not ShapeBase.NOT_SET:
                _params['page_size'] = page_size
            if token is not ShapeBase.NOT_SET:
                _params['token'] = token
            _request = shapes.GetSegmentVersionsRequest(**_params)
        response = self._boto_client.get_segment_versions(**_request.to_boto())

        return shapes.GetSegmentVersionsResponse.from_boto(response)

    def get_segments(
        self,
        _request: shapes.GetSegmentsRequest = None,
        *,
        application_id: str,
        page_size: str = ShapeBase.NOT_SET,
        token: str = ShapeBase.NOT_SET,
    ) -> shapes.GetSegmentsResponse:
        """
        Used to get information about your segments.
        """
        if _request is None:
            _params = {}
            if application_id is not ShapeBase.NOT_SET:
                _params['application_id'] = application_id
            if page_size is not ShapeBase.NOT_SET:
                _params['page_size'] = page_size
            if token is not ShapeBase.NOT_SET:
                _params['token'] = token
            _request = shapes.GetSegmentsRequest(**_params)
        response = self._boto_client.get_segments(**_request.to_boto())

        return shapes.GetSegmentsResponse.from_boto(response)

    def get_sms_channel(
        self,
        _request: shapes.GetSmsChannelRequest = None,
        *,
        application_id: str,
    ) -> shapes.GetSmsChannelResponse:
        """
        Get an SMS channel.
        """
        if _request is None:
            _params = {}
            if application_id is not ShapeBase.NOT_SET:
                _params['application_id'] = application_id
            _request = shapes.GetSmsChannelRequest(**_params)
        response = self._boto_client.get_sms_channel(**_request.to_boto())

        return shapes.GetSmsChannelResponse.from_boto(response)

    def get_user_endpoints(
        self,
        _request: shapes.GetUserEndpointsRequest = None,
        *,
        application_id: str,
        user_id: str,
    ) -> shapes.GetUserEndpointsResponse:
        """
        Returns information about the endpoints that are associated with a User ID.
        """
        if _request is None:
            _params = {}
            if application_id is not ShapeBase.NOT_SET:
                _params['application_id'] = application_id
            if user_id is not ShapeBase.NOT_SET:
                _params['user_id'] = user_id
            _request = shapes.GetUserEndpointsRequest(**_params)
        response = self._boto_client.get_user_endpoints(**_request.to_boto())

        return shapes.GetUserEndpointsResponse.from_boto(response)

    def phone_number_validate(
        self,
        _request: shapes.PhoneNumberValidateRequest = None,
        *,
        number_validate_request: shapes.NumberValidateRequest,
    ) -> shapes.PhoneNumberValidateResponse:
        """
        Returns information about the specified phone number.
        """
        if _request is None:
            _params = {}
            if number_validate_request is not ShapeBase.NOT_SET:
                _params['number_validate_request'] = number_validate_request
            _request = shapes.PhoneNumberValidateRequest(**_params)
        response = self._boto_client.phone_number_validate(**_request.to_boto())

        return shapes.PhoneNumberValidateResponse.from_boto(response)

    def put_event_stream(
        self,
        _request: shapes.PutEventStreamRequest = None,
        *,
        application_id: str,
        write_event_stream: shapes.WriteEventStream,
    ) -> shapes.PutEventStreamResponse:
        """
        Use to create or update the event stream for an app.
        """
        if _request is None:
            _params = {}
            if application_id is not ShapeBase.NOT_SET:
                _params['application_id'] = application_id
            if write_event_stream is not ShapeBase.NOT_SET:
                _params['write_event_stream'] = write_event_stream
            _request = shapes.PutEventStreamRequest(**_params)
        response = self._boto_client.put_event_stream(**_request.to_boto())

        return shapes.PutEventStreamResponse.from_boto(response)

    def put_events(
        self,
        _request: shapes.PutEventsRequest = None,
        *,
        application_id: str,
        events_request: shapes.EventsRequest,
    ) -> shapes.PutEventsResponse:
        """
        Use to record events for endpoints. This method creates events and creates or
        updates the endpoints that those events are associated with.
        """
        if _request is None:
            _params = {}
            if application_id is not ShapeBase.NOT_SET:
                _params['application_id'] = application_id
            if events_request is not ShapeBase.NOT_SET:
                _params['events_request'] = events_request
            _request = shapes.PutEventsRequest(**_params)
        response = self._boto_client.put_events(**_request.to_boto())

        return shapes.PutEventsResponse.from_boto(response)

    def remove_attributes(
        self,
        _request: shapes.RemoveAttributesRequest = None,
        *,
        application_id: str,
        attribute_type: str,
        update_attributes_request: shapes.UpdateAttributesRequest,
    ) -> shapes.RemoveAttributesResponse:
        """
        Used to remove the attributes for an app
        """
        if _request is None:
            _params = {}
            if application_id is not ShapeBase.NOT_SET:
                _params['application_id'] = application_id
            if attribute_type is not ShapeBase.NOT_SET:
                _params['attribute_type'] = attribute_type
            if update_attributes_request is not ShapeBase.NOT_SET:
                _params['update_attributes_request'] = update_attributes_request
            _request = shapes.RemoveAttributesRequest(**_params)
        response = self._boto_client.remove_attributes(**_request.to_boto())

        return shapes.RemoveAttributesResponse.from_boto(response)

    def send_messages(
        self,
        _request: shapes.SendMessagesRequest = None,
        *,
        application_id: str,
        message_request: shapes.MessageRequest,
    ) -> shapes.SendMessagesResponse:
        """
        Used to send a direct message.
        """
        if _request is None:
            _params = {}
            if application_id is not ShapeBase.NOT_SET:
                _params['application_id'] = application_id
            if message_request is not ShapeBase.NOT_SET:
                _params['message_request'] = message_request
            _request = shapes.SendMessagesRequest(**_params)
        response = self._boto_client.send_messages(**_request.to_boto())

        return shapes.SendMessagesResponse.from_boto(response)

    def send_users_messages(
        self,
        _request: shapes.SendUsersMessagesRequest = None,
        *,
        application_id: str,
        send_users_message_request: shapes.SendUsersMessageRequest,
    ) -> shapes.SendUsersMessagesResponse:
        """
        Used to send a message to a list of users.
        """
        if _request is None:
            _params = {}
            if application_id is not ShapeBase.NOT_SET:
                _params['application_id'] = application_id
            if send_users_message_request is not ShapeBase.NOT_SET:
                _params['send_users_message_request'
                       ] = send_users_message_request
            _request = shapes.SendUsersMessagesRequest(**_params)
        response = self._boto_client.send_users_messages(**_request.to_boto())

        return shapes.SendUsersMessagesResponse.from_boto(response)

    def update_adm_channel(
        self,
        _request: shapes.UpdateAdmChannelRequest = None,
        *,
        adm_channel_request: shapes.ADMChannelRequest,
        application_id: str,
    ) -> shapes.UpdateAdmChannelResponse:
        """
        Update an ADM channel.
        """
        if _request is None:
            _params = {}
            if adm_channel_request is not ShapeBase.NOT_SET:
                _params['adm_channel_request'] = adm_channel_request
            if application_id is not ShapeBase.NOT_SET:
                _params['application_id'] = application_id
            _request = shapes.UpdateAdmChannelRequest(**_params)
        response = self._boto_client.update_adm_channel(**_request.to_boto())

        return shapes.UpdateAdmChannelResponse.from_boto(response)

    def update_apns_channel(
        self,
        _request: shapes.UpdateApnsChannelRequest = None,
        *,
        apns_channel_request: shapes.APNSChannelRequest,
        application_id: str,
    ) -> shapes.UpdateApnsChannelResponse:
        """
        Use to update the APNs channel for an app.
        """
        if _request is None:
            _params = {}
            if apns_channel_request is not ShapeBase.NOT_SET:
                _params['apns_channel_request'] = apns_channel_request
            if application_id is not ShapeBase.NOT_SET:
                _params['application_id'] = application_id
            _request = shapes.UpdateApnsChannelRequest(**_params)
        response = self._boto_client.update_apns_channel(**_request.to_boto())

        return shapes.UpdateApnsChannelResponse.from_boto(response)

    def update_apns_sandbox_channel(
        self,
        _request: shapes.UpdateApnsSandboxChannelRequest = None,
        *,
        apns_sandbox_channel_request: shapes.APNSSandboxChannelRequest,
        application_id: str,
    ) -> shapes.UpdateApnsSandboxChannelResponse:
        """
        Update an APNS sandbox channel.
        """
        if _request is None:
            _params = {}
            if apns_sandbox_channel_request is not ShapeBase.NOT_SET:
                _params['apns_sandbox_channel_request'
                       ] = apns_sandbox_channel_request
            if application_id is not ShapeBase.NOT_SET:
                _params['application_id'] = application_id
            _request = shapes.UpdateApnsSandboxChannelRequest(**_params)
        response = self._boto_client.update_apns_sandbox_channel(
            **_request.to_boto()
        )

        return shapes.UpdateApnsSandboxChannelResponse.from_boto(response)

    def update_apns_voip_channel(
        self,
        _request: shapes.UpdateApnsVoipChannelRequest = None,
        *,
        apns_voip_channel_request: shapes.APNSVoipChannelRequest,
        application_id: str,
    ) -> shapes.UpdateApnsVoipChannelResponse:
        """
        Update an APNS VoIP channel
        """
        if _request is None:
            _params = {}
            if apns_voip_channel_request is not ShapeBase.NOT_SET:
                _params['apns_voip_channel_request'] = apns_voip_channel_request
            if application_id is not ShapeBase.NOT_SET:
                _params['application_id'] = application_id
            _request = shapes.UpdateApnsVoipChannelRequest(**_params)
        response = self._boto_client.update_apns_voip_channel(
            **_request.to_boto()
        )

        return shapes.UpdateApnsVoipChannelResponse.from_boto(response)

    def update_apns_voip_sandbox_channel(
        self,
        _request: shapes.UpdateApnsVoipSandboxChannelRequest = None,
        *,
        apns_voip_sandbox_channel_request: shapes.APNSVoipSandboxChannelRequest,
        application_id: str,
    ) -> shapes.UpdateApnsVoipSandboxChannelResponse:
        """
        Update an APNS VoIP sandbox channel
        """
        if _request is None:
            _params = {}
            if apns_voip_sandbox_channel_request is not ShapeBase.NOT_SET:
                _params['apns_voip_sandbox_channel_request'
                       ] = apns_voip_sandbox_channel_request
            if application_id is not ShapeBase.NOT_SET:
                _params['application_id'] = application_id
            _request = shapes.UpdateApnsVoipSandboxChannelRequest(**_params)
        response = self._boto_client.update_apns_voip_sandbox_channel(
            **_request.to_boto()
        )

        return shapes.UpdateApnsVoipSandboxChannelResponse.from_boto(response)

    def update_application_settings(
        self,
        _request: shapes.UpdateApplicationSettingsRequest = None,
        *,
        application_id: str,
        write_application_settings_request: shapes.
        WriteApplicationSettingsRequest,
    ) -> shapes.UpdateApplicationSettingsResponse:
        """
        Used to update the settings for an app.
        """
        if _request is None:
            _params = {}
            if application_id is not ShapeBase.NOT_SET:
                _params['application_id'] = application_id
            if write_application_settings_request is not ShapeBase.NOT_SET:
                _params['write_application_settings_request'
                       ] = write_application_settings_request
            _request = shapes.UpdateApplicationSettingsRequest(**_params)
        response = self._boto_client.update_application_settings(
            **_request.to_boto()
        )

        return shapes.UpdateApplicationSettingsResponse.from_boto(response)

    def update_baidu_channel(
        self,
        _request: shapes.UpdateBaiduChannelRequest = None,
        *,
        application_id: str,
        baidu_channel_request: shapes.BaiduChannelRequest,
    ) -> shapes.UpdateBaiduChannelResponse:
        """
        Update a BAIDU GCM channel
        """
        if _request is None:
            _params = {}
            if application_id is not ShapeBase.NOT_SET:
                _params['application_id'] = application_id
            if baidu_channel_request is not ShapeBase.NOT_SET:
                _params['baidu_channel_request'] = baidu_channel_request
            _request = shapes.UpdateBaiduChannelRequest(**_params)
        response = self._boto_client.update_baidu_channel(**_request.to_boto())

        return shapes.UpdateBaiduChannelResponse.from_boto(response)

    def update_campaign(
        self,
        _request: shapes.UpdateCampaignRequest = None,
        *,
        application_id: str,
        campaign_id: str,
        write_campaign_request: shapes.WriteCampaignRequest,
    ) -> shapes.UpdateCampaignResponse:
        """
        Use to update a campaign.
        """
        if _request is None:
            _params = {}
            if application_id is not ShapeBase.NOT_SET:
                _params['application_id'] = application_id
            if campaign_id is not ShapeBase.NOT_SET:
                _params['campaign_id'] = campaign_id
            if write_campaign_request is not ShapeBase.NOT_SET:
                _params['write_campaign_request'] = write_campaign_request
            _request = shapes.UpdateCampaignRequest(**_params)
        response = self._boto_client.update_campaign(**_request.to_boto())

        return shapes.UpdateCampaignResponse.from_boto(response)

    def update_email_channel(
        self,
        _request: shapes.UpdateEmailChannelRequest = None,
        *,
        application_id: str,
        email_channel_request: shapes.EmailChannelRequest,
    ) -> shapes.UpdateEmailChannelResponse:
        """
        Update an email channel.
        """
        if _request is None:
            _params = {}
            if application_id is not ShapeBase.NOT_SET:
                _params['application_id'] = application_id
            if email_channel_request is not ShapeBase.NOT_SET:
                _params['email_channel_request'] = email_channel_request
            _request = shapes.UpdateEmailChannelRequest(**_params)
        response = self._boto_client.update_email_channel(**_request.to_boto())

        return shapes.UpdateEmailChannelResponse.from_boto(response)

    def update_endpoint(
        self,
        _request: shapes.UpdateEndpointRequest = None,
        *,
        application_id: str,
        endpoint_id: str,
        endpoint_request: shapes.EndpointRequest,
    ) -> shapes.UpdateEndpointResponse:
        """
        Creates or updates an endpoint.
        """
        if _request is None:
            _params = {}
            if application_id is not ShapeBase.NOT_SET:
                _params['application_id'] = application_id
            if endpoint_id is not ShapeBase.NOT_SET:
                _params['endpoint_id'] = endpoint_id
            if endpoint_request is not ShapeBase.NOT_SET:
                _params['endpoint_request'] = endpoint_request
            _request = shapes.UpdateEndpointRequest(**_params)
        response = self._boto_client.update_endpoint(**_request.to_boto())

        return shapes.UpdateEndpointResponse.from_boto(response)

    def update_endpoints_batch(
        self,
        _request: shapes.UpdateEndpointsBatchRequest = None,
        *,
        application_id: str,
        endpoint_batch_request: shapes.EndpointBatchRequest,
    ) -> shapes.UpdateEndpointsBatchResponse:
        """
        Use to update a batch of endpoints.
        """
        if _request is None:
            _params = {}
            if application_id is not ShapeBase.NOT_SET:
                _params['application_id'] = application_id
            if endpoint_batch_request is not ShapeBase.NOT_SET:
                _params['endpoint_batch_request'] = endpoint_batch_request
            _request = shapes.UpdateEndpointsBatchRequest(**_params)
        response = self._boto_client.update_endpoints_batch(
            **_request.to_boto()
        )

        return shapes.UpdateEndpointsBatchResponse.from_boto(response)

    def update_gcm_channel(
        self,
        _request: shapes.UpdateGcmChannelRequest = None,
        *,
        application_id: str,
        gcm_channel_request: shapes.GCMChannelRequest,
    ) -> shapes.UpdateGcmChannelResponse:
        """
        Use to update the GCM channel for an app.
        """
        if _request is None:
            _params = {}
            if application_id is not ShapeBase.NOT_SET:
                _params['application_id'] = application_id
            if gcm_channel_request is not ShapeBase.NOT_SET:
                _params['gcm_channel_request'] = gcm_channel_request
            _request = shapes.UpdateGcmChannelRequest(**_params)
        response = self._boto_client.update_gcm_channel(**_request.to_boto())

        return shapes.UpdateGcmChannelResponse.from_boto(response)

    def update_segment(
        self,
        _request: shapes.UpdateSegmentRequest = None,
        *,
        application_id: str,
        segment_id: str,
        write_segment_request: shapes.WriteSegmentRequest,
    ) -> shapes.UpdateSegmentResponse:
        """
        Used to update a segment.
        """
        if _request is None:
            _params = {}
            if application_id is not ShapeBase.NOT_SET:
                _params['application_id'] = application_id
            if segment_id is not ShapeBase.NOT_SET:
                _params['segment_id'] = segment_id
            if write_segment_request is not ShapeBase.NOT_SET:
                _params['write_segment_request'] = write_segment_request
            _request = shapes.UpdateSegmentRequest(**_params)
        response = self._boto_client.update_segment(**_request.to_boto())

        return shapes.UpdateSegmentResponse.from_boto(response)

    def update_sms_channel(
        self,
        _request: shapes.UpdateSmsChannelRequest = None,
        *,
        application_id: str,
        sms_channel_request: shapes.SMSChannelRequest,
    ) -> shapes.UpdateSmsChannelResponse:
        """
        Update an SMS channel.
        """
        if _request is None:
            _params = {}
            if application_id is not ShapeBase.NOT_SET:
                _params['application_id'] = application_id
            if sms_channel_request is not ShapeBase.NOT_SET:
                _params['sms_channel_request'] = sms_channel_request
            _request = shapes.UpdateSmsChannelRequest(**_params)
        response = self._boto_client.update_sms_channel(**_request.to_boto())

        return shapes.UpdateSmsChannelResponse.from_boto(response)
