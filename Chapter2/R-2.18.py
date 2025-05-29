# 给出一个来自Python代码的简短片段，使用2.4.2节的Progression类，找到那个以2开始且以2作为前两个值的斐波那契数列的第8个值。
from ch02.progressions import FibonacciProgression

fib = FibonacciProgression(2, 2)
for _ in range(7):  # 跳过前7个值（索引0-6）
    next(fib)
print(next(fib))  # 打印第8个值（索引7）
