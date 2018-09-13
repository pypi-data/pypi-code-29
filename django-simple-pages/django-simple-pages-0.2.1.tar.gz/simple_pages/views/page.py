"""Views for rendering simple_pages.models.Page objects."""

from django.conf import settings
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.template import loader, exceptions
from django.utils.safestring import mark_safe
from django.views.generic import TemplateView

from ..models import Page


class PageView(TemplateView):
    """View to render a Page."""

    request = None
    page = None
    template_name = "simple_pages/default.html"

    def get_page(self, url):
        """Get and render the page for this view using the URL."""
        page = None

        if not url.startswith("/"):
            url = "/" + url

        # Try to fetch the Page by the current URL.
        try:
            page = Page.objects.get(access_url=url, enabled=True)
        except Page.DoesNotExist:

            # Change the URL according to the settings...
            if url.endswith("/"):
                _url = url.rstrip("/")
            elif settings.APPEND_SLASH:
                _url = url + "/"
            else:
                _url = url

            # ...and retry the query if it's been modified.
            if _url != url:
                try:
                    page = Page.objects.get(access_url=_url, enabled=True)
                except Page.DoesNotExist:
                    pass

        return page

    def dispatch(self, request, *args, **kwargs):
        """Set the Page instance, if found."""
        url = request.path_info
        self.request = request

        self.page = self.get_page(url=url)
        if not self.page:
            raise Http404

        if self.page.redirect_url:
            return HttpResponseRedirect(redirect_to=self.page.redirect_url)
        else:
            return super(PageView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        """Add the Page object to the context for this view."""
        self.page.title = mark_safe(self.page.title)
        self.page.content = mark_safe(self.page.content)

        context = super(PageView, self).get_context_data(**kwargs)
        context.update({"page": self.page})
        return context

    def get(self, request, *args, **kwargs):
        """Respond to GET requests."""
        context = self.get_context_data()
        template = self.get_template()
        return HttpResponse(template.render(context=context, request=request))

    def get_template(self):
        """Get the template based on the page's template_path."""
        try:
            # If self.page.template name is blank, it'll throw an IOError.
            t = loader.get_template(template_name=self.page.template_name)
        except (IOError, exceptions.TemplateDoesNotExist):
            t = loader.get_template(template_name=self.template_name)

        return t
