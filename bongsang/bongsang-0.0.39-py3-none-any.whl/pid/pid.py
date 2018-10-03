###########################
# PID
# Created by Bongsang Kim
###########################

OUT_MAX = 100
OUT_MIN = 0
Kp_MAX = 5000
Kp_MIN = 10
Ki_MAX = 10
Ki_MIN = .1
Kd_MAX = 10
Kd_MIN = 0



class PID_v04():
    def __init__(self, mode, sp, pv_init):
        dt = 0.1  # like robot control
        self.Kp = Kp_MIN
        self.Ki = Ki_MIN
        self.Kd = Kd_MIN

        self.Kp_MIN = Kp_MIN
        self.Kp_MAX = Kp_MAX

        self.out = OUT_MIN
        
        self.sp = sp
        self.pv_previous = pv_init

        self.proportional_error = 0
        self.integral_error = 0
        self.derivative_error = 0
        self.dt = dt

        self.mode = mode


    def print_parameters(self):
        print('Kp={}, Ki={}, Kd={}'.format(self.Kp, self.Ki, self.Kd))


    def get_parameters(self):
        params = {'Kp': self.Kp, 'Ki': self.Ki, 'Kd': self.Kd}
        return params


    def get_out(self, pv):
        # Propotional equation
        if self.mode == 'heating':
            self.proportional_error = self.sp - pv
        elif self.mode == 'cooling':
            self.proportional_error = pv - self.sp

        # Integral equation
        self.integral_error += self.Ki * self.proportional_error * self.dt

        # Derivative equation
        self.derivative_error = (pv - self.pv_previous) / self.dt

        # calculate the PID output
        P = self.Kp * self.proportional_error
        I = self.integral_error
        D = -self.Kd * self.derivative_error
        self.out += P + I + D

        # implement anti-reset windup
        if self.out <= OUT_MIN or self.out >= OUT_MAX:
            self.integral_error -= self.Ki * self.proportional_error * self.dt
            # clip output
            self.out = max(OUT_MIN, min(OUT_MAX, self.out))

        # return the controller output and PID terms
        self.pv_previous = pv

        return int(self.out)


    def set_parameters(self, Kp, Ki, Kd):
        if Kp >= self.Kp_MIN and Kp <= self.Kp_MAX:
            self.Kp = Kp
        else:
            raise ValueError('Kp is out of the boundary.')

        if Ki >= Ki_MIN and Ki <= Ki_MAX:
            self.Ki = Ki
        else:
            raise ValueError('Ki is out of the boundary.')

        if Kd >= Kd_MIN and Kd <= Kd_MAX:
            self.Kd = Kd


    def set_max(self):
        self.Kp = self.Kp_MAX
        self.Ki = Ki_MIN
        self.Kd = Kd_MIN


    def increase_Kp(self):
        self.Kp += 1.0
        if self.Kp >= self.Kp_MAX:
            self.Kp = self.Kp_MAX
    
    def decrease_Kp(self):
        self.Kp -= 1.0
        if self.Kp <= self.Kp_MIN:
            self.Kp = self.Kp_MIN

    def increase_Ki(self):
        # self.Ki += 1.0
        self.Ki += 0.1
        if self.Ki >= Ki_MAX:
            self.Ki = Ki_MAX
    
    def decrease_Ki(self):
        # self.Ki -= 1.0
        self.Ki -= 0.1
        if self.Ki <= Ki_MIN:
            self.Ki = Ki_MIN

    def increase_Kd(self):
        self.Kd += .1
        if self.Kd >= Kd_MAX:
            self.Kd = Kd_MAX

    def decrease_Kd(self):
        self.Kd -= .1
        if self.Kd <= Kd_MIN:
            self.Kd = Kd_MIN


    def reset(self):
        self.Kp = self.Kp_MIN
        self.Ki = Ki_MIN
        self.Kd = Kd_MIN



