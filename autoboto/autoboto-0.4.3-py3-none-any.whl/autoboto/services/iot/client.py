import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("iot", *args, **kwargs)

    def accept_certificate_transfer(
        self,
        _request: shapes.AcceptCertificateTransferRequest = None,
        *,
        certificate_id: str,
        set_as_active: bool = ShapeBase.NOT_SET,
    ) -> None:
        """
        Accepts a pending certificate transfer. The default state of the certificate is
        INACTIVE.

        To check for pending certificate transfers, call ListCertificates to enumerate
        your certificates.
        """
        if _request is None:
            _params = {}
            if certificate_id is not ShapeBase.NOT_SET:
                _params['certificate_id'] = certificate_id
            if set_as_active is not ShapeBase.NOT_SET:
                _params['set_as_active'] = set_as_active
            _request = shapes.AcceptCertificateTransferRequest(**_params)
        response = self._boto_client.accept_certificate_transfer(
            **_request.to_boto()
        )

    def add_thing_to_thing_group(
        self,
        _request: shapes.AddThingToThingGroupRequest = None,
        *,
        thing_group_name: str = ShapeBase.NOT_SET,
        thing_group_arn: str = ShapeBase.NOT_SET,
        thing_name: str = ShapeBase.NOT_SET,
        thing_arn: str = ShapeBase.NOT_SET,
    ) -> shapes.AddThingToThingGroupResponse:
        """
        Adds a thing to a thing group.
        """
        if _request is None:
            _params = {}
            if thing_group_name is not ShapeBase.NOT_SET:
                _params['thing_group_name'] = thing_group_name
            if thing_group_arn is not ShapeBase.NOT_SET:
                _params['thing_group_arn'] = thing_group_arn
            if thing_name is not ShapeBase.NOT_SET:
                _params['thing_name'] = thing_name
            if thing_arn is not ShapeBase.NOT_SET:
                _params['thing_arn'] = thing_arn
            _request = shapes.AddThingToThingGroupRequest(**_params)
        response = self._boto_client.add_thing_to_thing_group(
            **_request.to_boto()
        )

        return shapes.AddThingToThingGroupResponse.from_boto(response)

    def associate_targets_with_job(
        self,
        _request: shapes.AssociateTargetsWithJobRequest = None,
        *,
        targets: typing.List[str],
        job_id: str,
        comment: str = ShapeBase.NOT_SET,
    ) -> shapes.AssociateTargetsWithJobResponse:
        """
        Associates a group with a continuous job. The following criteria must be met:

          * The job must have been created with the `targetSelection` field set to "CONTINUOUS".

          * The job status must currently be "IN_PROGRESS".

          * The total number of targets associated with a job must not exceed 100.
        """
        if _request is None:
            _params = {}
            if targets is not ShapeBase.NOT_SET:
                _params['targets'] = targets
            if job_id is not ShapeBase.NOT_SET:
                _params['job_id'] = job_id
            if comment is not ShapeBase.NOT_SET:
                _params['comment'] = comment
            _request = shapes.AssociateTargetsWithJobRequest(**_params)
        response = self._boto_client.associate_targets_with_job(
            **_request.to_boto()
        )

        return shapes.AssociateTargetsWithJobResponse.from_boto(response)

    def attach_policy(
        self,
        _request: shapes.AttachPolicyRequest = None,
        *,
        policy_name: str,
        target: str,
    ) -> None:
        """
        Attaches a policy to the specified target.
        """
        if _request is None:
            _params = {}
            if policy_name is not ShapeBase.NOT_SET:
                _params['policy_name'] = policy_name
            if target is not ShapeBase.NOT_SET:
                _params['target'] = target
            _request = shapes.AttachPolicyRequest(**_params)
        response = self._boto_client.attach_policy(**_request.to_boto())

    def attach_principal_policy(
        self,
        _request: shapes.AttachPrincipalPolicyRequest = None,
        *,
        policy_name: str,
        principal: str,
    ) -> None:
        """
        Attaches the specified policy to the specified principal (certificate or other
        credential).

        **Note:** This API is deprecated. Please use AttachPolicy instead.
        """
        if _request is None:
            _params = {}
            if policy_name is not ShapeBase.NOT_SET:
                _params['policy_name'] = policy_name
            if principal is not ShapeBase.NOT_SET:
                _params['principal'] = principal
            _request = shapes.AttachPrincipalPolicyRequest(**_params)
        response = self._boto_client.attach_principal_policy(
            **_request.to_boto()
        )

    def attach_security_profile(
        self,
        _request: shapes.AttachSecurityProfileRequest = None,
        *,
        security_profile_name: str,
        security_profile_target_arn: str,
    ) -> shapes.AttachSecurityProfileResponse:
        """
        Associates a Device Defender security profile with a thing group or with this
        account. Each thing group or account can have up to five security profiles
        associated with it.
        """
        if _request is None:
            _params = {}
            if security_profile_name is not ShapeBase.NOT_SET:
                _params['security_profile_name'] = security_profile_name
            if security_profile_target_arn is not ShapeBase.NOT_SET:
                _params['security_profile_target_arn'
                       ] = security_profile_target_arn
            _request = shapes.AttachSecurityProfileRequest(**_params)
        response = self._boto_client.attach_security_profile(
            **_request.to_boto()
        )

        return shapes.AttachSecurityProfileResponse.from_boto(response)

    def attach_thing_principal(
        self,
        _request: shapes.AttachThingPrincipalRequest = None,
        *,
        thing_name: str,
        principal: str,
    ) -> shapes.AttachThingPrincipalResponse:
        """
        Attaches the specified principal to the specified thing.
        """
        if _request is None:
            _params = {}
            if thing_name is not ShapeBase.NOT_SET:
                _params['thing_name'] = thing_name
            if principal is not ShapeBase.NOT_SET:
                _params['principal'] = principal
            _request = shapes.AttachThingPrincipalRequest(**_params)
        response = self._boto_client.attach_thing_principal(
            **_request.to_boto()
        )

        return shapes.AttachThingPrincipalResponse.from_boto(response)

    def cancel_audit_task(
        self,
        _request: shapes.CancelAuditTaskRequest = None,
        *,
        task_id: str,
    ) -> shapes.CancelAuditTaskResponse:
        """
        Cancels an audit that is in progress. The audit can be either scheduled or on-
        demand. If the audit is not in progress, an "InvalidRequestException" occurs.
        """
        if _request is None:
            _params = {}
            if task_id is not ShapeBase.NOT_SET:
                _params['task_id'] = task_id
            _request = shapes.CancelAuditTaskRequest(**_params)
        response = self._boto_client.cancel_audit_task(**_request.to_boto())

        return shapes.CancelAuditTaskResponse.from_boto(response)

    def cancel_certificate_transfer(
        self,
        _request: shapes.CancelCertificateTransferRequest = None,
        *,
        certificate_id: str,
    ) -> None:
        """
        Cancels a pending transfer for the specified certificate.

        **Note** Only the transfer source account can use this operation to cancel a
        transfer. (Transfer destinations can use RejectCertificateTransfer instead.)
        After transfer, AWS IoT returns the certificate to the source account in the
        INACTIVE state. After the destination account has accepted the transfer, the
        transfer cannot be cancelled.

        After a certificate transfer is cancelled, the status of the certificate changes
        from PENDING_TRANSFER to INACTIVE.
        """
        if _request is None:
            _params = {}
            if certificate_id is not ShapeBase.NOT_SET:
                _params['certificate_id'] = certificate_id
            _request = shapes.CancelCertificateTransferRequest(**_params)
        response = self._boto_client.cancel_certificate_transfer(
            **_request.to_boto()
        )

    def cancel_job(
        self,
        _request: shapes.CancelJobRequest = None,
        *,
        job_id: str,
        comment: str = ShapeBase.NOT_SET,
        force: bool = ShapeBase.NOT_SET,
    ) -> shapes.CancelJobResponse:
        """
        Cancels a job.
        """
        if _request is None:
            _params = {}
            if job_id is not ShapeBase.NOT_SET:
                _params['job_id'] = job_id
            if comment is not ShapeBase.NOT_SET:
                _params['comment'] = comment
            if force is not ShapeBase.NOT_SET:
                _params['force'] = force
            _request = shapes.CancelJobRequest(**_params)
        response = self._boto_client.cancel_job(**_request.to_boto())

        return shapes.CancelJobResponse.from_boto(response)

    def cancel_job_execution(
        self,
        _request: shapes.CancelJobExecutionRequest = None,
        *,
        job_id: str,
        thing_name: str,
        force: bool = ShapeBase.NOT_SET,
        expected_version: int = ShapeBase.NOT_SET,
        status_details: typing.Dict[str, str] = ShapeBase.NOT_SET,
    ) -> None:
        """
        Cancels the execution of a job for a given thing.
        """
        if _request is None:
            _params = {}
            if job_id is not ShapeBase.NOT_SET:
                _params['job_id'] = job_id
            if thing_name is not ShapeBase.NOT_SET:
                _params['thing_name'] = thing_name
            if force is not ShapeBase.NOT_SET:
                _params['force'] = force
            if expected_version is not ShapeBase.NOT_SET:
                _params['expected_version'] = expected_version
            if status_details is not ShapeBase.NOT_SET:
                _params['status_details'] = status_details
            _request = shapes.CancelJobExecutionRequest(**_params)
        response = self._boto_client.cancel_job_execution(**_request.to_boto())

    def clear_default_authorizer(
        self,
        _request: shapes.ClearDefaultAuthorizerRequest = None,
    ) -> shapes.ClearDefaultAuthorizerResponse:
        """
        Clears the default authorizer.
        """
        if _request is None:
            _params = {}
            _request = shapes.ClearDefaultAuthorizerRequest(**_params)
        response = self._boto_client.clear_default_authorizer(
            **_request.to_boto()
        )

        return shapes.ClearDefaultAuthorizerResponse.from_boto(response)

    def create_authorizer(
        self,
        _request: shapes.CreateAuthorizerRequest = None,
        *,
        authorizer_name: str,
        authorizer_function_arn: str,
        token_key_name: str,
        token_signing_public_keys: typing.Dict[str, str],
        status: typing.Union[str, shapes.AuthorizerStatus] = ShapeBase.NOT_SET,
    ) -> shapes.CreateAuthorizerResponse:
        """
        Creates an authorizer.
        """
        if _request is None:
            _params = {}
            if authorizer_name is not ShapeBase.NOT_SET:
                _params['authorizer_name'] = authorizer_name
            if authorizer_function_arn is not ShapeBase.NOT_SET:
                _params['authorizer_function_arn'] = authorizer_function_arn
            if token_key_name is not ShapeBase.NOT_SET:
                _params['token_key_name'] = token_key_name
            if token_signing_public_keys is not ShapeBase.NOT_SET:
                _params['token_signing_public_keys'] = token_signing_public_keys
            if status is not ShapeBase.NOT_SET:
                _params['status'] = status
            _request = shapes.CreateAuthorizerRequest(**_params)
        response = self._boto_client.create_authorizer(**_request.to_boto())

        return shapes.CreateAuthorizerResponse.from_boto(response)

    def create_certificate_from_csr(
        self,
        _request: shapes.CreateCertificateFromCsrRequest = None,
        *,
        certificate_signing_request: str,
        set_as_active: bool = ShapeBase.NOT_SET,
    ) -> shapes.CreateCertificateFromCsrResponse:
        """
        Creates an X.509 certificate using the specified certificate signing request.

        **Note:** The CSR must include a public key that is either an RSA key with a
        length of at least 2048 bits or an ECC key from NIST P-256 or NIST P-384 curves.

        **Note:** Reusing the same certificate signing request (CSR) results in a
        distinct certificate.

        You can create multiple certificates in a batch by creating a directory, copying
        multiple .csr files into that directory, and then specifying that directory on
        the command line. The following commands show how to create a batch of
        certificates given a batch of CSRs.

        Assuming a set of CSRs are located inside of the directory my-csr-directory:

        On Linux and OS X, the command is:

        $ ls my-csr-directory/ | xargs -I {} aws iot create-certificate-from-csr
        --certificate-signing-request file://my-csr-directory/{}

        This command lists all of the CSRs in my-csr-directory and pipes each CSR file
        name to the aws iot create-certificate-from-csr AWS CLI command to create a
        certificate for the corresponding CSR.

        The aws iot create-certificate-from-csr part of the command can also be run in
        parallel to speed up the certificate creation process:

        $ ls my-csr-directory/ | xargs -P 10 -I {} aws iot create-certificate-from-csr
        --certificate-signing-request file://my-csr-directory/{}

        On Windows PowerShell, the command to create certificates for all CSRs in my-
        csr-directory is:

        > ls -Name my-csr-directory | %{aws iot create-certificate-from-csr
        --certificate-signing-request file://my-csr-directory/$_}

        On a Windows command prompt, the command to create certificates for all CSRs in
        my-csr-directory is:

        > forfiles /p my-csr-directory /c "cmd /c aws iot create-certificate-from-csr
        --certificate-signing-request file://@path"
        """
        if _request is None:
            _params = {}
            if certificate_signing_request is not ShapeBase.NOT_SET:
                _params['certificate_signing_request'
                       ] = certificate_signing_request
            if set_as_active is not ShapeBase.NOT_SET:
                _params['set_as_active'] = set_as_active
            _request = shapes.CreateCertificateFromCsrRequest(**_params)
        response = self._boto_client.create_certificate_from_csr(
            **_request.to_boto()
        )

        return shapes.CreateCertificateFromCsrResponse.from_boto(response)

    def create_job(
        self,
        _request: shapes.CreateJobRequest = None,
        *,
        job_id: str,
        targets: typing.List[str],
        document_source: str = ShapeBase.NOT_SET,
        document: str = ShapeBase.NOT_SET,
        description: str = ShapeBase.NOT_SET,
        presigned_url_config: shapes.PresignedUrlConfig = ShapeBase.NOT_SET,
        target_selection: typing.Union[str, shapes.
                                       TargetSelection] = ShapeBase.NOT_SET,
        job_executions_rollout_config: shapes.
        JobExecutionsRolloutConfig = ShapeBase.NOT_SET,
    ) -> shapes.CreateJobResponse:
        """
        Creates a job.
        """
        if _request is None:
            _params = {}
            if job_id is not ShapeBase.NOT_SET:
                _params['job_id'] = job_id
            if targets is not ShapeBase.NOT_SET:
                _params['targets'] = targets
            if document_source is not ShapeBase.NOT_SET:
                _params['document_source'] = document_source
            if document is not ShapeBase.NOT_SET:
                _params['document'] = document
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if presigned_url_config is not ShapeBase.NOT_SET:
                _params['presigned_url_config'] = presigned_url_config
            if target_selection is not ShapeBase.NOT_SET:
                _params['target_selection'] = target_selection
            if job_executions_rollout_config is not ShapeBase.NOT_SET:
                _params['job_executions_rollout_config'
                       ] = job_executions_rollout_config
            _request = shapes.CreateJobRequest(**_params)
        response = self._boto_client.create_job(**_request.to_boto())

        return shapes.CreateJobResponse.from_boto(response)

    def create_keys_and_certificate(
        self,
        _request: shapes.CreateKeysAndCertificateRequest = None,
        *,
        set_as_active: bool = ShapeBase.NOT_SET,
    ) -> shapes.CreateKeysAndCertificateResponse:
        """
        Creates a 2048-bit RSA key pair and issues an X.509 certificate using the issued
        public key.

        **Note** This is the only time AWS IoT issues the private key for this
        certificate, so it is important to keep it in a secure location.
        """
        if _request is None:
            _params = {}
            if set_as_active is not ShapeBase.NOT_SET:
                _params['set_as_active'] = set_as_active
            _request = shapes.CreateKeysAndCertificateRequest(**_params)
        response = self._boto_client.create_keys_and_certificate(
            **_request.to_boto()
        )

        return shapes.CreateKeysAndCertificateResponse.from_boto(response)

    def create_ota_update(
        self,
        _request: shapes.CreateOTAUpdateRequest = None,
        *,
        ota_update_id: str,
        targets: typing.List[str],
        files: typing.List[shapes.OTAUpdateFile],
        role_arn: str,
        description: str = ShapeBase.NOT_SET,
        target_selection: typing.Union[str, shapes.
                                       TargetSelection] = ShapeBase.NOT_SET,
        aws_job_executions_rollout_config: shapes.
        AwsJobExecutionsRolloutConfig = ShapeBase.NOT_SET,
        additional_parameters: typing.Dict[str, str] = ShapeBase.NOT_SET,
    ) -> shapes.CreateOTAUpdateResponse:
        """
        Creates an AWS IoT OTAUpdate on a target group of things or groups.
        """
        if _request is None:
            _params = {}
            if ota_update_id is not ShapeBase.NOT_SET:
                _params['ota_update_id'] = ota_update_id
            if targets is not ShapeBase.NOT_SET:
                _params['targets'] = targets
            if files is not ShapeBase.NOT_SET:
                _params['files'] = files
            if role_arn is not ShapeBase.NOT_SET:
                _params['role_arn'] = role_arn
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if target_selection is not ShapeBase.NOT_SET:
                _params['target_selection'] = target_selection
            if aws_job_executions_rollout_config is not ShapeBase.NOT_SET:
                _params['aws_job_executions_rollout_config'
                       ] = aws_job_executions_rollout_config
            if additional_parameters is not ShapeBase.NOT_SET:
                _params['additional_parameters'] = additional_parameters
            _request = shapes.CreateOTAUpdateRequest(**_params)
        response = self._boto_client.create_ota_update(**_request.to_boto())

        return shapes.CreateOTAUpdateResponse.from_boto(response)

    def create_policy(
        self,
        _request: shapes.CreatePolicyRequest = None,
        *,
        policy_name: str,
        policy_document: str,
    ) -> shapes.CreatePolicyResponse:
        """
        Creates an AWS IoT policy.

        The created policy is the default version for the policy. This operation creates
        a policy version with a version identifier of **1** and sets **1** as the
        policy's default version.
        """
        if _request is None:
            _params = {}
            if policy_name is not ShapeBase.NOT_SET:
                _params['policy_name'] = policy_name
            if policy_document is not ShapeBase.NOT_SET:
                _params['policy_document'] = policy_document
            _request = shapes.CreatePolicyRequest(**_params)
        response = self._boto_client.create_policy(**_request.to_boto())

        return shapes.CreatePolicyResponse.from_boto(response)

    def create_policy_version(
        self,
        _request: shapes.CreatePolicyVersionRequest = None,
        *,
        policy_name: str,
        policy_document: str,
        set_as_default: bool = ShapeBase.NOT_SET,
    ) -> shapes.CreatePolicyVersionResponse:
        """
        Creates a new version of the specified AWS IoT policy. To update a policy,
        create a new policy version. A managed policy can have up to five versions. If
        the policy has five versions, you must use DeletePolicyVersion to delete an
        existing version before you create a new one.

        Optionally, you can set the new version as the policy's default version. The
        default version is the operative version (that is, the version that is in effect
        for the certificates to which the policy is attached).
        """
        if _request is None:
            _params = {}
            if policy_name is not ShapeBase.NOT_SET:
                _params['policy_name'] = policy_name
            if policy_document is not ShapeBase.NOT_SET:
                _params['policy_document'] = policy_document
            if set_as_default is not ShapeBase.NOT_SET:
                _params['set_as_default'] = set_as_default
            _request = shapes.CreatePolicyVersionRequest(**_params)
        response = self._boto_client.create_policy_version(**_request.to_boto())

        return shapes.CreatePolicyVersionResponse.from_boto(response)

    def create_role_alias(
        self,
        _request: shapes.CreateRoleAliasRequest = None,
        *,
        role_alias: str,
        role_arn: str,
        credential_duration_seconds: int = ShapeBase.NOT_SET,
    ) -> shapes.CreateRoleAliasResponse:
        """
        Creates a role alias.
        """
        if _request is None:
            _params = {}
            if role_alias is not ShapeBase.NOT_SET:
                _params['role_alias'] = role_alias
            if role_arn is not ShapeBase.NOT_SET:
                _params['role_arn'] = role_arn
            if credential_duration_seconds is not ShapeBase.NOT_SET:
                _params['credential_duration_seconds'
                       ] = credential_duration_seconds
            _request = shapes.CreateRoleAliasRequest(**_params)
        response = self._boto_client.create_role_alias(**_request.to_boto())

        return shapes.CreateRoleAliasResponse.from_boto(response)

    def create_scheduled_audit(
        self,
        _request: shapes.CreateScheduledAuditRequest = None,
        *,
        frequency: typing.Union[str, shapes.AuditFrequency],
        target_check_names: typing.List[str],
        scheduled_audit_name: str,
        day_of_month: str = ShapeBase.NOT_SET,
        day_of_week: typing.Union[str, shapes.DayOfWeek] = ShapeBase.NOT_SET,
    ) -> shapes.CreateScheduledAuditResponse:
        """
        Creates a scheduled audit that is run at a specified time interval.
        """
        if _request is None:
            _params = {}
            if frequency is not ShapeBase.NOT_SET:
                _params['frequency'] = frequency
            if target_check_names is not ShapeBase.NOT_SET:
                _params['target_check_names'] = target_check_names
            if scheduled_audit_name is not ShapeBase.NOT_SET:
                _params['scheduled_audit_name'] = scheduled_audit_name
            if day_of_month is not ShapeBase.NOT_SET:
                _params['day_of_month'] = day_of_month
            if day_of_week is not ShapeBase.NOT_SET:
                _params['day_of_week'] = day_of_week
            _request = shapes.CreateScheduledAuditRequest(**_params)
        response = self._boto_client.create_scheduled_audit(
            **_request.to_boto()
        )

        return shapes.CreateScheduledAuditResponse.from_boto(response)

    def create_security_profile(
        self,
        _request: shapes.CreateSecurityProfileRequest = None,
        *,
        security_profile_name: str,
        behaviors: typing.List[shapes.Behavior],
        security_profile_description: str = ShapeBase.NOT_SET,
        alert_targets: typing.Dict[typing.Union[str, shapes.AlertTargetType],
                                   shapes.AlertTarget] = ShapeBase.NOT_SET,
    ) -> shapes.CreateSecurityProfileResponse:
        """
        Creates a Device Defender security profile.
        """
        if _request is None:
            _params = {}
            if security_profile_name is not ShapeBase.NOT_SET:
                _params['security_profile_name'] = security_profile_name
            if behaviors is not ShapeBase.NOT_SET:
                _params['behaviors'] = behaviors
            if security_profile_description is not ShapeBase.NOT_SET:
                _params['security_profile_description'
                       ] = security_profile_description
            if alert_targets is not ShapeBase.NOT_SET:
                _params['alert_targets'] = alert_targets
            _request = shapes.CreateSecurityProfileRequest(**_params)
        response = self._boto_client.create_security_profile(
            **_request.to_boto()
        )

        return shapes.CreateSecurityProfileResponse.from_boto(response)

    def create_stream(
        self,
        _request: shapes.CreateStreamRequest = None,
        *,
        stream_id: str,
        files: typing.List[shapes.StreamFile],
        role_arn: str,
        description: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateStreamResponse:
        """
        Creates a stream for delivering one or more large files in chunks over MQTT. A
        stream transports data bytes in chunks or blocks packaged as MQTT messages from
        a source like S3. You can have one or more files associated with a stream. The
        total size of a file associated with the stream cannot exceed more than 2 MB.
        The stream will be created with version 0. If a stream is created with the same
        streamID as a stream that existed and was deleted within last 90 days, we will
        resurrect that old stream by incrementing the version by 1.
        """
        if _request is None:
            _params = {}
            if stream_id is not ShapeBase.NOT_SET:
                _params['stream_id'] = stream_id
            if files is not ShapeBase.NOT_SET:
                _params['files'] = files
            if role_arn is not ShapeBase.NOT_SET:
                _params['role_arn'] = role_arn
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            _request = shapes.CreateStreamRequest(**_params)
        response = self._boto_client.create_stream(**_request.to_boto())

        return shapes.CreateStreamResponse.from_boto(response)

    def create_thing(
        self,
        _request: shapes.CreateThingRequest = None,
        *,
        thing_name: str,
        thing_type_name: str = ShapeBase.NOT_SET,
        attribute_payload: shapes.AttributePayload = ShapeBase.NOT_SET,
    ) -> shapes.CreateThingResponse:
        """
        Creates a thing record in the registry.

        This is a control plane operation. See
        [Authorization](http://docs.aws.amazon.com/iot/latest/developerguide/authorization.html)
        for information about authorizing control plane actions.
        """
        if _request is None:
            _params = {}
            if thing_name is not ShapeBase.NOT_SET:
                _params['thing_name'] = thing_name
            if thing_type_name is not ShapeBase.NOT_SET:
                _params['thing_type_name'] = thing_type_name
            if attribute_payload is not ShapeBase.NOT_SET:
                _params['attribute_payload'] = attribute_payload
            _request = shapes.CreateThingRequest(**_params)
        response = self._boto_client.create_thing(**_request.to_boto())

        return shapes.CreateThingResponse.from_boto(response)

    def create_thing_group(
        self,
        _request: shapes.CreateThingGroupRequest = None,
        *,
        thing_group_name: str,
        parent_group_name: str = ShapeBase.NOT_SET,
        thing_group_properties: shapes.ThingGroupProperties = ShapeBase.NOT_SET,
    ) -> shapes.CreateThingGroupResponse:
        """
        Create a thing group.

        This is a control plane operation. See
        [Authorization](http://docs.aws.amazon.com/iot/latest/developerguide/authorization.html)
        for information about authorizing control plane actions.
        """
        if _request is None:
            _params = {}
            if thing_group_name is not ShapeBase.NOT_SET:
                _params['thing_group_name'] = thing_group_name
            if parent_group_name is not ShapeBase.NOT_SET:
                _params['parent_group_name'] = parent_group_name
            if thing_group_properties is not ShapeBase.NOT_SET:
                _params['thing_group_properties'] = thing_group_properties
            _request = shapes.CreateThingGroupRequest(**_params)
        response = self._boto_client.create_thing_group(**_request.to_boto())

        return shapes.CreateThingGroupResponse.from_boto(response)

    def create_thing_type(
        self,
        _request: shapes.CreateThingTypeRequest = None,
        *,
        thing_type_name: str,
        thing_type_properties: shapes.ThingTypeProperties = ShapeBase.NOT_SET,
    ) -> shapes.CreateThingTypeResponse:
        """
        Creates a new thing type.
        """
        if _request is None:
            _params = {}
            if thing_type_name is not ShapeBase.NOT_SET:
                _params['thing_type_name'] = thing_type_name
            if thing_type_properties is not ShapeBase.NOT_SET:
                _params['thing_type_properties'] = thing_type_properties
            _request = shapes.CreateThingTypeRequest(**_params)
        response = self._boto_client.create_thing_type(**_request.to_boto())

        return shapes.CreateThingTypeResponse.from_boto(response)

    def create_topic_rule(
        self,
        _request: shapes.CreateTopicRuleRequest = None,
        *,
        rule_name: str,
        topic_rule_payload: shapes.TopicRulePayload,
    ) -> None:
        """
        Creates a rule. Creating rules is an administrator-level action. Any user who
        has permission to create rules will be able to access data processed by the
        rule.
        """
        if _request is None:
            _params = {}
            if rule_name is not ShapeBase.NOT_SET:
                _params['rule_name'] = rule_name
            if topic_rule_payload is not ShapeBase.NOT_SET:
                _params['topic_rule_payload'] = topic_rule_payload
            _request = shapes.CreateTopicRuleRequest(**_params)
        response = self._boto_client.create_topic_rule(**_request.to_boto())

    def delete_account_audit_configuration(
        self,
        _request: shapes.DeleteAccountAuditConfigurationRequest = None,
        *,
        delete_scheduled_audits: bool = ShapeBase.NOT_SET,
    ) -> shapes.DeleteAccountAuditConfigurationResponse:
        """
        Restores the default settings for Device Defender audits for this account. Any
        configuration data you entered is deleted and all audit checks are reset to
        disabled.
        """
        if _request is None:
            _params = {}
            if delete_scheduled_audits is not ShapeBase.NOT_SET:
                _params['delete_scheduled_audits'] = delete_scheduled_audits
            _request = shapes.DeleteAccountAuditConfigurationRequest(**_params)
        response = self._boto_client.delete_account_audit_configuration(
            **_request.to_boto()
        )

        return shapes.DeleteAccountAuditConfigurationResponse.from_boto(
            response
        )

    def delete_authorizer(
        self,
        _request: shapes.DeleteAuthorizerRequest = None,
        *,
        authorizer_name: str,
    ) -> shapes.DeleteAuthorizerResponse:
        """
        Deletes an authorizer.
        """
        if _request is None:
            _params = {}
            if authorizer_name is not ShapeBase.NOT_SET:
                _params['authorizer_name'] = authorizer_name
            _request = shapes.DeleteAuthorizerRequest(**_params)
        response = self._boto_client.delete_authorizer(**_request.to_boto())

        return shapes.DeleteAuthorizerResponse.from_boto(response)

    def delete_ca_certificate(
        self,
        _request: shapes.DeleteCACertificateRequest = None,
        *,
        certificate_id: str,
    ) -> shapes.DeleteCACertificateResponse:
        """
        Deletes a registered CA certificate.
        """
        if _request is None:
            _params = {}
            if certificate_id is not ShapeBase.NOT_SET:
                _params['certificate_id'] = certificate_id
            _request = shapes.DeleteCACertificateRequest(**_params)
        response = self._boto_client.delete_ca_certificate(**_request.to_boto())

        return shapes.DeleteCACertificateResponse.from_boto(response)

    def delete_certificate(
        self,
        _request: shapes.DeleteCertificateRequest = None,
        *,
        certificate_id: str,
        force_delete: bool = ShapeBase.NOT_SET,
    ) -> None:
        """
        Deletes the specified certificate.

        A certificate cannot be deleted if it has a policy attached to it or if its
        status is set to ACTIVE. To delete a certificate, first use the
        DetachPrincipalPolicy API to detach all policies. Next, use the
        UpdateCertificate API to set the certificate to the INACTIVE status.
        """
        if _request is None:
            _params = {}
            if certificate_id is not ShapeBase.NOT_SET:
                _params['certificate_id'] = certificate_id
            if force_delete is not ShapeBase.NOT_SET:
                _params['force_delete'] = force_delete
            _request = shapes.DeleteCertificateRequest(**_params)
        response = self._boto_client.delete_certificate(**_request.to_boto())

    def delete_job(
        self,
        _request: shapes.DeleteJobRequest = None,
        *,
        job_id: str,
        force: bool = ShapeBase.NOT_SET,
    ) -> None:
        """
        Deletes a job and its related job executions.

        Deleting a job may take time, depending on the number of job executions created
        for the job and various other factors. While the job is being deleted, the
        status of the job will be shown as "DELETION_IN_PROGRESS". Attempting to delete
        or cancel a job whose status is already "DELETION_IN_PROGRESS" will result in an
        error.

        Only 10 jobs may have status "DELETION_IN_PROGRESS" at the same time, or a
        LimitExceededException will occur.
        """
        if _request is None:
            _params = {}
            if job_id is not ShapeBase.NOT_SET:
                _params['job_id'] = job_id
            if force is not ShapeBase.NOT_SET:
                _params['force'] = force
            _request = shapes.DeleteJobRequest(**_params)
        response = self._boto_client.delete_job(**_request.to_boto())

    def delete_job_execution(
        self,
        _request: shapes.DeleteJobExecutionRequest = None,
        *,
        job_id: str,
        thing_name: str,
        execution_number: int,
        force: bool = ShapeBase.NOT_SET,
    ) -> None:
        """
        Deletes a job execution.
        """
        if _request is None:
            _params = {}
            if job_id is not ShapeBase.NOT_SET:
                _params['job_id'] = job_id
            if thing_name is not ShapeBase.NOT_SET:
                _params['thing_name'] = thing_name
            if execution_number is not ShapeBase.NOT_SET:
                _params['execution_number'] = execution_number
            if force is not ShapeBase.NOT_SET:
                _params['force'] = force
            _request = shapes.DeleteJobExecutionRequest(**_params)
        response = self._boto_client.delete_job_execution(**_request.to_boto())

    def delete_ota_update(
        self,
        _request: shapes.DeleteOTAUpdateRequest = None,
        *,
        ota_update_id: str,
        delete_stream: bool = ShapeBase.NOT_SET,
        force_delete_aws_job: bool = ShapeBase.NOT_SET,
    ) -> shapes.DeleteOTAUpdateResponse:
        """
        Delete an OTA update.
        """
        if _request is None:
            _params = {}
            if ota_update_id is not ShapeBase.NOT_SET:
                _params['ota_update_id'] = ota_update_id
            if delete_stream is not ShapeBase.NOT_SET:
                _params['delete_stream'] = delete_stream
            if force_delete_aws_job is not ShapeBase.NOT_SET:
                _params['force_delete_aws_job'] = force_delete_aws_job
            _request = shapes.DeleteOTAUpdateRequest(**_params)
        response = self._boto_client.delete_ota_update(**_request.to_boto())

        return shapes.DeleteOTAUpdateResponse.from_boto(response)

    def delete_policy(
        self,
        _request: shapes.DeletePolicyRequest = None,
        *,
        policy_name: str,
    ) -> None:
        """
        Deletes the specified policy.

        A policy cannot be deleted if it has non-default versions or it is attached to
        any certificate.

        To delete a policy, use the DeletePolicyVersion API to delete all non-default
        versions of the policy; use the DetachPrincipalPolicy API to detach the policy
        from any certificate; and then use the DeletePolicy API to delete the policy.

        When a policy is deleted using DeletePolicy, its default version is deleted with
        it.
        """
        if _request is None:
            _params = {}
            if policy_name is not ShapeBase.NOT_SET:
                _params['policy_name'] = policy_name
            _request = shapes.DeletePolicyRequest(**_params)
        response = self._boto_client.delete_policy(**_request.to_boto())

    def delete_policy_version(
        self,
        _request: shapes.DeletePolicyVersionRequest = None,
        *,
        policy_name: str,
        policy_version_id: str,
    ) -> None:
        """
        Deletes the specified version of the specified policy. You cannot delete the
        default version of a policy using this API. To delete the default version of a
        policy, use DeletePolicy. To find out which version of a policy is marked as the
        default version, use ListPolicyVersions.
        """
        if _request is None:
            _params = {}
            if policy_name is not ShapeBase.NOT_SET:
                _params['policy_name'] = policy_name
            if policy_version_id is not ShapeBase.NOT_SET:
                _params['policy_version_id'] = policy_version_id
            _request = shapes.DeletePolicyVersionRequest(**_params)
        response = self._boto_client.delete_policy_version(**_request.to_boto())

    def delete_registration_code(
        self,
        _request: shapes.DeleteRegistrationCodeRequest = None,
    ) -> shapes.DeleteRegistrationCodeResponse:
        """
        Deletes a CA certificate registration code.
        """
        if _request is None:
            _params = {}
            _request = shapes.DeleteRegistrationCodeRequest(**_params)
        response = self._boto_client.delete_registration_code(
            **_request.to_boto()
        )

        return shapes.DeleteRegistrationCodeResponse.from_boto(response)

    def delete_role_alias(
        self,
        _request: shapes.DeleteRoleAliasRequest = None,
        *,
        role_alias: str,
    ) -> shapes.DeleteRoleAliasResponse:
        """
        Deletes a role alias
        """
        if _request is None:
            _params = {}
            if role_alias is not ShapeBase.NOT_SET:
                _params['role_alias'] = role_alias
            _request = shapes.DeleteRoleAliasRequest(**_params)
        response = self._boto_client.delete_role_alias(**_request.to_boto())

        return shapes.DeleteRoleAliasResponse.from_boto(response)

    def delete_scheduled_audit(
        self,
        _request: shapes.DeleteScheduledAuditRequest = None,
        *,
        scheduled_audit_name: str,
    ) -> shapes.DeleteScheduledAuditResponse:
        """
        Deletes a scheduled audit.
        """
        if _request is None:
            _params = {}
            if scheduled_audit_name is not ShapeBase.NOT_SET:
                _params['scheduled_audit_name'] = scheduled_audit_name
            _request = shapes.DeleteScheduledAuditRequest(**_params)
        response = self._boto_client.delete_scheduled_audit(
            **_request.to_boto()
        )

        return shapes.DeleteScheduledAuditResponse.from_boto(response)

    def delete_security_profile(
        self,
        _request: shapes.DeleteSecurityProfileRequest = None,
        *,
        security_profile_name: str,
        expected_version: int = ShapeBase.NOT_SET,
    ) -> shapes.DeleteSecurityProfileResponse:
        """
        Deletes a Device Defender security profile.
        """
        if _request is None:
            _params = {}
            if security_profile_name is not ShapeBase.NOT_SET:
                _params['security_profile_name'] = security_profile_name
            if expected_version is not ShapeBase.NOT_SET:
                _params['expected_version'] = expected_version
            _request = shapes.DeleteSecurityProfileRequest(**_params)
        response = self._boto_client.delete_security_profile(
            **_request.to_boto()
        )

        return shapes.DeleteSecurityProfileResponse.from_boto(response)

    def delete_stream(
        self,
        _request: shapes.DeleteStreamRequest = None,
        *,
        stream_id: str,
    ) -> shapes.DeleteStreamResponse:
        """
        Deletes a stream.
        """
        if _request is None:
            _params = {}
            if stream_id is not ShapeBase.NOT_SET:
                _params['stream_id'] = stream_id
            _request = shapes.DeleteStreamRequest(**_params)
        response = self._boto_client.delete_stream(**_request.to_boto())

        return shapes.DeleteStreamResponse.from_boto(response)

    def delete_thing(
        self,
        _request: shapes.DeleteThingRequest = None,
        *,
        thing_name: str,
        expected_version: int = ShapeBase.NOT_SET,
    ) -> shapes.DeleteThingResponse:
        """
        Deletes the specified thing.
        """
        if _request is None:
            _params = {}
            if thing_name is not ShapeBase.NOT_SET:
                _params['thing_name'] = thing_name
            if expected_version is not ShapeBase.NOT_SET:
                _params['expected_version'] = expected_version
            _request = shapes.DeleteThingRequest(**_params)
        response = self._boto_client.delete_thing(**_request.to_boto())

        return shapes.DeleteThingResponse.from_boto(response)

    def delete_thing_group(
        self,
        _request: shapes.DeleteThingGroupRequest = None,
        *,
        thing_group_name: str,
        expected_version: int = ShapeBase.NOT_SET,
    ) -> shapes.DeleteThingGroupResponse:
        """
        Deletes a thing group.
        """
        if _request is None:
            _params = {}
            if thing_group_name is not ShapeBase.NOT_SET:
                _params['thing_group_name'] = thing_group_name
            if expected_version is not ShapeBase.NOT_SET:
                _params['expected_version'] = expected_version
            _request = shapes.DeleteThingGroupRequest(**_params)
        response = self._boto_client.delete_thing_group(**_request.to_boto())

        return shapes.DeleteThingGroupResponse.from_boto(response)

    def delete_thing_type(
        self,
        _request: shapes.DeleteThingTypeRequest = None,
        *,
        thing_type_name: str,
    ) -> shapes.DeleteThingTypeResponse:
        """
        Deletes the specified thing type . You cannot delete a thing type if it has
        things associated with it. To delete a thing type, first mark it as deprecated
        by calling DeprecateThingType, then remove any associated things by calling
        UpdateThing to change the thing type on any associated thing, and finally use
        DeleteThingType to delete the thing type.
        """
        if _request is None:
            _params = {}
            if thing_type_name is not ShapeBase.NOT_SET:
                _params['thing_type_name'] = thing_type_name
            _request = shapes.DeleteThingTypeRequest(**_params)
        response = self._boto_client.delete_thing_type(**_request.to_boto())

        return shapes.DeleteThingTypeResponse.from_boto(response)

    def delete_topic_rule(
        self,
        _request: shapes.DeleteTopicRuleRequest = None,
        *,
        rule_name: str,
    ) -> None:
        """
        Deletes the rule.
        """
        if _request is None:
            _params = {}
            if rule_name is not ShapeBase.NOT_SET:
                _params['rule_name'] = rule_name
            _request = shapes.DeleteTopicRuleRequest(**_params)
        response = self._boto_client.delete_topic_rule(**_request.to_boto())

    def delete_v2_logging_level(
        self,
        _request: shapes.DeleteV2LoggingLevelRequest = None,
        *,
        target_type: typing.Union[str, shapes.LogTargetType],
        target_name: str,
    ) -> None:
        """
        Deletes a logging level.
        """
        if _request is None:
            _params = {}
            if target_type is not ShapeBase.NOT_SET:
                _params['target_type'] = target_type
            if target_name is not ShapeBase.NOT_SET:
                _params['target_name'] = target_name
            _request = shapes.DeleteV2LoggingLevelRequest(**_params)
        response = self._boto_client.delete_v2_logging_level(
            **_request.to_boto()
        )

    def deprecate_thing_type(
        self,
        _request: shapes.DeprecateThingTypeRequest = None,
        *,
        thing_type_name: str,
        undo_deprecate: bool = ShapeBase.NOT_SET,
    ) -> shapes.DeprecateThingTypeResponse:
        """
        Deprecates a thing type. You can not associate new things with deprecated thing
        type.
        """
        if _request is None:
            _params = {}
            if thing_type_name is not ShapeBase.NOT_SET:
                _params['thing_type_name'] = thing_type_name
            if undo_deprecate is not ShapeBase.NOT_SET:
                _params['undo_deprecate'] = undo_deprecate
            _request = shapes.DeprecateThingTypeRequest(**_params)
        response = self._boto_client.deprecate_thing_type(**_request.to_boto())

        return shapes.DeprecateThingTypeResponse.from_boto(response)

    def describe_account_audit_configuration(
        self,
        _request: shapes.DescribeAccountAuditConfigurationRequest = None,
    ) -> shapes.DescribeAccountAuditConfigurationResponse:
        """
        Gets information about the Device Defender audit settings for this account.
        Settings include how audit notifications are sent and which audit checks are
        enabled or disabled.
        """
        if _request is None:
            _params = {}
            _request = shapes.DescribeAccountAuditConfigurationRequest(
                **_params
            )
        response = self._boto_client.describe_account_audit_configuration(
            **_request.to_boto()
        )

        return shapes.DescribeAccountAuditConfigurationResponse.from_boto(
            response
        )

    def describe_audit_task(
        self,
        _request: shapes.DescribeAuditTaskRequest = None,
        *,
        task_id: str,
    ) -> shapes.DescribeAuditTaskResponse:
        """
        Gets information about a Device Defender audit.
        """
        if _request is None:
            _params = {}
            if task_id is not ShapeBase.NOT_SET:
                _params['task_id'] = task_id
            _request = shapes.DescribeAuditTaskRequest(**_params)
        response = self._boto_client.describe_audit_task(**_request.to_boto())

        return shapes.DescribeAuditTaskResponse.from_boto(response)

    def describe_authorizer(
        self,
        _request: shapes.DescribeAuthorizerRequest = None,
        *,
        authorizer_name: str,
    ) -> shapes.DescribeAuthorizerResponse:
        """
        Describes an authorizer.
        """
        if _request is None:
            _params = {}
            if authorizer_name is not ShapeBase.NOT_SET:
                _params['authorizer_name'] = authorizer_name
            _request = shapes.DescribeAuthorizerRequest(**_params)
        response = self._boto_client.describe_authorizer(**_request.to_boto())

        return shapes.DescribeAuthorizerResponse.from_boto(response)

    def describe_ca_certificate(
        self,
        _request: shapes.DescribeCACertificateRequest = None,
        *,
        certificate_id: str,
    ) -> shapes.DescribeCACertificateResponse:
        """
        Describes a registered CA certificate.
        """
        if _request is None:
            _params = {}
            if certificate_id is not ShapeBase.NOT_SET:
                _params['certificate_id'] = certificate_id
            _request = shapes.DescribeCACertificateRequest(**_params)
        response = self._boto_client.describe_ca_certificate(
            **_request.to_boto()
        )

        return shapes.DescribeCACertificateResponse.from_boto(response)

    def describe_certificate(
        self,
        _request: shapes.DescribeCertificateRequest = None,
        *,
        certificate_id: str,
    ) -> shapes.DescribeCertificateResponse:
        """
        Gets information about the specified certificate.
        """
        if _request is None:
            _params = {}
            if certificate_id is not ShapeBase.NOT_SET:
                _params['certificate_id'] = certificate_id
            _request = shapes.DescribeCertificateRequest(**_params)
        response = self._boto_client.describe_certificate(**_request.to_boto())

        return shapes.DescribeCertificateResponse.from_boto(response)

    def describe_default_authorizer(
        self,
        _request: shapes.DescribeDefaultAuthorizerRequest = None,
    ) -> shapes.DescribeDefaultAuthorizerResponse:
        """
        Describes the default authorizer.
        """
        if _request is None:
            _params = {}
            _request = shapes.DescribeDefaultAuthorizerRequest(**_params)
        response = self._boto_client.describe_default_authorizer(
            **_request.to_boto()
        )

        return shapes.DescribeDefaultAuthorizerResponse.from_boto(response)

    def describe_endpoint(
        self,
        _request: shapes.DescribeEndpointRequest = None,
        *,
        endpoint_type: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeEndpointResponse:
        """
        Returns a unique endpoint specific to the AWS account making the call.
        """
        if _request is None:
            _params = {}
            if endpoint_type is not ShapeBase.NOT_SET:
                _params['endpoint_type'] = endpoint_type
            _request = shapes.DescribeEndpointRequest(**_params)
        response = self._boto_client.describe_endpoint(**_request.to_boto())

        return shapes.DescribeEndpointResponse.from_boto(response)

    def describe_event_configurations(
        self,
        _request: shapes.DescribeEventConfigurationsRequest = None,
    ) -> shapes.DescribeEventConfigurationsResponse:
        """
        Describes event configurations.
        """
        if _request is None:
            _params = {}
            _request = shapes.DescribeEventConfigurationsRequest(**_params)
        response = self._boto_client.describe_event_configurations(
            **_request.to_boto()
        )

        return shapes.DescribeEventConfigurationsResponse.from_boto(response)

    def describe_index(
        self,
        _request: shapes.DescribeIndexRequest = None,
        *,
        index_name: str,
    ) -> shapes.DescribeIndexResponse:
        """
        Describes a search index.
        """
        if _request is None:
            _params = {}
            if index_name is not ShapeBase.NOT_SET:
                _params['index_name'] = index_name
            _request = shapes.DescribeIndexRequest(**_params)
        response = self._boto_client.describe_index(**_request.to_boto())

        return shapes.DescribeIndexResponse.from_boto(response)

    def describe_job(
        self,
        _request: shapes.DescribeJobRequest = None,
        *,
        job_id: str,
    ) -> shapes.DescribeJobResponse:
        """
        Describes a job.
        """
        if _request is None:
            _params = {}
            if job_id is not ShapeBase.NOT_SET:
                _params['job_id'] = job_id
            _request = shapes.DescribeJobRequest(**_params)
        response = self._boto_client.describe_job(**_request.to_boto())

        return shapes.DescribeJobResponse.from_boto(response)

    def describe_job_execution(
        self,
        _request: shapes.DescribeJobExecutionRequest = None,
        *,
        job_id: str,
        thing_name: str,
        execution_number: int = ShapeBase.NOT_SET,
    ) -> shapes.DescribeJobExecutionResponse:
        """
        Describes a job execution.
        """
        if _request is None:
            _params = {}
            if job_id is not ShapeBase.NOT_SET:
                _params['job_id'] = job_id
            if thing_name is not ShapeBase.NOT_SET:
                _params['thing_name'] = thing_name
            if execution_number is not ShapeBase.NOT_SET:
                _params['execution_number'] = execution_number
            _request = shapes.DescribeJobExecutionRequest(**_params)
        response = self._boto_client.describe_job_execution(
            **_request.to_boto()
        )

        return shapes.DescribeJobExecutionResponse.from_boto(response)

    def describe_role_alias(
        self,
        _request: shapes.DescribeRoleAliasRequest = None,
        *,
        role_alias: str,
    ) -> shapes.DescribeRoleAliasResponse:
        """
        Describes a role alias.
        """
        if _request is None:
            _params = {}
            if role_alias is not ShapeBase.NOT_SET:
                _params['role_alias'] = role_alias
            _request = shapes.DescribeRoleAliasRequest(**_params)
        response = self._boto_client.describe_role_alias(**_request.to_boto())

        return shapes.DescribeRoleAliasResponse.from_boto(response)

    def describe_scheduled_audit(
        self,
        _request: shapes.DescribeScheduledAuditRequest = None,
        *,
        scheduled_audit_name: str,
    ) -> shapes.DescribeScheduledAuditResponse:
        """
        Gets information about a scheduled audit.
        """
        if _request is None:
            _params = {}
            if scheduled_audit_name is not ShapeBase.NOT_SET:
                _params['scheduled_audit_name'] = scheduled_audit_name
            _request = shapes.DescribeScheduledAuditRequest(**_params)
        response = self._boto_client.describe_scheduled_audit(
            **_request.to_boto()
        )

        return shapes.DescribeScheduledAuditResponse.from_boto(response)

    def describe_security_profile(
        self,
        _request: shapes.DescribeSecurityProfileRequest = None,
        *,
        security_profile_name: str,
    ) -> shapes.DescribeSecurityProfileResponse:
        """
        Gets information about a Device Defender security profile.
        """
        if _request is None:
            _params = {}
            if security_profile_name is not ShapeBase.NOT_SET:
                _params['security_profile_name'] = security_profile_name
            _request = shapes.DescribeSecurityProfileRequest(**_params)
        response = self._boto_client.describe_security_profile(
            **_request.to_boto()
        )

        return shapes.DescribeSecurityProfileResponse.from_boto(response)

    def describe_stream(
        self,
        _request: shapes.DescribeStreamRequest = None,
        *,
        stream_id: str,
    ) -> shapes.DescribeStreamResponse:
        """
        Gets information about a stream.
        """
        if _request is None:
            _params = {}
            if stream_id is not ShapeBase.NOT_SET:
                _params['stream_id'] = stream_id
            _request = shapes.DescribeStreamRequest(**_params)
        response = self._boto_client.describe_stream(**_request.to_boto())

        return shapes.DescribeStreamResponse.from_boto(response)

    def describe_thing(
        self,
        _request: shapes.DescribeThingRequest = None,
        *,
        thing_name: str,
    ) -> shapes.DescribeThingResponse:
        """
        Gets information about the specified thing.
        """
        if _request is None:
            _params = {}
            if thing_name is not ShapeBase.NOT_SET:
                _params['thing_name'] = thing_name
            _request = shapes.DescribeThingRequest(**_params)
        response = self._boto_client.describe_thing(**_request.to_boto())

        return shapes.DescribeThingResponse.from_boto(response)

    def describe_thing_group(
        self,
        _request: shapes.DescribeThingGroupRequest = None,
        *,
        thing_group_name: str,
    ) -> shapes.DescribeThingGroupResponse:
        """
        Describe a thing group.
        """
        if _request is None:
            _params = {}
            if thing_group_name is not ShapeBase.NOT_SET:
                _params['thing_group_name'] = thing_group_name
            _request = shapes.DescribeThingGroupRequest(**_params)
        response = self._boto_client.describe_thing_group(**_request.to_boto())

        return shapes.DescribeThingGroupResponse.from_boto(response)

    def describe_thing_registration_task(
        self,
        _request: shapes.DescribeThingRegistrationTaskRequest = None,
        *,
        task_id: str,
    ) -> shapes.DescribeThingRegistrationTaskResponse:
        """
        Describes a bulk thing provisioning task.
        """
        if _request is None:
            _params = {}
            if task_id is not ShapeBase.NOT_SET:
                _params['task_id'] = task_id
            _request = shapes.DescribeThingRegistrationTaskRequest(**_params)
        response = self._boto_client.describe_thing_registration_task(
            **_request.to_boto()
        )

        return shapes.DescribeThingRegistrationTaskResponse.from_boto(response)

    def describe_thing_type(
        self,
        _request: shapes.DescribeThingTypeRequest = None,
        *,
        thing_type_name: str,
    ) -> shapes.DescribeThingTypeResponse:
        """
        Gets information about the specified thing type.
        """
        if _request is None:
            _params = {}
            if thing_type_name is not ShapeBase.NOT_SET:
                _params['thing_type_name'] = thing_type_name
            _request = shapes.DescribeThingTypeRequest(**_params)
        response = self._boto_client.describe_thing_type(**_request.to_boto())

        return shapes.DescribeThingTypeResponse.from_boto(response)

    def detach_policy(
        self,
        _request: shapes.DetachPolicyRequest = None,
        *,
        policy_name: str,
        target: str,
    ) -> None:
        """
        Detaches a policy from the specified target.
        """
        if _request is None:
            _params = {}
            if policy_name is not ShapeBase.NOT_SET:
                _params['policy_name'] = policy_name
            if target is not ShapeBase.NOT_SET:
                _params['target'] = target
            _request = shapes.DetachPolicyRequest(**_params)
        response = self._boto_client.detach_policy(**_request.to_boto())

    def detach_principal_policy(
        self,
        _request: shapes.DetachPrincipalPolicyRequest = None,
        *,
        policy_name: str,
        principal: str,
    ) -> None:
        """
        Removes the specified policy from the specified certificate.

        **Note:** This API is deprecated. Please use DetachPolicy instead.
        """
        if _request is None:
            _params = {}
            if policy_name is not ShapeBase.NOT_SET:
                _params['policy_name'] = policy_name
            if principal is not ShapeBase.NOT_SET:
                _params['principal'] = principal
            _request = shapes.DetachPrincipalPolicyRequest(**_params)
        response = self._boto_client.detach_principal_policy(
            **_request.to_boto()
        )

    def detach_security_profile(
        self,
        _request: shapes.DetachSecurityProfileRequest = None,
        *,
        security_profile_name: str,
        security_profile_target_arn: str,
    ) -> shapes.DetachSecurityProfileResponse:
        """
        Disassociates a Device Defender security profile from a thing group or from this
        account.
        """
        if _request is None:
            _params = {}
            if security_profile_name is not ShapeBase.NOT_SET:
                _params['security_profile_name'] = security_profile_name
            if security_profile_target_arn is not ShapeBase.NOT_SET:
                _params['security_profile_target_arn'
                       ] = security_profile_target_arn
            _request = shapes.DetachSecurityProfileRequest(**_params)
        response = self._boto_client.detach_security_profile(
            **_request.to_boto()
        )

        return shapes.DetachSecurityProfileResponse.from_boto(response)

    def detach_thing_principal(
        self,
        _request: shapes.DetachThingPrincipalRequest = None,
        *,
        thing_name: str,
        principal: str,
    ) -> shapes.DetachThingPrincipalResponse:
        """
        Detaches the specified principal from the specified thing.
        """
        if _request is None:
            _params = {}
            if thing_name is not ShapeBase.NOT_SET:
                _params['thing_name'] = thing_name
            if principal is not ShapeBase.NOT_SET:
                _params['principal'] = principal
            _request = shapes.DetachThingPrincipalRequest(**_params)
        response = self._boto_client.detach_thing_principal(
            **_request.to_boto()
        )

        return shapes.DetachThingPrincipalResponse.from_boto(response)

    def disable_topic_rule(
        self,
        _request: shapes.DisableTopicRuleRequest = None,
        *,
        rule_name: str,
    ) -> None:
        """
        Disables the rule.
        """
        if _request is None:
            _params = {}
            if rule_name is not ShapeBase.NOT_SET:
                _params['rule_name'] = rule_name
            _request = shapes.DisableTopicRuleRequest(**_params)
        response = self._boto_client.disable_topic_rule(**_request.to_boto())

    def enable_topic_rule(
        self,
        _request: shapes.EnableTopicRuleRequest = None,
        *,
        rule_name: str,
    ) -> None:
        """
        Enables the rule.
        """
        if _request is None:
            _params = {}
            if rule_name is not ShapeBase.NOT_SET:
                _params['rule_name'] = rule_name
            _request = shapes.EnableTopicRuleRequest(**_params)
        response = self._boto_client.enable_topic_rule(**_request.to_boto())

    def get_effective_policies(
        self,
        _request: shapes.GetEffectivePoliciesRequest = None,
        *,
        principal: str = ShapeBase.NOT_SET,
        cognito_identity_pool_id: str = ShapeBase.NOT_SET,
        thing_name: str = ShapeBase.NOT_SET,
    ) -> shapes.GetEffectivePoliciesResponse:
        """
        Gets a list of the policies that have an effect on the authorization behavior of
        the specified device when it connects to the AWS IoT device gateway.
        """
        if _request is None:
            _params = {}
            if principal is not ShapeBase.NOT_SET:
                _params['principal'] = principal
            if cognito_identity_pool_id is not ShapeBase.NOT_SET:
                _params['cognito_identity_pool_id'] = cognito_identity_pool_id
            if thing_name is not ShapeBase.NOT_SET:
                _params['thing_name'] = thing_name
            _request = shapes.GetEffectivePoliciesRequest(**_params)
        response = self._boto_client.get_effective_policies(
            **_request.to_boto()
        )

        return shapes.GetEffectivePoliciesResponse.from_boto(response)

    def get_indexing_configuration(
        self,
        _request: shapes.GetIndexingConfigurationRequest = None,
    ) -> shapes.GetIndexingConfigurationResponse:
        """
        Gets the search configuration.
        """
        if _request is None:
            _params = {}
            _request = shapes.GetIndexingConfigurationRequest(**_params)
        response = self._boto_client.get_indexing_configuration(
            **_request.to_boto()
        )

        return shapes.GetIndexingConfigurationResponse.from_boto(response)

    def get_job_document(
        self,
        _request: shapes.GetJobDocumentRequest = None,
        *,
        job_id: str,
    ) -> shapes.GetJobDocumentResponse:
        """
        Gets a job document.
        """
        if _request is None:
            _params = {}
            if job_id is not ShapeBase.NOT_SET:
                _params['job_id'] = job_id
            _request = shapes.GetJobDocumentRequest(**_params)
        response = self._boto_client.get_job_document(**_request.to_boto())

        return shapes.GetJobDocumentResponse.from_boto(response)

    def get_logging_options(
        self,
        _request: shapes.GetLoggingOptionsRequest = None,
    ) -> shapes.GetLoggingOptionsResponse:
        """
        Gets the logging options.

        NOTE: use of this command is not recommended. Use `GetV2LoggingOptions` instead.
        """
        if _request is None:
            _params = {}
            _request = shapes.GetLoggingOptionsRequest(**_params)
        response = self._boto_client.get_logging_options(**_request.to_boto())

        return shapes.GetLoggingOptionsResponse.from_boto(response)

    def get_ota_update(
        self,
        _request: shapes.GetOTAUpdateRequest = None,
        *,
        ota_update_id: str,
    ) -> shapes.GetOTAUpdateResponse:
        """
        Gets an OTA update.
        """
        if _request is None:
            _params = {}
            if ota_update_id is not ShapeBase.NOT_SET:
                _params['ota_update_id'] = ota_update_id
            _request = shapes.GetOTAUpdateRequest(**_params)
        response = self._boto_client.get_ota_update(**_request.to_boto())

        return shapes.GetOTAUpdateResponse.from_boto(response)

    def get_policy(
        self,
        _request: shapes.GetPolicyRequest = None,
        *,
        policy_name: str,
    ) -> shapes.GetPolicyResponse:
        """
        Gets information about the specified policy with the policy document of the
        default version.
        """
        if _request is None:
            _params = {}
            if policy_name is not ShapeBase.NOT_SET:
                _params['policy_name'] = policy_name
            _request = shapes.GetPolicyRequest(**_params)
        response = self._boto_client.get_policy(**_request.to_boto())

        return shapes.GetPolicyResponse.from_boto(response)

    def get_policy_version(
        self,
        _request: shapes.GetPolicyVersionRequest = None,
        *,
        policy_name: str,
        policy_version_id: str,
    ) -> shapes.GetPolicyVersionResponse:
        """
        Gets information about the specified policy version.
        """
        if _request is None:
            _params = {}
            if policy_name is not ShapeBase.NOT_SET:
                _params['policy_name'] = policy_name
            if policy_version_id is not ShapeBase.NOT_SET:
                _params['policy_version_id'] = policy_version_id
            _request = shapes.GetPolicyVersionRequest(**_params)
        response = self._boto_client.get_policy_version(**_request.to_boto())

        return shapes.GetPolicyVersionResponse.from_boto(response)

    def get_registration_code(
        self,
        _request: shapes.GetRegistrationCodeRequest = None,
    ) -> shapes.GetRegistrationCodeResponse:
        """
        Gets a registration code used to register a CA certificate with AWS IoT.
        """
        if _request is None:
            _params = {}
            _request = shapes.GetRegistrationCodeRequest(**_params)
        response = self._boto_client.get_registration_code(**_request.to_boto())

        return shapes.GetRegistrationCodeResponse.from_boto(response)

    def get_topic_rule(
        self,
        _request: shapes.GetTopicRuleRequest = None,
        *,
        rule_name: str,
    ) -> shapes.GetTopicRuleResponse:
        """
        Gets information about the rule.
        """
        if _request is None:
            _params = {}
            if rule_name is not ShapeBase.NOT_SET:
                _params['rule_name'] = rule_name
            _request = shapes.GetTopicRuleRequest(**_params)
        response = self._boto_client.get_topic_rule(**_request.to_boto())

        return shapes.GetTopicRuleResponse.from_boto(response)

    def get_v2_logging_options(
        self,
        _request: shapes.GetV2LoggingOptionsRequest = None,
    ) -> shapes.GetV2LoggingOptionsResponse:
        """
        Gets the fine grained logging options.
        """
        if _request is None:
            _params = {}
            _request = shapes.GetV2LoggingOptionsRequest(**_params)
        response = self._boto_client.get_v2_logging_options(
            **_request.to_boto()
        )

        return shapes.GetV2LoggingOptionsResponse.from_boto(response)

    def list_active_violations(
        self,
        _request: shapes.ListActiveViolationsRequest = None,
        *,
        thing_name: str = ShapeBase.NOT_SET,
        security_profile_name: str = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.ListActiveViolationsResponse:
        """
        Lists the active violations for a given Device Defender security profile.
        """
        if _request is None:
            _params = {}
            if thing_name is not ShapeBase.NOT_SET:
                _params['thing_name'] = thing_name
            if security_profile_name is not ShapeBase.NOT_SET:
                _params['security_profile_name'] = security_profile_name
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.ListActiveViolationsRequest(**_params)
        response = self._boto_client.list_active_violations(
            **_request.to_boto()
        )

        return shapes.ListActiveViolationsResponse.from_boto(response)

    def list_attached_policies(
        self,
        _request: shapes.ListAttachedPoliciesRequest = None,
        *,
        target: str,
        recursive: bool = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
        page_size: int = ShapeBase.NOT_SET,
    ) -> shapes.ListAttachedPoliciesResponse:
        """
        Lists the policies attached to the specified thing group.
        """
        if _request is None:
            _params = {}
            if target is not ShapeBase.NOT_SET:
                _params['target'] = target
            if recursive is not ShapeBase.NOT_SET:
                _params['recursive'] = recursive
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            if page_size is not ShapeBase.NOT_SET:
                _params['page_size'] = page_size
            _request = shapes.ListAttachedPoliciesRequest(**_params)
        response = self._boto_client.list_attached_policies(
            **_request.to_boto()
        )

        return shapes.ListAttachedPoliciesResponse.from_boto(response)

    def list_audit_findings(
        self,
        _request: shapes.ListAuditFindingsRequest = None,
        *,
        task_id: str = ShapeBase.NOT_SET,
        check_name: str = ShapeBase.NOT_SET,
        resource_identifier: shapes.ResourceIdentifier = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        start_time: datetime.datetime = ShapeBase.NOT_SET,
        end_time: datetime.datetime = ShapeBase.NOT_SET,
    ) -> shapes.ListAuditFindingsResponse:
        """
        Lists the findings (results) of a Device Defender audit or of the audits
        performed during a specified time period. (Findings are retained for 180 days.)
        """
        if _request is None:
            _params = {}
            if task_id is not ShapeBase.NOT_SET:
                _params['task_id'] = task_id
            if check_name is not ShapeBase.NOT_SET:
                _params['check_name'] = check_name
            if resource_identifier is not ShapeBase.NOT_SET:
                _params['resource_identifier'] = resource_identifier
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if start_time is not ShapeBase.NOT_SET:
                _params['start_time'] = start_time
            if end_time is not ShapeBase.NOT_SET:
                _params['end_time'] = end_time
            _request = shapes.ListAuditFindingsRequest(**_params)
        response = self._boto_client.list_audit_findings(**_request.to_boto())

        return shapes.ListAuditFindingsResponse.from_boto(response)

    def list_audit_tasks(
        self,
        _request: shapes.ListAuditTasksRequest = None,
        *,
        start_time: datetime.datetime,
        end_time: datetime.datetime,
        task_type: typing.Union[str, shapes.AuditTaskType] = ShapeBase.NOT_SET,
        task_status: typing.Union[str, shapes.AuditTaskStatus] = ShapeBase.
        NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.ListAuditTasksResponse:
        """
        Lists the Device Defender audits that have been performed during a given time
        period.
        """
        if _request is None:
            _params = {}
            if start_time is not ShapeBase.NOT_SET:
                _params['start_time'] = start_time
            if end_time is not ShapeBase.NOT_SET:
                _params['end_time'] = end_time
            if task_type is not ShapeBase.NOT_SET:
                _params['task_type'] = task_type
            if task_status is not ShapeBase.NOT_SET:
                _params['task_status'] = task_status
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.ListAuditTasksRequest(**_params)
        response = self._boto_client.list_audit_tasks(**_request.to_boto())

        return shapes.ListAuditTasksResponse.from_boto(response)

    def list_authorizers(
        self,
        _request: shapes.ListAuthorizersRequest = None,
        *,
        page_size: int = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
        ascending_order: bool = ShapeBase.NOT_SET,
        status: typing.Union[str, shapes.AuthorizerStatus] = ShapeBase.NOT_SET,
    ) -> shapes.ListAuthorizersResponse:
        """
        Lists the authorizers registered in your account.
        """
        if _request is None:
            _params = {}
            if page_size is not ShapeBase.NOT_SET:
                _params['page_size'] = page_size
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            if ascending_order is not ShapeBase.NOT_SET:
                _params['ascending_order'] = ascending_order
            if status is not ShapeBase.NOT_SET:
                _params['status'] = status
            _request = shapes.ListAuthorizersRequest(**_params)
        response = self._boto_client.list_authorizers(**_request.to_boto())

        return shapes.ListAuthorizersResponse.from_boto(response)

    def list_ca_certificates(
        self,
        _request: shapes.ListCACertificatesRequest = None,
        *,
        page_size: int = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
        ascending_order: bool = ShapeBase.NOT_SET,
    ) -> shapes.ListCACertificatesResponse:
        """
        Lists the CA certificates registered for your AWS account.

        The results are paginated with a default page size of 25. You can use the
        returned marker to retrieve additional results.
        """
        if _request is None:
            _params = {}
            if page_size is not ShapeBase.NOT_SET:
                _params['page_size'] = page_size
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            if ascending_order is not ShapeBase.NOT_SET:
                _params['ascending_order'] = ascending_order
            _request = shapes.ListCACertificatesRequest(**_params)
        paginator = self.get_paginator("list_ca_certificates").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListCACertificatesResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListCACertificatesResponse.from_boto(response)

    def list_certificates(
        self,
        _request: shapes.ListCertificatesRequest = None,
        *,
        page_size: int = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
        ascending_order: bool = ShapeBase.NOT_SET,
    ) -> shapes.ListCertificatesResponse:
        """
        Lists the certificates registered in your AWS account.

        The results are paginated with a default page size of 25. You can use the
        returned marker to retrieve additional results.
        """
        if _request is None:
            _params = {}
            if page_size is not ShapeBase.NOT_SET:
                _params['page_size'] = page_size
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            if ascending_order is not ShapeBase.NOT_SET:
                _params['ascending_order'] = ascending_order
            _request = shapes.ListCertificatesRequest(**_params)
        paginator = self.get_paginator("list_certificates").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListCertificatesResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListCertificatesResponse.from_boto(response)

    def list_certificates_by_ca(
        self,
        _request: shapes.ListCertificatesByCARequest = None,
        *,
        ca_certificate_id: str,
        page_size: int = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
        ascending_order: bool = ShapeBase.NOT_SET,
    ) -> shapes.ListCertificatesByCAResponse:
        """
        List the device certificates signed by the specified CA certificate.
        """
        if _request is None:
            _params = {}
            if ca_certificate_id is not ShapeBase.NOT_SET:
                _params['ca_certificate_id'] = ca_certificate_id
            if page_size is not ShapeBase.NOT_SET:
                _params['page_size'] = page_size
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            if ascending_order is not ShapeBase.NOT_SET:
                _params['ascending_order'] = ascending_order
            _request = shapes.ListCertificatesByCARequest(**_params)
        paginator = self.get_paginator("list_certificates_by_ca").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListCertificatesByCAResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListCertificatesByCAResponse.from_boto(response)

    def list_indices(
        self,
        _request: shapes.ListIndicesRequest = None,
        *,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.ListIndicesResponse:
        """
        Lists the search indices.
        """
        if _request is None:
            _params = {}
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.ListIndicesRequest(**_params)
        response = self._boto_client.list_indices(**_request.to_boto())

        return shapes.ListIndicesResponse.from_boto(response)

    def list_job_executions_for_job(
        self,
        _request: shapes.ListJobExecutionsForJobRequest = None,
        *,
        job_id: str,
        status: typing.Union[str, shapes.JobExecutionStatus] = ShapeBase.
        NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListJobExecutionsForJobResponse:
        """
        Lists the job executions for a job.
        """
        if _request is None:
            _params = {}
            if job_id is not ShapeBase.NOT_SET:
                _params['job_id'] = job_id
            if status is not ShapeBase.NOT_SET:
                _params['status'] = status
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListJobExecutionsForJobRequest(**_params)
        response = self._boto_client.list_job_executions_for_job(
            **_request.to_boto()
        )

        return shapes.ListJobExecutionsForJobResponse.from_boto(response)

    def list_job_executions_for_thing(
        self,
        _request: shapes.ListJobExecutionsForThingRequest = None,
        *,
        thing_name: str,
        status: typing.Union[str, shapes.JobExecutionStatus] = ShapeBase.
        NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListJobExecutionsForThingResponse:
        """
        Lists the job executions for the specified thing.
        """
        if _request is None:
            _params = {}
            if thing_name is not ShapeBase.NOT_SET:
                _params['thing_name'] = thing_name
            if status is not ShapeBase.NOT_SET:
                _params['status'] = status
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListJobExecutionsForThingRequest(**_params)
        response = self._boto_client.list_job_executions_for_thing(
            **_request.to_boto()
        )

        return shapes.ListJobExecutionsForThingResponse.from_boto(response)

    def list_jobs(
        self,
        _request: shapes.ListJobsRequest = None,
        *,
        status: typing.Union[str, shapes.JobStatus] = ShapeBase.NOT_SET,
        target_selection: typing.Union[str, shapes.TargetSelection] = ShapeBase.
        NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        thing_group_name: str = ShapeBase.NOT_SET,
        thing_group_id: str = ShapeBase.NOT_SET,
    ) -> shapes.ListJobsResponse:
        """
        Lists jobs.
        """
        if _request is None:
            _params = {}
            if status is not ShapeBase.NOT_SET:
                _params['status'] = status
            if target_selection is not ShapeBase.NOT_SET:
                _params['target_selection'] = target_selection
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if thing_group_name is not ShapeBase.NOT_SET:
                _params['thing_group_name'] = thing_group_name
            if thing_group_id is not ShapeBase.NOT_SET:
                _params['thing_group_id'] = thing_group_id
            _request = shapes.ListJobsRequest(**_params)
        response = self._boto_client.list_jobs(**_request.to_boto())

        return shapes.ListJobsResponse.from_boto(response)

    def list_ota_updates(
        self,
        _request: shapes.ListOTAUpdatesRequest = None,
        *,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        ota_update_status: typing.Union[str, shapes.
                                        OTAUpdateStatus] = ShapeBase.NOT_SET,
    ) -> shapes.ListOTAUpdatesResponse:
        """
        Lists OTA updates.
        """
        if _request is None:
            _params = {}
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if ota_update_status is not ShapeBase.NOT_SET:
                _params['ota_update_status'] = ota_update_status
            _request = shapes.ListOTAUpdatesRequest(**_params)
        response = self._boto_client.list_ota_updates(**_request.to_boto())

        return shapes.ListOTAUpdatesResponse.from_boto(response)

    def list_outgoing_certificates(
        self,
        _request: shapes.ListOutgoingCertificatesRequest = None,
        *,
        page_size: int = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
        ascending_order: bool = ShapeBase.NOT_SET,
    ) -> shapes.ListOutgoingCertificatesResponse:
        """
        Lists certificates that are being transferred but not yet accepted.
        """
        if _request is None:
            _params = {}
            if page_size is not ShapeBase.NOT_SET:
                _params['page_size'] = page_size
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            if ascending_order is not ShapeBase.NOT_SET:
                _params['ascending_order'] = ascending_order
            _request = shapes.ListOutgoingCertificatesRequest(**_params)
        paginator = self.get_paginator("list_outgoing_certificates").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListOutgoingCertificatesResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListOutgoingCertificatesResponse.from_boto(response)

    def list_policies(
        self,
        _request: shapes.ListPoliciesRequest = None,
        *,
        marker: str = ShapeBase.NOT_SET,
        page_size: int = ShapeBase.NOT_SET,
        ascending_order: bool = ShapeBase.NOT_SET,
    ) -> shapes.ListPoliciesResponse:
        """
        Lists your policies.
        """
        if _request is None:
            _params = {}
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            if page_size is not ShapeBase.NOT_SET:
                _params['page_size'] = page_size
            if ascending_order is not ShapeBase.NOT_SET:
                _params['ascending_order'] = ascending_order
            _request = shapes.ListPoliciesRequest(**_params)
        paginator = self.get_paginator("list_policies").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListPoliciesResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListPoliciesResponse.from_boto(response)

    def list_policy_principals(
        self,
        _request: shapes.ListPolicyPrincipalsRequest = None,
        *,
        policy_name: str,
        marker: str = ShapeBase.NOT_SET,
        page_size: int = ShapeBase.NOT_SET,
        ascending_order: bool = ShapeBase.NOT_SET,
    ) -> shapes.ListPolicyPrincipalsResponse:
        """
        Lists the principals associated with the specified policy.

        **Note:** This API is deprecated. Please use ListTargetsForPolicy instead.
        """
        if _request is None:
            _params = {}
            if policy_name is not ShapeBase.NOT_SET:
                _params['policy_name'] = policy_name
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            if page_size is not ShapeBase.NOT_SET:
                _params['page_size'] = page_size
            if ascending_order is not ShapeBase.NOT_SET:
                _params['ascending_order'] = ascending_order
            _request = shapes.ListPolicyPrincipalsRequest(**_params)
        paginator = self.get_paginator("list_policy_principals").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListPolicyPrincipalsResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListPolicyPrincipalsResponse.from_boto(response)

    def list_policy_versions(
        self,
        _request: shapes.ListPolicyVersionsRequest = None,
        *,
        policy_name: str,
    ) -> shapes.ListPolicyVersionsResponse:
        """
        Lists the versions of the specified policy and identifies the default version.
        """
        if _request is None:
            _params = {}
            if policy_name is not ShapeBase.NOT_SET:
                _params['policy_name'] = policy_name
            _request = shapes.ListPolicyVersionsRequest(**_params)
        response = self._boto_client.list_policy_versions(**_request.to_boto())

        return shapes.ListPolicyVersionsResponse.from_boto(response)

    def list_principal_policies(
        self,
        _request: shapes.ListPrincipalPoliciesRequest = None,
        *,
        principal: str,
        marker: str = ShapeBase.NOT_SET,
        page_size: int = ShapeBase.NOT_SET,
        ascending_order: bool = ShapeBase.NOT_SET,
    ) -> shapes.ListPrincipalPoliciesResponse:
        """
        Lists the policies attached to the specified principal. If you use an Cognito
        identity, the ID must be in [AmazonCognito Identity
        format](http://docs.aws.amazon.com/cognitoidentity/latest/APIReference/API_GetCredentialsForIdentity.html#API_GetCredentialsForIdentity_RequestSyntax).

        **Note:** This API is deprecated. Please use ListAttachedPolicies instead.
        """
        if _request is None:
            _params = {}
            if principal is not ShapeBase.NOT_SET:
                _params['principal'] = principal
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            if page_size is not ShapeBase.NOT_SET:
                _params['page_size'] = page_size
            if ascending_order is not ShapeBase.NOT_SET:
                _params['ascending_order'] = ascending_order
            _request = shapes.ListPrincipalPoliciesRequest(**_params)
        paginator = self.get_paginator("list_principal_policies").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListPrincipalPoliciesResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListPrincipalPoliciesResponse.from_boto(response)

    def list_principal_things(
        self,
        _request: shapes.ListPrincipalThingsRequest = None,
        *,
        principal: str,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.ListPrincipalThingsResponse:
        """
        Lists the things associated with the specified principal.
        """
        if _request is None:
            _params = {}
            if principal is not ShapeBase.NOT_SET:
                _params['principal'] = principal
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.ListPrincipalThingsRequest(**_params)
        paginator = self.get_paginator("list_principal_things").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListPrincipalThingsResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListPrincipalThingsResponse.from_boto(response)

    def list_role_aliases(
        self,
        _request: shapes.ListRoleAliasesRequest = None,
        *,
        page_size: int = ShapeBase.NOT_SET,
        marker: str = ShapeBase.NOT_SET,
        ascending_order: bool = ShapeBase.NOT_SET,
    ) -> shapes.ListRoleAliasesResponse:
        """
        Lists the role aliases registered in your account.
        """
        if _request is None:
            _params = {}
            if page_size is not ShapeBase.NOT_SET:
                _params['page_size'] = page_size
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            if ascending_order is not ShapeBase.NOT_SET:
                _params['ascending_order'] = ascending_order
            _request = shapes.ListRoleAliasesRequest(**_params)
        response = self._boto_client.list_role_aliases(**_request.to_boto())

        return shapes.ListRoleAliasesResponse.from_boto(response)

    def list_scheduled_audits(
        self,
        _request: shapes.ListScheduledAuditsRequest = None,
        *,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.ListScheduledAuditsResponse:
        """
        Lists all of your scheduled audits.
        """
        if _request is None:
            _params = {}
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.ListScheduledAuditsRequest(**_params)
        response = self._boto_client.list_scheduled_audits(**_request.to_boto())

        return shapes.ListScheduledAuditsResponse.from_boto(response)

    def list_security_profiles(
        self,
        _request: shapes.ListSecurityProfilesRequest = None,
        *,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.ListSecurityProfilesResponse:
        """
        Lists the Device Defender security profiles you have created. You can use
        filters to list only those security profiles associated with a thing group or
        only those associated with your account.
        """
        if _request is None:
            _params = {}
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.ListSecurityProfilesRequest(**_params)
        response = self._boto_client.list_security_profiles(
            **_request.to_boto()
        )

        return shapes.ListSecurityProfilesResponse.from_boto(response)

    def list_security_profiles_for_target(
        self,
        _request: shapes.ListSecurityProfilesForTargetRequest = None,
        *,
        security_profile_target_arn: str,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        recursive: bool = ShapeBase.NOT_SET,
    ) -> shapes.ListSecurityProfilesForTargetResponse:
        """
        Lists the Device Defender security profiles attached to a target (thing group).
        """
        if _request is None:
            _params = {}
            if security_profile_target_arn is not ShapeBase.NOT_SET:
                _params['security_profile_target_arn'
                       ] = security_profile_target_arn
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if recursive is not ShapeBase.NOT_SET:
                _params['recursive'] = recursive
            _request = shapes.ListSecurityProfilesForTargetRequest(**_params)
        response = self._boto_client.list_security_profiles_for_target(
            **_request.to_boto()
        )

        return shapes.ListSecurityProfilesForTargetResponse.from_boto(response)

    def list_streams(
        self,
        _request: shapes.ListStreamsRequest = None,
        *,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        ascending_order: bool = ShapeBase.NOT_SET,
    ) -> shapes.ListStreamsResponse:
        """
        Lists all of the streams in your AWS account.
        """
        if _request is None:
            _params = {}
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if ascending_order is not ShapeBase.NOT_SET:
                _params['ascending_order'] = ascending_order
            _request = shapes.ListStreamsRequest(**_params)
        response = self._boto_client.list_streams(**_request.to_boto())

        return shapes.ListStreamsResponse.from_boto(response)

    def list_targets_for_policy(
        self,
        _request: shapes.ListTargetsForPolicyRequest = None,
        *,
        policy_name: str,
        marker: str = ShapeBase.NOT_SET,
        page_size: int = ShapeBase.NOT_SET,
    ) -> shapes.ListTargetsForPolicyResponse:
        """
        List targets for the specified policy.
        """
        if _request is None:
            _params = {}
            if policy_name is not ShapeBase.NOT_SET:
                _params['policy_name'] = policy_name
            if marker is not ShapeBase.NOT_SET:
                _params['marker'] = marker
            if page_size is not ShapeBase.NOT_SET:
                _params['page_size'] = page_size
            _request = shapes.ListTargetsForPolicyRequest(**_params)
        response = self._boto_client.list_targets_for_policy(
            **_request.to_boto()
        )

        return shapes.ListTargetsForPolicyResponse.from_boto(response)

    def list_targets_for_security_profile(
        self,
        _request: shapes.ListTargetsForSecurityProfileRequest = None,
        *,
        security_profile_name: str,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.ListTargetsForSecurityProfileResponse:
        """
        Lists the targets (thing groups) associated with a given Device Defender
        security profile.
        """
        if _request is None:
            _params = {}
            if security_profile_name is not ShapeBase.NOT_SET:
                _params['security_profile_name'] = security_profile_name
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.ListTargetsForSecurityProfileRequest(**_params)
        response = self._boto_client.list_targets_for_security_profile(
            **_request.to_boto()
        )

        return shapes.ListTargetsForSecurityProfileResponse.from_boto(response)

    def list_thing_groups(
        self,
        _request: shapes.ListThingGroupsRequest = None,
        *,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        parent_group: str = ShapeBase.NOT_SET,
        name_prefix_filter: str = ShapeBase.NOT_SET,
        recursive: bool = ShapeBase.NOT_SET,
    ) -> shapes.ListThingGroupsResponse:
        """
        List the thing groups in your account.
        """
        if _request is None:
            _params = {}
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if parent_group is not ShapeBase.NOT_SET:
                _params['parent_group'] = parent_group
            if name_prefix_filter is not ShapeBase.NOT_SET:
                _params['name_prefix_filter'] = name_prefix_filter
            if recursive is not ShapeBase.NOT_SET:
                _params['recursive'] = recursive
            _request = shapes.ListThingGroupsRequest(**_params)
        response = self._boto_client.list_thing_groups(**_request.to_boto())

        return shapes.ListThingGroupsResponse.from_boto(response)

    def list_thing_groups_for_thing(
        self,
        _request: shapes.ListThingGroupsForThingRequest = None,
        *,
        thing_name: str,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.ListThingGroupsForThingResponse:
        """
        List the thing groups to which the specified thing belongs.
        """
        if _request is None:
            _params = {}
            if thing_name is not ShapeBase.NOT_SET:
                _params['thing_name'] = thing_name
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.ListThingGroupsForThingRequest(**_params)
        response = self._boto_client.list_thing_groups_for_thing(
            **_request.to_boto()
        )

        return shapes.ListThingGroupsForThingResponse.from_boto(response)

    def list_thing_principals(
        self,
        _request: shapes.ListThingPrincipalsRequest = None,
        *,
        thing_name: str,
    ) -> shapes.ListThingPrincipalsResponse:
        """
        Lists the principals associated with the specified thing.
        """
        if _request is None:
            _params = {}
            if thing_name is not ShapeBase.NOT_SET:
                _params['thing_name'] = thing_name
            _request = shapes.ListThingPrincipalsRequest(**_params)
        response = self._boto_client.list_thing_principals(**_request.to_boto())

        return shapes.ListThingPrincipalsResponse.from_boto(response)

    def list_thing_registration_task_reports(
        self,
        _request: shapes.ListThingRegistrationTaskReportsRequest = None,
        *,
        task_id: str,
        report_type: typing.Union[str, shapes.ReportType],
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.ListThingRegistrationTaskReportsResponse:
        """
        Information about the thing registration tasks.
        """
        if _request is None:
            _params = {}
            if task_id is not ShapeBase.NOT_SET:
                _params['task_id'] = task_id
            if report_type is not ShapeBase.NOT_SET:
                _params['report_type'] = report_type
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.ListThingRegistrationTaskReportsRequest(**_params)
        response = self._boto_client.list_thing_registration_task_reports(
            **_request.to_boto()
        )

        return shapes.ListThingRegistrationTaskReportsResponse.from_boto(
            response
        )

    def list_thing_registration_tasks(
        self,
        _request: shapes.ListThingRegistrationTasksRequest = None,
        *,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        status: typing.Union[str, shapes.Status] = ShapeBase.NOT_SET,
    ) -> shapes.ListThingRegistrationTasksResponse:
        """
        List bulk thing provisioning tasks.
        """
        if _request is None:
            _params = {}
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if status is not ShapeBase.NOT_SET:
                _params['status'] = status
            _request = shapes.ListThingRegistrationTasksRequest(**_params)
        response = self._boto_client.list_thing_registration_tasks(
            **_request.to_boto()
        )

        return shapes.ListThingRegistrationTasksResponse.from_boto(response)

    def list_thing_types(
        self,
        _request: shapes.ListThingTypesRequest = None,
        *,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        thing_type_name: str = ShapeBase.NOT_SET,
    ) -> shapes.ListThingTypesResponse:
        """
        Lists the existing thing types.
        """
        if _request is None:
            _params = {}
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if thing_type_name is not ShapeBase.NOT_SET:
                _params['thing_type_name'] = thing_type_name
            _request = shapes.ListThingTypesRequest(**_params)
        paginator = self.get_paginator("list_thing_types").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListThingTypesResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListThingTypesResponse.from_boto(response)

    def list_things(
        self,
        _request: shapes.ListThingsRequest = None,
        *,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        attribute_name: str = ShapeBase.NOT_SET,
        attribute_value: str = ShapeBase.NOT_SET,
        thing_type_name: str = ShapeBase.NOT_SET,
    ) -> shapes.ListThingsResponse:
        """
        Lists your things. Use the **attributeName** and **attributeValue** parameters
        to filter your things. For example, calling `ListThings` with
        attributeName=Color and attributeValue=Red retrieves all things in the registry
        that contain an attribute **Color** with the value **Red**.
        """
        if _request is None:
            _params = {}
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if attribute_name is not ShapeBase.NOT_SET:
                _params['attribute_name'] = attribute_name
            if attribute_value is not ShapeBase.NOT_SET:
                _params['attribute_value'] = attribute_value
            if thing_type_name is not ShapeBase.NOT_SET:
                _params['thing_type_name'] = thing_type_name
            _request = shapes.ListThingsRequest(**_params)
        paginator = self.get_paginator("list_things").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListThingsResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListThingsResponse.from_boto(response)

    def list_things_in_thing_group(
        self,
        _request: shapes.ListThingsInThingGroupRequest = None,
        *,
        thing_group_name: str,
        recursive: bool = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.ListThingsInThingGroupResponse:
        """
        Lists the things in the specified group.
        """
        if _request is None:
            _params = {}
            if thing_group_name is not ShapeBase.NOT_SET:
                _params['thing_group_name'] = thing_group_name
            if recursive is not ShapeBase.NOT_SET:
                _params['recursive'] = recursive
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.ListThingsInThingGroupRequest(**_params)
        response = self._boto_client.list_things_in_thing_group(
            **_request.to_boto()
        )

        return shapes.ListThingsInThingGroupResponse.from_boto(response)

    def list_topic_rules(
        self,
        _request: shapes.ListTopicRulesRequest = None,
        *,
        topic: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        rule_disabled: bool = ShapeBase.NOT_SET,
    ) -> shapes.ListTopicRulesResponse:
        """
        Lists the rules for the specific topic.
        """
        if _request is None:
            _params = {}
            if topic is not ShapeBase.NOT_SET:
                _params['topic'] = topic
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if rule_disabled is not ShapeBase.NOT_SET:
                _params['rule_disabled'] = rule_disabled
            _request = shapes.ListTopicRulesRequest(**_params)
        paginator = self.get_paginator("list_topic_rules").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListTopicRulesResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListTopicRulesResponse.from_boto(response)

    def list_v2_logging_levels(
        self,
        _request: shapes.ListV2LoggingLevelsRequest = None,
        *,
        target_type: typing.Union[str, shapes.LogTargetType] = ShapeBase.
        NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.ListV2LoggingLevelsResponse:
        """
        Lists logging levels.
        """
        if _request is None:
            _params = {}
            if target_type is not ShapeBase.NOT_SET:
                _params['target_type'] = target_type
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.ListV2LoggingLevelsRequest(**_params)
        response = self._boto_client.list_v2_logging_levels(
            **_request.to_boto()
        )

        return shapes.ListV2LoggingLevelsResponse.from_boto(response)

    def list_violation_events(
        self,
        _request: shapes.ListViolationEventsRequest = None,
        *,
        start_time: datetime.datetime,
        end_time: datetime.datetime,
        thing_name: str = ShapeBase.NOT_SET,
        security_profile_name: str = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.ListViolationEventsResponse:
        """
        Lists the Device Defender security profile violations discovered during the
        given time period. You can use filters to limit the results to those alerts
        issued for a particular security profile, behavior or thing (device).
        """
        if _request is None:
            _params = {}
            if start_time is not ShapeBase.NOT_SET:
                _params['start_time'] = start_time
            if end_time is not ShapeBase.NOT_SET:
                _params['end_time'] = end_time
            if thing_name is not ShapeBase.NOT_SET:
                _params['thing_name'] = thing_name
            if security_profile_name is not ShapeBase.NOT_SET:
                _params['security_profile_name'] = security_profile_name
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.ListViolationEventsRequest(**_params)
        response = self._boto_client.list_violation_events(**_request.to_boto())

        return shapes.ListViolationEventsResponse.from_boto(response)

    def register_ca_certificate(
        self,
        _request: shapes.RegisterCACertificateRequest = None,
        *,
        ca_certificate: str,
        verification_certificate: str,
        set_as_active: bool = ShapeBase.NOT_SET,
        allow_auto_registration: bool = ShapeBase.NOT_SET,
        registration_config: shapes.RegistrationConfig = ShapeBase.NOT_SET,
    ) -> shapes.RegisterCACertificateResponse:
        """
        Registers a CA certificate with AWS IoT. This CA certificate can then be used to
        sign device certificates, which can be then registered with AWS IoT. You can
        register up to 10 CA certificates per AWS account that have the same subject
        field. This enables you to have up to 10 certificate authorities sign your
        device certificates. If you have more than one CA certificate registered, make
        sure you pass the CA certificate when you register your device certificates with
        the RegisterCertificate API.
        """
        if _request is None:
            _params = {}
            if ca_certificate is not ShapeBase.NOT_SET:
                _params['ca_certificate'] = ca_certificate
            if verification_certificate is not ShapeBase.NOT_SET:
                _params['verification_certificate'] = verification_certificate
            if set_as_active is not ShapeBase.NOT_SET:
                _params['set_as_active'] = set_as_active
            if allow_auto_registration is not ShapeBase.NOT_SET:
                _params['allow_auto_registration'] = allow_auto_registration
            if registration_config is not ShapeBase.NOT_SET:
                _params['registration_config'] = registration_config
            _request = shapes.RegisterCACertificateRequest(**_params)
        response = self._boto_client.register_ca_certificate(
            **_request.to_boto()
        )

        return shapes.RegisterCACertificateResponse.from_boto(response)

    def register_certificate(
        self,
        _request: shapes.RegisterCertificateRequest = None,
        *,
        certificate_pem: str,
        ca_certificate_pem: str = ShapeBase.NOT_SET,
        set_as_active: bool = ShapeBase.NOT_SET,
        status: typing.Union[str, shapes.CertificateStatus] = ShapeBase.NOT_SET,
    ) -> shapes.RegisterCertificateResponse:
        """
        Registers a device certificate with AWS IoT. If you have more than one CA
        certificate that has the same subject field, you must specify the CA certificate
        that was used to sign the device certificate being registered.
        """
        if _request is None:
            _params = {}
            if certificate_pem is not ShapeBase.NOT_SET:
                _params['certificate_pem'] = certificate_pem
            if ca_certificate_pem is not ShapeBase.NOT_SET:
                _params['ca_certificate_pem'] = ca_certificate_pem
            if set_as_active is not ShapeBase.NOT_SET:
                _params['set_as_active'] = set_as_active
            if status is not ShapeBase.NOT_SET:
                _params['status'] = status
            _request = shapes.RegisterCertificateRequest(**_params)
        response = self._boto_client.register_certificate(**_request.to_boto())

        return shapes.RegisterCertificateResponse.from_boto(response)

    def register_thing(
        self,
        _request: shapes.RegisterThingRequest = None,
        *,
        template_body: str,
        parameters: typing.Dict[str, str] = ShapeBase.NOT_SET,
    ) -> shapes.RegisterThingResponse:
        """
        Provisions a thing.
        """
        if _request is None:
            _params = {}
            if template_body is not ShapeBase.NOT_SET:
                _params['template_body'] = template_body
            if parameters is not ShapeBase.NOT_SET:
                _params['parameters'] = parameters
            _request = shapes.RegisterThingRequest(**_params)
        response = self._boto_client.register_thing(**_request.to_boto())

        return shapes.RegisterThingResponse.from_boto(response)

    def reject_certificate_transfer(
        self,
        _request: shapes.RejectCertificateTransferRequest = None,
        *,
        certificate_id: str,
        reject_reason: str = ShapeBase.NOT_SET,
    ) -> None:
        """
        Rejects a pending certificate transfer. After AWS IoT rejects a certificate
        transfer, the certificate status changes from **PENDING_TRANSFER** to
        **INACTIVE**.

        To check for pending certificate transfers, call ListCertificates to enumerate
        your certificates.

        This operation can only be called by the transfer destination. After it is
        called, the certificate will be returned to the source's account in the INACTIVE
        state.
        """
        if _request is None:
            _params = {}
            if certificate_id is not ShapeBase.NOT_SET:
                _params['certificate_id'] = certificate_id
            if reject_reason is not ShapeBase.NOT_SET:
                _params['reject_reason'] = reject_reason
            _request = shapes.RejectCertificateTransferRequest(**_params)
        response = self._boto_client.reject_certificate_transfer(
            **_request.to_boto()
        )

    def remove_thing_from_thing_group(
        self,
        _request: shapes.RemoveThingFromThingGroupRequest = None,
        *,
        thing_group_name: str = ShapeBase.NOT_SET,
        thing_group_arn: str = ShapeBase.NOT_SET,
        thing_name: str = ShapeBase.NOT_SET,
        thing_arn: str = ShapeBase.NOT_SET,
    ) -> shapes.RemoveThingFromThingGroupResponse:
        """
        Remove the specified thing from the specified group.
        """
        if _request is None:
            _params = {}
            if thing_group_name is not ShapeBase.NOT_SET:
                _params['thing_group_name'] = thing_group_name
            if thing_group_arn is not ShapeBase.NOT_SET:
                _params['thing_group_arn'] = thing_group_arn
            if thing_name is not ShapeBase.NOT_SET:
                _params['thing_name'] = thing_name
            if thing_arn is not ShapeBase.NOT_SET:
                _params['thing_arn'] = thing_arn
            _request = shapes.RemoveThingFromThingGroupRequest(**_params)
        response = self._boto_client.remove_thing_from_thing_group(
            **_request.to_boto()
        )

        return shapes.RemoveThingFromThingGroupResponse.from_boto(response)

    def replace_topic_rule(
        self,
        _request: shapes.ReplaceTopicRuleRequest = None,
        *,
        rule_name: str,
        topic_rule_payload: shapes.TopicRulePayload,
    ) -> None:
        """
        Replaces the rule. You must specify all parameters for the new rule. Creating
        rules is an administrator-level action. Any user who has permission to create
        rules will be able to access data processed by the rule.
        """
        if _request is None:
            _params = {}
            if rule_name is not ShapeBase.NOT_SET:
                _params['rule_name'] = rule_name
            if topic_rule_payload is not ShapeBase.NOT_SET:
                _params['topic_rule_payload'] = topic_rule_payload
            _request = shapes.ReplaceTopicRuleRequest(**_params)
        response = self._boto_client.replace_topic_rule(**_request.to_boto())

    def search_index(
        self,
        _request: shapes.SearchIndexRequest = None,
        *,
        query_string: str,
        index_name: str = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        query_version: str = ShapeBase.NOT_SET,
    ) -> shapes.SearchIndexResponse:
        """
        The query search index.
        """
        if _request is None:
            _params = {}
            if query_string is not ShapeBase.NOT_SET:
                _params['query_string'] = query_string
            if index_name is not ShapeBase.NOT_SET:
                _params['index_name'] = index_name
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if query_version is not ShapeBase.NOT_SET:
                _params['query_version'] = query_version
            _request = shapes.SearchIndexRequest(**_params)
        response = self._boto_client.search_index(**_request.to_boto())

        return shapes.SearchIndexResponse.from_boto(response)

    def set_default_authorizer(
        self,
        _request: shapes.SetDefaultAuthorizerRequest = None,
        *,
        authorizer_name: str,
    ) -> shapes.SetDefaultAuthorizerResponse:
        """
        Sets the default authorizer. This will be used if a websocket connection is made
        without specifying an authorizer.
        """
        if _request is None:
            _params = {}
            if authorizer_name is not ShapeBase.NOT_SET:
                _params['authorizer_name'] = authorizer_name
            _request = shapes.SetDefaultAuthorizerRequest(**_params)
        response = self._boto_client.set_default_authorizer(
            **_request.to_boto()
        )

        return shapes.SetDefaultAuthorizerResponse.from_boto(response)

    def set_default_policy_version(
        self,
        _request: shapes.SetDefaultPolicyVersionRequest = None,
        *,
        policy_name: str,
        policy_version_id: str,
    ) -> None:
        """
        Sets the specified version of the specified policy as the policy's default
        (operative) version. This action affects all certificates to which the policy is
        attached. To list the principals the policy is attached to, use the
        ListPrincipalPolicy API.
        """
        if _request is None:
            _params = {}
            if policy_name is not ShapeBase.NOT_SET:
                _params['policy_name'] = policy_name
            if policy_version_id is not ShapeBase.NOT_SET:
                _params['policy_version_id'] = policy_version_id
            _request = shapes.SetDefaultPolicyVersionRequest(**_params)
        response = self._boto_client.set_default_policy_version(
            **_request.to_boto()
        )

    def set_logging_options(
        self,
        _request: shapes.SetLoggingOptionsRequest = None,
        *,
        logging_options_payload: shapes.LoggingOptionsPayload,
    ) -> None:
        """
        Sets the logging options.

        NOTE: use of this command is not recommended. Use `SetV2LoggingOptions` instead.
        """
        if _request is None:
            _params = {}
            if logging_options_payload is not ShapeBase.NOT_SET:
                _params['logging_options_payload'] = logging_options_payload
            _request = shapes.SetLoggingOptionsRequest(**_params)
        response = self._boto_client.set_logging_options(**_request.to_boto())

    def set_v2_logging_level(
        self,
        _request: shapes.SetV2LoggingLevelRequest = None,
        *,
        log_target: shapes.LogTarget,
        log_level: typing.Union[str, shapes.LogLevel],
    ) -> None:
        """
        Sets the logging level.
        """
        if _request is None:
            _params = {}
            if log_target is not ShapeBase.NOT_SET:
                _params['log_target'] = log_target
            if log_level is not ShapeBase.NOT_SET:
                _params['log_level'] = log_level
            _request = shapes.SetV2LoggingLevelRequest(**_params)
        response = self._boto_client.set_v2_logging_level(**_request.to_boto())

    def set_v2_logging_options(
        self,
        _request: shapes.SetV2LoggingOptionsRequest = None,
        *,
        role_arn: str = ShapeBase.NOT_SET,
        default_log_level: typing.Union[str, shapes.LogLevel] = ShapeBase.
        NOT_SET,
        disable_all_logs: bool = ShapeBase.NOT_SET,
    ) -> None:
        """
        Sets the logging options for the V2 logging service.
        """
        if _request is None:
            _params = {}
            if role_arn is not ShapeBase.NOT_SET:
                _params['role_arn'] = role_arn
            if default_log_level is not ShapeBase.NOT_SET:
                _params['default_log_level'] = default_log_level
            if disable_all_logs is not ShapeBase.NOT_SET:
                _params['disable_all_logs'] = disable_all_logs
            _request = shapes.SetV2LoggingOptionsRequest(**_params)
        response = self._boto_client.set_v2_logging_options(
            **_request.to_boto()
        )

    def start_on_demand_audit_task(
        self,
        _request: shapes.StartOnDemandAuditTaskRequest = None,
        *,
        target_check_names: typing.List[str],
    ) -> shapes.StartOnDemandAuditTaskResponse:
        """
        Starts an on-demand Device Defender audit.
        """
        if _request is None:
            _params = {}
            if target_check_names is not ShapeBase.NOT_SET:
                _params['target_check_names'] = target_check_names
            _request = shapes.StartOnDemandAuditTaskRequest(**_params)
        response = self._boto_client.start_on_demand_audit_task(
            **_request.to_boto()
        )

        return shapes.StartOnDemandAuditTaskResponse.from_boto(response)

    def start_thing_registration_task(
        self,
        _request: shapes.StartThingRegistrationTaskRequest = None,
        *,
        template_body: str,
        input_file_bucket: str,
        input_file_key: str,
        role_arn: str,
    ) -> shapes.StartThingRegistrationTaskResponse:
        """
        Creates a bulk thing provisioning task.
        """
        if _request is None:
            _params = {}
            if template_body is not ShapeBase.NOT_SET:
                _params['template_body'] = template_body
            if input_file_bucket is not ShapeBase.NOT_SET:
                _params['input_file_bucket'] = input_file_bucket
            if input_file_key is not ShapeBase.NOT_SET:
                _params['input_file_key'] = input_file_key
            if role_arn is not ShapeBase.NOT_SET:
                _params['role_arn'] = role_arn
            _request = shapes.StartThingRegistrationTaskRequest(**_params)
        response = self._boto_client.start_thing_registration_task(
            **_request.to_boto()
        )

        return shapes.StartThingRegistrationTaskResponse.from_boto(response)

    def stop_thing_registration_task(
        self,
        _request: shapes.StopThingRegistrationTaskRequest = None,
        *,
        task_id: str,
    ) -> shapes.StopThingRegistrationTaskResponse:
        """
        Cancels a bulk thing provisioning task.
        """
        if _request is None:
            _params = {}
            if task_id is not ShapeBase.NOT_SET:
                _params['task_id'] = task_id
            _request = shapes.StopThingRegistrationTaskRequest(**_params)
        response = self._boto_client.stop_thing_registration_task(
            **_request.to_boto()
        )

        return shapes.StopThingRegistrationTaskResponse.from_boto(response)

    def test_authorization(
        self,
        _request: shapes.TestAuthorizationRequest = None,
        *,
        auth_infos: typing.List[shapes.AuthInfo],
        principal: str = ShapeBase.NOT_SET,
        cognito_identity_pool_id: str = ShapeBase.NOT_SET,
        client_id: str = ShapeBase.NOT_SET,
        policy_names_to_add: typing.List[str] = ShapeBase.NOT_SET,
        policy_names_to_skip: typing.List[str] = ShapeBase.NOT_SET,
    ) -> shapes.TestAuthorizationResponse:
        """
        Tests if a specified principal is authorized to perform an AWS IoT action on a
        specified resource. Use this to test and debug the authorization behavior of
        devices that connect to the AWS IoT device gateway.
        """
        if _request is None:
            _params = {}
            if auth_infos is not ShapeBase.NOT_SET:
                _params['auth_infos'] = auth_infos
            if principal is not ShapeBase.NOT_SET:
                _params['principal'] = principal
            if cognito_identity_pool_id is not ShapeBase.NOT_SET:
                _params['cognito_identity_pool_id'] = cognito_identity_pool_id
            if client_id is not ShapeBase.NOT_SET:
                _params['client_id'] = client_id
            if policy_names_to_add is not ShapeBase.NOT_SET:
                _params['policy_names_to_add'] = policy_names_to_add
            if policy_names_to_skip is not ShapeBase.NOT_SET:
                _params['policy_names_to_skip'] = policy_names_to_skip
            _request = shapes.TestAuthorizationRequest(**_params)
        response = self._boto_client.test_authorization(**_request.to_boto())

        return shapes.TestAuthorizationResponse.from_boto(response)

    def test_invoke_authorizer(
        self,
        _request: shapes.TestInvokeAuthorizerRequest = None,
        *,
        authorizer_name: str,
        token: str,
        token_signature: str,
    ) -> shapes.TestInvokeAuthorizerResponse:
        """
        Tests a custom authorization behavior by invoking a specified custom authorizer.
        Use this to test and debug the custom authorization behavior of devices that
        connect to the AWS IoT device gateway.
        """
        if _request is None:
            _params = {}
            if authorizer_name is not ShapeBase.NOT_SET:
                _params['authorizer_name'] = authorizer_name
            if token is not ShapeBase.NOT_SET:
                _params['token'] = token
            if token_signature is not ShapeBase.NOT_SET:
                _params['token_signature'] = token_signature
            _request = shapes.TestInvokeAuthorizerRequest(**_params)
        response = self._boto_client.test_invoke_authorizer(
            **_request.to_boto()
        )

        return shapes.TestInvokeAuthorizerResponse.from_boto(response)

    def transfer_certificate(
        self,
        _request: shapes.TransferCertificateRequest = None,
        *,
        certificate_id: str,
        target_aws_account: str,
        transfer_message: str = ShapeBase.NOT_SET,
    ) -> shapes.TransferCertificateResponse:
        """
        Transfers the specified certificate to the specified AWS account.

        You can cancel the transfer until it is acknowledged by the recipient.

        No notification is sent to the transfer destination's account. It is up to the
        caller to notify the transfer target.

        The certificate being transferred must not be in the ACTIVE state. You can use
        the UpdateCertificate API to deactivate it.

        The certificate must not have any policies attached to it. You can use the
        DetachPrincipalPolicy API to detach them.
        """
        if _request is None:
            _params = {}
            if certificate_id is not ShapeBase.NOT_SET:
                _params['certificate_id'] = certificate_id
            if target_aws_account is not ShapeBase.NOT_SET:
                _params['target_aws_account'] = target_aws_account
            if transfer_message is not ShapeBase.NOT_SET:
                _params['transfer_message'] = transfer_message
            _request = shapes.TransferCertificateRequest(**_params)
        response = self._boto_client.transfer_certificate(**_request.to_boto())

        return shapes.TransferCertificateResponse.from_boto(response)

    def update_account_audit_configuration(
        self,
        _request: shapes.UpdateAccountAuditConfigurationRequest = None,
        *,
        role_arn: str = ShapeBase.NOT_SET,
        audit_notification_target_configurations: typing.
        Dict[typing.Union[str, shapes.AuditNotificationType], shapes.
             AuditNotificationTarget] = ShapeBase.NOT_SET,
        audit_check_configurations: typing.
        Dict[str, shapes.AuditCheckConfiguration] = ShapeBase.NOT_SET,
    ) -> shapes.UpdateAccountAuditConfigurationResponse:
        """
        Configures or reconfigures the Device Defender audit settings for this account.
        Settings include how audit notifications are sent and which audit checks are
        enabled or disabled.
        """
        if _request is None:
            _params = {}
            if role_arn is not ShapeBase.NOT_SET:
                _params['role_arn'] = role_arn
            if audit_notification_target_configurations is not ShapeBase.NOT_SET:
                _params['audit_notification_target_configurations'
                       ] = audit_notification_target_configurations
            if audit_check_configurations is not ShapeBase.NOT_SET:
                _params['audit_check_configurations'
                       ] = audit_check_configurations
            _request = shapes.UpdateAccountAuditConfigurationRequest(**_params)
        response = self._boto_client.update_account_audit_configuration(
            **_request.to_boto()
        )

        return shapes.UpdateAccountAuditConfigurationResponse.from_boto(
            response
        )

    def update_authorizer(
        self,
        _request: shapes.UpdateAuthorizerRequest = None,
        *,
        authorizer_name: str,
        authorizer_function_arn: str = ShapeBase.NOT_SET,
        token_key_name: str = ShapeBase.NOT_SET,
        token_signing_public_keys: typing.Dict[str, str] = ShapeBase.NOT_SET,
        status: typing.Union[str, shapes.AuthorizerStatus] = ShapeBase.NOT_SET,
    ) -> shapes.UpdateAuthorizerResponse:
        """
        Updates an authorizer.
        """
        if _request is None:
            _params = {}
            if authorizer_name is not ShapeBase.NOT_SET:
                _params['authorizer_name'] = authorizer_name
            if authorizer_function_arn is not ShapeBase.NOT_SET:
                _params['authorizer_function_arn'] = authorizer_function_arn
            if token_key_name is not ShapeBase.NOT_SET:
                _params['token_key_name'] = token_key_name
            if token_signing_public_keys is not ShapeBase.NOT_SET:
                _params['token_signing_public_keys'] = token_signing_public_keys
            if status is not ShapeBase.NOT_SET:
                _params['status'] = status
            _request = shapes.UpdateAuthorizerRequest(**_params)
        response = self._boto_client.update_authorizer(**_request.to_boto())

        return shapes.UpdateAuthorizerResponse.from_boto(response)

    def update_ca_certificate(
        self,
        _request: shapes.UpdateCACertificateRequest = None,
        *,
        certificate_id: str,
        new_status: typing.Union[str, shapes.
                                 CACertificateStatus] = ShapeBase.NOT_SET,
        new_auto_registration_status: typing.
        Union[str, shapes.AutoRegistrationStatus] = ShapeBase.NOT_SET,
        registration_config: shapes.RegistrationConfig = ShapeBase.NOT_SET,
        remove_auto_registration: bool = ShapeBase.NOT_SET,
    ) -> None:
        """
        Updates a registered CA certificate.
        """
        if _request is None:
            _params = {}
            if certificate_id is not ShapeBase.NOT_SET:
                _params['certificate_id'] = certificate_id
            if new_status is not ShapeBase.NOT_SET:
                _params['new_status'] = new_status
            if new_auto_registration_status is not ShapeBase.NOT_SET:
                _params['new_auto_registration_status'
                       ] = new_auto_registration_status
            if registration_config is not ShapeBase.NOT_SET:
                _params['registration_config'] = registration_config
            if remove_auto_registration is not ShapeBase.NOT_SET:
                _params['remove_auto_registration'] = remove_auto_registration
            _request = shapes.UpdateCACertificateRequest(**_params)
        response = self._boto_client.update_ca_certificate(**_request.to_boto())

    def update_certificate(
        self,
        _request: shapes.UpdateCertificateRequest = None,
        *,
        certificate_id: str,
        new_status: typing.Union[str, shapes.CertificateStatus],
    ) -> None:
        """
        Updates the status of the specified certificate. This operation is idempotent.

        Moving a certificate from the ACTIVE state (including REVOKED) will not
        disconnect currently connected devices, but these devices will be unable to
        reconnect.

        The ACTIVE state is required to authenticate devices connecting to AWS IoT using
        a certificate.
        """
        if _request is None:
            _params = {}
            if certificate_id is not ShapeBase.NOT_SET:
                _params['certificate_id'] = certificate_id
            if new_status is not ShapeBase.NOT_SET:
                _params['new_status'] = new_status
            _request = shapes.UpdateCertificateRequest(**_params)
        response = self._boto_client.update_certificate(**_request.to_boto())

    def update_event_configurations(
        self,
        _request: shapes.UpdateEventConfigurationsRequest = None,
        *,
        event_configurations: typing.Dict[typing.Union[str, shapes.
                                                       EventType], shapes.
                                          Configuration] = ShapeBase.NOT_SET,
    ) -> shapes.UpdateEventConfigurationsResponse:
        """
        Updates the event configurations.
        """
        if _request is None:
            _params = {}
            if event_configurations is not ShapeBase.NOT_SET:
                _params['event_configurations'] = event_configurations
            _request = shapes.UpdateEventConfigurationsRequest(**_params)
        response = self._boto_client.update_event_configurations(
            **_request.to_boto()
        )

        return shapes.UpdateEventConfigurationsResponse.from_boto(response)

    def update_indexing_configuration(
        self,
        _request: shapes.UpdateIndexingConfigurationRequest = None,
        *,
        thing_indexing_configuration: shapes.
        ThingIndexingConfiguration = ShapeBase.NOT_SET,
        thing_group_indexing_configuration: shapes.
        ThingGroupIndexingConfiguration = ShapeBase.NOT_SET,
    ) -> shapes.UpdateIndexingConfigurationResponse:
        """
        Updates the search configuration.
        """
        if _request is None:
            _params = {}
            if thing_indexing_configuration is not ShapeBase.NOT_SET:
                _params['thing_indexing_configuration'
                       ] = thing_indexing_configuration
            if thing_group_indexing_configuration is not ShapeBase.NOT_SET:
                _params['thing_group_indexing_configuration'
                       ] = thing_group_indexing_configuration
            _request = shapes.UpdateIndexingConfigurationRequest(**_params)
        response = self._boto_client.update_indexing_configuration(
            **_request.to_boto()
        )

        return shapes.UpdateIndexingConfigurationResponse.from_boto(response)

    def update_role_alias(
        self,
        _request: shapes.UpdateRoleAliasRequest = None,
        *,
        role_alias: str,
        role_arn: str = ShapeBase.NOT_SET,
        credential_duration_seconds: int = ShapeBase.NOT_SET,
    ) -> shapes.UpdateRoleAliasResponse:
        """
        Updates a role alias.
        """
        if _request is None:
            _params = {}
            if role_alias is not ShapeBase.NOT_SET:
                _params['role_alias'] = role_alias
            if role_arn is not ShapeBase.NOT_SET:
                _params['role_arn'] = role_arn
            if credential_duration_seconds is not ShapeBase.NOT_SET:
                _params['credential_duration_seconds'
                       ] = credential_duration_seconds
            _request = shapes.UpdateRoleAliasRequest(**_params)
        response = self._boto_client.update_role_alias(**_request.to_boto())

        return shapes.UpdateRoleAliasResponse.from_boto(response)

    def update_scheduled_audit(
        self,
        _request: shapes.UpdateScheduledAuditRequest = None,
        *,
        scheduled_audit_name: str,
        frequency: typing.Union[str, shapes.AuditFrequency] = ShapeBase.NOT_SET,
        day_of_month: str = ShapeBase.NOT_SET,
        day_of_week: typing.Union[str, shapes.DayOfWeek] = ShapeBase.NOT_SET,
        target_check_names: typing.List[str] = ShapeBase.NOT_SET,
    ) -> shapes.UpdateScheduledAuditResponse:
        """
        Updates a scheduled audit, including what checks are performed and how often the
        audit takes place.
        """
        if _request is None:
            _params = {}
            if scheduled_audit_name is not ShapeBase.NOT_SET:
                _params['scheduled_audit_name'] = scheduled_audit_name
            if frequency is not ShapeBase.NOT_SET:
                _params['frequency'] = frequency
            if day_of_month is not ShapeBase.NOT_SET:
                _params['day_of_month'] = day_of_month
            if day_of_week is not ShapeBase.NOT_SET:
                _params['day_of_week'] = day_of_week
            if target_check_names is not ShapeBase.NOT_SET:
                _params['target_check_names'] = target_check_names
            _request = shapes.UpdateScheduledAuditRequest(**_params)
        response = self._boto_client.update_scheduled_audit(
            **_request.to_boto()
        )

        return shapes.UpdateScheduledAuditResponse.from_boto(response)

    def update_security_profile(
        self,
        _request: shapes.UpdateSecurityProfileRequest = None,
        *,
        security_profile_name: str,
        security_profile_description: str = ShapeBase.NOT_SET,
        behaviors: typing.List[shapes.Behavior] = ShapeBase.NOT_SET,
        alert_targets: typing.Dict[typing.Union[str, shapes.AlertTargetType],
                                   shapes.AlertTarget] = ShapeBase.NOT_SET,
        expected_version: int = ShapeBase.NOT_SET,
    ) -> shapes.UpdateSecurityProfileResponse:
        """
        Updates a Device Defender security profile.
        """
        if _request is None:
            _params = {}
            if security_profile_name is not ShapeBase.NOT_SET:
                _params['security_profile_name'] = security_profile_name
            if security_profile_description is not ShapeBase.NOT_SET:
                _params['security_profile_description'
                       ] = security_profile_description
            if behaviors is not ShapeBase.NOT_SET:
                _params['behaviors'] = behaviors
            if alert_targets is not ShapeBase.NOT_SET:
                _params['alert_targets'] = alert_targets
            if expected_version is not ShapeBase.NOT_SET:
                _params['expected_version'] = expected_version
            _request = shapes.UpdateSecurityProfileRequest(**_params)
        response = self._boto_client.update_security_profile(
            **_request.to_boto()
        )

        return shapes.UpdateSecurityProfileResponse.from_boto(response)

    def update_stream(
        self,
        _request: shapes.UpdateStreamRequest = None,
        *,
        stream_id: str,
        description: str = ShapeBase.NOT_SET,
        files: typing.List[shapes.StreamFile] = ShapeBase.NOT_SET,
        role_arn: str = ShapeBase.NOT_SET,
    ) -> shapes.UpdateStreamResponse:
        """
        Updates an existing stream. The stream version will be incremented by one.
        """
        if _request is None:
            _params = {}
            if stream_id is not ShapeBase.NOT_SET:
                _params['stream_id'] = stream_id
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if files is not ShapeBase.NOT_SET:
                _params['files'] = files
            if role_arn is not ShapeBase.NOT_SET:
                _params['role_arn'] = role_arn
            _request = shapes.UpdateStreamRequest(**_params)
        response = self._boto_client.update_stream(**_request.to_boto())

        return shapes.UpdateStreamResponse.from_boto(response)

    def update_thing(
        self,
        _request: shapes.UpdateThingRequest = None,
        *,
        thing_name: str,
        thing_type_name: str = ShapeBase.NOT_SET,
        attribute_payload: shapes.AttributePayload = ShapeBase.NOT_SET,
        expected_version: int = ShapeBase.NOT_SET,
        remove_thing_type: bool = ShapeBase.NOT_SET,
    ) -> shapes.UpdateThingResponse:
        """
        Updates the data for a thing.
        """
        if _request is None:
            _params = {}
            if thing_name is not ShapeBase.NOT_SET:
                _params['thing_name'] = thing_name
            if thing_type_name is not ShapeBase.NOT_SET:
                _params['thing_type_name'] = thing_type_name
            if attribute_payload is not ShapeBase.NOT_SET:
                _params['attribute_payload'] = attribute_payload
            if expected_version is not ShapeBase.NOT_SET:
                _params['expected_version'] = expected_version
            if remove_thing_type is not ShapeBase.NOT_SET:
                _params['remove_thing_type'] = remove_thing_type
            _request = shapes.UpdateThingRequest(**_params)
        response = self._boto_client.update_thing(**_request.to_boto())

        return shapes.UpdateThingResponse.from_boto(response)

    def update_thing_group(
        self,
        _request: shapes.UpdateThingGroupRequest = None,
        *,
        thing_group_name: str,
        thing_group_properties: shapes.ThingGroupProperties,
        expected_version: int = ShapeBase.NOT_SET,
    ) -> shapes.UpdateThingGroupResponse:
        """
        Update a thing group.
        """
        if _request is None:
            _params = {}
            if thing_group_name is not ShapeBase.NOT_SET:
                _params['thing_group_name'] = thing_group_name
            if thing_group_properties is not ShapeBase.NOT_SET:
                _params['thing_group_properties'] = thing_group_properties
            if expected_version is not ShapeBase.NOT_SET:
                _params['expected_version'] = expected_version
            _request = shapes.UpdateThingGroupRequest(**_params)
        response = self._boto_client.update_thing_group(**_request.to_boto())

        return shapes.UpdateThingGroupResponse.from_boto(response)

    def update_thing_groups_for_thing(
        self,
        _request: shapes.UpdateThingGroupsForThingRequest = None,
        *,
        thing_name: str = ShapeBase.NOT_SET,
        thing_groups_to_add: typing.List[str] = ShapeBase.NOT_SET,
        thing_groups_to_remove: typing.List[str] = ShapeBase.NOT_SET,
    ) -> shapes.UpdateThingGroupsForThingResponse:
        """
        Updates the groups to which the thing belongs.
        """
        if _request is None:
            _params = {}
            if thing_name is not ShapeBase.NOT_SET:
                _params['thing_name'] = thing_name
            if thing_groups_to_add is not ShapeBase.NOT_SET:
                _params['thing_groups_to_add'] = thing_groups_to_add
            if thing_groups_to_remove is not ShapeBase.NOT_SET:
                _params['thing_groups_to_remove'] = thing_groups_to_remove
            _request = shapes.UpdateThingGroupsForThingRequest(**_params)
        response = self._boto_client.update_thing_groups_for_thing(
            **_request.to_boto()
        )

        return shapes.UpdateThingGroupsForThingResponse.from_boto(response)

    def validate_security_profile_behaviors(
        self,
        _request: shapes.ValidateSecurityProfileBehaviorsRequest = None,
        *,
        behaviors: typing.List[shapes.Behavior],
    ) -> shapes.ValidateSecurityProfileBehaviorsResponse:
        """
        Validates a Device Defender security profile behaviors specification.
        """
        if _request is None:
            _params = {}
            if behaviors is not ShapeBase.NOT_SET:
                _params['behaviors'] = behaviors
            _request = shapes.ValidateSecurityProfileBehaviorsRequest(**_params)
        response = self._boto_client.validate_security_profile_behaviors(
            **_request.to_boto()
        )

        return shapes.ValidateSecurityProfileBehaviorsResponse.from_boto(
            response
        )
