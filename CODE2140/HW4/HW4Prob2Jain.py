import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-1.5, 1.5, 0.01)

y1 = np.sin(np.exp(2*x))
y2 = np.cos(np.exp(-2*x))

plt.figure()
plt.plot(x, y1, 'r', x, y2, 'b')
plt.grid()
plt.title('Lines on the same graph')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(['y = sin(e^2x)', 'y = cos(e^-2x)'])
plt.show()

plt.figure()
plt.subplot(2, 1, 1)
plt.title('Subplots on the same figure')
plt.plot(x, y1, 'r')
plt.legend(['y = sin(e^2x)'])
plt.grid()
plt.xlabel('x')
plt.ylabel('y')

plt.subplot(2, 1, 2)
plt.plot(x, y2, 'r')
plt.grid()

plt.legend(['y = cos(e^-2x)'])
plt.xlabel('x')
plt.ylabel('y')

plt.show()