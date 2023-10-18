import numpy as np
import pandas as pd
from sklearn.feature_selection import VarianceThreshold, SelectKBest, chi2, RFECV
from sklearn.svm import SVC


def slice(dataset) -> [pd.DataFrame, pd.DataFrame]:
	"""
	:param dataset: dataset
	:return: dataset without the target column and the target column
	"""
	return dataset.iloc[:, 0:-1], dataset.iloc[:, -1]


def mdav(dataset) -> float:
	"""
	:param dataset: dataset
	:return: the variance of the most dispersed attribute
	"""
	return np.var(dataset, axis=0).max()


def reduce_by_var(dataset, base) -> pd.DataFrame:
	"""
	:param dataset: dataset
	:param base: base mutiplier of mdav
	:return: the dataset without attributes higher than `base * mdav(dataset)`
	"""
	return VarianceThreshold(base * mdav(dataset)).fit_transform(dataset)


def reduce_with_univariate(dataset_x, dataset_y, k) -> pd.DataFrame:
	"""
	:param dataset: dataset
	:param k: number of attributes to keep
	:return: the dataset with the `k` most relevant attributes
	"""
	return SelectKBest(chi2, k=k).fit_transform(dataset_x, dataset_y)


def reduce_with_rfe(dataset_x, dataset_y):
	"""
	:param dataset: dataset
	:return: the dataset without attributes that are not relevant
	"""

	return RFECV(SVC(kernel="linear"), step=1, cv=5).fit_transform(dataset_x, dataset_y)
