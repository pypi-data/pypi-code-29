from dli.siren import siren_to_entity
from dli.client.utils import ensure_count_is_valid

"""
Functions related to the current logged in user.
"""

class MeFunctions:

    @property
    def __root(self):
        return self.get_root_siren().me()

    def get_my_packages(self, count=100):
        """
        Returns a list of packages where I'm:
        * A Manager
        * Tech Data Ops
        * Access Manager

        :param int count: The number of items to retrieve, defaults to 100.
        """
        ensure_count_is_valid(count)

        result = self.__root.my_packages(page_size=count)
        packages = result.get_entities(rel="package")
        return [siren_to_entity(p) for p in packages]
