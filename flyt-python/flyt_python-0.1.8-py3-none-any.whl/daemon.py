import json
import websocket
import time
import functools
import redis
import threading

connections = {}
host = 'localhost'
port = 6379
db_i = 0
r = redis.StrictRedis(host=host, port=port, db=db_i)
r.set('NUMBER_OF_CONNECTIONS', 0)

topics_and_types = dict(attitude=['/mavros/imu/data', 'sensor_msgs/Imu'],
                        attitude_euler=['/mavros/imu/data_euler', 'geometry_msgs/TwistStamped'],
                        local_position=['/mavros/local_position/local', 'geometry_msgs/TwistStamped'],
                        global_position=['/mavros/global_position/global', 'sensor_msgs/NavSatFix'],
                        battery_status=['/mavros/battery', 'sensor_msgs/BatteryState'],
                        VFR_HUD=['/mavros/vfr_hud', 'mavros_msgs/VFR_HUD'],
                        RC_DATA=['/mavros/rc/in', 'mavros_msgs/RCIn'],
                        distance_sensor=['/mavros/distance_sensor/lidarlite_pub', 'sensor_msgs/Range'],
                        vehicle_state=['/flyt/state', 'mavros_msgs/State'])

class DaemonConnectionClose(Exception) :
    pass
class DaemonTimeout(Exception):
    pass
class DaemonWebsocket(Exception):
    pass
class DroneOffline(Exception):
    pass

def encode_message(message):
    return json.dumps(message)

def decode_message(message):
    return json.loads(message)

def service_template(op, service, type_):
    return dict(op=op, service=service, type=type_)

def subscribe_unsubscribe_template(op, topic, type_):
    return dict(op=op, topic=topic, type=type_)

def on_error(error):
    """
    This API called internally when there is any error connecting to the Websocket
    :param error: error
    """
    raise DroneOffline("MAke sure that your is online.")

def on_close(id_, ws):
    """
    This API called internally when websocket connection is closed
    :param id_: Connection ID
    :param ws: WebsocketApp instance
    """
    remove_connection(id_)

def on_open(id_, ws):
    """
    This API called internally when Websocket connection is established
    :param id_: Connection ID
    :param ws: WebsocketAPP Instance
    """
    r.publish(str(id_) + "SOCK_INIT", "OK")
    pass

def on_message(id_, ws, message):
    """
    This API is called internally when there is a response message from Websocket Server
    :param id_: Connection ID
    :param ws: WebsocketApp Instance
    :param message: Response message from websocket server
    """
    message = decode_message(message)
    op = message['op']
    if op == "service_response":
        if message['service'] == "/get_global_namespace":
            namespace = message['values']['param_info']['param_value']
        else:
            namespace = message['service'].split('/')[1]
            connections[id_].data['on_request'][message['service']] = {"result": message['result'],
                                                                       "values": message["values"], "ts": time.time()}
            r.set(id_, json.dumps(connections[id_].data))
            r.pexpire(id_, 200)
            r.publish(str(id_) + "on_request" + message['service'], message)
    elif op == "publish":
        if (message['topic'].split('/')[3] == 'battery') and (
                int(time.time() - connections[id_].last_ping_battery) > connections[id_].timeout):
            unsubscribe(id_, "battery_status")
        elif (message['topic'].split('/')[3] == 'local_position') and (
                int(time.time() - connections[id_].last_ping_local) > connections[id_].timeout):
            unsubscribe(id_, "local_position")
        elif (message['topic'].split('/')[3] == 'global_position') and (
                int(time.time() - connections[id_].last_ping_global) > connections[id_].timeout):
            unsubscribe(id_, "global_position")
        elif (message['topic'].split('/')[3] == 'vfr_hud') and (
                int(time.time() - connections[id_].last_ping_vfr) > connections[id_].timeout):
            unsubscribe(id_, "VFR_HUD")
        elif (message['topic'].split('/')[3] == 'rc') and (
                int(time.time() - connections[id_].last_ping_rc) > connections[id_].timeout):
            unsubscribe(id_, "RC_DATA")
        elif (message['topic'].split('/')[3] == 'distance_sensor') and (
                int(time.time() - connections[id_].last_ping_distance) > connections[id_].timeout):
            unsubscribe(id_, "distance_sensor")
        elif (message['topic'].split('/')[3] == 'state') and (
                int(time.time() - connections[id_].last_ping_state) > connections[id_].timeout):
            unsubscribe(id_, "vehicle_state")
        if (message['topic'].split('/')[3] == 'imu'):
            if (message['topic'].split('/')[4] == 'data') and (
                    int(time.time() - connections[id_].last_ping_attitude) > connections[id_].timeout):
                unsubscribe(id_, "attitude")
            elif (message['topic'].split('/')[4] == 'data_euler') and (
                    int(time.time() - connections[id_].last_ping_att_eular) > connections[id_].timeout):
                unsubscribe(id_, "attitude_euler")
            else:
                pass
        else:
            pass
        namespace = message['topic'].split('/')[1]
        connections[id_].data['real_time'][message['topic']] = dict(msg=message['msg'], ts=time.time())
        r.set(id_, json.dumps(connections[id_].data))
        r.pexpire(id_, 200)
    else:
        raise DroneOffline("You don't belong here!")

