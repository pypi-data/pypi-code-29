import contextlib
import os
import re

from .validator import Validator


def dict_find_pattern(dic, pattern, search_in_keys=True, search_in_values=True):
    """
    Find keys and values in a (nested) dictionary with regular expression pattern.
    Examples:
        >>> from collections import OrderedDict
        >>> d = OrderedDict((
        ...     ('foo', 'bar'),
        ...     ('bar', 'baz'),
        ...     ('nested', dict(p1=1, p2=2)),
        ...     ('lst', ['bar', 'foo', dict(p3=3, p4=4)])
        ... ))
        >>> f = dict_find_pattern(d, '.*a.*', search_in_keys=True, search_in_values=False)
        >>> def print_findings(f):
        ...     for _, key, value in f:
        ...         print(key, value)
        >>> print_findings(f)
        bar baz
        >>> f = dict_find_pattern(d, '.*a.*', search_in_keys=False, search_in_values=True)
        >>> print_findings(f)
        foo bar
        bar baz

    Args:
        dic: Dictionary to scan for the specified pattern.
        pattern: The pattern to scan for.
        search_in_keys: If True keys will be probed for the pattern; otherwise not.
        search_in_values: If True values will be probed for the pattern; otherwise not.

    Returns:
        Generator to iterate over the findings.
    """

    def find(dic, regex):
        Validator.instance_of(target_type=dict, raise_ex=True, dic=dic)

        for k, v in dic.items():
            if search_in_keys and isinstance(k, str) and regex.match(k):
                yield dic, k, v
            if search_in_values and isinstance(v, str) and regex.match(v):
                yield dic, k, v
            if isinstance(v, list):
                for li in v:
                    # if value and isinstance(li, str) and regex.match(li):
                    #     yield dic, k, li
                    if isinstance(li, dict):
                        for j in find(li, regex):
                            yield j
            if isinstance(v, dict):
                for j in find(v, regex):
                    yield j

    regex = re.compile(pattern)
    return find(dic, regex)


@contextlib.contextmanager
def modified_environ(*remove, **update):
    """
    Temporarily updates the ``os.environ`` dictionary in-place and resets it to the original state when finished.
    (https://stackoverflow.com/questions/2059482/python-temporarily-modify-the-current-processs-environment/34333710#34333710)
    The ``os.environ`` dictionary is updated in-place so that the modification is sure to work in all situations.
    Args:
        remove: Environment variables to remove.
        update: Dictionary of environment variables and values to add/update.
    Examples:
        >>> with modified_environ(Test='abc'):
        ...     import os
        ...     print(os.environ.get('Test'))
        abc
        >>> print(os.environ.get('Test'))
        None
    """
    env = os.environ
    update = update or {}
    remove = remove or []

    # List of environment variables being updated or removed.
    stomped = (set(update.keys()) | set(remove)) & set(env.keys())
    # Environment variables and values to restore on exit.
    update_after = {k: env[k] for k in stomped}
    # Environment variables and values to remove on exit.
    remove_after = frozenset(k for k in update if k not in env)

    try:
        env.update(update)
        [env.pop(k, None) for k in remove]
        yield
    finally:
        env.update(update_after)
        [env.pop(k) for k in remove_after]


def eval_first_non_none(eval_list, **kwargs):
    """
    Executes a list of functions and returns the first non none result. All kwargs will be passed as kwargs to each
    individual function. If all functions return None, None is the overall result.

    Examples:

        >>> eval_first_non_none((lambda: None, lambda: None, lambda: 3))
        3
        >>> print(eval_first_non_none([lambda: None, lambda: None, lambda: None]))
        None
        >>> eval_first_non_none([
        ...     lambda cnt: cnt if cnt == 1 else None,
        ...     lambda cnt: cnt if cnt == 2 else None,
        ...     lambda cnt: cnt if cnt == 3 else None]
        ... , cnt=2)
        2
    """
    Validator.is_real_iterable(raise_ex=True, eval_list=eval_list)

    for eval_fun in eval_list:
        res = eval_fun(**kwargs)
        if res is not None:
            return res
    return None


class FileLocator:
    """
    Based on a base_path, the given file path and a possible parent file path the locator
    will construct a absolute file_path if the given file name is relative.

    If the file path is absolute the absolute file path will be used. If it's relative and a base_path is given the
    both will be concatenated. If no base path is given, the path from the parent file path will be used. If there is
    no parent file path the current working directory is the default.
    """

    def __init__(self, base_path=None, parent_overrides_base=False):
        """
        Args:
            base_path:
            parent_overrides_base: If set to True the file path of the parent (if any) will overrule the base_path;
                otherwise the base_path will overrule the parent's file path even (if any).
        """
        self.base_path = base_path and str(base_path)
        self.parent_overrides_base = bool(parent_overrides_base)

    def _eval_absolute_path(self, abs_or_rel_file_path, **kwargs):
        if os.path.isabs(abs_or_rel_file_path):
            return abs_or_rel_file_path

    def _eval_base_path(self, abs_or_rel_file_path, **kwargs):
        if self.base_path is not None:
            return os.path.join(self.base_path, abs_or_rel_file_path)

    def _eval_parent_file_path(self, abs_or_rel_file_path, parent_file_path, **kwargs):
        if parent_file_path is not None and Validator.is_file(parent_file_path=parent_file_path):
            # If the yaml data is from a file, we assume the base_path should be the path where the file is located
            return os.path.join(os.path.dirname(parent_file_path), abs_or_rel_file_path)

    def _eval_cwd(self, abs_or_rel_file_path, **kwargs):
        return os.path.join(os.getcwd(), abs_or_rel_file_path)

    def _eval_list(self):
        eval_list = [self._eval_absolute_path]
        if self.parent_overrides_base:
            return eval_list + [self._eval_parent_file_path, self._eval_base_path, self._eval_cwd]
        return eval_list + [self._eval_base_path, self._eval_parent_file_path, self._eval_cwd]

    def __call__(self, abs_or_rel_file_path, parent_file_path=None):
        """
        Given a file_path and the actual file path of the parent file the absolute path of the potential relative path
        will be determined. If `parent_file_path` is not None that basically means that the file to locate is part
        of an externally loaded file.
        Args:
            abs_or_rel_file_path: Absolute or relative file path.
            parent_file_path: When it's a file it is used to determine a base path if necessary.
        Returns:
            Returns the absolute path of the file. If it's already absolute, nothing changes.
        """
        return eval_first_non_none(
            self._eval_list(),
            abs_or_rel_file_path=abs_or_rel_file_path,
            parent_file_path=parent_file_path
        )
