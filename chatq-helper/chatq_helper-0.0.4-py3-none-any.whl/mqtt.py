import os
import json
import logging
import paho.mqtt.client as mqtt
import traceback
from .exceptions import BaseException


logger = logging.getLogger("chat.mqtt")


class ChatqMqttClient(mqtt.Client):
    def _handle_on_message(self, message):
        try:
            # Skip unrelated topic
            if message.topic.strip() == 'bots/heartbeat':
                return

            # Try and decode payload in multiple format
            try:
                message.payload = eval(message.payload)
            except (SyntaxError, NameError, TypeError, ZeroDivisionError):
                message.payload = json.loads(message.payload.decode('utf-8'))

            # For debugging
            logger.info("REQUEST TOPIC: " + message.topic.strip())
            logger.info("REQUEST PAYLOAD: " + str(message.payload))

            # Call handle message on new payload
            super(ChatqMqttClient, self)._handle_on_message(message)
        except BaseException as e:
            self.publish_exception(e, message, code=e.code)
        except Exception as e:
            self.publish_exception(e, message)

    def publish_exception(self, exception, message, code=500):
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
            logger.info("REPLY TOPIC: " + topic)
            logger.info("REPLY PAYLOAD: " + payload)

        self.publish(topic, payload)

    @classmethod
    def get_client(cls, on_connect):
        client = cls()
        client.on_connect = on_connect
        client.username_pw_set(
            username=os.environ.get('SOL_USERNAME', ''),
            password=os.environ.get('SOL_PASSWORD', ''))
        client.connect_async(
            os.environ.get('SOL_URI', ''), int(os.environ.get('SOL_MQTT_PORT', '0')),
            60)
        return client
