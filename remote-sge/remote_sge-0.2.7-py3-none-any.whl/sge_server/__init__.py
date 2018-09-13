"""
Main entry point into server application, given to gunicorn for serving the restful API.
"""
import json
import falcon
from sge.io.config import load_config
from sge_server import views, server_config

CONFIG = server_config.ServerConfig(load_config())

# if not isdir(SERVER_CONFIG.get('work_root')) or not isdir(SERVER_CONFIG.get('completed_files_root')):
#     raise ValueError("Check config file and ensure that work_root and completed_files_root exist.")

app = falcon.API()

app.add_route("/", views.DefaultRoute())
app.add_route("/jobs", views.JobCollection(CONFIG))
app.add_route("/jobs/{job_id}", views.JobItem(CONFIG))
