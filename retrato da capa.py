import numpy as np
import matplotlib
import matplotlib.pyplot as plt

# derivada no espaço de estados
def dF(x1, x2):
    return x2, -x1 - x2 

# plano x1-x2
X1, X2 = np.meshgrid(np.linspace(-3, 3, 1000), np.linspace(-3, 3, 1000))

# vetores no plano
dx1, dx2 = dF(X1, X2)

# gráfico em si
plt.rcParams["figure.autolayout"] = True
# figure()

teal = "#008080"
plt.streamplot(X1, X2, dx1, dx2, color=teal, linewidth=1, density=2)
ax = plt.gca()

for art in ax.get_children():
    if not isinstance(art, matplotlib.patches.FancyArrowPatch):
        continue
    art.remove()        # Method 1
    # art.set_alpha(0)  # Method 2

plt.axis("off")
# plt.show()
plt.savefig('Aulas/TnlC/Exercícios/Figuras/retrato da capa.pdf') # salva já na pasta das figuras