class PID_v03():
    def __init__(self, mode, sp, pv_init, Kp_MIN, Kp_MAX, dt):
        self.Kp = Kp_MIN
        self.Ki = Ki_MIN
        self.Kd = Kd_MIN

        self.Kp_MIN = Kp_MIN
        self.Kp_MAX = Kp_MAX

        self.out = OUT_MIN
        
        self.sp = sp
        self.pv_previous = pv_init

        self.proportional_error = 0
        self.integral_error = 0
        self.derivative_error = 0
        self.dt = dt

        self.mode = mode


    def print_parameters(self):
        print('Kp={}, Ki={}, Kd={}'.format(self.Kp, self.Ki, self.Kd))


    def get_parameters(self):
        params = {'Kp': self.Kp, 'Ki': self.Ki, 'Kd': self.Kd}
        return params


    def get_out(self, pv):
        # Propotional equation
        if self.mode == 'heating':
            self.proportional_error = self.sp - pv
        elif self.mode == 'cooling':
            self.proportional_error = pv - self.sp

        # Integral equation
        self.integral_error += self.Ki * self.proportional_error * self.dt

        # Derivative equation
        self.derivative_error = (pv - self.pv_previous) / self.dt

        # calculate the PID output
        P = self.Kp * self.proportional_error
        I = self.integral_error
        D = -self.Kd * self.derivative_error
        self.out += P + I + D

        # implement anti-reset windup
        if self.out <= OUT_MIN or self.out >= OUT_MAX:
            self.integral_error -= self.Ki * self.proportional_error * self.dt
            # clip output
            self.out = max(OUT_MIN, min(OUT_MAX, self.out))

        # return the controller output and PID terms
        self.pv_previous = pv

        return int(self.out)


    def set_parameters(self, Kp, Ki, Kd):
        if Kp >= self.Kp_MIN and Kp <= self.Kp_MAX:
            self.Kp = Kp
        else:
            raise ValueError('Kp is out of the boundary.')

        if Ki >= Ki_MIN and Ki <= Ki_MAX:
            self.Ki = Ki
        else:
            raise ValueError('Ki is out of the boundary.')

        if Kd >= Kd_MIN and Kd <= Kd_MAX:
            self.Kd = Kd


    def set_max(self):
        self.Kp = self.Kp_MAX
        self.Ki = Ki_MIN
        self.Kd = Kd_MIN


    def increase_Kp(self):
        self.Kp += 1.0
        if self.Kp >= self.Kp_MAX:
            self.Kp = self.Kp_MAX
    
    def decrease_Kp(self):
        self.Kp -= 1.0
        if self.Kp <= self.Kp_MIN:
            self.Kp = self.Kp_MIN

    def increase_Ki(self):
        # self.Ki += 1.0
        self.Ki += 0.1
        if self.Ki >= Ki_MAX:
            self.Ki = Ki_MAX
    
    def decrease_Ki(self):
        # self.Ki -= 1.0
        self.Ki -= 0.1
        if self.Ki <= Ki_MIN:
            self.Ki = Ki_MIN

    def increase_Kd(self):
        self.Kd += .1
        if self.Kd >= Kd_MAX:
            self.Kd = Kd_MAX

    def decrease_Kd(self):
        self.Kd -= .1
        if self.Kd <= Kd_MIN:
            self.Kd = Kd_MIN


    def reset(self):
        self.Kp = self.Kp_MIN
        self.Ki = Ki_MIN
        self.Kd = Kd_MIN



# class PID_v02():
#     def __init__(self, mode, sp, pv_init, Kp_MIN, Kp_MAX):
#         self.Kp = Kp_MIN
#         self.Ki = Ki_MIN
#         self.Kd = Kd_MIN

#         self.Kp_MIN = Kp_MIN
#         self.Kp_MAX = Kp_MAX

#         self.out = OUT_MIN
        
#         self.sp = sp
#         self.pv_previous = pv_init

#         self.proportional_error = 0
#         self.integral_error = 0
#         self.derivative_error = 0
#         # self.dt = 1.0
#         self.dt = 60

#         self.mode = mode


#     def print_parameters(self):
#         print('Kp={}, Ki={}, Kd={}'.format(self.Kp, self.Ki, self.Kd))


#     def get_parameters(self):
#         params = {'Kp': self.Kp, 'Ki': self.Ki, 'Kd': self.Kd}
#         return params


#     def get_out(self, pv):
#         # Propotional equation
#         if self.mode == 'heating':
#             self.proportional_error = self.sp - pv
#         elif self.mode == 'cooling':
#             self.proportional_error = pv - self.sp

#         # Integral equation
#         self.integral_error += self.Ki * self.proportional_error * self.dt

#         # Derivative equation
#         self.derivative_error = (pv - self.pv_previous) / self.dt

#         # calculate the PID output
#         P = self.Kp * self.proportional_error
#         I = self.integral_error
#         D = -self.Kd * self.derivative_error
#         self.out += P + I + D

#         # implement anti-reset windup
#         if self.out <= OUT_MIN or self.out >= OUT_MAX:
#             self.integral_error -= self.Ki * self.proportional_error * self.dt
#             # clip output
#             self.out = max(OUT_MIN, min(OUT_MAX, self.out))

#         # return the controller output and PID terms
#         self.pv_previous = pv

#         return int(self.out)


#     def set_parameters(self, Kp, Ki, Kd):
#         if Kp >= self.Kp_MIN and Kp <= self.Kp_MAX:
#             self.Kp = Kp
#         else:
#             raise ValueError('Kp is out of the boundary.')

