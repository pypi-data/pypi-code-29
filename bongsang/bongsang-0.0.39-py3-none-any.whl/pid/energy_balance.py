# Bongsang EMS AI Simulator
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
# from random import *

######################################################
# Energy balance model                               #
######################################################

class EnergyBalance_v06():  # For cooling & heating
    def __init__(self, mode, sp):
        print('mode=', mode)
        dt = 60  # 1 minute
        if mode == 'cooling':
            # self.wall_temperature = 22 + 273.15   # 벽의 온도 (SP - 2도 --> 벽이 열을 받아 온도가 올라갔다는 가정)
            self.wall_temperature = sp-3 + 273.15   # 벽의 온도 (SP - 2도 --> 벽이 열을 받아 온도가 올라갔다는 가정)
            self.overall_heat_transfer_coefficient = 10.0           # W/m^2-K
            self.mass = 10000    # kg (정풍량 방식의 공조 스펙값)
            self.heat_capacity = 1 * 1000.0  # J/kg-K
            self.surface_area = 200 # Area in m^2 (AHu#23의 대상 오피스 벽 넓이)
            self.alpha = 2000       # W / % heater (냉동기 열용량))
            self.emissivity = 0.9 # Emissivity
            self.stefan_boltzman_constant = 5.67e-8    # Stefan-Boltzman
            self.kelvin = 273.15
            
        elif mode == 'heating':
            # self.wall_temperature = 24 + 273.15   # 벽의 온도 (SP + 2도 --> 벽이 열을 받아 온도가 올라갔다는 가정)
            self.wall_temperature = sp+2 + 273.15   # 벽의 온도 (SP + 2도 --> 벽이 열을 받아 온도가 올라갔다는 가정)
            self.overall_heat_transfer_coefficient = 10.0           # W/m^2-K
            self.mass = 8000  # kg (정풍량 방식의 공조 스펙값)
            self.heat_capacity = 1 * 1000.0  # J/kg-K
            self.surface_area = 200 # Area in m^2 (AHu#23의 대상 오피스 벽 넓이)
            self.alpha = 1600       # W / % heater (보일러 열용량))
            self.emissivity = 0.9 # Emissivity
            self.stefan_boltzman_constant = 5.67e-8    # Stefan-Boltzman
            self.kelvin = 273.15

        self.mode = mode
        self.dt = dt


    def physics_equation(self, T, t, OUT):
        # Temperature State
        T_previous = T[0]

        if self.mode == 'cooling':
            # Nonlinear Energy Balance
            kelvin_temperature = (1.0 / (self.mass * self.heat_capacity)) * \
                                 (self.overall_heat_transfer_coefficient * self.surface_area * \
                                 (T_previous-self.wall_temperature) + self.emissivity * \
                                 self.stefan_boltzman_constant * self.surface_area * \
                                 (T_previous**4-self.wall_temperature**4) - self.alpha*OUT)
        elif self.mode == 'heating':
            kelvin_temperature = (1.0 / (self.mass * self.heat_capacity)) * \
                                 (self.overall_heat_transfer_coefficient * self.surface_area * \
                                 (T_previous-self.wall_temperature) + self.emissivity * \
                                 self.stefan_boltzman_constant * self.surface_area * \
                                 (T_previous**4-self.wall_temperature**4 ) + self.alpha*OUT)

        return kelvin_temperature


    def get_temperature(self, PV, OUT):
        PV_next = odeint(self.physics_equation, PV + self.kelvin, [0, self.dt], args=(OUT,))

        result = PV_next[1][0] - self.kelvin
        
        return result


    def set_parameters(self, wall_temperature, overall_heat_transfer_coefficient, mass, heat_capacity, surface_area, alpha, emissivity):
        self.wall_temperature = wall_temperature + self.kelvin
        self.overall_heat_transfer_coefficient = overall_heat_transfer_coefficient
        self.mass = mass
        self.heat_capacity = heat_capacity
        self.surface_area = surface_area
        self.alpha = alpha
        self.emissivity = emissivity