def run_thread_forever(a):
    """
    :param a: WebsocketApp instance
    """
    a.run_forever(ping_timeout=2)

def make_new_connection(job_request, timeout, header, conn_time):
    """
    This API creates new websocket connection
    :param job_request: job_request Queue
    :param timeout: Subscription Time in seconds
    :param header: Header for Websocket Connection
    :param conn_time: in seconds
    """
    namespace = job_request['namespace']
    id_ = job_request['id']
    vehicleID = job_request['vehicleID']
    header = header
    connection = Connection(namespace, id_, vehicleID)
    connections[id_] = connection
    on_message_private = functools.partial(on_message, id_)
    on_close_private = functools.partial(on_close, id_)
    on_error_private = functools.partial(on_error, id_)
    on_open_private = functools.partial(on_open, id_)
    ws = websocket.WebSocketApp("wss://dev.flytbase.com/websocket",   #ws://localhost:80/websocket",
                                header=header,
                                on_message=on_message_private,
                                on_error=on_error_private,
                                on_close=on_close_private,
                                on_open=on_open_private)
    wst = threading.Thread(target=run_thread_forever, args=(ws,))
    wst.daemon = True
    wst.start()
    connections[id_].conn_time = conn_time
    connections[id_].timeout = timeout
    connections[id_].ws = ws
    no_of_connections = int(r.get('NUMBER_OF_CONNECTIONS'))
    no_of_connections += 1
    r.set('NUMBER_OF_CONNECTIONS', no_of_connections)

def subscribe(id_, topic):
    """
    This API is used to subscribe a channel
    :param id_: Connection ID
    :param topic: topic to be subscribed
    """
    try:
        if topic in connections[id_].subscriptions:
            if topic == 'battery_status':
                connections[id_].last_ping_battery = time.time()
            elif topic == 'attitude':
                connections[id_].last_ping_attitude = time.time()
            elif topic == 'attitude_euler':
                connections[id_].last_ping_att_eular = time.time()
            elif topic == 'local_position':
                connections[id_].last_ping_local = time.time()
            elif topic == 'global_position':
                connections[id_].last_ping_global = time.time()
            elif topic == 'VFR_HUD':
                connections[id_].last_ping_vfr = time.time()
            elif topic == 'RC_DATA':
                connections[id_].last_ping_rc = time.time()
            elif topic == 'distance_sensor':
                connections[id_].last_ping_distance = time.time()
            elif topic == 'vehicle_state':
                connections[id_].last_ping_state = time.time()
            else:
                pass
        else:
            if topic == 'battery_status':
                connections[id_].last_ping_battery = time.time()
            elif topic == 'attitude':
                connections[id_].last_ping_attitude = time.time()
            elif topic == 'attitude_euler':
                connections[id_].last_ping_att_eular = time.time()
            elif topic == 'local_position':
                connections[id_].last_ping_local = time.time()
            elif topic == 'global_position':
                connections[id_].last_ping_global = time.time()
            elif topic == 'VFR_HUD':
                connections[id_].last_ping_vfr = time.time()
            elif topic == 'RC_DATA':
                connections[id_].last_ping_rc = time.time()
            elif topic == 'distance_sensor':
                connections[id_].last_ping_distance = time.time()
            elif topic == 'vehicle_state':
                connections[id_].last_ping_state = time.time()
            else:
                pass
    except KeyError:
        raise DaemonConnectionClose("Try to connect the drone")

        try:
            if not connections[id_].ws.sock.connected:
                connections[id_].ws.run_forever()

            namespace = connections[id_].namespace
            message = subscribe_unsubscribe_template("subscribe", '/' + namespace + topics_and_types[topic][0],
                                                 topics_and_types[topic][1])
            connections[id_].ws.send(encode_message(message))
            connections[id_].subscriptions.append(topic)
        except websocket._exceptions.WebSocketConnectionClosedException:
            raise DaemonConnectionClose('Connect your drone to the internet')
        except websocket.WebSocketTimeoutException:
            raise DaemonTimeout('Check your Internet Connection')

def unsubscribe(id_, topic):
    """
    This API is used to unsubscribe the subscribed channel
    :param id_: Connection ID
    :param topic: Topic to be unsubscribed
    """
    try:
        namespace = connections[id_].namespace
        message = subscribe_unsubscribe_template("unsubscribe", '/' + namespace + topics_and_types[topic][0],
                                                 topics_and_types[topic][1])
        connections[id_].ws.send(encode_message(message))
        connections[id_].subscriptions.remove(topic)
    except websocket._exceptions.WebSocketConnectionClosedException:
        raise DaemonConnectionClose('Connect your drone to the internet')
    except websocket.WebSocketTimeoutException:
        raise DaemonTimeout('Check your Internet Connection')

