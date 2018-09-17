# -*- coding:utf-8 -*-

import six
import numpy as np
from django.db import models
from django.test import TestCase
from rest_framework import serializers
from djsci.fields import *
from djsci.drf_fields import *
from hypothesis import given
import hypothesis.strategies as st
from hypothesis.extra.numpy import arrays, array_dtypes, scalar_dtypes, array_shapes


class TestingArrayModel(models.Model):
    arr = NumpyArrayField()


class TestingArraySerializer(serializers.ModelSerializer):
    class Meta:
        model = TestingArrayModel
        fields = ['id', 'arr']

    arr = DRFNumpyArrayField()


class FieldTestCase(TestCase):
    def test_arr(self):
        for i in range(10):
            arr = arrays(dtype='f8', shape=array_shapes()).example()
            m = TestingArrayModel(arr=arr)
            # m.save()
            # m = TestingArrayModel.objects.get(pk=m.id)
            six.print_(arr, TestingArraySerializer(m).data)
            self.assertEqual(np.allclose(arr, m.arr, equal_nan=True), True)