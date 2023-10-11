import numpy
import matplotlib.pyplot as plt
from scipy.spatial.distance import minkowski, euclidean, chebyshev, cityblock

Square = numpy.meshgrid(numpy.linspace(-1.1, 1.1, 512), numpy.linspace(-1.1, 1.1, 512), indexing='ij')
X = Square[0]
Y = Square[1]
f = lambda x, y, p: minkowski([x, y], [0.0, 0.0], p) <= 1.0
Ball = lambda p: numpy.vectorize(f)(X, Y, p)

plt.subplot(231, aspect='equal')
plt.imshow(Ball(1))
plt.axis('off')

plt.subplot(232, aspect='equal')
plt.imshow(Ball(2))
plt.axis('off')

plt.subplot(233, aspect='equal')
plt.imshow(Ball(4))
plt.axis('off')

# distancia euclídea
f = lambda x, y: euclidean([x, y], [0.0, 0.0]) <= 1.0
Ball = lambda: numpy.vectorize(f)(X, Y)

plt.subplot(234, aspect='equal')
plt.imshow(Ball())
plt.axis('off')

f = lambda x, y: chebyshev([x, y], [0.0, 0.0]) <= 1.0
Ball = lambda: numpy.vectorize(f)(X, Y)
plt.subplot(235, aspect='equal')
plt.imshow(Ball())
plt.axis('off')

f = lambda x, y: cityblock([x, y], [0.0, 0.0]) <= 1.0
Ball = lambda: numpy.vectorize(f)(X, Y)
plt.subplot(236, aspect='equal')
plt.imshow(Ball())
plt.axis('off')

plt.show()
