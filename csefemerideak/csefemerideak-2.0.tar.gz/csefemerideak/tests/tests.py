import datetime

from django.urls import reverse
from django.test import TestCase

from .factories import EfemerideaFactory


class TestViews(TestCase):
    def test_hamarkada_index(self):
        efemerideak = EfemerideaFactory.create_batch(5)
        response = self.client.get(
            reverse("csefemerideak_hamarkada_index", args=[efemerideak[0].hamarkada])
        )
        self.assertEqual(response.status_code, 200)

    def test_eguna_view(self):
        date = datetime.date(1900, 9, 1)
        EfemerideaFactory(date=date)
        response = self.client.get(
            reverse("csefemerideak_eguna_index", args=[date.month, date.day])
        )
        self.assertEqual(response.status_code, 200)
