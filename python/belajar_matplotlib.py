import matplotlib.pyplot as plt

x = [1, 5, 3, 4, 5]
y = [2, 4, 5, 8, 10]

plt.plot(x, y, marker="o")
plt.title("Grafik Pertama")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.show()