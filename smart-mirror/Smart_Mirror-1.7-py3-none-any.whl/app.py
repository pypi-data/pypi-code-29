from flask import Flask, render_template, jsonify, request, redirect, url_for
from smart_mirror import app, socketio
from flask_socketio import emit, send
import datetime
from smart_mirror.zomato import Zomato
from smart_mirror.pywit import RecognizeSpeech
import time


@socketio.on('voice_search')
def s_voice_search(message):
    voice_search()

def voice_search():
    text =  RecognizeSpeech('myspeech.wav', 4)
    if not 'entities' in text:
        return
    if 'intent' in text['entities']:
        if len(text['entities']['intent'])>0:
            if 'value' in text['entities']['intent'][0]:
                value = text['entities']['intent'][0]['value']
                if value == 'calendar':
                    socketio.emit('calendar', '', broadcast=True, include_self=False)
                elif value == 'home':
                    socketio.emit('home', '', broadcast=True, include_self=False)
                elif value == 'homepage':
                    socketio.emit('home', '', broadcast=True, include_self=False)
                elif value == 'clock':
                    socketio.emit('time', '', broadcast=True, include_self=False)
                elif value == 'youtube':
                    socketio.emit('yoututbe', '', broadcast=True, include_self=False)
                elif value == 'news':
                    socketio.emit('news', '', broadcast=True, include_self=False)
                elif value == 'route':
                    if 'train' in text['entities']:
                        trainNo = text['entities']['train'][0]['value']
                        socketio.emit('train_route', "/"+str(trainNo), broadcast=True, include_self=False)
                    else:
                        socketio.emit('train_route', '/12480', broadcast=True, include_self=False)
                elif value == 'weather':
                    if 'location' in text['entities']:
                        location = text['entities']['location'][0]['value']
                        socketio.emit('weather', "/"+str(location), broadcast=True, include_self=False)
                    else:
                        socketio.emit('home', '', broadcast=True, include_self=False)

    if 'Zomato_category' in text['entities']:
        if len(text['entities']['Zomato_category'])>0:
            if 'value' in text['entities']['Zomato_category'][0]:
                value = text['entities']['Zomato_category'][0]['value']
                category_id = zomato.getCategoryNo(value)
                if category_id:
                    socketio.emit('zomato', '/categories/' + str(category_id), broadcast=True, include_self=False)
    if 'Zomato_cuisines' in text['entities']:
        if len(text['entities']['Zomato_cuisines'])>0:
            if 'value' in text['entities']['Zomato_cuisines'][0]:
                value = text['entities']['Zomato_cuisines'][0]['value']
                cuisine_id = zomato.getCuisineNo(value)
                if cuisine_id:
                    socketio.emit('zomato', '/cuisines/' + str(cuisine_id), broadcast=True, include_self=False)
    if 'Destination' in text['entities']:
        if len(text['entities']['Destination'])>0:
            if 'value' in text['entities']['Destination'][0]:
                destination = text['entities']['Destination'][0]['value']
                if 'Source' in text['entities']:
                    source = text['entities']['Source'][0]['value']
                elif 'location' in text['entities']:
                    source = text['entities']['location'][0]['value']
                else:
                    source = getLocation()
                socketio.emit('railway', '?source_station='+ source +'&destination_station='+destination+'&journey_date=2018-09-21', broadcast=True, include_self=False)
    if 'Source' in text['entities']:
        print('train enq')
        if len(text['entities']['Source'])>0:
            if 'value' in text['entities']['Source'][0]:
                source = text['entities']['Source'][0]['value']
                if 'Destination' in text['entities']:
                    destination = text['entities']['Destination'][0]['value']
                elif 'location' in text['entities']:
                    destination = text['entities']['location'][0]['value']
                else:
                    destination = getLocation()
                if 'datetime' in text['entities']:
                    dateTime = text['entities']['datetime'][0]['value']
                    dateTime = dateTime[0:10]
                else:
                    dateTime = '2018-09-21'
                print(dateTime)
                socketio.emit('railway', '?source_station='+ source +'&destination_station='+destination+'&journey_date=' + dateTime, broadcast=True, include_self=False)
    if 'intent' in text['entities']:
        if len(text['entities']['intent'])>0:
            if 'value' in text['entities']['intent'][0]:
                if value == 'ticket':
                    socketio.emit('railway', '', broadcast=True, include_self=False)
                elif value == 'railway':
                    socketio.emit('railway', '', broadcast=True, include_self=False)
                




