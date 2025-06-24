# 执行实验分析：验证Python的sorted方法平均运行时间为O(n log n)这一假设。
import time
import random
import math
import numpy as np
import matplotlib.pyplot as plt

# 实验参数
n_values = [1000, 2000, 5000, 10000, 20000, 50000, 100000, 200000, 500000, 1000000]
num_samples = 5  # 每个n的样本数
num_runs = 3  # 每个样本的运行次数

# 存储结果
results = {}

for n in n_values:
    times = []  # 存储当前n的所有样本时间

    for _ in range(num_samples):
        # 生成随机列表
        arr = [random.randint(-10 ** 6, 10 ** 6) for _ in range(n)]
        run_times = []

        # 多次运行取中位数
        for _ in range(num_runs):
            arr_copy = arr.copy()  # 避免缓存影响
            start = time.perf_counter()
            sorted_arr = sorted(arr_copy)
            end = time.perf_counter()
            run_times.append(end - start)

        median_time = sorted(run_times)[len(run_times) // 2]
        times.append(median_time)

    # 计算平均时间
    avg_time = sum(times) / num_samples
    results[n] = avg_time

# 计算 K(n) = T(n) / (n * log2(n))
k_values = []
for n, t in results.items():
    log2n = math.log(n) / math.log(2)  # log2(n) = ln(n)/ln(2)
    k = t / (n * log2n)
    k_values.append(k)
    print(f"n = {n:7d}, T(n) = {t:.6f}s, K(n) = {k:.10f}")

# 绘制结果
plt.figure(figsize=(12, 6))

# 子图1：实际运行时间与 n log n 的对比
plt.subplot(1, 2, 1)
x_log = [n * math.log(n) for n in n_values]
plt.plot(n_values, list(results.values()), 'o-', label='Actual T(n)')
plt.plot(n_values, x_log, 'r--', label='Reference n log(n) (scaled)')
plt.xlabel('Input Size (n)')
plt.ylabel('Time (s)')
plt.title('Actual Runtime vs. n log(n)')
plt.legend()
plt.grid(True)

# 子图2：K(n) 的收敛情况
plt.subplot(1, 2, 2)
plt.plot(n_values, k_values, 's-', color='green')
plt.xlabel('Input Size (n)')
plt.ylabel('K(n) = T(n) / (n log₂ n)')
plt.title('Convergence of K(n) to a Constant')
plt.grid(True)

plt.tight_layout()
plt.show()
