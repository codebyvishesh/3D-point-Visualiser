import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
try:
    x_cor = float(input("Enter the x coordinate of the point: "))
    y_cor = float(input("Enter the y coordinate of the point: "))
    z_cor = float(input("Enter the z coordinate of the point: "))
    a = float(input("Enter the a coefficient: "))
    b = float(input("Enter the b coefficient: "))
    c = float(input("Enter the c coefficient: "))
    d = float(input("Enter the d coefficient: "))
except ValueError:
    print("Error: Invalid input. Please ensure all inputs are numerical values.")
    exit()
denominator = (a**2) + (b**2) + (c**2)
if denominator == 0:
    print("Error: The coefficients a, b, and c cannot all be zero.")
    print("This condition does not define a valid plane for reflection.")
    exit()
numerator = (x_cor * a) + (y_cor * b) + (z_cor * c) + d
k = -2 * (numerator / denominator)
x_new = x_cor + (a * k)
y_new = y_cor + (b * k)
z_new = z_cor + (c * k)
print(f"Original Point P: ({x_cor}, {y_cor}, {z_cor})")
print(f"Reflected Point P: ({x_new}, {y_new}, {z_new})")
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x_cor, y_cor, z_cor, color='blue', s=100, label='Original Point P')
ax.scatter(x_new, y_new, z_new, color='green', s=100, label='Reflected Point P\'')
ax.plot([x_cor, x_new], [y_cor, y_new], [z_cor, z_new], 'k--', label='Line P to P\'')
r_max = max(abs(x_cor), abs(y_cor), abs(z_cor), abs(x_new), abs(y_new), abs(z_new), 5) * 1.5
xx, yy = np.meshgrid(np.linspace(-r_max, r_max, 20), np.linspace(-r_max, r_max, 20))
if c != 0:
    zz = (-d - a * xx - b * yy) / c
    ax.plot_surface(xx, yy, zz, alpha=0.5, color='green', label='Reflection Plane')
elif b != 0:
    yy_plane = (-d - a * xx) / b
    ax.plot_surface(xx, yy_plane, yy.T, alpha=0.5, color='green')
elif a != 0:
    xx_plane = -d / a
    ax.plot_surface(xx_plane, xx, yy.T, alpha=0.5, color='green')
else:
    print("Cannot plot a zero-coefficient plane (a=b=c=0).")
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')
ax.set_title(f'Point Reflection Across Plane: {a}x + {b}y + {c}z + {d} = 0')
ax.legend()
ax.set_box_aspect([1, 1, 1])
plt.show() 