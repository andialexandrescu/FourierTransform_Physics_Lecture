# %%
import numpy as np
import matplotlib.pyplot as plt
import os
from IPython.display import display, Math, HTML
from matplotlib.animation import FuncAnimation

# %%
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

# %%
# b)
fig, axes = plt.subplots(2, 3, figsize=(15, 10)) # 2 linii, 3 coloane
selectie_omegam = np.random.choice(omegam, size=6, replace=False)
axes = axes.flatten()
for i, omega in enumerate(selectie_omegam):
    sm_n = np.exp(-1j*omega*tn)
    X_discret = x_n*sm_n

    ax = axes[i]
    for k in range(len(X_discret)-1): # conecteaza punctele prin segmente pe planul complex
        ax.plot([X_discret.real[k], X_discret.real[k+1]], [X_discret.imag[k], X_discret.imag[k+1]], color='blue')
    ax.scatter(X_discret.real, X_discret.imag, c=np.abs(X_discret), cmap='viridis')
    ax.set_xlabel("real")
    ax.set_ylabel("imaginar")
    ax.set_title(f"omega={omega:.2f}")
    ax.grid(True)

plt.tight_layout()
plt.show()
    

# %%
# pt animatii, ele sunt numai in fisierul python, nu merg in jupyternotebook
fig, axes = plt.subplots(2, 3, figsize=(15, 10))
axes = axes.flatten()
X_selectie_omegam = []
for omega in selectie_omegam:
    sm_n = np.exp(-1j*omega*tn)
    X_selectie_omegam.append(x_n*sm_n)

# ideea de baza din spatele animatiilor este ca pentru fiecare subplot din cele 6, sunt doua componente distincte, liniile care conecteaza punctele consecutive si scatter-ul (imprastierea) de puncte
# FuncAnimation urmareste un update per frame al liniilor si scatter-ului
linii = []
scat = []
for ax, omega, X_d in zip(axes, selectie_omegam, X_selectie_omegam):
    ax.set_xlim(X_d.real.min() * 1.1, X_d.real.max() * 1.1)
    ax.set_ylim(X_d.imag.min() * 1.1, X_d.imag.max() * 1.1)
    ax.set_xlabel("real")
    ax.set_ylabel("imaginar")
    ax.set_title(f"omega={omega:.2f}")
    ax.grid(True)
    
    linie, = ax.plot([], [], 'b-')
    scatter = ax.scatter([], [], c=[])
    linii.append(linie)
    scat.append(scatter)

def init():
    for linie, scatter in zip(linii, scat):
        linie.set_data([], [])
        scatter.set_offsets(np.empty((0, 2)))
    return linii + [s for scatter in scat for s in [scatter]]

def update(frame):
    for linie, scatter, X_d in zip(linii, scat, X_selectie_omegam):
        linie.set_data(X_d.real[:frame+1], X_d.imag[:frame+1])
        scatter.set_offsets(np.column_stack((X_d.real[:frame+1], X_d.imag[:frame+1])))
        scatter.set_array(np.abs(X_d[:frame+1]))
    return linii + [s for scatter in scat for s in [scatter]]

ani = FuncAnimation(fig, update, frames=len(tn), init_func=init, blit=True, interval=50, repeat=False)

plt.tight_layout()
plt.show()