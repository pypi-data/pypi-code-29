import os
import json
from  chatqhelper.debug import logger
import paho.mqtt.client as mqtt
import traceback
from chatqhelper import exceptions


logger = logger("chatqhelper.mqtt")


class MqttClient(mqtt.Client):
    def __init__(self):
        super(MqttClient, self).__init__()
        self.ignore_topics = set()
        self.is_log_request = False

    def ignore(self, topic):
        self.ignore_topics.add(topic)

    def log_request(self, is_log=True):
        self.is_log_request = is_log

    def _handle_on_message(self, message):
        try:
            if message.topic.strip() in self.ignore_topics:
                return

            message.payload = json.loads(message.payload.decode('utf-8'))
            if self.is_log_request:
                logger.info("request: " + message.topic.strip() + " -- " + str(message.payload))

            # Call handle message on new payload
            super(MqttClient, self)._handle_on_message(message)
        except Exception as e:
            self.publish_exception(e, message)

    def publish_exception(self, exception, message):
        code = getattr(exception, 'code', 500)
        logger.error(
            'exception from message: {0} {1}'.format(
                message.topic,
                str(message.payload)
            )
        )

        error = json.dumps({
            'exception': str(exception.__class__.__name__),
            'message': str(exception),
            'code': code
        })

        traceback.print_exc()
        logger.error(error)
        try:
            data = message.payload
            correlation_id = data.get('correlation_id', None)
            if correlation_id is not None:
                self.publish(
                    message.topic + '/reply-to/' + str(correlation_id),
                    error
                )
            else:
                self.publish('chat/exception', error)
        except Exception:
            pass

    def reply(self, msg, data, log_response=False):
        topic = msg.topic + "/reply-to/" + str(msg.payload.get('correlation_id'))
        payload = json.dumps(data)
        if log_response:
            logger.info("reply: " + topic + " -- " + str(payload))

        self.publish(topic, payload)

    @classmethod
    def create(cls, on_connect, is_log_request=False):
        client = cls()
        client.log_request(is_log_request)
        client.on_connect = on_connect
        client.username_pw_set(
            username=os.environ.get('SOL_USERNAME', ''),
            password=os.environ.get('SOL_PASSWORD', '')
        )

        client.connect_async(
            os.environ.get('SOL_URI', ''),
            int(os.environ.get('SOL_MQTT_PORT', '0')),
            60
        )

        return client
