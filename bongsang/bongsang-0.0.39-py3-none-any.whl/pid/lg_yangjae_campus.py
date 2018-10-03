# Bongsang EMS AI Simulator
from .building import RemoteControl_v03 as RemoteControl
######################################################
# Real World Building Model                          #
######################################################


class LgYangjaeCampus_v02():
    def __init__(self):
        self.simulator = RemoteControl()

    def login(self):
        self.simulator.login()

    def logout(self):
        self.simulator.login()

    def set_mode_manual(self):
        self.simulator.set_mode('manual')
    
    def set_mode_auto(self):
        self.simulator.set_mode('auto')

    def get_mode(self):
        return self.simulator.get_mode()

    def set_output(self, valve, output):
        self.simulator.set_output(valve, output)

    def get_output(self, valve):
        return self.simulator.get_output(valve)

    def get_temperature(self):
        return self.simulator.get_temperatue()


# class LgYangjaeCampus_v01():
#     def __init__(self):
#         self.simulator = RemoteControl()

#     def login(self):
#         self.simulator.login()

#     def logout(self):
#         self.simulator.login()

#     def set_mode_manual(self):
#         self.simulator.set_mode('manual')
    
#     def set_mode_auto(self):
#         self.simulator.set_mode('auto')

#     def get_mode(self):
#         return self.simulator.get_mode()

#     def set_output(self, output):
#         self.simulator.set_output(output)

#     def get_output(self, valve='cooling'):
#         return self.simulator.get_output(valve)

#     def get_temperature(self):
#         return self.simulator.get_temperatue()

