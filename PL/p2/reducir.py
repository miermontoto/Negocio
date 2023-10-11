import datasets.datasets_synthetic
import pandas as pd
import utils

# Carga inicial de datasets
iris = pd.read_csv('Practica 2/datasets/datasets-uci-iris.csv', sep=',', decimal='.', header=None, names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'target'])
letter = pd.read_csv('Practica 2/datasets/datasets-uci-letter.csv', sep=',', decimal='.')
synthetic = datasets.datasets_synthetic.gen()

iris_x, iris_y = utils.slice(iris)
letter_x, letter_y = utils.slice(letter)

datasets_x = [iris_x, letter_x]
datasets_y = [iris_y, letter_y]

# Parte 1. Eliminación de variables con poca varianza
reduced_by_variance = [utils.reduce_by_var(dataset, 0.1) for dataset in datasets_x]

# Parte 2. Eliminación de variables basada en estadísticos univariantes
reduced_by_univariate = [utils.reduce_with_univariate(datasets_x[i], datasets_y[i], 2) for i in range(len(datasets_x))]

# Parte 3. Eliminación recursiva de variables

utils.print_shapes(datasets_x, "Original")
utils.print_shapes(reduced_by_variance, "Reduced by variance")
utils.print_shapes(reduced_by_univariate, "Reduced by univariate statisticals")
