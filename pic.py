import matplotlib.pyplot as plt
import numpy as np
import scipy


x1 = np.arange(0,360,5)
y1 = np.sin(x1 * np.pi / 180.0)

x2 = x1
y2 = np.cos(x2 * np.pi / 180.0)

x3 = x1
y3 = np.tan(x3 * np.pi / 180.0)

plt.plot(x1,y1,lw=3)
plt.plot(x2,y2,"ro")
plt.plot(x3,y3,"y--",lw=5)

plt.ylabel("y_label")
plt.xlabel("x_label")
plt.title("Title")

plt.xlim(-30,390)
plt.ylim(-5,5)

plt.show()
