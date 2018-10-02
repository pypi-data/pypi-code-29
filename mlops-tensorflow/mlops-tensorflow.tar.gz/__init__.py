
def run(version, **kwargs):
  if version == 'v1':
    import mlops.driver.tensorflow.v1.driver as v1
    v1.run(**kwargs)
  else:
    raise 'Unknown driver version: ' + version
    
