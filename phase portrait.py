import numpy as np
import matplotlib.pyplot as plt

# derivada no espaço de estados
def dF(x1, x2):
    return x2, 2*x1 - x2

# plano x1-x2
X1, X2 = np.meshgrid(np.linspace(-6, 6, 30), np.linspace(-6, 6, 30))

# vetores no plano
dx1, dx2 = dF(X1, X2)

# gráfico em si
plt.rcParams["figure.autolayout"] = True

teal = "#008080"
plt.streamplot(X1, X2, dx1, dx2, color=teal, linewidth=1.1, density=1.5)

#plt.grid("on")
plt.axis("off")
plt.show()
