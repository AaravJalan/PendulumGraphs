import numpy as np
import matplotlib.pyplot as plt

# Constants
m = 1.0  # Mass (kg)
l = 9.81  # Length of pendulum (m)
g = 9.81  # Acceleration due to gravity (m/s^2)
F_0 = 1.0  # Amplitude of driving force (N)
omega_0 = np.sqrt(g / l)  # Natural frequency

# Driving frequencies
omega = np.linspace(0, 2, 1000)  # Driving frequency range

# Different damping coefficients
beta_values = [0.2, 0.3, 0.4, 0.5, 1, 2]

# Setting the Figure Size
fig, ax = plt.subplots(figsize=(10,6))

for beta in beta_values:
    # Amplitude calculation for each damping coefficient
    A = F_0 / (m * l * np.sqrt((omega_0**2 - omega**2)**2 + (2 * beta * omega)**2))
    plt.plot(omega, A, label=f"$\\beta$ = {beta}")

# Text Box to Display the Parameters
textstr = '\n'.join((
    r'$m=%.1f$' % (m, ),
    r'$F_0=%.1f$' % (F_0, ),
    r'$l=%.1f$' % (l, )))

props = dict(boxstyle='round', facecolor='white', alpha=1, edgecolor='lightgrey')

ax.text(0.905, 0.575, textstr, transform=ax.transAxes, fontsize=11.5,
        verticalalignment='top', bbox=props)

plt.axvline(omega_0, color='r', linestyle='--', label=f"Natural Frequency $\\omega_0$")
plt.xlabel(r'$\omega \text{ / } rad \text{ } s^{-1}$', fontsize=13, labelpad=10)
plt.ylabel(r'$\text{Amplitude, }A$', fontsize=13, labelpad=10)

# Adding Labels and Title
plt.legend(fontsize=11)
plt.xlim(0, 2)
plt.ylim(0, 0.3)
plt.yticks(fontsize=12)
plt.xticks(fontsize=12)
plt.grid(True, which='both', linestyle='--', linewidth=0.5)  

plt.savefig("ResonanceCurves.png", dpi=300, bbox_inches='tight')
plt.show() # Showing the plot
