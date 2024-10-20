import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Defining Differential Equations
def model(Y, t):
    x, y = Y
    dxdt = y
    dydt = -g/l * x - b/m * y
    return [dxdt, dydt]

b, m, g, l = 0.2, 0.5, 9.8, 2.5 # Pendulum Parameters

# Creating a Meshgrid for the Vector Field
x, y = np.meshgrid(np.linspace(-3.5, 3.5, 35), np.linspace(-3.5, 3.5, 27))

# Calculating the Vector Field
u = y
v = -g/l*x - b/m*y

# Normalising and Scaling Arrows
lengths = np.sqrt(u**2 + v**2)
max_length = np.max(lengths)
arrow_length = np.clip(lengths / max_length, 0.05, 1) * 0.35

# Normalising Vectors
norm = np.sqrt(u**2 + v**2)
norm[norm == 0] = 1
u = (u / norm) * arrow_length
v = (v / norm) * arrow_length

# Creating a Color Map Based on Position
colors = plt.cm.viridis((lengths.flatten() - lengths.min()) / (lengths.max() - lengths.min()))

fig, ax = plt.subplots(figsize=(12, 6)) # Setting the Figure Size

plt.axhline(0, color='darkgrey', linewidth=0.8)  
plt.axvline(0, color='darkgrey', linewidth=0.8)  

# Plotting the Vector Field
plt.quiver(x, y, u, v, color=colors, angles='xy', scale_units='xy', scale=1, width=0.002)

# Initial Conditions for the Solution Curve
Y0 = [1, 0]  
t = np.linspace(0, 40, 10000)  

# Integrating the System of Equations
sol = odeint(model, Y0, t)

dot_index = 0  
plt.scatter(sol[dot_index, 0], sol[dot_index, 1], color='mediumblue', zorder=5)  

# Plotting the Solution Curve
plt.plot(sol[:, 0], sol[:, 1], color='blue', linewidth=1.5, label='Solution Curve')

# Text Box to Display the Parameters
textstr = '\n'.join((
    r'$b=%.1f$' % (b, ),
    r'$m=%.1f$' % (m, ),
    r'$l=%.1f$' % (l, ),
    r'$\theta_0=1$',
    r'$v_0=0$'))

props = dict(boxstyle='round', facecolor='white', alpha=1, edgecolor='lightgrey')

ax.text(0.9175, 0.9, textstr, transform=ax.transAxes, fontsize=12,
        verticalalignment='top', bbox=props)

# Adding Labels and Title
plt.xlabel(r'$\theta\text{ / } rad$', fontsize=13, labelpad=10)
plt.ylabel(r'$\frac{d\theta}{dt} \text{ / } rad \text{ } s^{-1}$', fontsize=13, labelpad=10)
plt.legend(fontsize=11)
plt.xlim(-2.5, 2.5)
plt.ylim(-2.5, 2.5)

# Customizing the Plot
plt.xticks([-np.pi/2, 0, np.pi/2],
           [r'$-\frac{\pi}{2}$', r'$0$', r'$\frac{\pi}{2}$'], fontsize=12.5)
plt.yticks(np.arange(-2, 3, 1), fontsize=12)

plt.grid(True, which='both', linestyle='--', linewidth=0.5)

plt.savefig("UnderdampedApprox.png", dpi=300, bbox_inches='tight')
plt.show() # Showing the plot