class EnergyBalance_v05():  # For cooling & heating
    def __init__(self, mode, sp, dt):
        print('mode=', mode)
        if mode == 'cooling':
            # self.wall_temperature = 22 + 273.15   # 벽의 온도 (SP - 2도 --> 벽이 열을 받아 온도가 올라갔다는 가정)
            self.wall_temperature = sp-3 + 273.15   # 벽의 온도 (SP - 2도 --> 벽이 열을 받아 온도가 올라갔다는 가정)
            self.overall_heat_transfer_coefficient = 10.0           # W/m^2-K
            self.mass = 10000    # kg (정풍량 방식의 공조 스펙값)
            self.heat_capacity = 1 * 1000.0  # J/kg-K
            self.surface_area = 200 # Area in m^2 (AHu#23의 대상 오피스 벽 넓이)
            self.alpha = 2000       # W / % heater (냉동기 열용량))
            self.emissivity = 0.9 # Emissivity
            self.stefan_boltzman_constant = 5.67e-8    # Stefan-Boltzman
            self.kelvin = 273.15
            
        elif mode == 'heating':
            # self.wall_temperature = 24 + 273.15   # 벽의 온도 (SP + 2도 --> 벽이 열을 받아 온도가 올라갔다는 가정)
            self.wall_temperature = sp+2 + 273.15   # 벽의 온도 (SP + 2도 --> 벽이 열을 받아 온도가 올라갔다는 가정)
            self.overall_heat_transfer_coefficient = 10.0           # W/m^2-K
            self.mass = 8000  # kg (정풍량 방식의 공조 스펙값)
            self.heat_capacity = 1 * 1000.0  # J/kg-K
            self.surface_area = 200 # Area in m^2 (AHu#23의 대상 오피스 벽 넓이)
            self.alpha = 1600       # W / % heater (보일러 열용량))
            self.emissivity = 0.9 # Emissivity
            self.stefan_boltzman_constant = 5.67e-8    # Stefan-Boltzman
            self.kelvin = 273.15

        self.mode = mode
        self.dt = dt


    def physics_equation(self, T, t, OUT):
        # Temperature State
        T_previous = T[0]

        if self.mode == 'cooling':
            # Nonlinear Energy Balance
            kelvin_temperature = (1.0 / (self.mass * self.heat_capacity)) * \
                                 (self.overall_heat_transfer_coefficient * self.surface_area * \
                                 (T_previous-self.wall_temperature) + self.emissivity * \
                                 self.stefan_boltzman_constant * self.surface_area * \
                                 (T_previous**4-self.wall_temperature**4) - self.alpha*OUT)
        elif self.mode == 'heating':
            kelvin_temperature = (1.0 / (self.mass * self.heat_capacity)) * \
                                 (self.overall_heat_transfer_coefficient * self.surface_area * \
                                 (T_previous-self.wall_temperature) + self.emissivity * \
                                 self.stefan_boltzman_constant * self.surface_area * \
                                 (T_previous**4-self.wall_temperature**4 ) + self.alpha*OUT)

        return kelvin_temperature


    def get_temperature(self, PV, OUT):
        PV_next = odeint(self.physics_equation, PV + self.kelvin, [0, self.dt], args=(OUT,))

        result = PV_next[1][0] - self.kelvin
        
        return result


    def set_parameters(self, wall_temperature, overall_heat_transfer_coefficient, mass, heat_capacity, surface_area, alpha, emissivity):
        self.wall_temperature = wall_temperature + self.kelvin
        self.overall_heat_transfer_coefficient = overall_heat_transfer_coefficient
        self.mass = mass
        self.heat_capacity = heat_capacity
        self.surface_area = surface_area
        self.alpha = alpha
        self.emissivity = emissivity



# class EnergyBalance_v04():  # For cooling & heating
#     def __init__(self, mode, sp):
#         print('mode=', mode)
#         if mode == 'cooling':
#             # self.wall_temperature = 22 + 273.15   # 벽의 온도 (SP - 2도 --> 벽이 열을 받아 온도가 올라갔다는 가정)
#             self.wall_temperature = sp-3 + 273.15   # 벽의 온도 (SP - 2도 --> 벽이 열을 받아 온도가 올라갔다는 가정)
#             self.overall_heat_transfer_coefficient = 10.0           # W/m^2-K
#             self.mass = 10000    # kg (정풍량 방식의 공조 스펙값)
#             self.heat_capacity = 1 * 1000.0  # J/kg-K
#             self.surface_area = 200 # Area in m^2 (AHu#23의 대상 오피스 벽 넓이)
#             self.alpha = 2000       # W / % heater (냉동기 열용량))
#             self.emissivity = 0.9 # Emissivity
#             self.stefan_boltzman_constant = 5.67e-8    # Stefan-Boltzman
#             self.kelvin = 273.15
            
