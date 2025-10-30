import numpy as np
import matplotlib.pyplot as plt
import os
from IPython.display import display, Math, HTML
from matplotlib.animation import FuncAnimation

# a) fig 1
# vreau sa folosesc formulele de baza, nu cele echivalente in care nu ma ating de timp discret
# var1 - timpul e discret, iar pentru a ilustra pe cercul unitate punctele consecutive stabilesc o frecv discreta fixata M
frecv = 20
rata_esantionare = 1000
durata = 0.2
T = 1/rata_esantionare # perioada de esantionare
N = durata*rata_esantionare # nr_esantioane din exercitiile din lab2
n = np.arange(0, int(N)) # n = 0, 1, ... N-1

tn = n*T # momentele discrete de timp
x_n = 0.7*np.sin(2*np.pi*frecv*tn+np.pi/3)

m = np.arange(0, int(N)) # m = 0, 1, ... N-1
omega0 = (2*np.pi)/(N*T) # frecv de infasurare
omegam = m*omega0
#print(omega0, omegam, sep="\n")
M = 1 # frecv discreta fixata pentru a conecta puncte discrete consecutive intre ele din cauza faptului ca X_discret are dimensiunea NxN
sm_n = np.exp(-1j*omegam[M]*tn)

# ceva f f important, practic in laborator scrie o formula foarte simpla in care nici nu e specificat omega tocmai pt ca omegam[1] == omega0

#print(sm_n)
X_discret = x_n*sm_n

# pt animatii, ele sunt numai in fisierul python, nu merg in jupyternotebook
plt.ion()
fig, ax = plt.subplots()

for i in range(1, len(X_discret)):
    ax.set_xlim(X_discret.real.min() * 1.1, X_discret.real.max() * 1.1)
    ax.set_ylim(X_discret.imag.min() * 1.1, X_discret.imag.max() * 1.1)
    ax.set_xlabel("real")
    ax.set_ylabel("imaginar")
    ax.grid(True)
    ax.set_title("X pe cercul unitate")
    ax.scatter(X_discret.real[i], X_discret.imag[i], c=np.abs(X_discret[i]))
    plt.draw()
    plt.pause(0.05)
plt.ioff()
plt.show()