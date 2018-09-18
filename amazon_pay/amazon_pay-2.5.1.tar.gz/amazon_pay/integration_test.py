import json

from amazon_pay.client import AmazonPayClient

#client = AmazonPayClient(
#        mws_access_key='AKIAJIUGYOGHT2ONMCOQ',
#        mws_secret_key='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',
#       merchant_id='A2GWANJA6L1J87',
#        region='na',
#        currency_code='USD',
#        sandbox=True)

client = AmazonPayClient(
        mws_access_key='AKIAIPYPIWESY3GLTOYQ',
        mws_secret_key='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',
        merchant_id='A3URCZVLDMDI45',
        region='na',
        currency_code='USD',
        sandbox=True)


supplementary_data   = '{"AirlineMetaData" : {"version": 1.0, "airlineCode": "PAX", "flightDate": "2018-03-24T20:29:19.22Z", "departureAirport": "CDG", "destinationAirport": "LUX", "bookedLastTime": -1, "classOfTravel": "F", "passengers": {"numberOfPassengers": 4, "numberOfChildren": 1, "numberOfInfants": 1 }}, "AccommodationMetaData": {"version": 1.0, "startDate": "2018-03-24T20:29:19.22Z", "endDate": "2018-03-24T20:29:19.22Z", "lengthOfStay": 5, "numberOfGuests": 4, "class": "Standard", "starRating": 5, "bookedLastTime": -1 }, "OrderMetaData": {"version": 1.0, "numberOfItems": 3, "type": "Digital" }, "BuyerMetaData": {"version" : 1.0, "isFirstTimeCustomer" : true, "numberOfPastPurchases" : 2, "numberOfDisputedPurchases" : 3, "hasOpenDispute" : true, "riskScore" : 0.75 }}';
order_reference_id = 'S01-3946615-0638408'

ret = client.set_order_reference_details(
    amazon_order_reference_id=order_reference_id,
    order_total='1.00',
    seller_note='My seller note.',
    seller_order_id='MY_UNIQUE_ORDER_ID',
    store_name='My store name.',
    custom_information='My custom information.',
    supplementary_data=supplementary_data)
print(ret.to_dict())
print(ret.to_json()) # to_xml and to_dict are also valid

#ret = client.set_order_attributes(
 #   amazon_order_reference_id=order_reference_id,
  #  amount='1',
   # currency_code='USD',
    #seller_note='My seller note.',
    #seller_order_id='MY_UNIQUE_ORDER_ID',
    #supplementary_data=supplementary_data,
    #mws_auth_token='amzn.mws.d6ac8f2d-6a5f-b06a-bc12-1d0dbf4ca63d')
#print(ret.to_json())
#pretty_soa = json.dumps(
 #       json.loads(
  #          ret.to_json()),
   #     indent=4)
#print(pretty_soa)
ret1 = client.get_order_reference_details(amazon_order_reference_id=order_reference_id)
print(ret1.to_dict())

ret2 = client.confirm_order_reference(amazon_order_reference_id=order_reference_id)
print(ret2.to_json())

ret = client.set_order_attributes(
    amazon_order_reference_id=order_reference_id,
    store_name='My store name.',
    custom_information='My custom information.')
print(ret.to_json())

