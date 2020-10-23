# Title: 1a.py
# Purpose: To compute mean square error (MSE) vs. number of components (N) for a series of pulses with height 1
# Developers: Siddesh Sood, Shawn Boyd, Cameron Palmer
# Last Modified: October 23, 2020

# Importing libraries
import numpy as np
import matplotlib.pyplot as plt
import math as m

# Defining constants
PI = np.pi  # Pi
j = complex(0, 1)  # A complex number
e = m.e
T = 4  # Period between pulses
d = 2  # The length of the pulse
OMEGA = (2*PI)/T

def sincMe(x):
    y = 0
    if x != 0:
        y = np.sin(x)/x
    return y

# How many components to create and sum (a large number)
N = 100000



# Create an independent variable t to fit exactly one period T
indep_var = np.array(np.arange(0, T, 0.01).tolist())

# An array of Ns. Set NMax to the maximum number of Ns you want your signals to go to
NMax = 1000
NArray = np.array(np.arange(10, NMax, 10).tolist())

# Create the variable that will hold all signals
signals = np.zeros((len(indep_var), len(NArray) + 1))


signals[:, 0] = np.array([(d/T) * (sincMe((k*OMEGA*d * (1/2))))*e**(j*k*OMEGA*indep_var) for k in range(int(-N/2), int(N/2))]).sum(axis=0)
signals[:, 0] = signals[:, 0] + 0.5


# Compute the rest of the signals. Each has a different N
i = 0

for n in NArray:
    signals[:, i] = np.array(
        [(d / T) * (sincMe((k * OMEGA * d * (1 / 2)))) * e ** (j * k * OMEGA * indep_var) for k in
         range(int(-n / 2), int(n / 2))]).sum(axis=0)

    signals[:, i] = signals[:, i] + 0.5

    i = i + 1


# Original signal x1(t) for comparison purposes
x = 1*((indep_var <= 1) | ((indep_var >= (T-1)) & (indep_var <= T)))

# Computing Mean Square Error
MSE = np.zeros(len(NArray))
M = len(x)

for i in range(0, len(MSE)):
    MSE[i] = (1/M) * np.array([np.abs(x[k] - signals[k, i]) for k in range(1, M)]).sum(axis=0)

print(MSE)


plt.figure(2)
plt.plot(NArray, MSE)
plt.title("Number of Components (N) vs. Mean Square Error (MSE)")
plt.xlabel("N")
plt.ylabel("MSE")

plt.figure(0)
plt.plot(indep_var, x)
plt.title("Original Signal x(t), One Period")
plt.xlabel("t")
plt.ylabel("x1(t)")
#plt.show()



# Create many signals for comparison (signalN, where N is # of components)




plt.figure(1)
plt.plot(indep_var, signals[:, 1])
plt.title("Reconstructed Signal x(t), One Period")
plt.xlabel("t")
plt.ylabel("x1(t)")
plt.show()