@socketio.on('railway')
def s_railway(message):
    emit('railway', '', broadcast=True, include_self=False)

@socketio.on('train_route')
def s_train_route(message):
    emit('train_route', '/12480', broadcast=True, include_self=False)

@socketio.on('home')
def s_home(message):
    emit('home', '', broadcast=True, include_self=False)

@socketio.on('zomato')
def s_zomato(message):
    emit('zomato', '', broadcast=True, include_self=False)

@socketio.on('news')
def s_news(message):
    emit('news', '', broadcast=True, include_self=False)

@socketio.on('youtube')
def s_youtube(message):
    emit('youtube', '', broadcast=True, include_self=False)

@socketio.on('calendar')
def s_calendar(message):
    emit('calendar', '', broadcast=True, include_self=False)

@socketio.on('toggleLED')
def s_toggleLED(message):
    emit('toggleLED', '', broadcast=True, include_self=False)

@socketio.on('time')
def s_time(message):
    emit('time', '', broadcast=True, include_self=False)

@socketio.on('weather')
def s_weather(message):
    emit('weather', '/Pune', broadcast=True, include_self=False)


@app.route("/toggleLED")
def toggleLight():
    socketio.emit('toggleLED', '', broadcast=True)
    return ''

@app.route("/remote")
def remote():
    return render_template('remoteControl.html')

@app.route("/template")
def template():
    return render_template('template.html')


@app.route("/youtube")
def youtube():
    return """
    <iframe src="https://www.youtube.com/embed/3xokKYrHibc"  style="position:fixed; top:0px; left:0px; bottom:0px; right:0px; width:100%; height:100%; border:none; margin:0; padding:0; overflow:hidden; z-index:999999;" allowfullscreen>
    </iframe>
    """

@app.route("/calendar")
def getCalendar():
    return render_template('calendar.html')

@app.route("/news", methods=['GET'])
def getNews():
    from gnewsclient import gnewsclient
    client = gnewsclient()
    
    country = request.args.get('country')
    if(country):
        client.edition = country

    language = request.args.get('language')
    if(language):
        client.language = language

    topic = request.args.get('topic')
    if(topic):
        client.topic = topic

    # client.loaction = 'delhi'
    query = request.args.get('query')
    if(query):
        client.query = query

    return render_template('news.html', articles=client.get_news(), client=client, country=country, language=language, topic=topic)
    
@app.route("/railway")
def getRailway():

    source_station = request.args.get('source_station')
    destination_station = request.args.get('destination_station')
    journey_date = request.args.get('journey_date')
    if journey_date:
        journey_date = datetime.datetime.strptime(journey_date, "%Y-%m-%d").strftime('%d-%m-%Y')

    if(source_station and destination_station and journey_date):
        # API Call
        import requests

        # Source Station Name to Code
        url = 'https://api.railwayapi.com/v2/suggest-station/name/' + source_station + '/apikey/ep6m37hkms/'
        response = requests.get(url).json()
        if not validStation(response):
            url = 'https://api.railwayapi.com/v2/code-to-name/code/' + source_station + '/apikey/ep6m37hkms/'
            response = requests.get(url).json()
            if not validStation(response):
                return 'Invalid Source Station Name'
            for station in response['stations']:
                if station['code'].lower() == source_station.lower():
                    source_station = station['code']
                    break
            # source_station = station['code'] for station in response['stations'] if station['code'].lower() == source_station.lower()
            
            if not source_station:
                source_station = response['stations'][0]['code']
        else:    
            source_station = response['stations'][0]['code']
        
        # Destination Station Name to Code
        url = 'https://api.railwayapi.com/v2/suggest-station/name/' + destination_station + '/apikey/ep6m37hkms/'
        response = requests.get(url).json()
        if not validStation(response):
            url = 'https://api.railwayapi.com/v2/code-to-name/code/' + destination_station + '/apikey/ep6m37hkms/'
            response = requests.get(url).json()
            if not validStation(response):
                return 'Invalid Destination Station Name'

            for station in response['stations']:
                if station['code'].lower() == destination_station.lower():
                    destination_station = station['code']
                    break
            
            if not destination_station:
                destination_station = response['stations'][0]['code']
        else:
            destination_station = response['stations'][0]['code']
        
        return redirect(url_for('getTrainsList', source=source_station, destination=destination_station, journey_date=journey_date))
    
    return render_template('railway.html')

