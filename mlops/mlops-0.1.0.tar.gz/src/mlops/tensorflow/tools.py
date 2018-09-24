# coding: utf-8

import importlib

import six
import tensorflow as tf

from mlops.tensorflow.estimator import Estimator

def get_estimator(job_name, module_name, run_config, params):
  model = importlib.import_module(name=module_name)
  rc = tf.estimator.RunConfig(**run_config)
  return Estimator(
    module=model, config=rc, params=params)

def get_pipeline_spec(estimator, module_name, train_spec, eval_spec, params):
  pipeline = importlib.import_module(name=module_name)
  ts = tf.estimator.TrainSpec(
    input_fn=lambda: pipeline.train_input(params),
    **train_spec)
  es = tf.estimator.EvalSpec(
    input_fn=lambda: pipeline.eval_input(params),
    exporters=pipeline.exporters(params),
    **eval_spec)
  return ts, es

def train(estimator, train_spec, eval_spec):
  tf.estimator.train_and_evaluate(estimator, train_spec, eval_spec)

def evaluate(estimator, eval_spec):
  metrics = estimator.evaluate(eval_spec.input_fn, steps=eval_spec.steps)
  print('###### metrics ' + '#' * 65)
  for name, value in sorted(six.iteritems(metrics)):
    print('{:<30}: {}'.format(name, value))

def main():
  import argparse
  from ruamel.yaml import YAML
  p = argparse.ArgumentParser()
  p.add_argument('action', choices=['train','eval'])
  p.add_argument('-c', '--config', default='config.yaml')
  p.add_argument('-L','--log-level', default='DEBUG')
  args = p.parse_args()
  config = YAML().load(open(args.config))
  tf.logging.set_verbosity(args.log_level)

  estimator = get_estimator(
    job_name    = config['job_name'],
    module_name = config['model'],
    run_config  = config['run_config'],
    params      = config['params'])
  
  train_spec, eval_spec = get_pipeline_spec(
    estimator,
    module_name = config['pipeline'],
    train_spec  = config['train_spec'],
    eval_spec   = config['eval_spec'],
    params      = config['params'])

  if args.action == 'train':
    train(estimator, train_spec, eval_spec)
  elif args.action == 'eval':
    evaluate(estimator, eval_spec)

if __name__ == '__main__':
  main()