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
d = 2  # The length of the pulse
OMEGA = (2*PI)/T


# Define the constant for the number of terms that will reach us an "almost perfect" series of pulses.
# This will be the standard for what signals of lower constant 'N's will be compared to, as there isn't a nice way to
# represent a series of pulses in Python.

# How many components? A metric shit ton for our "original" (or as close to original as we can get) signal
N = 10000

# Create an independent variable t to fit exactly one period T
indep_var = np.array(np.arange(0, T, 0.01).tolist())
almostPerfectSquare = np.array([(d/T) * np.sinc((k*OMEGA*d) * (1/2))*e**(j*k*OMEGA*indep_var) for k in range(int((-N/2)), int(N/2))]).sum(axis=0)


print(almostPerfectSquare)
# Actual real one period of signal x1(t)
x = 1*((indep_var <= 1) | ((indep_var >= 3) & (indep_var <= 4)))

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


