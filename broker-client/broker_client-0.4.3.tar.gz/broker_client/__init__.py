# -*- coding: utf-8 -*-

import requests
import socket
import json
import logging
import time
from threading import Timer

from .economy import *

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

reputations_dict = {}

def locate(query={"@type": "*"}, broker_url="http://localhost:4000/broker"):
    locate_url = broker_url + "/locate-requests"
    try:
        logging.info("Locating query %s" % query)
        response = requests.post(locate_url,
                                data=json.dumps(query), 
                                headers={'Content-Type': 'application/json'})
        services = response.json()
        logging.info("Located services are %s" % list(map(lambda s: s["host"] + s["@id"], services)))
        return services
    except Exception as e:
        print("The locate request did not work")

def register(sd_filename="service-description.jsonld",
             replace_localhost_by_ip=True,
             economy_address=None,
             port=None):
    if replace_localhost_by_ip:
        sd = complete_sd(sd_filename, economy_address, port)

    sd_json = json.loads(sd)
    return do_register(sd_json["broker"] + "/registry", sd_json, 1, 10)

max_retries=5
def do_register(registry_url, sd_json, retries, waiting_time):
    try:
        requests.post(registry_url, json=sd_json)
        logging.info("Registered service %s" % (sd_json["host"] + sd_json["@id"]))
        return (True, sd_json)
    except Exception as e:
        if retries <= max_retries:
            print("Could not register at %s. Will perform retry #%s in %s seconds" % (registry_url, retries, waiting_time))
            retries += 1
            waiting_time *= 2
            time.sleep(waiting_time)
            do_register(registry_url, sd_json, retries, waiting_time)
        else:
            print("Reached max_retries=%s, but there was no available broker at %s" % (max_retries, registry_url))
            return (False, sd_json)

def get_service_description(filename="service-description.jsonld"):
    sd_file = open(filename, "r")
    sd = sd_file.read()
    sd_file.close()
    return sd

def find_my_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        ip = s.getsockname()[0]
    except:
        ip = None
    finally:
        s.close()
    return ip

def contract(data={"query": {"@type": "*"}}, broker_url="http://localhost:4000/broker"):
    contract_url = broker_url + "/contracts"
    try:
        logging.info("Running contract for %s" % data)
        response = requests.post(contract_url,
                                data=json.dumps(data),
                                headers={'Content-Type': 'application/json'})
        location = response.headers['location']
        contract_dict = response.json()
        logging.info("State dict created is %s \nAnd the transaction signed\
must be sent to location %s" %(json.dumps(contract_dict),location))
        return {'contract_dict':contract_dict,'location':location}
    except Exception as e:
        print("The contract request did not work")

def send_signed_tx(negotiation_dict, broker_url="http://localhost:4000/broker"):
    location = negotiation_dict['location']
    signed_tx = negotiation_dict['contract_dict']['tx']
    url = broker_url + location
    if signed_tx and location:
        try:
            response = requests.put(url, json={"tx": signed_tx})
            if response.status_code == 200:
                final_answer = wait_sla_establishment(url)
                #final_answer = {'delegate_token':token, "tx": tx, "state": state}
                print(final_answer)
                if final_answer:
                    logging.info("The negotiation is complete")
                    return final_answer
        except Exception as e:
            print(e)
            print("The sent of signed transaction did not work")
            return None
    else:
        return None

def wait_sla_establishment(url):
    response = requests.get(url)
    status, max_retries, retries = response.status_code, 3, 1
    while status != 200 and retries <= max_retries:
        time.sleep(3)
        response = requests.get(url)
        status = response.status_code
        retries+=1
    if status == 200:
        return response.json()
    else:
        return None

op_dict = {
        "POST": 1,
        "GET": 2,
        "PUT": 4,
        "DELETE": 8
}
def authorize_request(request,
                      provider_id,
                      put_owner_feedback=False,
                      broker_url="http://localhost:4000/broker",
                      use_reputation_handler=True):
    print(request.headers)
    origin = request.headers['x-m2m-origin']
    token = ""
    #keys_headers = list(dict(request.headers).keys())
    if 'x-token' in request.headers:
        token = request.headers['x-token']
    print()
    print(token)
    print()
    query_dict = {"fr": origin, "op": op_dict[request.method], "to": provider_id, "delegation_token": token}
    r = requests.get(broker_url+"/security/authorization-requests", params=query_dict)
    if use_reputation_handler:
        msg = request_watcher_for_providers(r, origin, put_owner_feedback)
    else:
        msg = None
    return {'validation':(r.status_code == 200),'reputations_dict':reputations_dict,'msg':msg}

