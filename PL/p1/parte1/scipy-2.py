import numpy
import matplotlib.pyplot as plt
from scipy.stats import uniform

x = numpy.linspace(1, 4, 1000)

# Función de densidad
plt.subplot(131)
plt.plot(x, uniform.pdf(x, 2, 1))

# Función de distribución
plt.subplot(132)
plt.plot(x, uniform.cdf(x, 2, 1))

# Generador aleatorio
plt.subplot(133)
plt.plot(uniform.rvs(2, 1, size=1000))

plt.show()
