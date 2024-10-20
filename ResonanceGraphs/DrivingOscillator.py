import numpy as np
import matplotlib.pyplot as plt

# Constants
beta = 0.2
B = 1
m = 1.0  # Mass (kg)
w = 1.0  # Frequency of the driving force (s^-1)
L = 9.81  # Length of pendulum (m)
g = 9.81  # Acceleration due to gravity (m/s^2)
F_0 = 10  # Amplitude of driving force (N)
w0 = np.sqrt(g / L)  # Natural frequency
wd = np.sqrt(w0**2-beta**2)
phi = np.arctan(beta/(np.sqrt(w0**2-beta**2)))
delt = np.pi/2

# Time Variable
t = np.linspace(0, 40, 700)

ht = B * np.exp(-beta * t) * np.cos(wd * t - phi)
A = F_0 / (m * L * np.sqrt((w0**2 - w**2)**2 + (2 * B * w)**2))
pt = A * np.cos(w * t - delt)
print(A)

res = pt + ht
fig, ax = plt.subplots(figsize=(10, 6))

plt.axhline(0, color='darkgrey', linewidth=1)  

# Plotting the data
line1, = plt.plot(t, ht, label=r'Without an External Driver', color='red', linewidth=0.95)
line2, = plt.plot(t, pt, label=r'External Driver', color='blue', linewidth=0.95)
line3, = plt.plot(t, res, label=r'Resultant', color='black', linestyle='--')

# Adding Labels and Title
plt.xlabel(r'$t\text{ / }s$', fontsize=13, labelpad=10)
plt.ylabel(r'$\theta\text{ / } rad$', fontsize=13, labelpad=10)
plt.legend(loc='upper right', fontsize=11)
ax.grid(True)

# Setting axis limits and ticks
ax.set_xlim(left=0, right=40)
ax.set_ylim(-1.25, 1.5)
ax.set_yticks([-1, -0.5, 0, 0.5, 1])
ax.set_yticklabels([r'$-\theta_0$', r'$-\frac{\theta_0}{2}$', r'$0$', r'$\frac{\theta_0}{2}$', r'$\theta_0$'],fontsize=12)

# Text Box to Display the Parameters
textstr = '\n'.join((
    r'$F=%.1f$' % (F_0,),
    r'$B=%.1f$' % (B,),
    r'$A=%.1f$' % (A, ),
    r'$l=g=%.1f$' % (L, ),
    r'$m=w=%.1f$' % (m,)))

props = dict(boxstyle='round', facecolor='white', alpha=1, edgecolor='lightgrey')

ax.text(0.87, 0.22, textstr, transform=ax.transAxes, fontsize=11,
        verticalalignment='top', bbox=props)

plt.savefig("DrivingOscillator.png", dpi=300, bbox_inches='tight')
plt.show() # Showing the plot
