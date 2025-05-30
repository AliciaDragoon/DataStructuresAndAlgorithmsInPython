# 2.3.4节的SequenceIterator类提供众所周知的前向迭代器。实现一个名为ReversedSequenceIterator的类，以此作为任何Python序列的反向迭代器。
# 第一次调用next返回序列的最后一个元素，第二次调用next返回倒数第二个元素，以此类推。
class ReversedSequenceIterator:
    """反向迭代器，用于迭代Python序列的逆序元素"""

    def __init__(self, sequence):
        """创建给定序列的反向迭代器"""
        self._seq = sequence  # 保存底层序列的引用
        self._index = len(sequence)  # 从序列末尾开始

    def __next__(self):
        """返回下一个元素，如果没有更多元素则引发StopIteration"""
        self._index -= 1  # 移动到前一个索引
        if self._index >= 0:
            return self._seq[self._index]  # 返回数据元素
        else:
            raise StopIteration()  # 没有更多元素

    def __iter__(self):
        """按照惯例，迭代器必须返回自身作为迭代器"""
        return self


# 创建列表的反向迭代器
numbers = [1, 2, 3, 4, 5]
reverse_iter = ReversedSequenceIterator(numbers)

# 使用 next() 函数迭代
print(next(reverse_iter))  # 输出: 5
print(next(reverse_iter))  # 输出: 4
print(next(reverse_iter))  # 输出: 3

# 使用 for 循环完成剩余迭代
for num in reverse_iter:
    print(num)
# 输出:
# 2
# 1
