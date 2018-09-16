import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("mturk", *args, **kwargs)

    def accept_qualification_request(
        self,
        _request: shapes.AcceptQualificationRequestRequest = None,
        *,
        qualification_request_id: str,
        integer_value: int = ShapeBase.NOT_SET,
    ) -> shapes.AcceptQualificationRequestResponse:
        """
        The `AcceptQualificationRequest` operation approves a Worker's request for a
        Qualification.

        Only the owner of the Qualification type can grant a Qualification request for
        that type.

        A successful request for the `AcceptQualificationRequest` operation returns with
        no errors and an empty body.
        """
        if _request is None:
            _params = {}
            if qualification_request_id is not ShapeBase.NOT_SET:
                _params['qualification_request_id'] = qualification_request_id
            if integer_value is not ShapeBase.NOT_SET:
                _params['integer_value'] = integer_value
            _request = shapes.AcceptQualificationRequestRequest(**_params)
        response = self._boto_client.accept_qualification_request(
            **_request.to_boto()
        )

        return shapes.AcceptQualificationRequestResponse.from_boto(response)

    def approve_assignment(
        self,
        _request: shapes.ApproveAssignmentRequest = None,
        *,
        assignment_id: str,
        requester_feedback: str = ShapeBase.NOT_SET,
        override_rejection: bool = ShapeBase.NOT_SET,
    ) -> shapes.ApproveAssignmentResponse:
        """
        The `ApproveAssignment` operation approves the results of a completed
        assignment.

        Approving an assignment initiates two payments from the Requester's Amazon.com
        account

          * The Worker who submitted the results is paid the reward specified in the HIT. 

          * Amazon Mechanical Turk fees are debited. 

        If the Requester's account does not have adequate funds for these payments, the
        call to ApproveAssignment returns an exception, and the approval is not
        processed. You can include an optional feedback message with the approval, which
        the Worker can see in the Status section of the web site.

        You can also call this operation for assignments that were previous rejected and
        approve them by explicitly overriding the previous rejection. This only works on
        rejected assignments that were submitted within the previous 30 days and only if
        the assignment's related HIT has not been deleted.
        """
        if _request is None:
            _params = {}
            if assignment_id is not ShapeBase.NOT_SET:
                _params['assignment_id'] = assignment_id
            if requester_feedback is not ShapeBase.NOT_SET:
                _params['requester_feedback'] = requester_feedback
            if override_rejection is not ShapeBase.NOT_SET:
                _params['override_rejection'] = override_rejection
            _request = shapes.ApproveAssignmentRequest(**_params)
        response = self._boto_client.approve_assignment(**_request.to_boto())

        return shapes.ApproveAssignmentResponse.from_boto(response)

    def associate_qualification_with_worker(
        self,
        _request: shapes.AssociateQualificationWithWorkerRequest = None,
        *,
        qualification_type_id: str,
        worker_id: str,
        integer_value: int = ShapeBase.NOT_SET,
        send_notification: bool = ShapeBase.NOT_SET,
    ) -> shapes.AssociateQualificationWithWorkerResponse:
        """
        The `AssociateQualificationWithWorker` operation gives a Worker a Qualification.
        `AssociateQualificationWithWorker` does not require that the Worker submit a
        Qualification request. It gives the Qualification directly to the Worker.

        You can only assign a Qualification of a Qualification type that you created
        (using the `CreateQualificationType` operation).

        Note: `AssociateQualificationWithWorker` does not affect any pending
        Qualification requests for the Qualification by the Worker. If you assign a
        Qualification to a Worker, then later grant a Qualification request made by the
        Worker, the granting of the request may modify the Qualification score. To
        resolve a pending Qualification request without affecting the Qualification the
        Worker already has, reject the request with the `RejectQualificationRequest`
        operation.
        """
        if _request is None:
            _params = {}
            if qualification_type_id is not ShapeBase.NOT_SET:
                _params['qualification_type_id'] = qualification_type_id
            if worker_id is not ShapeBase.NOT_SET:
                _params['worker_id'] = worker_id
            if integer_value is not ShapeBase.NOT_SET:
                _params['integer_value'] = integer_value
            if send_notification is not ShapeBase.NOT_SET:
                _params['send_notification'] = send_notification
            _request = shapes.AssociateQualificationWithWorkerRequest(**_params)
        response = self._boto_client.associate_qualification_with_worker(
            **_request.to_boto()
        )

        return shapes.AssociateQualificationWithWorkerResponse.from_boto(
            response
        )

    def create_additional_assignments_for_hit(
        self,
        _request: shapes.CreateAdditionalAssignmentsForHITRequest = None,
        *,
        hit_id: str,
        number_of_additional_assignments: int,
        unique_request_token: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateAdditionalAssignmentsForHITResponse:
        """
        The `CreateAdditionalAssignmentsForHIT` operation increases the maximum number
        of assignments of an existing HIT.

        To extend the maximum number of assignments, specify the number of additional
        assignments.

          * HITs created with fewer than 10 assignments cannot be extended to have 10 or more assignments. Attempting to add assignments in a way that brings the total number of assignments for a HIT from fewer than 10 assignments to 10 or more assignments will result in an `AWS.MechanicalTurk.InvalidMaximumAssignmentsIncrease` exception.

          * HITs that were created before July 22, 2015 cannot be extended. Attempting to extend HITs that were created before July 22, 2015 will result in an `AWS.MechanicalTurk.HITTooOldForExtension` exception.
        """
        if _request is None:
            _params = {}
            if hit_id is not ShapeBase.NOT_SET:
                _params['hit_id'] = hit_id
            if number_of_additional_assignments is not ShapeBase.NOT_SET:
                _params['number_of_additional_assignments'
                       ] = number_of_additional_assignments
            if unique_request_token is not ShapeBase.NOT_SET:
                _params['unique_request_token'] = unique_request_token
            _request = shapes.CreateAdditionalAssignmentsForHITRequest(
                **_params
            )
        response = self._boto_client.create_additional_assignments_for_hit(
            **_request.to_boto()
        )

        return shapes.CreateAdditionalAssignmentsForHITResponse.from_boto(
            response
        )

    def create_hit(
        self,
        _request: shapes.CreateHITRequest = None,
        *,
        lifetime_in_seconds: int,
        assignment_duration_in_seconds: int,
        reward: str,
        title: str,
        description: str,
        max_assignments: int = ShapeBase.NOT_SET,
        auto_approval_delay_in_seconds: int = ShapeBase.NOT_SET,
        keywords: str = ShapeBase.NOT_SET,
        question: str = ShapeBase.NOT_SET,
        requester_annotation: str = ShapeBase.NOT_SET,
        qualification_requirements: typing.List[shapes.QualificationRequirement
                                               ] = ShapeBase.NOT_SET,
        unique_request_token: str = ShapeBase.NOT_SET,
        assignment_review_policy: shapes.ReviewPolicy = ShapeBase.NOT_SET,
        hit_review_policy: shapes.ReviewPolicy = ShapeBase.NOT_SET,
        hit_layout_id: str = ShapeBase.NOT_SET,
        hit_layout_parameters: typing.List[shapes.HITLayoutParameter
                                          ] = ShapeBase.NOT_SET,
    ) -> shapes.CreateHITResponse:
        """
        The `CreateHIT` operation creates a new Human Intelligence Task (HIT). The new
        HIT is made available for Workers to find and accept on the Amazon Mechanical
        Turk website.

        This operation allows you to specify a new HIT by passing in values for the
        properties of the HIT, such as its title, reward amount and number of
        assignments. When you pass these values to `CreateHIT`, a new HIT is created for
        you, with a new `HITTypeID`. The HITTypeID can be used to create additional HITs
        in the future without needing to specify common parameters such as the title,
        description and reward amount each time.

        An alternative way to create HITs is to first generate a HITTypeID using the
        `CreateHITType` operation and then call the `CreateHITWithHITType` operation.
        This is the recommended best practice for Requesters who are creating large
        numbers of HITs.

        CreateHIT also supports several ways to provide question data: by providing a
        value for the `Question` parameter that fully specifies the contents of the HIT,
        or by providing a `HitLayoutId` and associated `HitLayoutParameters`.

        If a HIT is created with 10 or more maximum assignments, there is an additional
        fee. For more information, see [Amazon Mechanical Turk
        Pricing](https://requester.mturk.com/pricing).
        """
        if _request is None:
            _params = {}
            if lifetime_in_seconds is not ShapeBase.NOT_SET:
                _params['lifetime_in_seconds'] = lifetime_in_seconds
            if assignment_duration_in_seconds is not ShapeBase.NOT_SET:
                _params['assignment_duration_in_seconds'
                       ] = assignment_duration_in_seconds
            if reward is not ShapeBase.NOT_SET:
                _params['reward'] = reward
            if title is not ShapeBase.NOT_SET:
                _params['title'] = title
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if max_assignments is not ShapeBase.NOT_SET:
                _params['max_assignments'] = max_assignments
            if auto_approval_delay_in_seconds is not ShapeBase.NOT_SET:
                _params['auto_approval_delay_in_seconds'
                       ] = auto_approval_delay_in_seconds
            if keywords is not ShapeBase.NOT_SET:
                _params['keywords'] = keywords
            if question is not ShapeBase.NOT_SET:
                _params['question'] = question
            if requester_annotation is not ShapeBase.NOT_SET:
                _params['requester_annotation'] = requester_annotation
            if qualification_requirements is not ShapeBase.NOT_SET:
                _params['qualification_requirements'
                       ] = qualification_requirements
            if unique_request_token is not ShapeBase.NOT_SET:
                _params['unique_request_token'] = unique_request_token
            if assignment_review_policy is not ShapeBase.NOT_SET:
                _params['assignment_review_policy'] = assignment_review_policy
            if hit_review_policy is not ShapeBase.NOT_SET:
                _params['hit_review_policy'] = hit_review_policy
            if hit_layout_id is not ShapeBase.NOT_SET:
                _params['hit_layout_id'] = hit_layout_id
            if hit_layout_parameters is not ShapeBase.NOT_SET:
                _params['hit_layout_parameters'] = hit_layout_parameters
            _request = shapes.CreateHITRequest(**_params)
        response = self._boto_client.create_hit(**_request.to_boto())

        return shapes.CreateHITResponse.from_boto(response)

    def create_hit_type(
        self,
        _request: shapes.CreateHITTypeRequest = None,
        *,
        assignment_duration_in_seconds: int,
        reward: str,
        title: str,
        description: str,
        auto_approval_delay_in_seconds: int = ShapeBase.NOT_SET,
        keywords: str = ShapeBase.NOT_SET,
        qualification_requirements: typing.List[shapes.QualificationRequirement
                                               ] = ShapeBase.NOT_SET,
    ) -> shapes.CreateHITTypeResponse:
        """
        The `CreateHITType` operation creates a new HIT type. This operation allows you
        to define a standard set of HIT properties to use when creating HITs. If you
        register a HIT type with values that match an existing HIT type, the HIT type ID
        of the existing type will be returned.
        """
        if _request is None:
            _params = {}
            if assignment_duration_in_seconds is not ShapeBase.NOT_SET:
                _params['assignment_duration_in_seconds'
                       ] = assignment_duration_in_seconds
            if reward is not ShapeBase.NOT_SET:
                _params['reward'] = reward
            if title is not ShapeBase.NOT_SET:
                _params['title'] = title
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if auto_approval_delay_in_seconds is not ShapeBase.NOT_SET:
                _params['auto_approval_delay_in_seconds'
                       ] = auto_approval_delay_in_seconds
            if keywords is not ShapeBase.NOT_SET:
                _params['keywords'] = keywords
            if qualification_requirements is not ShapeBase.NOT_SET:
                _params['qualification_requirements'
                       ] = qualification_requirements
            _request = shapes.CreateHITTypeRequest(**_params)
        response = self._boto_client.create_hit_type(**_request.to_boto())

        return shapes.CreateHITTypeResponse.from_boto(response)

    def create_hit_with_hit_type(
        self,
        _request: shapes.CreateHITWithHITTypeRequest = None,
        *,
        hit_type_id: str,
        lifetime_in_seconds: int,
        max_assignments: int = ShapeBase.NOT_SET,
        question: str = ShapeBase.NOT_SET,
        requester_annotation: str = ShapeBase.NOT_SET,
        unique_request_token: str = ShapeBase.NOT_SET,
        assignment_review_policy: shapes.ReviewPolicy = ShapeBase.NOT_SET,
        hit_review_policy: shapes.ReviewPolicy = ShapeBase.NOT_SET,
        hit_layout_id: str = ShapeBase.NOT_SET,
        hit_layout_parameters: typing.List[shapes.HITLayoutParameter
                                          ] = ShapeBase.NOT_SET,
    ) -> shapes.CreateHITWithHITTypeResponse:
        """
        The `CreateHITWithHITType` operation creates a new Human Intelligence Task (HIT)
        using an existing HITTypeID generated by the `CreateHITType` operation.

        This is an alternative way to create HITs from the `CreateHIT` operation. This
        is the recommended best practice for Requesters who are creating large numbers
        of HITs.

        CreateHITWithHITType also supports several ways to provide question data: by
        providing a value for the `Question` parameter that fully specifies the contents
        of the HIT, or by providing a `HitLayoutId` and associated
        `HitLayoutParameters`.

        If a HIT is created with 10 or more maximum assignments, there is an additional
        fee. For more information, see [Amazon Mechanical Turk
        Pricing](https://requester.mturk.com/pricing).
        """
        if _request is None:
            _params = {}
            if hit_type_id is not ShapeBase.NOT_SET:
                _params['hit_type_id'] = hit_type_id
            if lifetime_in_seconds is not ShapeBase.NOT_SET:
                _params['lifetime_in_seconds'] = lifetime_in_seconds
            if max_assignments is not ShapeBase.NOT_SET:
                _params['max_assignments'] = max_assignments
            if question is not ShapeBase.NOT_SET:
                _params['question'] = question
            if requester_annotation is not ShapeBase.NOT_SET:
                _params['requester_annotation'] = requester_annotation
            if unique_request_token is not ShapeBase.NOT_SET:
                _params['unique_request_token'] = unique_request_token
            if assignment_review_policy is not ShapeBase.NOT_SET:
                _params['assignment_review_policy'] = assignment_review_policy
            if hit_review_policy is not ShapeBase.NOT_SET:
                _params['hit_review_policy'] = hit_review_policy
            if hit_layout_id is not ShapeBase.NOT_SET:
                _params['hit_layout_id'] = hit_layout_id
            if hit_layout_parameters is not ShapeBase.NOT_SET:
                _params['hit_layout_parameters'] = hit_layout_parameters
            _request = shapes.CreateHITWithHITTypeRequest(**_params)
        response = self._boto_client.create_hit_with_hit_type(
            **_request.to_boto()
        )

        return shapes.CreateHITWithHITTypeResponse.from_boto(response)

    def create_qualification_type(
        self,
        _request: shapes.CreateQualificationTypeRequest = None,
        *,
        name: str,
        description: str,
        qualification_type_status: typing.Union[str, shapes.
                                                QualificationTypeStatus],
        keywords: str = ShapeBase.NOT_SET,
        retry_delay_in_seconds: int = ShapeBase.NOT_SET,
        test: str = ShapeBase.NOT_SET,
        answer_key: str = ShapeBase.NOT_SET,
        test_duration_in_seconds: int = ShapeBase.NOT_SET,
        auto_granted: bool = ShapeBase.NOT_SET,
        auto_granted_value: int = ShapeBase.NOT_SET,
    ) -> shapes.CreateQualificationTypeResponse:
        """
        The `CreateQualificationType` operation creates a new Qualification type, which
        is represented by a `QualificationType` data structure.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if qualification_type_status is not ShapeBase.NOT_SET:
                _params['qualification_type_status'] = qualification_type_status
            if keywords is not ShapeBase.NOT_SET:
                _params['keywords'] = keywords
            if retry_delay_in_seconds is not ShapeBase.NOT_SET:
                _params['retry_delay_in_seconds'] = retry_delay_in_seconds
            if test is not ShapeBase.NOT_SET:
                _params['test'] = test
            if answer_key is not ShapeBase.NOT_SET:
                _params['answer_key'] = answer_key
            if test_duration_in_seconds is not ShapeBase.NOT_SET:
                _params['test_duration_in_seconds'] = test_duration_in_seconds
            if auto_granted is not ShapeBase.NOT_SET:
                _params['auto_granted'] = auto_granted
            if auto_granted_value is not ShapeBase.NOT_SET:
                _params['auto_granted_value'] = auto_granted_value
            _request = shapes.CreateQualificationTypeRequest(**_params)
        response = self._boto_client.create_qualification_type(
            **_request.to_boto()
        )

        return shapes.CreateQualificationTypeResponse.from_boto(response)

    def create_worker_block(
        self,
        _request: shapes.CreateWorkerBlockRequest = None,
        *,
        worker_id: str,
        reason: str,
    ) -> shapes.CreateWorkerBlockResponse:
        """
        The `CreateWorkerBlock` operation allows you to prevent a Worker from working on
        your HITs. For example, you can block a Worker who is producing poor quality
        work. You can block up to 100,000 Workers.
        """
        if _request is None:
            _params = {}
            if worker_id is not ShapeBase.NOT_SET:
                _params['worker_id'] = worker_id
            if reason is not ShapeBase.NOT_SET:
                _params['reason'] = reason
            _request = shapes.CreateWorkerBlockRequest(**_params)
        response = self._boto_client.create_worker_block(**_request.to_boto())

        return shapes.CreateWorkerBlockResponse.from_boto(response)

    def delete_hit(
        self,
        _request: shapes.DeleteHITRequest = None,
        *,
        hit_id: str,
    ) -> shapes.DeleteHITResponse:
        """
        The `DeleteHIT` operation is used to delete HIT that is no longer needed. Only
        the Requester who created the HIT can delete it.

        You can only dispose of HITs that are in the `Reviewable` state, with all of
        their submitted assignments already either approved or rejected. If you call the
        DeleteHIT operation on a HIT that is not in the `Reviewable` state (for example,
        that has not expired, or still has active assignments), or on a HIT that is
        Reviewable but without all of its submitted assignments already approved or
        rejected, the service will return an error.

          * HITs are automatically disposed of after 120 days. 

          * After you dispose of a HIT, you can no longer approve the HIT's rejected assignments. 

          * Disposed HITs are not returned in results for the ListHITs operation. 

          * Disposing HITs can improve the performance of operations such as ListReviewableHITs and ListHITs.
        """
        if _request is None:
            _params = {}
            if hit_id is not ShapeBase.NOT_SET:
                _params['hit_id'] = hit_id
            _request = shapes.DeleteHITRequest(**_params)
        response = self._boto_client.delete_hit(**_request.to_boto())

        return shapes.DeleteHITResponse.from_boto(response)

    def delete_qualification_type(
        self,
        _request: shapes.DeleteQualificationTypeRequest = None,
        *,
        qualification_type_id: str,
    ) -> shapes.DeleteQualificationTypeResponse:
        """
        The `DeleteQualificationType` deletes a Qualification type and deletes any HIT
        types that are associated with the Qualification type.

        This operation does not revoke Qualifications already assigned to Workers
        because the Qualifications might be needed for active HITs. If there are any
        pending requests for the Qualification type, Amazon Mechanical Turk rejects
        those requests. After you delete a Qualification type, you can no longer use it
        to create HITs or HIT types.

        DeleteQualificationType must wait for all the HITs that use the deleted
        Qualification type to be deleted before completing. It may take up to 48 hours
        before DeleteQualificationType completes and the unique name of the
        Qualification type is available for reuse with CreateQualificationType.
        """
        if _request is None:
            _params = {}
            if qualification_type_id is not ShapeBase.NOT_SET:
                _params['qualification_type_id'] = qualification_type_id
            _request = shapes.DeleteQualificationTypeRequest(**_params)
        response = self._boto_client.delete_qualification_type(
            **_request.to_boto()
        )

        return shapes.DeleteQualificationTypeResponse.from_boto(response)

    def delete_worker_block(
        self,
        _request: shapes.DeleteWorkerBlockRequest = None,
        *,
        worker_id: str,
        reason: str = ShapeBase.NOT_SET,
    ) -> shapes.DeleteWorkerBlockResponse:
        """
        The `DeleteWorkerBlock` operation allows you to reinstate a blocked Worker to
        work on your HITs. This operation reverses the effects of the CreateWorkerBlock
        operation. You need the Worker ID to use this operation. If the Worker ID is
        missing or invalid, this operation fails and returns the message “WorkerId is
        invalid.” If the specified Worker is not blocked, this operation returns
        successfully.
        """
        if _request is None:
            _params = {}
            if worker_id is not ShapeBase.NOT_SET:
                _params['worker_id'] = worker_id
            if reason is not ShapeBase.NOT_SET:
                _params['reason'] = reason
            _request = shapes.DeleteWorkerBlockRequest(**_params)
        response = self._boto_client.delete_worker_block(**_request.to_boto())

        return shapes.DeleteWorkerBlockResponse.from_boto(response)

    def disassociate_qualification_from_worker(
        self,
        _request: shapes.DisassociateQualificationFromWorkerRequest = None,
        *,
        worker_id: str,
        qualification_type_id: str,
        reason: str = ShapeBase.NOT_SET,
    ) -> shapes.DisassociateQualificationFromWorkerResponse:
        """
        The `DisassociateQualificationFromWorker` revokes a previously granted
        Qualification from a user.

        You can provide a text message explaining why the Qualification was revoked. The
        user who had the Qualification can see this message.
        """
        if _request is None:
            _params = {}
            if worker_id is not ShapeBase.NOT_SET:
                _params['worker_id'] = worker_id
            if qualification_type_id is not ShapeBase.NOT_SET:
                _params['qualification_type_id'] = qualification_type_id
            if reason is not ShapeBase.NOT_SET:
                _params['reason'] = reason
            _request = shapes.DisassociateQualificationFromWorkerRequest(
                **_params
            )
        response = self._boto_client.disassociate_qualification_from_worker(
            **_request.to_boto()
        )

        return shapes.DisassociateQualificationFromWorkerResponse.from_boto(
            response
        )

    def get_account_balance(
        self,
        _request: shapes.GetAccountBalanceRequest = None,
    ) -> shapes.GetAccountBalanceResponse:
        """
        The `GetAccountBalance` operation retrieves the amount of money in your Amazon
        Mechanical Turk account.
        """
        if _request is None:
            _params = {}
            _request = shapes.GetAccountBalanceRequest(**_params)
        response = self._boto_client.get_account_balance(**_request.to_boto())

        return shapes.GetAccountBalanceResponse.from_boto(response)

    def get_assignment(
        self,
        _request: shapes.GetAssignmentRequest = None,
        *,
        assignment_id: str,
    ) -> shapes.GetAssignmentResponse:
        """
        The `GetAssignment` operation retrieves the details of the specified Assignment.
        """
        if _request is None:
            _params = {}
            if assignment_id is not ShapeBase.NOT_SET:
                _params['assignment_id'] = assignment_id
            _request = shapes.GetAssignmentRequest(**_params)
        response = self._boto_client.get_assignment(**_request.to_boto())

        return shapes.GetAssignmentResponse.from_boto(response)

    def get_file_upload_url(
        self,
        _request: shapes.GetFileUploadURLRequest = None,
        *,
        assignment_id: str,
        question_identifier: str,
    ) -> shapes.GetFileUploadURLResponse:
        """
        The `GetFileUploadURL` operation generates and returns a temporary URL. You use
        the temporary URL to retrieve a file uploaded by a Worker as an answer to a
        FileUploadAnswer question for a HIT. The temporary URL is generated the instant
        the GetFileUploadURL operation is called, and is valid for 60 seconds. You can
        get a temporary file upload URL any time until the HIT is disposed. After the
        HIT is disposed, any uploaded files are deleted, and cannot be retrieved.
        Pending Deprecation on December 12, 2017. The Answer Specification structure
        will no longer support the `FileUploadAnswer` element to be used for the
        QuestionForm data structure. Instead, we recommend that Requesters who want to
        create HITs asking Workers to upload files to use Amazon S3.
        """
        if _request is None:
            _params = {}
            if assignment_id is not ShapeBase.NOT_SET:
                _params['assignment_id'] = assignment_id
            if question_identifier is not ShapeBase.NOT_SET:
                _params['question_identifier'] = question_identifier
            _request = shapes.GetFileUploadURLRequest(**_params)
        response = self._boto_client.get_file_upload_url(**_request.to_boto())

        return shapes.GetFileUploadURLResponse.from_boto(response)

    def get_hit(
        self,
        _request: shapes.GetHITRequest = None,
        *,
        hit_id: str,
    ) -> shapes.GetHITResponse:
        """
        The `GetHIT` operation retrieves the details of the specified HIT.
        """
        if _request is None:
            _params = {}
            if hit_id is not ShapeBase.NOT_SET:
                _params['hit_id'] = hit_id
            _request = shapes.GetHITRequest(**_params)
        response = self._boto_client.get_hit(**_request.to_boto())

        return shapes.GetHITResponse.from_boto(response)

    def get_qualification_score(
        self,
        _request: shapes.GetQualificationScoreRequest = None,
        *,
        qualification_type_id: str,
        worker_id: str,
    ) -> shapes.GetQualificationScoreResponse:
        """
        The `GetQualificationScore` operation returns the value of a Worker's
        Qualification for a given Qualification type.

        To get a Worker's Qualification, you must know the Worker's ID. The Worker's ID
        is included in the assignment data returned by the `ListAssignmentsForHIT`
        operation.

        Only the owner of a Qualification type can query the value of a Worker's
        Qualification of that type.
        """
        if _request is None:
            _params = {}
            if qualification_type_id is not ShapeBase.NOT_SET:
                _params['qualification_type_id'] = qualification_type_id
            if worker_id is not ShapeBase.NOT_SET:
                _params['worker_id'] = worker_id
            _request = shapes.GetQualificationScoreRequest(**_params)
        response = self._boto_client.get_qualification_score(
            **_request.to_boto()
        )

        return shapes.GetQualificationScoreResponse.from_boto(response)

    def get_qualification_type(
        self,
        _request: shapes.GetQualificationTypeRequest = None,
        *,
        qualification_type_id: str,
    ) -> shapes.GetQualificationTypeResponse:
        """
        The `GetQualificationType`operation retrieves information about a Qualification
        type using its ID.
        """
        if _request is None:
            _params = {}
            if qualification_type_id is not ShapeBase.NOT_SET:
                _params['qualification_type_id'] = qualification_type_id
            _request = shapes.GetQualificationTypeRequest(**_params)
        response = self._boto_client.get_qualification_type(
            **_request.to_boto()
        )

        return shapes.GetQualificationTypeResponse.from_boto(response)

    def list_assignments_for_hit(
        self,
        _request: shapes.ListAssignmentsForHITRequest = None,
        *,
        hit_id: str,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        assignment_statuses: typing.List[
            typing.Union[str, shapes.AssignmentStatus]] = ShapeBase.NOT_SET,
    ) -> shapes.ListAssignmentsForHITResponse:
        """
        The `ListAssignmentsForHIT` operation retrieves completed assignments for a HIT.
        You can use this operation to retrieve the results for a HIT.

        You can get assignments for a HIT at any time, even if the HIT is not yet
        Reviewable. If a HIT requested multiple assignments, and has received some
        results but has not yet become Reviewable, you can still retrieve the partial
        results with this operation.

        Use the AssignmentStatus parameter to control which set of assignments for a HIT
        are returned. The ListAssignmentsForHIT operation can return submitted
        assignments awaiting approval, or it can return assignments that have already
        been approved or rejected. You can set AssignmentStatus=Approved,Rejected to get
        assignments that have already been approved and rejected together in one result
        set.

        Only the Requester who created the HIT can retrieve the assignments for that
        HIT.

        Results are sorted and divided into numbered pages and the operation returns a
        single page of results. You can use the parameters of the operation to control
        sorting and pagination.
        """
        if _request is None:
            _params = {}
            if hit_id is not ShapeBase.NOT_SET:
                _params['hit_id'] = hit_id
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if assignment_statuses is not ShapeBase.NOT_SET:
                _params['assignment_statuses'] = assignment_statuses
            _request = shapes.ListAssignmentsForHITRequest(**_params)
        paginator = self.get_paginator("list_assignments_for_hit").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListAssignmentsForHITResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListAssignmentsForHITResponse.from_boto(response)

    def list_bonus_payments(
        self,
        _request: shapes.ListBonusPaymentsRequest = None,
        *,
        hit_id: str = ShapeBase.NOT_SET,
        assignment_id: str = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.ListBonusPaymentsResponse:
        """
        The `ListBonusPayments` operation retrieves the amounts of bonuses you have paid
        to Workers for a given HIT or assignment.
        """
        if _request is None:
            _params = {}
            if hit_id is not ShapeBase.NOT_SET:
                _params['hit_id'] = hit_id
            if assignment_id is not ShapeBase.NOT_SET:
                _params['assignment_id'] = assignment_id
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.ListBonusPaymentsRequest(**_params)
        paginator = self.get_paginator("list_bonus_payments").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListBonusPaymentsResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListBonusPaymentsResponse.from_boto(response)

    def list_hits(
        self,
        _request: shapes.ListHITsRequest = None,
        *,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.ListHITsResponse:
        """
        The `ListHITs` operation returns all of a Requester's HITs. The operation
        returns HITs of any status, except for HITs that have been deleted of with the
        DeleteHIT operation or that have been auto-deleted.
        """
        if _request is None:
            _params = {}
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.ListHITsRequest(**_params)
        paginator = self.get_paginator("list_hits").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListHITsResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListHITsResponse.from_boto(response)

    def list_hits_for_qualification_type(
        self,
        _request: shapes.ListHITsForQualificationTypeRequest = None,
        *,
        qualification_type_id: str,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.ListHITsForQualificationTypeResponse:
        """
        The `ListHITsForQualificationType` operation returns the HITs that use the given
        Qualification type for a Qualification requirement. The operation returns HITs
        of any status, except for HITs that have been deleted with the `DeleteHIT`
        operation or that have been auto-deleted.
        """
        if _request is None:
            _params = {}
            if qualification_type_id is not ShapeBase.NOT_SET:
                _params['qualification_type_id'] = qualification_type_id
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.ListHITsForQualificationTypeRequest(**_params)
        paginator = self.get_paginator("list_hits_for_qualification_type"
                                      ).paginate(**_request.to_boto())
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListHITsForQualificationTypeResponse.from_boto(
            first_page
        )
        result._page_iterator = page_generator
        return result

        return shapes.ListHITsForQualificationTypeResponse.from_boto(response)

    def list_qualification_requests(
        self,
        _request: shapes.ListQualificationRequestsRequest = None,
        *,
        qualification_type_id: str = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.ListQualificationRequestsResponse:
        """
        The `ListQualificationRequests` operation retrieves requests for Qualifications
        of a particular Qualification type. The owner of the Qualification type calls
        this operation to poll for pending requests, and accepts them using the
        AcceptQualification operation.
        """
        if _request is None:
            _params = {}
            if qualification_type_id is not ShapeBase.NOT_SET:
                _params['qualification_type_id'] = qualification_type_id
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.ListQualificationRequestsRequest(**_params)
        paginator = self.get_paginator("list_qualification_requests").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListQualificationRequestsResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListQualificationRequestsResponse.from_boto(response)

    def list_qualification_types(
        self,
        _request: shapes.ListQualificationTypesRequest = None,
        *,
        must_be_requestable: bool,
        query: str = ShapeBase.NOT_SET,
        must_be_owned_by_caller: bool = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.ListQualificationTypesResponse:
        """
        The `ListQualificationTypes` operation returns a list of Qualification types,
        filtered by an optional search term.
        """
        if _request is None:
            _params = {}
            if must_be_requestable is not ShapeBase.NOT_SET:
                _params['must_be_requestable'] = must_be_requestable
            if query is not ShapeBase.NOT_SET:
                _params['query'] = query
            if must_be_owned_by_caller is not ShapeBase.NOT_SET:
                _params['must_be_owned_by_caller'] = must_be_owned_by_caller
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.ListQualificationTypesRequest(**_params)
        paginator = self.get_paginator("list_qualification_types").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListQualificationTypesResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListQualificationTypesResponse.from_boto(response)

    def list_review_policy_results_for_hit(
        self,
        _request: shapes.ListReviewPolicyResultsForHITRequest = None,
        *,
        hit_id: str,
        policy_levels: typing.List[typing.Union[str, shapes.ReviewPolicyLevel]
                                  ] = ShapeBase.NOT_SET,
        retrieve_actions: bool = ShapeBase.NOT_SET,
        retrieve_results: bool = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.ListReviewPolicyResultsForHITResponse:
        """
        The `ListReviewPolicyResultsForHIT` operation retrieves the computed results and
        the actions taken in the course of executing your Review Policies for a given
        HIT. For information about how to specify Review Policies when you call
        CreateHIT, see Review Policies. The ListReviewPolicyResultsForHIT operation can
        return results for both Assignment-level and HIT-level review results.
        """
        if _request is None:
            _params = {}
            if hit_id is not ShapeBase.NOT_SET:
                _params['hit_id'] = hit_id
            if policy_levels is not ShapeBase.NOT_SET:
                _params['policy_levels'] = policy_levels
            if retrieve_actions is not ShapeBase.NOT_SET:
                _params['retrieve_actions'] = retrieve_actions
            if retrieve_results is not ShapeBase.NOT_SET:
                _params['retrieve_results'] = retrieve_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.ListReviewPolicyResultsForHITRequest(**_params)
        response = self._boto_client.list_review_policy_results_for_hit(
            **_request.to_boto()
        )

        return shapes.ListReviewPolicyResultsForHITResponse.from_boto(response)

    def list_reviewable_hits(
        self,
        _request: shapes.ListReviewableHITsRequest = None,
        *,
        hit_type_id: str = ShapeBase.NOT_SET,
        status: typing.Union[str, shapes.ReviewableHITStatus] = ShapeBase.
        NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.ListReviewableHITsResponse:
        """
        The `ListReviewableHITs` operation retrieves the HITs with Status equal to
        Reviewable or Status equal to Reviewing that belong to the Requester calling the
        operation.
        """
        if _request is None:
            _params = {}
            if hit_type_id is not ShapeBase.NOT_SET:
                _params['hit_type_id'] = hit_type_id
            if status is not ShapeBase.NOT_SET:
                _params['status'] = status
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.ListReviewableHITsRequest(**_params)
        paginator = self.get_paginator("list_reviewable_hits").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListReviewableHITsResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListReviewableHITsResponse.from_boto(response)

    def list_worker_blocks(
        self,
        _request: shapes.ListWorkerBlocksRequest = None,
        *,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.ListWorkerBlocksResponse:
        """
        The `ListWorkersBlocks` operation retrieves a list of Workers who are blocked
        from working on your HITs.
        """
        if _request is None:
            _params = {}
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.ListWorkerBlocksRequest(**_params)
        paginator = self.get_paginator("list_worker_blocks").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListWorkerBlocksResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListWorkerBlocksResponse.from_boto(response)

    def list_workers_with_qualification_type(
        self,
        _request: shapes.ListWorkersWithQualificationTypeRequest = None,
        *,
        qualification_type_id: str,
        status: typing.Union[str, shapes.QualificationStatus] = ShapeBase.
        NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.ListWorkersWithQualificationTypeResponse:
        """
        The `ListWorkersWithQualificationType` operation returns all of the Workers that
        have been associated with a given Qualification type.
        """
        if _request is None:
            _params = {}
            if qualification_type_id is not ShapeBase.NOT_SET:
                _params['qualification_type_id'] = qualification_type_id
            if status is not ShapeBase.NOT_SET:
                _params['status'] = status
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.ListWorkersWithQualificationTypeRequest(**_params)
        paginator = self.get_paginator("list_workers_with_qualification_type"
                                      ).paginate(**_request.to_boto())
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListWorkersWithQualificationTypeResponse.from_boto(
            first_page
        )
        result._page_iterator = page_generator
        return result

        return shapes.ListWorkersWithQualificationTypeResponse.from_boto(
            response
        )

    def notify_workers(
        self,
        _request: shapes.NotifyWorkersRequest = None,
        *,
        subject: str,
        message_text: str,
        worker_ids: typing.List[str],
    ) -> shapes.NotifyWorkersResponse:
        """
        The `NotifyWorkers` operation sends an email to one or more Workers that you
        specify with the Worker ID. You can specify up to 100 Worker IDs to send the
        same message with a single call to the NotifyWorkers operation. The
        NotifyWorkers operation will send a notification email to a Worker only if you
        have previously approved or rejected work from the Worker.
        """
        if _request is None:
            _params = {}
            if subject is not ShapeBase.NOT_SET:
                _params['subject'] = subject
            if message_text is not ShapeBase.NOT_SET:
                _params['message_text'] = message_text
            if worker_ids is not ShapeBase.NOT_SET:
                _params['worker_ids'] = worker_ids
            _request = shapes.NotifyWorkersRequest(**_params)
        response = self._boto_client.notify_workers(**_request.to_boto())

        return shapes.NotifyWorkersResponse.from_boto(response)

    def reject_assignment(
        self,
        _request: shapes.RejectAssignmentRequest = None,
        *,
        assignment_id: str,
        requester_feedback: str,
    ) -> shapes.RejectAssignmentResponse:
        """
        The `RejectAssignment` operation rejects the results of a completed assignment.

        You can include an optional feedback message with the rejection, which the
        Worker can see in the Status section of the web site. When you include a
        feedback message with the rejection, it helps the Worker understand why the
        assignment was rejected, and can improve the quality of the results the Worker
        submits in the future.

        Only the Requester who created the HIT can reject an assignment for the HIT.
        """
        if _request is None:
            _params = {}
            if assignment_id is not ShapeBase.NOT_SET:
                _params['assignment_id'] = assignment_id
            if requester_feedback is not ShapeBase.NOT_SET:
                _params['requester_feedback'] = requester_feedback
            _request = shapes.RejectAssignmentRequest(**_params)
        response = self._boto_client.reject_assignment(**_request.to_boto())

        return shapes.RejectAssignmentResponse.from_boto(response)

    def reject_qualification_request(
        self,
        _request: shapes.RejectQualificationRequestRequest = None,
        *,
        qualification_request_id: str,
        reason: str = ShapeBase.NOT_SET,
    ) -> shapes.RejectQualificationRequestResponse:
        """
        The `RejectQualificationRequest` operation rejects a user's request for a
        Qualification.

        You can provide a text message explaining why the request was rejected. The
        Worker who made the request can see this message.
        """
        if _request is None:
            _params = {}
            if qualification_request_id is not ShapeBase.NOT_SET:
                _params['qualification_request_id'] = qualification_request_id
            if reason is not ShapeBase.NOT_SET:
                _params['reason'] = reason
            _request = shapes.RejectQualificationRequestRequest(**_params)
        response = self._boto_client.reject_qualification_request(
            **_request.to_boto()
        )

        return shapes.RejectQualificationRequestResponse.from_boto(response)

    def send_bonus(
        self,
        _request: shapes.SendBonusRequest = None,
        *,
        worker_id: str,
        bonus_amount: str,
        assignment_id: str,
        reason: str,
        unique_request_token: str = ShapeBase.NOT_SET,
    ) -> shapes.SendBonusResponse:
        """
        The `SendBonus` operation issues a payment of money from your account to a
        Worker. This payment happens separately from the reward you pay to the Worker
        when you approve the Worker's assignment. The SendBonus operation requires the
        Worker's ID and the assignment ID as parameters to initiate payment of the
        bonus. You must include a message that explains the reason for the bonus
        payment, as the Worker may not be expecting the payment. Amazon Mechanical Turk
        collects a fee for bonus payments, similar to the HIT listing fee. This
        operation fails if your account does not have enough funds to pay for both the
        bonus and the fees.
        """
        if _request is None:
            _params = {}
            if worker_id is not ShapeBase.NOT_SET:
                _params['worker_id'] = worker_id
            if bonus_amount is not ShapeBase.NOT_SET:
                _params['bonus_amount'] = bonus_amount
            if assignment_id is not ShapeBase.NOT_SET:
                _params['assignment_id'] = assignment_id
            if reason is not ShapeBase.NOT_SET:
                _params['reason'] = reason
            if unique_request_token is not ShapeBase.NOT_SET:
                _params['unique_request_token'] = unique_request_token
            _request = shapes.SendBonusRequest(**_params)
        response = self._boto_client.send_bonus(**_request.to_boto())

        return shapes.SendBonusResponse.from_boto(response)

    def send_test_event_notification(
        self,
        _request: shapes.SendTestEventNotificationRequest = None,
        *,
        notification: shapes.NotificationSpecification,
        test_event_type: typing.Union[str, shapes.EventType],
    ) -> shapes.SendTestEventNotificationResponse:
        """
        The `SendTestEventNotification` operation causes Amazon Mechanical Turk to send
        a notification message as if a HIT event occurred, according to the provided
        notification specification. This allows you to test notifications without
        setting up notifications for a real HIT type and trying to trigger them using
        the website. When you call this operation, the service attempts to send the test
        notification immediately.
        """
        if _request is None:
            _params = {}
            if notification is not ShapeBase.NOT_SET:
                _params['notification'] = notification
            if test_event_type is not ShapeBase.NOT_SET:
                _params['test_event_type'] = test_event_type
            _request = shapes.SendTestEventNotificationRequest(**_params)
        response = self._boto_client.send_test_event_notification(
            **_request.to_boto()
        )

        return shapes.SendTestEventNotificationResponse.from_boto(response)

    def update_expiration_for_hit(
        self,
        _request: shapes.UpdateExpirationForHITRequest = None,
        *,
        hit_id: str,
        expire_at: datetime.datetime,
    ) -> shapes.UpdateExpirationForHITResponse:
        """
        The `UpdateExpirationForHIT` operation allows you update the expiration time of
        a HIT. If you update it to a time in the past, the HIT will be immediately
        expired.
        """
        if _request is None:
            _params = {}
            if hit_id is not ShapeBase.NOT_SET:
                _params['hit_id'] = hit_id
            if expire_at is not ShapeBase.NOT_SET:
                _params['expire_at'] = expire_at
            _request = shapes.UpdateExpirationForHITRequest(**_params)
        response = self._boto_client.update_expiration_for_hit(
            **_request.to_boto()
        )

        return shapes.UpdateExpirationForHITResponse.from_boto(response)

    def update_hit_review_status(
        self,
        _request: shapes.UpdateHITReviewStatusRequest = None,
        *,
        hit_id: str,
        revert: bool = ShapeBase.NOT_SET,
    ) -> shapes.UpdateHITReviewStatusResponse:
        """
        The `UpdateHITReviewStatus` operation updates the status of a HIT. If the status
        is Reviewable, this operation can update the status to Reviewing, or it can
        revert a Reviewing HIT back to the Reviewable status.
        """
        if _request is None:
            _params = {}
            if hit_id is not ShapeBase.NOT_SET:
                _params['hit_id'] = hit_id
            if revert is not ShapeBase.NOT_SET:
                _params['revert'] = revert
            _request = shapes.UpdateHITReviewStatusRequest(**_params)
        response = self._boto_client.update_hit_review_status(
            **_request.to_boto()
        )

        return shapes.UpdateHITReviewStatusResponse.from_boto(response)

    def update_hit_type_of_hit(
        self,
        _request: shapes.UpdateHITTypeOfHITRequest = None,
        *,
        hit_id: str,
        hit_type_id: str,
    ) -> shapes.UpdateHITTypeOfHITResponse:
        """
        The `UpdateHITTypeOfHIT` operation allows you to change the HITType properties
        of a HIT. This operation disassociates the HIT from its old HITType properties
        and associates it with the new HITType properties. The HIT takes on the
        properties of the new HITType in place of the old ones.
        """
        if _request is None:
            _params = {}
            if hit_id is not ShapeBase.NOT_SET:
                _params['hit_id'] = hit_id
            if hit_type_id is not ShapeBase.NOT_SET:
                _params['hit_type_id'] = hit_type_id
            _request = shapes.UpdateHITTypeOfHITRequest(**_params)
        response = self._boto_client.update_hit_type_of_hit(
            **_request.to_boto()
        )

        return shapes.UpdateHITTypeOfHITResponse.from_boto(response)

    def update_notification_settings(
        self,
        _request: shapes.UpdateNotificationSettingsRequest = None,
        *,
        hit_type_id: str,
        notification: shapes.NotificationSpecification = ShapeBase.NOT_SET,
        active: bool = ShapeBase.NOT_SET,
    ) -> shapes.UpdateNotificationSettingsResponse:
        """
        The `UpdateNotificationSettings` operation creates, updates, disables or re-
        enables notifications for a HIT type. If you call the UpdateNotificationSettings
        operation for a HIT type that already has a notification specification, the
        operation replaces the old specification with a new one. You can call the
        UpdateNotificationSettings operation to enable or disable notifications for the
        HIT type, without having to modify the notification specification itself by
        providing updates to the Active status without specifying a new notification
        specification. To change the Active status of a HIT type's notifications, the
        HIT type must already have a notification specification, or one must be provided
        in the same call to `UpdateNotificationSettings`.
        """
        if _request is None:
            _params = {}
            if hit_type_id is not ShapeBase.NOT_SET:
                _params['hit_type_id'] = hit_type_id
            if notification is not ShapeBase.NOT_SET:
                _params['notification'] = notification
            if active is not ShapeBase.NOT_SET:
                _params['active'] = active
            _request = shapes.UpdateNotificationSettingsRequest(**_params)
        response = self._boto_client.update_notification_settings(
            **_request.to_boto()
        )

        return shapes.UpdateNotificationSettingsResponse.from_boto(response)

    def update_qualification_type(
        self,
        _request: shapes.UpdateQualificationTypeRequest = None,
        *,
        qualification_type_id: str,
        description: str = ShapeBase.NOT_SET,
        qualification_type_status: typing.
        Union[str, shapes.QualificationTypeStatus] = ShapeBase.NOT_SET,
        test: str = ShapeBase.NOT_SET,
        answer_key: str = ShapeBase.NOT_SET,
        test_duration_in_seconds: int = ShapeBase.NOT_SET,
        retry_delay_in_seconds: int = ShapeBase.NOT_SET,
        auto_granted: bool = ShapeBase.NOT_SET,
        auto_granted_value: int = ShapeBase.NOT_SET,
    ) -> shapes.UpdateQualificationTypeResponse:
        """
        The `UpdateQualificationType` operation modifies the attributes of an existing
        Qualification type, which is represented by a QualificationType data structure.
        Only the owner of a Qualification type can modify its attributes.

        Most attributes of a Qualification type can be changed after the type has been
        created. However, the Name and Keywords fields cannot be modified. The
        RetryDelayInSeconds parameter can be modified or added to change the delay or to
        enable retries, but RetryDelayInSeconds cannot be used to disable retries.

        You can use this operation to update the test for a Qualification type. The test
        is updated based on the values specified for the Test, TestDurationInSeconds and
        AnswerKey parameters. All three parameters specify the updated test. If you are
        updating the test for a type, you must specify the Test and
        TestDurationInSeconds parameters. The AnswerKey parameter is optional; omitting
        it specifies that the updated test does not have an answer key.

        If you omit the Test parameter, the test for the Qualification type is
        unchanged. There is no way to remove a test from a Qualification type that has
        one. If the type already has a test, you cannot update it to be AutoGranted. If
        the Qualification type does not have a test and one is provided by an update,
        the type will henceforth have a test.

        If you want to update the test duration or answer key for an existing test
        without changing the questions, you must specify a Test parameter with the
        original questions, along with the updated values.

        If you provide an updated Test but no AnswerKey, the new test will not have an
        answer key. Requests for such Qualifications must be granted manually.

        You can also update the AutoGranted and AutoGrantedValue attributes of the
        Qualification type.
        """
        if _request is None:
            _params = {}
            if qualification_type_id is not ShapeBase.NOT_SET:
                _params['qualification_type_id'] = qualification_type_id
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if qualification_type_status is not ShapeBase.NOT_SET:
                _params['qualification_type_status'] = qualification_type_status
            if test is not ShapeBase.NOT_SET:
                _params['test'] = test
            if answer_key is not ShapeBase.NOT_SET:
                _params['answer_key'] = answer_key
            if test_duration_in_seconds is not ShapeBase.NOT_SET:
                _params['test_duration_in_seconds'] = test_duration_in_seconds
            if retry_delay_in_seconds is not ShapeBase.NOT_SET:
                _params['retry_delay_in_seconds'] = retry_delay_in_seconds
            if auto_granted is not ShapeBase.NOT_SET:
                _params['auto_granted'] = auto_granted
            if auto_granted_value is not ShapeBase.NOT_SET:
                _params['auto_granted_value'] = auto_granted_value
            _request = shapes.UpdateQualificationTypeRequest(**_params)
        response = self._boto_client.update_qualification_type(
            **_request.to_boto()
        )

        return shapes.UpdateQualificationTypeResponse.from_boto(response)
