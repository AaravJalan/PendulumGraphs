import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Defining Differential Equations
def model(Y, t):
    x, y = Y
    dxdt = y
    dydt = -g/l * np.sin(x) - b/m * y
    return [dxdt, dydt]

# Creating a Meshgrid for the Vector Field
x, y = np.meshgrid(np.linspace(-2.5*np.pi, 2.5*np.pi, 33), np.linspace(-3, 3, 22))

b, m, g, l = 0.23, 1, 9.8, 10 # Pendulum Parameters

# Calculating the Vector Field
u = y
v = -g/l * np.sin(x) - b/m * y

# Key Points for Smallest Arrows
key_points = [-2*np.pi, -np.pi, 0, np.pi, 2*np.pi]

# Calculating distance from nearest key point horizontally
distance_from_key_points_x = np.min([np.abs(x - kp) for kp in key_points], axis=0)

# Combining vertical and horizontal distances for arrow length scaling
distance_from_key_points = np.sqrt(distance_from_key_points_x**2 + y**2)

# Normalising and Scaling Arrows Based on Distance from Key Points
max_distance = np.max(distance_from_key_points)
arrow_length = np.clip(distance_from_key_points / max_distance, 0.1, 1) * 0.45

# Normalising Vectors
norm = np.sqrt(u**2 + v**2)
norm[norm == 0] = 1
u = (u / norm) * arrow_length
v = (v / norm) * arrow_length

# Creating a Color Map Based on Position
colors = plt.cm.viridis((distance_from_key_points.flatten() - distance_from_key_points.min()) / (distance_from_key_points.max() - distance_from_key_points.min()))

# Setting the Figure Size
fig, ax = plt.subplots(figsize=(13.33, 5.2))

# Axes Lines
plt.axhline(0, color='darkgrey', linewidth=0.8)  
plt.axvline(0, color='darkgrey', linewidth=0.8)  

# Plotting the Vector Field
plt.quiver(x, y, u, v, color=colors, angles='xy', scale_units='xy', scale=1, width=0.0014)

# Initial conditions for the solution curve
Y01 = [0, 2.6]
t1 = np.linspace(0, 40, 200)  
Y02 = [-2*np.pi, 2.4]
t2 = np.linspace(0, 40, 200)  
Y03 = [-0.5*np.pi, 0]
t3 = np.linspace(0, 40, 200)  
# Y04 = [2*np.pi, -2.003]
# t4 = np.linspace(0, 20, 200)  

# Integrating the System of Equations
sol1 = odeint(model, Y01, t1)
sol2 = odeint(model, Y02, t2)
sol3 = odeint(model, Y03, t3)
# sol4 = odeint(model, Y04, t4)

# Plotting the Solution Curve
plt.plot(sol2[:, 0], sol2[:, 1], color='red', linewidth=1.5, label='Curve 1')
plt.plot(sol1[:, 0], sol1[:, 1], color='green', linewidth=1.5, label='Curve 2')
plt.plot(sol3[:, 0], sol3[:, 1], color='magenta', linewidth=1.5, label='Curve 3')

index = 0
plt.scatter(sol1[index, 0], sol1[index, 1], color='darkgreen', zorder=5)
plt.scatter(sol2[index, 0], sol2[index, 1], color='maroon', zorder=5)
plt.scatter(sol3[index, 0], sol3[index, 1], color='purple', zorder=5)

# Plotting Smaller Dots at Key Points
for kp in key_points[::2]:
    plt.scatter(kp, 0, color='blue', s=15, zorder=5)  # Blue Dots

for kp in key_points[1::2]:
    plt.scatter(kp, 0, color='red', s=15, zorder=5)  # Red Dots

# Text Box to Display the Parameters
textstr = r'$l=%.1f$' % (l, )

props = dict(boxstyle='round', facecolor='white', alpha=1, edgecolor='lightgrey')

ax.text(0.82, 0.965, textstr, transform=ax.transAxes, fontsize=12,
        verticalalignment='top', bbox=props)

# Adding Labels and Title
plt.xlabel(r'$\theta\text{ / } rad$', fontsize=13, labelpad=10)
plt.ylabel(r'$\frac{d\theta}{dt} \text{ / } rad \text{ } s^{-1}$', fontsize=13, labelpad=10)
plt.legend(fontsize=10)
plt.xlim(-2.5*np.pi, 2.5*np.pi)
plt.ylim(-3, 3)

# Customizing the Plot
plt.xticks([-2*np.pi, -np.pi, 0, np.pi, 2*np.pi],
           [r'$-2\pi$', r'$-\pi$', r'$0$', r'$\pi$', r'$2\pi$'], fontsize=12)
plt.yticks(np.arange(-3, 4, 1), fontsize=12)
plt.grid(True, which='both', linestyle='--', linewidth=0.5)  

plt.savefig("DampedExact.png", dpi=300, bbox_inches='tight')
plt.show() # Showing the plot