async def service_call(id_, data):
    """
    This API is used to call Navigation APIs
    :param id_: Connection ID
    :param data: Data to be sent to Websocket Server
    """
    try:
        connections[id_].ws.send(encode_message(data))
    except websocket._exceptions.WebSocketConnectionClosedException:
        raise DaemonConnectionClose('Connect your drone to the internet')
    except websocket.WebSocketTimeoutException:
        raise DaemonTimeout('Check your Internet Connection')
    return "Service Call Sent"

def remove_connection(id_):
    """
    This API is responsible for closing the websocket connection
    :param id_: Connection ID
    """
    for topic in connections[id_].subscriptions:
        unsubscribe(id_, topic)
    r.set(id_, None)
    r.set(connections[id_].vehicleID, json.dumps({}))
    connections[id_].ws.close()
    connections.pop(id_, None)

def coro_manager(coro):
    try:
        coro.send(None)
    except StopIteration as stop:
        return stop.value

class Ping(object):
    """
    The run() method will be started and it will run in the background
    until the application exits.
    """

    def __init__(self, interval=1, id_=0):
        """ Constructor
        :type interval: int
        :param interval: Websocket connection time (Inactivity time), in seconds
        :param id_: Connection ID
        """
        self.interval = interval
        self.id_ = id_
        self.t1 = time.time()
        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True                            # Daemonize thread
        thread.start()      # Start the execution

    def run(self):
        """ Method that runs forever """
        while True:
            if connections[self.id_].conn_time < 0:
                time.sleep(13)
                connections[self.id_].ws.send(encode_message({'messgage':'Ping'}))
                time.sleep(self.interval)
            else:
                if int(time.time() - self.t1) > connections[self.id_].conn_time:
                    break
                else:
                    time.sleep(13)
                    connections[self.id_].ws.send(encode_message({'messgage': 'Ping'}))
                    time.sleep(self.interval)

class Connection():
    def __init__(self, namespace, id_, vehicleID):
        self.namespace = namespace
        self.id_ = id_
        self.data = dict(real_time={}, on_request={}, vehicleID=vehicleID)
        self.subscriptions = []
        self.ws = None
        self.vehicleID = vehicleID
        self.last_ping_battery = 0
        self.last_ping_state = 0
        self.last_ping_distance = 0
        self.last_ping_rc = 0
        self.last_ping_vfr = 0
        self.last_ping_global = 0
        self.last_ping_local = 0
        self.last_ping_att_eular = 0
        self.last_ping_attitude = 0
        self.timeout = 10
        self.conn_time = 5
        self.ws_time = 10
        r.set(vehicleID, json.dumps(dict(id=id_, namespace=namespace)))

class Listener(threading.Thread):
    def __init__(self, r, channels):
        try:
            threading.Thread.__init__(self)
            self.redis = r
            self.pubsub = self.redis.pubsub(ignore_subscribe_messages=True)
            self.pubsub.subscribe(channels)
        except:
            print("Connection is not established.")

    def work(self, item):
        pass

    def run(self):
        for item in self.pubsub.listen():
            if item['data'] == "KILL":
                self.pubsub.unsubscribe()
                break
            else:
                self.work(item)
                job_request = json.loads(item['data'].decode('utf-8'))
                if job_request:
                    if job_request['type'] == "NEW_CONN":
                        make_new_connection(job_request,timeout=job_request['timeout'],header=job_request['header'],
                                            conn_time=job_request['conn_time'] )
                        connections[job_request["id"]].ws_time = connections[job_request["id"]].ws_time + 10
                        time.sleep(1)
                        Ping(interval=5, id_=job_request["id"])
                    elif job_request['type'] == "CLOSE_CONN":
                        remove_connection(job_request["id"])
                    else:
                        if job_request['op'] == 'call_service':
                            connections[job_request["id"]].ws_time = connections[job_request["id"]].ws_time + 10
                            print(coro_manager(service_call(job_request['id'], job_request)))
                        elif job_request['op'] == 'subscribe':
                            if job_request['topic'] == 'random':
                                connections[job_request["id"]].ws_time = connections[job_request["id"]].ws_time + 10
                                ping(job_request["id"])
                            else:
                                connections[job_request["id"]].ws_time = connections[job_request["id"]].ws_time + 10
                                subscribe(job_request['id'], job_request['topic'])
                        elif job_request['op'] == 'unsubscribe':
                            connections[job_request["id"]].ws_time = connections[job_request["id"]].ws_time + 10
                            unsubscribe(job_request['id'], job_request['topic'])
                        else:
                            pass

if __name__ == "__main__":
    try:
        r = redis.Redis()
        client = Listener(r, ['JOB_REQUEST'])
        client.start()
    except:
        raise DroneOffline("Problem starting Daemon!!!")
