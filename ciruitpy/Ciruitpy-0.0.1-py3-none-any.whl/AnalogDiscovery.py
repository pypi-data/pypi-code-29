import dwf
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation


def generate_wave(device=None, channel=0, node=None, func=None, freq=1000, amp=5, offset=0, phase=0):
    close_when_done = False
    if device is None:
        close_when_done = True
        device = dwf.DwfAnalogOut()
    if node is None:
        node = device.NODE.CARRIER
    if func is None:
        func = device.FUNC.SINE
    device.nodeEnableSet(idxChannel=channel, node=node,  enable=True)
    device.nodeFunctionSet(idxChannel=channel, node=node, func=func)
    device.nodeFrequencySet(idxChannel=channel, node=node, hzFrequency=freq)
    device.nodeAmplitudeSet(idxChannel=channel, node=node, amplitude=amp)
    device.nodeOffsetSet(idxChannel=channel, node=node, offset=offset)
    device.nodePhaseSet(idxChannel=channel, node=node, degreePhase=phase)
    device.configure(idxChannel=channel, start=True)
    if close_when_done:
        device.close()


def stop_wave(device, node=None, channel=0):
    if node is None:
        node = device.NODE.CARRIER
    device.nodeEnableSet(channel, node, channel)


def read_data(device, channel=0, channel_range=25, mode=None, freq=10e10, number_of_samples=100000, display_plt=True):
    assert isinstance(device, dwf.DwfAnalogIn)
    if mode is None:
        mode = device.ACQMODE.RECORD
    device.channelEnableSet(channel, True)
    device.channelRangeSet(channel, channel_range)
    device.acquisitionModeSet(mode)
    device.frequencySet(freq)
    device.recordLengthSet(number_of_samples / freq)

    device.configure(False, True)
    record_data = np.array([], dtype=np.float64)
    while len(record_data) < number_of_samples:
        sts = device.status(True)

        available, lost, corrupted = device.statusRecord()

        if lost == 0 and corrupted == 0 and available > 0:
            record_data = np.append(record_data, device.statusData(channel, available))
    if display_plt:
        time_stamps = np.arange(0, len(record_data), 1 / freq)
        time_stamps = time_stamps * 10e3
        plt.plot(time_stamps, record_data)
        plt.title("Channel {}".format(channel))
        plt.xlabel("Time(mS)")
        plt.ylabel("Voltage(V)")
        plt.show()
    return record_data


def measure_voltage(device_in=None):
    close_when_done = False
    if device_in is None:
        device_in = dwf.DwfAnalogIn()
        close_when_done = True

    data = read_data(device_in, display_plt=False)
    if close_when_done:
        device_in.close()
    return np.average(data)


def measure_current(resistance, device_in=None):
    close_when_done = False
    if device_in is None:
        device_in = dwf.DwfAnalogIn()
        close_when_done = True

    data = read_data(device_in, display_plt=False)
    if close_when_done:
        device_in.close()
    return np.average(data) / resistance


fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
data = np.array([])
timestamps = np.array([])


def view_life_stats(device, channel=0, channel_range=25, mode=None, freq=10e3, number_of_samples=10000,
                    points_display=50):

    def animate(_):
        global data
        global timestamps
        ax.clear()

        data = np.append(data, read_data(device, channel, channel_range, mode, freq, number_of_samples,
                                         display_plt=False))
        # timestamps = timestamps / 10e3
        # timestamps = np.append(timestamps, np.arange(len(timestamps), len(data), 1/freq))
        if len(data) > points_display:
            display_y = data[-points_display:]
            # display_x = timestamps[-points_display:]
        else:
            display_y = data
            # display_x = timestamps
        ax.plot(display_y)
    ani = animation.FuncAnimation(fig, animate, interval=.1)
    plt.show()


def measure_voltages(number_items, device=None):
    close_device_when_done = False
    values = np.array([])
    if device is None:
        close_device_when_done = True
        device = dwf.DwfAnalogIn()
    for _ in number_items:
        while True:
            inp = input("Press Enter to read value")
            if inp == "/n":
                value = measure_voltage(device)
                print("Measured Value: {} V".format(value))
                values = np.append(values, value)
                break

    if close_device_when_done:
        device.close()
    return values


def measure_currents(number_items, resistor, device=None):
    close_device_when_done = False
    values = np.array([])
    if device is None:
        close_device_when_done = True
        device = dwf.DwfAnalogIn()
    for _ in number_items:
        while True:
            inp = input("Press Enter to read value")
            if inp == "/n":
                value = measure_current(resistor, device)
                print("Measured Value: {} V".format(value))
                values = np.append(values, value)
                break

    if close_device_when_done:
        device.close()
    return values
