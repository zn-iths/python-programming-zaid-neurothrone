import matplotlib.pyplot as plt

squares = [square ** 2 for square in range(-10, 10 + 1)]

plt.plot(squares)
plt.show()
