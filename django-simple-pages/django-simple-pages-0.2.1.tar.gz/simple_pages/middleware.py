"""Middleware for the simple_pages app."""

from django.http import Http404
from django.utils.deprecation import MiddlewareMixin

from .views import PageView


class PageFallbackMiddleware(MiddlewareMixin):
    """Checks any 404 responses and passes the request's URL to the PageView.

    If a corresponding Page is not found for the URL, the original 404
    response is returned.
    """

    def process_response(self, request, response):
        """If the response is 404, try to find a Page for the request's URL.

        :param request: The original HttpRequest.
        :param response: The original HttpResponse.
        """
        if response.status_code != 404:
            return response

        try:
            page = PageView()
            return page.dispatch(request)
        except Http404:
            return response
