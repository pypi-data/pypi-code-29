"""
Test cases for functionality provided by the provider.utils module
"""

from datetime import datetime, date

from django.db import models
from django.test import TestCase

from provider import utils


class UtilsTestCase(TestCase):
    def test_serialization(self):
        class SomeModel(models.Model):
            dt = models.DateTimeField()
            t = models.TimeField()
            d = models.DateField()

        instance = SomeModel(dt=datetime.now(),
                             d=date.today(),
                             t=datetime.now().time())
        instance.nonfield = 'hello'
        data = utils.serialize_instance(instance)
        instance2 = utils.deserialize_instance(SomeModel, data)
        self.assertEqual(instance.nonfield, instance2.nonfield)
        self.assertEqual(instance.d, instance2.d)
        self.assertEqual(instance.dt.date(), instance2.dt.date())
        for t1, t2 in [(instance.t, instance2.t),
                       (instance.dt.time(), instance2.dt.time())]:
            self.assertEqual(t1.hour, t2.hour)
            self.assertEqual(t1.minute, t2.minute)
            self.assertEqual(t1.second, t2.second)
            # AssertionError:
            #   datetime.time(10, 6, 28, 705776) !=
            #   datetime.time(10, 6, 28, 705000)
            self.assertEqual(int(t1.microsecond / 1000),
                             int(t2.microsecond / 1000))

    def test_none_child_(self):
        class ChildModel(models.Model):
            pass

        class ParentModel(models.Model):
            child = models.ForeignKey(ChildModel, on_delete=models.CASCADE, null=True)

        reference = ParentModel()

        data = utils.serialize_instance(reference)
        self.assertEqual(data['child_id'], None)

        instance = utils.deserialize_instance(ParentModel, data)
        self.assertEqual(instance.child, None)
