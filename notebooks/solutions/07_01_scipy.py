"""Exercise 1"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.signal import butter, lfilter
from scipy import fftpack

def gaussian(x, mu, sigma, A):
    return A*np.exp(-(x - mu)**2/(2*sigma**2))

sample_rate = 30
T = 5
t = np.linspace(0, T, T*sample_rate, endpoint=False)
y = gaussian(t, 3.1, 0.2, 3) + np.sin(1.2*2*np.pi*t) + 1.5*np.cos(9*2*np.pi*t)
plt.plot(t, y)

z = fftpack.rfft(y)
f = fftpack.rfftfreq(len(t), t[1] - t[0])

maxima = f[np.abs(z)**2 > 2100]
print("Noise frequencies:", maxima)

plt.figure(1)
plt.plot(f, np.abs(z)**2)
plt.xlabel('f / Hz')
for freq in maxima:
    plt.axvline(x=freq, color='black', alpha=0.3, lw=5)
plt.title('Discovery of Noise Frequencies')

def bandstop_filter(data, freq_window, fs, order=5):
    nyquist_frequency = fs/2
    freq_window = np.array(freq_window)
    normal_freq = freq_window/nyquist_frequency
    b, a = butter(order, normal_freq, btype='bandstop')
    y = lfilter(b, a, data)
    return y

plt.figure(2)
sample_rate = (len(t) - 1)/(t[-1])
y_filt = bandstop_filter(y, [1.15, 1.25], sample_rate)
y_filt = bandstop_filter(y_filt, [8.9, 9.1], sample_rate)
plt.plot(t, y_filt)
plt.title('Data after bandstop filtering')

params, __ = curve_fit(gaussian, t, y_filt)
print("Gaussian paramaters:", params)

plt.figure(3)
plt.plot(t, gaussian(t, *params))
plt.plot(t, y_filt)
plt.title('Filtered data fit with Gaussian');


"""Exercise 2"""

from scipy.special import eval_legendre
from scipy.integrate import quad

def f(x):
    return np.sin(np.pi*x)

def a(n):
    g = lambda x: f(x)*eval_legendre(n, x)
    integral = quad(g, -1, 1)[0]
    return (2*n + 1)/2 * integral

# first few a_n coefficients up to n = 5
print("Coefficients:", [a(n) for n in range(5+1)])

def legendre_series(x, N):
    y = np.zeros(len(x))
    for n in range(N+1):
        y += a(n)*eval_legendre(n, x)
    return y

x = np.linspace(-1, 1, 100)
plt.plot(x, f(x), label=r'$\sin(nx)$')
plt.plot(x, legendre_series(x, 5), label=r'$\sum_{n=0}^{5} a_n P_n(x)$')
plt.legend(loc='best');
