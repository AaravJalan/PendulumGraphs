import matplotlib.pyplot as plt
import numpy as np

# Defining the range for x values
x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)

# Defining the functions
y_x = x
y_tanx = np.tan(x)
y_sinx = np.sin(x)

# Creating the Plot
plt.figure(figsize=(10, 6))
plt.plot(x, y_tanx, label=r'$\tan(\theta)$', color='red')
plt.plot(x, y_x, label=r'$\theta$', color='blue')
plt.plot(x, y_sinx, label=r'$\sin(\theta)$', color='green')

# Adding Labels and Legend
plt.xlabel(r'$t\text{ y }s$', fontsize=13)
plt.xlabel(r'$\theta\text{ / }\text{rad}$', fontsize=13)
plt.ylabel('y')

plt.ylim(0, 1)
plt.xlim(0, 1)

plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True, linestyle='--', alpha=0.7)

plt.legend(fontsize=11)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

plt.savefig("SqueezeTheorem.png", dpi=300, bbox_inches='tight')
plt.show() # Showing the plot