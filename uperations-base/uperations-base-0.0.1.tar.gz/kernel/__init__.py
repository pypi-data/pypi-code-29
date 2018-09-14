
from operations.base import Base

LIBRARIES = {
    Base.name(): Base()
}

#EVENTS = {
#    TestEvent: [
#        Testlistener
#    ]
#}

def find_operation(library, operation):
    for tmp_lib in LIBRARIES:
        if tmp_lib == library:
            for op in LIBRARIES[tmp_lib].operations():
                if LIBRARIES[tmp_lib].operations()[op].name() == operation:
                    return LIBRARIES[tmp_lib].operations()[op]
            raise Exception("The operation %s:%s does not exist. " % (library, operation))
        raise Exception("The libary %s does not exist." % (library))