# -*- coding: utf-8 -*-
import argparse
import sys
import time
from copy import deepcopy
import redis
import json
from log4python.Log4python import log
import traceback

reload(sys)
logger = log("PriorityTasks")
sys.setdefaultencoding('utf8')


class PriorityTasks:
    '''
    ServerDemo:
        def init_worker(task):
            pass  # process task
        if __name__ == '__main__':
            task = PriorityTasks("Test")
            task.worker(init_worker)
    ClientDemo:
        # priority in ["high", "mid", "low"]
        PriorityTasks("Test").send_task(priority, task_params_json)
    '''
    def __init__(self, redis_conn_info, queue_key=None, work_status_queue_name="txt_redis_working_flag"):
        self.redis_conn_info = redis_conn_info
        self.queue_key = queue_key
        self.work_status_queue_name = work_status_queue_name
        self.key_file_tasks = self.queue_key+"_%s"
        logger.debug("PriorityTasksKey:[%s]" % self.queue_key)
        self.keys_file_tasks = [self.queue_key+"_high", self.queue_key+"_mid", self.queue_key+"_low"]
        self.redisCli = redis.StrictRedis(host=redis_conn_info['host'],
                                          port=redis_conn_info['port'], password=redis_conn_info['password'],
                                          db=redis_conn_info['db'])

    def get_tasks_by_priority(self):
        task = None
        for key_task in self.keys_file_tasks:
            # logger.debug("FetchKey:[%s]" % key_task)
            line = self.redisCli.lpop(key_task)
            if line:
                logger.debug("Key:[%s]; line:[%s]" % (key_task, line))
                task = line
                break
        return task

    def __send_task(self, priority, task_params):
        if not self.queue_key:
            tip = "The QueueKey is None, Nothing to Do."
            logger.error(tip)
            print(tip)
            return None

        queue_key = self.get_priority_queue(priority)
        conn_info = deepcopy(self.redis_conn_info)
        conn_info['password'] = "******"
        logger.debug("RedisInfo:[%s]; QueueKey:[%s]" % (json.dumps(conn_info,ensure_ascii=False), queue_key))
        self.redisCli.rpush(queue_key, task_params)

    def send_high_task(self, task_params):
        self.__send_task("high", task_params)

    def send_mid_task(self, task_params):
        self.__send_task("mid", task_params)

    def send_low_task(self, task_params):
        self.__send_task("low", task_params)

    def get_priority_queue(self, priority):
        key_process_priority = self.key_file_tasks % "high"
        if priority in ["high", "mid", "low"]:
            key_process_priority = self.key_file_tasks % priority
        else:
            logger.error("Log priority Level Not Found [%s]" % priority)
        return key_process_priority

    def worker(self, task_func):
        if not self.queue_key:
            tip = "The QueueKey is None, Nothing to Do."
            logger.error(tip)
            print(tip)
            return None

        work_status = False
        work_flag = self.redisCli.get(self.work_status_queue_name)
        conn_info = deepcopy(self.redis_conn_info)
        conn_info['password'] = "******"
        logger.debug("TasksRedisInfo:[%s]" % json.dumps(conn_info,ensure_ascii=False))
        if work_flag == "on":
            work_status = True
            logger.debug("CurrentTaskSwitchKey:[%s]; InitWork: Status is ON!!! " % self.work_status_queue_name)
        else:
            work_status = False
            logger.debug("CurrentTaskSwitchKey:[%s]; InitWork: Status is OFF!!!  Nothing to do...." % self.work_status_queue_name)

        while True:
            work_flag = self.redisCli.get(self.work_status_queue_name)
            if work_flag != "on":
                if work_status:
                    logger.debug("Work Status Change to OFF!!! ")
                work_status = False
                time.sleep(1)
                continue
            else:
                if work_status is False:
                    logger.debug("Work Status Change to ON!!! ")
                work_status = True

            task = self.get_tasks_by_priority()
            if task is None:
                time.sleep(1)
                continue

            task_func(task)

if __name__ == '__main__':
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument("logFile", type=str, help="specify the log file's path")
        args = parser.parse_args()
        print(args.logFile)
    except Exception, ex:
        logger.debug("Error: %s" % ex)
        logger.debug(traceback.format_exc())
