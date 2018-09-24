import requests

url = "https://developers.zomato.com/api/v2.1/"
headers = {
        'Content-Type': "application/json",
        'user-key': "72f8dd4f406bf491d16e078e8f5817f9",
        # 'user-key': "88180b3cbab730d79641d19dd4931627",
    }


class Zomato:
    zomato_location = ""
    user_location = ""
    search_query = ""

    def setLocation(self, location):
        type(self).user_location = location
        if type(self).user_location:
            response = requests.request("GET", url + "locations?query=" + type(self).user_location, headers=headers)
            response = response.json()
            # response = {}
            if 'location_suggestions' not in response:
                type(self).zomato_location = {"entity_type": "subzone", "entity_id": 3410, "title": "Kothrud, Pune", "latitude": 18.50634, "longitude": 73.806706, "city_id": 5, "city_name": "Pune", "country_id": 1, "country_name": "India"}
                return
            if not len(response['location_suggestions'])>0:
                self.location_suggestions = {"entity_type": "subzone", "entity_id": 3410, "title": "Kothrud, Pune", "latitude": 18.50634, "longitude": 73.806706, "city_id": 5, "city_name": "Pune", "country_id": 1, "country_name": "India"}
                return
            type(self).zomato_location = response['location_suggestions'][0]
            return
        else:
            type(self).zomato_location = {"entity_type": "subzone", "entity_id": 3410, "title": "Kothrud, Pune", "latitude": 18.50634, "longitude": 73.806706, "city_id": 5, "city_name": "Pune", "country_id": 1, "country_name": "India"}
        return

    def getLocation(self):
        if not type(self).zomato_location:
            self.setLocation(location="")
        return type(self).zomato_location
    
    def setSearchQuery(self, search_query):
        type(self).serch_query = search_query
    def getSearchQuery(self):
        if not type(self).search_query:
            return ""
        return type(self).search_query

    def getCategories(self):
        # response = requests.request("GET", url + "categories", headers=headers)
        # categories = response.json()['categories']
        categories = [{'categories': {'id': 1, 'name': 'Delivery'}}, {'categories': {'id': 2, 'name': 'Dine-out'}}, {'categories': {'id': 3, 'name': 'Nightlife'}}, {'categories': {'id': 4, 'name': 'Catching-up'}}, {'categories': {'id': 5, 'name': 'Takeaway'}}, {'categories': {'id': 6, 'name': 'Cafes'}}, {'categories': {'id': 7, 'name': 'Daily Menus'}}, {'categories': {'id': 8, 'name': 'Breakfast'}}, {'categories': {'id': 9, 'name': 'Lunch'}}, {'categories': {'id': 10, 'name': 'Dinner'}}, {'categories': {'id': 11, 'name': 'Pubs & Bars'}}, {'categories': {'id': 13, 'name': 'Pocket Friendly Delivery'}}, {'categories': {'id': 14, 'name':'Clubs & Lounges'}}]
        return categories

    def getCategoryNo(self, name):
        for each in self.getCategories():
            if each['categories']['name'] == name:
                return each['categories']['id']
        return ""

    def getEstablishments(self):
        # querystring = {"city_id":self.getLocation()['city_id']}
        # response = requests.request("GET", url + "establishments", headers=headers, params=querystring)
        # establishments = response.json()['establishments']
        establishments = [{"establishment":{"id":16,"name":"Casual Dining"}},{"establishment":{"id":7,"name":"Bar"}},{"establishment":{"id":21,"name":"Quick Bites"}},{"establishment":{"id":41,"name":"Beverage Shop"}},{"establishment":{"id":23,"name":"Dessert Parlour"}},{"establishment":{"id":1,"name":"Caf\u00e9"}},{"establishment":{"id":31,"name":"Bakery"}},{"establishment":{"id":6,"name":"Pub"}},{"establishment":{"id":81,"name":"Food Truck"}},{"establishment":{"id":5,"name":"Lounge"}},{"establishment":{"id":291,"name":"Sweet Shop"}},{"establishment":{"id":20,"name":"Food Court"}},{"establishment":{"id":4,"name":"Kiosk"}},{"establishment":{"id":18,"name":"Fine Dining"}},{"establishment":{"id":303,"name":"Irani Cafe"}}]
        return establishments
    
    def getCuisines(self):
        # querystring = {"city_id":self.getLocation()['city_id']}
        # response = requests.request("GET", url + "cuisines", headers=headers, params=querystring)
        # cuisines = response.json()['cuisines']
        cuisines = [{"cuisine":{"cuisine_id":3,"cuisine_name":"Asian"}},{"cuisine":{"cuisine_id":5,"cuisine_name":"Bakery"}},{"cuisine":{"cuisine_id":270,"cuisine_name":"Beverages"}},{"cuisine":{"cuisine_id":30,"cuisine_name":"Cafe"}},{"cuisine":{"cuisine_id":25,"cuisine_name":"Chinese"}},{"cuisine":{"cuisine_id":35,"cuisine_name":"Continental"}},{"cuisine":{"cuisine_id":100,"cuisine_name":"Desserts"}},{"cuisine":{"cuisine_id":40,"cuisine_name":"Fast Food"}},{"cuisine":{"cuisine_id":271,"cuisine_name":"Finger Food"}},{"cuisine":{"cuisine_id":143,"cuisine_name":"Healthy Food"}},{"cuisine":{"cuisine_id":233,"cuisine_name":"Ice Cream"}},{"cuisine":{"cuisine_id":55,"cuisine_name":"Italian"}},{"cuisine":{"cuisine_id":73,"cuisine_name":"Mexican"}},{"cuisine":{"cuisine_id":1015,"cuisine_name":"Mithai"}},{"cuisine":{"cuisine_id":75,"cuisine_name":"Mughlai"}},{"cuisine":{"cuisine_id":50,"cuisine_name":"North Indian"}},{"cuisine":{"cuisine_id":82,"cuisine_name":"Pizza"}},{"cuisine":{"cuisine_id":88,"cuisine_name":"Rajasthani"}},{"cuisine":{"cuisine_id":1023,"cuisine_name":"Rolls"}},{"cuisine":{"cuisine_id":85,"cuisine_name":"South Indian"}},{"cuisine":{"cuisine_id":90,"cuisine_name":"Street Food"}},{"cuisine":{"cuisine_id":95,"cuisine_name":"Thai"}}]
        return cuisines
    def getCuisineNo(self, name):
        for each in self.getCuisines():
            if each['cuisine']['cuisine_name'] == name:
                return each['cuisine']['cuisine_id']
        return ""

    def getCollections(self):
        querystring = {"city_id":self.getLocation()['city_id']}
        response = requests.request("GET", url + "collections", headers=headers, params=querystring)
        collections = response.json()['collections']
        # print(collections)
        return collections

    def getBestRestaurants(self):
        querystring = {"entity_id":self.getLocation()['entity_id'],"entity_type":self.getLocation()['entity_type']}
        response = requests.request("GET", url + "location_details", headers=headers, params=querystring)
        restaurants = response.json()['best_rated_restaurant']
        return restaurants

    def getRestaurants(self, startFrom=0):
        querystring = {"entity_id":self.getLocation()['entity_id'],"entity_type":self.getLocation()['entity_type'], "q":type(self).search_query, "start":20*startFrom}
        response = requests.request("GET", url + "search", headers=headers, params=querystring)
        restaurants = response.json()['restaurants']
        return restaurants
    
    def getRestaurants_by_category(self, category, startFrom=0):
        querystring = {"entity_id":self.getLocation()['entity_id'],"entity_type":self.getLocation()['entity_type'], "q":type(self).search_query, "category":category, "start":20*startFrom}
        print(querystring)
        response = requests.request("GET", url + "search", headers=headers, params=querystring)
        restaurants = response.json()['restaurants']
        print(restaurants)
        return restaurants
    
    def getRestaurants_by_establishment(self, establishment, startFrom=0):
        querystring = {"entity_id":self.getLocation()['entity_id'],"entity_type":self.getLocation()['entity_type'], "q":type(self).search_query, "establishment_type":establishment, "start":20*startFrom}
        print(querystring)
        response = requests.request("GET", url + "search", headers=headers, params=querystring)
        restaurants = response.json()['restaurants']
        return restaurants
    
    def getRestaurants_by_cuisine(self, cuisine, startFrom=0):
        querystring = {"entity_id":self.getLocation()['entity_id'],"entity_type":self.getLocation()['entity_type'], "q":type(self).search_query, "cuisines":cuisine, "start":20*startFrom}
        print(querystring)
        response = requests.request("GET", url + "search", headers=headers, params=querystring)
        restaurants = response.json()['restaurants']
        return restaurants
    
    def getRestaurants_by_collection(self, collection, startFrom=0):
        querystring = {"entity_id":self.getLocation()['entity_id'],"entity_type":self.getLocation()['entity_type'], "q":type(self).search_query, "collection_id":collection, "start":20*startFrom}
        print(querystring)
        response = requests.request("GET", url + "search", headers=headers, params=querystring)
        restaurants = response.json()['restaurants']
        return restaurants