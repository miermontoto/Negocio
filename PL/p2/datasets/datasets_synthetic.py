from sklearn.datasets import make_classification
import pandas as pd


def gen():
	return make_classification(n_samples=1000, n_features=10, n_informative=3, n_redundant=0, n_repeated=0, n_classes=2, random_state=0, shuffle=False)
