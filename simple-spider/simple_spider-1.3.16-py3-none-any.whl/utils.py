import time,tomd,markdown,re
from urllib import parse


class Utils:

    @staticmethod
    def build_get_url(base, path, query={}):
        if '?' in path:
            tmp = path.split('?')
            path = tmp[0]

        query['t'] = time.time()
        return parse.urljoin(base, "%s?%s" % (path, parse.urlencode(query)))

    @staticmethod
    def url_encode(str):
        return parse.quote(str)

    @staticmethod
    def url_decode(str):
        return parse.unquote(str)

    @staticmethod
    def url_qs(url, name):
        obj = parse.urlparse(url)
        qs = parse.parse_qs(obj.query)
        for key in qs:
            val = qs[key]
            if len(val) == 1:
                qs[key] = val[0]
            else:
                qs[key] = val

        return qs.get(name)

    @staticmethod
    def normalize_html(html):
        md = tomd.Tomd(html).markdown
        return markdown.markdown(md)

    @staticmethod
    def clear_styles(html):
        re_style=re.compile('<\s*style[^>]*>[^<]*<\s*/\s*style\s*>',re.I)#style
        html=re_style.sub('',html)#去掉style
        return html

    @staticmethod
    def fetch_text(reg, str):
        list = re.findall(reg, str, re.S)
        if list and len(list) > 0:
            return list[0]
        else:
            return None


