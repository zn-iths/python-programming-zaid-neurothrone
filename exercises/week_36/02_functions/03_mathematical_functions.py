import matplotlib.pyplot as plt
import numpy as np

numbers = np.linspace(-10, 10)

f = lambda x: x ** 2 - 3
g = lambda x: 4 * x - 7

x_plot = f(numbers)
y_plot = g(numbers)

plt.plot(x_plot)
plt.plot(y_plot)
plt.show()



