""" TensorFlow Driver Utils """

import attr
import tensorflow as tf

@attr.s
class Ops:
  model          = attr.ib()
  losses         = attr.ib()
  evaluate       = attr.ib()
  train          = attr.ib()
  train_input_fn = attr.ib()
  eval_input_fn  = attr.ib()
  train_hooks    = attr.ib(default=None)
  eval_hooks     = attr.ib(default=None)
  exporters      = attr.ib(default=None)

def load_ops(user_module, params):
  #TODO: check ops have required function
  th = user_module.train_hooks(params) if hasattr(user_module, 'train_hooks') else None
  eh = user_module.eval_hooks(params)  if hasattr(user_module, 'eval_hooks')  else None
  es = user_module.exporters(params)   if hasattr(user_module, 'exporters')   else None
  return Ops(
    model          = user_module.model,
    losses         = user_module.losses,
    evaluate       = user_module.evaluate,
    train          = user_module.train,
    train_input_fn = lambda: user_module.pipeline(True, params),
    train_hooks    = th,
    eval_input_fn  = lambda: user_module.pipeline(False, params),
    eval_hooks     = eh,
    exporters      = es,
  )

def load_config(ops, cfg):
  tf.logging.set_verbosity(cfg['log_verbosity'])
  rc = tf.estimator.RunConfig(
    tf_random_seed                = cfg['random_seed'],
    save_summary_steps            = cfg['save_summary_steps'],
    save_checkpoints_steps        = cfg['save_checkpoints_steps'],
    save_checkpoints_secs         = cfg['save_checkpoints_secs'],
    keep_checkpoint_max           = cfg['keep_checkpoint_max'],
    keep_checkpoint_every_n_hours = cfg['keep_checkpoint_every_n_hours'],
    log_step_count_steps          = cfg['log_step_count_steps'],
  )
  ts = tf.estimator.TrainSpec(
    input_fn  = ops.train_input_fn,
    max_steps = cfg['train_max_steps'],
  )
  es = tf.estimator.EvalSpec(
    input_fn         = ops.eval_input_fn,
    exporters        = ops.exporters,
    name             = cfg['eval_name'],
    steps            = cfg['eval_steps'],
    start_delay_secs = cfg['eval_start_delay_secs'],
    throttle_secs    = cfg['eval_throttle_secs'],
  )
  return rc, ts, es
