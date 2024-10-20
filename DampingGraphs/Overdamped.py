import numpy as np
import matplotlib.pyplot as plt

# Overdamped Paramters
b_o = 0.9
m_o = 0.4
A1_o = 1
A2_o = 0
g_o = 9.8
l_o = 24.5

# Time variable
t = np.linspace(0, 25, 700)

# Overdamped Function
theta_overdamped = np.exp(-b_o / (2 * m_o) * t) * (
    A1_o * np.exp(t * np.sqrt((b_o / (2 * m_o))**2 - g_o / l_o)) +
    A2_o * np.exp(-t * np.sqrt((b_o / (2 * m_o))**2 - g_o / l_o))
)

fig, ax = plt.subplots(figsize=(7, 6))
plt.axhline(0, color='darkgrey', linewidth=1)
plt.plot(t, theta_overdamped, label=r'Overdamped', color='red')

# Text Box to Display the Parameters
textstr = '\n'.join((
    r'$b=%.1f$' % (b_o, ),
    r'$m=%.1f$' % (m_o, ),
    r'$g=%.2f$' % (g_o, ),
    r'$l=%.1f$' % (l_o, )))

props = dict(boxstyle='round', facecolor='white', alpha=0.8, edgecolor='lightgrey')

ax.text(0.865, 0.9, textstr, transform=ax.transAxes, fontsize=11,
        verticalalignment='top', bbox=props)

# Adding labels and legend
plt.xlabel(r'$t\text{ / }s$', fontsize=13, labelpad=10)
plt.ylabel(r'$\theta\text{ / } rad$', fontsize=13, labelpad=10)
plt.legend(loc='upper right', fontsize=11)
plt.grid(True, which='both', linestyle='--', linewidth=0.4)

# Setting axis limits and ticks
ax.set_xlim(left=0, right=25)
ax.set_ylim(-0.05, 1.25)
ax.set_yticks([0, 0.5, 1], [r'$0$', r'$\frac{\theta_0}{2}$', r'$\theta_0$'], fontsize=12)

plt.savefig("Overdamped.png", dpi=300, bbox_inches='tight')
plt.show() # Showing the plot