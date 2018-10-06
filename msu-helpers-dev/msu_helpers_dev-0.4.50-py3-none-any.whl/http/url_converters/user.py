from ...interface.models.user import *

__all__ = ('UserSearchModelConverter',)


class UserSearchModelConverter:
    regex = '([\wА-Яа-я]+)(/([\wА-Яа-я]+))?(/([\wА-Яа-я\-\d]{0,10}))?'

    def to_python(self, value):
        return UserSearchModel(value)

    # def to_url(self, value):
    #     return '%04d' % value
