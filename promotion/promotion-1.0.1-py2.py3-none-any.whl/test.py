import re

content = """
<ul class="pagelink">
                <li>上一篇：<a href="/web/python/259.html">python获取本月第一天，本年第一天</a> </li>
                <li>下一篇：<a href="/web/python/263.html">python计算本月的天数</a> </li>
            </ul>
            """
pattern = re.compile('</?a[^>]*>')
print(pattern.sub('', content))