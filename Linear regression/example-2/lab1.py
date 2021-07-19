# 注：这里当 x >= 0.1 时，LASSO 回归后的系数为 0，回归分析失效
import pandas as pd
import numpy as np
from sklearn.linear_model import Lasso
from sklearn.linear_model import LinearRegression as LR
import matplotlib.pyplot as plt
sheet = pd.read_excel('example1.xlsx', engine = 'openpyxl')
sheet
X=sheet.iloc[:,:-1]
Y=sheet.iloc[:,1:]
Y=np.log(Y)
X=1000/(X+273.15)
lasso1 = Lasso(alpha=0.1)
lasso1.fit(X, Y)
# lasso2 = Lasso(alpha=1)
# lasso2.fit(X, y)
# lasso3 = Lasso(alpha=10)
# lasso3.fit(X, y)
pre_y = lasso1.predict(X)
plt.figure()
# plt.xticks(np.arange(2.8, 3.4, 0.1))
# plt.yticks(np.arange(1.4, 2, 0.1))
plt.plot(X,pre_y,label='Group I samples', linestyle='--',color='r')
# plt.plot(pre_x,pre_y_2,label='Group II samples', linestyle=':')
# plt.plot(pre_x,pre_y_3,label='Group III samples', linestyle=':',color='b')
plt.scatter(X, Y,label='samples')
plt.legend()
plt.show()