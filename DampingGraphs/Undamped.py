import numpy as np
import matplotlib.pyplot as plt

# Undamped Paramters
b = 0.2
m = 0.5
g = 9.81
l = 2.5

# Time Variable
t = np.linspace(0, 25, 700)

theta_normal = np.cos(t * np.sqrt(g / l - (b**2) / (4 * m **2)))

fig, ax = plt.subplots(figsize=(10, 6))
plt.axhline(0, color='darkgrey', linewidth=1)  

# Creating the plot
plt.plot(t, theta_normal, label=r'Undamped', color='green')

# Text Box to Display the Parameters
textstr = r'$w_0=%.1f$' % (2)

props = dict(boxstyle='round', facecolor='white', alpha=0.8, edgecolor='lightgrey')

ax.text(0.905, 0.9, textstr, transform=ax.transAxes, fontsize=11,
        verticalalignment='top', bbox=props)

# Adding labels and legend
plt.xlabel(r'$t\text{ / }s$', fontsize=13, labelpad=10)
plt.ylabel(r'$\theta\text{ / } rad$', fontsize=13, labelpad=10)
plt.legend(loc='upper right', fontsize=11)
plt.grid(True, which='both', linestyle='--', linewidth=0.4)

# Setting axis limits and ticks
plt.xlim(left=0, right=25)
plt.ylim(-1.25, 1.25)
plt.yticks([-1, -0.5, 0, 0.5, 1], [r'$-\theta_0$', r'$-\frac{\theta_0}{2}$', r'$0$', r'$\frac{\theta_0}{2}$', r'$\theta_0$'], fontsize=12)
plt.xticks(fontsize=12)

plt.savefig("Undamped.png", dpi=300, bbox_inches='tight')
plt.show() # Showing the Plot