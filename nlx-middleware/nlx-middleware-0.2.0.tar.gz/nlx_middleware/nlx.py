from typing import Generator, Tuple

from django.apps import apps

__all__ = ['get_service_pairs', 'TO_NLX', 'FROM_NLX']

TO_NLX = 'to-nlx'
FROM_NLX = 'from-nlx'


def get_service_pairs(direction: str) -> Generator[Tuple[str, str], None, None]:
    """
    Return an interable yielding replacement pairs to rewrite from/to NLx urls.

    This is the main entry point to retrieve rewrite data. Depending on if and
    when features in NLx land, this may be changed into swappable backends
    to manage the pairs.

    TODO: caching?
    """
    assert direction in [TO_NLX, FROM_NLX], f"Unknown direction: '{direction}'"

    if not apps.is_installed('nlx_middleware'):
        # app not installed -> no models registered -> nothing to do
        # in an alternative scenario, we *might* fall back to querying NLx
        # directory if this becomes possible.
        return ()

    NLxService = apps.get_model('nlx_middleware.NLxService')

    if direction == TO_NLX:
        from_attr, to_attr = 'address', 'outway_address'
    elif direction == FROM_NLX:
        from_attr, to_attr = 'outway_address', 'address'

    for service in NLxService.objects.iterator():
        yield (
            getattr(service, from_attr),
            getattr(service, to_attr),
        )
