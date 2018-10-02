# -*- coding: utf-8 -*-
import json
import logging
_logger = logging.getLogger(__name__)
try:
    import urllib3
    urllib3.disable_warnings()
    pool = urllib3.PoolManager()
except:
    _logger.warning("no se ha cargado urllib3")


class Client(object):
    url = "https://api.simpliroute.com/v1/"
    user_token = False
    visit = False
    visits = []

    def __init__(self, token, url=False):
        if url:
            self.url = url
        self.user_token = token

    def set_url(self, url):
        self.url = url

    def _connect(self, params, end_point='routes/visits/', method='POST'):
        url = self.url + end_point
        headers = {
            'authorization': 'TOKEN {0}'.format(self.user_token),
            'content-type': 'application/json',
        }
        print("body %s" % json.dumps(params))
        print(url)
        response = pool.request(method, url, body=json.dumps(params), headers=headers)

        print(response.data)
        return json.loads(response.data)

    def send_visit(self, params):
        self.visit = Visit(self._connect(params))

    def get_visit(self, visit_id):
        end_point = 'routes/visits/{0}'.format(visit_id)
        res = self._connect({}, end_point, method='GET')
        self.visit = Visit(res)

    def get_by_date(self, date):
        end_point = 'routes/visits/?planed_date={0}'.format(date)
        res = self._connect({}, end_point, method='GET')
        for r in res:
            self.visits.append(Visit(res))

    def update_visit(self, params):
        end_point = 'routes/visits/{0}/'.format(self.visit.id)
        self.visit = Visit(self._connect(params, end_point, method="PUT"))

    def send_optimization(self, params):
        url = 'https://optimizator.simpliroute.com/vrp/'
        self.set_url(url)
        resp = self._connect(params, end_point='optimize/sync/', method='POST')
        opt = OptimizationResp(resp)

    def etc(self):
        url = 'https://optimizator.simpliroute.com/etc/sync'


class Visit(object):
    id = None
    order = None
    tracking_id = ""
    status = ""
    title = ""
    address = ""
    latitude = ""
    longitude = ""
    load = None
    load_2 = None
    load_3 = None
    window_start = ""
    window_end = ""
    window_start_2 = ""
    window_end_2 = ""
    duration = ""
    contact_name = ""
    contact_phone = ""
    contact_email = ""
    reference = ""
    notes = ""
    skills_required = []
    skills_optional = []
    planned_date = ""
    route = None
    route_estimated_time_start = None
    estimated_time_arrival = None
    estimated_time_departure = None
    checkin_time = None
    checkout_time = None
    checkout_latitude = None
    checkout_longitude = None
    checkout_comment = ""
    checkout_observation = None
    signature = None
    pictures = []
    created = ""
    modified = ""
    eta_predicted = ""
    eta_current = ""
    driver = None
    vehicle = None
    priority = False
    sms_enabled = False
    has_alert = False
    priority_level = None

    def __init__(self, params):
        self.from_response(params)

    def from_response(self, params):
        for key, par in params.items():
            setattr(self, key, par)


class Tour(object):
    nodes = []

    def __init__(self, params):
        for n in params:
            node = Node(n)
            self.nodes.append(node)


class Vehicle(object):

    ident = "Vehicle 1"
    location_start = {
        "ident": "warehouse B",
        "lat": -33.4233926,
        "lon": -70.6104996
    }
    location_end = {
        "ident": "warehouse C",
        "lat": -33.345523,
        "lon": -70.456992
    }
    capacity = 3500
    capacity_2 = 3500
    capacity_3 = 3500
    shift_start = "09:00"
    shift_end = "18:00"
    skills = ["north-east", "electricity", "cold"]
    refill = 30
    tours = []

    def __init__(self, params):
        for key, p in params.items():
            setattr(self, key, p)


class Optimization(object):
    vehicles = []
    nodes = []
    balance = True
    all_vehicles = False
    join = True
    open_ended = False
    single_tour = True
    fmv = 1.0

    def __init__(self, params):
        for v in params['vehicles']:
            vehicle = Vehicle(v)
            self.vehicles.append(vehicle)
        for n in params['nodes']:
            node = Node(n)
            self.nodes.append(node)
        self.balance = params.get('balance')
        self.all_vehicles = params.get('all_vehicles')
        self.join = params.get('join')
        self.open_ended = params.get('open_ended')
        self.single_tour = params.get('single_tour')
        self.fmv = params.get('fmv')


class OptimizationResp(Optimization):
    tours = []

    def __init__(self, params):
        for t in params:
            tour = Tour(t)
            self.tours.append(tour)


class Node(object):
    ident = ""
    lat = None
    lon = None
    load = None
    load_2 = None
    load_2 = None
    window_start = ""
    window_end = ""
    window_start_2 = ""
    window_end_2 = ""
    duration = None
    skills_required = []
    skills_optional = []
    priority_level = None

    def __init__(self, params):
        for key, p in params.items():
            setattr(self, key, p)

'''
client = Client(token='52654663d153ce6a76a023eb9a637b434db0f5e5')
params = {
            "order": 1,
            "title": "Dansanti Test1",
            "address": "Parcela 19, culiprán, Melipilla, Chile",
            "latitude": "-33.774290",
            "longitude": "-71.250123",
            "contact_name": "Daniel",
            "contact_phone": "+123413123212",
            "contact_email": "apu@example.com",
            "reference": "invoice_id",
            "notes": "Leave at front door",
            "planned_date": "2018-08-19",
            "window_start": "19:00",
          }
client.send_visit(params)
client.get_visit(client.visit.id)
print(client.visit.id)
opt = {
    "vehicles": [
        {
            "ident": "Vehicle 1",
            "location_start": {
                "ident": "warehouse A",
                "lat": "-33.423392",
                "lon": "-70.610499"
            },
            "location_end": {
                "ident": "warehouse C",
                "lat": "-33.423392",
                "lon": "-70.610499"
            },
            "capacity": "3500",
            "capacity_2": "3500",
            "capacity_3": "3500",
            "shift_start": "9:00",
            "shift_end": "22:00",
            "skills": []
        }
    ],
    "nodes": [
        {
            "ident": "Dansanti Test1",
            "lat": "-33.774290",
            "lon": "-71.250123",
            "window_start": "09:00",
            "window_end": "17:00",
            "window_start_2": "19:00",
            "window_end_2": "22:00",
            "duration": 15
        }
    ],
    "balance": True,
    "all_vehicles": False,
    "join": True,
    "open_ended": False,
    "single_tour": True,
    "fmv": "1.0"

}
client.send_optimization(opt)
'''
