class Paginator(object):
    '''
    A class for paginating, you can save and transmit data with it after get data from database.
    This class applicable for pagination in admin system
    '''

    def __init__(self, page, pages, items, total, per_page=10):
        '''
        :param int page: Current page number
        :param int pages: Total page count
        :param object items: Paging data
        :param int total: Total item count
        :param int per_page: How many items per page
        '''
        self.page = page
        self.pages = pages
        self.items = items
        self.total = total
        self.per_page = per_page

    def get_dict(self):
        '''
        Convert Paginator instance to dict

        :return: Paging data
        :rtype: dict
        '''

        return dict(
            page=self.page,
            pages=self.pages,
            per_page=self.per_page,
            items=self.items,
            total=self.total
        )
