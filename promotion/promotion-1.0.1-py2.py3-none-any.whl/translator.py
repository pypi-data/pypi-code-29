# -*- coding:utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import hashlib
import random
import re

from multiprocessing.dummy import Pool as ThreadPool
from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.tmt.v20180321 import tmt_client, models

__author__ = "TANG BIN <bintang.hit@gmail.com>"
__date__ = "24 Sep 2018"


__all__ = [
    'BaseTranslator',
    'BaiduTranslator',
    'TencentTranslator',
]


class BaseTranslator(object):
    def __init__(self, max_try_time=3, threads=20):
        self.max_try_time = max_try_time
        self.threads = threads


    def _split_text_n_tag(self, content):
        """ 从html中分离出tag和text，表达成text+tag+text+ta 
        g...
        的形式，这样可以在text翻译后迭代组装

        Args:
            content: html

        Returns:
            texts, tags
        """
        texts = []
        tags = []

        bpos = content.find('<')
        epos = 0
        while bpos != -1:
            cur_epos = bpos + 1
            if content[cur_epos] == '/':
                cur_epos += 1

            blank_pos = content.find(' ', cur_epos)
            bracket_pos = content.find('>', cur_epos)
            tag_name = content[cur_epos:blank_pos]
            if blank_pos == -1 or blank_pos > bracket_pos:
                tag_name = content[cur_epos:bracket_pos]
            tag_name = tag_name.rstrip("/")

            # 判断tag是否符合html tag的规范
            if tag_name.isalnum() and len(tag_name) < 10:
                if bracket_pos == -1:
                    bpos = -1
                else:
                    texts.append(content[epos:bpos])
                    epos = bracket_pos + 1
                    tags.append(content[bpos:epos])
                    bpos = content.find('<', epos)
            else:
                bpos = cur_epos
        texts.append(content[epos:])

        return texts, tags


    def _translate(self, text, source, target):
        """ 翻译插件需要实现的接口

        Arags:
            text: 源语言文本
            source: 源语言
            target: 目标语言

        Returns:
            翻译成目标语言后的文本
        """
        raise NotImplementedError


    def _translate_tag(self, tag, source, target):
        if tag[:5] != '<img ':
            return tag

        patterns = [re.compile(r'(alt=["|\'])(.*?)([\'|"])'), 
                    re.compile(r'(title=["|\'])(.*?)([\'|"])')]
        for pattern in patterns:
            text = re.search(pattern, tag)
            if text is None or len(text.groups()) < 3:
                continue
            trans_text = self._translate(text.group(2), source, target)
            trans_text = '' if trans_text is None else trans_text
            tag = pattern.sub(r"\g<1>" + trans_text + r"\g<3>", tag)

        return tag


    def translate(self, content, source='zh', target='en'):
        """ 翻译接口
        
        Args:
            content: 待翻译的内容
            source: 源语言
            target: 目标语言
        
        Returns:
            成功返回翻译后的文本，否则返回None
        """
        def _generate_args(texts):
            for idx, text in enumerate(texts):
                yield (text, source, target)

        texts, tags = self._split_text_n_tag(content)

        thread_pool = ThreadPool(self.threads)
        trans_texts = []
        for args in _generate_args(texts):
            trans_texts.append(thread_pool.apply_async(self._translate, args))

        thread_pool.close()
        thread_pool.join()

        thread_pool = ThreadPool(self.threads)
        trans_tags = []
        for args in _generate_args(tags):
            trans_tags.append(thread_pool.apply_async(self._translate_tag, args))

        thread_pool.close()
        thread_pool.join()

        arrays = []
        try:
            for idx, text in enumerate(trans_texts):
                text = text.get()
                text = '' if text is None else text
                arrays.append(text)

                if idx < len(trans_tags):
                    tag = trans_tags[idx].get()
                    tag = '' if tag is None else tag
                    arrays.append(tag)

            return ''.join(arrays)

        except Exception as e:
            print(e)
            return None


class BaiduTranslator(BaseTranslator):
    def __init__(self, max_try_time=3, threads=20):
        BaseTranslator.__init__(self, max_try_time, threads)
        self.appid = '20180826000198976' #你的appid
        self.secret_key = 'czLP2B29jZrijqXyfSdF' #你的密钥
        self.url = 'http://api.fanyi.baidu.com/api/trans/vip/translate'


    def _translate(self, text, source, target):
        if text.strip() == "":
            return text

        salt = random.randint(32768, 65536)
        sign = self.appid + text + str(salt) + self.secret_key
        md5_ins = hashlib.md5()
        md5_ins.update(sign.encode('utf-8'))
        sign = md5_ins.hexdigest()

        data = {
            'q': text,
            'from': source,
            'to': target,
            'appid': self.appid,
            'salt': salt,
            'sign': sign
        }
        
        for try_time in range(self.max_try_time):
            try:
                response = requests.post(self.url, data, timeout=2)
                if response.status_code != 200:
                    continue

                result = response.json()
                if 'error_code' in result:
                    continue

                return response.json()['trans_result'][0]['dst']
            except Exception as e:
                continue

        return None


class TencentTranslator(BaseTranslator):
    def __init__(self, max_try_time=3, threads=20):
        BaseTranslator.__init__(self, max_try_time, threads)
        self.proj_id = '1123359'
        self.secret_id = 'AKIDxpdMxNW9QXWJyY7IPL9NZbXM1Wr9vOKA'
        self.secret_key = 'Z1WwDKI5hGlCVfeT7gDaouthKl283mKq'

        cred = credential.Credential(self.secret_id, self.secret_key)
        self.client = tmt_client.TmtClient(cred, "ap-guangzhou")


    def _translate(self, text, source, target):
        """
        pip install tencentcloud-sdk-python
        """
        if text.strip() == "":
            return text

        request = models.TextTranslateRequest()
        request.Source = source
        request.Target = target
        request.ProjectId = self.proj_id
        request.SourceText = text

        for try_time in range(self.max_try_time):
            try:
                response = self.client.TextTranslate(request)
                return response.TargetText

            except TencentCloudSDKException as err:
                continue

        return None

