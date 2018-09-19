#!/usr/bin/env python
import json
import os

from orchestrate.runner.optimizer import SigOptOptimizer

def main():
  config_path = os.environ.get('ORCHESTRATE_CONFIG', '/etc/orchestrate/config.json')
  log_path = os.environ.get('ORCHESTRATE_LOG', '/var/orchestrate/log.json')
  suggestion_path = os.environ.get('ORCHESTRATE_SUGGESTION', '/var/orchestrate/suggestion.json')
  pod_name = os.environ.get('POD_NAME', 'unknown')
  experiment_id = os.environ['ORCHESTRATE_EXPERIMENT_ID']
  with open(config_path) as config_fp:
    config = json.load(config_fp)
  optimizer = SigOptOptimizer(
    config=config,
    log_path=log_path,
    suggestion_path=suggestion_path,
    pod_name=pod_name,
    experiment_id=experiment_id,
  )
  optimizer.optimization_loop()
