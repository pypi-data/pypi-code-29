# Third-party module: attrs, lets us create data classes until Python 3.7 goes mainstream
try: import attr
except ImportError:
  print('This script requires the attrs module, install it with "sudo pip3 install attrs"')
  sys.exit(1)

@attr.s
class Track(object):
  filename: str        = attr.ib()
  properties: dict     = attr.ib()
  basename: str        = attr.ib(init=False)
  ext: str             = attr.ib(init=False)
  n: int               = attr.ib(init=False)
  actual_options: str  = attr.ib(default='')
  desired_options: str = attr.ib(default='')
  recode_result: bool  = attr.ib(default=False)

  def __attrs_post_init__(self):
    elements = self.filename.split('.')
    self.basename = elements[0]
    self.ext = elements[-1]

    # Populate the track number, if it exists (otherwise 0)
    track_num = ''.join([s for s in self.basename if s.isdigit()])
    self.n = 0 if not track_num else int(track_num)

  def apply_properties(self, properties):
    self.properties.update(properties)

  def properties_as_str(self, order):
    values = []
    for key_name in order:
      values.append(self.properties[key_name])
    return ', '.join(values)

