import numpy as np
import matplotlib.pyplot as plt

# Underdamped Parameters
b_u = 0.2
m_u = 0.5
g_u = 9.81
l_u = 2.5
A_u = 1.0053
phi_u = 0.102778689405

# Time Variable
t = np.linspace(0, 25, 700)

# Underdamped Function
theta_underdamped = A_u * np.exp(-b_u / (2 * m_u) * t) * np.cos(t * np.sqrt(g_u / l_u - (b_u**2) / (4 * m_u**2)) - phi_u)
asymptote_a = A_u * np.exp(-b_u / (2 * m_u) * t)
asymptote_b = -1 * A_u * np.exp(-b_u / (2 * m_u) * t)

fig, ax = plt.subplots(figsize=(7, 6))
plt.axhline(0, color='darkgrey', linewidth=1)  

# Plot the data
line1, = plt.plot(t, theta_underdamped, label=r'Underdamped', color='black')
line2, = plt.plot(t, asymptote_a, color='red', label=r'$\pm e^{-\beta t}$', alpha=0.2)
plt.plot(t, asymptote_b, color='red', alpha=0.2)  # This plot is not included in the legend

# Adding labels and legend
plt.xlabel(r'$t\text{ (}s\text{)}$', fontsize=13)
plt.ylabel(r'$\theta\text{ (rad)}$', fontsize=13)
plt.legend(loc='upper right', fontsize=11)
ax.grid(True)

# Setting axis limits and ticks
ax.set_xlim(left=0, right=25)
ax.set_ylim(-1.25, 1.25)
ax.set_yticks([-1, -0.5, 0, 0.5, 1])
ax.set_yticklabels([r'$-\theta_0$', r'$-\frac{\theta_0}{2}$', r'$0$', r'$\frac{\theta_0}{2}$', r'$\theta_0$'], fontsize=12)

# Text Box to Display the Parameters
textstr = '\n'.join((
    r'$b=%.1f$' % (b_u, ),
    r'$m=%.1f$' % (m_u, ),
    r'$g=%.2f$' % (g_u, ),
    r'$l=%.1f$' % (l_u, )))

props = dict(boxstyle='round', facecolor='white', alpha=0.8, edgecolor='lightgrey')

ax.text(0.865, 0.855, textstr, transform=ax.transAxes, fontsize=11,
        verticalalignment='top', bbox=props)

plt.savefig("Underdamped.png", dpi=300, bbox_inches='tight')
plt.show() # Showing the plot
