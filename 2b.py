# Title: 1a.py
# Purpose: To compute mean square error (MSE) vs. number of components (N) for the signal given in part 2b of EE 321's Project 3
# Developers: Siddesh Sood, Shawn Boyd, Cameron Palmer
# Last Modified: October 22, 2020

# Importing libraries
import numpy as np
import matplotlib.pyplot as plt
import math as m

# Defining constants
PI = np.pi  # Pi
j = complex(0, 1)  # A complex number
e = m.e
T = 2  # Period between pulses
OMEGA = (2*PI)/T


# How many components to create and sum (a large number)
N = 100


# Create an independent variable t to fit exactly one period T
indep_var = np.array(np.arange(0, T, 0.01).tolist())

# An array of Ns. Set NMax to the maximum number of Ns you want your signals to go to
NMax = 1000
NArray = np.array(np.arange(10, NMax, 10).tolist())

# Create the variable that will hold all signals
signals = np.zeros((len(indep_var), len(NArray) + 1))


signals[:, 0] = np.array([(-1 + e**(-2*j*k*OMEGA)/(k**2*OMEGA**2*T))*e**(j*k*OMEGA*indep_var) for k in range(int(1), int(N+1))]).sum(axis=0)
#signals[:, 0] = signals[:, 0] + 0.5


# Compute the rest of the signals. Each has a different N
i = 0


for n in NArray:
    signals[:, i] = np.array(
        [(-1 + e**(-2*j*k*OMEGA)/(k**2*OMEGA**2*T)) for k in
         range(int(1), int(n + 1))]).sum(axis=0)

    signals[:, i] = signals[:, i] + 0.5

    i = i + 1


# Original signal x1(t) for comparison purposes
#x = (indep_var*(indep_var <= 1 & indep_var >= 0) | (2-indep_var) * ((indep_var >= 1) & (indep_var <= 2)))

"""
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
"""

plt.figure(0)
#plt.plot(indep_var, x)
plt.title("Original Signal x(t), One Period")
plt.xlabel("t")
plt.ylabel("x1(t)")
#plt.show()



# Create many signals for comparison (signalN, where N is # of components)




plt.figure(1)
plt.plot(indep_var, signals[:, 0])
plt.title("Reconstructed Signal x(t), One Period")
plt.xlabel("t")
plt.ylabel("x(t)")
plt.show()