def validStation(response):
    if 'stations' not in response:
        return False
    if not len(response['stations'])>0:
        return False
    if not 'code' in response['stations'][0]:
        return False
    return True

@app.route("/trains_list/<source>/<destination>/<journey_date>")
def getTrainsList(source, destination, journey_date):
    # print("Source: " + source)
    # print("Destination: " + destination)
    # print("Journey_date: " + journey_date)

    # # API Call
    import requests
    url = 'https://api.railwayapi.com/v2/between/source/'+source+'/dest/'+destination+'/date/'+journey_date+'/apikey/ep6m37hkms/'
    response = requests.get(url).json()

    list = response['trains']
    # print(list)
    # list = [{'src_departure_time': '14:20', 'number': '12587', 'name': 'AMAR NATH EXP', 'dest_arrival_time': '12:35', 'travel_time': '22:15', 'days': [{'runs': 'Y', 'code': 'MON'}, {'runs': 'N', 'code': 'TUE'}, {'runs': 'N', 'code': 'WED'}, {'runs': 'N', 'code': 'THU'}, {'runs': 'N', 'code': 'FRI'}, {'runs': 'N', 'code': 'SAT'}, {'runs': 'N', 'code': 'SUN'}], 'to_station': {'lat': 32.7060401, 'lng': 74.8799925, 'name': 'JAMMU TAWI', 'code': 'JAT'}, 'from_station': {'lat': 26.7600217, 'lng': 83.3668129, 'name': 'GORAKHPUR', 'code': 'GKP'}, 'classes': [{'code': '1A', 'name': 'FIRST AC'}, {'code': 'SL', 'name': 'SLEEPER CLASS'}, {'code': '3E', 'name': '3rd AC ECONOMY'}, {'code': '2S', 'name': 'SECOND SEATING'}, {'code': '3A', 'name': 'THIRD AC'}, {'code': 'FC', 'name': 'FIRST CLASS'}, {'code': 'CC', 'name': 'AC CHAIR CAR'}, {'code': '2A', 'name': 'SECOND AC'}]}, {'src_departure_time': '14:40', 'number': '15655', 'name': 'KYQ - SVDK EXPRESS', 'dest_arrival_time': '13:40', 'travel_time': '23:00', 'days': [{'runs': 'Y', 'code': 'MON'}, {'runs': 'N', 'code': 'TUE'}, {'runs': 'N', 'code': 'WED'}, {'runs': 'N', 'code': 'THU'}, {'runs': 'N', 'code': 'FRI'}, {'runs': 'N', 'code': 'SAT'}, {'runs': 'N', 'code': 'SUN'}], 'to_station': {'lat': 32.7060401, 'lng': 74.8799925, 'name': 'JAMMU TAWI', 'code': 'JAT'}, 'from_station': {'lat': 26.7600217, 'lng': 83.3668129, 'name': 'GORAKHPUR', 'code': 'GKP'}, 'classes': [{'code': '1A', 'name': 'FIRST AC'}, {'code': 'SL', 'name': 'SLEEPER CLASS'}, {'code': '3E', 'name': '3rd AC ECONOMY'}, {'code': '2S', 'name': 'SECOND SEATING'}, {'code': '3A', 'name': 'THIRD AC'}, {'code': 'FC', 'name': 'FIRST CLASS'}, {'code': 'CC', 'name': 'AC CHAIR CAR'}, {'code':'2A', 'name': 'SECOND AC'}]}]
    return render_template('trains_list.html', trains_list=list, source=source, destination=destination, journey_date=journey_date)

