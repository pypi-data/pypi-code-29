# Create your models here.
import django.http
from django.core.exceptions import ValidationError
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db import models
from django.shortcuts import render
from django.utils.translation import ugettext_lazy as _
from mutagen.mp3 import MP3
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page
from wagtail.documents.edit_handlers import DocumentChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index


# Create your models here.

class PodcastParentPage(RoutablePageMixin, Page):
    """
    The model that acts as the base page for the podcast. All podcasts are children of this page and this page lists the various podcasts.
    """

    languages = (
        ('af-ZA', 'Afrikaans'),
        ('en-ZA', 'English')
    )

    language = models.CharField(max_length=5, choices=languages, default='af-ZA', help_text=_('Language of podcast'),
                                verbose_name=_('Language'))

    copyright = models.CharField(max_length=255, help_text=_('Copyright holder of podcast'),
                                 verbose_name=_('Copyright'))

    subtitle = models.CharField(max_length=255, help_text=_('Subtitle of podacst'), verbose_name=_('Subtitle'))

    author = models.CharField(max_length=255, help_text=_('Author of podcast'), verbose_name=_('Author'))

    description = models.TextField(help_text=_('Description of nature of podcast'), verbose_name=_('Description'))

    owner_name = models.CharField(max_length=255, help_text=_('Owner of the podcast channel'),
                                  verbose_name=_('Owner name'))

    owner_email = models.EmailField(help_text=_('Email address of the podcast owner'), verbose_name=_('Owner email'))

    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name=_('Image'),
        help_text=_('Cover image for podcast')
    )

    category = models.CharField(max_length=255, help_text=_('Category of the podcast address'),
                                verbose_name=_('Category'))

    page_text = RichTextField(null=True, help_text=_('Main text page that appears on the root page'),
                              verbose_name=_('Page Text'))

    itunes_url = models.URLField(blank=True, verbose_name=_('Itunes Podcast Url'))
    google_url = models.URLField(blank=True, verbose_name=_('Google Play Podcast Url'))
    blubrry_url = models.URLField(blank=True, verbose_name=_('Blubrry Podcast Url'))

    explicit = models.BooleanField(default=False, help_text=_('Whether the podcast channel contains explicit content'),
                                   verbose_name=_('Explicit'))

    content_panels = Page.content_panels + [
        FieldPanel('language'),
        FieldPanel('copyright'),
        FieldPanel('subtitle'),
        FieldPanel('author'),
        FieldPanel('description'),
        FieldPanel('owner_name'),
        FieldPanel('owner_email'),
        ImageChooserPanel('image'),
        FieldPanel('page_text'),
        FieldPanel('category'),
        MultiFieldPanel([
            FieldPanel('itunes_url'),
            FieldPanel('google_url'),
            FieldPanel('blubrry_url')], heading=_('Podcast Directory URLs'), classname='collapsible collapsed'),
        FieldPanel('explicit')
    ]

    show_in_menus = True
    subpage_types = ['wagtail_podcast.PodcastPage']

    search_fields = Page.search_fields + [
        index.SearchField('page_text'),
        index.SearchField('description')
    ]

    class Meta:
        verbose_name = _("Podcast Root Page")

    def get_context(self, request: django.http.HttpRequest, *args, **kwargs):
        """
        Normal get_context used by Wagtail overridden to include to archives and podcasts

        :param request:
        :param args: Django request args
        :param kwargs: Django request kwargs
        :return: Context of the page
        """

        context = super(PodcastParentPage, self).get_context(request)

        context['archives'] = self.get_archives()
        context['podcasts'] = self.get_pagination(request, kwargs)

        return context

    @route(r"^podcast/$")
    def podcastFeed(self, request: django.http.HttpRequest, **kwargs) -> django.http.HttpResponse:
        """
        Routing for the feed url for use by clients and services to access the rss/xml feed

        :param request: Normal django request
        :param kwargs:  Normal django request kwargs
        :return: rss/xml file
        """
        podcasts = PodcastPage.objects.live()
        return render(request, "wagtail_podcast/feed.xml",
                      {'self': self, 'page': self, 'podcasts': podcasts}, content_type='application/rss+xml')

    @route(r"^(?P<year>(?:19|20)\d\d)/(?P<month>1[012]|0[1-9])/$")
    def archiveMonth(self, request: django.http.HttpRequest, **kwargs) -> django.http.HttpResponse:
        """
        Routing for a specific year and month combination

        :param request: Normal Django request object
        :param kwargs: Normal Django request kwargs
        :return: Page displaying the podcasts from a specific month and year combo with pagination
        """

        return render(request, "wagtail_podcast/podcast_parent_page.html",
                      {'self': self, 'page': self, 'podcasts': self.get_pagination(request, kwargs),
                       'archives': self.get_archives()})

    @route(r"^(?P<year>(?:19|20)\d\d)/$")
    def archiveYear(self, request: django.http.HttpRequest, **kwargs) -> django.http.HttpResponse:
        """
        Returns the entries of a year

        :param request: Django request object
        :param kwargs: Django request kwargs
        :return: HttpResponse
        """

        return render(request, "wagtail_podcast/podcast_parent_page.html",
                      {'self': self, 'page': self, 'podcasts': self.get_pagination(request, kwargs),
                       'archives': self.get_archives()})

    @property
    def get_podcasts(self) -> models.QuerySet:
        """
        Returns all the podcast objects that are currently live

        :return: Returns a Queryset of all the podcast objects
        """

        return PodcastPage.objects.live()

    def get_archives(self) -> list:
        """
        Return the archives of the podcast (date-based)

        :return: List of dictionaries containing a key of 'date' and an archive to accompany it
        """

        archives = list(PodcastPage.objects.live().dates('first_published_at', 'month', order='DESC'))
        archives = [{'date': archive} for archive in archives]
        return archives

    def get_pagination(self, request: django.http.request.HttpRequest, kwargs) -> django.core.paginator.Paginator:
        """
        Paginates the podcast queryset. We return the last 5 podcasts by default.

        :param request: Django request object
        :param kwargs: Django kwargs associated with the request
        :return: Returns a pagination object
        """

        if ('year' in kwargs) and ('month' in kwargs):
            podcasts = PodcastPage.objects.live().filter(first_published_at__year=kwargs['year'],
                                                         first_published_at__month=kwargs['month']).order_by(
                '-first_published_at')
        elif 'year' in kwargs:
            podcasts = PodcastPage.objects.live().filter(first_published_at__year=kwargs['year']).order_by(
                '-first_published_at')
        else:
            podcasts = self.get_children().live().order_by('-first_published_at')
        paginator = Paginator(podcasts, 5)  # Show 5 resources per page

        page = request.GET.get('page')
        try:
            podcasts = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            podcasts = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            podcasts = paginator.page(paginator.num_pages)

        return podcasts

    @property
    def get_podcast_url(self) -> str:
        """
        Return URL of a the podcast parent page

        :return: Url of the podcast parent page
        """

        return self.url

    @property
    def get_feed_url(self) -> str:
        """
        Returns the url of the feed of the podcast. Used for subscribing to and submitting to services like iTunes

        :return: URL of the podcast
        """

        return self.url + 'podcast/'


