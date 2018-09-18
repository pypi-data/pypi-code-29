from visaplan.plone.base import Base, Interface
from Products.CMFCore.utils import getToolByName


class IPortalUserCatalog(Interface):
    pass


class Adapter(Base):

    def __call__(self):
        return getToolByName(self.context, 'portal_user_catalog')
