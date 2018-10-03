"""Python wrappers around TensorFlow ops.

This file is MACHINE GENERATED! Do not edit.
Original C++ source file: ops_py_wrapper.cc
"""

import collections as _collections
import six as _six

from tensorflow.python import pywrap_tensorflow as _pywrap_tensorflow
from tensorflow.python.eager import context as _context
from tensorflow.python.eager import core as _core
from tensorflow.python.eager import execute as _execute
from tensorflow.python.framework import dtypes as _dtypes
from tensorflow.python.framework import errors as _errors
from tensorflow.python.framework import tensor_shape as _tensor_shape

from tensorflow.core.framework import op_def_pb2 as _op_def_pb2
# Needed to trigger the call to _set_call_cpp_shape_fn.
from tensorflow.python.framework import common_shapes as _common_shapes
from tensorflow.python.framework import op_def_registry as _op_def_registry
from tensorflow.python.framework import ops as _ops
from tensorflow.python.framework import op_def_library as _op_def_library
from tensorflow.python.util.tf_export import tf_export


_cobine_sparse_successor_outputs = ["result_indices", "result_values",
                                   "result_shape"]
_CobineSparseSuccessorOutput = _collections.namedtuple(
    "CobineSparseSuccessor", _cobine_sparse_successor_outputs)


