import requests
import time
import redis
import json
import threading
from flyt_python.utils import add_to_job_requests, get_data

host = 'localhost'
port = 6379
db_i = 0
r = redis.StrictRedis(host=host, port=port, db=db_i)
url = 'https://dev.flytbase.com/rest/ros/get_global_namespace'


class Unauthorized(Exception):
    pass
class DroneOffline(Exception):
    pass
class BadRequest(Exception):
    pass
class ConnError(Exception):
    pass

class DroneApiConnector():
    def __init__(self, token, vehicle_id, timeout=60, time_constant=20, conn_time=10, wait_for_drone_response=False):
        """
        Get namespace and make a websocket connection with the drone
        :param token: Personal Access Token assigned to the User (Flytbase Platform)
        :param vehicle_id: Vehicle ID assigned to the drone (Flytbase Platform)
        :param ip_address: Drone's IPv4 Address
        :param timeout: Subscription time in seconds
        :param time_constant: Data storage time in seconds
        :param conn_time: after this much time of inactivity the websocket connection closes
        :param wait_for_drone_response: True/False
        """
        if len(token) != 40 or len(vehicle_id) != 8:
            raise Unauthorized("The token length should be 40 characters and the VehicleID should be 8 characters")
        self.activated = False
        self.timeout = timeout
        self.headers = dict(Authorization='Token ' + token, VehicleID=vehicle_id)

        try:
            result = requests.get(url, headers=self.headers)
            if (result.status_code == 200):
                result = json.loads(result.content.decode('utf-8'))
                self.namespace = result["param_info"]["param_value"]
            elif(result.status_code == 404):
                raise DroneOffline('Make sure that your drone is online')
            elif(result.status_code == 401):
                raise Unauthorized('Token/Vehicle_id is Invalid')
            else:
                raise BadRequest("Request can't be processed")
        except requests.exceptions.SSLError:
            raise ConnError("Retry")
        except requests.exceptions.Timeout:
            raise ConnError("Connection Timeout")
        except ConnectionError:
            raise ConnectionError('Check your Internet connection')

        no_of_connections = (r.get('NUMBER_OF_CONNECTIONS'))
        if no_of_connections == None:
            no_of_connections = 0
        else:
            no_of_connections = int(no_of_connections) + 1
        self.id = no_of_connections
        self.wait_for_drone_response = not wait_for_drone_response
        header = {
            "Authorization": 'Token '+token,
            "VehicleID": vehicle_id,
            "Content-Type":"application/json"
        }
        self.conn_time = conn_time
        job_request = dict(type="NEW_CONN", namespace=self.namespace, id=self.id, vehicleID=vehicle_id,
                           timeout=self.timeout, header=header, conn_time = self.conn_time)
        add_to_job_requests(job_request)

        wst = threading.Thread(target=self.filter_unnecessary, args=())
        wst.daemon = True
        wst.start()

        self.time_constant = time_constant
        self.pubsub = r.pubsub(ignore_subscribe_messages=True)
        self.activated = True

    def call_service(self, op, service, type_):
        if not self.activated:
            return "Wait for the drone" + self.namespace + " to activate"
        request = dict(op=op, service='/' + self.namespace + service, type=type_, id=self.id)
        add_to_job_requests(request)

    # Navigation APIs
    def takeoff(self, height=1.5):
        """
        Takeoff to given height at current location. (minimum 1.5 meters)
        :param height: Altitude
        :return: {"success": True/False, "message": "debug message"}
        """
        if not self.activated:
            return "WAIT FOR DRONE" + self.namespace + " TO ACTIVATE"
        if height < 1.5:
            height = 1.5
        request = dict(op="call_service", service="/" + self.namespace + "/navigation/take_off",
                       type="core_api/TakeOff", args={"takeoff_alt": height}, id=self.id)
        add_to_job_requests(request)

        if self.wait_for_drone_response:
            return "Takeoff Request Submitted Successfully"
        else:
            return self.handle_return("/" + self.namespace + "/navigation/take_off", "on_request")


    def land(self, async=False):
        """
        Land vehicle at current position. Check API usage section below before using this API.
        :param async: If true, asynchronous mode is set
        :return: {"success": True/False, "message": "debug message"}
        """        #self.takeoff_response()
        if not self.activated:
            return "WAIT FOR DRONE" + self.namespace + " TO ACTIVATE"
        request = dict(op="call_service", service="/" + self.namespace + "/navigation/land", type="core_api/Land",
                       args={"async": async}, id=self.id)
        add_to_job_requests(request)
        if async and self.wait_for_drone_response:
            return "Land Request Submitted Successfully"
        else:
            return self.handle_return("/" + self.namespace + "/navigation/land", "on_request")

    def arm(self):
        """
        This API arms the motors.
        :return: {"success": True/False, "message": "debug message"}
        """
        if not self.activated:
            return "WAIT FOR DRONE" + self.namespace + " TO ACTIVATE"
        request = dict(op="call_service", service="/" + self.namespace + "/navigation/arm", type="core_api/Arm",
                       id=self.id)
        add_to_job_requests(request)
        return self.handle_return("/" + self.namespace + "/navigation/arm", "on_request")

    def disarm(self):
        """
        This API disarms the motors.
        :return: {"success": True/False, "message": "debug message"}
        """
        if not self.activated:
            return "WAIT FOR DRONE" + self.namespace + " TO ACTIVATE"
        request = dict(op="call_service", service="/" + self.namespace + "/navigation/disarm", type="core_api/Disarm",
                       id=self.id)
        add_to_job_requests(request)
        return self.handle_return("/" + self.namespace + "/navigation/disarm", "on_request")

    def hold_position(self):
        """
        Position hold / hover / loiter at current position.
        :return: {"success": True/False, "message": "debug message"}
        """
        if not self.activated:
            return "WAIT FOR DRONE" + self.namespace + " TO ACTIVATE"
        request = dict(op="call_service", service="/" + self.namespace + "/navigation/position_hold",
                       type="core_api/PositionHold", id=self.id)

        add_to_job_requests(request)
        return self.handle_return("/" + self.namespace + "/navigation/position_hold", "on_request")

    def set_local_position(self, x, y, z, yaw=0.0, tolerance=1.0, async=False, relative=True, yaw_valid=False, body_frame=False):
        """
        This API commands the vehicle to go to a specified location in local frame and hover.
        :param x,y,z: Position Setpoint in NED-Frame (in body-frame if body_frame=true)
        :param yaw: Yaw Setpoint in radians
        :param tolerance: Acceptance radius in meters, default value=1.0m
        :param async: If true, asynchronous mode is set
        :param relative: If true, position setpoints relative to current position is sent
        :param yaw_valid: Must be set to true, if yaw
        :param body_frame: If true, position setpoints are relative with respect to body frame
        :return: {"success": True/False, "message": "debug message"}
        """
        if not self.activated:
            return "WAIT FOR DRONE" + self.namespace + " TO ACTIVATE"

        request = dict(op="call_service", service="/" + self.namespace + "/navigation/position_set",
                       type="core_api/PositionSet", id=self.id, args=dict(x=x, y=y, z=z, yaw=yaw,
                                                                          tolerance=tolerance, async=async,
                                                                          relative=relative, yaw_valid=yaw_valid,
                                                                          body_frame=body_frame))
        add_to_job_requests(request)
        if async and self.wait_for_drone_response:
            return "Local Position Set Request Submitted Successfully"
        else:
            return self.handle_return("/" + self.namespace + "/navigation/position_set", "on_request")

    def set_global_position(self, lat_x, long_y, rel_alt_z, yaw=0.0, tolerance=1.0, async=False, yaw_valid=False):
        """
        This API sets a desired position setpoint in global coordinate system (WGS84).
        :param lat_x: Latitude
        :param long_y: Longitude
        :param rel_alt_z: relative height from current location in meters
        :param yaw: Yaw Setpoint in radians
        :param tolerance: Acceptance radius in meters, default value=1.0m
        :param async: If true, asynchronous mode is set
        :param yaw_valid: Must be set to true, if yaw
        :return: {"success": True/False, "message": "debug message"}
        """
        if not self.activated:
            return "WAIT FOR DRONE" + self.namespace + " TO ACTIVATE"
        request = dict(op="call_service", service="/" + self.namespace + "/navigation/position_set_global",
                       type="core_api/PositionHoldGlobal", id=self.id, args=dict(lat_x=lat_x, long_y=long_y,
                                                                                 rel_alt_z=rel_alt_z, yaw=yaw,
                                                                                 tolerance=tolerance, async=async,
                                                                                 yaw_valid=yaw_valid))
        add_to_job_requests(request)
        if async and self.wait_for_drone_response:
            return "Global Position Set Request Submitted Successfully"
        else:
            return self.handle_return("/" + self.namespace + "/navigation/position_set_global", "on_request")

    def set_velocity(self, vx, vy, vz, yaw_rate, tolerance=1.0, async=False, relative=True, yaw_rate_valid=False,body_frame=False):
        """
        This API gives linear (vx,vy,vz) and angular (yaw_rate) velocity setpoint to vehicle.
        :param vx, vy, vz: Velocity Setpoint in NED-Frame (in body-frame if body_frame=true)
        :param yaw_rate: Yaw rate Setpoint in rad/sec
        :param tolerance: Acceptance range in m/s, default value=1.0 m/s
        :param async: If true, asynchronous mode is set
        :param relative: If true, velocity setpoints relative to current position is sent
        :param yaw_rate_valid: Must be set to true, if yaw
        :param body_frame: If true, velocity setpoints are relative with respect to body frame
        :return: {"success": True/False, "message": "debug message"}
        """
        if not self.activated:
            return "WAIT FOR DRONE" + self.namespace + " TO ACTIVATE"
        request = dict(op="call_service", service="/" + self.namespace + "/navigation/velocity_set",
                       type="core_api/VelocitySet", id=self.id,
                       args=dict(vx=vx, vy=vy, vz=vz, yaw_rate=yaw_rate, tolerance=tolerance, async=async,
                                 relative=relative,
                                 yaw_rate_valid=yaw_rate_valid, body_frame=body_frame))
        add_to_job_requests(request)
        if async and self.wait_for_drone_response:
            return "Velocity Set Request Submitted Successfully"
        else:
            return self.handle_return("/" + self.namespace + "/navigation/velocity_set", "on_request")

    def execute_script(self, appname, arguments):
        """
        This API can run onboard executable scripts in python, shell, etc.
        :param appname: Name of the script. Script should be present in /flyt/flytapps/onboard_user/install directory.
        :param arguments: arguments separated by space e.g. “arg1 arg2 arg3”
        :return: {"success": True/False, "message": "debug message"}
        """
        if not self.activated:
            return "WAIT FOR DRONE" + self.namespace + " TO ACTIVATE"
        request = dict(op="call_service", service="/" + self.namespace + "/navigation/exec_script",
                       type="core_api/ExecScript", id=self.id, args=dict(appname=appname, arguments=arguments))
        add_to_job_requests(request)
        return self.handle_return("/" + self.namespace + "/navigation/exec_script", "on_request")

    def get_waypoints(self):
        """
        This API returns list of current waypoints on autopilot.
        :return: {"success": True/False, "message": "debug message"}
        """
        if not self.activated:
            return "WAIT FOR DRONE" + self.namespace + " TO ACTIVATE"
        request = dict(op="call_service", service="/" + self.namespace + "/navigation/waypoint_get",
                       type="core_api/WaypointGet", id=self.id)
        add_to_job_requests(request)
        return self.handle_return("/" + self.namespace + "/navigation/waypoint_get","on_request" )

    def set_waypoints(self, waypoints_raw):
        """
        This API replaces current list of waypoints on autopilot with new list passed.
        :param waypoints_raw:
                    waypoints_raw:
                    [
                        {
                            frame : The Frame in which the waypoints are given
                                    0: Global
                                    1: Local NED
                                    2: Mission
                                    3: Global Rel Alt
                            command: defines the function of the waypoint
                                    16: Waypoints
                                    17: Loiter
                                    18: Loiter Turns
                                    19: Loiter time
                                    20: Return to Launch
                                    21: Land
                                    22: Take Off
                            is_current: Set it as the first waypoint
                            autocontinue: continue to the next waypoint as soon as the current waypoint is achieved
                            param1: Time to stay at the location in sec.
                            param2: radius around the waypoint within which the waypoint is marked as done
                            param3: Orbit radius in meters
                            param4: Yaw/direction in degrees
                            x_lat: Latitude
                            y_long: Longitude
                            z_alt: Relative altitude
                        },
                        {},
                        {},...
                    ]
        :return: {"success": True/False, "message": "debug message"}
        """
        if not self.activated:
            return "WAIT FOR DRONE" + self.namespace + " TO ACTIVATE"
        waypoints_new = []
        for waypoint in waypoints_raw:
            waypoint_new = {}
            waypoint_new = waypoint
            waypoints_new.append(waypoint_new)
        request = dict(op="call_service", service="/" + self.namespace + "/navigation/waypoint_set",
                       type="core_api/WaypointSet", id=self.id, args=dict(waypoints=waypoints_new))
        add_to_job_requests(request)
        return self.handle_return("/" + self.namespace + "/navigation/waypoint_set", "on_request")

    def execute_waypoints(self):
        """
        Exectute / resume current list of waypoints.
        :return: {"success": True/False, "message": "debug message"}
        """
        if not self.activated:
            return "WAIT FOR DRONE" + self.namespace + " TO ACTIVATE"
        request = dict(op="call_service", service="/" + self.namespace + "/navigation/waypoint_execute",
                       type="core_api/WaypointExecute", id=self.id)
        add_to_job_requests(request)
        return self.handle_return("/" + self.namespace + "/navigation/waypoint_execute", "on_request")

    def clear_waypoints(self):
        """
        Clear list of waypoints on autopilot.
        :return: {"success": True/False, "message": "debug message"}
        """
        if not self.activated:
            return "WAIT FOR DRONE" + self.namespace + " TO ACTIVATE"
        request = dict(op="call_service", service="/" + self.namespace + "/navigation/waypoint_clear",
                       type="core_api/WaypointClear", id=self.id)
        add_to_job_requests(request)
        return self.handle_return("/" + self.namespace + "/navigation/waypoint_clear", "on_request")

    def pause_waypoints(self):
        """
        This API pauses ongoing waypoint mission.
        :return: {"success": True/False, "message": "debug message"}
        """
        if not self.activated:
            return "WAIT FOR DRONE" + self.namespace + " TO ACTIVATE"
        request = dict(op="call_service", service="/" + self.namespace + "/navigation/waypoint_pause",
                       type="core_api/WaypointPause", id=self.id)
        add_to_job_requests(request)
        return self.handle_return("/" + self.namespace + "/navigation/pause_waypoints", "on_request")

    def set_current_waypoint(self, wp_seq):
        """
        Sets the waypoint Id specified, as the current waypoint from the list of already set wayopints.
        :param wp_seq: Id of the waypoint fro the list of set waypoints.
        :return: {"success": True/False, "message": "debug message"}
        """
        if not self.activated:
            return "WAIT FOR DRONE" + self.namespace + " TO ACTIVATE"
        request = dict(op="call_service", service="/" + self.namespace + "/navigation/waypoint_set_current",
                       type="core_api/WaypointSetCurrent", id=self.id, args=dict(wp_seq=wp_seq))
        add_to_job_requests(request)
        return self.handle_return("/" + self.namespace + "/navigation/waypoint_set_current", "on_request")

    def set_home(self, lat, lon, alt, set_current=False):
        """
        Manually store a location as new home.
        :param lat, lon, alt: Latitude, longitude and relative altitude
        :param set_current: If true uses current location and altitude of the device else uses the provided values.
        :return: {"success": True/False, "message": "debug message"}
        """
        if not self.activated:
            return "WAIT FOR DRONE" + self.namespace + " TO ACTIVATE"
        request = dict(op="call_service", service="/" + self.namespace + "/navigation/set_home",
                       type="core_api/SetHome", id=self.id,
                       args=dict(lat=lat, lon=lon, alt=alt, set_current=set_current))
        add_to_job_requests(request)
        return self.handle_return("/" + self.namespace + "/navigation/set_home", "on_request")

    def RTL(self):
        """
        Trigger RTL mode transition of the vehicle.
        :return: {"success": True/False, "message": "debug message"}
        """
        if not self.activated:
            return "WAIT FOR DRONE" + self.namespace + " TO ACTIVATE"
        request = dict(op="call_service", service="/" + self.namespace + "/navigation/rtl", type="core_api/RTL",
                       id=self.id)
        add_to_job_requests(request)
        return self.handle_return("/" + self.namespace + "/navigation/rtl", "on_request")

    # Parameter APIs
    def set_gimbal(self, roll, pitch, yaw):
        """
        This API sends gimbal attitude setpoint command to the autopilot via
        MAVLink and outputs pwm signals on gimbal-dedicated port of FlytPOD/Pixhawk.
        :param roll: roll command to gimbal in radians
        :param pitch: pitch command to gimbal in radians
        :param yaw: yaw command to gimbal in radians
        :return: {"success": True/False, "message": "debug message"}
        """
        if not self.activated:
            return "WAIT FOR DRONE" + self.namespace + " TO ACTIVATE"
        request = dict(op="call_service", service="/" + self.namespace + "/payload/gimbal_set",
                       type="core_api/GimbalSet", id=self.id, args=dict(roll=roll, pitch=pitch, yaw=yaw))
        add_to_job_requests(request)
        return self.handle_return("/" + self.namespace + "/payload/gimbal_set", "on_request")

    def set_params(self, param_id, param_value):
        """
        This API sets the value of a desired parameter
        :param param_id: Name of the parameter to be updated
        :param param_value: Value of the parameter to be set.
        :return: {"success": True/False, "message": "debug message"}
        """
        if not self.activated:
            return "WAIT FOR DRONE" + self.namespace + " TO ACTIVATE"
        request = dict(op="call_service", service="/" + self.namespace + "/param/param_set", type="core_api/param_set",
                       id=self.id, args=dict(param_id=param_id,param_value=param_value))
        add_to_job_requests(request)
        return self.handle_return("/" + self.namespace + "/navigation/param_set", "on_request")

    def get_all_params(self):
        """
        This API gets all the parameters available in FlytOS with their values.
        :return: {"success": True/False, "message": "debug message"}
        """
        if not self.activated:
            return "WAIT FOR DRONE" + self.namespace + " TO ACTIVATE"
        request = dict(op="call_service", service="/" + self.namespace + "/param/param_get_all",
                       type="core_api/ParamGetAll", id=self.id)
        add_to_job_requests(request)
        return self.handle_return("/" + self.namespace + "/param/param_get_all", "on_request")

    def save_params(self):
        """
        This API saves the parameters to a file which allows data retention on reboot of FlytOS running systems.
        :return: {"success": True/False, "message": "debug message"}
        """
        if not self.activated:
            return "WAIT FOR DRONE" + self.namespace + " TO ACTIVATE"
        request = dict(op="call_service", service="/" + self.namespace + "/param/param_save", type="core_api/ParamSave",
                       id=self.id)
        add_to_job_requests(request)
        return self.handle_return("/" + self.namespace + "/param/param_save", "on_request")

    def load_params(self):
        """
        This API loads parameters from a file where parameters were saved before or a newly uploaded param file.
        :return: {"success": True/False, "message": "debug message"}
        """
        if not self.activated:
            return "WAIT FOR DRONE" + self.namespace + " TO ACTIVATE"
        request = dict(op="call_service", service="/" + self.namespace + "/param/param_load", type="core_api/ParamLoad",
                       id=self.id)
        add_to_job_requests(request)
        return self.handle_return("/" + self.namespace + "/param/param_load", "on_request")

    def delete_params(self, param_id):
        """
        This API deletes a parameter from FlytOS.
        :param param_id: Name of the paramter to be deleted
        :return: {"success": True/False, "message": "debug message"}
        """
        if not self.activated:
            return "WAIT FOR DRONE" + self.namespace + " TO ACTIVATE"
        request = dict(op="call_service", service="/" + self.namespace + "/param/param_delete",
                       type="core_api/ParamDelete", id=self.id)
        add_to_job_requests(request)
        return self.handle_return("/" + self.namespace + "/param/delete_params", "on_request")

    def get_param_value(self, param_id):
        """
        This API gets the value of a particular parameter specified.
        :param param_id: Name of the parameter
        :return: {"success": True/False, "message": "debug message", "param_value":"value"}
        """
        if not self.activated:
            return "WAIT FOR DRONE" + self.namespace + " TO ACTIVATE"
        request = dict(op="call_service", service="/" + self.namespace + "/param/param_get", type="core_api/ParamGet",
                       id=self.id, args=dict(param_id=param_id))
        add_to_job_requests(request)
        return self.handle_return("/" + self.namespace + "/param/param_get", "on_request")

    def reset_params(self):
        """
        This API resets all the parameter value to the last save parameter state.
        :return: {"success": True/False, "message": "debug message"}
        """
        if not self.activated:
            return "WAIT FOR DRONE" + self.namespace + " TO ACTIVATE"
        request = dict(op="call_service", service="/" + self.namespace + "/param/param_reset",
                       type="core_api/ParamReset", id=self.id)
        add_to_job_requests(request)
        return self.handle_return("/" + self.namespace + "/param/param_reset", "on_request")

    def actuator_testing(self, actuator_id, time_s):
        """
        This API allows for testing an actuator by providing actuator ID and time to rotate as parameters.
        If the corresponding actuator rotates on execution of the API correctly for the defined time then
        the motors are correctly connected.
        :param actuator_id: Decide which actuator to trigger.
        :param time_s: Time in seconds to rotate the actuator
        :return: {"success": True/False, "message": "debug message"}
        """
        if not self.activated:
            return "WAIT FOR DRONE" + self.namespace + " TO ACTIVATE"
        request = dict(op="call_service", service="/" + self.namespace + "/setup/actuator_testing",
                       type='core_api/ActuatorTesting', args=dict(actuator_id=actuator_id, time_s=time_s), id=self.id)
        add_to_job_requests(request)
        return self.handle_return("/" + self.namespace + "/setup/actuator_testing", "on_request")

    def ESC_calibration(self, pwm_min,pwm_max,num_of_actuators,calibration_state):
        """
        This API helps calibrate ESCs.
        :param pwm_min: Min PWM value to be expected
        :param pwm_max: Max PWM value to be expected
        :param num_of_actuators: Number of actuator in the frame.
        :param calibration_state: 1/2/3
        :return: {"success": True/False, "message": "debug message"}
        """
        if not self.activated:
            return "WAIT FOR DRONE" + self.namespace + " TO ACTIVATE"
        request = {'op': "call_service", 'service': "/" + self.namespace + "/setup/esc_calibration",
                   'type': "core_api/EscCalibration", 'args': dict(pwm_min=pwm_min, pwm_max=pwm_max,
                                                                   num_of_actuators=num_of_actuators,
                                                                   calibration_state=calibration_state), 'id': self.id}
        add_to_job_requests(request)
        return self.handle_return("/" + self.namespace + "/setup/esc_calibration", "on_request")

    def module_calibration(self, module_calibrate):
        """
        This API helps calibrate accelerometer, magnetometer, gyroscope, level and RC.
        :param module_calibrate: module to calibrate.
                                1: accel
                                2: gyro
                                3: mag
                                4: radio
                                7: level
        :return: {"success": True/False, "message": "debug message"}
        """
        if not self.activated:
            return "WAIT FOR DRONE" + self.namespace + " TO ACTIVATE"
        request = dict(op="call_service", service="/" + self.namespace + "/setup/module_calibration",
                       type="core_api/ModuleCalibration",args={"module_calibrate": module_calibrate},  id=self.id)
        add_to_job_requests(request)
        return self.handle_return("/" + self.namespace + "/setup/module_calibration", "on_request")

    def get_attitude_quaternion(self):
        """
        This API subscribes/polls attitude data (angle and angular rate) in quaternion.
        :return: Instance of class attitude_quaternion
        """
        if not self.activated:
            return "WAIT FOR DRONE" + self.namespace + " TO ACTIVATE"
        request = dict(op="subscribe", topic="attitude", type="random", id=self.id)
        add_to_job_requests(request)
        result = self.get_realtime_data()
        while(True):
            if (('success' not in result) and ('/'+self.namespace+'/mavros/imu/data' in result['real_time'])):
                #print(result)
                if 'succeess' not in result['real_time']['/' + self.namespace + '/mavros/imu/data']['msg']:
                    Response = dict(
                        x=result['real_time']['/' + self.namespace + '/mavros/imu/data']['msg']['orientation']['x'],
                        y=result['real_time']['/' + self.namespace + '/mavros/imu/data']['msg']['orientation']['y'],
                        z=result['real_time']['/' + self.namespace + '/mavros/imu/data']['msg']['orientation']['z'],
                        w=result['real_time']['/' + self.namespace + '/mavros/imu/data']['msg']['orientation']['w'],
                        rollspeed=
                        result['real_time']['/' + self.namespace + '/mavros/imu/data']['msg']['angular_velocity']['x'],
                        pitchspeed=
                        result['real_time']['/' + self.namespace + '/mavros/imu/data']['msg']['angular_velocity']['y'],
                        yawspeed=
                        result['real_time']['/' + self.namespace + '/mavros/imu/data']['msg']['angular_velocity']['z'])
                else:
                    Response = dict(success = "False", reason = result['real_time']['/'+self.namespace+'/mavros/imu/data']['msg']['reason'])
                break
            else:
                result = self.get_realtime_data()
        return Response

    def get_battery_status(self):
        """
        This API subscribes/polls battery status. Please check API usage section below before using API.
        :return: Instance of class battery_status

        """
        if not self.activated:
            return "WAIT FOR DRONE" + self.namespace + " TO ACTIVATE"
        request = dict(op="subscribe", topic="battery_status", type="random", id=self.id)
        add_to_job_requests(request)
        result = self.get_realtime_data()
        while (True):
            if (('success' not in result) and ('/'+self.namespace+'/mavros/battery' in result['real_time'])):
                if 'success' not in result['real_time']['/'+self.namespace+'/mavros/battery']['msg']:
                    Response = dict(voltage = result['real_time']['/' + self.namespace + '/mavros/battery']['msg']['voltage'],
                            current = result['real_time']['/' + self.namespace + '/mavros/battery']['msg']['current'],
                            remaining = result['real_time']['/' + self.namespace + '/mavros/battery']['msg']['percentage'])
                else:
                    Response = dict(success = "False", reason = result['real_time']['/'+self.namespace+'/mavros/battery']['msg']['reason'])
                break
            else:
                result = self.get_realtime_data()
        return Response

    def get_attitude_euler(self):
        """
        This API subscribes/polls attitude data (angle and angular rate) in euler angles.
        :return: Instance of class attitude_euler
        """
        if not self.activated:
            return "WAIT FOR DRONE" + self.namespace + " TO ACTIVATE"
        request = dict(op="subscribe", topic="attitude_euler", type="random", id=self.id)
        add_to_job_requests(request)
        result = self.get_realtime_data()
        while(True):
            if (('success' not in result) and ('/'+self.namespace+'/mavros/imu/data_euler') in result['real_time']):
                if 'success' not in result['real_time']['/' + self.namespace + '/mavros/data_euler']['msg']:
                    Response = dict(
                        roll=
                        result['real_time']['/' + self.namespace + '/mavros/imu/data_euler']['msg']['twist']['linear'][
                            'x'],
                        pitch=
                        result['real_time']['/' + self.namespace + '/mavros/imu/data_euler']['msg']['twist']['linear'][
                            'y'],
                        yaw=
                        result['real_time']['/' + self.namespace + '/mavros/imu/data_euler']['msg']['twist']['linear'][
                            'z'],
                        rollspeed=
                        result['real_time']['/' + self.namespace + '/mavros/imu/data_euler']['msg']['twist']['angular'][
                            'x'],
                        pitchspeed=
                        result['real_time']['/' + self.namespace + '/mavros/imu/data_euler']['msg']['twist']['angular'][
                            'y'],
                        yawspeed=
                        result['real_time']['/' + self.namespace + '/mavros/imu/data_euler']['msg']['twist']['angular'][
                            'z'])
                else:
                    Response = dict(success="False",
                                    reason=result['real_time']['/' + self.namespace + '/mavros/data_euler']['msg'][
                                        'reason'])
                break
            else:
                result = self.get_realtime_data()
        return Response

    def get_local_position(self):
        """
        This API subscribes/polls linear position, velocity data in NED frame.
        :return: Instance of class local_position

        """
        if not self.activated:
            return "WAIT FOR DRONE" + self.namespace + " TO ACTIVATE"
        request = dict(op="subscribe", topic="local_position", type="random", id=self.id)
        add_to_job_requests(request)
        result = self.get_realtime_data()
        while(True):
            if (('success' not in result) and ('/'+self.namespace+'/mavros/local_position/local' in result['real_time'])):
                if 'success' not in result['real_time']['/' + self.namespace + '/mavros/local_position/local']['msg']:
                    Response = dict(
                        x=result['real_time']['/' + self.namespace + '/mavros/local_position/local']['msg']['twist']['linear']['x'],
                        y=result['real_time']['/' + self.namespace + '/mavros/local_position/local']['msg']['twist']['linear']['y'],
                        z=result['real_time']['/' + self.namespace + '/mavros/local_position/local']['msg']['twist']['linear']['z'],
                        vx=result['real_time']['/' + self.namespace + '/mavros/local_position/local']['msg']['twist']['angular']['x'],
                        vy=result['real_time']['/' + self.namespace + '/mavros/local_position/local']['msg']['twist']['angular']['y'],
                        vz=result['real_time']['/' + self.namespace + '/mavros/local_position/local']['msg']['twist']['angular']['z'])
                else:
                    Response = dict(success="False",
                                   reason=
                                   result['real_time']['/' + self.namespace + '/mavros/local_position/local']['msg'][
                                       'reason'])
                break
            else:
                result = self.get_realtime_data()
        return Response  

    def get_global_position(self):
        """
        This API subscribes/polls position data in global coordinate system.
        :return: Instance of class global_position

        """
        if not self.activated:
            return "WAIT FOR DRONE" + self.namespace + " TO ACTIVATE"
        request = dict(op="subscribe", topic="global_position", type="random", id=self.id)
        add_to_job_requests(request)
        result = self.get_realtime_data()
        while(True):
            if (('success' not in result) and ('/'+self.namespace+'/mavros/global_position/global' in result['real_time'])):
                if 'success' not in result['real_time']['/' + self.namespace + '/mavros/global_position/global']['msg']:
                    Response = dict(
                        lat=result['real_time']['/' + self.namespace + '/mavros/global_position/global']['msg'][
                            'latitude'],
                        long=result['real_time']['/' + self.namespace + '/mavros/global_position/global']['msg'][
                            'longitude'],
                        alt=result['real_time']['/' + self.namespace + '/mavros/global_position/global']['msg'][
                            'altitude'])
                else:
                    Response = dict(success = "False", reason = result['real_time']['/'+self.namespace+'/mavros/global_position/global']['msg']['reason'])
                break
            else:
                result = self.get_realtime_data()
        return Response         

    def get_vfr_hud(self):
        """
        This API subscribes/polls VFR HUD data.
        :return: Instance of class vfr_hud

        """
        if not self.activated:
            return "WAIT FOR DRONE" + self.namespace + " TO ACTIVATE"
        request = dict(op="subscribe", topic="VFR_HUD", type="random", id=self.id)
        add_to_job_requests(request)
        result = self.get_realtime_data()
        while (True):
            if (('success' not in result) and ('/'+self.namespace+'/mavros/vfr_hud' in result['real_time'])):
                if 'success' not in result['real_time']['/' + self.namespace + '/mavros/vfr_hud']['msg']:
                    Response = dict(airspeed=result['real_time']['/'+self.namespace+'/mavros/vfr_hud']['msg']['airspeed'],
                                groundspeed=result['real_time']['/'+self.namespace+'/mavros/vfr_hud']['msg']['groundspeed'],
                                heading=result['real_time']['/'+self.namespace+'/mavros/vfr_hud']['msg']['heading'],
                                throttle=result['real_time']['/'+self.namespace+'/mavros/vfr_hud']['msg']['throttle'],
                                altitude=result['real_time']['/'+self.namespace+'/mavros/vfr_hud']['msg']['altitude'],
                                climb=result['real_time']['/'+self.namespace+'/mavros/vfr_hud']['msg']['climb'])
                else:
                    Response = dict(success = "False", reason = result['real_time']['/'+self.namespace+'/mavros/vfr_hud']['msg']['reason'])
                break
            else:
                result = self.get_realtime_data()
        return Response

    def get_rc_data(self):
        """
        This API subscribes/polls the input rc channel data.
        :return: Instance of class rc_data

        """
        if not self.activated:
            return "WAIT FOR DRONE" + self.namespace + " TO ACTIVATE"
        request = dict(op="subscribe", topic="RC_DATA", type="random", id=self.id)
        add_to_job_requests(request)
        result = self.get_realtime_data()
        while (True):
            if (('success' not in result) and ('/'+self.namespace+'/mavros/rc/in' in result['real_time'])):
                if 'success' not in result['real_time']['/' + self.namespace + '/mavros/rc/in']['msg']:
                    Response = dict(rssi=result['real_time']['/'+self.namespace+'/mavros/rc/in']['msg']['rssi'],
                                channels=result['real_time']['/'+self.namespace+'/mavros/rc/in']['msg']['channels'])
                else:
                    Response = dict(success = "False", reason = result['real_time']['/'+self.namespace+'/mavros/rc/in']['msg']['reason'])
                break
            else:
                result = self.get_realtime_data()
        return Response

    def get_vehicle_state(self):
        """
        This API subscribes/polls the vehicle state data.
        :return: Instance of class vehicle_state

        """
        if not self.activated:
            return "WAIT FOR DRONE" + self.namespace + " TO ACTIVATE"
        request = dict(op="subscribe", topic="vehicle_state", type="random", id=self.id)
        add_to_job_requests(request)
        result = self.get_realtime_data()
        while (True):
            if (('success' not in result) and ('/'+self.namespace+'/flyt/state' in result["real_time"])):
                if 'success' not in result['real_time']['/' + self.namespace + '/flyt/state']['msg']:
                    Response = dict(connected=result['real_time']['/'+self.namespace+'/flyt/state']['msg']['connected'],
                                armed=result['real_time']['/'+self.namespace+'/flyt/state']['msg']['armed'],
                                guided=result['real_time']['/'+self.namespace+'/flyt/state']['msg']['guided'],
                                mode=result['real_time']['/'+self.namespace+'/flyt/state']['msg']['mode'],
                                mav_type=result['real_time']['/'+self.namespace+'/flyt/state']['msg']['mav_type'],
                                mav_autopilot=result['real_time']['/'+self.namespace+'/flyt/state']['msg']['mav_autopilot'],
                                mav_sys_status=result['real_time']['/'+self.namespace+'/flyt/state']['msg']['mav_sys_status'])
                else:
                    Response = dict(success = "False", reason = result['real_time']['/'+self.namespace+'/flyt/state']['msg']['reason'])
                break
            else:
                result = self.get_realtime_data()
        return Response

    def get_distance_sensor(self):
        """
        This API subscribes/polls distance sensor data.
        :return: Instance of class dist_sensor
        """
        if not self.activated:
            return "WAIT FOR DRONE" + self.namespace + " TO ACTIVATE"
        request = dict(op="subscribe", topic="distance_sensor", type="random", id=self.id)
        add_to_job_requests(request)
        result = self.get_realtime_data()
        while (True):
            if (('success' not in result) and ('/mavros/distance_sensor/lidarlite_pub' in result['real_time'])):
                if 'success' not in result['real_time']['/' + self.namespace + '/mavros/distance_sensor/lidarlite_pub']['msg']:
                    Response = dict(radiation_type=result['real_time']['/mavros/distance_sensor/lidarlite_pub']['msg'][
                    'radiation_type'],
                                field_of_view=result['real_time']['/mavros/distance_sensor/lidarlite_pub']['msg'][
                                    'field_of_view'],
                                min_range=result['real_time']['/mavros/distance_sensor/lidarlite_pub']['msg'][
                                    'min_range'],
                                max_range=result['real_time']['/mavros/distance_sensor/lidarlite_pub']['msg'][
                                    'max_range'],
                                range=result['real_time']['/mavros/distance_sensor/lidarlite_pub']['msg']['range'])
                else:
                    Response = dict(success = "False", reason = result['real_time']['/'+self.namespace+'/mavros/distance_sensor/lidarlite_pub']['msg']['reason'])
                break
            else:
                result = self.get_realtime_data()
        return Response

    def get_realtime_data(self):
        if not self.activated:
            return "WAIT FOR DRONE" + self.namespace + " TO ACTIVATE"
        return get_data(self.id, 'real_time')

    def get_onrequest_data(self):
        if not self.activated:
            return "WAIT FOR DRONE" + self.namespace + " TO ACTIVATE"
        return get_data(self.id, 'on_request')

    def connect(self):
        return self.handle_return('SOCK_INIT', '')

    def disconnect(self):
        request = dict(type="CLOSE_CONN", id=self.id)
        add_to_job_requests(request)
        return "CLOSE_INITIATED"

    def handle_return(self, path, place):
        if not self.activated:
            return "WAIT FOR DRONE" + self.namespace  + " TO ACTIVATE"
        self.pubsub.subscribe([str(self.id) + place + path])
        print("Processing ", place + path)

        for item in self.pubsub.listen():
            data = item['data']
            a = data.decode('utf-8').replace("'", '"')
            try:
                b = a.replace('True','"True"',10000)
                b = b.replace('False', '"False"', 10000)
                c = json.loads(b)
                d = {
                    "success": c['values']['success'],
                    "message": c['values']['message']
                }
                if 'param_info' in c['values']:
                    d = {
                        "success": c['values']['success'],
                        "message": c['values']['message'],
                        "param_value": c['values']['param_info']['param_value']
                    }
                if 'param_list' in c['values']:
                    d = {
                        "success": c['values']['success'],
                        "message": c['values']['message'],
                        "param_id": c['values']['param_list']['param_id'],
                        "param_value": c['values']['param_list']['param_value']
                    }
            except:
                d = a
                pass
            self.pubsub.unsubscribe([str(self.id) + place + path])
            return d

    def filter_unnecessary(self):
        while True:
            time.sleep(1.9)
            raw_data = r.get(self.id)
            data = None
            if raw_data:
                try:
                    data = json.loads(raw_data)
                    keys1 = data["real_time"].keys()
                    keys2 = data["on_request"].keys()
                    for key in keys1:
                        if data['real_time'][key]:
                            if time.time() - data["real_time"][key]['ts'] > self.time_constant:
                                data["real_time"][key] = {}
                                r.set(self.id, json.dumps(data))
                            else:
                                continue
                        else:
                            continue
                    for key in keys2:
                        if not data["on_request"][key]:
                            continue
                        else:
                            if time.time() - data["on_request"][key]['ts'] > self.time_constant:
                                data["on_request"][key] = {}
                                r.set(self.id, json.dumps(data))
                except:
                    pass
            else:
                continue
