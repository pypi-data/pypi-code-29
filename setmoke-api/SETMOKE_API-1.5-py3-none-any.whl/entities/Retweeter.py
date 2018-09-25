class Retweeter:
    def __init__(self):
        self.display_name = None
        self.display_picture = None
        self.time = None




    def set_display_name(self, display_name):
        self.display_name = display_name

    def set_display_picture(self, display_picture):
        self.display_picture = display_picture

    def set_time(self, time):
        self.time = time



    def get_display_name(self):
        return self.display_name

    def get_display_picture(self):
        return self.display_picture

    def get_time(self):
        return self.time
