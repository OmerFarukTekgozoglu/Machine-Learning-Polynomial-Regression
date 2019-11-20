# -*- coding: utf-8 -*-

#Polynominal Regression Modeli 

import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

from sklearn.model_selection import train_test_split

dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values

plt.plot(X, y, 'ro')
plt.axis([0, 11, 0, 1100000])
plt.title("Veri Setinin Dağılımı")
plt.xlabel("Mesleki Kademe/Derece")
plt.ylabel("Yıllık Maaş")
plt.show()

#Veri seti eğitim ve test seti bölümlemesi için küçük olduğu için tüm veri setini eğitim için kullanacağız.

#karşılaştırma yapmak için bir linear reg. modeli bir de polynominal reg. modeli oluşturalım.

#Linear Reg.
from sklearn.linear_model import LinearRegression
linear_reg = LinearRegression()
linear_reg.fit(X,y)

#Polynominal Reg.
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree = 4)
X_poly = poly_reg.fit_transform(X)
linear_reg_poly = LinearRegression()
linear_reg_poly.fit(X_poly, y)

#Linear Reg. sonuçlarının görselleştirilmesi
plt.scatter(X, y, color = 'red') #X ve Y eksenlerinin sınırlarıdır.
plt.plot(X, linear_reg.predict(X), color = 'blue') #X ve Y eksenlerine ne konulacağıdır.
plt.title("Lineer Regresyon Modeli")
plt.xlabel("Mesleki Kademe/Derece")
plt.ylabel("Maaş")
plt.show()
 
"""
Buraya DİKKAT !
"""
#Polynominal Reg. sonuçlarının görselleştirilmesi
X_grid = np.arange(min(X), max(X), 0.1)
X_grid = X_grid.reshape(len(X_grid), 1)
plt.scatter(X, y, color = 'red') 
plt.plot(X_grid, linear_reg_poly.predict(poly_reg.fit_transform(X_grid)), color = 'blue') 
plt.title("Polynomial Regresyon Modeli")
plt.xlabel("Mesleki Kademe/Derece")
plt.ylabel("Maaş")
plt.show()

print("Lineer regresyon modeli doğruluk skoru: %" + str(linear_reg.score(X,y)*100))
print("Polynomial regresyon modeli doğruluk skoru: %" + str(linear_reg_poly.score(poly_reg.fit_transform(X), y)*100))

#Linear Reg. Modeline göre yeni bir verinin tahmininin yapılması
linear_reg.predict(4.2)
#Poly Reg. Modeline göre yeni bir verinin tahmininin yapılması
linear_reg_poly.predict(poly_reg.fit_transform(4.2))