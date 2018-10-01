from urllib3.contrib.socks import SOCKSProxyManager
import urllib3
import urllib.parse
from bs4 import BeautifulSoup as Soup
import user_agent
import multiprocessing
from typing import List
from multiprocessing import Manager

class CrawlerBase:
    """ 
    A Base class for crawlers and spiders that will be able to implement multiprocessing
    Each child class must have a 'self.parse' function since that is the function that gets called for
    every new site visited.

    The Queue handling is done automatically so you have no reason to work with the queue directly. The queue item is passed as a first argument to the parse function

    The multiprocessing is implemented in such a way that you can add urls (or other things) to the queue while the scraper is running. Which you can do 
    in the 'self.scrape' function through self.addUrlToTheQueue()
    """
    def __init__(self, pool_size=4):
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.pool_size = pool_size
        m = multiprocessing.Manager()
        self.queue = m.Queue()
    
    def fillQueueFromList(self, arr: List):
        for item in arr:
            self.queue.put(item)
    
    def addToQueue(self, item: any) -> None:
        self.queue.put(item)
    
    def addUrlToTheQueue(self, url: str):
        self.queue.put(url)

    def downloadSourceCode(self, url, proxy=None) -> urllib3.response.HTTPResponse:
        """ 
        Downloads and returns the source code 
        of the website from the passed-in url 
        """
        http = None
        customHeader = {'user-agent': user_agent.generate_user_agent()}

        if proxy:
            if 'socks5' in proxy['server']:
                http = SOCKSProxyManager(
                    proxy['server'],
                    headers=customHeader,
                    username=proxy['username'],
                    password=proxy['password']
                )
            else:
                auth = f"{proxy['username']}:{proxy['password']}"
                default_headers = urllib3.make_headers(proxy_basic_auth=auth)
                print({**customHeader, **default_headers})
                http = urllib3.ProxyManager(proxy['server'], headers={**customHeader, **default_headers})

        else:
            http = urllib3.PoolManager(headers=customHeader)
    
        r = http.request('GET', url)

        return r
    
    def downloadSourceCodeAsBs4(self, url, proxy = None) -> Soup:
        """ Downloads the website and converts it to bs4 """
        r = self.downloadSourceCode(url=url, proxy=proxy)
        return Soup(r.data, 'html.parser')

    def waitForMultiprocessesToFinish(self, processes_to_await: List):
        """ Blocks until all the processes from the array are not finished """
        return [l.get() for l in processes_to_await]

    def runSingleProcessUntilQueueEmpty(self, *args, **kwargs):
        """ 
        Will run the self.parse function one at a time
        Until the queue is empty
        """
        while not self.queue.empty():
            self.parse(self.queue.get(), *args, **kwargs)

    def runMultipleProcessesUntilQueueEmpty(self, *args, **kwargs):
        """ 
        Will run the self.parse function in parralell by chunks of 
        self.pool_size Until the Queue is empty 
        and there are no more sites to crawl
        """
        while not self.queue.empty():
            # Fill the pool
            pool = multiprocessing.Pool(processes=4)
            processes = []
            for _ in range(self.pool_size):
                if self.queue.empty():
                    continue
                else:
                    processes.append(pool.apply_async(
                        self.parse,
                        args=(
                            self.queue.get(),
                        )
                    ))
            # This function blocks the program so that the
            # while loop is not exited while the processes are running
            # and have not filled the queue yet
            self.waitForMultiprocessesToFinish(processes)
            pool.close()
            pool.join()
    
    def parse(self):
        raise NotImplementedError("This class should be used only as a base class")

