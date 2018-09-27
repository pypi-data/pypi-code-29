import numpy as np

def hill_radius(r_p,q_p):
    return r_p*(q_p/3)**(1./3)

def omega_frame(r_p,q_p):
    a_p = r_p #tmp
    return a_p*np.sqrt((1.+q_p)/r_p**3)#todo : check
