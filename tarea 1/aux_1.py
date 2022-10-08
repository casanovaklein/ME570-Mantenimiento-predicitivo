import numpy as np
import matplotlib.pyplot as plt

dt = 0.005 # paso de tiempo
dt2 = 0.035
df = 1/dt # frecuencia de muestreo
N1 = 256 # numero de puntos
T1 = dt*N1 # tiempo final
T2 = dt2*N1
t = np.arange(dt, T1,dt) # discretizacion temporal
t2 = np.linspace(dt2, T2, N1, endpoint=True)
x = 10*np.sin(50*np.pi*t) # senal disretizada
x2 = 10*np.sin(50*np.pi*t2)

# plots..
plt.figure()
plt.plot(t, x, label = 'dt = 0.005')
plt.plot(t2, x2 ,label = 'dt = 0.035')
#plt.scatter(t, x, label ='puntos discretos', c='r')
plt.ylim(-15, 15)
plt.xlim(0,1)
plt.legend()
plt.show()

from scipy.fft import fft, fftfreq

xf_crudo = fft(x)
w_crudo = fftfreq(len(t), dt)


xf_crudo2 = fft(x2)
w_crudo2 = fftfreq(len(t2), dt2)

# tenemos que hacer ciuertas manipuaciones a estos arrays para conseguir solo frecuencias postivas y que ademas se converve la energia
xf = 2/len(xf_crudo)*np.abs(xf_crudo[0:len(xf_crudo)//2])
wf = w_crudo[:len(w_crudo)//2]


xf2 = 2/len(xf_crudo2)*np.abs(xf_crudo2[0:len(xf_crudo2)//2])
wf2 = w_crudo2[:len(w_crudo2)//2]

plt.figure(2)
plt.plot(wf2, xf2)
plt.plot(wf, xf)
plt.grid()
plt.show()