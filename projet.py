#Coucou Julie!
#ici on peut mettre notre code
#je copie le code de l'énoncé

import numpy as np 
import matplotlib.pyplot as plt
#%matplotlib inline 
plt.rcParams["figure.figsize"] = (3,3)
from mpl_toolkits.mplot3d import Axes3D
from scipy.integrate import solve_ivp

###                 Tracé d'une sigmoïde
def sigmoid(x):
    a = 2.0   # la pente au niveau du seuil est a/4
    theta = 5.0  # seuil
    return 1/(1+np.exp(-a*(x-theta)))-1/(1+np.exp(a*theta))

x = np.linspace(-10,10)
plt.figure()
plt.plot(x,sigmoid(x))
plt.grid(True)
plt.xlabel('$x$')
plt.title("Fonction d'activation")
plt.show()



###                 Matrice d'interconnection
W = np.array([[5.0, -4.0], [8.0, -1.0]])
print(W)