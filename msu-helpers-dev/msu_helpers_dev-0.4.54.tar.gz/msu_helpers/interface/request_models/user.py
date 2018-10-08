from .base import *

__all__ = ('UserSearchModel',)


class UserSearchModel(Base):
    regex = ('(?P<p_first_name>[\wА-Яа-я]+)'
             '(/(?P<p_last_name>[\wА-Яа-я]+))?'
             '(/(?P<p_group_code>[\wА-Яа-я\-\d]{0,10}))?')

    __str_fields__ = ('p_first_name', 'p_last_name', 'p_group_code')

    def __init__(self, value=''):
        super().__init__(value)

        self.p_first_name: str = self.parsed_data.get('p_first_name', '')
        self.p_last_name: str = self.parsed_data.get('p_last_name', '')
        self.p_group_code: str = self.parsed_data.get('p_group_code', '')

        self.validate()
