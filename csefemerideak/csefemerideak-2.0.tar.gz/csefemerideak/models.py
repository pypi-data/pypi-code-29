from django.db import models
from django.template.loader import render_to_string
from datetime import datetime
from django.conf import settings

from django.urls import reverse

from django.conf import settings
from .utils.text import truncate_words

TITLE_WORDS = getattr(settings, "UZTARRIA_TITLE_WORDS", 10)


class EfemerideaManager(models.Manager):
    """ """

    def gaurkoak(self):
        gaur = datetime.today()
        return Efemeridea.objects.filter(
            eguna=gaur.day, hila=gaur.month, is_public=True
        )

    def egunbatekoak(self, date):
        return Efemeridea.objects.filter(
            eguna=date.day, hila=date.month, is_public=True
        )

    def urtebatekoak(self, urtea):
        return Efemeridea.objects.filter(urtea=urtea, is_public=True)

    def hamarkadabatekoak(self, hamarkada):
        return Efemeridea.objects.filter(hamarkada=hamarkada, is_public=True)


class Efemeridea(models.Model):
    """ """

    text = models.TextField()
    moretext = models.TextField(null=True, blank=True)
    date = models.DateField()

    eguna = models.IntegerField(db_index=True)
    hila = models.IntegerField(db_index=True)
    urtea = models.IntegerField(db_index=True)
    hamarkada = models.IntegerField(db_index=True)

    is_public = models.BooleanField(default=True)

    added = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    objects = models.Manager()
    egunekoak = EfemerideaManager()

    def _get_title(self):
        """ """
        return truncate_words(self.text, TITLE_WORDS * 2)

    title = property(_get_title)

    def has_moretext(self):
        """ """
        return self.moretext and True or False

    has_moretext.boolean = True

    def get_absolute_url(self):
        """ """
        return reverse("csefemerideak_efemeridea", args=[self.pk])

    def __unicode__(self):
        return "%s-%s-%s: %s" % (self.urtea, self.hila, self.eguna, self.text[:100])

    def save(self, *args, **kwargs):
        """ """
        self.urtea = self.date.year
        self.hila = self.date.month
        self.eguna = self.date.day
        self.hamarkada = self.urtea // 10 * 10
        super(Efemeridea, self).save(*args, **kwargs)

    class Meta:
        ordering = ["-date"]
        verbose_name = "Efemeridea"
        verbose_name_plural = "Efemerideak"


"""
def update_fields(sender, instance, *args, **kwargs):
    instance.urtea = instance.date.year
    instance.hila = instance.date.month
    instance.eguna = instance.date.day
    instance.hamarkada = instance.urtea/10*10   

pre_save.connect(update_fields, sender=Efemeridea)
"""
