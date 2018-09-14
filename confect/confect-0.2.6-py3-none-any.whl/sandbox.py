from types import DynamicClassAttribute

import confect


class A:
    b = {0: 3}

    @DynamicClassAttribute
    def name(self):
        return self[0]


a = A()


conf = confect.new_conf()


conf.prop()
