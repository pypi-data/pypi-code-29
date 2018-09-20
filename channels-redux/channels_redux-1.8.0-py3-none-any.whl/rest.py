from collections import OrderedDict
from importlib import import_module
from sys import stderr
from typing import Type

from django.conf import settings
from django.conf.urls import url as urlpattern
from django.core.exceptions import ImproperlyConfigured
from django.db.models import Model
from django.utils.module_loading import autodiscover_modules
from rest_framework import serializers, viewsets
from rest_framework.routers import DefaultRouter, APIRootView


class RestAPIRootView(APIRootView):
    view_name = 'All Root'

    def get_view_name(self):
        if self.view_name:
            return self.view_name
        else:
            return super(APIRootView, self).get_view_name()


def getpath(obj, path):
    current = obj
    for part in path:
        current = getattr(current, part)
    return current


class RestRouter(DefaultRouter):
    APIRootView = RestAPIRootView

    BASE_NAME_PATH = ['_meta', 'label_lower']
    MODEL_NAME = ['_meta', 'verbose_name_plural']
    NAMESPACE_PATH = ['_meta', 'app_label']

    _registered_serializers = {}
    _apps = []
    _urls_by_app = OrderedDict()

    def __init__(self, *args, **kwargs):
        skip_warning = kwargs.pop('skip_warning') or False
        if not skip_warning:
            print("You're instantiating RestRouter, you should probably use channels_redux.rest.router instead")
        super(RestRouter, self).__init__(*args, **kwargs)

    def get_default_base_name(self, viewset):
        """
        If `base_name` is not specified, attempt to automatically determine
        it from the viewset.
        """
        queryset = getattr(viewset, 'queryset', None)

        assert queryset is not None, '`base_name` argument not specified, and could ' \
                                     'not automatically determine the name from the viewset, as ' \
                                     'it does not have a `.queryset` attribute.'

        return getpath(queryset.model, self.BASE_NAME_PATH)

    def register_model(self, model, serializer=None, viewset=None,
                       fields=None, exclude_fields=None, include_fields=None,
                       queryset=None, filter_func=None, url=None, permissions_classes=None):
        exclude_fields = exclude_fields or set()
        include_fields = include_fields or set()
        fields = self.get_default_fields_for_model(model, fields, exclude_fields, include_fields)

        serializer = serializer or self.get_default_serializer(model, fields)
        self._registered_serializers[model] = serializer
        if not issubclass(serializer, HyperlinkedModelSerializer):
            print("Serializer is not an instance of channels_redux.rest.HyperlinkedModelSerializer "
                  "unexpected behavior may occur", file=stderr)

        queryset = queryset or self.get_default_queryset(model)
        if viewset is None:
            viewset = self.get_default_viewset(queryset, serializer, filter_func, permissions_classes)
        else:
            viewset.serializer_class = serializer  # Ensure that the serializer on the viewset matches the one we expect

        if url is None:
            url = self.get_default_url(model)
        self.register(url, viewset)
        self.add_url(model)

    def add_url(self, model):
        app_config = model._meta.app_config
        self._apps.append(app_config)

        existing_urls = self._urls_by_app.get(app_config.verbose_name, OrderedDict())
        existing_urls[self.format_url(getpath(model, self.MODEL_NAME))] = self.list_name(model)
        self._urls_by_app[app_config.verbose_name] = existing_urls

    def list_name(self, model):
        return self.routes[0].name.format(basename=getpath(model, self.BASE_NAME_PATH))

    def get_default_queryset(self, model):
        return model.objects.all()

    def get_serializer(self, model):
        return self._registered_serializers[model]

    def get_default_url(self, model):
        return '/'.join((
            self.format_url(getpath(model, self.NAMESPACE_PATH)),
            self.format_url(getpath(model, self.MODEL_NAME))
        ))

    def format_url(self, part: str):
        return part.replace(' ', '-').replace('_', '-')

    def get_default_serializer(self, model_class, serializer_fields):
        class ModelSerializer(HyperlinkedModelSerializer):
            class Meta:
                model = model_class
                fields = serializer_fields
        return ModelSerializer

    def get_default_viewset(self, qs, serializer, filter_func, permissions):
        class ModelViewSet(viewsets.ModelViewSet):
            queryset = qs
            serializer_class = serializer
            permission_classes = permissions or tuple()

            def get_queryset(self):
                if filter_func is None:
                    return self.queryset
                return filter_func(self.queryset, self.request)
        return ModelViewSet

    def get_default_fields_for_model(self, model: Type[Model], fields, exclude_fields, include_fields):
        if fields is not None:
            updated_fields = set(fields)
            updated_fields.add('pk')
            updated_fields.add('url')
            return tuple(updated_fields)

        updated_fields = set(include_fields)
        excluded = set(exclude_fields)

        updated_fields.add('url')  # Always include this
        updated_fields |= model._meta._property_names  # This include pk as well as developer defined properties

        for field in model._meta.get_fields():
            if field.auto_created or field.name in excluded:  # Skip reverse relations
                continue
            updated_fields.add(field.name)

        return tuple(updated_fields)

    def get_urls(self):
        extra_urls = []
        for app_config in self._apps:
            root_view = self.APIRootView.as_view(api_root_dict=self._urls_by_app[app_config.verbose_name],
                                                 view_name='{} Root'.format(app_config.verbose_name))

            extra_urls.append(urlpattern(r'^{}/$'.format(self.format_url(app_config.name)),
                                         view=root_view,
                                         name='{}-root'.format(app_config.name)))
        extra_urls.append(urlpattern('^all/$', view=super(RestRouter, self).get_api_root_view(), name='all-root'))
        return super(RestRouter, self).get_urls() + extra_urls

    def get_api_root_view(self, api_urls=None):
        api_root_dict = OrderedDict()
        for app_config in self._apps:
            api_root_dict[app_config.verbose_name] = '{}-root'.format(app_config.name)
        api_root_dict['All'] = 'all-root'
        return self.APIRootView.as_view(api_root_dict=api_root_dict, view_name='Api Root')


def autodiscover():
    autodiscover_modules('rest', register_to=None)


def _get_router_class():
    module_path, class_name = settings.CHANNELS_REDUX_ROUTER_CLASS.rsplit('.', 1)
    try:
        router_module = import_module(module_path)
        return getattr(router_module, class_name)
    except (AttributeError, ImportError) as e:
        raise ImproperlyConfigured(
            'settings.CHANNELS_REDUX_ROUTER_CLASS is improperly configured. Could not find {}. '
            'Please supply a valid class or use the default.'.format(settings.CHANNELS_REDUX_ROUTER_CLASS)
        ) from e


RouterClass = _get_router_class()
router = RouterClass(skip_warning=True)


class HyperlinkedModelSerializer(serializers.HyperlinkedModelSerializer):
    @staticmethod
    def fix_view_name(field_kwargs, model):
        if 'view_name' in field_kwargs:
            view_name_suffix = field_kwargs['view_name'].split('-')[-1]
            field_kwargs['view_name'] = "{}:{}-{}".format(settings.API_APP_NAMESPACE,
                                                          getpath(model, RouterClass.BASE_NAME_PATH),
                                                          view_name_suffix)
        return field_kwargs

    def build_url_field(self, field_name, model_class):
        field_class, field_kwargs = super().build_url_field(field_name, model_class)
        return field_class, self.fix_view_name(field_kwargs, self.Meta.model)

    def build_relational_field(self, field_name, relation_info):
        field_class, field_kwargs = super().build_relational_field(field_name, relation_info)
        return field_class, self.fix_view_name(field_kwargs, model=relation_info[1])
