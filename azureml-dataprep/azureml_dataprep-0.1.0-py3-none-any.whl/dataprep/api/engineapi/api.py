# Copyright (c) Microsoft Corporation. All rights reserved.
# pylint: skip-file
# This file is auto-generated. Do not modify.
from typing import List, Dict, Any
from asyncio import AbstractEventLoop
from .messagehandler import AsyncMessageHandler
from . import typedefinitions
from ..errorhandlers import raise_engine_error


class NotificationHandler:
    def __init__(self):
        self.process_function = None
        self.method = None
        self.id = None
        self.Completed = False

    def process_message(self, message):
        if not self.Completed and 'error' in message:
            self.Completed = True
            raise_engine_error(message['error'])
        elif not self.Completed and 'method' in message and message['method'] == self.method:
            self.Completed = self.process_function(message['params'])
        elif not self.Completed and 'id' in message and message['id'] == self.id:
            self.Completed = self.process_function(message['result'])


class EngineAPI:
    def __init__(self, message_handler: AsyncMessageHandler, event_loop: AbstractEventLoop):
        self._message_handler = message_handler
        self._event_loop = event_loop

    async def process_notifications(self, handlers: List[NotificationHandler]):
        def is_completed(handlers: List[NotificationHandler]):
            for handler in handlers:
                if not handler.Completed:
                    return False
            return True

        while not is_completed(handlers):
            message = await self._message_handler.read_line()
            for handler in handlers:
                handler.process_message(message)

    def add_block_to_list(self,
                          message_args: typedefinitions.AddBlockToListMessageArguments,
                          handlers: List[NotificationHandler] = None) -> typedefinitions.AnonymousBlockData:
        message_sent = self._message_handler.send_message('Engine.AddBlockToList', message_args)
        message_id = self._event_loop.run_until_complete(message_sent)
        response = None

        def save_response(data):
            nonlocal response
            response = data
            return True
        handler = NotificationHandler()
        handler.process_function = save_response
        handler.id = message_id
        handlers = handlers + [handler] if handlers is not None else [handler]
        self._event_loop.run_until_complete(self.process_notifications(handlers))
        return typedefinitions.AnonymousBlockData.from_pod(response) if response is not None else None

    def add_temporary_secrets(self,
                              message_args: Dict[str, str],
                              handlers: List[NotificationHandler] = None) -> None:
        message_sent = self._message_handler.send_message('Engine.AddTemporarySecrets', message_args)
        message_id = self._event_loop.run_until_complete(message_sent)
        response = None

        def save_response(data):
            nonlocal response
            response = data
            return True
        handler = NotificationHandler()
        handler.process_function = save_response
        handler.id = message_id
        handlers = handlers + [handler] if handlers is not None else [handler]
        self._event_loop.run_until_complete(self.process_notifications(handlers))
        return response

    def anonymous_data_source_prose_suggestions(self,
                                                message_args: typedefinitions.AnonymousDataSourceProseSuggestionsMessageArguments,
                                                handlers: List[NotificationHandler] = None) -> typedefinitions.DataSourceProperties:
        message_sent = self._message_handler.send_message('GetProseAnonymousDataSourcePropertiesSuggestion', message_args)
        message_id = self._event_loop.run_until_complete(message_sent)
        response = None

        def save_response(data):
            nonlocal response
            response = data
            return True
        handler = NotificationHandler()
        handler.process_function = save_response
        handler.id = message_id
        handlers = handlers + [handler] if handlers is not None else [handler]
        self._event_loop.run_until_complete(self.process_notifications(handlers))
        return typedefinitions.DataSourceProperties.from_pod(response) if response is not None else None

    def anonymous_send_message_to_block(self,
                                        message_args: typedefinitions.AnonymousSendMessageToBlockMessageArguments,
                                        handlers: List[NotificationHandler] = None) -> typedefinitions.AnonymousSendMessageToBlockMessageResponseData:
        message_sent = self._message_handler.send_message('Engine.SendMessageToBlock', message_args)
        message_id = self._event_loop.run_until_complete(message_sent)
        response = None

        def save_response(data):
            nonlocal response
            response = data
            return True
        handler = NotificationHandler()
        handler.process_function = save_response
        handler.id = message_id
        handlers = handlers + [handler] if handlers is not None else [handler]
        self._event_loop.run_until_complete(self.process_notifications(handlers))
        return typedefinitions.AnonymousSendMessageToBlockMessageResponseData.from_pod(response) if response is not None else None

    def create_anonymous_reference(self,
                                   message_args: typedefinitions.CreateAnonymousReferenceMessageArguments,
                                   handlers: List[NotificationHandler] = None) -> typedefinitions.ActivityReference:
        message_sent = self._message_handler.send_message('Engine.CreateAnonymousReference', message_args)
        message_id = self._event_loop.run_until_complete(message_sent)
        response = None

        def save_response(data):
            nonlocal response
            response = data
            return True
        handler = NotificationHandler()
        handler.process_function = save_response
        handler.id = message_id
        handlers = handlers + [handler] if handlers is not None else [handler]
        self._event_loop.run_until_complete(self.process_notifications(handlers))
        return typedefinitions.ActivityReference.from_pod(response) if response is not None else None

    def execute_anonymous_blocks(self,
                                 message_args: typedefinitions.ExecuteAnonymousBlocksMessageArguments,
                                 handlers: List[NotificationHandler] = None) -> None:
        message_sent = self._message_handler.send_message('Engine.ExecuteActivity', message_args)
        message_id = self._event_loop.run_until_complete(message_sent)
        response = None

        def save_response(data):
            nonlocal response
            response = data
            return True
        handler = NotificationHandler()
        handler.process_function = save_response
        handler.id = message_id
        handlers = handlers + [handler] if handlers is not None else [handler]
        self._event_loop.run_until_complete(self.process_notifications(handlers))
        return response

    def execute_inspector(self,
                          message_args: typedefinitions.ExecuteInspectorCommonArguments,
                          handlers: List[NotificationHandler] = None) -> typedefinitions.ExecuteInspectorCommonResponse:
        message_sent = self._message_handler.send_message('Engine.ExecuteInspector', message_args)
        message_id = self._event_loop.run_until_complete(message_sent)
        response = None

        def save_response(data):
            nonlocal response
            response = data
            return True
        handler = NotificationHandler()
        handler.process_function = save_response
        handler.id = message_id
        handlers = handlers + [handler] if handlers is not None else [handler]
        self._event_loop.run_until_complete(self.process_notifications(handlers))
        return typedefinitions.ExecuteInspectorCommonResponse.from_pod(response) if response is not None else None

    def export_script(self,
                      message_args: typedefinitions.ExportScriptMessageArguments,
                      handlers: List[NotificationHandler] = None) -> List[typedefinitions.SecretData]:
        message_sent = self._message_handler.send_message('Project.ExportScript', message_args)
        message_id = self._event_loop.run_until_complete(message_sent)
        response = None

        def save_response(data):
            nonlocal response
            response = data
            return True
        handler = NotificationHandler()
        handler.process_function = save_response
        handler.id = message_id
        handlers = handlers + [handler] if handlers is not None else [handler]
        self._event_loop.run_until_complete(self.process_notifications(handlers))
        return [typedefinitions.SecretData.from_pod(i) if i is not None else None for i in response] if response is not None else None

    def get_project(self,
                    message_args: str,
                    handlers: List[NotificationHandler] = None) -> typedefinitions.AnonymousProjectData:
        message_sent = self._message_handler.send_message('Engine.GetProject', message_args)
        message_id = self._event_loop.run_until_complete(message_sent)
        response = None

        def save_response(data):
            nonlocal response
            response = data
            return True
        handler = NotificationHandler()
        handler.process_function = save_response
        handler.id = message_id
        handlers = handlers + [handler] if handlers is not None else [handler]
        self._event_loop.run_until_complete(self.process_notifications(handlers))
        return typedefinitions.AnonymousProjectData.from_pod(response) if response is not None else None

    def get_secrets(self,
                    message_args: typedefinitions.GetSecretsMessageArguments,
                    handlers: List[NotificationHandler] = None) -> List[typedefinitions.SecretData]:
        message_sent = self._message_handler.send_message('Engine.GetSecrets', message_args)
        message_id = self._event_loop.run_until_complete(message_sent)
        response = None

        def save_response(data):
            nonlocal response
            response = data
            return True
        handler = NotificationHandler()
        handler.process_function = save_response
        handler.id = message_id
        handlers = handlers + [handler] if handlers is not None else [handler]
        self._event_loop.run_until_complete(self.process_notifications(handlers))
        return [typedefinitions.SecretData.from_pod(i) if i is not None else None for i in response] if response is not None else None

    def infer_types(self,
                    message_args: List[typedefinitions.AnonymousBlockData],
                    handlers: List[NotificationHandler] = None) -> Dict[str, typedefinitions.FieldInference]:
        message_sent = self._message_handler.send_message('Engine.InferTypes', message_args)
        message_id = self._event_loop.run_until_complete(message_sent)
        response = None

        def save_response(data):
            nonlocal response
            response = data
            return True
        handler = NotificationHandler()
        handler.process_function = save_response
        handler.id = message_id
        handlers = handlers + [handler] if handlers is not None else [handler]
        self._event_loop.run_until_complete(self.process_notifications(handlers))
        return {k: typedefinitions.FieldInference.from_pod(v) if v is not None else None for k, v in response.items()} if response is not None else None

    def load_project_from_json(self,
                               message_args: str,
                               handlers: List[NotificationHandler] = None) -> typedefinitions.AnonymousProjectData:
        message_sent = self._message_handler.send_message('Engine.LoadProjectFromJson', message_args)
        message_id = self._event_loop.run_until_complete(message_sent)
        response = None

        def save_response(data):
            nonlocal response
            response = data
            return True
        handler = NotificationHandler()
        handler.process_function = save_response
        handler.id = message_id
        handlers = handlers + [handler] if handlers is not None else [handler]
        self._event_loop.run_until_complete(self.process_notifications(handlers))
        return typedefinitions.AnonymousProjectData.from_pod(response) if response is not None else None

    def register_secret(self,
                        message_args: typedefinitions.RegisterSecretMessageArguments,
                        handlers: List[NotificationHandler] = None) -> typedefinitions.Secret:
        message_sent = self._message_handler.send_message('SecretManager.RegisterSecrert', message_args)
        message_id = self._event_loop.run_until_complete(message_sent)
        response = None

        def save_response(data):
            nonlocal response
            response = data
            return True
        handler = NotificationHandler()
        handler.process_function = save_response
        handler.id = message_id
        handlers = handlers + [handler] if handlers is not None else [handler]
        self._event_loop.run_until_complete(self.process_notifications(handlers))
        return typedefinitions.Secret.from_pod(response) if response is not None else None

    def resolve_reference(self,
                          message_args: typedefinitions.ResolveReferenceMessageArguments,
                          handlers: List[NotificationHandler] = None) -> typedefinitions.ActivityReference:
        message_sent = self._message_handler.send_message('Engine.ResolveReference', message_args)
        message_id = self._event_loop.run_until_complete(message_sent)
        response = None

        def save_response(data):
            nonlocal response
            response = data
            return True
        handler = NotificationHandler()
        handler.process_function = save_response
        handler.id = message_id
        handlers = handlers + [handler] if handlers is not None else [handler]
        self._event_loop.run_until_complete(self.process_notifications(handlers))
        return typedefinitions.ActivityReference.from_pod(response) if response is not None else None

    def save_project_from_data(self,
                               message_args: typedefinitions.SaveProjectFromDataMessageArguments,
                               handlers: List[NotificationHandler] = None) -> None:
        message_sent = self._message_handler.send_message('Project.SaveAnonymous', message_args)
        message_id = self._event_loop.run_until_complete(message_sent)
        response = None

        def save_response(data):
            nonlocal response
            response = data
            return True
        handler = NotificationHandler()
        handler.process_function = save_response
        handler.id = message_id
        handlers = handlers + [handler] if handlers is not None else [handler]
        self._event_loop.run_until_complete(self.process_notifications(handlers))
        return response

    def save_project_to_json(self,
                             message_args: typedefinitions.AnonymousProjectData,
                             handlers: List[NotificationHandler] = None) -> str:
        message_sent = self._message_handler.send_message('Project.SaveAnonymousToJson', message_args)
        message_id = self._event_loop.run_until_complete(message_sent)
        response = None

        def save_response(data):
            nonlocal response
            response = data
            return True
        handler = NotificationHandler()
        handler.process_function = save_response
        handler.id = message_id
        handlers = handlers + [handler] if handlers is not None else [handler]
        self._event_loop.run_until_complete(self.process_notifications(handlers))
        return response
