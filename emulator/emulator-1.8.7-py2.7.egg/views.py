#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 04:54:09 2018

@author: ashraya
"""

#import ast
import json
import logging
import os
import time
from threading import Thread
from logging.handlers import RotatingFileHandler

from flask import Flask, render_template, request

from emulator.functions import generate_exclusion_report, generate_inclusion_report, generate_trigger_report
from emulator.common import update_selected_devices
from emulator.timer import stub_event_thread_loop
import emulator.paho.mqtt.publish, emulator.paho.mqtt.subscribe

# App config.

hostname = "localhost"
port = 5000
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = os.urandom(12)
app.config['ENV'] = 'development'

def Log(info):
    if (DEBUG == True):
        filename = "log.log"
        if os.path.exists(filename):
            append_write = 'a' # append if already exists
        else:
            append_write = 'w' # make a new file if not

        fp= open(filename, append_write)
        fp.write(info + '\n')
        fp.close()
        app.logger.debug(info)

devices_file = os.path.dirname(os.path.realpath(__file__)) + '/selected_devices.json'
devices = []

@app.route("/")
def init():
    return render_template('front.html')

@app.after_request
def add_header(r):
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate, public, max-age=0"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    return r

def get_devices_from_jsonfiles():
    devices = []
    filepath = os.path.dirname(os.path.realpath(__file__)) + "/static/prop_files/"
    if os.path.exists(filepath):
        files = os.listdir(filepath)

        for d in files:
            if (d.find("json") > -1):
                devices.append(d[:d.find('.')])
    return devices

@app.route('/init_onload', methods = ['POST'])
def init_onload():
    selected_devices = []
    if os.path.exists(devices_file):
        selected_devices = json.load(open(devices_file, 'w+'))

        try:
            t = Thread(target=stub_event_thread_loop, args=(devices_file, ))
            t.start()
        except:
            Log("init_onload : Unable to start core-event thread loop") 

    return json.dumps(selected_devices)

@app.route('/init2_onload', methods = ['POST'])
def init2_onload():
        devices = get_devices_from_jsonfiles()

        return json.dumps(devices)

@app.route('/remove_device', methods = ['POST'])
def remove_device():
    data = request.data
    data1 = data

    selected_devices = json.load(open(devices_file))

    for device in range(len(selected_devices)):
        bdata1 = data1.decode('utf-8')
        ddata1 = selected_devices[device].get("id")

        if (str(bdata1) == str(ddata1)):
            selected_devices.pop(device)

            with open(devices_file, 'w+') as jsonfile:
                json.dump(selected_devices, jsonfile)
            jsonfile.close()

            topic, report = generate_exclusion_report(str(bdata1))

            emulator.paho.mqtt.publish.single(topic, json.dumps(report), hostname=hostname)

            break

    return json.dumps(selected_devices)

@app.route('/get_properties', methods = ['POST'])
def get_properties():
    Log("get_properties")
    if request.method == 'POST':
        data = request.data
        data1 = data

        selected_devices = json.load(open(devices_file))
        for device in range(len(selected_devices)):
            bdata1 = data1.decode('utf-8')
            try:
                ddata1 = selected_devices[device].get("id")
            except KeyError:
                Log("get_properties : KeyError! : " + str(bdata1))

            if (str(bdata1) == str(ddata1)):
                return json.dumps(selected_devices[device])

    Log("get_properties : Error! ")
    return "Error"

def update_services(req):
    svs_dict = {}
    for key in req:
        if (key.find("services") > -1) or (key.find("sensor_") == 0):
            key_status = False
            if (req[key] != ""):
                key_status = True
            else:
                key_status = False

            if ((key == "sensor_presence") or (key == "sensor_contact")):
                svs_dict[key] = key_status
            else:
                svs_dict[key[key.find('_')+1:]] = key_status

    return svs_dict

@app.route('/properties', methods = ['POST'])
def properties():
    if request.method == 'POST':
        selected_devices = []

        if os.path.exists(devices_file):
            selected_devices = json.load(open(devices_file))

        req = request.json
        req1 = json.loads(req)
        device_id = req1["id"]
        req1["time"] = time.time()
        selected_devices = update_selected_devices(devices_file, selected_devices, req1, device_id)

        modify_svs = update_services(req1)
        devices = get_devices_from_jsonfiles()

        device = ""
        for d in devices:
            if (device_id.find(d) > -1):
                device = d
                break

        # Initially, generate an UP/DOWN event based on status and if UP, proceed, else return
        topic, report = generate_trigger_report("state", device_id, device, str(req1["status"]))
        if topic != "":
            Log("properties : topic : "+ topic)
            Log("properties : report : "+ str(report))
            emulator.paho.mqtt.publish.single(topic, json.dumps(report), hostname=hostname)

        if req1["status"] != "true":
            return json.dumps(selected_devices)

        skey = ""
        for key in req1:
            topic = ""
            report = ""

            try:
                Log("properties : " + str(key) + ":" + str(req1[key]))

                if ((key == "ping") and (req1["ping"] == 'on')):
                    topic, report = generate_trigger_report("ping", device_id, device, str(req1["status"]))
                elif (key.find("services") > -1):
                    if (req1[key] == 'true'):
                        topic, report = generate_trigger_report(key[key.find('_')+1:], device_id, device, modify_svs[key[key.find('_')+1:]])
                elif ((key.find("battery") > -1) or (key.find("color") > -1)):
                    topic, report = generate_trigger_report(str(req1[key]), device_id, device, True)
                elif ((key == "sensor_presence") or (key == "sensor_contact")):
                    #if (req1[key] == 'true'): # Send false report as well
                    topic, report = generate_trigger_report(key, device_id, device, modify_svs[key])
                elif ((key.find("sensor_") == 0) or (key.find("meter") == 0)):
                    skey = req1[key]
                    continue
                elif ((key.find("value_sensor") > -1) or (key.find("value_meter") > -1)):
                    if (req1[key] == ""):
                        continue
                    topic, report = generate_trigger_report(skey, device_id, device, True, str(req1[key]))
                    skey = ""
                else:
                    continue

                if topic == "":
                    continue
                else:
                    Log("properties : topic : "+ topic)
                    Log("properties : report : "+ str(report))
                    emulator.paho.mqtt.publish.single(topic, json.dumps(report), hostname=hostname)
            except KeyError:
                Log("properties : KeyError! : " + str(key) + " : " + str(req1[key]))
        return json.dumps(selected_devices)

    return "Error"

@app.route('/add_device', methods = ['POST'])
def add_device():
    if request.method == 'POST':
        selected_devices = []
        if os.path.exists(devices_file):
            selected_devices = json.load(open(devices_file))

        req1 = ""
        data = request.data
        data1 = data

        data1 = str(data1.decode('utf-8'))
        devices = get_devices_from_jsonfiles()
        #devices = get_devices()

        for d in devices:
            if (data1.find(d) > -1):
                file_path = os.path.dirname(os.path.realpath(__file__)) + "/static/prop_files/" + d + ".json"

                if os.path.exists(file_path):
                    req1 = json.load(open(file_path))

                    topic, report = generate_inclusion_report(req1, data1)
                    report["val"]["status"] = "false"
                    report["val"]["id"] = data1
                    report["val"]["time"] = time.time()
                    Log("add_device : report : "+ str(report)+" : " + str(type(report)))

                    selected_devices = update_selected_devices(devices_file, selected_devices, report["val"], data1)

                    emulator.paho.mqtt.publish.single(topic, json.dumps(report), hostname=hostname)
                    return json.dumps(selected_devices)

    return "Error"

def main():
    formatter = logging.Formatter("[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s")
    handler = RotatingFileHandler('log.log', maxBytes=1000000, backupCount=1)
    handler.setLevel(logging.DEBUG)
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)

    app.run(debug=False, port=port)
