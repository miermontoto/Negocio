import numpy
import matplotlib.pyplot as plt
from scipy.spatial.distance import minkowski


def f(x, y, p):
    return minkowski([x, y], [0.0, 0.0], p) <= 1.0


def ball(p):
    return numpy.vectorize(f)(X, Y, p)


Square = numpy.meshgrid(numpy.linspace(-1.1, 1.1, 512), numpy.linspace(-1.1, 1.1, 512), indexing='ij')
X = Square[0]
Y = Square[1]
plt.imshow(ball(3))
plt.axis('off')
plt.show()
