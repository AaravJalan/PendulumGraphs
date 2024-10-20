import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Defining Differential Equations
def model(Y, t):
    x, y = Y
    dxdt = y
    dydt = -g/l * x - b/m * y + F*np.cos(w*t)
    return [dxdt, dydt]

# # Low Damping
# b, m, g, l, w, F, t0 = 0.2, 0.5, 9.8, 2.5, 1, 3, 0.1

# # High Damping
# b, m, g, l, w, F, t0 = 0.5, 0.5, 9.8, 2.5, 1, 3, 0.1

# # Equal Frequencies
# b, m, g, l, w, F, t0 = 0, 0.5, 9.8, 9.8, 1, 0.25, -0.1

# Creating a Meshgrid for the Vector Field
x, y = np.meshgrid(np.linspace(-3.5, 3.5, 35), np.linspace(-3.5, 3.5, 27))

# Calculating the Vector Field
u = y
v = -g/l*x - b/m*y + np.cos(w*0)

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

# Setting the Figure Size
fig, ax = plt.subplots(figsize=(7, 6))

plt.axhline(0, color='darkgrey', linewidth=0.8)  
plt.axvline(0, color='darkgrey', linewidth=0.8)  

# Plotting the Vector Field
plt.quiver(x, y, u, v, color=colors, angles='xy', scale_units='xy', scale=1, width=0.002)

# Initial Conditions for the Solution Curve
Y0 = [t0, 0]  
t = np.linspace(0, 40, 10000)  

# Integrating the System of Equations
sol = odeint(model, Y0, t)

dot_index = 0  
plt.scatter(sol[dot_index, 0], sol[dot_index, 1], color='mediumblue', zorder=5)  

# Plotting the Solution Curve
plt.plot(sol[:, 0], sol[:, 1], color='blue', linewidth=1.5, label='Solution Curve')

# Adding Labels and Title
plt.xlabel(r'$\theta\text{ / } rad$', fontsize=17, labelpad=10)
plt.ylabel(r'$\frac{d\theta}{dt} \text{ / } rad \text{ } s^{-1}$', fontsize=17, labelpad=10)
plt.legend(fontsize=12)
plt.xlim(-2.5, 2.5)
plt.ylim(-2.5, 2.5)

# Customizing the Plot
plt.xticks([-np.pi/2, 0, np.pi/2],
           [r'$-\frac{\pi}{2}$', r'$0$', r'$\frac{\pi}{2}$'],fontsize=20)
plt.yticks(np.arange(-2, 3, 1), fontsize=20)

plt.grid(True, which='both', linestyle='--', linewidth=0.5)  

# plt.savefig("EqualFrequencies.png", dpi=300, bbox_inches='tight')
# plt.savefig("LowDampedDriven.png", dpi=300, bbox_inches='tight')
# plt.savefig("HighDampedDriven.png", dpi=300, bbox_inches='tight')

plt.show() # Showing the plot