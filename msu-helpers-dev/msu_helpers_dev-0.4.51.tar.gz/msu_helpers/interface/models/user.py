import re

__all__ = ('UserSearchModel',)


class UserSearchModel:
    def __init__(self, value=''):
        self.parsed_data = re.match('(?P<first_name>[\wА-Яа-я]+)'
                                    '(/(?P<last_name>[\wА-Яа-я]+))?'
                                    '(/(?P<group_code>[\wА-Яа-я\-\d]{0,10}))?',
                                    value).groupdict()
        self.first_name: str = self.parsed_data.get('first_name', '')
        self.last_name: str = self.parsed_data.get('last_name', '')
        self.group_code: str = self.parsed_data.get('group_code', '')

    def __str__(self):
        return f'{self.parsed_data}'
