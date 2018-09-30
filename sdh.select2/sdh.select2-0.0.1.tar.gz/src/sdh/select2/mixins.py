from django.db.models import QuerySet

from rest_framework.response import Response
from rest_framework.decorators import action

from .serializers import Select2Serializer
from .filters import Select2SearchFilter
from .paginators import Select2Pagination


class Select2Mixin(object):
    """
    List a queryset for select2 jQuery library.
    """
    select2_serializer_class = Select2Serializer
    select2_queryset = None
    select2_pagination_class = Select2Pagination
    select2_filter_backends = (Select2SearchFilter,)
    select2_search_fields = ('name', )

    def get_select2_serializer_class(self):
        """
        Return the class to use for the serializer.
        Defaults to using `self.select2_serializer_class`.

        You may want to override this if you need to provide different
        serializations depending on the incoming request.
        """
        assert self.select2_serializer_class is not None, (
            "'%s' should either include a `select2_serializer_class` attribute, "
            "or override the `select2_serializer_class()` method."
            % self.__class__.__name__
        )
        return self.select2_serializer_class

    def get_select2_serializer(self, *args, **kwargs):
        """
        Return the serializer instance that should be used for validating and
        deserializing input, and for serializing output.
        """
        serializer_class = self.get_select2_serializer_class()
        kwargs['context'] = self.get_serializer_context()
        return serializer_class(*args, **kwargs)

    def get_select2_queryset(self):
        """
        Get the list of items for this view.
        This must be an iterable, and may be a queryset.
        Defaults to using `self.select2_queryset`.

        This method should always be used rather than accessing `self.select2_queryset`
        directly, as `self.queryset` gets evaluated only once, and those results
        are cached for all subsequent requests.

        You may want to override this if you need to provide different
        querysets depending on the incoming request.

        (Eg. return a list of items that is specific to the user)
        """
        assert self.queryset is not None, (
            "'%s' should either include a `queryset` attribute, "
            "or override the `get_queryset()` method."
            % self.__class__.__name__
        )

        _queryset = self.select2_queryset or self.queryset
        if isinstance(_queryset, QuerySet):
            # Ensure queryset is re-evaluated on each request.
            _queryset = _queryset.all()

        for backend in list(self.select2_filter_backends):
            _queryset = backend().filter_queryset(self.request, _queryset, self)
        return _queryset

    @property
    def select2_paginator(self):
        """
        The paginator instance associated with the view, or `None`.
        """
        if not hasattr(self, '_select2_paginator'):
            if self.select2_pagination_class is None:
                self._select2_paginator = None
            else:
                self._select2_paginator = self.select2_pagination_class()
        return self._select2_paginator

    def select2_filter_queryset(self, queryset):
        """
        Given a queryset, filter it with whichever filter backend is in use.

        You are unlikely to want to override this method, although you may need
        to call it either from a list view, or from a custom `get_object`
        method if you want to apply the configured filtering backend to the
        default queryset.
        """
        for backend in list(self.select2_filter_backends):
            queryset = backend().filter_queryset(self.request, queryset, self)
        return queryset

    @action(detail=False)
    def select2(self, request):
        queryset = self.select2_filter_queryset(self.get_select2_queryset())

        page = self.select2_paginator.paginate_queryset(queryset, request, view=self)
        if page is not None:
            serializer = self.get_select2_serializer(page, many=True)
            return self.select2_paginator.get_paginated_response(serializer.data)

        serializer = self.get_select2_serializer(queryset, many=True)
        return Response(serializer.data)
