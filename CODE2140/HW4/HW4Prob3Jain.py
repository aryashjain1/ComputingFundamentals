import numpy as np
import matplotlib.pyplot as plt

t = np.arange(-4 * np.pi, 4 * np.pi, 0.01)
x = np.cos(t) + 2 * np.cos(t / 4)
y = np.sin(t) - 2 * np.sin(t / 4)

plt.figure()
plt.plot(x, y, 'r--')
plt.grid()
plt.title('Plotting parametric functions')
plt.xlabel('x')
plt.ylabel('y')
plt.text(4, 2,'x = cos(t) - 2cos(t/4)')
plt.text(4, 1, 'y = sin(t) - 2sin(t/4)')
plt.show()