#         if Ki >= Ki_MIN and Ki <= Ki_MAX:
#             self.Ki = Ki
#         else:
#             raise ValueError('Ki is out of the boundary.')

#         if Kd >= Kd_MIN and Kd <= Kd_MAX:
#             self.Kd = Kd


#     def set_max(self):
#         self.Kp = self.Kp_MAX
#         self.Ki = Ki_MIN
#         self.Kd = Kd_MIN


#     def increase_Kp(self):
#         self.Kp += 1.0
#         if self.Kp >= self.Kp_MAX:
#             self.Kp = self.Kp_MAX
    
#     def decrease_Kp(self):
#         self.Kp -= 1.0
#         if self.Kp <= self.Kp_MIN:
#             self.Kp = self.Kp_MIN

#     def increase_Ki(self):
#         # self.Ki += 1.0
#         self.Ki += 0.1
#         if self.Ki >= Ki_MAX:
#             self.Ki = Ki_MAX
    
#     def decrease_Ki(self):
#         # self.Ki -= 1.0
#         self.Ki -= 0.1
#         if self.Ki <= Ki_MIN:
#             self.Ki = Ki_MIN

#     def increase_Kd(self):
#         self.Kd += .1
#         if self.Kd >= Kd_MAX:
#             self.Kd = Kd_MAX

#     def decrease_Kd(self):
#         self.Kd -= .1
#         if self.Kd <= Kd_MIN:
#             self.Kd = Kd_MIN


#     def reset(self):
#         self.Kp = self.Kp_MIN
#         self.Ki = Ki_MIN
#         self.Kd = Kd_MIN



# class PID_v01():
#     def __init__(self, sp=30, pv_init=20):
#         self.Kp = Kp_MIN
#         self.Ki = Ki_MIN
#         self.Kd = Kd_MIN

#         self.out = OUT_MIN
        
#         self.sp = sp
#         self.pv_previous = pv_init

#         self.proportional_error = 0
#         self.integral_error = 0
#         self.derivative_error = 0

#         self.dt = 1.0


#     def print_parameters(self):
#         print('Kp={}, Ki={}, Kd={}'.format(self.Kp, self.Ki, self.Kd))


#     def get_parameters(self):
#         params = {'Kp': self.Kp, 'Ki': self.Ki, 'Kd': self.Kd}
#         return params


#     def get_out(self, pv):
#         # Propotional equation
#         self.proportional_error = self.sp - pv

#         # Integral equation
#         self.integral_error += self.Ki * self.proportional_error * self.dt

#         # Derivative equation
#         self.derivative_error = (pv - self.pv_previous) / self.dt

#         # calculate the PID output
#         P = self.Kp * self.proportional_error
#         I = self.integral_error
#         D = -self.Kd * self.derivative_error
#         self.out += P + I + D

#         # implement anti-reset windup
#         if self.out <= OUT_MIN or self.out >= OUT_MAX:
#             self.integral_error -= self.Ki * self.proportional_error * self.dt
#             # clip output
#             self.out = max(OUT_MIN, min(OUT_MAX, self.out))

#         # return the controller output and PID terms
#         self.pv_previous = pv

#         return int(self.out)


#     def set_parameters(self, Kp, Ki, Kd):
#         if Kp >= Kp_MIN and Kp <= Kp_MAX:
#             self.Kp = Kp

#         if Ki >= Ki_MIN and Ki <= Ki_MAX:
#             self.Ki = Ki

#         if Kd >= Kd_MIN and Kd <= Kd_MAX:
#             self.Kd = Kd


#     def set_max(self):
#         self.Kp = Kp_MAX
#         self.Ki = Ki_MIN
#         self.Kd = Kd_MIN


#     def increase_Kp(self):
#         self.Kp += 1.0
#         if self.Kp >= Kp_MAX:
#             self.Kp = Kp_MAX
    
#     def decrease_Kp(self):
#         self.Kp -= 1.0
#         if self.Kp <= Kp_MIN:
#             self.Kp = Kp_MIN

#     def increase_Ki(self):
#         self.Ki += .01
#         if self.Ki >= Ki_MAX:
#             self.Ki = Ki_MAX
    
#     def decrease_Ki(self):
#         self.Ki -= .01
#         if self.Ki <= Ki_MIN:
#             self.Ki = Ki_MIN

#     def increase_Kd(self):
#         self.Kd += .1
#         if self.Kd >= Kd_MAX:
#             self.Kd = Kd_MAX

#     def decrease_Kd(self):
#         self.Kd -= .1
#         if self.Kd <= Kd_MIN:
#             self.Kd = Kd_MIN


#     def reset(self):
#         self.Kp = Kp_MIN
#         self.Ki = Ki_MIN
#         self.Kd = Kd_MIN
