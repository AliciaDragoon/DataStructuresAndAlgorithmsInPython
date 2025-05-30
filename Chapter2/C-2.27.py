# 在2.3.5节中对于Range r，“k in r”，我们注意到Range类的版本隐式地支持迭代，因为它显式支持__len__和__getitem__。该类也接受对布尔类型的隐式支持。
# 这个测试通过范围基于前向迭代器进行评估，通过实验证明2 in Range(10_000_000)对比9_999_999 in Range(10_000_000)的相对速度。请提供一种__contains__方法
# 更有效的实现，以确定特定的值是否属于给定范围内。所提供方法的运行时间应独立于范围的大小。
import time


class Range:
    """A class that mimic's the built-in range class."""

    def __init__(self, start, stop=None, step=1):
        if step == 0:
            raise ValueError('step cannot be 0')

        if stop is None:
            start, stop = 0, start

        # 存储关键参数用于高效计算
        self._start = start
        self._stop = stop
        self._step = step
        self._length = max(0, (stop - start + step - 1) // step)

    def __len__(self):
        return self._length

    def __getitem__(self, k):
        if k < 0:
            k += len(self)

        if not 0 <= k < self._length:
            raise IndexError('index out of range')

        return self._start + k * self._step

    def __contains__(self, value):
        """高效检查值是否在范围内，时间复杂度 O(1)"""
        # 检查值是否在有效区间内
        if self._step > 0:
            if value < self._start or value >= self._stop:
                return False
        else:  # step < 0
            if value > self._start or value <= self._stop:
                return False

        # 检查值是否在等差数列上
        offset = value - self._start
        # 检查是否能被步长整除
        return offset % self._step == 0


large_range = Range(0, 10_000_000)


def test_contains(value):
    start = time.perf_counter_ns()
    result = value in large_range
    end = time.perf_counter_ns()
    elapsed = (end - start) / 1000  # 转换为微秒
    print(f"{value} in large_range: {result} | 耗时: {elapsed:.3f} μs")


# 测试不同值
test_contains(0)
test_contains(5_000_000)
test_contains(9_999_999)
test_contains(10_000_000)

# 原生方法
# 0 in large_range: True | 耗时: 4.500 μs
# 5000000 in large_range: True | 耗时: 705756.900 μs
# 9999999 in large_range: True | 耗时: 1306312.200 μs
# 10000000 in large_range: False | 耗时: 1295219.500 μs

# __contains__方法
# 0 in large_range: True | 耗时: 1.200 μs
# 5000000 in large_range: True | 耗时: 1.200 μs
# 9999999 in large_range: True | 耗时: 0.600 μs
# 10000000 in large_range: False | 耗时: 0.300 μs
