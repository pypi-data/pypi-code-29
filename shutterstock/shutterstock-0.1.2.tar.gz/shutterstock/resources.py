from shutterstock.endpoint import EndPoint, EndPointParam, ChoicesParam
from shutterstock.resource import Resource, ResourceObjectMethod, \
    ResourceCollectionMethod


class ImageEndPoint(EndPoint):
    """Endpoint for Shutterstock images"""
    MINIMAL = 'minimal'
    FULL = 'full'
    VIEW_CHOICES = (MINIMAL, FULL, )

    id = EndPointParam(required=True,
                       help_text='Required. The ID of the image.')
    view = ChoicesParam(required=True, default=MINIMAL, choices=VIEW_CHOICES,
                        help_text='Required. Minimal view does not return licensing options, categories, keywords')


class Contributor(Resource):
    LIST = EndPoint('/contributors')
    GET = EndPoint('/contributors/{id}')


class Image(Resource):
    LIST = ImageEndPoint('/images')
    GET = ImageEndPoint('/images/{id}')


class ImageCollectionListEndPoint(EndPoint):
    id = EndPointParam()


class ImageCollection(Resource):
    LIST = ImageCollectionListEndPoint('/images/collections')
    GET = EndPoint('/images/collections/{id}')
    ITEMS = EndPoint('/images/collections/{id}/items')

    @ResourceCollectionMethod(resource=Image, id='id')
    def items(cls, **params):
        response = cls.API.get(cls.ITEMS, **params)
        ids = [item['id'] for item in response['data']]
        return cls.API.get(Image.LIST, id=ids, view=params.get('view', 'minimal'))


class ImageLicense(Resource):
    LIST = EndPoint('/images/licenses')
    DOWNLOAD = EndPoint('/images/licenses/{id}/downloads')
    LICENSE = EndPoint('/images/licenses?subscription_id={subscription_id}', params=['images'])

    @ResourceObjectMethod(id='id')
    def download(cls, **params):
        return cls.API.post(cls.DOWNLOAD, **params)

    @ResourceCollectionMethod(id='id')
    def license(cls, **params):
        return cls.API.post(cls.LICENSE, **params)
    
    
class ImageContributor(Resource):
    GET = EndPoint('/contributors/{contributor_id}')
