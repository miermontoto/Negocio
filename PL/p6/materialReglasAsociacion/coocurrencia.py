# Ejemplo de matriz de coocurrencia
# Transacciones
# 1: A, B
# 2: A, C
# 3: B, C
# 4: A, B, C
# 5: C

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Conjunto de datos
transacciones = [
    ['A', 'B'],
    ['A', 'C'],
    ['B', 'C'],
    ['A', 'B', 'C'],
    ['C']
]

# Convertir a DataFrame con One-Hot Encoding
oht = pd.DataFrame([[int(item in trans) for item in ['A', 'B', 'C']] for trans in transacciones], columns=['A', 'B', 'C'])

# Matriz de Co-ocurrencia
co_ocurrencia = oht.T.dot(oht)

# Cálculo del Lift
lift = pd.DataFrame(index=['A', 'B', 'C'], columns=['A', 'B', 'C'])
for i in ['A', 'B', 'C']:
    for j in ['A', 'B', 'C']:
        lift.loc[i, j] = co_ocurrencia.loc[i, j] / (oht[i].sum() * oht[j].sum())

print(lift)


# Visualización con Heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(lift.astype(float), annot=True, cmap='viridis', cbar=True, linewidths=.5)
plt.title("Matriz de Lift")
plt.show()