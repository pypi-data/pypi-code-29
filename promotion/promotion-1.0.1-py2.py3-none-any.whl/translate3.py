import sys,importlib
import json
import requests
import hashlib
import urllib
import random
import re
from urllib import parse
from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.tmt.v20180321 import tmt_client, models


def tencent_translate(content):
    """
    pip install tencentcloud-sdk-python
    """
    proj_id = '1123359'
    secret_id = 'AKIDxpdMxNW9QXWJyY7IPL9NZbXM1Wr9vOKA'
    secret_key = 'Z1WwDKI5hGlCVfeT7gDaouthKl283mKq'

    def _process_img_tag(tag, client, request):
        return tag

    try:
        cred = credential.Credential(secret_id, secret_key)
        client = tmt_client.TmtClient(cred, "ap-guangzhou")
        request = models.TextTranslateRequest()
        request.Source = 'zh'
        request.Target = 'en'
        request.ProjectId = proj_id

        texts = []
        for text in content.split("</p>"):
            if not text:
                continue

            bpos = text.find('<p')
            epos = text.find('>', bpos)
            target = text[bpos:epos+1]

            ibpos = text.find('<img ', epos+1)
            if ibpos != -1:
                request.SourceText = text[epos+1:ibpos]
                response = client.TextTranslate(request)
                target += response.TargetText

                target += text[ibpos:epos+1]

                iepos = text.find('>', ibpos)
                request.SourceText = text[iepos+1:]
                response = client.TextTranslate(request)
                target += response.TargetText

            else:
                request.SourceText = text[epos+1:]
                response = client.TextTranslate(request)
                target += response.TargetText

            if bpos != -1:
                target += '</p>'
            texts.append(target)

        return ''.join(texts)

    except TencentCloudSDKException as err:
        return ''


if len(sys.argv)!= 5:
    print(len(sys.argv))
    print("命令行参数长度不为5")
    sys.exit()
else:
    LabelCookie = parse.unquote(sys.argv[1])
    LabelUrl = parse.unquote(sys.argv[2])
    #PageType为List,Content,Pages分别代表列表页，内容页，多页http请求处理，Save代表内容处理
    PageType=sys.argv[3]
    SerializerStr = parse.unquote(sys.argv[4])
    if (SerializerStr[0:2] != '''{"'''):
        file_object = open(SerializerStr)
        try:
            SerializerStr = file_object.read()
            SerializerStr = parse.unquote(SerializerStr)
        finally:
            file_object.close()
    LabelArray = json.loads(SerializerStr)


#以下是用户编写代码区域
    if PageType == "Save":
        for key, value in LabelArray.items():
            if LabelArray[key] and (isinstance(value, str) or isinstance(value, unicode)):
                LabelArray[key] = tencent_translate(value)


#以上是用户编写代码区域
    LabelArray = json.dumps(LabelArray)
    print(LabelArray)