#         elif mode == 'heating':
#             # self.wall_temperature = 24 + 273.15   # 벽의 온도 (SP + 2도 --> 벽이 열을 받아 온도가 올라갔다는 가정)
#             self.wall_temperature = sp+2 + 273.15   # 벽의 온도 (SP + 2도 --> 벽이 열을 받아 온도가 올라갔다는 가정)
#             self.overall_heat_transfer_coefficient = 10.0           # W/m^2-K
#             self.mass = 8000  # kg (정풍량 방식의 공조 스펙값)
#             self.heat_capacity = 1 * 1000.0  # J/kg-K
#             self.surface_area = 200 # Area in m^2 (AHu#23의 대상 오피스 벽 넓이)
#             self.alpha = 1600       # W / % heater (보일러 열용량))
#             self.emissivity = 0.9 # Emissivity
#             self.stefan_boltzman_constant = 5.67e-8    # Stefan-Boltzman
#             self.kelvin = 273.15

#         self.mode = mode


#     def physics_equation(self, T, t, OUT):
#         # Temperature State
#         T_previous = T[0]

#         if self.mode == 'cooling':
#             # Nonlinear Energy Balance
#             kelvin_temperature = (1.0 / (self.mass * self.heat_capacity)) * \
#                                  (self.overall_heat_transfer_coefficient * self.surface_area * \
#                                  (T_previous-self.wall_temperature) + self.emissivity * \
#                                  self.stefan_boltzman_constant * self.surface_area * \
#                                  (T_previous**4-self.wall_temperature**4) - self.alpha*OUT)
#         elif self.mode == 'heating':
#             kelvin_temperature = (1.0 / (self.mass * self.heat_capacity)) * \
#                                  (self.overall_heat_transfer_coefficient * self.surface_area * \
#                                  (T_previous-self.wall_temperature) + self.emissivity * \
#                                  self.stefan_boltzman_constant * self.surface_area * \
#                                  (T_previous**4-self.wall_temperature**4 ) + self.alpha*OUT)

#         return kelvin_temperature


#     def get_temperature(self, PV, OUT):
#         dt = 60
#         PV_next = odeint(self.physics_equation, PV + self.kelvin, [0, dt], args=(OUT,))

#         result = PV_next[1][0] - self.kelvin
        
#         return result


#     def set_parameters(self, wall_temperature, overall_heat_transfer_coefficient, mass, heat_capacity, surface_area, alpha, emissivity):
#         self.wall_temperature = wall_temperature + self.kelvin
#         self.overall_heat_transfer_coefficient = overall_heat_transfer_coefficient
#         self.mass = mass
#         self.heat_capacity = heat_capacity
#         self.surface_area = surface_area
#         self.alpha = alpha
#         self.emissivity = emissivity



# class EnergyBalance_v01():
#     def __init__(self):
#         self.Ta = 10 + 273.15   # K
#         self.U = 10.0           # W/m^2-K
#         self.m = 4.0/1000.0     # kg
#         # self.m = 12.0/1000.0     # kg
#         self.Cp = 0.5 * 1000.0  # J/kg-K
#         self.A = 12.0 / 100.0**2 # Area in m^2
#         # self.A = 24.0 / 100.0**2 # Area in m^2
#         self.alpha = 0.01       # W / % heater
#         self.emissivity = 0.9          # Emissivity
#         self.stefan_boltzman = 5.67e-8    # Stefan-Boltzman
#         self.kelvin = 273.15


#     def physics_equation(self, T, t, OUT):
#         # Temperature State
#         T_previous = T[0]

#         # Nonlinear Energy Balance
#         kelvin_temperature = (1.0 / (self.m * self.Cp)) * (self.U * self.A * (self.Ta - T_previous) \
#                 + self.emissivity * self.stefan_boltzman * self.A * (self.Ta**4 - T_previous**4) \
#                 + self.alpha*OUT)

#         return kelvin_temperature


#     def get_temperature(self, PV, OUT):
#         dt = 1
#         PV_next = odeint(self.physics_equation, PV + self.kelvin, [0, dt], args=(OUT,))
        
#         return PV_next[1][0] - self.kelvin


# class EnergyBalance_v02():  # for heating
#     def __init__(self):
#         self.wall_temperature = 24 + 273.15   # 벽의 온도 (SP + 2도 --> 벽이 열을 받아 온도가 올라갔다는 가정)
#         self.overall_heat_transfer_coefficient = 10.0           # W/m^2-K
#         self.mass = 8000  # kg (정풍량 방식의 공조 스펙값)
#         self.heat_capacity = 1 * 1000.0  # J/kg-K
#         self.surface_area = 200 # Area in m^2 (AHu#23의 대상 오피스 벽 넓이)
#         self.alpha = 1600       # W / % heater (보일러 열용량))
#         self.emissivity = 0.9 # Emissivity
#         self.stefan_boltzman_constant = 5.67e-8    # Stefan-Boltzman
#         self.kelvin = 273.15


