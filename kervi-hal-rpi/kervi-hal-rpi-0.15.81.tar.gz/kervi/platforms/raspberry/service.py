import os
import sys
import subprocess
            
from kervi.core.utility.superformatter import SuperFormatter

_service_file_template = """
[Unit]
Description=Kervi python application: {app_name}
After=multi-user.target

[Service]
Type=idle
ExecStart={python_path} {script_path} --as-service

[Install]
WantedBy=multi-user.target
"""

_install_path = "/etc/systemd/system/"


def service_manager(commands, app_name, app_id, script_path):
    
    service_name = "kervi_service_"+app_id
    service_file_path = _install_path + "kervi_service_" + app_id + ".service"
    for command in commands:
        if command=="start":
            print("Starting service %s" % (service_name))
            try:
                print("start service:", service_name)
                subprocess.check_call(["systemctl", "start", service_name], stderr=sys.stderr, stdout=sys.stdout)
            except Exception as ex:
                print("Error starting service:", ex)

        elif command=="stop":
            print("Stopping service %s" % (service_name))
            subprocess.check_call(["systemctl", "stop", service_name])
        
        elif command=="restart":
            print("Restarting service %s" % (service_name))
            subprocess.check_call(["systemctl", "restart", service_name])
        
        elif command == "status":
            print("get status for service", service_name)
            subprocess.check_call(["systemctl", "status", service_name], stderr=sys.stderr, stdout=sys.stdout)

        elif command=="install":
            print("Installing kervi application as service %s" % (service_name))
            sf = SuperFormatter()
            service_file_text = sf.format(
                _service_file_template,
                python_path = sys.executable,
                script_path= script_path,
                app_name=app_name
            )

            with open(service_file_path, "w") as text_file:
                text_file.write(service_file_text)
            subprocess.check_call(["systemctl", "daemon-reload"])
            subprocess.check_call(["systemctl", "enable", service_name])

        elif command=="uninstall":
            print("uninstall service %s" % (service_name))
            subprocess.check_call(["systemctl", "stop", service_name])
            os.remove(service_file_path)
            subprocess.check_call(["systemctl", "daemon-reload"])
            
            
        else:
            print("Unknown command - '%s'" % command)
        