def request_watcher_for_providers(request, consumer_id, put_owner_feedback=False):
    global reputations_dict
    end_time = request.headers['expiration-time']   # Vai vir do request
    validation = (request.status_code == 200)
    if (not consumer_id in reputations_dict or reputations_dict['trades'] >= 1) and end_time:
        if not consumer_id in reputations_dict:
            reputations_dict[consumer_id] = {'fails':0,'uses':0,'end_time':end_time,'trades':0}
        delay = calculate_seconds_to_expiration(end_time)
        if delay > 0:
            t = Timer(delay+1, send_reputation, (consumer_id, put_owner_feedback))
            t.start()
    elif not end_time:
        reputations_dict[consumer_id]['fails'] += 5
        return "Never heard about you. Please first start negotiation throught Broker"
    if validation:
        reputations_dict[consumer_id]['uses'] += 1
        return "Everything OK with your request"
    else:
        reputations_dict[consumer_id]['fails'] += 1
        return "Permission expired. Negotiate again with me throught Broker to use my resource(s)"

def request_watcher_for_consumers(request, provider_id):
    global reputations_dict
    validation = (request.status_code == 200)
    if not provider_id in reputations_dict:
        reputations_dict[provider_id] = {'fails':0,'uses':0,'trades':0}
    if validation:
        reputations_dict[provider_id]['uses'] += 1
    else:
        reputations_dict[provider_id]['fails'] += 1
    return {'validation':validation,'reputations_dict':reputations_dict,'resource':request.json()}

def use_service_provider(query, provider_id, method='GET', data=None, use_reputation_handler=True):
    if method == 'GET':
        if query['operations'] == 'delegate':
            if data['token']:
                headers_dict = {
                        'x-m2m-origin':query['consumer']['host'],
                        'x-token':data['token']
                }
                print(headers_dict)
                r = requests.get(provider_id, headers=headers_dict)
            else:
                logging.info("Token was not given")
                return None
        else:
            headers_dict = {'x-m2m-origin':query['consumer']['host']}
            r = requests.get(provider_id,headers = headers_dict)
    elif method == 'POST':
        if query['operations'] == 'delegate':
            if data['token']:
                headers_dict = {
                        'x-m2m-origin':query['consumer']['host'],
                        'x-token':data['token']
                }
                r = requests.post(provider_id, json=data, headers=headers_dict)
            else:
                logging.info("Token was not given")
                return None
        else:
            headers_dict = {'x-m2m-origin':query['consumer']['host']}
            r = requests.post(provider_id, json=data, headers=headers_dict)
    if use_reputation_handler:
        helper = request_watcher_for_consumers(r, provider_id)
        return helper
    else:
        response = r.json()
        # print("From broker_client => Resource: " + str(response))
        return {'validation':(r.status_code == 200),'resource':response}

def calculate_seconds_to_expiration(str_expiration):
    return int(str_expiration) - int(time.time())

def compute_reputation(service_id, put_owner_feedback=False, owner_feedback=None):
    if reputations_dict[service_id]['uses'] >= 1:
        fails = float(reputations_dict[service_id]['fails'])/reputations_dict[service_id]['uses']
    else:
        fails = int(reputations_dict[service_id]['fails'])/2
    if fails > 2.5:
        fails = 2.5
    request_feedback = 5 - fails*2
    if put_owner_feedback:
        if not owner_feedback:
            owner_feedback = int(input("Por favor, insira o seu feedback para o serviço "
                                        + str(service_id) + " num intervalo de 0 a 5: "))
        return (owner_feedback+request_feedback)/2
    else:
        return request_feedback

def send_reputation(service_id,
                    put_owner_feedback=False,
                    owner_feedback=None,
                    broker_url='http://localhost:4000/broker'):
    reputation = compute_reputation(service_id, put_owner_feedback, owner_feedback)
    broker_url = broker_url + '/reputations'
    status = 0
    while status != 200:
        r = requests.post(broker_url, json={'service_id':service_id, 'reputation': reputation})
        status = r.status_code
    reputations_dict[service_id]['fails'] = 0
    reputations_dict[service_id]['uses'] = 0
    reputations_dict[service_id]['trades'] += 1

def complete_sd(filename="service-description.jsonld", economy_address=None, port=None):
    sd = get_service_description(filename)
    my_ip = find_my_ip()
    if economy_address:
        sd = sd.replace("put_address_here", economy_address)
    if my_ip:
        sd = sd.replace("localhost", my_ip)
        if port:
            sd = sd.replace("8080", str(port))
    return sd
