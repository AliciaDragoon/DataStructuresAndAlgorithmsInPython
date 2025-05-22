# 演示如何使用Python列表解析语法来产生列表[0,2,6,12,20,30,42,56,72,90]。
sequence = [n * n - n for n in range(1, 11)]  # 使用n² - n公式
print(sequence)  # 输出: [0, 2, 6, 12, 20, 30, 42, 56, 72, 90]
