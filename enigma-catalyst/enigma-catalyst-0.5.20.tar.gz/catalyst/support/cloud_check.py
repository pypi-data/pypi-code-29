from logbook.queues import ZeroMQSubscriber
from logbook import StderrHandler

my_handler = StderrHandler()
subscriber = ZeroMQSubscriber("tcp://20.20.20.20:6965")
#subscriber = ZeroMQSubscriber('tcp://127.0.0.1:5050', multi=True)
controller = subscriber.dispatch_in_background(my_handler)
a = True
while a:
    if not a:
        a = False

controller.stop()
subscriber.close()