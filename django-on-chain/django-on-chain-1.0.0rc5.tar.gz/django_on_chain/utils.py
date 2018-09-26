from django.utils.translation import get_language

try:
    from urlparse import parse_qs, urlparse
except ImportError:  # For Python 3
    from urllib.parse import parse_qs, urlparse


def django_files_to_requests_files(files):
    return {k: (f.name, f.read(), f.content_type) for k, f in files.items()} if files is not None else None


def to_error_list(errors, fields):
    """
    Converts from django error format to a list of error strings. The fields must have `label` attribute.

    :param errors: Usually `serializer.errors` or `form.errors`
    :param fields: Usually `serializer.fields` or `form.fields`
    :return: A list of error strings
    """
    return [
        '{field_name}: {error_message}'.format(
            field_name=fields[field_key].label,
            error_message=field_errors[0].encode('utf-8'),
        )
        for field_key, field_errors in errors.items()
    ]


def append_lang_param(url, param_name):
    query = urlparse(url).query
    if param_name not in parse_qs(query):
        if url[-1] not in ['?', '&']:
            url += '&' if query else '?'
        url += '{}={}'.format(param_name, get_language())
    return url
