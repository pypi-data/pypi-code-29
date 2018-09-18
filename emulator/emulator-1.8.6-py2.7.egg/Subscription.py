from emulator.fimp.address import Address, MsgType, ResourceType
from emulator.fimp.message import Message, ValueType
from emulator.fimp.mqtt_transport import MqttTransport

import _thread
import time
import json

log_file = "log.log"

DEBUG = True

def Log(log):
    if (DEBUG == True):
        with open(log_file, "a") as logFp:
            logFp.write(log + "\n")

def handler():
    return

def msg_handler(topic, address, fimp_msg):
    print("FIMP_msg_handler: Message from address : " + topic)
    print("FIMP_msg_handler: Message from address : " + str(address))
    print("FIMP_msg_handler: Message from address : " + str(fimp_msg))

    """ try:
        _thread.start_new_thread(handler)
    except:
        Log("init_onload : Unable to start core-subscription thread") """

def stub_subscribe():
    Log("stub_subscribe: subscribe to all core events: # ")

    mq_transport = MqttTransport()
    mq_transport.set_message_handler(msg_handler)
    mq_transport.connect()
    mq_transport.subscribe("#")
    
    Log("stub_subscribe: Done!")

    mq_transport.stop()

    return