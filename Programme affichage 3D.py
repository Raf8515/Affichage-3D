import matplotlib.pyplot as plt  
from mpl_toolkits.mplot3d.art3d import Poly3DCollection 
import numpy as np 
from matplotlib.widgets import Button  
# Définition des sommets du cube
vertices = np.array([[0, 0, 0],
                     [1, 0, 0],
                     [1, 1, 0],
                     [0, 1, 0],
                     [0, 0, 1],
                     [1, 0, 1],
                     [1, 1, 1],
                     [0, 1, 1]])

# Définition des faces du cube en utilisant les sommets
faces = [[vertices[j] for j in [0, 1, 2, 3]],  # Face inférieure
         [vertices[j] for j in [4, 5, 6, 7]],  # Face supérieure
         [vertices[j] for j in [0, 1, 5, 4]],  # Face avant
         [vertices[j] for j in [2, 3, 7, 6]],  # Face arrière
         [vertices[j] for j in [1, 2, 6, 5]],  # Face droite
         [vertices[j] for j in [4, 7, 3, 0]]]  # Face gauche

# Création d'une figure et d'un axe 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Ajout des faces du cube à l'axe 3D avec des propriétés de couleur et de transparence
ax.add_collection3d(Poly3DCollection(faces, 
                                     facecolors='cyan', linewidths=1, edgecolors='r', alpha=.25))

# Définition des limites des axes
ax.set_xlim([0, 1])
ax.set_ylim([0, 1])
ax.set_zlim([0, 1])

# Initialisation des variables pour le contrôle de la grille et des axes
grid_on = True
axes_on = True

# Création des axes pour les boutons
button_ax_grid = plt.axes([0.7, 0.05, 0.1, 0.075])
button_ax_axes = plt.axes([0.81, 0.15, 0.1, 0.075])

# Création des boutons
button_grid = Button(button_ax_grid, 'Grille ON/OFF')
button_axes = Button(button_ax_axes, 'Axes ON/OFF')

# Fonction pour basculer l'affichage de la grille
def toggle_grid(event):
    global grid_on
    grid_on = not grid_on
    ax.grid(grid_on)  
    fig.canvas.draw_idle()  

# Fonction pour basculer l'affichage des axes
def toggle_axes(event):
    global axes_on
    axes_on = not axes_on
    ax.set_axis_off() if not axes_on else ax.set_axis_on()  
    fig.canvas.draw_idle() 

# Assignation des fonctions de bascule aux boutons
button_grid.on_clicked(toggle_grid)
button_axes.on_clicked(toggle_axes)

# Affichage de la figure
plt.show()
