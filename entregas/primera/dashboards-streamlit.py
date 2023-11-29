# Ejemplo de dashboard con Streamlit
# Juan Francisco Mier Montoto, UO283319
# Es indudablemente peor que el de teoría, está sorprendentemente bien implementado

# Importar las bibliotecas necesarias
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.datasets import load_wine
import matplotlib.pyplot as plt

# Cargar el dataset de vinos
wine = load_wine()
wine_df = pd.DataFrame(data=np.c_[wine['data'], wine['target']],
                       columns=wine['feature_names'] + ['target'])

# Convertir el target a int para evitar problemas en gráficos
wine_df['target'] = wine_df['target'].astype(int)

# Inicializar la aplicación Streamlit
st.title('Visualización de Datos del Dataset de Vinos (UO283319)')

# Barra lateral para selección de características
feature = st.sidebar.selectbox('Seleccione una característica para mostrar', wine_df.columns[:-1])

# Crear un histograma para la característica seleccionada
st.write(f'Histograma para {feature}')
fig, ax = plt.subplots()
ax.hist(wine_df[feature], bins=20, alpha=0.7, color='blue')
ax.set_title(f'Distribución de {feature}')
ax.set_xlabel(feature)
ax.set_ylabel('Cantidad')
st.pyplot(fig)

# Mostrar tabla con las primeras 10 filas del DataFrame
st.write('Primeras 10 filas del Dataset:')
st.write(wine_df.head(10))

# Ejecutar la aplicación
# No es necesario agregar código aquí, Streamlit ejecuta la aplicación automáticamente
