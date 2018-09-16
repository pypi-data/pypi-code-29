import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("importexport", *args, **kwargs)

    def cancel_job(
        self,
        _request: shapes.CancelJobInput = None,
        *,
        job_id: str,
        api_version: str = ShapeBase.NOT_SET,
    ) -> shapes.CancelJobOutput:
        """
        This operation cancels a specified job. Only the job owner can cancel it. The
        operation fails if the job has already started or is complete.
        """
        if _request is None:
            _params = {}
            if job_id is not ShapeBase.NOT_SET:
                _params['job_id'] = job_id
            if api_version is not ShapeBase.NOT_SET:
                _params['api_version'] = api_version
            _request = shapes.CancelJobInput(**_params)
        response = self._boto_client.cancel_job(**_request.to_boto())

        return shapes.CancelJobOutput.from_boto(response)

    def create_job(
        self,
        _request: shapes.CreateJobInput = None,
        *,
        job_type: typing.Union[str, shapes.JobType],
        manifest: str,
        validate_only: bool,
        manifest_addendum: str = ShapeBase.NOT_SET,
        api_version: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateJobOutput:
        """
        This operation initiates the process of scheduling an upload or download of your
        data. You include in the request a manifest that describes the data transfer
        specifics. The response to the request includes a job ID, which you can use in
        other operations, a signature that you use to identify your storage device, and
        the address where you should ship your storage device.
        """
        if _request is None:
            _params = {}
            if job_type is not ShapeBase.NOT_SET:
                _params['job_type'] = job_type
            if manifest is not ShapeBase.NOT_SET:
                _params['manifest'] = manifest
            if validate_only is not ShapeBase.NOT_SET:
                _params['validate_only'] = validate_only
            if manifest_addendum is not ShapeBase.NOT_SET:
                _params['manifest_addendum'] = manifest_addendum
            if api_version is not ShapeBase.NOT_SET:
                _params['api_version'] = api_version
            _request = shapes.CreateJobInput(**_params)
        response = self._boto_client.create_job(**_request.to_boto())

        return shapes.CreateJobOutput.from_boto(response)

    def get_shipping_label(
        self,
        _request: shapes.GetShippingLabelInput = None,
        *,
        job_ids: typing.List[str],
        name: str = ShapeBase.NOT_SET,
        company: str = ShapeBase.NOT_SET,
        phone_number: str = ShapeBase.NOT_SET,
        country: str = ShapeBase.NOT_SET,
        state_or_province: str = ShapeBase.NOT_SET,
        city: str = ShapeBase.NOT_SET,
        postal_code: str = ShapeBase.NOT_SET,
        street1: str = ShapeBase.NOT_SET,
        street2: str = ShapeBase.NOT_SET,
        street3: str = ShapeBase.NOT_SET,
        api_version: str = ShapeBase.NOT_SET,
    ) -> shapes.GetShippingLabelOutput:
        """
        This operation generates a pre-paid UPS shipping label that you will use to ship
        your device to AWS for processing.
        """
        if _request is None:
            _params = {}
            if job_ids is not ShapeBase.NOT_SET:
                _params['job_ids'] = job_ids
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if company is not ShapeBase.NOT_SET:
                _params['company'] = company
            if phone_number is not ShapeBase.NOT_SET:
                _params['phone_number'] = phone_number
            if country is not ShapeBase.NOT_SET:
                _params['country'] = country
            if state_or_province is not ShapeBase.NOT_SET:
                _params['state_or_province'] = state_or_province
            if city is not ShapeBase.NOT_SET:
                _params['city'] = city
            if postal_code is not ShapeBase.NOT_SET:
                _params['postal_code'] = postal_code
            if street1 is not ShapeBase.NOT_SET:
                _params['street1'] = street1
            if street2 is not ShapeBase.NOT_SET:
                _params['street2'] = street2
            if street3 is not ShapeBase.NOT_SET:
                _params['street3'] = street3
            if api_version is not ShapeBase.NOT_SET:
                _params['api_version'] = api_version
            _request = shapes.GetShippingLabelInput(**_params)
        response = self._boto_client.get_shipping_label(**_request.to_boto())

        return shapes.GetShippingLabelOutput.from_boto(response)

    def get_status(
        self,
        _request: shapes.GetStatusInput = None,
        *,
        job_id: str,
        api_version: str = ShapeBase.NOT_SET,
    ) -> shapes.GetStatusOutput:
        """
        This operation returns information about a job, including where the job is in
        the processing pipeline, the status of the results, and the signature value
        associated with the job. You can only return information about jobs you own.
        """
        if _request is None:
            _params = {}
            if job_id is not ShapeBase.NOT_SET:
                _params['job_id'] = job_id
            if api_version is not ShapeBase.NOT_SET:
                _params['api_version'] = api_version
            _request = shapes.GetStatusInput(**_params)
        response = self._boto_client.get_status(**_request.to_boto())

        return shapes.GetStatusOutput.from_boto(response)

    def list_jobs(
        self,
        _request: shapes.ListJobsInput = None,
        *,
        max_jobs: int = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
        api_version: str = ShapeBase.NOT_SET,
    ) -> shapes.ListJobsOutput:
        """
        This operation returns the jobs associated with the requester. AWS Import/Export
        lists the jobs in reverse chronological order based on the date of creation. For
        example if Job Test1 was created 2009Dec30 and Test2 was created 2010Feb05, the
        ListJobs operation would return Test2 followed by Test1.
        """
        if _request is None:
            _params = {}
            if max_jobs is not ShapeBase.NOT_SET:
                _params['max_jobs'] = max_jobs
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            if api_version is not ShapeBase.NOT_SET:
                _params['api_version'] = api_version
            _request = shapes.ListJobsInput(**_params)
        paginator = self.get_paginator("list_jobs").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListJobsOutput.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListJobsOutput.from_boto(response)

    def update_job(
        self,
        _request: shapes.UpdateJobInput = None,
        *,
        job_id: str,
        manifest: str,
        job_type: typing.Union[str, shapes.JobType],
        validate_only: bool,
        api_version: str = ShapeBase.NOT_SET,
    ) -> shapes.UpdateJobOutput:
        """
        You use this operation to change the parameters specified in the original
        manifest file by supplying a new manifest file. The manifest file attached to
        this request replaces the original manifest file. You can only use the operation
        after a CreateJob request but before the data transfer starts and you can only
        use it on jobs you own.
        """
        if _request is None:
            _params = {}
            if job_id is not ShapeBase.NOT_SET:
                _params['job_id'] = job_id
            if manifest is not ShapeBase.NOT_SET:
                _params['manifest'] = manifest
            if job_type is not ShapeBase.NOT_SET:
                _params['job_type'] = job_type
            if validate_only is not ShapeBase.NOT_SET:
                _params['validate_only'] = validate_only
            if api_version is not ShapeBase.NOT_SET:
                _params['api_version'] = api_version
            _request = shapes.UpdateJobInput(**_params)
        response = self._boto_client.update_job(**_request.to_boto())

        return shapes.UpdateJobOutput.from_boto(response)
