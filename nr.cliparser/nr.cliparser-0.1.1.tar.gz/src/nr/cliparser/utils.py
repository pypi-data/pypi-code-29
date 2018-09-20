
import os
import sys

if sys.version_info[0] == 3:
  from io import StringIO
else:
  from io import BytesIO as StringIO


def terminal_size(default=(80, 30)):
  """
  Determines the size of the terminal. If the size can not be obtained,
  the specified *default* size is returned.
  """

  if os.name == 'nt':
    # http://code.activestate.com/recipes/440694-determine-size-of-console-window-on-windows/
    import ctypes, struct
    h = ctypes.windll.kernel32.GetStdHandle(-12)
    csbi = ctypes.create_string_buffer(22)
    res = ctypes.windll.kernel32.GetConsoleScreenBufferInfo(h, csbi)
    if res:
      (bufx, bufy, curx, cury, wattr, left, top, right,
       bottom, maxx, maxy) = struct.unpack('hhhhHhhhhhh', csbi.raw)
      sizex = right - left
      sizey = bottom - top
      return (sizex, sizey)
    else:
      return default
  else:
    # http://stackoverflow.com/a/3010495/791713
    import fcntl, termios, struct
    try:
      data = fcntl.ioctl(0, termios.TIOCGWINSZ, struct.pack('HHHH', 0, 0, 0, 0))
    except OSError as exc:
      # craftr-build/craftr#169 -- On OSX on Travis CI the call fails, probably
      # because the process is not attached to a TTY.
      if exc.errno in (errno.ENODEV, errno.ENOTTY):
        return default
      raise
    h, w, hp, wp = struct.unpack('HHHH', data)
    return w, h
