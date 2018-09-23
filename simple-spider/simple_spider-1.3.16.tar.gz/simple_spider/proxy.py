import os, random
class Proxy:

    def __init__(self,proxy_list):
        self.init_proxy_list = proxy_list
        self.proxy_map = {}
        self.load_proxies()
        self.current_proxy = None

    def http_proxy(self):
        if self.current_proxy:
            return self.current_proxy
        else:
            self.switch_proxy()
            return self.current_proxy

    def switch_proxy(self, reload=True):
        proxy_list = []
        for proxy, score in self.proxy_map.items():
            if score > 0.5:
                proxy_list.append(proxy)

        # 如果没有取到任何代理，则尝试重新加载一次
        if len(proxy_list) == 0 and reload:
            self.load_proxies()
            return self.switch_proxy(reload = False)

        if len(proxy_list) > 0:
            result = random.sample(proxy_list,1) # 随机取一个
            self.current_proxy = result[0]
        else:
            self.current_proxy = None

    def inc_score(self,proxy):
        if self.proxy_map.get(proxy,None):
            score = self.proxy_map.get(proxy)
            next_score = score * (1 + 0.5)
            self.proxy_map[proxy] = next_score if next_score <= 1.0 else 1.0

    def desc_score(self,proxy):
        if self.proxy_map.get(proxy,None):
            score = self.proxy_map.get(proxy)
            self.proxy_map[proxy] = score * (1 - 0.5)

    def load_proxies(self):
        if not self.init_proxy_list:
            return
        if not os.path.exists(self.init_proxy_list):
            #print(self.init_proxy_list)
            return

        for line in open(self.init_proxy_list):
            line = line.strip()
            if line and line != '':
                # 首先，判断原来的map中是否含有，没有再重新插入
                score = self.proxy_map.get(line,None)
                if score is None:
                    self.proxy_map.update({line: 1.0}) # 默认1.0分
                else:
                    pass



