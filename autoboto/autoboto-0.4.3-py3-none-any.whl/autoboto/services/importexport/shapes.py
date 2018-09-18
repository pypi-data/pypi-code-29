import datetime
import typing
from autoboto import ShapeBase, OutputShapeBase, TypeInfo
import dataclasses


@dataclasses.dataclass
class Artifact(ShapeBase):
    """
    A discrete item that contains the description and URL of an artifact (such as a
    PDF).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "url",
                "URL",
                TypeInfo(str),
            ),
        ]

    # The associated description for this object.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The URL for a given Artifact.
    url: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class BucketPermissionException(ShapeBase):
    """
    The account specified does not have the appropriate bucket permissions.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    # The human-readable description of a particular error.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CancelJobInput(ShapeBase):
    """
    Input structure for the CancelJob operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_id",
                "JobId",
                TypeInfo(str),
            ),
            (
                "api_version",
                "APIVersion",
                TypeInfo(str),
            ),
        ]

    # A unique identifier which refers to a particular job.
    job_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the version of the client tool.
    api_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CancelJobOutput(OutputShapeBase):
    """
    Output structure for the CancelJob operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "success",
                "Success",
                TypeInfo(bool),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies whether (true) or not (false) AWS Import/Export updated your job.
    success: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CanceledJobIdException(ShapeBase):
    """
    The specified job ID has been canceled and is no longer valid.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    # The human-readable description of a particular error.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateJobInput(ShapeBase):
    """
    Input structure for the CreateJob operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_type",
                "JobType",
                TypeInfo(typing.Union[str, JobType]),
            ),
            (
                "manifest",
                "Manifest",
                TypeInfo(str),
            ),
            (
                "validate_only",
                "ValidateOnly",
                TypeInfo(bool),
            ),
            (
                "manifest_addendum",
                "ManifestAddendum",
                TypeInfo(str),
            ),
            (
                "api_version",
                "APIVersion",
                TypeInfo(str),
            ),
        ]

    # Specifies whether the job to initiate is an import or export job.
    job_type: typing.Union[str, "JobType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The UTF-8 encoded text of the manifest file.
    manifest: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Validate the manifest and parameter values in the request but do not
    # actually create a job.
    validate_only: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # For internal use only.
    manifest_addendum: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the version of the client tool.
    api_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateJobOutput(OutputShapeBase):
    """
    Output structure for the CreateJob operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "job_id",
                "JobId",
                TypeInfo(str),
            ),
            (
                "job_type",
                "JobType",
                TypeInfo(typing.Union[str, JobType]),
            ),
            (
                "signature",
                "Signature",
                TypeInfo(str),
            ),
            (
                "signature_file_contents",
                "SignatureFileContents",
                TypeInfo(str),
            ),
            (
                "warning_message",
                "WarningMessage",
                TypeInfo(str),
            ),
            (
                "artifact_list",
                "ArtifactList",
                TypeInfo(typing.List[Artifact]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A unique identifier which refers to a particular job.
    job_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies whether the job to initiate is an import or export job.
    job_type: typing.Union[str, "JobType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An encrypted code used to authenticate the request and response, for
    # example, "DV+TpDfx1/TdSE9ktyK9k/bDTVI=". Only use this value is you want to
    # create the signature file yourself. Generally you should use the
    # SignatureFileContents value.
    signature: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The actual text of the SIGNATURE file to be written to disk.
    signature_file_contents: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An optional message notifying you of non-fatal issues with the job, such as
    # use of an incompatible Amazon S3 bucket name.
    warning_message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A collection of artifacts.
    artifact_list: typing.List["Artifact"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateJobQuotaExceededException(ShapeBase):
    """
    Each account can create only a certain number of jobs per day. If you need to
    create more than this, please contact awsimportexport@amazon.com to explain your
    particular use case.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    # The human-readable description of a particular error.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ExpiredJobIdException(ShapeBase):
    """
    Indicates that the specified job has expired out of the system.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    # The human-readable description of a particular error.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetShippingLabelInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_ids",
                "jobIds",
                TypeInfo(typing.List[str]),
            ),
            (
                "name",
                "name",
                TypeInfo(str),
            ),
            (
                "company",
                "company",
                TypeInfo(str),
            ),
            (
                "phone_number",
                "phoneNumber",
                TypeInfo(str),
            ),
            (
                "country",
                "country",
                TypeInfo(str),
            ),
            (
                "state_or_province",
                "stateOrProvince",
                TypeInfo(str),
            ),
            (
                "city",
                "city",
                TypeInfo(str),
            ),
            (
                "postal_code",
                "postalCode",
                TypeInfo(str),
            ),
            (
                "street1",
                "street1",
                TypeInfo(str),
            ),
            (
                "street2",
                "street2",
                TypeInfo(str),
            ),
            (
                "street3",
                "street3",
                TypeInfo(str),
            ),
            (
                "api_version",
                "APIVersion",
                TypeInfo(str),
            ),
        ]

    job_ids: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the name of the person responsible for shipping this package.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the name of the company that will ship this package.
    company: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the phone number of the person responsible for shipping this
    # package.
    phone_number: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the name of your country for the return address.
    country: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the name of your state or your province for the return address.
    state_or_province: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the name of your city for the return address.
    city: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the postal code for the return address.
    postal_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the first part of the street address for the return address, for
    # example 1234 Main Street.
    street1: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the optional second part of the street address for the return
    # address, for example Suite 100.
    street2: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the optional third part of the street address for the return
    # address, for example c/o Jane Doe.
    street3: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the version of the client tool.
    api_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetShippingLabelOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "shipping_label_url",
                "ShippingLabelURL",
                TypeInfo(str),
            ),
            (
                "warning",
                "Warning",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )
    shipping_label_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    warning: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetStatusInput(ShapeBase):
    """
    Input structure for the GetStatus operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_id",
                "JobId",
                TypeInfo(str),
            ),
            (
                "api_version",
                "APIVersion",
                TypeInfo(str),
            ),
        ]

    # A unique identifier which refers to a particular job.
    job_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the version of the client tool.
    api_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetStatusOutput(OutputShapeBase):
    """
    Output structure for the GetStatus operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "job_id",
                "JobId",
                TypeInfo(str),
            ),
            (
                "job_type",
                "JobType",
                TypeInfo(typing.Union[str, JobType]),
            ),
            (
                "location_code",
                "LocationCode",
                TypeInfo(str),
            ),
            (
                "location_message",
                "LocationMessage",
                TypeInfo(str),
            ),
            (
                "progress_code",
                "ProgressCode",
                TypeInfo(str),
            ),
            (
                "progress_message",
                "ProgressMessage",
                TypeInfo(str),
            ),
            (
                "carrier",
                "Carrier",
                TypeInfo(str),
            ),
            (
                "tracking_number",
                "TrackingNumber",
                TypeInfo(str),
            ),
            (
                "log_bucket",
                "LogBucket",
                TypeInfo(str),
            ),
            (
                "log_key",
                "LogKey",
                TypeInfo(str),
            ),
            (
                "error_count",
                "ErrorCount",
                TypeInfo(int),
            ),
            (
                "signature",
                "Signature",
                TypeInfo(str),
            ),
            (
                "signature_file_contents",
                "SignatureFileContents",
                TypeInfo(str),
            ),
            (
                "current_manifest",
                "CurrentManifest",
                TypeInfo(str),
            ),
            (
                "creation_date",
                "CreationDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "artifact_list",
                "ArtifactList",
                TypeInfo(typing.List[Artifact]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A unique identifier which refers to a particular job.
    job_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies whether the job to initiate is an import or export job.
    job_type: typing.Union[str, "JobType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A token representing the location of the storage device, such as "AtAWS".
    location_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A more human readable form of the physical location of the storage device.
    location_message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A token representing the state of the job, such as "Started".
    progress_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A more human readable form of the job status.
    progress_message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Name of the shipping company. This value is included when the LocationCode
    # is "Returned".
    carrier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The shipping tracking number assigned by AWS Import/Export to the storage
    # device when it's returned to you. We return this value when the
    # LocationCode is "Returned".
    tracking_number: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Amazon S3 bucket for user logs.
    log_bucket: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The key where the user logs were stored.
    log_key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Number of errors. We return this value when the ProgressCode is Success or
    # SuccessWithErrors.
    error_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An encrypted code used to authenticate the request and response, for
    # example, "DV+TpDfx1/TdSE9ktyK9k/bDTVI=". Only use this value is you want to
    # create the signature file yourself. Generally you should use the
    # SignatureFileContents value.
    signature: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An encrypted code used to authenticate the request and response, for
    # example, "DV+TpDfx1/TdSE9ktyK9k/bDTVI=". Only use this value is you want to
    # create the signature file yourself. Generally you should use the
    # SignatureFileContents value.
    signature_file_contents: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The last manifest submitted, which will be used to process the job.
    current_manifest: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Timestamp of the CreateJob request in ISO8601 date format. For example
    # "2010-03-28T20:27:35Z".
    creation_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A collection of artifacts.
    artifact_list: typing.List["Artifact"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class InvalidAccessKeyIdException(ShapeBase):
    """
    The AWS Access Key ID specified in the request did not match the manifest's
    accessKeyId value. The manifest and the request authentication must use the same
    AWS Access Key ID.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    # The human-readable description of a particular error.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidAddressException(ShapeBase):
    """
    The address specified in the manifest is invalid.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    # The human-readable description of a particular error.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidCustomsException(ShapeBase):
    """
    One or more customs parameters was invalid. Please correct and resubmit.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    # The human-readable description of a particular error.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidFileSystemException(ShapeBase):
    """
    File system specified in export manifest is invalid.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    # The human-readable description of a particular error.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidJobIdException(ShapeBase):
    """
    The JOBID was missing, not found, or not associated with the AWS account.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    # The human-readable description of a particular error.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidManifestFieldException(ShapeBase):
    """
    One or more manifest fields was invalid. Please correct and resubmit.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    # The human-readable description of a particular error.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidParameterException(ShapeBase):
    """
    One or more parameters had an invalid value.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    # The human-readable description of a particular error.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidVersionException(ShapeBase):
    """
    The client tool version is invalid.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    # The human-readable description of a particular error.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Job(ShapeBase):
    """
    Representation of a job returned by the ListJobs operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_id",
                "JobId",
                TypeInfo(str),
            ),
            (
                "creation_date",
                "CreationDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "is_canceled",
                "IsCanceled",
                TypeInfo(bool),
            ),
            (
                "job_type",
                "JobType",
                TypeInfo(typing.Union[str, JobType]),
            ),
        ]

    # A unique identifier which refers to a particular job.
    job_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Timestamp of the CreateJob request in ISO8601 date format. For example
    # "2010-03-28T20:27:35Z".
    creation_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Indicates whether the job was canceled.
    is_canceled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies whether the job to initiate is an import or export job.
    job_type: typing.Union[str, "JobType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class JobType(str):
    """
    Specifies whether the job to initiate is an import or export job.
    """
    Import = "Import"
    Export = "Export"


@dataclasses.dataclass
class ListJobsInput(ShapeBase):
    """
    Input structure for the ListJobs operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "max_jobs",
                "MaxJobs",
                TypeInfo(int),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
            (
                "api_version",
                "APIVersion",
                TypeInfo(str),
            ),
        ]

    # Sets the maximum number of jobs returned in the response. If there are
    # additional jobs that were not returned because MaxJobs was exceeded, the
    # response contains <IsTruncated>true</IsTruncated>. To return the additional
    # jobs, see Marker.
    max_jobs: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the JOBID to start after when listing the jobs created with your
    # account. AWS Import/Export lists your jobs in reverse chronological order.
    # See MaxJobs.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the version of the client tool.
    api_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListJobsOutput(OutputShapeBase):
    """
    Output structure for the ListJobs operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "jobs",
                "Jobs",
                TypeInfo(typing.List[Job]),
            ),
            (
                "is_truncated",
                "IsTruncated",
                TypeInfo(bool),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list container for Jobs returned by the ListJobs operation.
    jobs: typing.List["Job"] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates whether the list of jobs was truncated. If true, then call
    # ListJobs again using the last JobId element as the marker.
    is_truncated: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self, ) -> typing.Generator["ListJobsOutput", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class MalformedManifestException(ShapeBase):
    """
    Your manifest is not well-formed.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    # The human-readable description of a particular error.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class MissingCustomsException(ShapeBase):
    """
    One or more required customs parameters was missing from the manifest.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    # The human-readable description of a particular error.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class MissingManifestFieldException(ShapeBase):
    """
    One or more required fields were missing from the manifest file. Please correct
    and resubmit.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    # The human-readable description of a particular error.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class MissingParameterException(ShapeBase):
    """
    One or more required parameters was missing from the request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    # The human-readable description of a particular error.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class MultipleRegionsException(ShapeBase):
    """
    Your manifest file contained buckets from multiple regions. A job is restricted
    to buckets from one region. Please correct and resubmit.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    # The human-readable description of a particular error.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class NoSuchBucketException(ShapeBase):
    """
    The specified bucket does not exist. Create the specified bucket or change the
    manifest's bucket, exportBucket, or logBucket field to a bucket that the
    account, as specified by the manifest's Access Key ID, has write permissions to.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    # The human-readable description of a particular error.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UnableToCancelJobIdException(ShapeBase):
    """
    AWS Import/Export cannot cancel the job
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    # The human-readable description of a particular error.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UnableToUpdateJobIdException(ShapeBase):
    """
    AWS Import/Export cannot update the job
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    # The human-readable description of a particular error.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateJobInput(ShapeBase):
    """
    Input structure for the UpateJob operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_id",
                "JobId",
                TypeInfo(str),
            ),
            (
                "manifest",
                "Manifest",
                TypeInfo(str),
            ),
            (
                "job_type",
                "JobType",
                TypeInfo(typing.Union[str, JobType]),
            ),
            (
                "validate_only",
                "ValidateOnly",
                TypeInfo(bool),
            ),
            (
                "api_version",
                "APIVersion",
                TypeInfo(str),
            ),
        ]

    # A unique identifier which refers to a particular job.
    job_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The UTF-8 encoded text of the manifest file.
    manifest: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies whether the job to initiate is an import or export job.
    job_type: typing.Union[str, "JobType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Validate the manifest and parameter values in the request but do not
    # actually create a job.
    validate_only: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the version of the client tool.
    api_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateJobOutput(OutputShapeBase):
    """
    Output structure for the UpateJob operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "success",
                "Success",
                TypeInfo(bool),
            ),
            (
                "warning_message",
                "WarningMessage",
                TypeInfo(str),
            ),
            (
                "artifact_list",
                "ArtifactList",
                TypeInfo(typing.List[Artifact]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies whether (true) or not (false) AWS Import/Export updated your job.
    success: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An optional message notifying you of non-fatal issues with the job, such as
    # use of an incompatible Amazon S3 bucket name.
    warning_message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A collection of artifacts.
    artifact_list: typing.List["Artifact"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )
