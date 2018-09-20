from mountainlab_pytools import mlproc as mlp
import h5py

class KBucketHdf5File:
    def __init__(self,kbucket_path):
      self._kbucket_path=kbucket_path
      if kbucket_path.startswith('kbucket://') or kbucket_path.startswith('sha1://'):
        path_or_url=mlp.locateFile(kbucket_path)
        if not path_or_url:
          raise Exception('Not found on kbucket: '+kbucket_path)
        if path_or_url.startswith('http://') or path_or_url.startswith('https://'):
          self._url=path_or_url
          self._path=None
        else:
          self._path=path_or_url
          self._url=None
      else:
        self._path=kbucket_path
        self._url=None
    def getAttributes(self):
      if self._path:
        with h5py.File(self._path,'r') as f:
          return dict(f.attrs)
      else:
        

    