@app.route("/train_route/<int:train_no>")
def getTrainRoute(train_no):
    # API Call
    import requests
    url = 'https://api.railwayapi.com/v2/route/train/'+str(train_no)+'/apikey/ep6m37hkms/'
    response = requests.get(url).json()

    train = response['train']
    # train = {'name': 'SURYANAGARI EXP', 'number': '12480', 'classes': [{'name': 'SECOND AC', 'available': 'Y', 'code': '2A'}, {'name': 'FIRST CLASS', 'available': 'N', 'code': 'FC'}, {'name': 'SECOND SEATING', 'available': 'N', 'code': '2S'}, {'name': '3rd AC ECONOMY', 'available': 'N', 'code': '3E'}, {'name': 'FIRST AC', 'available': 'Y', 'code': '1A'}, {'name': 'THIRD AC', 'available': 'Y', 'code': '3A'}, {'name': 'AC CHAIR CAR','available': 'N', 'code': 'CC'}, {'name': 'SLEEPER CLASS', 'available': 'Y', 'code': 'SL'}], 'days': [{'code': 'MON', 'runs': 'Y'}, {'code': 'TUE', 'runs': 'Y'}, {'code': 'WED', 'runs': 'Y'}, {'code': 'THU', 'runs': 'Y'}, {'code': 'FRI', 'runs': 'Y'}, {'code': 'SAT', 'runs': 'Y'}, {'code': 'SUN', 'runs': 'Y'}]}
    # print(train)
    route = response['route']
    # route = [{'schdep': '13:30', 'distance': 0.0, 'station': {'lng': 72.8412300201636, 'name': 'BANDRA TERMINUS', 'code': 'BDTS', 'lat': 19.0635016}, 'scharr': 'SOURCE', 'halt': -1, 'day': 1, 'no': 1}, {'schdep': '14:00', 'distance': 18.0, 'station': {'lng': 72.8568773, 'name': 'BORIVALI', 'code': 'BVI', 'lat': 19.2287385}, 'scharr': '13:57', 'halt': 3, 'day': 1, 'no': 2}, {'schdep': '17:27', 'distance': 251.0, 'station': {'lng': 72.8081281, 'name': 'SURAT', 'code': 'ST', 'lat': 21.1864607}, 'scharr': '17:22', 'halt': 5, 'day': 1, 'no': 3}, {'schdep': '18:05', 'distance': 301.0, 'station': {'lng': 72.9945103, 'name': 'ANKLESHWAR JN', 'code': 'AKV', 'lat': 21.6293206}, 'scharr': '18:03', 'halt': 2, 'day': 1, 'no': 4}, {'schdep': '19:15', 'distance': 380.0, 'station': {'lng': 73.1957373, 'name': 'VADODARA JN', 'code': 'BRC', 'lat': 22.297076}, 'scharr': '19:10', 'halt': 5, 'day': 1, 'no': 5}, {'schdep': '19:45', 'distance': 416.0, 'station': {'lng': 72.9625629, 'name': 'ANAND JN', 'code': 'ANND', 'lat': 22.5584995}, 'scharr': '19:44', 'halt': 1, 'day': 1, 'no': 6}, {'schdep': '21:35', 'distance': 480.0, 'station': {'lng': 72.5797068, 'name': 'AHMEDABAD JN', 'code': 'ADI', 'lat': 23.0216238}, 'scharr': '21:15', 'halt': 20, 'day': 1, 'no': 7}, {'schdep': '22:44', 'distance': 567.0, 'station': {'lng': 72.5, 'name': 'MAHESANA JN', 'code': 'MSH', 'lat': 23.666667}, 'scharr': '22:42', 'halt': 2, 'day': 1, 'no': 8}, {'schdep': '00:33', 'distance': 632.0, 'station': {'lng': 72.4366375, 'name': 'PALANPUR JN', 'code': 'PNU', 'lat': 24.1709794}, 'scharr': '00:30', 'halt': 3, 'day': 2, 'no': 9}, {'schdep': '01:32', 'distance': 685.0, 'station': {'lng': 72.7820384, 'name': 'ABU ROAD', 'code': 'ABR', 'lat': 24.4828256}, 'scharr': '01:22', 'halt': 10, 'day': 2, 'no': 10}, {'schdep': '02:58', 'distance': 767.0, 'station': {'lng': 73.1530272, 'name': 'JAWAI BANDH', 'code': 'JWB', 'lat': 25.1130774}, 'scharr': '02:56', 'halt': 2, 'day': 2, 'no': 11}, {'schdep': '03:25', 'distance': 783.0, 'station': {'lng': 73.2354341, 'name': 'FALNA', 'code': 'FA', 'lat': 25.2335457}, 'scharr': '03:23', 'halt': 2, 'day': 2, 'no':12}, {'schdep': '03:40', 'distance': 798.0, 'station': {'lng': 87.267956, 'name': 'RANI', 'code': 'RANI','lat': 26.4190285}, 'scharr': '03:38', 'halt': 2, 'day': 2, 'no': 13}, {'schdep': '04:42', 'distance': 850.0, 'station': {'lng': 73.6097336, 'name': 'MARWAR JN', 'code': 'MJ', 'lat': 25.7259059}, 'scharr': '04:40', 'halt': 2, 'day': 2, 'no': 14}, {'schdep': '05:13', 'distance': 880.0, 'station': {'lng': 73.3277411, 'name': 'PALI MARWAR', 'code': 'PMY', 'lat': 25.7912871}, 'scharr': '05:08', 'halt': 5, 'day': 2, 'no': 15}, {'schdep': '05:46', 'distance': 922.0, 'station': {'lng': 10.030189, 'name': 'LUNI JN', 'code': 'LUNI','lat': 44.0778272}, 'scharr': '05:43', 'halt': 3, 'day': 2, 'no': 16}, {'schdep': 'DEST', 'distance': 953.0, 'station': {'lng': 73.0351433, 'name': 'JODHPUR JN', 'code': 'JU', 'lat': 26.2967719}, 'scharr': '06:30', 'halt': -1, 'day': 2, 'no': 17}]
    # print(route)
    return render_template('train_route.html', train=train, route=route)

