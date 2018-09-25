def createProfile(userId, name, email):
    return {'query': 'mutation{createProfile(gcId: "' + str(userId) + '", name: "' + name + '", email:"' +
                              email + '"){gcID, name, email}}'}

def deleteProfile(userId):
    return {'query': 'mutation{deleteProfile(gcId: "' + str(userId) +'"){gcID, name, email}}'}