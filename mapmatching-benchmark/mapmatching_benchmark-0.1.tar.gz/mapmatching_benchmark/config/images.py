
class Images:
    def __init__(self, properties: dict=None):
        self.path = properties.get("path")
        self.main_comparison = properties.get("main_comparison")
        self.accuracy_period = properties.get("accuracy_period")
        self.accuracy_time = properties.get("accuracy_time")
        self.time_period = properties.get("time_period")
        self.cost_count = properties.get("cost_count")


        pass

