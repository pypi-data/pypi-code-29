import demjson
import os


dependencies = lambda:"dependencies"

def load_config(config_path, handler):

    def handle(dep_data):
        def handle_config(config_data):
            if dependencies() in config_data:
                [handle(dep) for dep in config_data[dependencies()]]
                
        handle_config(handler(dep_data))

    def handle_from_root(config_data):
        if dependencies() in config_data:
            [handle(dep) for dep in config_data["dependencies"]]

    handle_from_root(demjson.decode_file(config_path))
     
