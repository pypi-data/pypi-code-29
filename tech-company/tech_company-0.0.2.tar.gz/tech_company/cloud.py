# The Cloud
# Sometimes it works, sometimes it doesn't

import random


class Cloud(object):
    @staticmethod
    def is_working(force=False):
        base_chance_to_succeed = 70

        if force:  # seriously we really need the cloud to work today
            return True
        else:
            return random.randrange(100) < base_chance_to_succeed