@app.route("/time")
def showTime():
    return render_template('snippet_time.html')

@app.route("/weather/<cityName>")
def getWeathe(cityName):
    from weather import Weather, Unit
    weather = Weather(unit=Unit.CELSIUS)
    # location = weather.lookup_by_location(cityName)
    location = weather.lookup_by_location(cityName)
    # print(location.print_obj)
    # print(condition.text)
    # return jsonify(location.print_obj)
    # location.astronomy
    # print("Temp:", location.item['description'])
    # print("Condition:", location.condition.text)
    # print(location.forecast[0].text)

    if(location):
        weatherDetails = {
            "City": location.location.city,
            "State": location.location.region,
            "Country": location.location.country,
            "Sunrise": location.astronomy['sunrise'],
            "Sunset": location.astronomy['sunset'],
            "Humidity": location.atmosphere['humidity'],
            "Temp": location.condition.temp,
            "Condition": location.condition.text
        }
        return render_template('snippet_weather.html', weather=weatherDetails, cityName=cityName)
    return ""



@app.route("/")
def hello():
    return redirect(url_for('getWeather', cityName = getLocation()))

def getLocation():
    import geocoder
    g = geocoder.ip('me')
    return g.response.json()['city']

@app.route("/home")
def home():
    return render_template('home.html')    

zomato = Zomato()

def setZomatoParameters():
    your_location = request.args.get('your_location')
    if not your_location:
        your_location = getLocation()
        print("Location: " + str(your_location))
    zomato.setLocation(your_location)
    
    search_query = request.args.get('search_query')
    zomato.setSearchQuery(search_query)


