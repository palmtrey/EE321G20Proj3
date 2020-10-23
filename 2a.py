# Title: 1a.py
# Purpose: To compute mean square error (MSE) vs. number of components (N) for a series of pulses with height 1
# Developers: Siddesh Sood, Shawn Boyd, Cameron Palmer
# Last Modified: October 22, 2020

# Importing libraries
import numpy as np
import matplotlib.pyplot as plt
import math as m
import csv

# Defining constants
PI = np.pi  # Pi
j = complex(0, 1)  # A complex number
e = m.e
T = 4  # Period between pulses
d = 1  # The length of the pulse
OMEGA = (2*PI)/T

def sincMe(x):
    y = 0
    if x != 0:
        y = np.sin(x)/x
    return y

# How many components to create and sum (a large number)
N = 10000

NArray = np.array(np.arange(10, 10000, 10).tolist())

# Create an independent variable t to fit exactly one period T
indep_var = np.array(np.arange(0, T, 0.01).tolist())
almostPerfectSquare = np.array([(d/T) * ((sincMe((k*OMEGA*d * (1/2)))))*e**(j*k*OMEGA*indep_var) for k in range(int(-N/2), int(N/2))]).sum(axis=0)

#allSignalsOfN = np.array([(d/T) * (((m.sin((k*OMEGA*d)))/(k*OMEGA*d)) * (1/2))*e**(j*k*OMEGA*indep_var) for k in range(int(1), NArray)]).sum(axis=0)

# Actual real one period of signal x1(t)
x = 1*((indep_var <= 1) | ((indep_var >= (T-1)) & (indep_var <= T)))

plt.figure(0)
plt.plot(indep_var, x)
plt.title("Original Signal x(t), One Period")
plt.xlabel("t")
plt.ylabel("x1(t)")
#plt.show()



# Create many signals for comparison (signalN, where N is # of components)




plt.figure(1)
plt.plot(indep_var, almostPerfectSquare)
plt.title("Reconstructed Signal x(t), One Period")
plt.xlabel("t")
plt.ylabel("x1(t)")
plt.show()


