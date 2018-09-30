# -*- encoding:utf-8 -*-

from __future__ import absolute_import
import pycurl
import random
try:
    from io import BytesIO
except ImportError:
    from StringIO import StringIO as BytesIO
import certifi
from PIL import Image

class XdeCurl:
    '''
    CRUL操作类
    '''

    @staticmethod
    def get_version():
        return pycurl.version

    @staticmethod
    def _check_url(url):
        if url[:8] != 'https://' and url[:7] != 'http://':
            print("url is invalid")
            return False

    @staticmethod
    def getRandAgent():
        '''
        随机获取一个agent
        '''
        agents = [
            "Mozilla/5.0 (iPhone; CPU iPhone OS 10_0_2 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/14A456 Safari/602.1",
            "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
            "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
            "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14",
            "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; JuziBrowser)",
            "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)",
            "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)",
            "Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)"]
        randKey = random.randint(0, len(agents) - 1)
        return agents[randKey]

    @staticmethod
    def get(url, timeout=30, agent='', referer='', cookie='', proxy='', authorization='', isfollow=1, returnType=0,
            http_header=[]):
        if XdeCurl._check_url(url) == False:
            return

        statusCode = 0
        buffer = BytesIO()
        ch = pycurl.Curl()
        ch.setopt(ch.URL, url)
        ch.setopt(ch.TIMEOUT, timeout)
        if len(agent) < 1:
            agent = XdeCurl.getRandAgent()
        ch.setopt(ch.USERAGENT, agent)
        ch.setopt(ch.WRITEDATA, buffer)
        if referer.strip():
            ch.setopt(ch.REFERER, referer)
        if url[:5] == 'https':
            ch.setopt(ch.CAINFO, certifi.where())
        if isfollow == 1:
            ch.setopt(ch.FOLLOWLOCATION, 1)
        if len(cookie) > 0:
            ch.setopt(ch.COOKIE, cookie)
        if len(proxy) > 0:
            ch.setopt(ch.PROXY, proxy)
            ch.setopt(ch.HTTPPROXYTUNNEL, 1)  # 隧道代理
            ch.setopt(ch.NOSIGNAL, 1)
        # ch.setopt(ch.PROXYTYPE, 5)

        headers = http_header
        if len(authorization) > 0:
            headers.append('Authorization: ' + authorization)
        if len(headers) > 0:
            ch.setopt(ch.HTTPHEADER, headers)

        if returnType == 2:
            ch.setopt(ch.HEADER, True)
            h = BytesIO()
            ch.setopt(pycurl.HEADERFUNCTION, h.write)

        ch.perform()
        if returnType == 1:  # 只返回http状态码
            statusCode = ch.getinfo(ch.HTTP_CODE)
            ch.close()
            return statusCode
        elif returnType == 2:
            ch.close()
            return h.getvalue()

        ch.close()
        return buffer.getvalue()

    @staticmethod
    def post(url, postData, postType=1, timeout=30, agent='', referer='', cookie='', proxy='', authorization='',
             isfollow=1, returnType=0, http_header=[]):
        '''
        post请求
        postData 请求数据
        postType 1时postData为字典型  2时postData为字符串型
        '''
        if XdeCurl._check_url(url) == False:
            return

        buffer = BytesIO()
        ch = pycurl.Curl()

        if postType == 1:
            post_data = []
            for key in postData.keys():
                if isinstance(postData[key], dict):
                    if 'type' in postData[key]:
                        if postData[key]['type'] == 'file':
                            try:
                                im = Image.open(postData[key]['file'])
                                im.close()
                            except Exception as err:
                                print(err)
                                continue
                            post_data.append((key, (ch.FORM_FILE, str(postData[key]['file']).encode('utf-8'))))
                        elif postData[key]['type'] == 'multiplefile':
                            imgList = []
                            imgList = postData[key]['file'].split(';')
                            for img in imgList:
                                if len(img) < 1:
                                    continue
                                try:
                                    im = Image.open(img)
                                    im.close()
                                except Exception as err:
                                    print(err)
                                    continue
                                post_data.append((key + '[]', (ch.FORM_FILE, img)))
                            if 'target' in postData[key]:
                                post_data.append(
                                    (key + '___Target', (ch.FORM_CONTENTS, postData[key]['target'].encode('utf-8'))))

                else:
                    post_data.append((key, (ch.FORM_CONTENTS, str(postData[key]).encode('utf-8'))))
        elif postType == 2:
            post_data = postData

        # print(post_data)
        #         return
        ch.setopt(ch.MAXREDIRS, 5)
        # ch.setopt(ch.AUTOREFERER,1)
        #         ch.setopt(ch.CONNECTTIMEOUT, 60)
        ch.setopt(ch.TIMEOUT, timeout)
        # ch.setopt(ch.PROXY,proxy)
        ch.setopt(ch.HTTPPROXYTUNNEL, 1)
        if referer.strip():
            ch.setopt(ch.REFERER, referer)
        # ch.setopt(ch.NOSIGNAL, 1)
        if isfollow == 1:
            ch.setopt(ch.FOLLOWLOCATION, 1)
        if len(agent) < 1:
            agent = XdeCurl.getRandAgent()
        if len(cookie) > 0:
            ch.setopt(ch.COOKIE, cookie)
        if len(proxy) > 0:
            ch.setopt(ch.PROXY, proxy)
            ch.setopt(ch.HTTPPROXYTUNNEL, 1)  # 隧道代理
            ch.setopt(ch.NOSIGNAL, 1)
            ch.setopt(ch.SSL_VERIFYPEER, 0)
        ch.setopt(ch.USERAGENT, agent)
        # Option -d/--data <data>  HTTP POST data
        if postType == 1:
            ch.setopt(ch.POST, 1)
            ch.setopt(ch.HTTPPOST, post_data)
        elif postType == 2:
            ch.setopt(ch.POSTFIELDS, post_data)
        ch.setopt(ch.URL, url)
        # ch.setopt(crl.WRITEFUNCTION, crl.fp.write)
        ch.setopt(ch.WRITEDATA, buffer)

        headers = http_header
        if len(authorization) > 0:
            headers.append('Authorization: ' + authorization)
        if len(headers) > 0:
            ch.setopt(ch.HTTPHEADER, headers)

        if returnType == 2:
            ch.setopt(ch.HEADER, True)
            h = BytesIO()
            ch.setopt(pycurl.HEADERFUNCTION, h.write)

        ch.perform()
        if returnType == 1:  # 只返回http状态码
            statusCode = ch.getinfo(ch.HTTP_CODE)
            ch.close()
            return statusCode
        elif returnType == 2:
            ch.close()
            return h.getvalue()

        ch.close()
        return buffer.getvalue()