class PodcastPage(Page):
    """
    Model that acts as a specific podcast and is a child of the PodcastParentPage object
    """

    episodeTypes = (
        ('full', _('Full')),
        ('trailer', _('Trailer')),
        ('bonus', _('Bonus'))
    )

    episodeType = models.CharField(max_length=255, choices=episodeTypes, default='full', help_text=_('Type of episode'),
                                   verbose_name=_('Episode Type'))
    author = models.CharField(max_length=255, help_text=_('Author of particular podcast'), verbose_name=_('Author'))
    subtitle = models.CharField(max_length=255, help_text=_('Subtitle of particular podcast'),
                                verbose_name=_('Subtitle'))
    description = models.TextField(help_text=_('Description of podcast'), verbose_name=_('Description'))

    recording = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name=_('Recording')
    )

    explicit = models.BooleanField(default=False, help_text=_('Whether the podcast contains explicit content'),
                                   verbose_name=_('Explicit'))

    guid = Page.pk

    duration = models.IntegerField(default=300)

    length = models.IntegerField(default=1024)

    page_text = RichTextField(null=True, help_text=_('Content that accompanies the podcast'),
                              verbose_name=_('Page Text'))

    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name=_('Image')
    )

    content_panels = Page.content_panels + [
        FieldPanel('episodeType'),
        FieldPanel('author'),
        FieldPanel('subtitle'),
        FieldPanel('description'),
        FieldPanel('page_text'),
        DocumentChooserPanel('recording'),
        ImageChooserPanel('image'),
        FieldPanel('explicit')
    ]

    show_in_menus = False
    parent_page_type = ['wagtail_podcast.PodcastParentPage']
    subpage_types = []

    search_fields = Page.search_fields + [
        index.SearchField('description'),
        index.SearchField('page_text'),
        index.SearchField('subtitle'),
    ]

    class Meta:
        verbose_name = _("Podcast")

    def clean(self):
        """
        Validates that the audio file passed is indeed a valid MP3 file.
        """

        try:
            self.duration = int(MP3(self.recording.file.path).info.length)
        except Exception as e:
            raise ValidationError('Not a valid MP3 file')

    def save(self, *args, **kwargs):
        """
        Saves the model and adds metadata like length of file in bytes for Itunes and other services and well as adds the duration to the model.

        :param args: Not important
        :param kwargs: Not important
        """

        self.length = self.recording.file.size
        self.duration = int(MP3(self.recording.file.path).info.length)
        if not self.image:
            self.image = PodcastParentPage.objects.live()[0].image
        super(PodcastPage, self).save()

    def get_context(self, request: django.http.HttpRequest, *args, **kwargs):
        """
        Returns the context for a given page. This overriden function adds the archives to the context.

        :param request: Django request object
        :param args: Django request \*args
        :param kwargs: Django request \*\*kwargs
        :return: Django/Wagtail context object
        """

        context = super(PodcastPage, self).get_context(request)

        context['archives'] = self.get_archives()

        return context

    def get_archives(self) -> list:
        """
        Gets the archives relating to the podcast

        :param self:
        :return: List of dictionaries containing 'date' as key and a podcast as a value
        """
        archives = list(PodcastPage.objects.live().dates('first_published_at', 'month', order='DESC'))
        archives = [{'date': archive} for archive in archives]
        return archives

    @property
    def get_podcast_url(self) -> str:
        """
        Get the url of the parent podcast page

        :return: URL of the parent page
        """
        return self.get_parent().url

    @property
    def get_feed_url(self) -> str:
        """
        Get the url of the feed that represents the rss/xml file of the podcast

        :return: URL of the rss/xml feed
        """
        return self.get_parent().url + 'podcast/'

    @property
    def itunes_url(self) -> str:
        """
        Returns the itunes url

        :return: Itunes URL
        """
        return self.get_parent().specific.itunes_url

    @property
    def google_url(self) -> str:
        """
        Returns the Google Play url

        :return: Google Play URL
        """
        return self.get_parent().specific.google_url

    @property
    def blubrry_url(self) -> str:
        """
        Returns the blubrry url

        :return: Blubrry URL
        """
        return self.get_parent().specific.blubrry_url
