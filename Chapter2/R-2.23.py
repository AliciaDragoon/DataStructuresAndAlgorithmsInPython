# 在之前的问题中有相似的问题，使用方法__lt__参数化Sequence类，使其支持字典比较seq1<seq2。
from abc import ABCMeta, abstractmethod


class Sequence(metaclass=ABCMeta):
    """Our own version of collections.Sequence abstract base class."""

    @abstractmethod
    def __len__(self):
        """Return the length of the sequence."""

    @abstractmethod
    def __getitem__(self, j):
        """Return the element at index j of the sequence."""

    def __contains__(self, val):
        """Return True if val found in the sequence; False otherwise."""
        for j in range(len(self)):
            if self[j] == val:  # found match
                return True
        return False

    def index(self, val):
        """Return leftmost index at which val is found (or raise ValueError)."""
        for j in range(len(self)):
            if self[j] == val:  # leftmost match
                return j
        raise ValueError('value not in sequence')  # never found a match

    def count(self, val):
        """Return the number of elements equal to given value."""
        k = 0
        for j in range(len(self)):
            if self[j] == val:  # found a match
                k += 1
        return k

    def __eq__(self, other):
        """Return True if two sequences are element-wise equal."""
        if not isinstance(other, Sequence):
            return False

        if len(self) != len(other):
            return False

        for index in range(len(self)):
            if self[index] != other[index]:
                return False
        return True

    def __lt__(self, other):
        """Lexicographical comparison for sequences (dictionary order)."""
        # 检查是否为相同类型
        if not isinstance(other, Sequence):
            return NotImplemented

        # 获取共同长度（较短序列的长度）
        min_length = min(len(self), len(other))

        # 逐个元素比较
        for i in range(min_length):
            if self[i] < other[i]:
                return True
            if self[i] > other[i]:
                return False

        # 如果共同部分相等，则较短的序列较小
        return len(self) < len(other)


class MyList(Sequence):
    def __init__(self, items):
        self._items = items

    def __len__(self):
        return len(self._items)

    def __getitem__(self, j):
        return self._items[j]


# 创建测试序列
seq1 = MyList([1, 2, 3])  # 序列A
seq2 = MyList([1, 2, 4])  # 序列B（第三元素较大）
seq3 = MyList([1, 2, 3, 0])  # 序列C（相同前缀但更长）
seq4 = MyList([1, 1, 5])  # 序列D（第二元素较小）

# 测试比较
print(seq1 < seq2)  # True: [1,2,3] < [1,2,4]
print(seq1 < seq3)  # True: [1,2,3] < [1,2,3,0]（相同前缀但seq1较短）
print(seq1 < seq4)  # False: [1,2,3] > [1,1,5]（第二元素2>1）
print(seq3 < seq1)  # False: [1,2,3,0] > [1,2,3]（较长序列较大）
