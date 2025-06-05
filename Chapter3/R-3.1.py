# 画出函数8n、4nlog(n)、2n^2、n^3和2^n的图形，其中x轴和y轴均为对数刻度。也就是说，若函数f(n)的值为y，则x坐标为1og(n)，y坐标为1og(y)，
# 其中，(x，y)为一个点。
import numpy as np
import matplotlib.pyplot as plt

# 设置中文字体支持
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 创建n值范围（从1到50，取100个点）
n = np.linspace(1, 50, 100)

# 计算各个函数的值
f1 = 8 * n  # 8n
f2 = 4 * n * np.log(n)  # 4nlog(n) - 使用自然对数
f3 = 2 * n ** 2  # 2n^2
f4 = n ** 3  # n^3
f5 = 2 ** n  # 2^n

# 创建双对数坐标系图形
plt.figure(figsize=(10, 8))

# 绘制各函数曲线
plt.loglog(n, f1, label='8n', linewidth=2, color='blue')
plt.loglog(n, f2, label='4nlog(n)', linewidth=2, color='green')
plt.loglog(n, f3, label='2n^2', linewidth=2, color='red')
plt.loglog(n, f4, label='n^3', linewidth=2, color='purple')
plt.loglog(n, f5, label='2^n', linewidth=2, color='orange')

# 添加图例和标签
plt.legend(fontsize=12)
plt.title('函数增长比较 (双对数坐标系)', fontsize=16)
plt.xlabel('log(n)', fontsize=14)
plt.ylabel('log(y)', fontsize=14)
plt.grid(True, which="both", linestyle='--', alpha=0.6)

# 调整坐标轴范围以便更好显示各曲线
plt.xlim(1, 50)
plt.ylim(1, 1e15)

# 显示图形
plt.tight_layout()
plt.show()
