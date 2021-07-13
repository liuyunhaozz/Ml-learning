import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

def trans(degree):
    return (degree + 273) / 1000

x = [[1 / trans(25)], [1 / trans(50)], [1 / trans(70)], [1 / trans(80)]]

D_1 = [[4.11], [4.92], [6.10], [6.66]]
D_2 = [[4.27], [4.92], [6.14], [6.62]]
y_1 = np.log(D_1)
y_2 = np.log(D_2)

from sklearn.linear_model import LinearRegression
linreg_1 = LinearRegression()
linreg_2 = LinearRegression()
linreg_3 = LinearRegression()
linreg_1.fit(x, y_1)
linreg_2.fit(x, y_2)
linreg_3.fit(np.vstack((x, x)), np.vstack((y_1, y_2)))

pre_x = [[2.8], [3.4]]
pre_y_1 = linreg_1.predict(pre_x)
pre_y_2 = linreg_2.predict(pre_x)
pre_y_3 = linreg_3.predict(pre_x)
# print(pre_y_1)
# print(pre_y_2)
plt.figure()
plt.xlabel(r"$1/T(10^{-3}K)$")
plt.ylabel(r"$lnD(cm^2/s)$")
plt.xticks(np.arange(2.8, 3.4, 0.1))
plt.yticks(np.arange(1.4, 2, 0.1))
plt.plot(pre_x,pre_y_1,label='Group I samples', linestyle='--',color='r')
plt.plot(pre_x,pre_y_2,label='Group II samples', linestyle=':')

plt.scatter(x,y_1,label='Group I samples')
plt.scatter(x,y_2,label='Group II samples', marker ='^')
plt.plot(pre_x,pre_y_3,label='All samples', linestyle='-', linewidth=0.5, color='b')
plt.legend()
plt.show()