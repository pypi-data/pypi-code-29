import asyncio
import logging
import time
import RPi.GPIO as GPIO
from .snap import get_snapcast_client

logging.basicConfig(level=logging.INFO)
SENSOR_PIN = 7
MUTE_BRIGHTNESS = 0.1


def dark_mute():
    '''Uses brighness level to mute or unmute device'''
    # Snapcast library only supports asynchronous so need to wrap in async loop
    logger = logging.getLogger('darkmute')
    loop = asyncio.new_event_loop()
    client = get_snapcast_client(loop)
    GPIO.setmode(GPIO.BOARD)
    is_muted = client.muted
    try:
        while True:
            brightness = measure_brightness(SENSOR_PIN)
            if brightness < MUTE_BRIGHTNESS and not is_muted:
                # client.muted did not work so need client.set_muted
                # loop used here and also passed into snap.py to get server
                logger.info('muting client')
                loop.run_until_complete(client.set_muted(True))
                is_muted = client.muted
            elif brightness > MUTE_BRIGHTNESS and is_muted:
                logger.info('unmuting client')
                loop.run_until_complete(client.set_muted(False))
                is_muted = client.muted
    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()
        loop.close()


def measure_brightness(pin_to_circuit):
    '''Measure brightness using photoresistor-capacitor circuit.'''
    charge_time = 0

    GPIO.setup(pin_to_circuit, GPIO.OUT)
    GPIO.output(pin_to_circuit, GPIO.LOW)
    time.sleep(0.1)

    GPIO.setup(pin_to_circuit, GPIO.IN)

    while (GPIO.input(pin_to_circuit) == GPIO.LOW):
        charge_time += 1

    return 1000/charge_time


if __name__ == '__main__':
    dark_mute()
