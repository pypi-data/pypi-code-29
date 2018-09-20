#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. codeauthor:: Cédric Dumay <cedric.dumay@gmail.com>


"""
import logging

import jaeger_client
import opentracing

logger = logging.getLogger(__name__)


class OpenTracingCodec(object):
    FORMAT = opentracing.Format.TEXT_MAP
    TAGS = []
    MANAGED = ()

    @classmethod
    def _validate_object(cls, obj):
        """ validate that the given object is supported by the codec

        :param Any obj: object to use as context
        """
        if len(cls.MANAGED) > 0:
            if not issubclass(obj.__class__, cls.MANAGED):
                logger.warning(
                    "{} instance is not managed by this codec, "
                    "allowed: {}".format(
                        obj.__class__.__name__,
                        [str(x.__name__) for x in cls.MANAGED]
                    )
                )
                return False
        return True

    @classmethod
    def start_span(cls, obj=None, context=None, name=None, tags=None):
        """ Create a span using the given object or context

        :param Any obj: current context for object
        :param jaeger_client.SpanContext context: current context from a span
        :param str name: span name
        :param dict tags: additional tags
        :return: a span
        :rtype: jaeger_client.Span
        """
        span_tags = tags or dict()
        child_of = None

        if obj and cls._validate_object(obj):
            span_tags.update(cls.extract_tags(obj))
            child_of = cls.extract(obj)

        # we overwrite object context if a context is set!
        if context and issubclass(context.__class__, (opentracing.span.Span, opentracing.span.SpanContext)):
            child_of = context

        span = opentracing.tracer.start_span(
            operation_name=name or cls.name(obj), child_of=child_of,
            tags=span_tags
        )
        span.__codec = cls
        if cls._validate_object(obj):
            cls._prerun(span, obj)
        return span

    @classmethod
    def stop_span(cls, span, obj=None, **kwargs):
        """ Finish the given span

        :param jaeger_client.Span span: span to close
        :param Any obj: object to use as context
        :param dict kwargs: additional data
        """
        if cls._validate_object(obj):
            cls._postrun(span, obj, **kwargs)
        return span.finish()

    @classmethod
    def name(cls, obj):
        """ Extract span name from the given object

        :param Any obj: Object to use as context
        :return: Span name
        :rtype: str
        """
        return str(obj)

    @classmethod
    def extract(cls, obj):
        """ Extract span context from the given object

        :param Any obj: Object to use as context
        :return: a SpanContext instance extracted from the inner span object or None if no
            such span context could be found.
        """
        if cls._validate_object(obj):
            return opentracing.tracer.extract(cls.FORMAT, obj)

    @classmethod
    def extract_tags(cls, obj):
        """ Extract tags from the given object

        :param Any obj: Object to use as context
        :return: Tags to add on span
        :rtype: dict
        """
        return dict(
            [(attr, getattr(obj, attr, None)) for attr in cls.TAGS]
        )

    @classmethod
    def inject(cls, span, obj):
        """ Injects the span context into a `carrier` object.

        :param jaeger_client.SpanContext span: the SpanContext instance
        :param Any obj: Object to use as context
        """
        if cls._validate_object(obj):
            opentracing.tracer.inject(span, cls.FORMAT, obj)

    @classmethod
    def _prerun(cls, span, obj, **kwargs):
        """ Trigger to execute just after span creation

        :param jaeger_client.SpanContext span: the SpanContext instance
        :param Any obj: Object to use as context
        :param dict kwargs: additional data
        """

    @classmethod
    def _postrun(cls, span, obj, **kwargs):
        """ Trigger to execute just before closing the span

        :param jaeger_client.Span span: the SpanContext instance
        :param Any obj: Object to use as context
        :param dict kwargs: additional data
        """
