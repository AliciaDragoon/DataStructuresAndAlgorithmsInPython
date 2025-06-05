# 算法A和B执行的操作个数分别为8nlog(n)和2n^2。确定n₀，满足：当n≥n₀时，A比B更优。
import numpy as np
import matplotlib.pyplot as plt

# 设置中文字体支持
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

n = np.arange(1, 50, 1)
# 计算操作次数
A = 8 * n * np.log2(n)  # log₂(n)
B = 2 * n ** 2

plt.figure(figsize=(10, 6))
plt.plot(n, A, 'b-', label='A: $8n\log_2{n}$')
plt.plot(n, B, 'r-', label='B: $2n^2$')
plt.axvline(x=17, color='gray', linestyle='--')
plt.annotate('$n_0=17$', (17, 0), (20, 50), arrowprops=dict(arrowstyle='->'))
plt.fill_between(n, A, B, where=(n >= 17), color='green', alpha=0.3)

plt.legend()
plt.xlabel('$n$')
plt.ylabel('操作次数')
plt.title('算法 A 与 B 的性能比较')
plt.grid(True)
plt.show()
