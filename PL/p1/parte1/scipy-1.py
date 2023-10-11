import scipy
import matplotlib.pyplot as plt
from scipy.stats import norm
import numpy as np


def signaltonoise(a, axis=0, ddof=0):
    a = np.asanyarray(a)
    m = a.mean(axis)
    sd = a.std(axis=axis, ddof=ddof)
    return np.where(sd == 0, 0, m / sd)


face = scipy.datasets.ascent().astype(float)  # INSTALAR POOCH!!! → se utiliza datasets para eliminar warning de ejecución
faceruido16 = face + norm.rvs(loc=0, scale=16, size=face.shape)
faceruido64 = face + norm.rvs(loc=0, scale=64, size=face.shape)
print(signaltonoise(face, axis=None))

plt.gray()  # se muestran las imágenes en escala de grises

# foto original, sin ruido
plt.subplot(131, aspect='equal')
plt.imshow(face)

# foto con ruido (varianza 16)
plt.subplot(132, aspect='equal')
plt.imshow(faceruido16)

# foto con ruido (varianza 64)
plt.subplot(133, aspect='equal')
plt.imshow(faceruido64)

plt.show()
