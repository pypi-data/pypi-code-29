from method_override import settings


class MethodOverrideMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_view(self, request, view_func, view_args, view_kwargs):
        if request.method != 'POST':
            return None
        method = self._get_method_override(request)
        if method in settings.ALLOWED_HTTP_METHODS:
            request.method = method

    def _get_method_override(self, request):
        method = (
            request.POST.get(settings.PARAM_KEY) or
            request.META.get(settings.HTTP_HEADER)
        )
        return method and method.upper()
