import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.linear_model import Perceptron

sheet = pd.read_excel('example2.xlsx', engine='openpyxl')


hmix = sheet['Hmix'].to_numpy()
smix = sheet['Smix'].to_numpy()

x = np.dstack((hmix, smix))[0]

y = sheet['Phase'].to_numpy()

length = len(hmix)
positive_x1 = [x[i,0] for i in range(length) if y[i] == 1]
positive_x2 = [x[i,1] for i in range(length) if y[i] == 1]
negative_x1 = [x[i,0] for i in range(length) if y[i] == 0]
negative_x2 = [x[i,1] for i in range(length) if y[i] == 0]

clf = Perceptron(fit_intercept=False,max_iter=300,shuffle=False)
#使用训练数据进行训练
clf.fit(x, y)
#得到训练结果，权重矩阵
print(clf.coef_)
#输出为：[[-0.38478876,4.41537463]]
 
#超平面的截距，此处输出为：[0.]
print(clf.intercept_)

#画出正例和反例的散点图
plt.scatter(positive_x1,positive_x2,c='red')
plt.scatter(negative_x1,negative_x2,c='blue')
#画出超平面（在本例中即是一条直线）
line_x = np.arange(-40,10)
line_y = line_x * (-clf.coef_[0][0] / clf.coef_[0][1]) - clf.intercept_
plt.plot(line_x,line_y)
plt.show()