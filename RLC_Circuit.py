# Solving an RLC Circuit using Euler Method
import matplotlib.pyplot as plt
import numpy as np

# Circuit Parameters
R = 200 # Resistance (Ohms)
L = 5 # Inductance (Henries)
C = 0.0001 # Capacitance (Farads)
V = 0 # DC Voltage Source (Volts) - Set to 0 for natural response

# Initial conditions (t = 0)
i0 = 0 #current
q0 = 1 #charge

# Constant Coefficients
i_coeff = R/L
q_coeff = 1/(L*C)

# Time Parameters
t0 = 0 # Initial time
tf = 0.5 # Final time
dt = 0.0001 # Increment
num_steps = int((tf-t0)/dt)

#Creating Array
t_values = np.linspace(t0, tf, num_steps + 1)
i_values = np.zeros(num_steps + 1)
q_values = np.zeros(num_steps + 1)
i_values[0] = i0
q_values[0] = q0

for k in range(0, num_steps):
    i_values[k+1] = i_values[k] + (V - i_coeff * i_values[k] -q_coeff * q_values[k]) * dt
    q_values[k+1] = q_values[k] + i_values[k] * dt

# Graph for Current
plt.figure(1)
plt.plot(t_values, i_values)
plt.title("Figure 1: RLC Circuit Current Simulation using Euler Method")
plt.xlabel("Time (s)")
plt.ylabel("Current (A)")
plt.grid(True)

# Graph for Charge
plt.figure(2)
plt.plot(t_values, q_values)
plt.title("Figure 2: RLC Circuit Charge Simulation using Euler Method")
plt.xlabel("Time (s)")
plt.ylabel("Charge (C)")
plt.grid(True)

plt.show()