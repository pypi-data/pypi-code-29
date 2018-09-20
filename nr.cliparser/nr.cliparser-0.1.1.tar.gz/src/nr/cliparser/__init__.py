
"""
Command-line parser for the Node.py command-line interface.
"""

from __future__ import print_function
from .formatter import TableFormatter
from .utils import StringIO

import collections
import os
import sys

__version__ = '0.1.1'
__author__ = 'Niklas Rosenstein <rosensteinniklas@gmail.com>'

DISALLOW = 'disallow'
ALLOW = 'allow'
REQUIRE = 'require'


class Dialect(object):

  def __init__(self, single='-', double='--', remainder='--',
               brace_open='[', brace_close=']'):
    self.single = single
    self.double = double
    self.remainder = remainder
    self.brace_open = brace_open
    self.brace_close = brace_close

  def is_flag(self, arg):
    if arg.startswith(self.single) or arg.startswith(self.double):
      return True
    return False


class Argument(object):

  def __init__(self, dest, matcher, consumer, multiple=False, help=None, metavar=None, default=NotImplemented):
    if default is NotImplemented:
      default = consumer.suggest_default()
    self.dest = dest
    self.matcher = matcher
    self.consumer = consumer
    self.multiple = multiple
    self.help = help
    self.metavar = metavar or dest
    self.default = default

  def __repr__(self):
    return 'Argument(dest={!r}, matcher={!r}, consumer={!r}, multiple={!r}, help={!r}, metavar={!r}, default={!r})'.format(
      self.dest, self.matcher, self.consumer, self.multiple, self.help, self.metavar, self.default)

  @property
  def positional(self):
    return isinstance(self.matcher, PositionalMatcher)

  def format_usage(self, dialect, detailed=True):
    if self.positional:
      return self.consumer.format_usage(dialect, self.metavar, detailed)
    return self.matcher.format_usage(dialect) + ' ' + self.consumer.format_usage(dialect, self.metavar, detailed)

  def format_help(self, dialect, formatter, depth):
    if isinstance(self.consumer, SubparserConsumer):
      formatter.put_row([])
    formatter.put_row([self.format_usage(dialect, False), self.help or ''], paddings=[depth*2])
    self.consumer.format_help(dialect, self.metavar, formatter, depth)


class Parser(object):

  def __init__(self, dialect=None, parent=None, prog=None):
    if prog is None:
      prog = os.path.splitext(os.path.basename(sys.argv[0]))[0]
    self.prog = prog
    self.dialect = dialect or Dialect()
    self.parent = parent
    self.arguments = collections.OrderedDict()

  def subparser(self, dest, matcher=None, consumer=None, nargs=None,
                braces=None, **kwargs):
    if consumer is None:
      if nargs is None:
        nargs = '...'
      if braces is None:
        braces = (nargs != '...')
      consumer = Consumer(nargs, braces)
    parser = Parser(self.dialect, self, prog='{} {}'.format(self.prog, dest))
    consumer = SubparserConsumer(parser, consumer)
    self.argument(dest, matcher, consumer, positional=False, **kwargs)
    return parser

  def argument(self, dest, matcher=None, consumer=None, nargs=1, braces=None,
               positional=None, **kwargs):
    if matcher is None:
      for prefix in (self.dialect.double, self.dialect.single):
        if dest.startswith(prefix):
          stripped_dest = dest[len(prefix):]
          break
      else:
        stripped_dest = dest
      if stripped_dest != dest:  # Had flags
        if positional is None:
          positional = False
        elif positional:
          raise ValueError('can not mix flag with positional=True')
      if positional is None:
        positional = True
      if positional:
        matcher = PositionalMatcher(dest)
      else:
        matcher = Matcher(dest, exact=True)
      dest = stripped_dest
    if consumer is None:
      if braces is None:
        braces = DISALLOW if nargs == '...' else ALLOW
      consumer = Consumer(nargs, braces)
    if dest in self.arguments:
      raise ValueError('{!r} already used'.format(dest))
    self.arguments[dest] = Argument(dest, matcher, consumer, **kwargs)

  def parse_known(self, argv=None):
    if argv is None:
      argv = sys.argv[1:]
    argv = list(argv)
    args = {}
    parsed = set()
    while argv:
      for arg in self.arguments.values():
        if arg.dest in parsed: continue
        if arg.matcher.match(argv[0], self.dialect):
          if not arg.positional:
            argv.pop(0)
          try:
            consumed_args = arg.consumer.consume(argv, self.dialect)
          except ArgumentBraceUnclosed:
            self.error('{}: argument brace not closed'.format(arg.matcher.format_usage(self.dialect)))
          except ArgumentCountMismatch as e:
            self.error('{}: unexpected number of arguments, expected {}, got {}'.format(
              arg.matcher.format_usage(self.dialect), e.expected, e.got))
          if arg.multiple:
            args.setdefault(arg.dest, []).append(consumed_args)
          else:
            args[arg.dest] = consumed_args
            parsed.add(arg.dest)
          break
      else:
        break
    for arg in self.arguments.values():
      args.setdefault(arg.dest, [] if arg.multiple else arg.default)
    return args, argv

  def parse(self, argv=None):
    args, argv = self.parse_known(argv)
    if argv:
      self.error('unparsed arguments:', argv)
    return args

  def error(self, *message, **kwargs):
    code = kwargs.pop('code', 1)
    if kwargs:
      raise TypeError('unexpected keyword argument {!r}'.format(list(kwargs.keys())[0]))
    self.print_usage(sys.stderr)
    print('error:', *message, file=sys.stderr)
    sys.exit(code)

  def format_usage(self):
    fp = StringIO()
    for arg in self.arguments.values():
      fp.write('{} '.format(arg.format_usage(self.dialect)))
    return fp.getvalue()

  def print_usage(self, fp):
    print('usage:', self.prog, self.format_usage(), file=fp)

  def format_help(self, formatter=None, depth=0):
    formatter = formatter or TableFormatter()
    for arg in self.arguments.values():
      arg.format_help(self.dialect, formatter, depth)
    return formatter

  def print_help(self, fp=None):
    self.print_usage(fp)
    print(file=fp)
    print(self.format_help().format(), file=fp)


