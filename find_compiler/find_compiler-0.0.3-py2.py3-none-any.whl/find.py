import os
import glob

def find_match_in_path(name, path=None):
  path = path or os.environ.get('PATH')
  results = []
  for dir in path.split(os.pathsep):
    matches = glob.glob(os.path.join(dir, name))
    results.extend(matches)
  return results