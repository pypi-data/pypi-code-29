"""
ZJLANG number utils function

author: tim.tang
date: 2018-09-01
"""


def divmod(val1, val2):
  """
  Absulte division and moduler.

  different from builtin divmod function
  """
  assert val2 > 0

  div = abs(val1) // abs(val2)
  mod = abs(val1) % abs(val2)
  if val1 < 0:
    div, mod = -div, -mod
  return div, mod