def getZomato(restaurants=None):
    if not restaurants:
        restaurants = zomato.getBestRestaurants()
    return render_template('zomato.html', your_location=zomato.getLocation()['title'], search_query=zomato.getSearchQuery(), categories=zomato.getCategories(), establishments=zomato.getEstablishments(), cuisines=zomato.getCuisines(), collections=zomato.getCollections(), restaurants=restaurants)

@app.route("/zomato")
def showZomato():
    setZomatoParameters()
    return getZomato()

@app.route("/zomato/categories/<int:category_id>")
def showZomatoCategories(category_id):
    return redirect(url_for('showZomatoCategoriesPageNo', category_id=category_id, pageNo=1))
@app.route("/zomato/categories/<int:category_id>/<int:pageNo>")
def showZomatoCategoriesPageNo(category_id, pageNo):
    setZomatoParameters()
    return getZomato(restaurants=zomato.getRestaurants_by_category(category_id, pageNo-1))

@app.route("/zomato/establishments/<int:establishment_id>")
def showZomatoEstablishments(establishment_id):
    return redirect(url_for('showZomatoEstablishmentsPageNo', establishment_id=establishment_id, pageNo=1))
@app.route("/zomato/establishments/<int:establishment_id>/<int:pageNo>")
def showZomatoEstablishmentsPageNo(establishment_id, pageNo):
    setZomatoParameters()
    return getZomato(restaurants=zomato.getRestaurants_by_establishment(establishment_id, pageNo-1))

@app.route("/zomato/cuisines/<int:cuisine_id>")
def showZomatoCuisines(cuisine_id):
    return redirect(url_for('showZomatoCuisinesPageNo', cuisine_id=cuisine_id, pageNo=1))
@app.route("/zomato/cuisines/<int:cuisine_id>/<int:pageNo>")
def showZomatoCuisinesPageNo(cuisine_id, pageNo):
    setZomatoParameters()
    return getZomato(restaurants=zomato.getRestaurants_by_cuisine(cuisine_id, pageNo-1))

@app.route("/zomato/collections/<int:collection_id>")
def showZomatoCollections(collection_id):
    return redirect(url_for('showZomatoCollectionsPageNo', collection_id=collection_id, pageNo=1))
@app.route("/zomato/collections/<int:collection_id>/<int:pageNo>")
def showZomatoCollectionsPageNo(collection_id, pageNo):
    setZomatoParameters()
    return getZomato(restaurants=zomato.getRestaurants_by_collection(collection_id, pageNo-1))


@app.route("/zomato/all")
def showAllZomato():
    return redirect(url_for('showAllZomatoPageNo', pageNo=1))
@app.route("/zomato/all/<int:pageNo>")
def showAllZomatoPageNo(pageNo):
    setZomatoParameters()
    return getZomato(restaurants=zomato.getRestaurants(pageNo-1))

@app.route("/home/<cityName>")
def getWeather(cityName):
    # import geocoder
    # g = geocoder.ip('me')
    # print("Location:", end="")
    # print(g.latlng)

    from weather import Weather, Unit
    weather = Weather(unit=Unit.CELSIUS)
    # location = weather.lookup_by_location(cityName)
    location = weather.lookup_by_location(cityName)
    # print(location.print_obj)
    # print(condition.text)
    # return jsonify(location.print_obj)
    # location.astronomy
    # print("Temp:", location.item['description'])
    # print("Condition:", location.condition.text)
    # print(location.forecast[0].text)

    if(location):
        weatherDetails = {
            "City": location.location.city,
            "State": location.location.region,
            "Country": location.location.country,
            "Sunrise": location.astronomy['sunrise'],
            "Sunset": location.astronomy['sunset'],
            "Humidity": location.atmosphere['humidity'],
            "Temp": location.condition.temp,
            "Condition": location.condition.text
        }
        return render_template('home.html', weather=weatherDetails, cityName=cityName)
    return ""
    # return jsonify(location.print_obj)
    # return location.forecast

# def main():
#     app.run(port=5000)