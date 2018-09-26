try:
    from djangorestframework_camel_case.util import camel_to_underscore
except ImportError:  # drf-camel-case not provided
    def camel_to_underscore(value):
        return value


__all__ = ['camel_to_underscore']
