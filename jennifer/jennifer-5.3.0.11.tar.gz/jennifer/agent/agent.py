import os
import json
import socket
import struct
import logging
import sys
import time
import threading
import traceback
import zlib
from random import random
from jennifer.api import task
from jennifer.recorder import Recorder
from jennifer.api import task
from .transaction import Transaction

record_types = {
    'method': 1,
    'sql': 2,
    'event_detail_msg': 3,
    'service': 4,
    'txcall': 5,
    'browser_info': 6,
    'thread_name': 7,
    'thread_stack': 8,
    'user_id': 9,
    'dbc': 10,
    'stack_trace': 11,
    'count': 12,
}


class Agent(object):
    def __init__(self):
        self.transactions = []
        self.inst_id = -1
        self.recorder = None
        self.master_lock = threading.Lock()
        self.logger = logging.getLogger('jennifer')
        self.config_pid = 0

    def gen_new_txid(self):
        return int(str(int(random() * 100)) + str(self.current_time()))

    def current_time(self):
        return int(time.time() * 1000)

    def current_cputime(self):
        if hasattr(time, 'process_time'):
            return int(time.process_time() * 1000)
        return int(time.clock() * 1000)

    def current_thread_id(self):
        return threading.get_ident()

    def current_thread(self):
        return threading.current_thread()

    def current_transaction(self):
        ret = None
        thread_id = self.current_thread_id()
        for t in self.transactions:
            if t.thread_id == thread_id:
                ret = t
                break
        return ret

    def set_config(self, config):
        self.address = config['address']
        self.recorder = Recorder()
        self.config_pid = os.getpid()

        self.master_lock.acquire()
        ret = self.connect_master()
        self.master_lock.release()
        if ret:
            task.run_timer(self.agent_loop)

    def connect_master(self):
        self.master = None
        if not os.path.exists(self.address):
            return False
        try:
            self.master = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
            self.master.connect(self.address)
            self.handshake_to_master()
            task.run_task(self.master_loop)
            return True
        except ConnectionRefusedError as e:
            self.master = None
            return False

    def handshake_to_master(self):
        version = b'{"version":1,"pid":' + \
            str(os.getpid()).encode('utf-8') + b'}'
        self.master.send(b'\x08jennifer' + \
            struct.pack('>L', len(version)) + version)

    def send_to_master(self, cmd, params):
        if os.getpid() != self.config_pid:
            self.set_config({
                'address': self.address
            })
        try:
            p = json.dumps(params, default=str).encode('utf-8')
            pack = struct.pack('>B', len(cmd)) + \
                cmd.encode('utf-8') + \
                struct.pack('>L', len(p)) + \
                p
            self.master_lock.acquire()
            if self.master is None:
                if not self.connect_master():
                    self.master_lock.release()
                    return
            self.master.send(pack)
        except (BrokenPipeError, OSError):
            self.master = None
        self.master_lock.release()

    def agent_loop(self):
        metrics = self.recorder.record_self()
        self.send_to_master('record_metric', metrics)
        current = self.current_time()
        current_cpu = self.current_cputime()
        self.send_to_master('active_service', {
            'active_services': [
                t.to_active_service_dict(current, current_cpu)
                for t in self.transactions
            ],
        })

    def master_loop(self):
        while True:
            if self.master is None:
                break
            try:
                bcmd_len = self.master.recv(1)
                if len(bcmd_len) < 1:
                    break  # failed to connect master
                cmd_len = ord(bcmd_len)
                cmd = self.master.recv(cmd_len)
                param_len, = struct.unpack('>L', self.master.recv(4))
                try:
                    param = json.loads(self.master.recv(param_len))
                except:
                    continue

                if cmd == b'active_detail':
                    txid = param.get('txid')
                    request_id = param.get('request_id')
                    if txid is not None and request_id is not None:
                        data = self.get_active_service_detail(txid)
                        if data is not None:
                            data['request_id'] = request_id
                            self.send_to_master('active_detail', data)
            except (BrokenPipeError, OSError):
                break

    def get_active_service_detail(self, txid):
        ret = None
        cpu_time = self.current_cputime()
        current_time = self.current_time()
        for t in self.transactions:
            if t.txid == txid:
                stack = 'Fail to get a callstack'
                frame = sys._current_frames().get(t.thread_id)
                if frame is not None:
                    stack = ''.join(traceback.format_stack(frame))
                ret = {
                    'txid': t.txid,
                    'thread_id': t.thread_id,
                    'service_name': t.path_info,
                    'elapsed': current_time - t.start_time,
                    'method': t.request_method,
                    'http_query': t.query_string,
                    'sql_count': t.sql_count,
                    'sql_time': t.sql_time,
                    'tx_time': t.external_call_time,
                    'tx_count': t.external_call_count,
                    'fetch_count': t.fetch_count,
                    'cpu_time': cpu_time - t.start_system_time,
                    'start_time': t.start_time,
                    'stack': stack,
                }

        return ret

    def start_transaction(
        self,
        environ,
        wmonid,
        wsgi_handler_name=None,
        start_time=None
    ):
        if start_time is None:
            start_time = self.current_time()
        txid = self.gen_new_txid()
        transaction = Transaction(
            agent=self,
            start_time=start_time,
            txid=txid,
            environ=environ,
            wmonid=wmonid,
        )
        self.transactions.append(transaction)
        transaction.start_system_time = self.current_cputime()
        self.send_to_master('start_transaction', {})
        return transaction

    def end_transaction(self, transaction):
        try:
            self.transactions.remove(transaction)
            self.send_to_master('end_transaction', {
                'transaction': transaction.to_dict(),
                'profiler': transaction.profiler.to_dict(),
            })
        except ValueError:
            pass

    def _hash_text(self, text):
        hashkey = zlib.crc32(text.encode('utf-8'))
        if hashkey > 0x7FFFFFFF:
            return (hashkey & 0x7FFFFFFF) * -1
        return hashkey

    def hash_text(self, text, hash_type='service'):
        if text is None or len(text) is 0:
            return 0
        self.send_to_master('record_text', {
            'type': record_types.get(hash_type, 0),
            'text': text,
        })
        return self._hash_text(text)
