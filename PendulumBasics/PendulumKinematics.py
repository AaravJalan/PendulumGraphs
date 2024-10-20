import numpy as np
import matplotlib.pyplot as plt

# Time Variable
theta = np.linspace(0, 25, 700)

x = np.cos(theta)
v = -np.sin(theta)
a = -np.cos(theta)

plt.figure(figsize=(10, 6))

# Axes Lines
plt.axhline(0, color='darkgrey', linewidth=1)

# Creating the plot
plt.plot(theta, x, label=r'Displacement', color='green', alpha=0.8, linewidth=1.5)
plt.plot(theta, v, label=r'Velocity', color='blue', alpha=0.8, linestyle='--', linewidth=1.5)
plt.plot(theta, a, label=r'Acceleration', color='red', alpha=0.8, linestyle='--', linewidth=1.5)

plt.xlabel(r'$t\text{ / }s$', fontsize=14, labelpad=15)  # Lower the x-axis label
plt.ylabel(r'$\text{Magnitude}\text{  /  m, ms}^{-1},\text{ ms}^{-2}$', fontsize=13, labelpad=5)  # Move the y-axis label to the left
plt.legend(loc='lower right', fontsize=11)
plt.grid(True, which='both', linestyle='--', linewidth=0.5)  

# Setting axis limits and ticks
plt.xlim(left=0, right= 2*np.pi)
plt.xticks([0, np.pi/2, np.pi, 1.5*np.pi, 2*np.pi], [r'$0$', r'$\frac{T}{4}$', r'$\frac{T}{2}$', r'$\frac{3T}{2}$', r'$T$'], fontsize=13)
plt.ylim(-1.05, 1.05)
plt.yticks([-1, -0.5, 0, 0.5, 1], [r'$-\text{Max}$', r'$-\frac{\text{Max}}{2}$', r'$0$', r'$\frac{\text{Max}}{2}$', r'$\text{Max}$'], fontsize=13)

plt.savefig("PendulumKinematics.png", dpi=300, bbox_inches='tight')
plt.show() # Showing the plot