#     def physics_equation(self, T, t, OUT):
#         # Temperature State
#         T_previous = T[0]

#         # # Nonlinear Energy Balance
#         # kelvin_temperature = (1.0 / (self.mass * self.heat_capacity)) * \
#         # (self.overall_heat_transfer_coefficient * self.surface_area * \
#         # (self.ambient_temperature - T_previous) + self.emissivity * \
#         # self.stefan_boltzman_constant * self.surface_area * \
#         # (self.ambient_temperature**4 - T_previous**4) - self.alpha*OUT)

#         # Nonlinear Energy Balance
#         kelvin_temperature = (1.0 / (self.mass * self.heat_capacity)) * \
#         (self.overall_heat_transfer_coefficient * self.surface_area * \
#         (T_previous-self.wall_temperature) + self.emissivity * \
#         self.stefan_boltzman_constant * self.surface_area * \
#         (T_previous**4-self.wall_temperature**4 ) + self.alpha*OUT)



#         return kelvin_temperature


#     def get_temperature(self, PV, OUT):
#         dt = 1
#         PV_next = odeint(self.physics_equation, PV + self.kelvin, [0, dt], args=(OUT,))
        
#         return PV_next[1][0] - self.kelvin


#     def set_parameters(self, wall_temperature, overall_heat_transfer_coefficient, mass, heat_capacity, surface_area, alpha, emissivity):
#         self.wall_temperature = wall_temperature + self.kelvin
#         self.overall_heat_transfer_coefficient = overall_heat_transfer_coefficient
#         self.mass = mass
#         self.heat_capacity = heat_capacity
#         self.surface_area = surface_area
#         self.alpha = alpha
#         self.emissivity = emissivity



# class EnergyBalance_v03():  # For cooling
#     def __init__(self):
#         self.wall_temperature = 22 + 273.15   # 벽의 온도 (SP - 2도 --> 벽이 열을 받아 온도가 올라갔다는 가정)
#         self.overall_heat_transfer_coefficient = 10.0           # W/m^2-K
#         self.mass = 10000    # kg (정풍량 방식의 공조 스펙값)
#         self.heat_capacity = 1 * 1000.0  # J/kg-K
#         self.surface_area = 200 # Area in m^2 (AHu#23의 대상 오피스 벽 넓이)
#         self.alpha = 2000       # W / % heater (냉동기 열용량))
#         self.emissivity = 0.9 # Emissivity
#         self.stefan_boltzman_constant = 5.67e-8    # Stefan-Boltzman
#         self.kelvin = 273.15


#     def physics_equation(self, T, t, OUT):
#         # Temperature State
#         T_previous = T[0]

#         # # Nonlinear Energy Balance
#         # kelvin_temperature = (1.0 / (self.mass * self.heat_capacity)) * \
#         # (self.overall_heat_transfer_coefficient * self.surface_area * \
#         # (self.ambient_temperature - T_previous) + self.emissivity * \
#         # self.stefan_boltzman_constant * self.surface_area * \
#         # (self.ambient_temperature**4 - T_previous**4) - self.alpha*OUT)

#         # Nonlinear Energy Balance
#         kelvin_temperature = (1.0 / (self.mass * self.heat_capacity)) * \
#         (self.overall_heat_transfer_coefficient * self.surface_area * \
#         (T_previous-self.wall_temperature) + self.emissivity * \
#         self.stefan_boltzman_constant * self.surface_area * \
#         (T_previous**4-self.wall_temperature**4) - self.alpha*OUT)

#         #print('kelvin_temperature=', kelvin_temperature)


#         return kelvin_temperature


#     def get_temperature(self, PV, OUT):
#         dt = 1
#         PV_next = odeint(self.physics_equation, PV + self.kelvin, [0, dt], args=(OUT,))
        
#         return PV_next[1][0] - self.kelvin


#     def set_parameters(self, wall_temperature, overall_heat_transfer_coefficient, mass, heat_capacity, surface_area, alpha, emissivity):
#         self.wall_temperature = wall_temperature + self.kelvin
#         self.overall_heat_transfer_coefficient = overall_heat_transfer_coefficient
#         self.mass = mass
#         self.heat_capacity = heat_capacity
#         self.surface_area = surface_area
#         self.alpha = alpha
#         self.emissivity = emissivity



