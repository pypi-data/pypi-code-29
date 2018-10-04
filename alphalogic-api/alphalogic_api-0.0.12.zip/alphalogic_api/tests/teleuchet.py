# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import time
import requests
from datetime import datetime
import traceback
import base64

from functools import partial
from alphalogic_api import options
from alphalogic_api.objects import Root, Object
from alphalogic_api.attributes import Visible, Access
from alphalogic_api.objects import ParameterBool, ParameterLong, ParameterDouble, ParameterDatetime, ParameterString
from alphalogic_api.decorators import command, run
from alphalogic_api.logger import log
from alphalogic_api import init


class AuthError(Exception):
    pass


class DiagHelper(object):
    """
    Класс упрощающий работу с диагностическим пакетом адаптера.
    Он также спускает вниз по дереву reset()
    """

    def reset(self):
        self.state_no_connection('reset')
        for node in self.children():
            node.reset()

    def state_connected(self, reason=''):
        self.manager.state_connected(self.id, reason)

    def state_no_connection(self, reason=''):
        self.manager.state_no_connection(self.id, reason)

    def state_error(self, reason=''):
        log.error(reason)
        self.manager.state_error(self.id, reason)

    def state_ok(self, reason=''):
        self.manager.state_ok(self.id, reason)


class TeleuchetAPI(object):

    def __init__(self, url, token, timeout):
        self.url = url
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update({'Authorization': 'Basic ' + base64.b64encode(token)})

    def get_json(self, url):
        r = self.session.get(url, timeout=self.timeout)
        self.check_status(r)
        return r.json()

    def get_hubs(self):
        return self.get_json('{0}/hubs'.format(self.url))['hubs']

    def get_hub(self, id):
        return self.get_json('{0}/hubs/{1}'.format(self.url, id))

    def get_meters(self, id):
        return self.get_json('{0}/hubs/{1}/meters'.format(self.url, id))

    def get_meter(self, hub_id, id):
        j = self.get_meters(hub_id)
        j = [m for m in j if m['meterId'] == id]
        return j[0] if j else None

    def get_meter_sensors(self, id):
        return self.get_json('{0}/meters/{1}/functions'.format(self.url, id))

    def get_sensors(self, hub_id):
        return self.get_json('{0}/hubs/{1}/sensors'.format(self.url, hub_id))

    def get_sensor(self, id):
        return self.get_json('{0}/sensors/{1}/metaData'.format(self.url, id))

    def get_sensor_value(self, id):
        return self.get_json('{0}/sensors/{1}/current'.format(self.url, id))

    @staticmethod
    def check_status(r):
        if r.ok:
            return

        codes = {
            400: 'Не корректный запрос',
            401: 'Ошибка авторизации',
            403: 'Нет доступа. Для данного пользователя нет доступа к запрашиваемым данным.',
            404: 'Запрашиваемый ресурс не найден',
            500: 'Общий сбой на стороне сервера',
            501: 'Указанный запрос не может быть обработан',
            502: 'Ошибка обработки запроса Услугой',
            503: 'Временный сбой на стороне сервера. Следует повторить запрос через >5 секунд',
            504: 'Тайм-аут обработки запроса Услугой'
        }

        if r.status_code in codes:
            if r.status_code == 401:
                raise AuthError(codes[r.status_code])
            raise Exception('HTTP {}: {}'.format(r.status_code, codes[r.status_code]))  #TODO
        else:
            status = 'HTTP {}'.format(r.status_code)
            raise Exception(status)  #TODO


def handle_set_id(node, parameter):
    try:
        node.reset()
        node.update()
    except Exception as err:
        node.state_error(err.message)


class SensorType(object):
    boolean = 0
    integer = 1
    double = 2
    blob = 3
    string = 4


