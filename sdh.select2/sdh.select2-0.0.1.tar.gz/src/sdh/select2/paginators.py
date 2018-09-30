from collections import OrderedDict

from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination


class Select2Pagination(PageNumberPagination):
    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('results', data),
            ('pagination', {'more': self.get_next_link()})
        ]))
