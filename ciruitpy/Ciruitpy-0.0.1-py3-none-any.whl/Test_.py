import numpy as np
from CircuitPy.BaseFunction import *

sample_size = 10
max_value = 10000
tolerance = 1e-16


def test_ohms_law():
    test_outcome = True
    current = np.random.randint(1, max_value, size=sample_size).astype(np.float64)
    resistance = np.random.randint(1, max_value, size=sample_size).astype(np.float64)
    voltage = current * resistance

    if np.allclose(current, ohms_law(voltage=voltage, resistance=resistance), atol=tolerance):
        print("current test pass!!")
    else:
        print("current test fail")
        test_outcome = False

    if np.allclose(voltage, ohms_law(current=current, resistance=resistance), atol=tolerance):
        print("voltage test pass!!")
    else:
        print("voltage test fail")
        test_outcome = False

    if np.allclose(resistance, ohms_law(voltage=voltage, current=current), atol=tolerance):
        print("current test pass!!")
    else:
        print("current test fail")
        test_outcome = False
    return test_outcome


def test_resistors_in_parallel():
    resistors = np.random.randint(1, max_value, size=sample_size).astype(np.float64)
    invet = np.float_power(resistors, -1)
    if np.allclose(1/invet.sum(), resistors_parallel(resistors), atol=tolerance):
        print("resistors in parallel pass")
        return True
    else:
        print("resistors in parallel fail")
        return False


def test_current_division():
    current = np.random.randint(1, max_value, size=1).astype(np.float64)
    resistance = np.random.randint(1, max_value, size=sample_size).astype(np.float64)
    voltage = ohms_law(resistance=resistors_parallel(resistance), current=current)

    if np.allclose(current, current_division(resistors=resistance, current=current)["current"].sum()):
        print("pass")
    else:
        print("fail")

    if np.allclose(current, current_division(resistors=resistance, voltage=voltage)["current"].sum()):
        print("pass")
    else:
        print("fail")


def test_voltage_division():
    current = np.random.randint(1, max_value, size=1).astype(np.float64)
    resistance = np.random.randint(1, max_value, size=sample_size).astype(np.float64)
    voltage = ohms_law(resistance=resistance.sum(), current=current)

    if np.allclose(voltage, voltage_division(resistors=resistance, current=current)["voltage"].sum()):
        print("pass")
    else:
        print("fail")

    if np.allclose(voltage, voltage_division(resistors=resistance, voltage=voltage)["voltage"].sum()):
        print("pass")
    else:
        print("fail")


def test_save_data():
    data = [
        ["table 3", current_division(resistors=np.random.randint(1, max_value, size=sample_size),
                                     current=np.random.randint(1, max_value, size=1))],
        ["table 4", voltage_division(resistors=np.random.randint(1, max_value, size=sample_size),
                                     current=np.random.randint(1, max_value, size=1))]
    ]
    save_data_to_exec(dataframes=data, file_name="D:\Code\CircuitLabDataRecorder\data1.docx")


def test_load_data():
    load_data_from_exec("data1.xlsx")


def test_mesh_analysis():
    print(mesh_analysis(np.array([
        [50, 0, -30],
        [0, 40, -20],
        [-30, -20, 100]
    ]), np.array([80, 80, 0])))


def test_cap_impedance():
    print(capacitor_impedance(np.random.randint(0, 1000, 100000), 400))

test_cap_impedance()