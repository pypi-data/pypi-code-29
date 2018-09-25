def QueryProfile(userId):
    return {'query': 'query{profiles(gcID: "' + str(userId) + '"){name, email, avatar, mobilePhone, officePhone,' +
                 'address{streetAddress,city, province, postalCode, country}}}'}