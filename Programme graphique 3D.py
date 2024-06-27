from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.tri import Triangulation
from matplotlib.widgets import Button

fig = plt.figure(figsize=(14, 6))

ax1 = fig.add_subplot(121, projection='3d')
z = np.linspace(0, 1, 100)
x = z * np.sin(25 * z)
y = z * np.cos(25 * z)
c = x + y
sc1 = ax1.scatter(x, y, z, c=c)
ax1.set_title('3D Scatter plot')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_zlabel('z')

ax2 = fig.add_subplot(122, projection='3d')
def f(x, y):
    return np.sin(np.sqrt(x ** 2 + y ** 2))

x = np.linspace(-6, 6, 30)
y = np.linspace(-6, 6, 30)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

tri = Triangulation(X.ravel(), Y.ravel())
surf = ax2.plot_trisurf(tri, Z.ravel(), cmap='cool', edgecolor='none', alpha=0.8)
ax2.set_title('Surface Triangulation Plot of f(x, y) = sin(sqrt(x^2 + y^2))', fontsize=14)
ax2.set_xlabel('x', fontsize=12)
ax2.set_ylabel('y', fontsize=12)
ax2.set_zlabel('z', fontsize=12)

def toggle_grid(event):
    ax1.grid(not ax1._axis3don)
    ax2.grid(not ax2._axis3don)
    plt.draw()

def toggle_axes(event):
    ax1._axis3don = not ax1._axis3don
    ax2._axis3don = not ax2._axis3don
    ax1.axis(ax1._axis3don)
    ax2.axis(ax2._axis3don)
    plt.draw()

ax_toggle_grid = plt.axes([0.35, 0.02, 0.1, 0.075])
btn_toggle_grid = Button(ax_toggle_grid, 'Grille ON/OFF')

ax_toggle_axes = plt.axes([0.55, 0.02, 0.1, 0.075])
btn_toggle_axes = Button(ax_toggle_axes, 'Axes ON/OFF')

btn_toggle_grid.on_clicked(toggle_grid)
btn_toggle_axes.on_clicked(toggle_axes)

plt.show()

