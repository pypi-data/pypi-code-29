# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Public API for performing evaluations using the EvalSavedModel."""

from __future__ import absolute_import
from __future__ import division

from __future__ import print_function



import apache_beam as beam

from tensorflow_model_analysis import constants
from tensorflow_model_analysis import types
from tensorflow_model_analysis.eval_saved_model import dofn
from tensorflow_transform.beam import shared
from tensorflow_model_analysis.types_compat import Any, Callable, Dict, Generator, List, Optional, Tuple

MetricVariablesType = List[Any]  # pylint: disable=invalid-name

# For use in Beam type annotations, because Beam's support for Python types
# in Beam type annotations is not complete.
_BeamSliceKeyType = beam.typehints.Tuple[  # pylint: disable=invalid-name
    beam.typehints.Tuple[bytes, beam.typehints.Union[bytes, int, float]], Ellipsis]

_METRICS_NAMESPACE = 'tensorflow_model_analysis'


@beam.typehints.with_input_types(beam.typehints.List[types.ExampleAndExtracts])
@beam.typehints.with_output_types(beam.typehints.Any)
class _TFMAPredictionDoFn(dofn.EvalSavedModelDoFn):
  """A DoFn that loads the model and predicts."""

  def __init__(self, eval_saved_model_path,
               add_metrics_callbacks,
               shared_handle):
    super(_TFMAPredictionDoFn, self).__init__(
        eval_saved_model_path, add_metrics_callbacks, shared_handle)
    self._predict_batch_size = beam.metrics.Metrics.distribution(
        _METRICS_NAMESPACE, 'predict_batch_size')
    self._num_instances = beam.metrics.Metrics.counter(_METRICS_NAMESPACE,
                                                       'num_instances')

  def process(self, element
             ):
    batch_size = len(element)
    self._predict_batch_size.update(batch_size)
    self._num_instances.inc(batch_size)
    serialized_examples = [x.example for x in element]

    # Compute FeaturesPredictionsLabels for each serialized_example
    for example_and_extracts, fpl in zip(
        element, self._eval_saved_model.predict_list(serialized_examples)):

      # Make a a shallow copy, so we don't mutate the original.
      element_copy = (
          example_and_extracts.create_copy_with_shallow_copy_of_extracts())
      element_copy.extracts[constants.FEATURES_PREDICTIONS_LABELS_KEY] = fpl
      yield element_copy


@beam.ptransform_fn
@beam.typehints.with_input_types(beam.typehints.Any)
@beam.typehints.with_output_types(beam.typehints.Any)
def TFMAPredict(  # pylint: disable=invalid-name
    examples,
    eval_saved_model_path,
    add_metrics_callbacks,
    shared_handle,
    desired_batch_size = None):
  """A PTransform that adds predictions to ExamplesAndExtracts.

  Args:
    examples: PCollection of serialized examples to be fed to the model
    eval_saved_model_path: Path to the EvalSavedModle
    add_metrics_callbacks: Optional list of add_metrics_callbacks. See docstring
      for Evaluate in api/impl/evaluate.py for more details.
    shared_handle: Handle to a shared.Shared object for sharing the in-memory
      model within / between stages.
    desired_batch_size: Optional. Desired batch size for prediction.

  Returns:
    PCollection of ExamplesAndExtracts, where the extracts contains the
    features, predictions, labels retrieved.
  """
  batch_args = {}
  if desired_batch_size:
    batch_args = dict(
        min_batch_size=desired_batch_size, max_batch_size=desired_batch_size)

  # We don't actually need to add the add_metrics_callbacks to do Predict,
  # but because if we want to share the model between Predict and subsequent
  # stages (i.e. we use same shared handle for this and subsequent stages),
  # then if we don't add the metrics callbacks here, they won't be present
  # in the model in the later stages if we reuse the model from this stage.
  return (examples
          | 'Batch' >> beam.BatchElements(**batch_args)
          | 'Predict' >> beam.ParDo(
              _TFMAPredictionDoFn(
                  eval_saved_model_path=eval_saved_model_path,
                  add_metrics_callbacks=add_metrics_callbacks,
                  shared_handle=shared_handle)))
