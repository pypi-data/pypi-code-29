import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("budgets", *args, **kwargs)

    def create_budget(
        self,
        _request: shapes.CreateBudgetRequest = None,
        *,
        account_id: str,
        budget: shapes.Budget,
        notifications_with_subscribers: typing.List[
            shapes.NotificationWithSubscribers] = ShapeBase.NOT_SET,
    ) -> shapes.CreateBudgetResponse:
        """
        Creates a budget and, if included, notifications and subscribers.
        """
        if _request is None:
            _params = {}
            if account_id is not ShapeBase.NOT_SET:
                _params['account_id'] = account_id
            if budget is not ShapeBase.NOT_SET:
                _params['budget'] = budget
            if notifications_with_subscribers is not ShapeBase.NOT_SET:
                _params['notifications_with_subscribers'
                       ] = notifications_with_subscribers
            _request = shapes.CreateBudgetRequest(**_params)
        response = self._boto_client.create_budget(**_request.to_boto())

        return shapes.CreateBudgetResponse.from_boto(response)

    def create_notification(
        self,
        _request: shapes.CreateNotificationRequest = None,
        *,
        account_id: str,
        budget_name: str,
        notification: shapes.Notification,
        subscribers: typing.List[shapes.Subscriber],
    ) -> shapes.CreateNotificationResponse:
        """
        Creates a notification. You must create the budget before you create the
        associated notification.
        """
        if _request is None:
            _params = {}
            if account_id is not ShapeBase.NOT_SET:
                _params['account_id'] = account_id
            if budget_name is not ShapeBase.NOT_SET:
                _params['budget_name'] = budget_name
            if notification is not ShapeBase.NOT_SET:
                _params['notification'] = notification
            if subscribers is not ShapeBase.NOT_SET:
                _params['subscribers'] = subscribers
            _request = shapes.CreateNotificationRequest(**_params)
        response = self._boto_client.create_notification(**_request.to_boto())

        return shapes.CreateNotificationResponse.from_boto(response)

    def create_subscriber(
        self,
        _request: shapes.CreateSubscriberRequest = None,
        *,
        account_id: str,
        budget_name: str,
        notification: shapes.Notification,
        subscriber: shapes.Subscriber,
    ) -> shapes.CreateSubscriberResponse:
        """
        Creates a subscriber. You must create the associated budget and notification
        before you create the subscriber.
        """
        if _request is None:
            _params = {}
            if account_id is not ShapeBase.NOT_SET:
                _params['account_id'] = account_id
            if budget_name is not ShapeBase.NOT_SET:
                _params['budget_name'] = budget_name
            if notification is not ShapeBase.NOT_SET:
                _params['notification'] = notification
            if subscriber is not ShapeBase.NOT_SET:
                _params['subscriber'] = subscriber
            _request = shapes.CreateSubscriberRequest(**_params)
        response = self._boto_client.create_subscriber(**_request.to_boto())

        return shapes.CreateSubscriberResponse.from_boto(response)

    def delete_budget(
        self,
        _request: shapes.DeleteBudgetRequest = None,
        *,
        account_id: str,
        budget_name: str,
    ) -> shapes.DeleteBudgetResponse:
        """
        Deletes a budget. You can delete your budget at any time.

        **Deleting a budget also deletes the notifications and subscribers associated
        with that budget.**
        """
        if _request is None:
            _params = {}
            if account_id is not ShapeBase.NOT_SET:
                _params['account_id'] = account_id
            if budget_name is not ShapeBase.NOT_SET:
                _params['budget_name'] = budget_name
            _request = shapes.DeleteBudgetRequest(**_params)
        response = self._boto_client.delete_budget(**_request.to_boto())

        return shapes.DeleteBudgetResponse.from_boto(response)

    def delete_notification(
        self,
        _request: shapes.DeleteNotificationRequest = None,
        *,
        account_id: str,
        budget_name: str,
        notification: shapes.Notification,
    ) -> shapes.DeleteNotificationResponse:
        """
        Deletes a notification.

        **Deleting a notification also deletes the subscribers associated with the
        notification.**
        """
        if _request is None:
            _params = {}
            if account_id is not ShapeBase.NOT_SET:
                _params['account_id'] = account_id
            if budget_name is not ShapeBase.NOT_SET:
                _params['budget_name'] = budget_name
            if notification is not ShapeBase.NOT_SET:
                _params['notification'] = notification
            _request = shapes.DeleteNotificationRequest(**_params)
        response = self._boto_client.delete_notification(**_request.to_boto())

        return shapes.DeleteNotificationResponse.from_boto(response)

    def delete_subscriber(
        self,
        _request: shapes.DeleteSubscriberRequest = None,
        *,
        account_id: str,
        budget_name: str,
        notification: shapes.Notification,
        subscriber: shapes.Subscriber,
    ) -> shapes.DeleteSubscriberResponse:
        """
        Deletes a subscriber.

        **Deleting the last subscriber to a notification also deletes the
        notification.**
        """
        if _request is None:
            _params = {}
            if account_id is not ShapeBase.NOT_SET:
                _params['account_id'] = account_id
            if budget_name is not ShapeBase.NOT_SET:
                _params['budget_name'] = budget_name
            if notification is not ShapeBase.NOT_SET:
                _params['notification'] = notification
            if subscriber is not ShapeBase.NOT_SET:
                _params['subscriber'] = subscriber
            _request = shapes.DeleteSubscriberRequest(**_params)
        response = self._boto_client.delete_subscriber(**_request.to_boto())

        return shapes.DeleteSubscriberResponse.from_boto(response)

    def describe_budget(
        self,
        _request: shapes.DescribeBudgetRequest = None,
        *,
        account_id: str,
        budget_name: str,
    ) -> shapes.DescribeBudgetResponse:
        """
        Describes a budget.
        """
        if _request is None:
            _params = {}
            if account_id is not ShapeBase.NOT_SET:
                _params['account_id'] = account_id
            if budget_name is not ShapeBase.NOT_SET:
                _params['budget_name'] = budget_name
            _request = shapes.DescribeBudgetRequest(**_params)
        response = self._boto_client.describe_budget(**_request.to_boto())

        return shapes.DescribeBudgetResponse.from_boto(response)

    def describe_budgets(
        self,
        _request: shapes.DescribeBudgetsRequest = None,
        *,
        account_id: str,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeBudgetsResponse:
        """
        Lists the budgets associated with an account.
        """
        if _request is None:
            _params = {}
            if account_id is not ShapeBase.NOT_SET:
                _params['account_id'] = account_id
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.DescribeBudgetsRequest(**_params)
        response = self._boto_client.describe_budgets(**_request.to_boto())

        return shapes.DescribeBudgetsResponse.from_boto(response)

    def describe_notifications_for_budget(
        self,
        _request: shapes.DescribeNotificationsForBudgetRequest = None,
        *,
        account_id: str,
        budget_name: str,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeNotificationsForBudgetResponse:
        """
        Lists the notifications associated with a budget.
        """
        if _request is None:
            _params = {}
            if account_id is not ShapeBase.NOT_SET:
                _params['account_id'] = account_id
            if budget_name is not ShapeBase.NOT_SET:
                _params['budget_name'] = budget_name
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.DescribeNotificationsForBudgetRequest(**_params)
        response = self._boto_client.describe_notifications_for_budget(
            **_request.to_boto()
        )

        return shapes.DescribeNotificationsForBudgetResponse.from_boto(response)

    def describe_subscribers_for_notification(
        self,
        _request: shapes.DescribeSubscribersForNotificationRequest = None,
        *,
        account_id: str,
        budget_name: str,
        notification: shapes.Notification,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeSubscribersForNotificationResponse:
        """
        Lists the subscribers associated with a notification.
        """
        if _request is None:
            _params = {}
            if account_id is not ShapeBase.NOT_SET:
                _params['account_id'] = account_id
            if budget_name is not ShapeBase.NOT_SET:
                _params['budget_name'] = budget_name
            if notification is not ShapeBase.NOT_SET:
                _params['notification'] = notification
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.DescribeSubscribersForNotificationRequest(
                **_params
            )
        response = self._boto_client.describe_subscribers_for_notification(
            **_request.to_boto()
        )

        return shapes.DescribeSubscribersForNotificationResponse.from_boto(
            response
        )

    def update_budget(
        self,
        _request: shapes.UpdateBudgetRequest = None,
        *,
        account_id: str,
        new_budget: shapes.Budget,
    ) -> shapes.UpdateBudgetResponse:
        """
        Updates a budget. You can change every part of a budget except for the
        `budgetName` and the `calculatedSpend`. When a budget is modified, the
        `calculatedSpend` drops to zero until AWS has new usage data to use for
        forecasting.
        """
        if _request is None:
            _params = {}
            if account_id is not ShapeBase.NOT_SET:
                _params['account_id'] = account_id
            if new_budget is not ShapeBase.NOT_SET:
                _params['new_budget'] = new_budget
            _request = shapes.UpdateBudgetRequest(**_params)
        response = self._boto_client.update_budget(**_request.to_boto())

        return shapes.UpdateBudgetResponse.from_boto(response)

    def update_notification(
        self,
        _request: shapes.UpdateNotificationRequest = None,
        *,
        account_id: str,
        budget_name: str,
        old_notification: shapes.Notification,
        new_notification: shapes.Notification,
    ) -> shapes.UpdateNotificationResponse:
        """
        Updates a notification.
        """
        if _request is None:
            _params = {}
            if account_id is not ShapeBase.NOT_SET:
                _params['account_id'] = account_id
            if budget_name is not ShapeBase.NOT_SET:
                _params['budget_name'] = budget_name
            if old_notification is not ShapeBase.NOT_SET:
                _params['old_notification'] = old_notification
            if new_notification is not ShapeBase.NOT_SET:
                _params['new_notification'] = new_notification
            _request = shapes.UpdateNotificationRequest(**_params)
        response = self._boto_client.update_notification(**_request.to_boto())

        return shapes.UpdateNotificationResponse.from_boto(response)

    def update_subscriber(
        self,
        _request: shapes.UpdateSubscriberRequest = None,
        *,
        account_id: str,
        budget_name: str,
        notification: shapes.Notification,
        old_subscriber: shapes.Subscriber,
        new_subscriber: shapes.Subscriber,
    ) -> shapes.UpdateSubscriberResponse:
        """
        Updates a subscriber.
        """
        if _request is None:
            _params = {}
            if account_id is not ShapeBase.NOT_SET:
                _params['account_id'] = account_id
            if budget_name is not ShapeBase.NOT_SET:
                _params['budget_name'] = budget_name
            if notification is not ShapeBase.NOT_SET:
                _params['notification'] = notification
            if old_subscriber is not ShapeBase.NOT_SET:
                _params['old_subscriber'] = old_subscriber
            if new_subscriber is not ShapeBase.NOT_SET:
                _params['new_subscriber'] = new_subscriber
            _request = shapes.UpdateSubscriberRequest(**_params)
        response = self._boto_client.update_subscriber(**_request.to_boto())

        return shapes.UpdateSubscriberResponse.from_boto(response)
