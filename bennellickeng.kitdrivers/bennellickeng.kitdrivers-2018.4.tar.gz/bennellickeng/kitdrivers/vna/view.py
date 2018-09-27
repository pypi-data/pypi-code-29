#!/usr/bin/env python
import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

d = np.loadtxt(open(sys.argv[1],"rb"),delimiter=",",skiprows=0)

print d
print np.shape(d)

freq = d[:,0]

raw_phase = d[:,2]
shifted_phase = raw_phase - 53

def freq_scale_func(f, p):
    f_ref = 10000000
    f_diff = f - f_ref
    return p - (0.0000052 * f_diff)

vec_freq_scale_func = np.vectorize(freq_scale_func)
freq_adjusted_phase = vec_freq_scale_func(freq, shifted_phase)

def wrap_func(p):
    if p < -180:
        return p + 360
    elif p >= 180:
        return p - 360
    else:
        return p

vec_wap_func = np.vectorize(wrap_func)
wrapped_phase = vec_wap_func(freq_adjusted_phase)

phase = wrapped_phase * -1

vrmsratioa = np.divide( d[:,4], d[:,3])
vm = np.vstack( (vrmsratioa))
f = np.log10(vm)
vdb = (f * 20) + 5
print np.shape(vdb)


sen = np.vstack((d[:,5]))
vsense = sen
print np.shape(vsense)


fig = plt.figure()
ax1 = fig.add_subplot(211)

ax1.plot(freq, vdb, 'b.')
#ax1.plot(freq, vsense, 'g.')
ax1.set_xlabel('Frequency (Hz)')
# Make the y-axis label and tick labels match the line color.
ax1.set_ylabel('Amplitude dB', color='b')
for tl in ax1.get_yticklabels():
    tl.set_color('b')





ax2 = ax1.twinx()

ax2.plot(freq, phase, 'r.')
#ax2.plot(freq, ip, 'y.')
ax2.set_ylabel('phase (deg)', color='r')
for tl in ax2.get_yticklabels():
    tl.set_color('r')

#ax1.set_xscale('log')
#ax2.set_xscale('log')
ax1.set_xlim((10000000,20000000))
ax2.set_xlim((10000000,20000000))



ax3 = fig.add_subplot(212)
ax3.plot(freq, vsense, 'g.')


ax1.add_line(Line2D([13560000,13560000],[-20,20]))
ax3.add_line(Line2D([13560000,13560000],[-10,10]))

plt.show()


for i in  freq[:20]:
    print i