class Matcher(object):

  def __init__(self, name, positional=False, exact=False):
    self.name = name
    self.positional = positional
    self.exact = exact

  def format_usage(self, dialect):
    return self.name

  def match(self, arg, dialect):
    if self.positional:
      return True
    if self.exact:
      return self.name == arg
    else:
      if arg == dialect.single + self.name:
        return True
      if arg == dialect.double + self.name:
        return True
      return False


class PositionalMatcher(object):

  def __init__(self, name):
    self.name = name

  def format_usage(self, dialect):
    return self.name

  def match(self, arg, dialect):
    return not dialect.is_flag(arg)


class Consumer(object):

  MORE = 'more'        # More arguments are required
  SAT = 'sat'          # More arguments are allowed
  MAX = 'max'          # No more arguments are allowed
  TOOMANY = 'toomany'  # Too many arguments

  def __init__(self, nargs=1, braces=DISALLOW):
    if braces is True:
      braces = ALLOW
    elif braces is False:
      braces = DISALLOW
    if braces not in (DISALLOW, ALLOW, REQUIRE):
      raise ValueError('invalid braces={!r}'.format(braces))
    if braces in (ALLOW, REQUIRE) and nargs == '...':
      raise ValueError("nargs='...' and braces are incompatible")
    self.nargs = nargs
    self.braces = braces
    self.state([])  # validate value of nargs

  def __repr__(self):
    return 'Consumer(nargs={!r}, braces={!r})'.format(self.nargs, self.braces)

  def state(self, consumed_args):
    if isinstance(self.nargs, str):
      if self.nargs == '*':
        return self.SAT
      elif self.nargs == '+':
        if not consumed_args:
          return self.MORE
        return self.SAT
      elif self.nargs == '?':
        if len(consumed_args) == 1:
          return self.MAX
        elif len(consumed_args) > 1:
          return self.TOOMANY
        else:
          return self.SAT
      elif self.nargs == '...':
        return self.SAT
      else:
        raise ValueError('invalid nargs={!r}'.format(self.nargs))
    elif isinstance(self.nargs, int):
      if len(consumed_args) < self.nargs:
        return self.MORE
      elif len(consumed_args) == self.nargs:
        return self.MAX
      else:
        return self.TOOMANY
    else:
      raise TypeError('invalid type nargs={!r}'.format(self.nargs))

  def suggest_default(self):
    if self.nargs in (1, '?'):
      return None
    elif self.nargs == 0:
      return False
    else:
      return []

  def format_usage(self, dialect, metavar, detailed):
    if self.nargs == '*':
      return '[{} ...]'.format(metavar)
    elif self.nargs == '+':
      return '<{} ...>'.format(metavar)
    elif self.nargs == '?':
      return '[{}]'.format(metavar)
    elif self.nargs == '...':
      return '...'
    elif isinstance(self.nargs, int):
      if self.nargs == 0:
        return ''
      if self.nargs == 1:
        return '<{}>'.format(metavar)
      return '<{} x{}>'.format(metavar, self.nargs)
    else:
      assert False, repr(self.nargs)

  def format_help(self, dialect, metavar, formatter, depth):
    pass

  def consume(self, args, dialect):
    opened_brace = False
    closed_brace = False
    if args and self.braces in (ALLOW, REQUIRE):
      if args[0] == dialect.brace_open:
        opened_brace = True
        args.pop(0)
    if self.braces == REQUIRE and not opened_brace:
      args = []  # No more parseable args

    consumed_args = []
    state = self.state(consumed_args)
    while args:
      if opened_brace and self.braces in (ALLOW, REQUIRE):
        if args[0] == dialect.brace_close:
          args.pop(0)
          closed_brace = True
          break
      if not opened_brace and self.nargs != '...':
        # Check if the front argument is a flag. In that case we don't
        # want to consume any more arguments.
        if dialect.is_flag(args[0]):
          break

      if state == self.TOOMANY:
        raise RuntimeError('too many arguments consumed')
      elif state == self.MAX:
        break
      elif state in (self.MORE, self.SAT):
        consumed_args.append(args.pop(0))
      else: assert False
      state = self.state(consumed_args)

    if opened_brace and not closed_brace:
      raise ArgumentBraceUnclosed()
    if state == self.MORE:
      raise ArgumentCountMismatch(self.nargs, len(consumed_args))

    if self.nargs == 0:
      return True
    elif self.nargs == 1:
      return consumed_args[0]
    elif self.nargs == '?':
      return consumed_args[0] if consumed_args else None
    return consumed_args


class SubparserConsumer(object):

  def __init__(self, parser, consumer):
    self.parser = parser
    self.consumer = consumer

  def suggest_default(self):
    return None

  def format_usage(self, dialect, metavar, detailed):
    return '[ {} ]'.format(self.parser.format_usage().strip()
      if detailed else
      self.consumer.format_usage(dialect, metavar, detailed).strip())

  def format_help(self, dialect, metavar, formatter, depth):
    self.parser.format_help(formatter, depth+1)

  def consume(self, args, dialect):
    consumed_args = self.consumer.consume(args, dialect)
    return self.parser.parse(consumed_args)


class ArgumentCountMismatch(Exception):

  def __init__(self, expected, got):
    self.expected = expected
    self.got = got


class ArgumentBraceUnclosed(Exception):
  pass
