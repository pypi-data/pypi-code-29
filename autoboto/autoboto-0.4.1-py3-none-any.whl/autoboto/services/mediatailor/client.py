import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("mediatailor", *args, **kwargs)

    def delete_playback_configuration(
        self,
        _request: shapes.DeletePlaybackConfigurationRequest = None,
        *,
        name: str,
    ) -> shapes.DeletePlaybackConfigurationResponse:
        """
        Deletes the configuration for the specified name.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            _request = shapes.DeletePlaybackConfigurationRequest(**_params)
        response = self._boto_client.delete_playback_configuration(
            **_request.to_boto()
        )

        return shapes.DeletePlaybackConfigurationResponse.from_boto(response)

    def get_playback_configuration(
        self,
        _request: shapes.GetPlaybackConfigurationRequest = None,
        *,
        name: str,
    ) -> shapes.GetPlaybackConfigurationResponse:
        """
        Returns the configuration for the specified name.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            _request = shapes.GetPlaybackConfigurationRequest(**_params)
        response = self._boto_client.get_playback_configuration(
            **_request.to_boto()
        )

        return shapes.GetPlaybackConfigurationResponse.from_boto(response)

    def list_playback_configurations(
        self,
        _request: shapes.ListPlaybackConfigurationsRequest = None,
        *,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListPlaybackConfigurationsResponse:
        """
        Returns a list of the configurations defined in AWS Elemental MediaTailor. You
        can specify a max number of configurations to return at a time. The default max
        is 50. Results are returned in pagefuls. If AWS Elemental MediaTailor has more
        configurations than the specified max, it provides parameters in the response
        that you can use to retrieve the next pageful.
        """
        if _request is None:
            _params = {}
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListPlaybackConfigurationsRequest(**_params)
        response = self._boto_client.list_playback_configurations(
            **_request.to_boto()
        )

        return shapes.ListPlaybackConfigurationsResponse.from_boto(response)

    def put_playback_configuration(
        self,
        _request: shapes.PutPlaybackConfigurationRequest = None,
        *,
        ad_decision_server_url: str = ShapeBase.NOT_SET,
        cdn_configuration: shapes.CdnConfiguration = ShapeBase.NOT_SET,
        name: str = ShapeBase.NOT_SET,
        slate_ad_url: str = ShapeBase.NOT_SET,
        video_content_source_url: str = ShapeBase.NOT_SET,
    ) -> shapes.PutPlaybackConfigurationResponse:
        """
        Adds a new configuration to AWS Elemental MediaTailor.
        """
        if _request is None:
            _params = {}
            if ad_decision_server_url is not ShapeBase.NOT_SET:
                _params['ad_decision_server_url'] = ad_decision_server_url
            if cdn_configuration is not ShapeBase.NOT_SET:
                _params['cdn_configuration'] = cdn_configuration
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if slate_ad_url is not ShapeBase.NOT_SET:
                _params['slate_ad_url'] = slate_ad_url
            if video_content_source_url is not ShapeBase.NOT_SET:
                _params['video_content_source_url'] = video_content_source_url
            _request = shapes.PutPlaybackConfigurationRequest(**_params)
        response = self._boto_client.put_playback_configuration(
            **_request.to_boto()
        )

        return shapes.PutPlaybackConfigurationResponse.from_boto(response)
