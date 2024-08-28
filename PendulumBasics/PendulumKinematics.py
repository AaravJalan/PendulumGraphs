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

plt.xlabel(r'$\theta\text{ / }\text{rad}$', fontsize=13, fontweight='bold')
plt.ylabel(r'$\text{Magnitude}$', fontsize=13, fontweight='bold')
plt.legend(loc='lower right', fontsize=11)
plt.grid(True, which='both', linestyle='--', linewidth=0.5)  

# Setting axis limits and ticks
plt.xlim(left=0, right= 2*np.pi)
plt.xticks([0, np.pi/2, np.pi, 1.5*np.pi, 2*np.pi], [r'$\theta_0$', r'$0$', r'$-\theta_0$', r'$0$', r'$\theta_0$'], fontsize=12)
plt.ylim(-1.05, 1.05)
plt.yticks([-1, -0.5, 0, 0.5, 1], [r'$-\text{Max}$', r'$-\frac{\text{Max}}{2}$', r'$0$', r'$\frac{\text{Max}}{2}$', r'$\text{Max}$'], fontsize=12)

plt.savefig("PendulumKinematics.png", dpi=300, bbox_inches='tight')
plt.show() # Showung the plot