class Sensor(Object, DiagHelper):
    """
    {"sensorId":136885,"name":"Масса за час","sensorType":2,"period":60,
    "valueType":3,"suffix":null,"unit":null,"offset":0,"length":4,"isVirtual":false,"isCritical":true}
    """
    sensorId = ParameterLong(default=0, callback=handle_set_id, visible=Visible.common)
    sensorName = ParameterString(visible=Visible.common, access=Access.read_only)
    sensorType = ParameterLong(choices=((1, 'Аналоговый'), (2, 'Цифровой')),
                               visible=Visible.runtime, access=Access.read_only)
    sensorPeriod = ParameterLong(visible=Visible.common, access=Access.read_only)
    valueType = ParameterLong(choices=((SensorType.boolean, 'Bool'),
                                       (SensorType.integer, 'Int'),
                                       (SensorType.double, 'Double'),
                                       (SensorType.blob, 'Blob'),
                                       (SensorType.string, 'String')),
                              visible=Visible.runtime, access=Access.read_only)
    valueT = ParameterLong(visible=Visible.runtime, access=Access.read_only)

    unit = ParameterString(visible=Visible.common, access=Access.read_only)
    offset = ParameterLong(visible=Visible.common, access=Access.read_only)
    length = ParameterLong(visible=Visible.common, access=Access.read_only)
    isVirtual = ParameterBool(visible=Visible.common, access=Access.read_only)
    isCritical = ParameterBool(visible=Visible.common, access=Access.read_only)

    bool_value = ParameterBool(visible=Visible.runtime, access=Access.read_only)
    int_value = ParameterLong(visible=Visible.runtime, access=Access.read_only)
    string_value = ParameterString(visible=Visible.runtime, access=Access.read_only)
    double_value = ParameterDouble(visible=Visible.runtime, access=Access.read_only)

    value_timestamp = ParameterDatetime(visible=Visible.runtime, access=Access.read_only)

    def handle_prepare_for_work(self):
        self.reset()
        self.update()

    def update(self):
        try:
            if self.parent().ready_to_work.val:
                if not self.ready_to_work.val:
                    j = self.root().api.get_sensor(self.sensorId.val)
                    self.sensorName.val = j['name']
                    self.sensorType.val = j['sensorType']
                    self.sensorPeriod.val = j['period']
                    self.valueType.val = j['valueType']
                    self.valueT.val = j['valueType']
                    self.unit.val = j['unit']
                    self.offset.val = j['offset']
                    self.length.val = j['length']
                    self.isVirtual.val = j['isVirtual']
                    self.isCritical.val = j['isCritical']

                    self.update_value()

        except Exception as err:
            self.state_no_connection(err.message)

    def update_value(self):
        try:
            j = self.root().api.get_sensor_value(self.sensorId.val)

            if self.sensorType.val == SensorType.boolean:
                self.bool_value.val = bool(j['value'])
            elif self.sensorType.val == SensorType.integer:
                self.int_value.val = int(j['value'])
            elif self.sensorType.val == SensorType.double:
                self.double_value.val = float(j['value'])
            else:
                self.string_value.val = j['value']

            self.value_timestamp.val = datetime.strptime(j['date'], '%Y-%m-%dT%H:%M:%S')

            self.state_ok('OK')

        except Exception as err:
            self.state_error(err.message)

    def run_function(self):
        if self.parent().connected.val and not self.connected.val:
            self.update()
        else:
            self.update_value()

    @run(period_one=10)
    def run(self):
        self.run_function()


class Meter(Object, DiagHelper):
    """
    {"meterId":478,"meterName":"1","meterAddress":"1","meterModel":
    "ВИС.Т","meterVendor":"Логика","hubConnectionId":4604,"hubConnectionName":"U1"
    """
    meterId = ParameterLong(default=0, callback=handle_set_id, visible=Visible.common)
    meterName = ParameterString(visible=Visible.runtime, access=Access.read_only)
    meterModel = ParameterString(visible=Visible.runtime, access=Access.read_only)
    meterVendor = ParameterString(visible=Visible.runtime, access=Access.read_only)
    meterAddress = ParameterString(visible=Visible.runtime, access=Access.read_only)
    hubConnectionName = ParameterString(visible=Visible.runtime, access=Access.read_only)

    def handle_prepare_for_work(self):
        self.reset()
        self.update()

    def handle_get_available_children(self):
        p = partial(Sensor, sensorId=0)
        p.cls = Sensor
        children = [(p, 'Sensor')]
        for h in self.root().api.get_meter_sensors(self.meterId.val):
            if 'sensorId' in h and 'name' in h:
                p = partial(Sensor, sensorId=h['sensorId'], displayName=h['name'])
                p.cls = Sensor
                children.append((p, h['name']))
        return children

    def update(self):
        try:
            if self.parent().ready_to_work.val:
                if not self.ready_to_work.val:
                    j = self.root().api.get_meter(self.parent().hubId.val, self.meterId.val)
                    if not j:
                        raise Exception('Не найден')

                    self.meterName.val = j['meterName']
                    self.meterModel.val = j['meterModel']
                    self.meterVendor.val = j['meterVendor']
                    self.meterAddress.val = j['meterAddress']
                    self.hubConnectionName.val = j['hubConnectionName']
                    self.state_ok('OK')

        except Exception as err:
            log.error(traceback.format_exc().decode('utf-8'))
            self.state_no_connection(err.message)


