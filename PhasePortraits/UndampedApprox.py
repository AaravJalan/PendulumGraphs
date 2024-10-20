import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Defining Differential Equations
def model(Y, t):
    x, y = Y
    dxdt = y
    dydt = -x
    return [dxdt, dydt]

# Creating a Meshgrid for the Vector Field
x, y = np.meshgrid(np.linspace(-4, 4, 34), np.linspace(-4, 4, 34))

# Calculating the Vector Field
u = y
v = -x

# Calculating the distance from the center
lengths = np.sqrt(x**2 + y**2)
max_length = np.max(lengths)
arrow_length = np.clip(lengths / max_length, 0.05, 1)
arrow_length *= 0.4 

# Normalising Vectors and scale by arrow_length
norm = np.sqrt(u**2 + v**2)
norm[norm == 0] = 1
u = (u / norm) * arrow_length
v = (v / norm) * arrow_length

# Setting the Figure Size
fig, ax = plt.subplots(figsize=(6, 6))

# Axes Lines
plt.axhline(0, color='darkgrey', linewidth=0.8)  
plt.axvline(0, color='darkgrey', linewidth=0.8)  

# Creating a Color Map Based on Position
colors = plt.cm.viridis((lengths - lengths.min()) / (lengths.max() - lengths.min()))
colors = colors.reshape(-1, 4) 

# Initial conditions for the solution curve
Y0 = [1,0]
t = np.linspace(0, 10, 200)  

# Integrating the System of Equations
sol = odeint(model, Y0, t)

# Plotting the Solution Curve
plt.plot(sol[:, 0], sol[:, 1], color='blue', linewidth=2, label='Solution Curve')

dot_index = 0  
plt.scatter(sol[dot_index, 0], sol[dot_index, 1], color='mediumblue', zorder=5)  

# Plotting the Vector Field
plt.quiver(x, y, u, v, color=colors, angles='xy', scale_units='xy', scale=1, width=0.0025)

g = 9.8 # Pendulum Parameters

# Text Box to Display the Parameters
textstr = '\n'.join((
    r'$l=g=%.1f$' % (g, ),
    r'$\theta_0=1$',
    r'$v_0=0$'))

props = dict(boxstyle='round', facecolor='white', alpha=1, edgecolor='lightgrey')

ax.text(0.81, 0.9, textstr, transform=ax.transAxes, fontsize=11,
        verticalalignment='top', bbox=props)

# Adding Labels and Title
plt.xlabel(r'$\theta\text{ / } rad$', fontsize=13, labelpad=10)
plt.ylabel(r'$\frac{d\theta}{dt} \text{ / } rad \text{ } s^{-1}$', fontsize=13, labelpad=10)
plt.legend(fontsize=10)
plt.xlim(-2, 2)
plt.ylim(-2, 2)

# Customizing the Plot
plt.xticks([-np.pi/2, 0, np.pi/2],
           [r'$-\frac{\pi}{2}$', r'$0$', r'$\frac{\pi}{2}$'], fontsize=12)
plt.yticks(np.arange(-2, 3, 1), fontsize=12)
plt.grid(True, which='both', linestyle='--', linewidth=0.5)  

plt.savefig("UndampedApprox.png", dpi=300, bbox_inches='tight')

plt.show() # Showing the plot