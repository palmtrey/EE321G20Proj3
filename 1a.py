# Title: 1a.py
# Purpose: EE 321 Project 3. To graph the signal given in section 1a, as well as its counterparts reconstructed with fewer components than the original signal
# Developers: Siddesh Sood, Shawn Boyd, Cameron Palmer
# Last Modified: October 23, 2020

# Importing libraries
import numpy as np
import matplotlib.pyplot as plt

# Defining constants
PI = np.pi
T = 2
OMEGA = (2*PI)/T
j = complex(0, 1)

# Defining the signal
indep_var = np.array(np.arange(0, 2, 0.01).tolist())
dep_var = 1 + (1/2) * np.cos(OMEGA * indep_var) + np.sin(2 * OMEGA * indep_var)


dep_varN4 = 1+(1/2)*np.cos(OMEGA*indep_var) + (1/2) * np.sin(2*OMEGA*indep_var) + (1/(j*2)) * np.cos(2*OMEGA*indep_var)
dep_varN3 = 1 + 1/4*((np.cos(OMEGA*indep_var)) + j*np.sin(OMEGA*indep_var)) + 1/(j*2)*(np.cos(2*OMEGA*indep_var) + j*(np.sin(2*OMEGA*indep_var)))

plt.figure(0)
plt.plot(indep_var, dep_var)
plt.title('Graph of x(t) = 1 + 1/2 cos(wt) + sin(2wt)')
plt.xlabel("t")
plt.ylabel("x(t)")

plt.figure(1)
plt.plot(indep_var, dep_varN4)
plt.title("Graph of x4(t) = 1 + 1/2 cos(wt) + 1/2sin(wt) + 1/j2 cos(2wt)")
plt.xlabel("t")
plt.ylabel("x(t)")

plt.figure(2)
plt.plot(indep_var, dep_varN3)
plt.title("Graph of x3(t) = 1 + 1/4 (cos(wt) + jsin(wt)) + 1/j2 (cos(2wt) + jsin(2wt)")
plt.xlabel("t")
plt.ylabel("x(t)")



plt.show()