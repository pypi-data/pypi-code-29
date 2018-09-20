
import re
import textwrap

from .utils import StringIO, terminal_size

try:
  from itertools import zip_longest as zip_longest
except ImportError:
  from itertools import izip_longest as zip_longest


class TableFormatter(object):

  class Cell(object):
    def __init__(self, lines, colspan, padding):
      self.lines = lines
      self.colspan = colspan
      self.padding = padding
    def __repr__(self):
      return 'Cell(lines={!r}, colspan={!r}, padding={!r})'.format(
        self.lines, self.colspan, self.padding)
    def max_width(self):
      return self.padding + max(sum(len(w) for w in l) + len(l)-1 for l in self.lines)
    def columnize(self, width):
      lines = []
      for line in (' '.join(x) for x in self.lines):
        if line:
          lines += (' ' * self.padding + l for l in textwrap.wrap(line, width))
        else:
          lines.append('')
      return lines

  def __init__(self, width=None, width_fallback=80, vgap=0,
               gap='  ', left='', right=''):
    if width is None:
      width = terminal_size((width, 0))[0]
    self.width = width
    self.vgap = vgap
    self.gap = gap
    self.left = left
    self.right = right
    self.rows = []

  def put_row(self, cols, colspans=None, paddings=None):
    if paddings is None:
      paddings = []
    if colspans is None:
      colspans = []
    paddings = iter(paddings)
    colspans = iter(colspans)
    row = []
    for i, text in enumerate(cols):
      text = textwrap.dedent(text).strip()
      lines = text.split('\n')
      indents = [len(x) - len(x.lstrip()) for x in lines]
      lines = [x.split() for x in lines]
      for indent, line in zip(indents, lines):
        if line:
          line[0] = ' ' * indent + line[0]
      row.append(self.Cell(lines, max(0, next(colspans, 1)), next(paddings, 0)))
    self.rows.append(row)

  def format(self):
    if not self.rows:
      return ''
    ncols = max(sum(c.colspan for c in row) for row in self.rows)
    if ncols <= 0:
      ncols = 1

    # Calculate the colspan of full scaling cells.
    # We weight the column assigned based on the size of the content.
    for i, row in enumerate(self.rows):
      fixed = [c for c in row if c.colspan >= 1]
      fixed_cols = sum(c.colspan for c in fixed)
      unfixed = [c for c in row if c.colspan < 1]
      if not unfixed:
        continue
      if len(unfixed) > ncols - fixed_cols:
        raise RuntimeError("no columns left that can be assigned in row {}".format(i))
      weights = [c.max_width() for c in unfixed]
      weightsum = sum(weights)
      weights = [(c, float(w)/weightsum) for c, w in zip(unfixed, weights)]
      weights.sort(key=lambda t: t[1])
      consumed = 0
      for c, w in weights:
        span = min(ncols - fixed_cols - consumed, max(1, round(ncols - fixed_cols) * w))
        consumed += span
        c.colspan = span

    # Calculate the required width of every non-spanning column.
    target_widths = [0] * ncols
    for row in self.rows:
      offset = 0
      for c in row:
        if c.colspan == 1:
          target_widths[offset] = max(target_widths[offset], c.max_width())
        offset += c.colspan

    # Adjust the required width of elementary columns width the
    # spanning columns.
    max_width = self.width - len(self.gap) * (ncols - 1)
    avg_width = max_width // ncols
    for row in self.rows:
      offset = 0
      for c in row:
        if c.colspan != 1:
          remaining = c.max_width()
          for i in range(offset, offset+c.colspan):
            remaining -= min(avg_width, target_widths[i])
            target_widths[i] = max(min(remaining, avg_width), target_widths[i])
        offset += c.colspan

    # Everything below the average width does not need to be compressed.
    below_avg_sum = sum(w for w in target_widths if w <= avg_width)
    above_avg_sum = sum(w for w in target_widths if w > avg_width)
    n_above_avg = sum(1 for w in target_widths if w > avg_width)
    width_to_compress = above_avg_sum - (max_width - below_avg_sum)

    # Reduce the size of the columns that are too wide.
    final_widths = target_widths[:]
    for i, w in enumerate(target_widths):
      if w > avg_width:
        final_widths[i] = max(1, final_widths[i] - int(width_to_compress))

    if sum(final_widths) != max_width:
      # TODO: Further adjust width if the total width is not exactly
      # the formatter width.
      pass

    fp = StringIO()
    for row in self.rows:
      offset = 0
      widths = []
      column_lines = []
      for c in row:
        widths.append(sum(final_widths[offset:offset+c.colspan]) + len(self.gap) * (c.colspan - 1))
        column_lines.append(c.columnize(widths[-1]))
        offset += c.colspan
      offset = 0
      for line in zip_longest(*column_lines): # Transpose
        for i, (text, width) in enumerate(zip(line, widths)):
          text = (text or '').rstrip().ljust(width)
          assert len(text) == width
          if i == 0:
            fp.write(self.left)
          elif i < len(widths):
            fp.write(self.gap)
          fp.write(text)
          if i == len(widths)-1:
            fp.write(self.right)
        fp.write('\n')
      if not row:
        fp.write('\n')
      else:
        fp.write('\n' * self.vgap)

    return fp.getvalue()
