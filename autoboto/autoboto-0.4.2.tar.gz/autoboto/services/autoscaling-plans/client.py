import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("autoscaling-plans", *args, **kwargs)

    def create_scaling_plan(
        self,
        _request: shapes.CreateScalingPlanRequest = None,
        *,
        scaling_plan_name: str,
        application_source: shapes.ApplicationSource,
        scaling_instructions: typing.List[shapes.ScalingInstruction],
    ) -> shapes.CreateScalingPlanResponse:
        """
        Creates a scaling plan.

        A scaling plan contains a set of instructions used to configure dynamic scaling
        for the scalable resources in your application. AWS Auto Scaling creates target
        tracking scaling policies based on the scaling instructions in your scaling
        plan.
        """
        if _request is None:
            _params = {}
            if scaling_plan_name is not ShapeBase.NOT_SET:
                _params['scaling_plan_name'] = scaling_plan_name
            if application_source is not ShapeBase.NOT_SET:
                _params['application_source'] = application_source
            if scaling_instructions is not ShapeBase.NOT_SET:
                _params['scaling_instructions'] = scaling_instructions
            _request = shapes.CreateScalingPlanRequest(**_params)
        response = self._boto_client.create_scaling_plan(**_request.to_boto())

        return shapes.CreateScalingPlanResponse.from_boto(response)

    def delete_scaling_plan(
        self,
        _request: shapes.DeleteScalingPlanRequest = None,
        *,
        scaling_plan_name: str,
        scaling_plan_version: int,
    ) -> shapes.DeleteScalingPlanResponse:
        """
        Deletes the specified scaling plan.
        """
        if _request is None:
            _params = {}
            if scaling_plan_name is not ShapeBase.NOT_SET:
                _params['scaling_plan_name'] = scaling_plan_name
            if scaling_plan_version is not ShapeBase.NOT_SET:
                _params['scaling_plan_version'] = scaling_plan_version
            _request = shapes.DeleteScalingPlanRequest(**_params)
        response = self._boto_client.delete_scaling_plan(**_request.to_boto())

        return shapes.DeleteScalingPlanResponse.from_boto(response)

    def describe_scaling_plan_resources(
        self,
        _request: shapes.DescribeScalingPlanResourcesRequest = None,
        *,
        scaling_plan_name: str,
        scaling_plan_version: int,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeScalingPlanResourcesResponse:
        """
        Describes the scalable resources in the specified scaling plan.
        """
        if _request is None:
            _params = {}
            if scaling_plan_name is not ShapeBase.NOT_SET:
                _params['scaling_plan_name'] = scaling_plan_name
            if scaling_plan_version is not ShapeBase.NOT_SET:
                _params['scaling_plan_version'] = scaling_plan_version
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.DescribeScalingPlanResourcesRequest(**_params)
        response = self._boto_client.describe_scaling_plan_resources(
            **_request.to_boto()
        )

        return shapes.DescribeScalingPlanResourcesResponse.from_boto(response)

    def describe_scaling_plans(
        self,
        _request: shapes.DescribeScalingPlansRequest = None,
        *,
        scaling_plan_names: typing.List[str] = ShapeBase.NOT_SET,
        scaling_plan_version: int = ShapeBase.NOT_SET,
        application_sources: typing.List[shapes.ApplicationSource
                                        ] = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeScalingPlansResponse:
        """
        Describes the specified scaling plans or all of your scaling plans.
        """
        if _request is None:
            _params = {}
            if scaling_plan_names is not ShapeBase.NOT_SET:
                _params['scaling_plan_names'] = scaling_plan_names
            if scaling_plan_version is not ShapeBase.NOT_SET:
                _params['scaling_plan_version'] = scaling_plan_version
            if application_sources is not ShapeBase.NOT_SET:
                _params['application_sources'] = application_sources
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.DescribeScalingPlansRequest(**_params)
        response = self._boto_client.describe_scaling_plans(
            **_request.to_boto()
        )

        return shapes.DescribeScalingPlansResponse.from_boto(response)

    def update_scaling_plan(
        self,
        _request: shapes.UpdateScalingPlanRequest = None,
        *,
        scaling_plan_name: str,
        scaling_plan_version: int,
        application_source: shapes.ApplicationSource = ShapeBase.NOT_SET,
        scaling_instructions: typing.List[shapes.ScalingInstruction
                                         ] = ShapeBase.NOT_SET,
    ) -> shapes.UpdateScalingPlanResponse:
        """
        Updates the scaling plan for the specified scaling plan.

        You cannot update a scaling plan if it is in the process of being created,
        updated, or deleted.
        """
        if _request is None:
            _params = {}
            if scaling_plan_name is not ShapeBase.NOT_SET:
                _params['scaling_plan_name'] = scaling_plan_name
            if scaling_plan_version is not ShapeBase.NOT_SET:
                _params['scaling_plan_version'] = scaling_plan_version
            if application_source is not ShapeBase.NOT_SET:
                _params['application_source'] = application_source
            if scaling_instructions is not ShapeBase.NOT_SET:
                _params['scaling_instructions'] = scaling_instructions
            _request = shapes.UpdateScalingPlanRequest(**_params)
        response = self._boto_client.update_scaling_plan(**_request.to_boto())

        return shapes.UpdateScalingPlanResponse.from_boto(response)
