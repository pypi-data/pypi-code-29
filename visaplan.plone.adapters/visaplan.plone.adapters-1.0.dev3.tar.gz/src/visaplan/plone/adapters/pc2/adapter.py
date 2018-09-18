from tomcom.adapter.public import Interface, Base
from visaplan.plone.tools.context import decorated_tool


class ICatalogToolAdapter(Interface):
    pass


class Adapter(Base):

    def __call__(self):
        return decorated_tool(self.context, 'portal_catalog',
                              limit_get_delta=1)
