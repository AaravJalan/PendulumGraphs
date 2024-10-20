import numpy as np
import matplotlib.pyplot as plt

# Defining the function for the pendulum period
def pendulum_period(theta_0_rad, l):
    # Calculate the period using the given formula
    T = 2 * np.pi * np.sqrt(l / 9.8) * (
        1 +
        (1/4 * np.sin(theta_0_rad / 2)**2) +
        (9/64 * np.sin(theta_0_rad / 2)**4) +
        (25/256 * np.sin(theta_0_rad / 2)**6) +
        (49/1024 * np.sin(theta_0_rad / 2)**8) +
        (81/4096 * np.sin(theta_0_rad / 2)**10) +
        (121/16384 * np.sin(theta_0_rad / 2)**12) +
        (169/65536 * np.sin(theta_0_rad / 2)**14) +
        (225/262144 * np.sin(theta_0_rad / 2)**16) +
        (289/1048576 * np.sin(theta_0_rad / 2)**18) +
        (361/4194304 * np.sin(theta_0_rad / 2)**20)
    )
    return T

# Creating an array of theta values from -90 to 90 degrees
theta_values = np.linspace(-np.pi/2,np.pi/2, 700)

# Calculating the corresponding period values
T_values_a = pendulum_period(theta_values, 5)      # Length = 1.00 m
T_values_b = pendulum_period(theta_values, 6)   # Length = 1.25 m
T_values_c = pendulum_period(theta_values, 7)    # Length = 1.50 m

# Calculating the constant periods
T1_values = 2 * np.pi * np.sqrt(5 / 9.8)
T2_values = 2 * np.pi * np.sqrt(6 / 9.8)
T3_values = 2 * np.pi * np.sqrt(7 / 9.8)

plt.axvline(0, color='darkgrey', linewidth=1)

# Creating the plot
plt.figure(figsize=(10, 6))
plt.plot(theta_values, T_values_c, label=r'$l = 7 \, \text{m}$', color='green', linewidth=1.5)
plt.axhline(T3_values, color='green', linestyle='--', linewidth=1.25)

plt.plot(theta_values, T_values_b, label=r'$l = 6 \, \text{m}$', color='red', linewidth=1.5)
plt.axhline(T2_values, color='red', linestyle='--', linewidth=1.25)

plt.plot(theta_values, T_values_a, label=r'$l = 5 \, \text{m}$', color='blue', linewidth=1.5)
plt.axhline(T1_values, color='blue', linestyle='--', linewidth=1.25)

# Add labels and legend
plt.xlabel(r'$\theta_0 \text{ / }rad$', fontsize=13, labelpad=10)
plt.ylabel(r'$T \text{ / } s$', fontsize=13, labelpad=13)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.legend(loc='upper right', fontsize=11)

# Setting limits for the axes
plt.xlim(-np.pi/2, np.pi/2)
plt.ylim(4, 7)  # Adjusted y-limits
plt.xticks([-np.pi/2, -np.pi/4, 0, np.pi/4, np.pi/2], [r'$-\frac{\pi}{2}$', r'$-\frac{\pi}{4}$', r'$0$', r'$\frac{\pi}{4}$',r'$\frac{\pi}{2}$',], fontsize=12)
plt.yticks([4, 4.5, 5, 5.5, 6, 6.5, 7], fontsize=12)
plt.grid(True, which='both', linestyle='--', linewidth=0.4)


plt.savefig("ExactPeriod.png", dpi=300, bbox_inches='tight')
plt.show() # Showing the plot
