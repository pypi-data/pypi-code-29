#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. codeauthor:: Cédric Dumay <cedric.dumay@gmail.com>


"""
import opentracing
from cdumay_opentracing import OpenTracingSpan, OpenTracingDriver


class RequestSpan(OpenTracingSpan):
    """A container to store the current span"""

    def __init__(self, obj, tags=None):
        OpenTracingSpan.__init__(
            self, obj, " ".join((obj.method, obj.path)), tags
        )


class RequestDriver(OpenTracingDriver):
    FORMAT = opentracing.Format.HTTP_HEADERS
    TAGS = ['path', 'method']

    @classmethod
    def extract(cls, data):
        """ Extract span context from a `carrier` object

        :param Any data: the `carrier` object.
        :return: a SpanContext instance extracted from `carrier` or None if no
            such span context could be found.
        """
        return opentracing.tracer.extract(cls.FORMAT, data.headers)

    @classmethod
    def inject(cls, span, data):
        """ Injects the span context into a `carrier` object.

        :param opentracing.span.SpanContext span: the SpanContext instance to inject
        :param Any data: the `carrier` object.
        """

        opentracing.tracer.inject(span, cls.FORMAT, data.headers)

    @classmethod
    def tags(cls, data):
        """ Extract tags from `carrier` object.

        :param Any data: the `carrier` object.
        :return: Tags to add on span
        :rtype: dict
        """
        return dict([(attr, getattr(data, attr, None)) for attr in cls.TAGS])
