# Write a program that displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes.

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1.0,4.0,0.0001)

f = x
g = x**2
h = x**3

plt.plot(x,f,"g.")                # f line in green
plt.plot(x,g,"b.")                # g line in blue
plt.plot(x,h,"r.")                # h line in red
plt.title("f, g and h lines")
plt.xlabel("x")
plt.ylabel("y")

plt.show()






