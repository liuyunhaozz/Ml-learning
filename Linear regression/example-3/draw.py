import numpy as np
import matplotlib.pyplot as plt

x = [51, 100, 510, 1000, 5100, 10000]
y = [0.295, 0.379, 0.634, 1.039, 2.442, 2.573]

plt.scatter(x, y, color="red")
plt.title("稳压二极管输出电压与负载电阻的关系")
plt.xlabel("负载电阻值 R (Ω)")
plt.ylabel("输出电压 Vdz (V)")

linear_model = np.polyfit(x, y, 3)
linear_model_fn = np.poly1d(linear_model)
x_s = np.linspace(51, 10500, 100000)

# 防止中文乱码
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

plt.plot(x_s, linear_model_fn(x_s), color="green")

plt.show()
