# 算法A和B执行的操作个数分别为40n^2和2n^3。确定n₀，满足：当n≥n₀时，A比B更优。
import numpy as np
import matplotlib.pyplot as plt

# 设置中文字体支持
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

n = np.arange(1, 50)
A = 40 * n ** 2
B = 2 * n ** 3

plt.figure(figsize=(10, 6))
plt.plot(n, A, 'b-', label='算法A: $40n^2$')
plt.plot(n, B, 'r-', label='算法B: $2n^3$')
plt.axvline(x=21, color='gray', linestyle='--', label='临界点 n=21')

# 填充A优于B的区域
plt.fill_between(n, A, B, where=(n >= 21), color='green', alpha=0.3)

plt.title('算法A与算法B性能比较')
plt.xlabel('问题规模 n')
plt.ylabel('操作次数')
plt.legend()
plt.grid(True)
plt.yscale('log')  # y轴对数刻度便于观察
plt.show()
