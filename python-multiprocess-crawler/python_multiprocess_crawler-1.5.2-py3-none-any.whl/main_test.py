from main import CrawlerBase

# class Test(CrawlerBase):
#     def __init__(self, *args, **kwargs) -> None:
#         # calling the __init__ method of the CrawlerBase Class
#         super(GoogleCrawler, self).__init__(*args, **kwargs)

if __name__ == "__main__":
    c = CrawlerBase()
    p = c.downloadSourceCode('www.google.com', proxy={
        'server': 'http://sk15.nordvpn.com',
        'username': 'rolik.jakob@protonmail.com',
        'password': 'mfbsitSoIaFetb46'
    })

    print(p.data)