class Hub(Object, DiagHelper):
    hubId = ParameterLong(default=0, callback=handle_set_id, visible=Visible.common)
    hubName = ParameterString(visible=Visible.runtime, access=Access.read_only)
    groupName = ParameterString(visible=Visible.runtime, access=Access.read_only)
    customerName = ParameterString(visible=Visible.runtime, access=Access.read_only)
    lastOnlineDate = ParameterDatetime(visible=Visible.runtime, access=Access.read_only)
    description = ParameterString(visible=Visible.runtime, access=Access.read_only)

    def handle_prepare_for_work(self):
        self.reset()
        self.update()

    def handle_get_available_children(self):
        p = partial(Meter, meterId=0)
        p.cls = Meter
        children = [(p, 'Meter')]
        for h in self.root().api.get_meters(self.hubId.val):
            if 'meterId' in h and 'meterName' in h:
                p = partial(Meter, meterId=h['meterId'], displayName=h['meterName'])
                p.cls = Meter
                children.append((p, h['meterName']))
        return children

    def update(self):
        try:
            if self.parent().ready_to_work.val:
                if not self.ready_to_work.val:
                    j = self.root().api.get_hub(self.hubId.val)
                    self.hubName.val = j['name']
                    self.customerName.val = j['сustomerName']  #russian
                    self.groupName.val = j['groupName']
                    self.lastOnlineDate.val = datetime.strptime(j['lastOnlineDate'], '%Y-%m-%dT%H:%M:%S.%f')
                    self.description.val = j['description']
                    self.state_ok('OK')

        except Exception as err:
            log.error(traceback.format_exc().decode('utf-8'))
            self.state_no_connection(err.message)


def handle_change_api(node, parameter):
    node.api = TeleuchetAPI(node.url.val, node.token.val, node.timeout.val)
    node.reset()


class TeleuchetRoot(Root, DiagHelper):

    # parameters
    url = ParameterString(default='https://api.m2mconnect.ru/v1/api', callback=handle_change_api, visible=Visible.setup)
    token = ParameterString(callback=handle_change_api, visible=Visible.setup)
    timeout = ParameterDouble(default=3.0, callback=handle_change_api, visible=Visible.setup)
    api = None
    #last_event_time = ParameterDatetime(visible=Visible.hidden, access=Access.read_only)

    def handle_prepare_for_work(self):
        self.reset()
        self.api = TeleuchetAPI(self.url.val, self.token.val, self.timeout.val)
        self.run_function()

    def handle_get_available_children(self):
        p = partial(Hub, hubId=0)
        p.cls = Hub
        children = [(p, 'Hub')]
        try:
            for h in self.api.get_hubs():
                if 'name' in h and 'hubId' in h:
                    p = partial(Hub, hubId=h['hubId'], displayName=h['name'])
                    p.cls = Hub
                    children.append((p, h['name']))
        except Exception as err:
            log.error(err.message)
        return children

    def update(self):
        def upd(node):
            for child in node.children():
                child.update()
                upd(child)
        upd(self)

    def run_function(self):
        try:
            if not self.ready_to_work.val:
                self.api.get_hubs()  # проверка связи с сервером
                self.state_ok('OK')
                self.update()

            if self.ready_to_work.val:
                # TODO wait events
                self.update()
                self.state_ok('OK')

        except AuthError as err:
            self.state_no_connection(err.message)

        except Exception as err:
            t = traceback.format_exc().decode('utf-8')
            self.state_error(t)

    @run(period=20)
    def run(self):
        self.run_function()


if __name__ == '__main__':

    root = TeleuchetRoot()
    root.join()
