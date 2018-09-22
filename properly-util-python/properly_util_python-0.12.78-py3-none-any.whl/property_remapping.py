
from properly_util_python.dynamo_utils import get_dynamo_item
from properly_util_python.dynamo_helper import DynamoHelperBase
from properly_util_python.table_helper import TableHelper
import copy


# Consider: Are there alternate approaches that make the object modelling more consistent or clear?


# This class is used to:
# a) merge user supplied info (stored in an offer) and informationn from the property table into and object that
# represents a current view of a property.
# b) when merging the above, it remaps the property attributes to create a different object shape that is more in line
# with the comparable object itself.

class PropertyRemapping:

    def __init__(self, dynamo_helper: DynamoHelperBase):
        self.dynamo_helper = dynamo_helper
        self.table_helper = TableHelper(dynamo_helper)

    def get_home_from_offer_id(self, offer_id, *args, **kwargs):
        offer_data = {}
        offer_table_name = self.table_helper.get_table_name(TableHelper.OFFER_TABLE_NAME)
        user_home = get_dynamo_item(offer_table_name, offer_id)

        if kwargs.get('send_offer_data'):
            offer_data = copy.deepcopy(user_home)
        if 'userSuppliedInfo' in user_home:
            user_home['userSuppliedInfo']['offerId'] = user_home['id']

        property_table_name = self.table_helper.get_table_name(TableHelper.PROPERTY_TABLE_NAME)
        user_home_more_info = get_dynamo_item(property_table_name, user_home['propertyId'])

        print('\n\nget_home_from_offer_id:', user_home_more_info, '\n\n')

        user_home = user_home.get('userSuppliedInfo', {})

        location = user_home_more_info.get('location', {})
        user_home.update(location)
        user_home_verified = user_home_more_info.get('verifiedInfo', {})
        user_home.update(user_home_verified)

        print('\n\nget_home_from_offer_id user_home:', user_home, '\n\n')

        user_home = PropertyRemapping.dynamo_offer_property_to_comps_mapper(user_home, *args, **kwargs)

        if kwargs.get('send_offer_data'):
            return {
                'offer': offer_data,
                'home': user_home,
            }
        else:
            return user_home

    # This field remapper takes fields as they are used in the user supplied info, and in the location block of the property api
    # (those fields are on the right hand side of the map_dict)
    # if they are found it creates a new key using the name on the left hand side _if_ it is not already present

    @staticmethod
    def dynamo_offer_property_to_comps_mapper(user_home: dict, *args, **kwargs):

        map_dict = {
            'address': 'formattedAddress',
            'googleFormattedAddress': 'formattedAddress',
            'latitude': 'lat',
            'longitude': 'lng',
            # 'bedrooms': 'numBedrooms',
            # 'bathroomsHalf': 'numHalfBaths',
            'livingSpaceSquareMetersAG': 'livingSpaceSquareMeter',
            # 'yrBuilt': 'decadeBuilt',
            # 'yearBuilt': 'decadeBuilt',
        }

        if kwargs.get('show_all_keys'):
            more_keys = {
                'googlePlaceId': 'placeId',
                'googleFormattedAddress': 'formattedAddress',
            }
            map_dict.update(more_keys)
        for k, v in map_dict.items():
            if v in user_home and not user_home.get(k):
                user_home[k] = user_home[v]
                if v not in ['formattedAddress', 'decadeBuilt'] and kwargs.get('pop_extra_keys'):
                    user_home.pop(v, None)

        remove_keys = [k for k in user_home.keys() if k not in map_dict.keys()]

        if kwargs.get('pop_extra_keys'):
            for k in remove_keys:
                user_home.pop(k, None)

        return user_home

