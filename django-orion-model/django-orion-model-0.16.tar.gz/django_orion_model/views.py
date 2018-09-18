from django.views.generic.detail import SingleObjectMixin


class DynamicSingleObjectMixin(SingleObjectMixin):
    """Provides de capability to load a object  by a specific subclass stored in a """
    model = None
    subclass_field = "subclass"

    def get_object(self, queryset=None):
        obj = super() .get_object(queryset)
        self.model = getattr(obj, self.subclass_field, "__class__")
        return getattr(obj, self.model.lower())
