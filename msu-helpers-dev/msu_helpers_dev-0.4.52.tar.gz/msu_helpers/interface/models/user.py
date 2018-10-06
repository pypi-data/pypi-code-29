import re

__all__ = ('UserSearchModel',)


class UserSearchModel:
    def __init__(self, value=''):
        param_match = re.match('(?P<first_name>[\wА-Яа-я]+)'
                               '(/(?P<last_name>[\wА-Яа-я]+))?'
                               '(/(?P<group_code>[\wА-Яа-я\-\d]{0,10}))?',
                               value)

        if param_match:
            self.parsed_data = param_match.groupdict()
        else:
            self.parsed_data = dict()

        self.first_name: str = self.parsed_data.get('first_name', '')
        self.last_name: str = self.parsed_data.get('last_name', '')
        self.group_code: str = self.parsed_data.get('group_code', '')

        if self.first_name is None:
            self.first_name = ''

        if self.last_name is None:
            self.last_name = ''

        if self.group_code is None:
            self.group_code = ''

    def __str__(self):
        return f'{self.parsed_data}'
