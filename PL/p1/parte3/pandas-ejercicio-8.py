import pandas as pd
import numpy as np
from sklearn.model_selection import cross_val_score, cross_val_predict
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error


df = pd.read_excel("Churn_Modelling_NANs.xlsx", na_values='NA')

# 1. Elimina las filas con valores perdidos
df = df.dropna()

# 2. Selecciona un dataframe 'X' con las columnas 'CreditScore','Age','Tenure','Balance','NumOfProducts','HasCrCard','IsActiveMember'
X = df[['CreditScore', 'Age', 'Tenure', 'Balance', 'NumOfProducts', 'HasCrCard', 'IsActiveMember']]

# 3. Selecciona un dataframe 'y' con la columna 'EstimatedSalary'
y = df[['EstimatedSalary']]

# 4. Haz tres modelos (LinearRegression, SVR, RandomForestRegressor) de Y frente a X
# 	 y compara el error cuadrático medio de los tres con validación cruzada (10 fold)
cv = 10

# LinearRegression
lr = LinearRegression()
lr_scores = cross_val_score(lr, X, y, cv=cv, scoring="neg_mean_squared_error")
lr_rmse_scores = np.sqrt(-lr_scores)
print("LinearRegression")
print("Scores:", lr_rmse_scores)
print("Mean:", lr_rmse_scores.mean())
print("Standard deviation:", lr_rmse_scores.std())

# SVR
svr = SVR(kernel="linear")
svr_scores = cross_val_score(svr, X, y, cv=cv, scoring="neg_mean_squared_error")
svr_rmse_scores = np.sqrt(-svr_scores)
print("SVR")
print("Scores:", svr_rmse_scores)
print("Mean:", svr_rmse_scores.mean())
print("Standard deviation:", svr_rmse_scores.std())

# RandomForestRegressor
rfr = RandomForestRegressor(n_estimators=10)
rfr_scores = cross_val_score(rfr, X, y, cv=cv, scoring="neg_mean_squared_error")
rfr_rmse_scores = np.sqrt(-rfr_scores)
print("RandomForestRegressor")
print("Scores:", rfr_rmse_scores)
print("Mean:", rfr_rmse_scores.mean())
print("Standard deviation:", rfr_rmse_scores.std())

# 5. Selecciona un dataframe 'XC' con las columnas CreditScore, Age, Tenure, Balance,
# 	 NumOfProducts, HasCrCard, IsActiveMember, EstimatedSalary y un dataframe 'C' con
# 	 la columna Exited. Haz tres clasificaciones diferentes de C frente a XC y compara
# 	 sus porcentajes de aciertos con validación cruzada (10 fold)
XC = df[['CreditScore', 'Age', 'Tenure', 'Balance', 'NumOfProducts', 'HasCrCard', 'IsActiveMember', 'EstimatedSalary']]
C = df[['Exited']]

# LinearRegression
lr = LinearRegression()
lr_scores = cross_val_score(lr, XC, C, cv=cv, scoring="accuracy")
print("LinearRegression")
print("Scores:", lr_scores)
print("Mean:", lr_scores.mean())
print("Standard deviation:", lr_scores.std())

# SVR
svr = SVR(kernel="linear")
svr_scores = cross_val_score(svr, XC, C, cv=cv, scoring="accuracy")
print("SVR")
print("Scores:", svr_scores)
print("Mean:", svr_scores.mean())

# RandomForestRegressor
rfr = RandomForestRegressor(n_estimators=10)
rfr_scores = cross_val_score(rfr, XC, C, cv=cv, scoring="accuracy")
print("RandomForestRegressor")
print("Scores:", rfr_scores)
print("Mean:", rfr_scores.mean())
print("Standard deviation:", rfr_scores.std())


