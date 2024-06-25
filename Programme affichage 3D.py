import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np
from matplotlib.widgets import Button

vertices = np.array([[0, 0, 0],
                     [1, 0, 0],
                     [1, 1, 0],
                     [0, 1, 0],
                     [0, 0, 1],
                     [1, 0, 1],
                     [1, 1, 1],
                     [0, 1, 1]])

faces = [[vertices[j] for j in [0, 1, 2, 3]],
         [vertices[j] for j in [4, 5, 6, 7]],
         [vertices[j] for j in [0, 1, 5, 4]],
         [vertices[j] for j in [2, 3, 7, 6]],
         [vertices[j] for j in [1, 2, 6, 5]],
         [vertices[j] for j in [4, 7, 3, 0]]]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.add_collection3d(Poly3DCollection(faces, 
                                     facecolors='cyan', linewidths=1, edgecolors='r', alpha=.25))

ax.set_xlim([0, 1])
ax.set_ylim([0, 1])
ax.set_zlim([0, 1])

grid_on = True
axes_on = True

button_ax_grid = plt.axes([0.7, 0.05, 0.1, 0.075])
button_ax_axes = plt.axes([0.81, 0.15, 0.1, 0.075])

button_grid = Button(button_ax_grid, 'Grille ON/OFF')
button_axes = Button(button_ax_axes, 'Axes ON/OFF')

def toggle_grid(event):
    global grid_on
    grid_on = not grid_on
    ax.grid(grid_on)
    fig.canvas.draw_idle()

def toggle_axes(event):
    global axes_on
    axes_on = not axes_on
    ax.set_axis_off() if not axes_on else ax.set_axis_on()
    fig.canvas.draw_idle()

button_grid.on_clicked(toggle_grid)
button_axes.on_clicked(toggle_axes)

plt.show()
