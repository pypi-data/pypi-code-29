#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. codeauthor:: Cédric Dumay <cedric.dumay@gmail.com>


"""
import opentracing
import requests

from cdumay_opentracing import OpenTracingManager, SpanProxy
from cdumay_rest_client.client import RESTClient


class RequestSpan(SpanProxy):
    FORMAT = opentracing.Format.HTTP_HEADERS
    TAGS = ['url', 'method']

    @classmethod
    def name(cls, obj):
        return " ".join((obj.method, obj.path))

    @classmethod
    def extract(cls, obj):
        """ Extract span context from the given object

        :param Any obj: Object to use as context
        :return: a SpanContext instance extracted from the inner span object or None if no
            such span context could be found.
        """
        return opentracing.tracer.extract(cls.FORMAT, obj.headers)

    @classmethod
    def inject(cls, span, obj):
        """ Injects the span context into a `carrier` object.

        :param opentracing.span.SpanContext span: the SpanContext instance
        :param Any obj: Object to use as context
        """
        opentracing.tracer.inject(span, cls.FORMAT, obj.headers)

    @classmethod
    def postrun(cls, span, obj, **kwargs):
        """ Trigger to execute just before closing the span

        :param opentracing.span.Span  span: the SpanContext instance
        :param Any obj: Object to use as context
        :param dict kwargs: additional data
        """
        span.set_tag("response.status_code", obj.status_code)
        span.set_tag(
            "response.content_lenght", len(getattr(obj, 'content', ""))
        )


class OpentracingRESTClient(RESTClient):
    def _request_wrapper(self, **kwargs):
        with OpenTracingManager.create_span(
                obj=None, name="{method} {url}".format_map(kwargs),
                context=OpenTracingManager.get_current_span(self)
        ) as span_proxy:
            span_proxy.inject(span_proxy.span, kwargs['headers'])
            resp = requests.request(**kwargs)
            RequestSpan.postrun(span_proxy.span, resp)
            return resp
