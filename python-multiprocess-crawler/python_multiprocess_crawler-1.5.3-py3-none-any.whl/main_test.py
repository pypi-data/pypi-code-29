from main import CrawlerBase

class Test(CrawlerBase):
    def __init__(self, *args, **kwargs) -> None:
        # calling the __init__ method of the CrawlerBase Class
        super(Test, self).__init__(*args, **kwargs)
    
    def parse(self, site):
        print(site)


if __name__ == "__main__":
    c = Test()
    c.addToQueue('www.google.com')
    c.runMultipleProcessesUntilQueueEmpty()