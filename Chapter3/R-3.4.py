# 请给出一个函数示例，该函数在双对数坐标轴和标准坐标轴中的图形相同。
import numpy as np
import matplotlib.pyplot as plt

# 设置中文字体支持
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 生成数据
x = np.linspace(1, 100, 100)
y = x

# 线性坐标系下绘制 y = x
plt.figure()
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('线性坐标系下的 y = x')
plt.grid(True)

# 双对数坐标系下绘制 y = x
plt.figure()
plt.loglog(x, y)
plt.xlabel('log(x)')
plt.ylabel('log(y)')
plt.title('双对数坐标系下的 y = x')
plt.grid(True, which='both', linestyle='--')

plt.show()
