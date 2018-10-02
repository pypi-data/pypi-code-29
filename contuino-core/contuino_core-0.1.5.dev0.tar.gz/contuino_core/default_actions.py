# -*- coding: utf-8 -*-

from enum import Enum


class Events(Enum):
    """Predefined Events"""
    PICK_UP = 0
    HIT = 1
    SHOOT = 2
    SPRINT = 3
    JUMP = 4
    CROUCH = 5
    PRONE = 6
    STAND = 7
    RELOAD = 8
    MOVE_UP = 9
    MOVE_LEFT = 10
    MOVE_RIGHT = 11
    MOVE_DOWN = 12
    MOVE_FORWARD = 13
    MOVE_BACKWARD = 14
    ROTATION = 15
    MENU = 16
    NEXT = 17
    PREVIOUS = 18
    TOGGLE_1 = 19
    TOGGLE_2 = 20
    TOGGLE_3 = 21
    TOGGLE_4 = 22
    TOGGLE_5 = 23
    SLOT_1 = 24
    SLOT_2 = 25
    SLOT_3 = 26
    SLOT_4 = 27
    SLOT_5 = 28
    CUSTOM_1 = 29
    CUSTOM_2 = 30
    CUSTOM_3 = 31
    CUSTOM_4 = 32
    CUSTOM_5 = 33


class Sensors(Enum):
    """Predefined Sensors"""
    CUSTOM = 0
    WATER_LEVEL = 1
    LIGHT = 2
    INFRARED_PROXIMITY = 3
    INFRARED_TEMPERATURE = 4
    INFRARED_RECEIVER = 5
    TEMPERATURE = 6
    HUMIDITY = 7
    PRESSURE = 8
    BAROMETER = 9
    MICROPHONE = 10
    GAS = 11
    SWITCH = 12
    TILT_SWITCH = 13
    TRACK_BALL = 14
    HCHO = 15
    ACCELEROMETER = 16
    GYROSCOPE = 17
    COMPASS = 18
    BUTTON = 19
    CABLE = 20
    CAMERA = 21
    MOTION = 22
    TOUCH = 23
    ALCOHOL = 24
    WATER = 25
    HALL = 26
    AIR_QUALITY = 27
    SERVO = 28
    THUMB_JOYSTICK = 29
    LINE_FINDER = 30
    PIEZO = 31
    GPS = 32
    MOISTURE = 33
    GESTURE = 34
    DUST = 35
    KNOCK = 36
    KEYPAD = 37
    POTENTIOMETER = 38
