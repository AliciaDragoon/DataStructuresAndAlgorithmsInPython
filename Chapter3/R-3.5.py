# 试解释：在双对数坐标轴中，斜率为c的函数n^c，为何其图形为一条直线？
# f(n) = n^c => log(f(n)) = log(n^c) = c·log(n)
import numpy as np
import matplotlib.pyplot as plt

# 设置中文字体支持
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

n = np.logspace(0, 2, 100)  # n从1到100（对数均匀分布）

# 创建图形
plt.figure(figsize=(10, 8))

# 绘制标准坐标系
plt.subplot(2, 1, 1)
for c in [0.5, 1, 2]:
    plt.plot(n, n ** c, label=f'$n^{{{c}}}$')
plt.title('标准坐标系')
plt.xlabel('n')
plt.ylabel('f(n)')
plt.grid(True)
plt.legend()
plt.yscale('linear')

# 绘制双对数坐标系
plt.subplot(2, 1, 2)
for c in [0.5, 1, 2]:
    plt.plot(np.log10(n), np.log10(n ** c), label=f'斜率={c}')
plt.title('双对数坐标系')
plt.xlabel('$\log_{10}(n)$')
plt.ylabel('$\log_{10}(f(n))$')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
