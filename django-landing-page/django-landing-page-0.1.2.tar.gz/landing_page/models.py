import os
from uuid import uuid4

import itertools

from django.utils.text import slugify
from ckeditor.fields import RichTextField
from django.conf import settings
from django.db import models
from django.utils.deconstruct import deconstructible
from django.utils.translation import ugettext as _
from sorl.thumbnail import ImageField
from fontawesome.fields import IconField


@deconstructible
class PathAndRename(object):

    def __init__(self, sub_path):
        self.path = sub_path

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        filename = '{}.{}'.format(uuid4().hex, ext)
        return os.path.join(self.path, filename)

image_handler = PathAndRename("external_profiles")


class Link(models.Model):
    """

    """
    title = models.CharField(_('Link title'), max_length=100)
    link = models.URLField(_('Url'))
    image = ImageField(_('Link image'), upload_to=image_handler, null=True, blank=True)
    sort_order = models.PositiveIntegerField(_('Sort order'), default=1)
    icon = IconField(_('Icon'), null=True, blank=True)

    class Meta:
        """

        """
        abstract = True
        ordering = ['-sort_order']


class Part(models.Model):
    """

    """
    title = models.CharField(_('Link title'), max_length=100)
    link = models.URLField(_('Link'), null=True, blank=True)
    image = ImageField(_('Image'), upload_to=image_handler, null=True, blank=True)
    sort_order = models.PositiveIntegerField(_('Sort order'), default=1)
    icon = IconField(_('Icon'), null=True, blank=True)
    short_text = models.TextField(_('Short text'), max_length=500, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        """

        """
        abstract = True
        ordering = ['-sort_order']


class ServicePart(Part):
    pass


class TestimonialPart(Part):
    pass


class PricingPart(Part):
    """

    """
    amount = models.CharField(_('Amount'), max_length=10)
    period = models.CharField(_('Pricing period'), max_length=10, null=True, blank=True)


PORTFOLIO_TARGET = (
    ('image', _('Image')),
    ('image_url', _('Image url')),
    ('video', _('Video'))
)


class PortfolioPart(Part):
    """

    """
    title = models.CharField(_('Link title'), max_length=100, null=True, blank=True)
    link = models.URLField(_('Link'), null=True, blank=True)
    image = ImageField(_('Image'), upload_to=image_handler, null=True, blank=True)
    image_url = models.URLField(_('Image url'), null=True, blank=True)
    youtube_code = models.URLField(_('YouTube code'), null=True, blank=True)
    sort_order = models.PositiveIntegerField(_('Sort order'), default=1)
    description = models.TextField(_('Description'), max_length=500, null=True, blank=True)
    preview_target = models.CharField(_('Portfolio preview target'), max_length=15, choices=PORTFOLIO_TARGET, default='image')
    link_target = models.CharField(_('Portfolio click target'), max_length=15, choices=PORTFOLIO_TARGET, default='image')


class Layout(models.Model):
    """

    """
    title = models.CharField(_('Title'), max_length=20)
    folder_name = models.CharField(_('Folder name'), max_length=50)
    bootstrap_based = models.BooleanField(_('Based on Bootstrap 4'), default=False)
    materialize_based = models.BooleanField(_('Based on Materialize'), default=False)
    uses_fontawesome4 = models.BooleanField(_('Uses Font Awesome 4'), default=False)
    uses_fontawesome5 = models.BooleanField(_('Uses Font Awesome 5'), default=False)
    uses_jquery = models.BooleanField(_('Uses jQuery'), default=False)

    def __str__(self):
        return self.title


class LandingPage(models.Model):
    """

    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="landing_pages")
    title = models.CharField(_('Title'), max_length=200)
    slug = models.SlugField(_('Slug'), max_length=100, unique=True)
    tagline = models.CharField(_('Tagline'), max_length=200, null=True, blank=True)
    statement = models.CharField(_('Statement'), max_length=250, null=True, blank=True)
    logo_image = ImageField(_('Logo image'), upload_to=image_handler, null=True, blank=True)
    background_image = ImageField(_('Background image'), upload_to=image_handler, null=True, blank=True)
    hero_image = ImageField(_('Hero image'), upload_to=image_handler, null=True, blank=True)
    hero_youtube_code = models.CharField(_('Hero YouTube code'), max_length=50, null=True, blank=True)
    layout = models.ForeignKey(Layout, on_delete=models.CASCADE)
    copyright_text = models.CharField(_('Copyright text'), max_length=200, null=True, blank=True)

    # About section
    enable_about = models.BooleanField(_('Enable about section'), default=True)
    about_title = models.CharField(_('About title'), max_length=200, default=_('About'))
    about_text = RichTextField(_('About'), null=True, blank=True)
    about_image = ImageField(_('About image'), upload_to=image_handler, null=True, blank=True)

    # Services section
    enable_services = models.BooleanField(_('Enable services section'), default=True)
    services_title = models.CharField(_('Services title'), max_length=200, default=_('Services'))
    services_text = RichTextField(_('Your services'), null=True, blank=True)
    service_parts = models.ManyToManyField(ServicePart, blank=True)

    # Testimonials section
    enable_testimonials = models.BooleanField(_('Enable testimonial section'), default=True)
    testimonials_title = models.CharField(_('Testimonials title'), max_length=200, default=_('Testimonials'))
    testimonials_text = RichTextField(_('Your testimonials'), null=True, blank=True)
    testimonials_parts = models.ManyToManyField(TestimonialPart, blank=True)

    # Pricing section
    enable_pricing = models.BooleanField(_('Enable pricing section'), default=True)
    pricing_title = models.CharField(_('Pricing title'), max_length=200, default=_('Pricing'))
    pricing_text = RichTextField(_('Pricing text'), null=True, blank=True)
    pricing_parts = models.ManyToManyField(PricingPart, blank=True)

    # Portfolio section
    enable_portfolio = models.BooleanField(_('Enable portfolio section'), default=True)
    portfolio_title = models.CharField(_('Portfolio title'), max_length=200, default=_('Portfolio'))
    portfolio_text = RichTextField(_('Portfolio text'), null=True, blank=True)
    portfolio_parts = models.ManyToManyField(PortfolioPart, blank=True)

    # Contact section
    enable_contact = models.BooleanField(_('Enabled contact section'), default=True)
    contact_title = models.CharField(_('Contact Title'), max_length=200, null=True, blank=True)
    contact_text = RichTextField(_('Contact text'), null=True, blank=True)
    homepage = models.URLField(null=True, blank=True)
    email = models.EmailField(_('Email address'), null=True, blank=True)
    phone_number1 = models.CharField(_('Phone number #1'), max_length=20, null=True, blank=True)
    phone_number2 = models.CharField(_('Phone number #2'), max_length=20, null=True, blank=True)
    address1 = models.CharField(_('Address'), max_length=100, null=True, blank=True)
    address2 = models.CharField(_('Extended address'), max_length=100, null=True, blank=True)
    city = models.CharField(_('City'), max_length=100, null=True, blank=True)
    zip_code = models.CharField(_('Zip code'), max_length=10, null=True, blank=True)
    country = models.CharField(_('Country'), max_length=100, null=True, blank=True)
    latitude = models.CharField(_('Latitude'), max_length=15, null=True, blank=True)
    longitude = models.CharField(_('Longitude'), max_length=15, null=True, blank=True)

    # Social media
    facebook = models.URLField(_('Facebook'), null=True, blank=True)
    twitter = models.URLField(_('Twitter'), null=True, blank=True)
    instagram = models.URLField(_('Instagram'), null=True, blank=True)
    github = models.URLField(_('GitHub'), null=True, blank=True)
    linkedin = models.URLField(_('LinkedIn'), null=True, blank=True)
    googleplus = models.URLField(_('Google+'), null=True, blank=True)
    youtube = models.URLField(_('YouTube'), null=True, blank=True)
    flickr = models.URLField(_('Flickr'), null=True, blank=True)

    def __str__(self):
        return _("Landing page for %s") % self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            max_length = LandingPage._meta.get_field('slug').max_length
            self.slug = orig = slugify(self.title)[:max_length]

            for x in itertools.count(1):
                if not LandingPage.objects.filter(slug=self.slug).exists():
                    break

                self.slug = "%s-%d" % (orig[:max_length - len(str(x)) - 1], x)
        super(LandingPage, self).save(*args, **kwargs)
