# collection.Sequence抽象基类不提供对两个序列的比较支持，从代码段2-14中修改Sequence类，使其定义包含__eq__方法，使两个序列中的元素相等时，
# 表达式seq1==seq2返回True。
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
        # 检查是否为相同类型（或兼容类型）
        if not isinstance(other, Sequence):
            return False

        # 检查长度是否相同
        if len(self) != len(other):
            return False

        # 逐个元素比较
        for index in range(len(self)):
            if self[index] != other[index]:
                return False
        return True


class MyList(Sequence):
    def __init__(self, items):
        self._items = items

    def __len__(self):
        return len(self._items)

    def __getitem__(self, j):
        return self._items[j]


# 创建测试序列
seq1 = MyList([1, 2, 3])
seq2 = MyList([1, 2, 3])
seq3 = MyList([1, 2, 4])
seq4 = MyList([1, 2, 3, 4])

# 测试比较
print(seq1 == seq2)  # True (相同元素)
print(seq1 == seq3)  # False (不同元素)
print(seq1 == seq4)  # False (不同长度)
print(seq1 == [1, 2, 3])  # False (不同类型)
