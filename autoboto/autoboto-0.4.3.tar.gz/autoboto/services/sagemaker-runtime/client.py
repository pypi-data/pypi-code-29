import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("sagemaker-runtime", *args, **kwargs)

    def invoke_endpoint(
        self,
        _request: shapes.InvokeEndpointInput = None,
        *,
        endpoint_name: str,
        body: typing.Any,
        content_type: str = ShapeBase.NOT_SET,
        accept: str = ShapeBase.NOT_SET,
        custom_attributes: str = ShapeBase.NOT_SET,
    ) -> shapes.InvokeEndpointOutput:
        """
        After you deploy a model into production using Amazon SageMaker hosting
        services, your client applications use this API to get inferences from the model
        hosted at the specified endpoint.

        For an overview of Amazon SageMaker, see [How It
        Works](http://docs.aws.amazon.com/sagemaker/latest/dg/how-it-works.html).

        Amazon SageMaker strips all POST headers except those supported by the API.
        Amazon SageMaker might add additional headers. You should not rely on the
        behavior of headers outside those enumerated in the request syntax.

        Cals to `InvokeEndpoint` are authenticated by using AWS Signature Version 4. For
        information, see [Authenticating Requests (AWS Signature Version
        4)](http://docs.aws.amazon.com/AmazonS3/latest/API/sig-v4-authenticating-
        requests.html) in the _Amazon S3 API Reference_.

        Endpoints are scoped to an individual account, and are not public. The URL does
        not contain the account ID, but Amazon SageMaker determines the account ID from
        the authentication token that is supplied by the caller.
        """
        if _request is None:
            _params = {}
            if endpoint_name is not ShapeBase.NOT_SET:
                _params['endpoint_name'] = endpoint_name
            if body is not ShapeBase.NOT_SET:
                _params['body'] = body
            if content_type is not ShapeBase.NOT_SET:
                _params['content_type'] = content_type
            if accept is not ShapeBase.NOT_SET:
                _params['accept'] = accept
            if custom_attributes is not ShapeBase.NOT_SET:
                _params['custom_attributes'] = custom_attributes
            _request = shapes.InvokeEndpointInput(**_params)
        response = self._boto_client.invoke_endpoint(**_request.to_boto())

        return shapes.InvokeEndpointOutput.from_boto(response)