@tf_export('cobine_sparse_successor')
def cobine_sparse_successor(parent_indices, parent_shape, child_indices, child_values, child_shape, name=None):
  r"""TODO: add doc.

  Args:
    parent_indices: A `Tensor` of type `int64`.
    parent_shape: A `Tensor` of type `int64`.
    child_indices: A `Tensor` of type `int64`.
    child_values: A `Tensor` of type `string`.
    child_shape: A `Tensor` of type `int64`.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (result_indices, result_values, result_shape).

    result_indices: A `Tensor` of type `int64`.
    result_values: A `Tensor` of type `string`.
    result_shape: A `Tensor` of type `int64`.
  """
  _ctx = _context._context
  if _ctx is None or not _ctx._eager_context.is_eager:
    _, _, _op = _op_def_lib._apply_op_helper(
        "CobineSparseSuccessor", parent_indices=parent_indices,
        parent_shape=parent_shape, child_indices=child_indices,
        child_values=child_values, child_shape=child_shape, name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = None
    _execute.record_gradient(
      "CobineSparseSuccessor", _inputs_flat, _attrs, _result, name)
    _result = _CobineSparseSuccessorOutput._make(_result)
    return _result

  else:
    try:
      _result = _pywrap_tensorflow.TFE_Py_FastPathExecute(
        _ctx._context_handle, _ctx._eager_context.device_name,
        "CobineSparseSuccessor", name, _ctx._post_execution_callbacks,
        parent_indices, parent_shape, child_indices, child_values,
        child_shape)
      _result = _CobineSparseSuccessorOutput._make(_result)
      return _result
    except _core._FallbackException:
      return cobine_sparse_successor_eager_fallback(
          parent_indices, parent_shape, child_indices, child_values,
          child_shape, name=name, ctx=_ctx)
    except _core._NotOkStatusException as e:
      if name is not None:
        message = e.message + " name: " + name
      else:
        message = e.message
      _six.raise_from(_core._status_to_exception(e.code, message), None)


def cobine_sparse_successor_eager_fallback(parent_indices, parent_shape, child_indices, child_values, child_shape, name=None, ctx=None):
  r"""This is the slowpath function for Eager mode.
  This is for function cobine_sparse_successor
  """
  _ctx = ctx if ctx else _context.context()
  parent_indices = _ops.convert_to_tensor(parent_indices, _dtypes.int64)
  parent_shape = _ops.convert_to_tensor(parent_shape, _dtypes.int64)
  child_indices = _ops.convert_to_tensor(child_indices, _dtypes.int64)
  child_values = _ops.convert_to_tensor(child_values, _dtypes.string)
  child_shape = _ops.convert_to_tensor(child_shape, _dtypes.int64)
  _inputs_flat = [parent_indices, parent_shape, child_indices, child_values, child_shape]
  _attrs = None
  _result = _execute.execute(b"CobineSparseSuccessor", 3, inputs=_inputs_flat,
                             attrs=_attrs, ctx=_ctx, name=name)
  _execute.record_gradient(
      "CobineSparseSuccessor", _inputs_flat, _attrs, _result, name)
  _result = _CobineSparseSuccessorOutput._make(_result)
  return _result

_ops.RegisterShape("CobineSparseSuccessor")(None)


_expand_char_ngrams_outputs = ["indices", "values", "shape"]
_ExpandCharNgramsOutput = _collections.namedtuple(
    "ExpandCharNgrams", _expand_char_ngrams_outputs)


@tf_export('expand_char_ngrams')
def expand_char_ngrams(source, minn, maxn, itself, name=None):
  r"""TODO: add doc.

  Args:
    source: A `Tensor` of type `string`.
    minn: An `int`.
    maxn: An `int`.
    itself: A `string` from: `"ASIS", "NEVER", "ALWAYS", "ALONE"`.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (indices, values, shape).

    indices: A `Tensor` of type `int64`.
    values: A `Tensor` of type `string`.
    shape: A `Tensor` of type `int64`.
  """
  _ctx = _context._context
  if _ctx is None or not _ctx._eager_context.is_eager:
    minn = _execute.make_int(minn, "minn")
    maxn = _execute.make_int(maxn, "maxn")
    itself = _execute.make_str(itself, "itself")
    _, _, _op = _op_def_lib._apply_op_helper(
        "ExpandCharNgrams", source=source, minn=minn, maxn=maxn,
        itself=itself, name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = ("minn", _op.get_attr("minn"), "maxn", _op.get_attr("maxn"),
              "itself", _op.get_attr("itself"))
    _execute.record_gradient(
      "ExpandCharNgrams", _inputs_flat, _attrs, _result, name)
    _result = _ExpandCharNgramsOutput._make(_result)
    return _result

  else:
    try:
      _result = _pywrap_tensorflow.TFE_Py_FastPathExecute(
        _ctx._context_handle, _ctx._eager_context.device_name,
        "ExpandCharNgrams", name, _ctx._post_execution_callbacks, source,
        "minn", minn, "maxn", maxn, "itself", itself)
      _result = _ExpandCharNgramsOutput._make(_result)
      return _result
    except _core._FallbackException:
      return expand_char_ngrams_eager_fallback(
          source, minn=minn, maxn=maxn, itself=itself, name=name, ctx=_ctx)
    except _core._NotOkStatusException as e:
      if name is not None:
        message = e.message + " name: " + name
      else:
        message = e.message
      _six.raise_from(_core._status_to_exception(e.code, message), None)


def expand_char_ngrams_eager_fallback(source, minn, maxn, itself, name=None, ctx=None):
  r"""This is the slowpath function for Eager mode.
  This is for function expand_char_ngrams
  """
  _ctx = ctx if ctx else _context.context()
  minn = _execute.make_int(minn, "minn")
  maxn = _execute.make_int(maxn, "maxn")
  itself = _execute.make_str(itself, "itself")
  source = _ops.convert_to_tensor(source, _dtypes.string)
  _inputs_flat = [source]
  _attrs = ("minn", minn, "maxn", maxn, "itself", itself)
  _result = _execute.execute(b"ExpandCharNgrams", 3, inputs=_inputs_flat,
                             attrs=_attrs, ctx=_ctx, name=name)
  _execute.record_gradient(
      "ExpandCharNgrams", _inputs_flat, _attrs, _result, name)
  _result = _ExpandCharNgramsOutput._make(_result)
  return _result

_ops.RegisterShape("ExpandCharNgrams")(None)


_expand_split_chars_outputs = ["indices", "values", "shape"]
_ExpandSplitCharsOutput = _collections.namedtuple(
    "ExpandSplitChars", _expand_split_chars_outputs)


@tf_export('expand_split_chars')
def expand_split_chars(source, name=None):
  r"""TODO: add doc.

  Args:
    source: A `Tensor` of type `string`.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (indices, values, shape).

    indices: A `Tensor` of type `int64`.
    values: A `Tensor` of type `string`.
    shape: A `Tensor` of type `int64`.
  """
  _ctx = _context._context
  if _ctx is None or not _ctx._eager_context.is_eager:
    _, _, _op = _op_def_lib._apply_op_helper(
        "ExpandSplitChars", source=source, name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = None
    _execute.record_gradient(
      "ExpandSplitChars", _inputs_flat, _attrs, _result, name)
    _result = _ExpandSplitCharsOutput._make(_result)
    return _result

  else:
    try:
      _result = _pywrap_tensorflow.TFE_Py_FastPathExecute(
        _ctx._context_handle, _ctx._eager_context.device_name,
        "ExpandSplitChars", name, _ctx._post_execution_callbacks, source)
      _result = _ExpandSplitCharsOutput._make(_result)
      return _result
    except _core._FallbackException:
      return expand_split_chars_eager_fallback(
          source, name=name, ctx=_ctx)
    except _core._NotOkStatusException as e:
      if name is not None:
        message = e.message + " name: " + name
      else:
        message = e.message
      _six.raise_from(_core._status_to_exception(e.code, message), None)


def expand_split_chars_eager_fallback(source, name=None, ctx=None):
  r"""This is the slowpath function for Eager mode.
  This is for function expand_split_chars
  """
  _ctx = ctx if ctx else _context.context()
  source = _ops.convert_to_tensor(source, _dtypes.string)
  _inputs_flat = [source]
  _attrs = None
  _result = _execute.execute(b"ExpandSplitChars", 3, inputs=_inputs_flat,
                             attrs=_attrs, ctx=_ctx, name=name)
  _execute.record_gradient(
      "ExpandSplitChars", _inputs_flat, _attrs, _result, name)
  _result = _ExpandSplitCharsOutput._make(_result)
  return _result

_ops.RegisterShape("ExpandSplitChars")(None)


_expand_split_words_outputs = ["indices", "values", "shape"]
_ExpandSplitWordsOutput = _collections.namedtuple(
    "ExpandSplitWords", _expand_split_words_outputs)


@tf_export('expand_split_words')
def expand_split_words(source, extended=False, name=None):
  r"""TODO: add doc.

  Args:
    source: A `Tensor` of type `string`.
    extended: An optional `bool`. Defaults to `False`.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (indices, values, shape).

    indices: A `Tensor` of type `int64`.
    values: A `Tensor` of type `string`.
    shape: A `Tensor` of type `int64`.
  """
  _ctx = _context._context
  if _ctx is None or not _ctx._eager_context.is_eager:
    if extended is None:
      extended = False
    extended = _execute.make_bool(extended, "extended")
    _, _, _op = _op_def_lib._apply_op_helper(
        "ExpandSplitWords", source=source, extended=extended, name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = ("extended", _op.get_attr("extended"))
    _execute.record_gradient(
      "ExpandSplitWords", _inputs_flat, _attrs, _result, name)
    _result = _ExpandSplitWordsOutput._make(_result)
    return _result

  else:
    try:
      _result = _pywrap_tensorflow.TFE_Py_FastPathExecute(
        _ctx._context_handle, _ctx._eager_context.device_name,
        "ExpandSplitWords", name, _ctx._post_execution_callbacks, source,
        "extended", extended)
      _result = _ExpandSplitWordsOutput._make(_result)
      return _result
    except _core._FallbackException:
      return expand_split_words_eager_fallback(
          source, extended=extended, name=name, ctx=_ctx)
    except _core._NotOkStatusException as e:
      if name is not None:
        message = e.message + " name: " + name
      else:
        message = e.message
      _six.raise_from(_core._status_to_exception(e.code, message), None)


def expand_split_words_eager_fallback(source, extended=False, name=None, ctx=None):
  r"""This is the slowpath function for Eager mode.
  This is for function expand_split_words
  """
  _ctx = ctx if ctx else _context.context()
  if extended is None:
    extended = False
  extended = _execute.make_bool(extended, "extended")
  source = _ops.convert_to_tensor(source, _dtypes.string)
  _inputs_flat = [source]
  _attrs = ("extended", extended)
  _result = _execute.execute(b"ExpandSplitWords", 3, inputs=_inputs_flat,
                             attrs=_attrs, ctx=_ctx, name=name)
  _execute.record_gradient(
      "ExpandSplitWords", _inputs_flat, _attrs, _result, name)
  _result = _ExpandSplitWordsOutput._make(_result)
  return _result

_ops.RegisterShape("ExpandSplitWords")(None)


@tf_export('transform_lower_case')
def transform_lower_case(source, name=None):
  r"""TODO: add doc.

  Args:
    source: A `Tensor` of type `string`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `string`.
  """
  _ctx = _context._context
  if _ctx is None or not _ctx._eager_context.is_eager:
    _, _, _op = _op_def_lib._apply_op_helper(
        "TransformLowerCase", source=source, name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = None
    _execute.record_gradient(
      "TransformLowerCase", _inputs_flat, _attrs, _result, name)
    _result, = _result
    return _result

  else:
    try:
      _result = _pywrap_tensorflow.TFE_Py_FastPathExecute(
        _ctx._context_handle, _ctx._eager_context.device_name,
        "TransformLowerCase", name, _ctx._post_execution_callbacks, source)
      return _result
    except _core._FallbackException:
      return transform_lower_case_eager_fallback(
          source, name=name, ctx=_ctx)
    except _core._NotOkStatusException as e:
      if name is not None:
        message = e.message + " name: " + name
      else:
        message = e.message
      _six.raise_from(_core._status_to_exception(e.code, message), None)


def transform_lower_case_eager_fallback(source, name=None, ctx=None):
  r"""This is the slowpath function for Eager mode.
  This is for function transform_lower_case
  """
  _ctx = ctx if ctx else _context.context()
  source = _ops.convert_to_tensor(source, _dtypes.string)
  _inputs_flat = [source]
  _attrs = None
  _result = _execute.execute(b"TransformLowerCase", 1, inputs=_inputs_flat,
                             attrs=_attrs, ctx=_ctx, name=name)
  _execute.record_gradient(
      "TransformLowerCase", _inputs_flat, _attrs, _result, name)
  _result, = _result
  return _result

_ops.RegisterShape("TransformLowerCase")(None)


@tf_export('transform_normalize_unicode')
def transform_normalize_unicode(source, form, name=None):
  r"""TODO: add doc.

  Args:
    source: A `Tensor` of type `string`.
    form: A `string` from: `"NFC", "NFD", "NFKC", "NFKD"`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `string`.
  """
  _ctx = _context._context
  if _ctx is None or not _ctx._eager_context.is_eager:
    form = _execute.make_str(form, "form")
    _, _, _op = _op_def_lib._apply_op_helper(
        "TransformNormalizeUnicode", source=source, form=form, name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = ("form", _op.get_attr("form"))
    _execute.record_gradient(
      "TransformNormalizeUnicode", _inputs_flat, _attrs, _result, name)
    _result, = _result
    return _result

  else:
    try:
      _result = _pywrap_tensorflow.TFE_Py_FastPathExecute(
        _ctx._context_handle, _ctx._eager_context.device_name,
        "TransformNormalizeUnicode", name, _ctx._post_execution_callbacks,
        source, "form", form)
      return _result
    except _core._FallbackException:
      return transform_normalize_unicode_eager_fallback(
          source, form=form, name=name, ctx=_ctx)
    except _core._NotOkStatusException as e:
      if name is not None:
        message = e.message + " name: " + name
      else:
        message = e.message
      _six.raise_from(_core._status_to_exception(e.code, message), None)


def transform_normalize_unicode_eager_fallback(source, form, name=None, ctx=None):
  r"""This is the slowpath function for Eager mode.
  This is for function transform_normalize_unicode
  """
  _ctx = ctx if ctx else _context.context()
  form = _execute.make_str(form, "form")
  source = _ops.convert_to_tensor(source, _dtypes.string)
  _inputs_flat = [source]
  _attrs = ("form", form)
  _result = _execute.execute(b"TransformNormalizeUnicode", 1,
                             inputs=_inputs_flat, attrs=_attrs, ctx=_ctx,
                             name=name)
  _execute.record_gradient(
      "TransformNormalizeUnicode", _inputs_flat, _attrs, _result, name)
  _result, = _result
  return _result

_ops.RegisterShape("TransformNormalizeUnicode")(None)


@tf_export('transform_regex_replace')
def transform_regex_replace(source, pattern, rewrite, name=None):
  r"""TODO: add doc.

  Args:
    source: A `Tensor` of type `string`.
    pattern: A list of `strings` that has length `>= 1`.
    rewrite: A list of `strings` that has length `>= 1`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `string`.
  """
  _ctx = _context._context
  if _ctx is None or not _ctx._eager_context.is_eager:
    if not isinstance(pattern, (list, tuple)):
      raise TypeError(
          "Expected list for 'pattern' argument to "
          "'transform_regex_replace' Op, not %r." % pattern)
    pattern = [_execute.make_str(_s, "pattern") for _s in pattern]
    if not isinstance(rewrite, (list, tuple)):
      raise TypeError(
          "Expected list for 'rewrite' argument to "
          "'transform_regex_replace' Op, not %r." % rewrite)
    rewrite = [_execute.make_str(_s, "rewrite") for _s in rewrite]
    _, _, _op = _op_def_lib._apply_op_helper(
        "TransformRegexReplace", source=source, pattern=pattern,
        rewrite=rewrite, name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = ("pattern", _op.get_attr("pattern"), "rewrite",
              _op.get_attr("rewrite"))
    _execute.record_gradient(
      "TransformRegexReplace", _inputs_flat, _attrs, _result, name)
    _result, = _result
    return _result

  else:
    try:
      _result = _pywrap_tensorflow.TFE_Py_FastPathExecute(
        _ctx._context_handle, _ctx._eager_context.device_name,
        "TransformRegexReplace", name, _ctx._post_execution_callbacks, source,
        "pattern", pattern, "rewrite", rewrite)
      return _result
    except _core._FallbackException:
      return transform_regex_replace_eager_fallback(
          source, pattern=pattern, rewrite=rewrite, name=name, ctx=_ctx)
    except _core._NotOkStatusException as e:
      if name is not None:
        message = e.message + " name: " + name
      else:
        message = e.message
      _six.raise_from(_core._status_to_exception(e.code, message), None)


def transform_regex_replace_eager_fallback(source, pattern, rewrite, name=None, ctx=None):
  r"""This is the slowpath function for Eager mode.
  This is for function transform_regex_replace
  """
  _ctx = ctx if ctx else _context.context()
  if not isinstance(pattern, (list, tuple)):
    raise TypeError(
        "Expected list for 'pattern' argument to "
        "'transform_regex_replace' Op, not %r." % pattern)
  pattern = [_execute.make_str(_s, "pattern") for _s in pattern]
  if not isinstance(rewrite, (list, tuple)):
    raise TypeError(
        "Expected list for 'rewrite' argument to "
        "'transform_regex_replace' Op, not %r." % rewrite)
  rewrite = [_execute.make_str(_s, "rewrite") for _s in rewrite]
  source = _ops.convert_to_tensor(source, _dtypes.string)
  _inputs_flat = [source]
  _attrs = ("pattern", pattern, "rewrite", rewrite)
  _result = _execute.execute(b"TransformRegexReplace", 1, inputs=_inputs_flat,
                             attrs=_attrs, ctx=_ctx, name=name)
  _execute.record_gradient(
      "TransformRegexReplace", _inputs_flat, _attrs, _result, name)
  _result, = _result
  return _result

_ops.RegisterShape("TransformRegexReplace")(None)


@tf_export('transform_string_replace')
def transform_string_replace(source, needle, haystack, name=None):
  r"""TODO: add doc.

  Args:
    source: A `Tensor` of type `string`.
    needle: A list of `strings` that has length `>= 1`.
    haystack: A list of `strings` that has length `>= 1`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `string`.
  """
  _ctx = _context._context
  if _ctx is None or not _ctx._eager_context.is_eager:
    if not isinstance(needle, (list, tuple)):
      raise TypeError(
          "Expected list for 'needle' argument to "
          "'transform_string_replace' Op, not %r." % needle)
    needle = [_execute.make_str(_s, "needle") for _s in needle]
    if not isinstance(haystack, (list, tuple)):
      raise TypeError(
          "Expected list for 'haystack' argument to "
          "'transform_string_replace' Op, not %r." % haystack)
    haystack = [_execute.make_str(_s, "haystack") for _s in haystack]
    _, _, _op = _op_def_lib._apply_op_helper(
        "TransformStringReplace", source=source, needle=needle,
        haystack=haystack, name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = ("needle", _op.get_attr("needle"), "haystack",
              _op.get_attr("haystack"))
    _execute.record_gradient(
      "TransformStringReplace", _inputs_flat, _attrs, _result, name)
    _result, = _result
    return _result

  else:
    try:
      _result = _pywrap_tensorflow.TFE_Py_FastPathExecute(
        _ctx._context_handle, _ctx._eager_context.device_name,
        "TransformStringReplace", name, _ctx._post_execution_callbacks,
        source, "needle", needle, "haystack", haystack)
      return _result
    except _core._FallbackException:
      return transform_string_replace_eager_fallback(
          source, needle=needle, haystack=haystack, name=name, ctx=_ctx)
    except _core._NotOkStatusException as e:
      if name is not None:
        message = e.message + " name: " + name
      else:
        message = e.message
      _six.raise_from(_core._status_to_exception(e.code, message), None)


def transform_string_replace_eager_fallback(source, needle, haystack, name=None, ctx=None):
  r"""This is the slowpath function for Eager mode.
  This is for function transform_string_replace
  """
  _ctx = ctx if ctx else _context.context()
  if not isinstance(needle, (list, tuple)):
    raise TypeError(
        "Expected list for 'needle' argument to "
        "'transform_string_replace' Op, not %r." % needle)
  needle = [_execute.make_str(_s, "needle") for _s in needle]
  if not isinstance(haystack, (list, tuple)):
    raise TypeError(
        "Expected list for 'haystack' argument to "
        "'transform_string_replace' Op, not %r." % haystack)
  haystack = [_execute.make_str(_s, "haystack") for _s in haystack]
  source = _ops.convert_to_tensor(source, _dtypes.string)
  _inputs_flat = [source]
  _attrs = ("needle", needle, "haystack", haystack)
  _result = _execute.execute(b"TransformStringReplace", 1,
                             inputs=_inputs_flat, attrs=_attrs, ctx=_ctx,
                             name=name)
  _execute.record_gradient(
      "TransformStringReplace", _inputs_flat, _attrs, _result, name)
  _result, = _result
  return _result

_ops.RegisterShape("TransformStringReplace")(None)


@tf_export('transform_title_case')
def transform_title_case(source, name=None):
  r"""TODO: add doc.

  Args:
    source: A `Tensor` of type `string`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `string`.
  """
  _ctx = _context._context
  if _ctx is None or not _ctx._eager_context.is_eager:
    _, _, _op = _op_def_lib._apply_op_helper(
        "TransformTitleCase", source=source, name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = None
    _execute.record_gradient(
      "TransformTitleCase", _inputs_flat, _attrs, _result, name)
    _result, = _result
    return _result

  else:
    try:
      _result = _pywrap_tensorflow.TFE_Py_FastPathExecute(
        _ctx._context_handle, _ctx._eager_context.device_name,
        "TransformTitleCase", name, _ctx._post_execution_callbacks, source)
      return _result
    except _core._FallbackException:
      return transform_title_case_eager_fallback(
          source, name=name, ctx=_ctx)
    except _core._NotOkStatusException as e:
      if name is not None:
        message = e.message + " name: " + name
      else:
        message = e.message
      _six.raise_from(_core._status_to_exception(e.code, message), None)


def transform_title_case_eager_fallback(source, name=None, ctx=None):
  r"""This is the slowpath function for Eager mode.
  This is for function transform_title_case
  """
  _ctx = ctx if ctx else _context.context()
  source = _ops.convert_to_tensor(source, _dtypes.string)
  _inputs_flat = [source]
  _attrs = None
  _result = _execute.execute(b"TransformTitleCase", 1, inputs=_inputs_flat,
                             attrs=_attrs, ctx=_ctx, name=name)
  _execute.record_gradient(
      "TransformTitleCase", _inputs_flat, _attrs, _result, name)
  _result, = _result
  return _result

_ops.RegisterShape("TransformTitleCase")(None)


@tf_export('transform_upper_case')
def transform_upper_case(source, name=None):
  r"""TODO: add doc.

  Args:
    source: A `Tensor` of type `string`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `string`.
  """
  _ctx = _context._context
  if _ctx is None or not _ctx._eager_context.is_eager:
    _, _, _op = _op_def_lib._apply_op_helper(
        "TransformUpperCase", source=source, name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = None
    _execute.record_gradient(
      "TransformUpperCase", _inputs_flat, _attrs, _result, name)
    _result, = _result
    return _result

  else:
    try:
      _result = _pywrap_tensorflow.TFE_Py_FastPathExecute(
        _ctx._context_handle, _ctx._eager_context.device_name,
        "TransformUpperCase", name, _ctx._post_execution_callbacks, source)
      return _result
    except _core._FallbackException:
      return transform_upper_case_eager_fallback(
          source, name=name, ctx=_ctx)
    except _core._NotOkStatusException as e:
      if name is not None:
        message = e.message + " name: " + name
      else:
        message = e.message
      _six.raise_from(_core._status_to_exception(e.code, message), None)


def transform_upper_case_eager_fallback(source, name=None, ctx=None):
  r"""This is the slowpath function for Eager mode.
  This is for function transform_upper_case
  """
  _ctx = ctx if ctx else _context.context()
  source = _ops.convert_to_tensor(source, _dtypes.string)
  _inputs_flat = [source]
  _attrs = None
  _result = _execute.execute(b"TransformUpperCase", 1, inputs=_inputs_flat,
                             attrs=_attrs, ctx=_ctx, name=name)
  _execute.record_gradient(
      "TransformUpperCase", _inputs_flat, _attrs, _result, name)
  _result, = _result
  return _result

_ops.RegisterShape("TransformUpperCase")(None)


@tf_export('transform_wrap_with')
def transform_wrap_with(source, left, right, name=None):
  r"""TODO: add doc.

  Args:
    source: A `Tensor` of type `string`.
    left: A `string`.
    right: A `string`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `string`.
  """
  _ctx = _context._context
  if _ctx is None or not _ctx._eager_context.is_eager:
    left = _execute.make_str(left, "left")
    right = _execute.make_str(right, "right")
    _, _, _op = _op_def_lib._apply_op_helper(
        "TransformWrapWith", source=source, left=left, right=right, name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = ("left", _op.get_attr("left"), "right", _op.get_attr("right"))
    _execute.record_gradient(
      "TransformWrapWith", _inputs_flat, _attrs, _result, name)
    _result, = _result
    return _result

  else:
    try:
      _result = _pywrap_tensorflow.TFE_Py_FastPathExecute(
        _ctx._context_handle, _ctx._eager_context.device_name,
        "TransformWrapWith", name, _ctx._post_execution_callbacks, source,
        "left", left, "right", right)
      return _result
    except _core._FallbackException:
      return transform_wrap_with_eager_fallback(
          source, left=left, right=right, name=name, ctx=_ctx)
    except _core._NotOkStatusException as e:
      if name is not None:
        message = e.message + " name: " + name
      else:
        message = e.message
      _six.raise_from(_core._status_to_exception(e.code, message), None)


def transform_wrap_with_eager_fallback(source, left, right, name=None, ctx=None):
  r"""This is the slowpath function for Eager mode.
  This is for function transform_wrap_with
  """
  _ctx = ctx if ctx else _context.context()
  left = _execute.make_str(left, "left")
  right = _execute.make_str(right, "right")
  source = _ops.convert_to_tensor(source, _dtypes.string)
  _inputs_flat = [source]
  _attrs = ("left", left, "right", right)
  _result = _execute.execute(b"TransformWrapWith", 1, inputs=_inputs_flat,
                             attrs=_attrs, ctx=_ctx, name=name)
  _execute.record_gradient(
      "TransformWrapWith", _inputs_flat, _attrs, _result, name)
  _result, = _result
  return _result

_ops.RegisterShape("TransformWrapWith")(None)


@tf_export('transform_zero_digits')
def transform_zero_digits(source, name=None):
  r"""TODO: add doc.

  Args:
    source: A `Tensor` of type `string`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `string`.
  """
  _ctx = _context._context
  if _ctx is None or not _ctx._eager_context.is_eager:
    _, _, _op = _op_def_lib._apply_op_helper(
        "TransformZeroDigits", source=source, name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = None
    _execute.record_gradient(
      "TransformZeroDigits", _inputs_flat, _attrs, _result, name)
    _result, = _result
    return _result

  else:
    try:
      _result = _pywrap_tensorflow.TFE_Py_FastPathExecute(
        _ctx._context_handle, _ctx._eager_context.device_name,
        "TransformZeroDigits", name, _ctx._post_execution_callbacks, source)
      return _result
    except _core._FallbackException:
      return transform_zero_digits_eager_fallback(
          source, name=name, ctx=_ctx)
    except _core._NotOkStatusException as e:
      if name is not None:
        message = e.message + " name: " + name
      else:
        message = e.message
      _six.raise_from(_core._status_to_exception(e.code, message), None)


def transform_zero_digits_eager_fallback(source, name=None, ctx=None):
  r"""This is the slowpath function for Eager mode.
  This is for function transform_zero_digits
  """
  _ctx = ctx if ctx else _context.context()
  source = _ops.convert_to_tensor(source, _dtypes.string)
  _inputs_flat = [source]
  _attrs = None
  _result = _execute.execute(b"TransformZeroDigits", 1, inputs=_inputs_flat,
                             attrs=_attrs, ctx=_ctx, name=name)
  _execute.record_gradient(
      "TransformZeroDigits", _inputs_flat, _attrs, _result, name)
  _result, = _result
  return _result

_ops.RegisterShape("TransformZeroDigits")(None)

def _InitOpDefLibrary(op_list_proto_bytes):
  op_list = _op_def_pb2.OpList()
  op_list.ParseFromString(op_list_proto_bytes)
  _op_def_registry.register_op_list(op_list)
  op_def_lib = _op_def_library.OpDefLibrary()
  op_def_lib.add_op_list(op_list)
  return op_def_lib
# op {
#   name: "CobineSparseSuccessor"
#   input_arg {
#     name: "parent_indices"
#     type: DT_INT64
#   }
#   input_arg {
#     name: "parent_shape"
#     type: DT_INT64
#   }
#   input_arg {
#     name: "child_indices"
#     type: DT_INT64
#   }
#   input_arg {
#     name: "child_values"
#     type: DT_STRING
#   }
#   input_arg {
#     name: "child_shape"
#     type: DT_INT64
#   }
#   output_arg {
#     name: "result_indices"
#     type: DT_INT64
#   }
#   output_arg {
#     name: "result_values"
#     type: DT_STRING
#   }
#   output_arg {
#     name: "result_shape"
#     type: DT_INT64
#   }
#   is_stateful: true
# }
# op {
#   name: "ExpandCharNgrams"
#   input_arg {
#     name: "source"
#     type: DT_STRING
#   }
#   output_arg {
#     name: "indices"
#     type: DT_INT64
#   }
#   output_arg {
#     name: "values"
#     type: DT_STRING
#   }
#   output_arg {
#     name: "shape"
#     type: DT_INT64
#   }
#   attr {
#     name: "minn"
#     type: "int"
#   }
#   attr {
#     name: "maxn"
#     type: "int"
#   }
#   attr {
#     name: "itself"
#     type: "string"
#     allowed_values {
#       list {
#         s: "ASIS"
#         s: "NEVER"
#         s: "ALWAYS"
#         s: "ALONE"
#       }
#     }
#   }
#   is_stateful: true
# }
# op {
#   name: "ExpandSplitChars"
#   input_arg {
#     name: "source"
#     type: DT_STRING
#   }
#   output_arg {
#     name: "indices"
#     type: DT_INT64
#   }
#   output_arg {
#     name: "values"
#     type: DT_STRING
#   }
#   output_arg {
#     name: "shape"
#     type: DT_INT64
#   }
#   is_stateful: true
# }
# op {
#   name: "ExpandSplitWords"
#   input_arg {
#     name: "source"
#     type: DT_STRING
#   }
#   output_arg {
#     name: "indices"
#     type: DT_INT64
#   }
#   output_arg {
#     name: "values"
#     type: DT_STRING
#   }
#   output_arg {
#     name: "shape"
#     type: DT_INT64
#   }
#   attr {
#     name: "extended"
#     type: "bool"
#     default_value {
#       b: false
#     }
#   }
#   is_stateful: true
# }
# op {
#   name: "TransformLowerCase"
#   input_arg {
#     name: "source"
#     type: DT_STRING
#   }
#   output_arg {
#     name: "result"
#     type: DT_STRING
#   }
#   is_stateful: true
# }
# op {
#   name: "TransformNormalizeUnicode"
#   input_arg {
#     name: "source"
#     type: DT_STRING
#   }
#   output_arg {
#     name: "result"
#     type: DT_STRING
#   }
#   attr {
#     name: "form"
#     type: "string"
#     allowed_values {
#       list {
#         s: "NFC"
#         s: "NFD"
#         s: "NFKC"
#         s: "NFKD"
#       }
#     }
#   }
#   is_stateful: true
# }
# op {
#   name: "TransformRegexReplace"
#   input_arg {
#     name: "source"
#     type: DT_STRING
#   }
#   output_arg {
#     name: "result"
#     type: DT_STRING
#   }
#   attr {
#     name: "pattern"
#     type: "list(string)"
#     has_minimum: true
#     minimum: 1
#   }
#   attr {
#     name: "rewrite"
#     type: "list(string)"
#     has_minimum: true
#     minimum: 1
#   }
#   is_stateful: true
# }
# op {
#   name: "TransformStringReplace"
#   input_arg {
#     name: "source"
#     type: DT_STRING
#   }
#   output_arg {
#     name: "result"
#     type: DT_STRING
#   }
#   attr {
#     name: "needle"
#     type: "list(string)"
#     has_minimum: true
#     minimum: 1
#   }
#   attr {
#     name: "haystack"
#     type: "list(string)"
#     has_minimum: true
#     minimum: 1
#   }
#   is_stateful: true
# }
# op {
#   name: "TransformTitleCase"
#   input_arg {
#     name: "source"
#     type: DT_STRING
#   }
#   output_arg {
#     name: "result"
#     type: DT_STRING
#   }
#   is_stateful: true
# }
# op {
#   name: "TransformUpperCase"
#   input_arg {
#     name: "source"
#     type: DT_STRING
#   }
#   output_arg {
#     name: "result"
#     type: DT_STRING
#   }
#   is_stateful: true
# }
# op {
#   name: "TransformWrapWith"
#   input_arg {
#     name: "source"
#     type: DT_STRING
#   }
#   output_arg {
#     name: "result"
#     type: DT_STRING
#   }
#   attr {
#     name: "left"
#     type: "string"
#   }
#   attr {
#     name: "right"
#     type: "string"
#   }
#   is_stateful: true
# }
# op {
#   name: "TransformZeroDigits"
#   input_arg {
#     name: "source"
#     type: DT_STRING
#   }
#   output_arg {
#     name: "result"
#     type: DT_STRING
#   }
#   is_stateful: true
# }
_op_def_lib = _InitOpDefLibrary(b"\n\257\001\n\025CobineSparseSuccessor\022\022\n\016parent_indices\030\t\022\020\n\014parent_shape\030\t\022\021\n\rchild_indices\030\t\022\020\n\014child_values\030\007\022\017\n\013child_shape\030\t\032\022\n\016result_indices\030\t\032\021\n\rresult_values\030\007\032\020\n\014result_shape\030\t\210\001\001\n\221\001\n\020ExpandCharNgrams\022\n\n\006source\030\007\032\013\n\007indices\030\t\032\n\n\006values\030\007\032\t\n\005shape\030\t\"\013\n\004minn\022\003int\"\013\n\004maxn\022\003int\"0\n\006itself\022\006string:\036\n\034\022\004ASIS\022\005NEVER\022\006ALWAYS\022\005ALONE\210\001\001\nE\n\020ExpandSplitChars\022\n\n\006source\030\007\032\013\n\007indices\030\t\032\n\n\006values\030\007\032\t\n\005shape\030\t\210\001\001\n[\n\020ExpandSplitWords\022\n\n\006source\030\007\032\013\n\007indices\030\t\032\n\n\006values\030\007\032\t\n\005shape\030\t\"\024\n\010extended\022\004bool\032\002(\000\210\001\001\n/\n\022TransformLowerCase\022\n\n\006source\030\007\032\n\n\006result\030\007\210\001\001\n`\n\031TransformNormalizeUnicode\022\n\n\006source\030\007\032\n\n\006result\030\007\"(\n\004form\022\006string:\030\n\026\022\003NFC\022\003NFD\022\004NFKC\022\004NFKD\210\001\001\nl\n\025TransformRegexReplace\022\n\n\006source\030\007\032\n\n\006result\030\007\"\033\n\007pattern\022\014list(string)(\0010\001\"\033\n\007rewrite\022\014list(string)(\0010\001\210\001\001\nm\n\026TransformStringReplace\022\n\n\006source\030\007\032\n\n\006result\030\007\"\032\n\006needle\022\014list(string)(\0010\001\"\034\n\010haystack\022\014list(string)(\0010\001\210\001\001\n/\n\022TransformTitleCase\022\n\n\006source\030\007\032\n\n\006result\030\007\210\001\001\n/\n\022TransformUpperCase\022\n\n\006source\030\007\032\n\n\006result\030\007\210\001\001\nO\n\021TransformWrapWith\022\n\n\006source\030\007\032\n\n\006result\030\007\"\016\n\004left\022\006string\"\017\n\005right\022\006string\210\001\001\n0\n\023TransformZeroDigits\022\n\n\006source\030\007\032\n\n\006result\030\007\210\001\001")
