from django.db import transaction
from django.db.models import QuerySet
from . import exceptions, settings
import json


class ProcessQuerySet(QuerySet):
    def from_json(self, data):
        try:
            data = json.loads(data)
        except Exception:
            raise exceptions.ConfigurationError(
                'JSON data could not be parsed.'
            )

        if not isinstance(data, dict):
            raise exceptions.ConfigurationError(
                'Spec must be an object, not %s.' % type(data).__name__
            )

        return self.create_process(**data)

    @transaction.atomic()
    def create_process(
        self,
        input_bundle,
        output_bundle,
        operations=[],
        meta={}
    ):
        from .models import Bundle, Operation

        if not isinstance(input_bundle, dict):
            raise exceptions.ConfigurationError(
                'input_bundle must be an object, not %s.' % type(
                    input_bundle
                ).__name__
            )

        if not isinstance(output_bundle, dict):
            raise exceptions.ConfigurationError(
                'output_bundle must be an object, not %s.' % type(
                    output_bundle
                ).__name__
            )

        if not isinstance(operations, (list, tuple)):
            raise exceptions.ConfigurationError(
                'operations must be an array, not %s.' % type(
                    operations
                ).__name__
            )

        if not any(operations):
            raise exceptions.ConfigurationError(
                'operations array is empty.'
            )

        if not isinstance(meta, dict):
            raise exceptions.ConfigurationError(
                'meta must be an object, not %s.' % type(meta).__name__
            )

        tags = meta.pop('tags', [])

        try:
            input_bundle = Bundle.objects.create_bundle(**input_bundle)
        except exceptions.BundleConfigurationError as ex:
            raise exceptions.ConfigurationError(
                "Error with input_bundle.%s: %s" % (
                    ex.key,
                    ex.args[0]
                )
            )

        try:
            output_bundle = Bundle.objects.create_bundle(**output_bundle)
        except exceptions.BundleConfigurationError as ex:
            raise exceptions.ConfigurationError(
                "Error with output_bundle.%s: %s" % (
                    ex.key,
                    ex.args[0]
                )
            )

        process = self.create(
            input_bundle=input_bundle,
            output_bundle=output_bundle,
            meta=json.dumps(meta)
        )

        for i, operation in enumerate(operations):
            try:
                Operation.objects.create_operation(
                    process,
                    i,
                    **operation
                )
            except exceptions.OperationConfigurationError as ex:
                raise exceptions.ConfigurationError(
                    "Error with operations[%d]: %s" % (
                        ex.index,
                        ex.args[0]
                    )
                )

        if not isinstance(tags, (list, tuple)):
            raise exceptions.ConfigurationError(
                'meta.tags must be an array, not %s.' % type(tags).__name__
            )

        for index, tag in enumerate(tags):
            if not isinstance(tag, str):
                raise exceptions.ConfigurationError(
                    'meta.tags[%d] must be a string, not %s.' % (
                        index,
                        type(tag).__name__
                    )
                )

            process.tags.create(name=tag)

        return process


class BundleQuerySet(QuerySet):
    @transaction.atomic()
    def create_bundle(self, **kwargs):
        bundle = self.create()

        for name, kw in kwargs.items():
            kind = kw.pop('type', None)
            mime_type = kw.pop('mime_type', None)

            if not kind:
                raise exceptions.BundleConfigurationError(
                    name,
                    'Missing type definition.'
                )

            if kind == 'media' and not mime_type:
                raise exceptions.BundleConfigurationError(
                    name,
                    'Missing mime_type definition for media type.'
                )

            if kind not in settings.BUNDLE_ITEM_KINDS:
                raise exceptions.BundleConfigurationError(
                    name,
                    '"%s" is not a valid type.' % kind
                )

            for k, v in kw.items():
                raise exceptions.BundleConfigurationError(
                    name,
                    '"%s" is not a valid property.' % k
                )

            try:
                bundle.create_item(
                    name,
                    kind=kind,
                    mime_type=mime_type
                )
            except Exception:  # pragma: no cover
                raise exceptions.BundleConfigurationError(
                    name,
                    'Unknown error in item definition.'
                )

        return bundle


class OperationQuerySet(QuerySet):
    @transaction.atomic()
    def create_operation(self, process, index, **kwargs):
        name = kwargs.pop('name', None)
        if not name:
            raise exceptions.OperationConfigurationError(
                index,
                'Missing name definition.'
            )

        if not isinstance(name, str):
            raise exceptions.OperationConfigurationError(
                index,
                'name must be a string, not %s.' % type(name).__name__
            )

        match = settings.CODENAME_RE.match(name)

        if match is None:
            raise exceptions.OperationConfigurationError(
                index,
                'name must be in "nemsapce.function" format.'
            )

        namespace, function = match.groups()
        only = kwargs.pop('only', {})
        scheduling = kwargs.pop('scheduling', 'auto')
        can_fail = kwargs.pop('can_fail', False)
        messages = kwargs.pop('messages', {})
        only_tags = []

        if scheduling not in settings.OPERATION_SCHEDULES:
            raise exceptions.OperationConfigurationError(
                index,
                'scheduling must be set to "auto" or "manual".'
            )

        if not isinstance(can_fail, bool):
            raise exceptions.OperationConfigurationError(
                index,
                'can_fail must be a boolean, not %s.' % type(can_fail).__name__
            )

        if not isinstance(only, dict):
            raise exceptions.OperationConfigurationError(
                index,
                'only must be an object, not %s.' % type(only).__name__
            )

        for k, v in only.items():
            if k == 'tags':
                if not isinstance(v, (list, tuple)):
                    raise exceptions.OperationConfigurationError(
                        index,
                        'only.tags must be an array, not %s.' % (
                            type(v).__name__
                        )
                    )

                for i, a in enumerate(v):
                    if not isinstance(a, str):
                        raise exceptions.OperationConfigurationError(
                            index,
                            'only.tags[%d] must be a string, not %s.' % (
                                i,
                                type(a).__name__
                            )
                        )

                    only_tags.append(a)

                continue

            raise exceptions.OperationConfigurationError(
                index,
                'only contains an invalid property ("%s").' % k
            )

        if not isinstance(messages, dict):
            raise exceptions.OperationConfigurationError(
                index,
                'messages must be an object, not %s.' % (
                    type(messages).__name__
                )
            )

        for k, v in messages.items():
            if k not in settings.MESSAGE_KINDS:
                raise exceptions.OperationConfigurationError(
                    index,
                    '"%s" is not a valid message type.' % k
                )

            if not isinstance(v, str):
                raise exceptions.OperationConfigurationError(
                    index,
                    'messages.%s must be a string, not %s.' % (
                        k,
                        type(v).__name__
                    )
                )

        try:
            obj = self.model(
                process=process,
                namespace=namespace,
                function=function,
                ordering=index,
                scheduling=scheduling,
                can_fail=can_fail,
                **kwargs
            )

            if not obj.verbose_name:
                obj.verbose_name = obj.function.replace('_', ' ').capitalize()

            obj.full_clean()
        except Exception:  # pragma: no cover
            raise exceptions.OperationConfigurationError(
                index,
                'Unknown error in process definition'
            )

        obj.save()

        for tag in only_tags:
            obj.restrictions.create(
                kind='tag',
                value=tag
            )

        for kind, text in messages.items():
            obj.messages.create(
                kind=kind,
                text=text
            )

        return obj
