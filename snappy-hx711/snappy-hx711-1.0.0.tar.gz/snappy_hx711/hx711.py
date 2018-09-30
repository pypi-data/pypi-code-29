""" SNAPpy library for the HX711 Load Cell Amplifier."""

OUTPUT = True
INPUT = False

HIGH = True
LOW = False

# Globals:
hx711_clock_pin = None
hx711_data_pin = None
hx711_gain = 1
hx711_ready_timeout = 10  # Wait up to 10ms for HX711 to become ready


def hx711_begin(clock_pin, data_pin):
    """Sets up the clock and data pins for the HX711.

    Note: This must be called before making any readings.
    """
    global hx711_clock_pin, hx711_data_pin
    hx711_clock_pin = clock_pin
    hx711_data_pin = data_pin

    setPinDir(hx711_clock_pin, OUTPUT)
    writePin(hx711_clock_pin, LOW)
    setPinDir(hx711_data_pin, INPUT)


def hx711_set_gain(new_hx711_gain):
    """Sets the gain level and channel for the HX711.

    Three values are allowed for `new_hx711_gain`: 128, 64, and 32.
    Gain values of 128 and 64 use input channel A, while gain value
    32 uses channel B.

    Returns "Invalid gain value" if an invalid gain is provided.
    """
    global hx711_gain
    if new_hx711_gain == 128:   # input channel A, gain factor 128
        hx711_gain = 1
    elif new_hx711_gain == 64:  # input channel A, gain factor 64
        hx711_gain = 3
    elif new_hx711_gain == 32:  # input channel B, gain factor 32
        hx711_gain = 2
    else:
        return "Invalid gain value"

    hx711_read()
    return hx711_gain


def hx711_read():
    """Makes and returns a measurement.

    Returns a measurement in the form of a 3-byte string that represents
    a signed 24-bit value.

    Returns "Not ready" if the HX711 ready check times out.
    """
    global hx711_ready_timeout

    i = 0
    while not hx711_is_ready():
        pulsePin(-1, -1000)
        i += 1
        if i == hx711_ready_timeout:
            return "Not ready"

    byte2 = None  # MSB
    byte1 = None
    byte0 = None  # LSB

    i = 0
    current_byte = 0
    while i < 8:
        pulsePin(hx711_clock_pin, -1, HIGH)
        current_byte = (current_byte << 1) + int(readPin(hx711_data_pin))
        i += 1
    byte2 = current_byte

    current_byte = 0
    while i < 16:
        pulsePin(hx711_clock_pin, -1, HIGH)
        current_byte = (current_byte << 1) + int(readPin(hx711_data_pin))
        i += 1
    byte1 = current_byte

    current_byte = 0
    while i < 24:
        pulsePin(hx711_clock_pin, -1, HIGH)
        current_byte = (current_byte << 1) + int(readPin(hx711_data_pin))
        i += 1
    byte0 = current_byte

    # Set the gain for the next measurement
    i = 0
    while i < hx711_gain:
        pulsePin(hx711_clock_pin, -1, HIGH)
        i += 1

    return chr(byte2) + chr(byte1) + chr(byte0)


def hx711_is_ready():
    """Determines if the HX711 is ready for measurement.

    Returns True if the HX711 is ready, otherwise returns False.
    """
    return readPin(hx711_data_pin) == LOW
