#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. codeauthor:: Cédric Dumay <cedric.dumay@gmail.com>


"""
import logging
import opentracing
from jaeger_client import Span

logger = logging.getLogger(__name__)


class SpanProxy(object):
    FORMAT = opentracing.Format.TEXT_MAP
    TAGS = []

    def __init__(self, span, obj):
        self.span = span
        self.obj = obj

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

        :param opentracing.span.SpanContext span: the SpanContext instance
        :param Any obj: Object to use as context
        """
        opentracing.tracer.inject(span, cls.FORMAT, obj)

    @classmethod
    def prerun(cls, span, obj, **kwargs):
        """ Trigger to execute just after span creation

        :param opentracing.span.SpanContext span: the SpanContext instance
        :param Any obj: Object to use as context
        :param dict kwargs: additional data
        """

    @classmethod
    def postrun(cls, span, obj, **kwargs):
        """ Trigger to execute just before closing the span

        :param opentracing.span.Span  span: the SpanContext instance
        :param Any obj: Object to use as context
        :param dict kwargs: additional data
        """

    @classmethod
    def log_kv(cls, span, obj, event, **kwargs):
        """ Trigger to execute just before closing the span

        :param opentracing.span.Span span: the SpanContext instance
        :param Any obj: Object to use as context
        :param str event: Event name
        :param dict kwargs: additional data
        """
        return span.log_kv({"event": event, **kwargs})

    def __enter__(self):
        """Invoked when span is used as a context manager.

        :return: returns the Span itself
        """
        if self not in OpenTracingManager._proxies:
            OpenTracingManager._proxies.append(self)
        self.prerun(self.span, self.obj)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context guard used by the with statement"""
        if self in OpenTracingManager._proxies:
            OpenTracingManager._proxies.remove(self)
        self.postrun(self.span, self.obj)
        Span.__exit__(self.span, exc_type, exc_val, exc_tb)


class OpenTracingManager(object):
    _registry = dict()
    _proxies = list()

    @classmethod
    def register(cls, proxy_factory, *classes):
        """ Register a driver for the given class(es)

        :param cdumay_opentracing.SpanProxy proxy_factory: codec to register.
        :param list classes: Classes managed by the factory.
        """
        if not issubclass(proxy_factory, SpanProxy):
            raise RuntimeError(
                "Only class which implement SpanProxy are allowed"
            )
        for clazz in classes:
            OpenTracingManager._registry[clazz] = proxy_factory
            logger.debug("Registered {} for {}".format(proxy_factory, clazz))

    @classmethod
    def get_proxy_factory(cls, obj):
        """ Return the registered proxy factory for the given object

        :param Any obj: Object to use
        :return: Codec which implement SpanProxy
        :rtype: cdumay_opentracing.SpanProxy
        """
        for clazz, driver in OpenTracingManager._registry.items():
            if isinstance(obj, clazz):
                logger.debug("{} driver will be used for {}".format(
                    driver, obj
                ))
                return driver

        logger.warning(
            "No driver found for {}, default will be used".format(obj)
        )
        return SpanProxy

    @classmethod
    def get_current_span(cls, obj):
        """ Get the current span

        :param Any obj: Any object
        :return: The current span
        :rtype: opentracing.span.Span or None
        """
        if len(OpenTracingManager._proxies) > 0:
            return OpenTracingManager._proxies[-1].span
        else:
            proxy_factory = cls.get_proxy_factory(obj)
            if proxy_factory:
                try:
                    return proxy_factory.extract(obj)
                except:
                    pass

    @classmethod
    def create_span(cls, obj, name=None, context=None, tags=None):
        """ Create a new span

        :param Any obj: Any object
        :param str name: Span name
        :param opentracing.span.Span context: Non-managed span (extracted)
        :param dict tags: Additional tags
        :return: Span
        :rtype: OpenTracingSpan
        """
        span_tags = tags or dict()
        proxy_factory = cls.get_proxy_factory(obj)
        if obj:
            span_tags.update(proxy_factory.extract_tags(obj))

        proxy = proxy_factory(obj=obj, span=opentracing.tracer.start_span(
            operation_name=name or proxy_factory.name(obj),
            child_of=context or OpenTracingManager.get_current_span(obj),
            tags=tags or proxy_factory.extract_tags(obj)
        ))
        OpenTracingManager._proxies.append(proxy)
        return proxy

    @classmethod
    def finish_span(cls, proxy=None):
        """ Terminate the given span proxy

        :param opentracing.SpanProxy proxy: span proxy to finish
        """
        if proxy:
            OpenTracingManager._proxies.remove(proxy)
        else:
            proxy = OpenTracingManager._proxies.pop()

        if proxy:
            proxy.span.finish()

    @classmethod
    def finish_all(cls):
        for proxy in OpenTracingManager._proxies[::-1]:
            proxy.span.finish()
        OpenTracingManager._proxies = list()

    @classmethod
    def log_kv(cls, event, proxy=None, obj=None, timestamp=None, **kwargs):
        """ Adds a log record to the Span.

        :param str event: Span event name.
        :param cdumay_opentracing.SpanProxy proxy: the span proxy instance to use.
        :param Any obj: Object to use
        :param float timestamp: A unix timestamp per time.time(); current time if None
        :param dict kwargs: A dict of string keys and values of any type to log
        :return: Returns the Span itself, for call chaining.
        :rtype: opentracing.span.Span
        """
        span = proxy.span if proxy else cls.get_current_span(obj)
        if span:
            return span.log_kv(dict(event=event, **kwargs), timestamp=timestamp)
