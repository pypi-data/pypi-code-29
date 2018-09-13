'''
Created on 11 de set de 2018

@author: koliveirab
'''
import json
from locust import HttpLocust, TaskSet
from locust import task

class Tasks(TaskSet):
    @task
    def index(self):
        self.client.get("/")

class WebsiteUser(HttpLocust):
    host = "http:localhost:8000/users"
    task_set = Tasks
    min_wait = 2000
    max_wait = 3000