from NorrisUtils import RawUtils
import NorrisUtils.BuildVirant as BuildVariant


def extractHeaders(str):
    return RawUtils.extractRawDict(str, {}, '\n', ': ')


headerstr = '''Connection: keep-alive
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9'''

if BuildVariant.DebugBackDoor:
    print(extractHeaders(headerstr))
