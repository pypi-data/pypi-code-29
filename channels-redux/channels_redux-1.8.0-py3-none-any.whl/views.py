import os.path
from typing import List, Union

from django.db.models import QuerySet, Model
from django.views.generic import *

from channels_redux.rest import router


def get_app_name(obj):
    return obj.__module__.split('.')[0]


def redux_objects(key_field, *model_object_pairs):
    object_state = {}
    for pair in model_object_pairs:
        model_name, serialized_objects = pair
        existing = object_state.get(model_name, {})
        object_state[model_name] = {
            **existing,
            **key_to_object_dict(key_field, serialized_objects)
        }
    return object_state


def key_to_object_dict(key_field, serialized_objects: Union[list, dict]):
    if isinstance(serialized_objects, list):
        return {obj[key_field]: obj for obj in serialized_objects}
    else:
        return {serialized_objects[key_field]: serialized_objects}


class ReactView(TemplateView):
    use_objects_as_state = True
    querysets = None  # type: List[Union[QuerySet, Model]]
    initial_react_state = {}
    react_component = None
    template_component_name = 'component'
    react_dist_directory = 'dist'
    template_state_name = 'props'
    key_field = 'url'

    def get_initial_react_state(self):
        if self.use_objects_as_state:
            return self.object_based_react_state()
        else:
            return self.initial_react_state

    def get_react_component(self):
        return os.path.join(self.react_dist_directory, get_app_name(self), self.react_component)

    def get_context_data(self, **kwargs):
        return {
            **super(ReactView, self).get_context_data(**kwargs),
            **self.get_react_context()
        }

    def get_react_context(self):
        context = {
            self.template_state_name: self.get_initial_react_state(),
            self.template_component_name: self.get_react_component(),
            "key_field": self.key_field
        }
        return context

    def get_querysets(self) -> List[Union[QuerySet, Model]]:
        return self.querysets

    def object_based_react_state(self):
        return {"objects": self.get_serialized_objects()}

    def get_serialized_objects(self):
        model_object_pairs = []
        for queryset_or_object in self.get_querysets():
            if isinstance(queryset_or_object, QuerySet):
                serializer = router.get_serializer(queryset_or_object.model)
                model_name = queryset_or_object.model._meta.label_lower
                many = True
            else:
                serializer = router.get_serializer(queryset_or_object._meta.model)
                model_name = queryset_or_object._meta.label_lower
                many = False
            serialized_objects = serializer(queryset_or_object,
                                            context={'request': self.request, 'view': self, 'format': None},
                                            many=many).data
            model_object_pairs.append((model_name, serialized_objects))
        return redux_objects(self.key_field, *model_object_pairs)


ReactMultiModelView = ReactView  # Alias for ReactView to avoid breaking backwards compatibility
