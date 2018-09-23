import queue,traceback,simplejson,pyquery,logging,time
from urllib import parse

from .fetcher import Fetcher

logger = logging.getLogger('SimpleSpider')


class BaseSpider:

    def __init__(self, options={}):
        '''
        option指定相关配置参数
        :param options:
            * enable_session: 开启抓取器的session，将自动保存IP等
            * proxy_list : 代理列表
            * debug_proxy: 开启调试代理。debug_proxy有值的情况下，会忽略proxy_list选项
        '''

        self.task_queue = queue.Queue()
        self.fetcher = Fetcher(options)

    def run(self, skip_start=False):
        if not skip_start:
            self.start()

        while True:
            try:
                task = self.task_queue.get_nowait()
                self._do_task(task)

                time.sleep(1)
            except queue.Empty:
                logger.info("task queue is empty now")
                break
            except Exception as e:
                # 其他异常
                raise e



    def crawl(self,url, callback,
              method = 'GET',
              data = {},
              headers={},
              cookies = {},
              save={},
              content_type='html',
              encoding='utf8',
              options={}):
        if not url or not callback:
            raise Exception("Url and callback should be set")

        # 先测试一下是否
        cb_func = getattr(self,callback.__name__)
        if not callable(cb_func):
            raise Exception("%s is not callback", callback.__name__)

        task = {
            'url': url,
            'callback': callback.__name__,
            'method': method,
            'data': data,
            'cookies': cookies,
            'headers': headers,
            'options': options,
            'save': save,
            'content_type': content_type,
            'encoding': encoding
        }
        logging.info("New crawl task: url = %s, callback = %s" %(url, cb_func))
        self.task_queue.put(task)

    def debug_crawl(self, **params):
        self.crawl(**params)
        self.run(skip_start=True)

    def _do_task(self,task):
        self.fetcher.pick_new_proxy()

        url = task.get('url')
        callback = task.get('callback')
        headers = task.get('headers',{})
        options = task.get('options',{})
        method = task.get('method','GET')
        data = task.get('data',{})
        cookies = task.get('cookies',{})
        data_type = task.get('content_type','html')
        encoding = task.get('encoding','utf8')

        # 判断是否需要限流
        last_execute = task.get('last_execute', 0)
        current_proxy = self.fetcher.current_proxy()
        if time.time() - last_execute <= self.throttle(url, current_proxy):
            # 命中节流
            logger.debug("Hit throttling, try next time. url = %s, proxy = %s" % (url, current_proxy) )
            self.task_queue.put(task) # 重新放入队列即可，不额外处理
            return

        logger.debug("Start crawling %s with callback = %s and content-type = %s" % (url, callback, data_type))

        err = None
        result = ''
        try:
            logger.info("Do fetching url: %s" % url)
            result = self.fetcher.fetch(url, method= method, headers= headers, cookies = cookies, data= data, encoding= encoding)
            status_code = result.get('status_code',404)

            logger.debug("Got status code %d " % status_code)

            if status_code == 200:
                pass
            else:
                err = SpiderError(
                    status_code=status_code,
                    reason=result.get('reason',''),
                    url=url,
                    content=result.get('content'),
                    proxy=self.fetcher.current_proxy())

        except Exception as e:
            err = SpiderError(
                status_code = 0,
                reason = str(e),
                url = url,
                content = None,
                proxy = self.fetcher.current_proxy()
            )

        cb = getattr(self,callback)
        if callable(cb):
            ret = True
            try:
                if err:
                    logger.warning("Found error when fetching %s, status code = %s, and err reason = %s " %(url, err.status_code, err.reason))
                    ret = cb(err, SpiderResponse(result, type= 'text', task= task, is_err=True))
                else:
                    ret = cb(None, SpiderResponse(result, type= data_type,task= task, is_err=False))
            except Exception as e:
                logger.error('Error when process fetch result: %s' % traceback.format_exc())

            if ret is True:
                self.evaluate_proxy(self.fetcher.current_proxy(), True)
            else:
                # 返回False，表示处理失败，包括返回了爬虫页面之类，这个情况下，需要给代理扣分，并且稍后重试
                self.evaluate_proxy(self.fetcher.current_proxy(), False)
                self.retry_task(task)

    def retry_task(self,task):
        retry = task.get('retry', 0)
        options = task.get('options', {})
        max_reties = options.get('retry', 3)  # 重试次数

        if retry >= max_reties:
            logger.info("Skip task because retry max count, url= %s" % task.get('url'))
        else:
            retry += 1
            task.update(
                {
                    'retry': retry,
                    'last_execute': time.time()
                 }
            )
            self.task_queue.put(task)

    def evaluate_proxy(self,proxy, status):
        if status:
            self.fetcher.inc_proxy_score(proxy)
        else:
            self.fetcher.desc_proxy_score(proxy)


    def throttle(self,url,proxy):
        return 1

    def start(self):
        logger.warn("start must be implement")


class SpiderError:
    def __init__(self, status_code,reason, url, content, proxy):
        self.status_code = status_code
        self.reason = reason
        self.url = url
        self.content = content
        self.proxy = proxy


class SpiderResponse:
    def __init__(self, result, type='text', task={},is_err = False):

        self.content = None
        self.json = None
        self.doc = None
        self.save = task.get('save',{})
        self.url = result.get('url')
        self.url_qs = {}
        self.task = task

        # 组装对象
        if is_err:
            self.content = result.get('reason','')
        else:
            if type == 'text':
                self.content = result.get('text','')
            elif type == 'bin':
                self.content = result.get('content','')
            elif type == 'json':
                self.content = result.get('text', '')
                self.json = simplejson.loads(self.content)
            elif type == 'html':
                self.content = result.get('text', '')
                self.doc = pyquery.PyQuery(self.content)
            else:
                # 默认使用html来解析
                self.content = result.get('text', '')
                self.doc = pyquery.PyQuery(self.content)

        # 组装url参数快捷方式
        obj_url = parse.urlparse(self.url)
        qs = parse.parse_qs(obj_url.query)
        for key in qs:
            val = qs[key]
            if len(val) == 1:
                qs[key] = val[0]
            else:
                qs[key] = val
        self.url_qs = qs



