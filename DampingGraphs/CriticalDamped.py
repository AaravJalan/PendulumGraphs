import numpy as np
import matplotlib.pyplot as plt

# Critically Damped Parameters
b_c = 0.5
m_c = 0.25
A_c = 1
B_c = 1

# Time Variable
t = np.linspace(0, 25, 700)

# Critically Damped Function
theta_critically = np.exp(-b_c / (2 * m_c) * t) * (A_c * t + B_c)
fig, ax = plt.subplots(figsize=(7, 6))
plt.plot(t, theta_critically, label=r'Critically Damped', color='blue')

# Text Box to Display the Parameters
textstr = '\n'.join((
    r'$b=%.1f$' % (b_c, ),
    r'$m=%.1f$' % (m_c, )))

props = dict(boxstyle='round', facecolor='white', alpha=0.8, edgecolor='lightgrey')

ax.text(0.8725, 0.9, textstr, transform=ax.transAxes, fontsize=11,
        verticalalignment='top', bbox=props)

# Adding labels and legend
plt.xlabel(r'$t\text{ (}s\text{)}$', fontsize=13)
plt.ylabel(r'$\theta\text{ (rad)}$', fontsize=13)
plt.legend(loc='upper right', fontsize=11)
plt.grid(True, which='both', linestyle='--', linewidth=0.4)

# Setting axis limits and ticks
plt.xlim(left=0, right=25)
plt.ylim(-0.05, 1.25)
plt.yticks([0, 0.5, 1], [r'$0$', r'$\frac{\theta_0}{2}$', r'$\theta_0$'], fontsize=12)
plt.xticks(fontsize=12)

plt.savefig("CriticallyDamped.png", dpi=300, bbox_inches='tight')
plt.show() # Showing the plot