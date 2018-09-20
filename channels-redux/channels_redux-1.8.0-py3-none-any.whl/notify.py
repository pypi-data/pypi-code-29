import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.layers import get_channel_layer
from channels.routing import URLRouter
from django.conf import settings
from django.conf.urls import url
from django.urls import NoReverseMatch
from rest_framework.reverse import reverse


class NotifierMixin(object):
    @classmethod
    def get_api_base_name(cls):
        return '{}:{}'.format(settings.API_APP_NAMESPACE, cls._meta.label_lower)


class NotifyRouter(URLRouter):
    def __init__(self, path=r'^ws/notify/$', name='ws-notify'):
        super().__init__([url(path, NotifyConsumer, name=name)])


class NotifyConsumer(AsyncWebsocketConsumer):
    """An AsyncWebsocketConsumer for notifying subscribers of changes to database objects"""
    @property
    def user(self):
        return self.scope["user"]

    async def connect(self):
        if self.user.is_anonymous:
            await self.close()

        await self.accept()

    async def receive(self, text_data=None, bytes_data=None):
        json_data = json.loads(text_data)
        operation = {
            "subscribe.new": self.subscribe_new,
            "subscribe.existing": self.subscribe_existing,
        }.get(json_data["type"], None)

        if operation is None:
            raise NotImplementedError("Operation {} is not supported. Received data {}".format(operation, json_data))
        await operation(json_data)

    async def subscribe_new(self, message: dict):
        await self.subscribe_to_group(message['model'])

    async def subscribe_existing(self, message: dict):
        model = message['model']
        ids = message['ids']
        for pk in ids:
            await self.subscribe_to_group(self.group_name(model, pk))

    async def subscribe_to_group(self, group_name):
        await self.channel_layer.group_add(group_name, self.channel_name)

    async def notify(self, event):
        await self.send(text_data=json.dumps({
            "model": event['model'],
            "pk": event['pk'],
            "type": event['subtype'],
            "url": event['url']
        }))

    @staticmethod
    def group_name(model, pk=None):
        return '{}.{}'.format(model, pk) if pk else model

    @staticmethod
    def group_send_sync(channel_layer, message, pk=None):
        group_name = NotifyConsumer.group_name(message["model"], pk)
        async_to_sync(channel_layer.group_send)(group_name, message)

    @staticmethod
    def object_updated(instance: NotifierMixin):
        channel_layer = get_channel_layer()
        message = NotifyConsumer.message_for_instance("updated", instance)
        NotifyConsumer.group_send_sync(channel_layer, message, instance.pk)

    @staticmethod
    def object_updated_reverse(model, pk_set):
        channel_layer = get_channel_layer()
        api_base_name = model.get_api_base_name()
        for pk in pk_set:
            message = NotifyConsumer.message("updated", model._meta.label_lower, pk, api_base_name)
            NotifyConsumer.group_send_sync(channel_layer, message)

    @staticmethod
    def object_created(instance: NotifierMixin):
        channel_layer = get_channel_layer()
        message = NotifyConsumer.message_for_instance("created", instance)
        NotifyConsumer.group_send_sync(channel_layer, message)

    @staticmethod
    def object_deleted(instance: NotifierMixin):
        channel_layer = get_channel_layer()
        message = NotifyConsumer.message_for_instance("deleted", instance)
        NotifyConsumer.group_send_sync(channel_layer, message, instance.pk)

    @staticmethod
    def message(message_type, model, pk, api_base_name):
        try:
            return {
                "type": "notify",
                "subtype": message_type,
                "model": model,
                "pk": str(pk),
                "url": reverse('{}-detail'.format(api_base_name), args=(pk,))
            }
        except NoReverseMatch:
            print('API url does not exist for {}'.format(api_base_name))

    @staticmethod
    def message_for_instance(message_type, instance: NotifierMixin):
        return NotifyConsumer.message(
            message_type,
            model=instance._meta.label_lower,
            pk=instance.pk,
            api_base_name=instance.get_api_base_name()
        )
