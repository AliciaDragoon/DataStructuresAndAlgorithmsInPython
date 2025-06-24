# 对3.3.3节的三个算法prefix_average1、prefix_average2和prefix_average3执行实验分析。将它们的运行时间形象化为一个输入大小的函数，
# 并以双对数图的形式表示。
import timeit
import random
import matplotlib.pyplot as plt
import numpy as np


def prefix_average1(S):
    n = len(S)
    A = [0] * n
    for j in range(n):
        total = 0
        for i in range(j + 1):
            total += S[i]
        A[j] = total / (j + 1)
    return A


def prefix_average2(S):
    n = len(S)
    A = [0] * n
    for j in range(n):
        A[j] = sum(S[0:j + 1]) / (j + 1)
    return A


def prefix_average3(S):
    n = len(S)
    A = [0] * n
    total = 0
    for j in range(n):
        total += S[j]
        A[j] = total / (j + 1)
    return A


# 实验参数设置
n_values = [100, 200, 500, 1000, 2000, 5000, 10000]  # 输入大小
repeats = 10  # 每个数据点重复次数
results = {1: [], 2: [], 3: []}  # 存储时间结果

# 执行时间测量
random.seed(42)  # 固定随机种子
for n in n_values:
    S = [random.random() for _ in range(n)]  # 生成随机列表

    # 测量每个算法的执行时间
    for algo in [1, 2, 3]:
        total_time = 0
        for _ in range(repeats):
            timer = timeit.Timer(f"prefix_average{algo}(S)", globals=globals())
            total_time += timer.timeit(number=1)
        avg_time = total_time / repeats
        results[algo].append(avg_time)

# 绘制双对数图
plt.figure(figsize=(10, 6))
markers = ['o', 's', '^']
for algo in [1, 2, 3]:
    plt.loglog(n_values, results[algo],
               marker=markers[algo - 1],
               label=f'prefix_average{algo}')

# 添加理论参考线
x_ref = np.array(n_values)
plt.loglog(x_ref, 1e-7 * x_ref, '--', color='gray', label='O(n)')
plt.loglog(x_ref, 1e-7 * x_ref ** 2, ':', color='gray', label='O(n²)')

plt.xlabel('Input Size (n)', fontsize=12)
plt.ylabel('Execution Time (seconds)', fontsize=12)
plt.title('Prefix Averages Algorithm Comparison', fontsize=14)
plt.legend()
plt.grid(True, which="both", ls="-", alpha=0.3)
plt.tight_layout()
plt.savefig('prefix_averages_comparison.png', dpi=300)
plt.show()