if __name__ == '__main__':
    from bongsang.pid.pid import PID_v03 as PID

    ####### cooling Yangjae Energy Balance Test ###########
    mode='cooling'
    sp=25.5
    pv_init = 29
    dt = 60
    simulator = EnergyBalance_v05(mode, sp, dt=dt)
    pv_previous = pv_init
    pid = PID(mode, sp, pv_init, Kp_MIN=10, Kp_MAX=6000, dt=dt)
    pid.set_parameters(272, 1, 0)

    # out_list = [100, 100, 100, 100, 100, 80, 80, 80, 80, 80, 70, 70, 70, 70, 70, 60, 60, 60, 60, 60, 50, 50, 50, 50, 50, 40, 40, 40, 40, 40, 30, 30, 30, 30, 30, 20, 20, 20, 20, 20, 10, 10, 10, 10, 10, 0, 0, 0, 0, 0]

    pv_list = []
    pv_list.append(pv_previous)
    out_list = []
    out_list.append(0)

    for i in range(120):
        # pv_next = simulator.get_temperature(pv_previous, out_list[i-1])
        out = pid.get_out(pv_previous)
        if out < 0 or out > 100:
            print('error!')

        out_list.append(out)
        pv_next = simulator.get_temperature(pv_previous, out)
        pv_list.append(pv_next)
        pv_previous = pv_next

    baseline = np.ones(len(pv_list)) * sp
    plt.subplot(211)
    title = 'SP={}, PV_init={}, Mode={}, Kp={}, Ki={}'.format(sp, pv_init, mode, pid.Kp, pid.Ki)
    plt.title(title)

    plt.plot(range(len(baseline)), baseline, range(len(pv_list)), pv_list)
    plt.subplot(212)
    plt.step(range(len(out_list)), out_list)
    plt.show()


#     ####### heating Yangjae Energy Balance Test ###########
#     # simulator = EnergyBalance_v04('heating')
#     # pv_previous = 10
#     # sp = 20
#     # pid = PID(sp, pv_previous, mode='heating')
#     # pid.set_parameters(200, 8, 0)

#     # # out_list = [100, 100, 100, 100, 100, 80, 80, 80, 80, 80, 70, 70, 70, 70, 70, 60, 60, 60, 60, 60, 50, 50, 50, 50, 50, 40, 40, 40, 40, 40, 30, 30, 30, 30, 30, 20, 20, 20, 20, 20, 10, 10, 10, 10, 10, 0, 0, 0, 0, 0]

#     # pv_list = []
#     # pv_list.append(pv_previous)
#     # out_list = []
#     # out_list.append(0)

#     # for i in range(5000):
#     #     # pv_next = simulator.get_temperature(pv_previous, out_list[i-1])
#     #     out = pid.get_out(pv_previous)
#     #     out_list.append(out)
#     #     pv_next = simulator.get_temperature(pv_previous, out)
#     #     pv_list.append(pv_next)
#     #     pv_previous = pv_next

#     # baseline = np.ones(len(pv_list)) * sp
#     # plt.subplot(211)
#     # plt.title('SP=20, Init=10, heating mode')

#     # plt.plot(range(len(baseline)), baseline, range(len(pv_list)), pv_list)
#     # plt.subplot(212)
#     # plt.step(range(len(out_list)), out_list)
#     # plt.show()


#     ####### Original Energy Balance Test ###########
#     # simulator = EnergyBalance_v03()
#     # pv_previous = 27
#     # sp = 25
#     # pid = PID(sp, pv_previous, mode='cooling')
#     # pid.set_parameters(100, 0.1, 0)

#     # # out_list = [100, 100, 100, 100, 100, 80, 80, 80, 80, 80, 70, 70, 70, 70, 70, 60, 60, 60, 60, 60, 50, 50, 50, 50, 50, 40, 40, 40, 40, 40, 30, 30, 30, 30, 30, 20, 20, 20, 20, 20, 10, 10, 10, 10, 10, 0, 0, 0, 0, 0]

#     # pv_list = []
#     # pv_list.append(pv_previous)
#     # out_list = []
#     # out_list.append(0)

#     # for i in range(5000):
#     #     # pv_next = simulator.get_temperature(pv_previous, out_list[i-1])
#     #     out = pid.get_out(pv_previous)
#     #     out_list.append(out)
#     #     pv_next = simulator.get_temperature(pv_previous, out)
#     #     pv_list.append(pv_next)
#     #     pv_previous = pv_next

#     # baseline = np.ones(len(pv_list)) * sp
#     # plt.subplot(211)
#     # plt.title('SP=27, Init=25, cooling mode')

#     # plt.plot(range(len(baseline)), baseline, range(len(pv_list)), pv_list)
#     # plt.subplot(212)
#     # plt.step(range(len(out_list)), out_list)
#     # plt.show()