if __name__ == '__main__':
    print(XdeCurl.get_version())

    print(XdeCurl.get("https://api.douban.com/v2/book/isbn/9787807681472"))

    # print(XdeCurl.post("http://test.com/test/interface/test/",
    #                 {"key":"80f0b510fcf7c07cd5c1e4a21eae8242",
    #                  "isbn":"9780060675111",
    #                  "bookName":"测试",
    #                  "certifyStatus":"failed",
    #                  "smallImg":{"type":"multiplefile", "file":"D:/tmp/1c40be7270380b2ae09ffd2ed1e54447_l.jpg;D:/tmp/1c40be7270380b2ae09ffd2ed1e54447_m.jpg;",
    #                              "target":"dangdang/1c40/1c40be7270380b2ae09ffd2ed1e54447_l.jpg;dangdang/1c40/1c40be7270380b2ae09ffd2ed1e54447_m.jpg"}}))

    print(XdeCurl.getRandAgent())

    # print(XdeCurl.get("http://test.com/3794504281111111111111111111/", proxy = "http://110.72.17.71:8123", timeout = 60))


    # print(XdeCurl.get("http://192.168.1.1/userRpm/StatusRpm.htm?Disconnect=%B6%CF%20%CF%DF&wan=3", referer="http://192.168.1.1/userRpm/StatusRpm.htm", authorization="Basic YWRtaW46ZjZlNmI2ZGYyZA=="))


    x = XdeCurl.get('https://www.baidu.com/',returnType=2)
    print(x)

