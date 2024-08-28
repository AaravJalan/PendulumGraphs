import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

# Underdamped
b_u = 0.2
m_u = 0.5
g_u = 9.81
l_u = 2.5
A_u = 1.0053
phi_u = 0.102778689405

# Critically Damped
b_c = 0.5
m_c = 0.25
A_c = 1
B_c = 1

# Overdamped
b_o = 0.9
m_o = 0.4
A1_o = 1
A2_o = 0
g_o = 9.8
l_o = 24.5

# Time variable
t = np.linspace(0, 25, 700)

# Underdamped function
theta_underdamped = A_u * np.exp(-b_u / (2 * m_u) * t) * np.cos(t * np.sqrt(g_u / l_u - (b_u**2) / (4 * m_u**2)) - phi_u)

# Critically damped function
theta_critically = np.exp(-b_c / (2 * m_c) * t) * (A_c * t + B_c)

# Overdamped function
theta_overdamped = np.exp(-b_o / (2 * m_o) * t) * (
    A1_o * np.exp(t * np.sqrt((b_o / (2 * m_o))**2 - g_o / l_o)) +
    A2_o * np.exp(-t * np.sqrt((b_o / (2 * m_o))**2 - g_o / l_o))
)

theta_normal = np.cos(t * np.sqrt(g_u / l_u - (b_u**2) / (4 * m_u**2)))

plt.figure(figsize=(10, 6))
plt.axhline(0, color='darkgrey', linewidth=1)  

# Creating the plot
plt.plot(t, theta_normal, label=r'Undamped', color='green', alpha=0.6, linewidth=0.75)
plt.plot(t, theta_underdamped, label=r'Underdamped', color='black')
plt.plot(t, theta_critically, label=r'Critically Damped', color='blue')
plt.plot(t, theta_overdamped, label=r'Overdamped', color='red')

# Adding labels and legend
plt.xlabel(r'$t\text{ (}s\text{)}$', fontsize=13)
plt.ylabel(r'$\theta\text{ (rad)}$', fontsize=13)
plt.legend(loc='upper right', fontsize=11)
plt.grid(True, which='both', linestyle='--', linewidth=0.4)

# Setting axis limits and ticks
plt.xlim(left=0, right=25)
plt.ylim(-1.25, 1.25)
plt.yticks([-1, -0.5, 0, 0.5, 1], [r'$-\theta_0$', r'$-\frac{\theta_0}{2}$', r'$0$', r'$\frac{\theta_0}{2}$', r'$\theta_0$'], fontsize=12)
plt.xticks(fontsize=12)

plt.savefig("AllDampingGraphs.png", dpi=300, bbox_inches='tight')
plt.show() # Showing the Plot