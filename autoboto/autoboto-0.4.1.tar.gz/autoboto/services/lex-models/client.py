import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("lex-models", *args, **kwargs)

    def create_bot_version(
        self,
        _request: shapes.CreateBotVersionRequest = None,
        *,
        name: str,
        checksum: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateBotVersionResponse:
        """
        Creates a new version of the bot based on the `$LATEST` version. If the
        `$LATEST` version of this resource hasn't changed since you created the last
        version, Amazon Lex doesn't create a new version. It returns the last created
        version.

        You can update only the `$LATEST` version of the bot. You can't update the
        numbered versions that you create with the `CreateBotVersion` operation.

        When you create the first version of a bot, Amazon Lex sets the version to 1.
        Subsequent versions increment by 1. For more information, see versioning-intro.

        This operation requires permission for the `lex:CreateBotVersion` action.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if checksum is not ShapeBase.NOT_SET:
                _params['checksum'] = checksum
            _request = shapes.CreateBotVersionRequest(**_params)
        response = self._boto_client.create_bot_version(**_request.to_boto())

        return shapes.CreateBotVersionResponse.from_boto(response)

    def create_intent_version(
        self,
        _request: shapes.CreateIntentVersionRequest = None,
        *,
        name: str,
        checksum: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateIntentVersionResponse:
        """
        Creates a new version of an intent based on the `$LATEST` version of the intent.
        If the `$LATEST` version of this intent hasn't changed since you last updated
        it, Amazon Lex doesn't create a new version. It returns the last version you
        created.

        You can update only the `$LATEST` version of the intent. You can't update the
        numbered versions that you create with the `CreateIntentVersion` operation.

        When you create a version of an intent, Amazon Lex sets the version to 1.
        Subsequent versions increment by 1. For more information, see versioning-intro.

        This operation requires permissions to perform the `lex:CreateIntentVersion`
        action.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if checksum is not ShapeBase.NOT_SET:
                _params['checksum'] = checksum
            _request = shapes.CreateIntentVersionRequest(**_params)
        response = self._boto_client.create_intent_version(**_request.to_boto())

        return shapes.CreateIntentVersionResponse.from_boto(response)

    def create_slot_type_version(
        self,
        _request: shapes.CreateSlotTypeVersionRequest = None,
        *,
        name: str,
        checksum: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateSlotTypeVersionResponse:
        """
        Creates a new version of a slot type based on the `$LATEST` version of the
        specified slot type. If the `$LATEST` version of this resource has not changed
        since the last version that you created, Amazon Lex doesn't create a new
        version. It returns the last version that you created.

        You can update only the `$LATEST` version of a slot type. You can't update the
        numbered versions that you create with the `CreateSlotTypeVersion` operation.

        When you create a version of a slot type, Amazon Lex sets the version to 1.
        Subsequent versions increment by 1. For more information, see versioning-intro.

        This operation requires permissions for the `lex:CreateSlotTypeVersion` action.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if checksum is not ShapeBase.NOT_SET:
                _params['checksum'] = checksum
            _request = shapes.CreateSlotTypeVersionRequest(**_params)
        response = self._boto_client.create_slot_type_version(
            **_request.to_boto()
        )

        return shapes.CreateSlotTypeVersionResponse.from_boto(response)

    def delete_bot(
        self,
        _request: shapes.DeleteBotRequest = None,
        *,
        name: str,
    ) -> None:
        """
        Deletes all versions of the bot, including the `$LATEST` version. To delete a
        specific version of the bot, use the DeleteBotVersion operation.

        If a bot has an alias, you can't delete it. Instead, the `DeleteBot` operation
        returns a `ResourceInUseException` exception that includes a reference to the
        alias that refers to the bot. To remove the reference to the bot, delete the
        alias. If you get the same exception again, delete the referring alias until the
        `DeleteBot` operation is successful.

        This operation requires permissions for the `lex:DeleteBot` action.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            _request = shapes.DeleteBotRequest(**_params)
        response = self._boto_client.delete_bot(**_request.to_boto())

    def delete_bot_alias(
        self,
        _request: shapes.DeleteBotAliasRequest = None,
        *,
        name: str,
        bot_name: str,
    ) -> None:
        """
        Deletes an alias for the specified bot.

        You can't delete an alias that is used in the association between a bot and a
        messaging channel. If an alias is used in a channel association, the `DeleteBot`
        operation returns a `ResourceInUseException` exception that includes a reference
        to the channel association that refers to the bot. You can remove the reference
        to the alias by deleting the channel association. If you get the same exception
        again, delete the referring association until the `DeleteBotAlias` operation is
        successful.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if bot_name is not ShapeBase.NOT_SET:
                _params['bot_name'] = bot_name
            _request = shapes.DeleteBotAliasRequest(**_params)
        response = self._boto_client.delete_bot_alias(**_request.to_boto())

    def delete_bot_channel_association(
        self,
        _request: shapes.DeleteBotChannelAssociationRequest = None,
        *,
        name: str,
        bot_name: str,
        bot_alias: str,
    ) -> None:
        """
        Deletes the association between an Amazon Lex bot and a messaging platform.

        This operation requires permission for the `lex:DeleteBotChannelAssociation`
        action.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if bot_name is not ShapeBase.NOT_SET:
                _params['bot_name'] = bot_name
            if bot_alias is not ShapeBase.NOT_SET:
                _params['bot_alias'] = bot_alias
            _request = shapes.DeleteBotChannelAssociationRequest(**_params)
        response = self._boto_client.delete_bot_channel_association(
            **_request.to_boto()
        )

    def delete_bot_version(
        self,
        _request: shapes.DeleteBotVersionRequest = None,
        *,
        name: str,
        version: str,
    ) -> None:
        """
        Deletes a specific version of a bot. To delete all versions of a bot, use the
        DeleteBot operation.

        This operation requires permissions for the `lex:DeleteBotVersion` action.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if version is not ShapeBase.NOT_SET:
                _params['version'] = version
            _request = shapes.DeleteBotVersionRequest(**_params)
        response = self._boto_client.delete_bot_version(**_request.to_boto())

    def delete_intent(
        self,
        _request: shapes.DeleteIntentRequest = None,
        *,
        name: str,
    ) -> None:
        """
        Deletes all versions of the intent, including the `$LATEST` version. To delete a
        specific version of the intent, use the DeleteIntentVersion operation.

        You can delete a version of an intent only if it is not referenced. To delete an
        intent that is referred to in one or more bots (see how-it-works), you must
        remove those references first.

        If you get the `ResourceInUseException` exception, it provides an example
        reference that shows where the intent is referenced. To remove the reference to
        the intent, either update the bot or delete it. If you get the same exception
        when you attempt to delete the intent again, repeat until the intent has no
        references and the call to `DeleteIntent` is successful.

        This operation requires permission for the `lex:DeleteIntent` action.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            _request = shapes.DeleteIntentRequest(**_params)
        response = self._boto_client.delete_intent(**_request.to_boto())

    def delete_intent_version(
        self,
        _request: shapes.DeleteIntentVersionRequest = None,
        *,
        name: str,
        version: str,
    ) -> None:
        """
        Deletes a specific version of an intent. To delete all versions of a intent, use
        the DeleteIntent operation.

        This operation requires permissions for the `lex:DeleteIntentVersion` action.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if version is not ShapeBase.NOT_SET:
                _params['version'] = version
            _request = shapes.DeleteIntentVersionRequest(**_params)
        response = self._boto_client.delete_intent_version(**_request.to_boto())

    def delete_slot_type(
        self,
        _request: shapes.DeleteSlotTypeRequest = None,
        *,
        name: str,
    ) -> None:
        """
        Deletes all versions of the slot type, including the `$LATEST` version. To
        delete a specific version of the slot type, use the DeleteSlotTypeVersion
        operation.

        You can delete a version of a slot type only if it is not referenced. To delete
        a slot type that is referred to in one or more intents, you must remove those
        references first.

        If you get the `ResourceInUseException` exception, the exception provides an
        example reference that shows the intent where the slot type is referenced. To
        remove the reference to the slot type, either update the intent or delete it. If
        you get the same exception when you attempt to delete the slot type again,
        repeat until the slot type has no references and the `DeleteSlotType` call is
        successful.

        This operation requires permission for the `lex:DeleteSlotType` action.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            _request = shapes.DeleteSlotTypeRequest(**_params)
        response = self._boto_client.delete_slot_type(**_request.to_boto())

    def delete_slot_type_version(
        self,
        _request: shapes.DeleteSlotTypeVersionRequest = None,
        *,
        name: str,
        version: str,
    ) -> None:
        """
        Deletes a specific version of a slot type. To delete all versions of a slot
        type, use the DeleteSlotType operation.

        This operation requires permissions for the `lex:DeleteSlotTypeVersion` action.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if version is not ShapeBase.NOT_SET:
                _params['version'] = version
            _request = shapes.DeleteSlotTypeVersionRequest(**_params)
        response = self._boto_client.delete_slot_type_version(
            **_request.to_boto()
        )

    def delete_utterances(
        self,
        _request: shapes.DeleteUtterancesRequest = None,
        *,
        bot_name: str,
        user_id: str,
    ) -> None:
        """
        Deletes stored utterances.

        Amazon Lex stores the utterances that users send to your bot. Utterances are
        stored for 15 days for use with the GetUtterancesView operation, and then stored
        indefinitely for use in improving the ability of your bot to respond to user
        input.

        Use the `DeleteStoredUtterances` operation to manually delete stored utterances
        for a specific user.

        This operation requires permissions for the `lex:DeleteUtterances` action.
        """
        if _request is None:
            _params = {}
            if bot_name is not ShapeBase.NOT_SET:
                _params['bot_name'] = bot_name
            if user_id is not ShapeBase.NOT_SET:
                _params['user_id'] = user_id
            _request = shapes.DeleteUtterancesRequest(**_params)
        response = self._boto_client.delete_utterances(**_request.to_boto())

    def get_bot(
        self,
        _request: shapes.GetBotRequest = None,
        *,
        name: str,
        version_or_alias: str,
    ) -> shapes.GetBotResponse:
        """
        Returns metadata information for a specific bot. You must provide the bot name
        and the bot version or alias.

        This operation requires permissions for the `lex:GetBot` action.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if version_or_alias is not ShapeBase.NOT_SET:
                _params['version_or_alias'] = version_or_alias
            _request = shapes.GetBotRequest(**_params)
        response = self._boto_client.get_bot(**_request.to_boto())

        return shapes.GetBotResponse.from_boto(response)

    def get_bot_alias(
        self,
        _request: shapes.GetBotAliasRequest = None,
        *,
        name: str,
        bot_name: str,
    ) -> shapes.GetBotAliasResponse:
        """
        Returns information about an Amazon Lex bot alias. For more information about
        aliases, see versioning-aliases.

        This operation requires permissions for the `lex:GetBotAlias` action.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if bot_name is not ShapeBase.NOT_SET:
                _params['bot_name'] = bot_name
            _request = shapes.GetBotAliasRequest(**_params)
        response = self._boto_client.get_bot_alias(**_request.to_boto())

        return shapes.GetBotAliasResponse.from_boto(response)

    def get_bot_aliases(
        self,
        _request: shapes.GetBotAliasesRequest = None,
        *,
        bot_name: str,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        name_contains: str = ShapeBase.NOT_SET,
    ) -> shapes.GetBotAliasesResponse:
        """
        Returns a list of aliases for a specified Amazon Lex bot.

        This operation requires permissions for the `lex:GetBotAliases` action.
        """
        if _request is None:
            _params = {}
            if bot_name is not ShapeBase.NOT_SET:
                _params['bot_name'] = bot_name
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if name_contains is not ShapeBase.NOT_SET:
                _params['name_contains'] = name_contains
            _request = shapes.GetBotAliasesRequest(**_params)
        paginator = self.get_paginator("get_bot_aliases").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.GetBotAliasesResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.GetBotAliasesResponse.from_boto(response)

    def get_bot_channel_association(
        self,
        _request: shapes.GetBotChannelAssociationRequest = None,
        *,
        name: str,
        bot_name: str,
        bot_alias: str,
    ) -> shapes.GetBotChannelAssociationResponse:
        """
        Returns information about the association between an Amazon Lex bot and a
        messaging platform.

        This operation requires permissions for the `lex:GetBotChannelAssociation`
        action.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if bot_name is not ShapeBase.NOT_SET:
                _params['bot_name'] = bot_name
            if bot_alias is not ShapeBase.NOT_SET:
                _params['bot_alias'] = bot_alias
            _request = shapes.GetBotChannelAssociationRequest(**_params)
        response = self._boto_client.get_bot_channel_association(
            **_request.to_boto()
        )

        return shapes.GetBotChannelAssociationResponse.from_boto(response)

    def get_bot_channel_associations(
        self,
        _request: shapes.GetBotChannelAssociationsRequest = None,
        *,
        bot_name: str,
        bot_alias: str,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        name_contains: str = ShapeBase.NOT_SET,
    ) -> shapes.GetBotChannelAssociationsResponse:
        """
        Returns a list of all of the channels associated with the specified bot.

        The `GetBotChannelAssociations` operation requires permissions for the
        `lex:GetBotChannelAssociations` action.
        """
        if _request is None:
            _params = {}
            if bot_name is not ShapeBase.NOT_SET:
                _params['bot_name'] = bot_name
            if bot_alias is not ShapeBase.NOT_SET:
                _params['bot_alias'] = bot_alias
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if name_contains is not ShapeBase.NOT_SET:
                _params['name_contains'] = name_contains
            _request = shapes.GetBotChannelAssociationsRequest(**_params)
        paginator = self.get_paginator("get_bot_channel_associations").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.GetBotChannelAssociationsResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.GetBotChannelAssociationsResponse.from_boto(response)

    def get_bot_versions(
        self,
        _request: shapes.GetBotVersionsRequest = None,
        *,
        name: str,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.GetBotVersionsResponse:
        """
        Gets information about all of the versions of a bot.

        The `GetBotVersions` operation returns a `BotMetadata` object for each version
        of a bot. For example, if a bot has three numbered versions, the
        `GetBotVersions` operation returns four `BotMetadata` objects in the response,
        one for each numbered version and one for the `$LATEST` version.

        The `GetBotVersions` operation always returns at least one version, the
        `$LATEST` version.

        This operation requires permissions for the `lex:GetBotVersions` action.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.GetBotVersionsRequest(**_params)
        paginator = self.get_paginator("get_bot_versions").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.GetBotVersionsResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.GetBotVersionsResponse.from_boto(response)

    def get_bots(
        self,
        _request: shapes.GetBotsRequest = None,
        *,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        name_contains: str = ShapeBase.NOT_SET,
    ) -> shapes.GetBotsResponse:
        """
        Returns bot information as follows:

          * If you provide the `nameContains` field, the response includes information for the `$LATEST` version of all bots whose name contains the specified string.

          * If you don't specify the `nameContains` field, the operation returns information about the `$LATEST` version of all of your bots.

        This operation requires permission for the `lex:GetBots` action.
        """
        if _request is None:
            _params = {}
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if name_contains is not ShapeBase.NOT_SET:
                _params['name_contains'] = name_contains
            _request = shapes.GetBotsRequest(**_params)
        paginator = self.get_paginator("get_bots").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.GetBotsResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.GetBotsResponse.from_boto(response)

    def get_builtin_intent(
        self,
        _request: shapes.GetBuiltinIntentRequest = None,
        *,
        signature: str,
    ) -> shapes.GetBuiltinIntentResponse:
        """
        Returns information about a built-in intent.

        This operation requires permission for the `lex:GetBuiltinIntent` action.
        """
        if _request is None:
            _params = {}
            if signature is not ShapeBase.NOT_SET:
                _params['signature'] = signature
            _request = shapes.GetBuiltinIntentRequest(**_params)
        response = self._boto_client.get_builtin_intent(**_request.to_boto())

        return shapes.GetBuiltinIntentResponse.from_boto(response)

    def get_builtin_intents(
        self,
        _request: shapes.GetBuiltinIntentsRequest = None,
        *,
        locale: typing.Union[str, shapes.Locale] = ShapeBase.NOT_SET,
        signature_contains: str = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.GetBuiltinIntentsResponse:
        """
        Gets a list of built-in intents that meet the specified criteria.

        This operation requires permission for the `lex:GetBuiltinIntents` action.
        """
        if _request is None:
            _params = {}
            if locale is not ShapeBase.NOT_SET:
                _params['locale'] = locale
            if signature_contains is not ShapeBase.NOT_SET:
                _params['signature_contains'] = signature_contains
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.GetBuiltinIntentsRequest(**_params)
        paginator = self.get_paginator("get_builtin_intents").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.GetBuiltinIntentsResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.GetBuiltinIntentsResponse.from_boto(response)

    def get_builtin_slot_types(
        self,
        _request: shapes.GetBuiltinSlotTypesRequest = None,
        *,
        locale: typing.Union[str, shapes.Locale] = ShapeBase.NOT_SET,
        signature_contains: str = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.GetBuiltinSlotTypesResponse:
        """
        Gets a list of built-in slot types that meet the specified criteria.

        For a list of built-in slot types, see [Slot Type
        Reference](https://developer.amazon.com/public/solutions/alexa/alexa-skills-
        kit/docs/built-in-intent-ref/slot-type-reference) in the _Alexa Skills Kit_.

        This operation requires permission for the `lex:GetBuiltInSlotTypes` action.
        """
        if _request is None:
            _params = {}
            if locale is not ShapeBase.NOT_SET:
                _params['locale'] = locale
            if signature_contains is not ShapeBase.NOT_SET:
                _params['signature_contains'] = signature_contains
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.GetBuiltinSlotTypesRequest(**_params)
        paginator = self.get_paginator("get_builtin_slot_types").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.GetBuiltinSlotTypesResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.GetBuiltinSlotTypesResponse.from_boto(response)

    def get_export(
        self,
        _request: shapes.GetExportRequest = None,
        *,
        name: str,
        version: str,
        resource_type: typing.Union[str, shapes.ResourceType],
        export_type: typing.Union[str, shapes.ExportType],
    ) -> shapes.GetExportResponse:
        """
        Exports the contents of a Amazon Lex resource in a specified format.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if version is not ShapeBase.NOT_SET:
                _params['version'] = version
            if resource_type is not ShapeBase.NOT_SET:
                _params['resource_type'] = resource_type
            if export_type is not ShapeBase.NOT_SET:
                _params['export_type'] = export_type
            _request = shapes.GetExportRequest(**_params)
        response = self._boto_client.get_export(**_request.to_boto())

        return shapes.GetExportResponse.from_boto(response)

    def get_import(
        self,
        _request: shapes.GetImportRequest = None,
        *,
        import_id: str,
    ) -> shapes.GetImportResponse:
        """
        Gets information about an import job started with the `StartImport` operation.
        """
        if _request is None:
            _params = {}
            if import_id is not ShapeBase.NOT_SET:
                _params['import_id'] = import_id
            _request = shapes.GetImportRequest(**_params)
        response = self._boto_client.get_import(**_request.to_boto())

        return shapes.GetImportResponse.from_boto(response)

    def get_intent(
        self,
        _request: shapes.GetIntentRequest = None,
        *,
        name: str,
        version: str,
    ) -> shapes.GetIntentResponse:
        """
        Returns information about an intent. In addition to the intent name, you must
        specify the intent version.

        This operation requires permissions to perform the `lex:GetIntent` action.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if version is not ShapeBase.NOT_SET:
                _params['version'] = version
            _request = shapes.GetIntentRequest(**_params)
        response = self._boto_client.get_intent(**_request.to_boto())

        return shapes.GetIntentResponse.from_boto(response)

    def get_intent_versions(
        self,
        _request: shapes.GetIntentVersionsRequest = None,
        *,
        name: str,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.GetIntentVersionsResponse:
        """
        Gets information about all of the versions of an intent.

        The `GetIntentVersions` operation returns an `IntentMetadata` object for each
        version of an intent. For example, if an intent has three numbered versions, the
        `GetIntentVersions` operation returns four `IntentMetadata` objects in the
        response, one for each numbered version and one for the `$LATEST` version.

        The `GetIntentVersions` operation always returns at least one version, the
        `$LATEST` version.

        This operation requires permissions for the `lex:GetIntentVersions` action.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.GetIntentVersionsRequest(**_params)
        paginator = self.get_paginator("get_intent_versions").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.GetIntentVersionsResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.GetIntentVersionsResponse.from_boto(response)

    def get_intents(
        self,
        _request: shapes.GetIntentsRequest = None,
        *,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        name_contains: str = ShapeBase.NOT_SET,
    ) -> shapes.GetIntentsResponse:
        """
        Returns intent information as follows:

          * If you specify the `nameContains` field, returns the `$LATEST` version of all intents that contain the specified string.

          * If you don't specify the `nameContains` field, returns information about the `$LATEST` version of all intents. 

        The operation requires permission for the `lex:GetIntents` action.
        """
        if _request is None:
            _params = {}
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if name_contains is not ShapeBase.NOT_SET:
                _params['name_contains'] = name_contains
            _request = shapes.GetIntentsRequest(**_params)
        paginator = self.get_paginator("get_intents").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.GetIntentsResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.GetIntentsResponse.from_boto(response)

    def get_slot_type(
        self,
        _request: shapes.GetSlotTypeRequest = None,
        *,
        name: str,
        version: str,
    ) -> shapes.GetSlotTypeResponse:
        """
        Returns information about a specific version of a slot type. In addition to
        specifying the slot type name, you must specify the slot type version.

        This operation requires permissions for the `lex:GetSlotType` action.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if version is not ShapeBase.NOT_SET:
                _params['version'] = version
            _request = shapes.GetSlotTypeRequest(**_params)
        response = self._boto_client.get_slot_type(**_request.to_boto())

        return shapes.GetSlotTypeResponse.from_boto(response)

    def get_slot_type_versions(
        self,
        _request: shapes.GetSlotTypeVersionsRequest = None,
        *,
        name: str,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.GetSlotTypeVersionsResponse:
        """
        Gets information about all versions of a slot type.

        The `GetSlotTypeVersions` operation returns a `SlotTypeMetadata` object for each
        version of a slot type. For example, if a slot type has three numbered versions,
        the `GetSlotTypeVersions` operation returns four `SlotTypeMetadata` objects in
        the response, one for each numbered version and one for the `$LATEST` version.

        The `GetSlotTypeVersions` operation always returns at least one version, the
        `$LATEST` version.

        This operation requires permissions for the `lex:GetSlotTypeVersions` action.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.GetSlotTypeVersionsRequest(**_params)
        paginator = self.get_paginator("get_slot_type_versions").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.GetSlotTypeVersionsResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.GetSlotTypeVersionsResponse.from_boto(response)

    def get_slot_types(
        self,
        _request: shapes.GetSlotTypesRequest = None,
        *,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        name_contains: str = ShapeBase.NOT_SET,
    ) -> shapes.GetSlotTypesResponse:
        """
        Returns slot type information as follows:

          * If you specify the `nameContains` field, returns the `$LATEST` version of all slot types that contain the specified string.

          * If you don't specify the `nameContains` field, returns information about the `$LATEST` version of all slot types. 

        The operation requires permission for the `lex:GetSlotTypes` action.
        """
        if _request is None:
            _params = {}
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if name_contains is not ShapeBase.NOT_SET:
                _params['name_contains'] = name_contains
            _request = shapes.GetSlotTypesRequest(**_params)
        paginator = self.get_paginator("get_slot_types").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.GetSlotTypesResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.GetSlotTypesResponse.from_boto(response)

    def get_utterances_view(
        self,
        _request: shapes.GetUtterancesViewRequest = None,
        *,
        bot_name: str,
        bot_versions: typing.List[str],
        status_type: typing.Union[str, shapes.StatusType],
    ) -> shapes.GetUtterancesViewResponse:
        """
        Use the `GetUtterancesView` operation to get information about the utterances
        that your users have made to your bot. You can use this list to tune the
        utterances that your bot responds to.

        For example, say that you have created a bot to order flowers. After your users
        have used your bot for a while, use the `GetUtterancesView` operation to see the
        requests that they have made and whether they have been successful. You might
        find that the utterance "I want flowers" is not being recognized. You could add
        this utterance to the `OrderFlowers` intent so that your bot recognizes that
        utterance.

        After you publish a new version of a bot, you can get information about the old
        version and the new so that you can compare the performance across the two
        versions.

        Utterance statistics are generated once a day. Data is available for the last 15
        days. You can request information for up to 5 versions in each request. The
        response contains information about a maximum of 100 utterances for each
        version.

        This operation requires permissions for the `lex:GetUtterancesView` action.
        """
        if _request is None:
            _params = {}
            if bot_name is not ShapeBase.NOT_SET:
                _params['bot_name'] = bot_name
            if bot_versions is not ShapeBase.NOT_SET:
                _params['bot_versions'] = bot_versions
            if status_type is not ShapeBase.NOT_SET:
                _params['status_type'] = status_type
            _request = shapes.GetUtterancesViewRequest(**_params)
        response = self._boto_client.get_utterances_view(**_request.to_boto())

        return shapes.GetUtterancesViewResponse.from_boto(response)

    def put_bot(
        self,
        _request: shapes.PutBotRequest = None,
        *,
        name: str,
        locale: typing.Union[str, shapes.Locale],
        child_directed: bool,
        description: str = ShapeBase.NOT_SET,
        intents: typing.List[shapes.Intent] = ShapeBase.NOT_SET,
        clarification_prompt: shapes.Prompt = ShapeBase.NOT_SET,
        abort_statement: shapes.Statement = ShapeBase.NOT_SET,
        idle_session_ttl_in_seconds: int = ShapeBase.NOT_SET,
        voice_id: str = ShapeBase.NOT_SET,
        checksum: str = ShapeBase.NOT_SET,
        process_behavior: typing.Union[str, shapes.ProcessBehavior] = ShapeBase.
        NOT_SET,
        create_version: bool = ShapeBase.NOT_SET,
    ) -> shapes.PutBotResponse:
        """
        Creates an Amazon Lex conversational bot or replaces an existing bot. When you
        create or update a bot you are only required to specify a name, a locale, and
        whether the bot is directed toward children under age 13. You can use this to
        add intents later, or to remove intents from an existing bot. When you create a
        bot with the minimum information, the bot is created or updated but Amazon Lex
        returns the `` response `FAILED`. You can build the bot after you add one or
        more intents. For more information about Amazon Lex bots, see how-it-works.

        If you specify the name of an existing bot, the fields in the request replace
        the existing values in the `$LATEST` version of the bot. Amazon Lex removes any
        fields that you don't provide values for in the request, except for the
        `idleTTLInSeconds` and `privacySettings` fields, which are set to their default
        values. If you don't specify values for required fields, Amazon Lex throws an
        exception.

        This operation requires permissions for the `lex:PutBot` action. For more
        information, see auth-and-access-control.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if locale is not ShapeBase.NOT_SET:
                _params['locale'] = locale
            if child_directed is not ShapeBase.NOT_SET:
                _params['child_directed'] = child_directed
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if intents is not ShapeBase.NOT_SET:
                _params['intents'] = intents
            if clarification_prompt is not ShapeBase.NOT_SET:
                _params['clarification_prompt'] = clarification_prompt
            if abort_statement is not ShapeBase.NOT_SET:
                _params['abort_statement'] = abort_statement
            if idle_session_ttl_in_seconds is not ShapeBase.NOT_SET:
                _params['idle_session_ttl_in_seconds'
                       ] = idle_session_ttl_in_seconds
            if voice_id is not ShapeBase.NOT_SET:
                _params['voice_id'] = voice_id
            if checksum is not ShapeBase.NOT_SET:
                _params['checksum'] = checksum
            if process_behavior is not ShapeBase.NOT_SET:
                _params['process_behavior'] = process_behavior
            if create_version is not ShapeBase.NOT_SET:
                _params['create_version'] = create_version
            _request = shapes.PutBotRequest(**_params)
        response = self._boto_client.put_bot(**_request.to_boto())

        return shapes.PutBotResponse.from_boto(response)

    def put_bot_alias(
        self,
        _request: shapes.PutBotAliasRequest = None,
        *,
        name: str,
        bot_version: str,
        bot_name: str,
        description: str = ShapeBase.NOT_SET,
        checksum: str = ShapeBase.NOT_SET,
    ) -> shapes.PutBotAliasResponse:
        """
        Creates an alias for the specified version of the bot or replaces an alias for
        the specified bot. To change the version of the bot that the alias points to,
        replace the alias. For more information about aliases, see versioning-aliases.

        This operation requires permissions for the `lex:PutBotAlias` action.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if bot_version is not ShapeBase.NOT_SET:
                _params['bot_version'] = bot_version
            if bot_name is not ShapeBase.NOT_SET:
                _params['bot_name'] = bot_name
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if checksum is not ShapeBase.NOT_SET:
                _params['checksum'] = checksum
            _request = shapes.PutBotAliasRequest(**_params)
        response = self._boto_client.put_bot_alias(**_request.to_boto())

        return shapes.PutBotAliasResponse.from_boto(response)

    def put_intent(
        self,
        _request: shapes.PutIntentRequest = None,
        *,
        name: str,
        description: str = ShapeBase.NOT_SET,
        slots: typing.List[shapes.Slot] = ShapeBase.NOT_SET,
        sample_utterances: typing.List[str] = ShapeBase.NOT_SET,
        confirmation_prompt: shapes.Prompt = ShapeBase.NOT_SET,
        rejection_statement: shapes.Statement = ShapeBase.NOT_SET,
        follow_up_prompt: shapes.FollowUpPrompt = ShapeBase.NOT_SET,
        conclusion_statement: shapes.Statement = ShapeBase.NOT_SET,
        dialog_code_hook: shapes.CodeHook = ShapeBase.NOT_SET,
        fulfillment_activity: shapes.FulfillmentActivity = ShapeBase.NOT_SET,
        parent_intent_signature: str = ShapeBase.NOT_SET,
        checksum: str = ShapeBase.NOT_SET,
        create_version: bool = ShapeBase.NOT_SET,
    ) -> shapes.PutIntentResponse:
        """
        Creates an intent or replaces an existing intent.

        To define the interaction between the user and your bot, you use one or more
        intents. For a pizza ordering bot, for example, you would create an `OrderPizza`
        intent.

        To create an intent or replace an existing intent, you must provide the
        following:

          * Intent name. For example, `OrderPizza`.

          * Sample utterances. For example, "Can I order a pizza, please." and "I want to order a pizza."

          * Information to be gathered. You specify slot types for the information that your bot will request from the user. You can specify standard slot types, such as a date or a time, or custom slot types such as the size and crust of a pizza.

          * How the intent will be fulfilled. You can provide a Lambda function or configure the intent to return the intent information to the client application. If you use a Lambda function, when all of the intent information is available, Amazon Lex invokes your Lambda function. If you configure your intent to return the intent information to the client application. 

        You can specify other optional information in the request, such as:

          * A confirmation prompt to ask the user to confirm an intent. For example, "Shall I order your pizza?"

          * A conclusion statement to send to the user after the intent has been fulfilled. For example, "I placed your pizza order."

          * A follow-up prompt that asks the user for additional activity. For example, asking "Do you want to order a drink with your pizza?"

        If you specify an existing intent name to update the intent, Amazon Lex replaces
        the values in the `$LATEST` version of the intent with the values in the
        request. Amazon Lex removes fields that you don't provide in the request. If you
        don't specify the required fields, Amazon Lex throws an exception. When you
        update the `$LATEST` version of an intent, the `status` field of any bot that
        uses the `$LATEST` version of the intent is set to `NOT_BUILT`.

        For more information, see how-it-works.

        This operation requires permissions for the `lex:PutIntent` action.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if slots is not ShapeBase.NOT_SET:
                _params['slots'] = slots
            if sample_utterances is not ShapeBase.NOT_SET:
                _params['sample_utterances'] = sample_utterances
            if confirmation_prompt is not ShapeBase.NOT_SET:
                _params['confirmation_prompt'] = confirmation_prompt
            if rejection_statement is not ShapeBase.NOT_SET:
                _params['rejection_statement'] = rejection_statement
            if follow_up_prompt is not ShapeBase.NOT_SET:
                _params['follow_up_prompt'] = follow_up_prompt
            if conclusion_statement is not ShapeBase.NOT_SET:
                _params['conclusion_statement'] = conclusion_statement
            if dialog_code_hook is not ShapeBase.NOT_SET:
                _params['dialog_code_hook'] = dialog_code_hook
            if fulfillment_activity is not ShapeBase.NOT_SET:
                _params['fulfillment_activity'] = fulfillment_activity
            if parent_intent_signature is not ShapeBase.NOT_SET:
                _params['parent_intent_signature'] = parent_intent_signature
            if checksum is not ShapeBase.NOT_SET:
                _params['checksum'] = checksum
            if create_version is not ShapeBase.NOT_SET:
                _params['create_version'] = create_version
            _request = shapes.PutIntentRequest(**_params)
        response = self._boto_client.put_intent(**_request.to_boto())

        return shapes.PutIntentResponse.from_boto(response)

    def put_slot_type(
        self,
        _request: shapes.PutSlotTypeRequest = None,
        *,
        name: str,
        description: str = ShapeBase.NOT_SET,
        enumeration_values: typing.List[shapes.EnumerationValue
                                       ] = ShapeBase.NOT_SET,
        checksum: str = ShapeBase.NOT_SET,
        value_selection_strategy: typing.
        Union[str, shapes.SlotValueSelectionStrategy] = ShapeBase.NOT_SET,
        create_version: bool = ShapeBase.NOT_SET,
    ) -> shapes.PutSlotTypeResponse:
        """
        Creates a custom slot type or replaces an existing custom slot type.

        To create a custom slot type, specify a name for the slot type and a set of
        enumeration values, which are the values that a slot of this type can assume.
        For more information, see how-it-works.

        If you specify the name of an existing slot type, the fields in the request
        replace the existing values in the `$LATEST` version of the slot type. Amazon
        Lex removes the fields that you don't provide in the request. If you don't
        specify required fields, Amazon Lex throws an exception. When you update the
        `$LATEST` version of a slot type, if a bot uses the `$LATEST` version of an
        intent that contains the slot type, the bot's `status` field is set to
        `NOT_BUILT`.

        This operation requires permissions for the `lex:PutSlotType` action.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if enumeration_values is not ShapeBase.NOT_SET:
                _params['enumeration_values'] = enumeration_values
            if checksum is not ShapeBase.NOT_SET:
                _params['checksum'] = checksum
            if value_selection_strategy is not ShapeBase.NOT_SET:
                _params['value_selection_strategy'] = value_selection_strategy
            if create_version is not ShapeBase.NOT_SET:
                _params['create_version'] = create_version
            _request = shapes.PutSlotTypeRequest(**_params)
        response = self._boto_client.put_slot_type(**_request.to_boto())

        return shapes.PutSlotTypeResponse.from_boto(response)

    def start_import(
        self,
        _request: shapes.StartImportRequest = None,
        *,
        payload: typing.Any,
        resource_type: typing.Union[str, shapes.ResourceType],
        merge_strategy: typing.Union[str, shapes.MergeStrategy],
    ) -> shapes.StartImportResponse:
        """
        Starts a job to import a resource to Amazon Lex.
        """
        if _request is None:
            _params = {}
            if payload is not ShapeBase.NOT_SET:
                _params['payload'] = payload
            if resource_type is not ShapeBase.NOT_SET:
                _params['resource_type'] = resource_type
            if merge_strategy is not ShapeBase.NOT_SET:
                _params['merge_strategy'] = merge_strategy
            _request = shapes.StartImportRequest(**_params)
        response = self._boto_client.start_import(**_request.to_boto())

        return shapes.StartImportResponse.from_boto(response)
