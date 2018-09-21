"""
abadge - generate badges/shields with pure HTML/CSS.



"""
from copy import deepcopy

label_css = '''
    background: #444;
    border-radius: 4px 0px 0px 4px;
    color: white;
    font-family: DejaVu Sans,Verdana,sans;
    font-size: 80%;
    padding: 4px 8px 4px 8px;
    text-shadow: 1px 1px black
}'''

value_css = '''
.badge-value {
    background: #2b2;
    border-radius: 0px 4px 4px 0px;
    color: white;
    font-family: DejaVu Sans,Verdana,sans;
    font-size: 80%;
    padding: 4px 8px 4px 8px;
    text-shadow: 1px 1px black
}
'''


class Badge(object):
    """
    Class which represent status badges/shields.

    This class can be instantiated to generate many badges with the same
    format::

        passed_badge = Badge(value_text_color='#11a')
        print(success_badge.to_html('build', 'passed'))
        print(success_badge.to_html('tests', 'ok'))

    or for one-shot generation::

        print(Badge(label='tests', value='4/8').to_html())
        print(Badge().to_html(label='tests', value='4/8'))  # Same thing
        print(Badge.make_badge(tests, '4/8'))               # This too

    """
    default_config = {
        'border_radius': '4px',
        'font_family': 'DejaVu Sans, Verdana, sans',
        'font_size': '80%',
        'label': '',
        'label_background': '#444',
        'label_text_color': 'white',
        'label_text_shadow': '1px 1px black',
        'link_decoration': 'none',
        'link_target': '',
        'padding': '4px 8px 4px 8px',
        'thresholds': {},
        'url': '',
        'value': '',
        'value_background': '#888',
        'value_backgrounds': {},
        'value_text_color': 'white',
        'value_text_shadow': '1px 1px black',
    }

    template = '<span style="' \
               'background:{label_background};' \
               'border-radius:{border_radius} 0px 0px {border_radius};' \
               'color:{label_text_color};' \
               'font-family:{font_family};' \
               'font-size:{font_size};' \
               'padding:{padding};' \
               'text-shadow:{label_text_shadow};' \
               '">{label}</span>' \
               '<span style="' \
               'background:{value_background};' \
               'border-radius:0px {border_radius} {border_radius} 0px;' \
               'color:{value_text_color};' \
               'font-family:{font_family};' \
               'font-size:{font_size};' \
               'padding:{padding};' \
               'text-shadow:{value_text_shadow};' \
               '">{value}</span>'

    href_template = '<a href="{url}"{link_target}' \
                    ' style="text-decoration:{link_decoration};">'

    def __init__(self, *args, **kwargs):
        """
        Create a badge object with the given configuration.

        Most configuration options are simply CSS settings. Please visit the
        w3c site for detailed information about the values.

        Optional arguments:
        label -- text for the label (left) part
        value -- text for the value (right) part

        Keyword arguments:
        border_radius -- how rounded the corners of the badge should be
                        (CSS "padding")
        font_family -- font to use in the badge (CSS "font-family")
        font_size -- size of the font (CSS "font-size")
        label -- the text in label part of the badge
        label_background -- background color for the label (left) part
                        (CSS "background")
        label_text_color -- text color for the label (left) part
                        (CSS "text-color")
        label_text_shadow -- text shadow for the label part (CSS "text-color")
        link_decoration -- the CSS "text-decoration" setting for the link
        link_target -- set the "target" attribute for the link
        padding -- amount of space between the border and the badge
                   (CSS "padding")
        thresholds -- threshold configuration
        url -- make the badge link to the set URL
        value -- the value part of the badge
        value_background -- background color for the value part
                        (CSS "background")
        value_backgrounds -- dict with value to color mapping for the value
                        part (CSS "background"). Overrides ``value_background``
        value_text_color -- text color for the value part (CSS "text-color")
        value_text_shadow -- text shadow for the value part (CSS "text-shadow")
        """
        self.config = deepcopy(self.default_config)
        self.config.update(self._parse_args(args, kwargs))
        if len(args) > 0:
            self.config['label'] = args[0]
        if len(args) > 1:
            self.config['value'] = args[1]

    @classmethod
    def _parse_args(cls, args, kwargs):
        """
        Parse kwargs and return a dict.
        :param kwargs: dict to parse
        :return:
        """
        if len(args) > 2:
            raise ValueError('a maximum of 2 optional argument may be given'
                             ' ({} were given.)'.format(len(args)))
        for k in kwargs.keys():
            if k not in cls.default_config:
                raise TypeError('unknown option {}'.format(k))
        return kwargs

    @classmethod
    def _determine_type(cls, values):
        is_float = False
        for value in values:
            try:
                float(value)
                if '.' in str(value):
                    is_float = True
            except ValueError:
                return 'str'
        return 'float' if is_float else 'int'

    @classmethod
    def _get_caster_func(cls, order, thresholds):
        value_type = cls._determine_type(list(thresholds['colors'].keys()))
        if order == 'auto' and value_type == 'str':
            return None
        casters = {'str': lambda s: str(s),
                   'int': lambda i: int(i),
                   'float': lambda f: float(f), }
        return casters[value_type]

    @classmethod
    def _get_fraction(cls, min, max, value):
        """
        Determine the fraction od a value between a min and max
        :param min: value which is fraction 0.0
        :param max: value which is fraction 1.0
        :param value: min <= value <= max
        :return: value's fraction between min and max
        """
        if max == min:
            return 0.0
        return (value - min) / (max - min)

    @classmethod
    def _shade(cls, fraction, color1, color2):
        """
        Shades the color between color1 and color2, based on the given
        fraction.
        :param fraction: distance between color1 and color2.
        :param color1: color string in either #rgb or #rrggbb format
        :param color2:  color string in either #rgb or #rrggbb format
        :return: new color string
        """
        cols = []
        for c in [color1, color2]:
            if len(c) == 4:
                cols.append([16 * int(i, 16) for i in list(c[1:])])
            elif len(c) == 7:
                cols.append([int(c[1:3], 16),
                             int(c[3:5], 16),
                             int(c[5:7], 16)])
            else:
                raise ValueError('{}: Error: neither 4 nor 7 characters long'
                                 ''.format(c))
        shade = ['#']
        for i in range(0, 3):
            distance = cols[1][i] - cols[0][i]
            shade.append('{:02x}'
                         ''.format(int(cols[0][i] + distance * fraction)))
        return ''.join(shade)

    @classmethod
    def _get_value_background(cls, config):
        """
        Return the calculated background color based on the "value" key.

        :param config: the config dict
        :return: color string
        """
        try:
            this = config['thresholds'][config['label']]
            order = this.get('order', 'auto')
            if order != 'strict':
                caster = cls._get_caster_func(order, this)
                if caster:
                    thresholds = sorted(list(this['colors'].keys()),
                                        key=lambda v: caster(v))
                    last = thresholds[0]
                    for threshold in thresholds:
                        if caster(config['value']) <= caster(threshold):
                            if this.get('shade', None):
                                fraction = cls._get_fraction(last,
                                                             threshold,
                                                             caster(config['value']))
                                return cls._shade(fraction,
                                                  this['colors'][last],
                                                  this['colors'][threshold])
                            return this['colors'][threshold]
                        last = threshold
                    return this['above']
            return this['colors'][config['value']]
        except KeyError:
            pass

        try:
            return config['value_backgrounds'][config['value']]
        except KeyError:
            pass

        return config['value_background']

    def to_html(self, *args, **kwargs):
        """
        Render HTML for this badge
        :return: string with HTML
        """
        conf = deepcopy(self.config)
        conf.update(self._parse_args(args, kwargs))
        if len(args) > 0:
            conf['label'] = args[0]
        if len(args) > 1:
            conf['value'] = args[1]
        conf['value_background'] = self._get_value_background(conf)
        if conf['url']:
            if conf['link_target']:
                target = conf['link_target']
                conf['link_target'] = ' target="{}"'.format(target)
                if target == '_blank':
                    conf['link_target'] += ' rel="noopener noreferer"'
            return (self.href_template.format(**conf)
                    + self.template.format(**conf) + '</a>')
        return self.template.format(**conf)

    @classmethod
    def make_badge(cls, *args, **kwargs):
        """
        Return the HTML for the given
        :param kwargs:
        :return:
        """
        return Badge().to_html(*args, **kwargs)
