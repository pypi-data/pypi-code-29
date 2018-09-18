#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. codeauthor:: Cédric Dumay <cedric.dumay@gmail.com>


"""
import logging

import opentracing

logger = logging.getLogger(__name__)


class OpenTracingDriver(object):
    FORMAT = opentracing.Format.TEXT_MAP
    TAGS = []

    @classmethod
    def extract(cls, data):
        """ Extract span context from a `carrier` object

        :param Any data: the `carrier` object.
        :return: a SpanContext instance extracted from `carrier` or None if no
            such span context could be found.
        """
        return opentracing.tracer.extract(cls.FORMAT, data)

    @classmethod
    def inject(cls, span, data):
        """ Injects the span context into a `carrier` object.

        :param opentracing.span.SpanContext span: the SpanContext instance to inject
        :param Any data: the `carrier` object.
        """

        opentracing.tracer.inject(span, cls.FORMAT, data)

    @classmethod
    def tags(cls, data):
        """ Extract tags from `carrier` object.

        :param Any data: the `carrier` object.
        :return: Tags to add on span
        :rtype: dict
        """
        return vars(data)

    @classmethod
    def log_kv(cls, span, data, event, **kwargs):
        """ Adds a log record to the Span.

        :param opentracing.span.Span span: the Span instance to use.
        :param Any data: the `carrier` object.
        :param str event: Span event name.
        :param dict kwargs: A dict of string keys and values of any type to log
        :return: Returns the Span itself, for call chaining.
        :rtype: opentracing.span.Span
        """
        return span.log_kv({"event": event, **kwargs})


class OpenTracingSpan(object):
    """A container to store the current span"""

    def __init__(self, obj, name, tags=None):
        self.obj = obj
        self.name = name
        self.tags = tags
        self._span = None

    def __enter__(self):
        """Context guard used by the with statement"""
        self._span = OpenTracingManager.create_span(
            self.obj, self.name, self.tags
        )
        return self._span

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context guard used by the with statement"""
        OpenTracingManager.finish_span(self._span)


class OpenTracingManager(object):
    _registry = dict()
    _spans = list()

    @classmethod
    def register(cls, clazz, driver):
        """ Register a driver for the given class

        :param Any clazz: Class managed by the driver.
        :param cdumay_opentracing.OpenTracingDriver driver: Driver to register.
        """
        if not issubclass(driver, OpenTracingDriver):
            raise RuntimeError(
                "Only class which implement OpenTracingDriver are allowed"
            )
        OpenTracingManager._registry[clazz] = driver
        logger.debug("Registered {} for {}".format(driver, clazz))

    @classmethod
    def get_driver(cls, obj):
        """ Find registered driver for the given object

        :param Any obj: object to manipulate
        :return: registered driver for this class
        :rtype: cdumay_opentracing.OpenTracingDriver
        """
        for clazz, driver in OpenTracingManager._registry.items():
            if isinstance(obj, clazz):
                logger.debug("{} driver will be used for {}".format(
                    driver, obj
                ))
                return driver
        logger.warning("No driver found for {}, default will be used".format(
            obj
        ))
        return OpenTracingDriver

    @classmethod
    def tags(cls, obj):
        """ Extract tags from `carrier` object using a registered driver.

        :param Any obj: object to manipulate
        :return: Tags to add on span
        :rtype: dict
        """
        driver = cls.get_driver(obj)
        return driver.tags(obj) if driver else dict()

    @classmethod
    def get_current_span(cls, obj):
        """ Get the current span

        :param Any obj: Any object
        :return: The current span
        :rtype: opentracing.span.Span or None
        """
        if len(OpenTracingManager._spans) > 0:
            return OpenTracingManager._spans[-1]
        else:
            driver = cls.get_driver(obj)
            if driver:
                try:
                    return driver.extract(obj)
                except:
                    pass

    @classmethod
    def create_span(cls, obj, name, tags=None):
        """ Create a new span

        :param Any obj: Any object
        :param str name: Span name
        :param dict tags: Additional tags
        :return: Span
        :rtype: opentracing.span.Span
        """
        parent = cls.get_current_span(obj)
        driver = cls.get_driver(obj)
        span_tags = tags or dict()

        if obj:
            span_tags.update(driver.tags(obj))
        span = opentracing.tracer.start_span(
            operation_name=name, child_of=parent, tags=span_tags
        )
        OpenTracingManager._spans.append(span)
        return span

    @classmethod
    def finish_span(cls, span=None):
        """ Terminate the given span

        :param opentracing.span.Span span: Span to finish
        """
        if span:
            OpenTracingManager._spans.remove(span)
        else:
            span = OpenTracingManager._spans.pop()

        if span:
            span.finish()

    @classmethod
    def finish_all(cls):
        for span in OpenTracingManager._spans[::-1]:
            span.finish()
        OpenTracingManager._spans = list()

    @classmethod
    def log_kv(cls, span, obj, event, **kwargs):
        """ Adds a log record to the Span.

        :param opentracing.span.Span span: the Span instance to use.
        :param Any obj: the `carrier` object.
        :param str event: Span event name.
        :param dict kwargs: A dict of string keys and values of any type to log
        :return: Returns the Span itself, for call chaining.
        :rtype: opentracing.span.Span
        """
        return cls.get_driver(obj).log_kv(span, obj, event, **kwargs)
