import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,2*np.pi,1000)
y = np.cos(x)

fig, ax = plt.subplots()
ax.plot(x,y)
ax.set_xlabel('x')
ax.set_ylabel('y')
fig.tight_layout()