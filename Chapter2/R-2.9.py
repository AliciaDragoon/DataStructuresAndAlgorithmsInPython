# 实现2.3.3节Vector类的__sub__方法，使表达式u-v返回一个代表两矢量间差异的新矢量实例。
from ch02.vector import Vector


class VectorHasSub(Vector):
    def __sub__(self, other):
        """Return difference of two vectors."""
        if len(self) != len(other):  # relies on __len__ method
            raise ValueError('dimensions must agree')
        result = Vector(len(self))  # start with vector of zeros
        for j in range(len(self)):
            result[j] = self[j] - other[j]
        return result


if __name__ == '__main__':
    u = VectorHasSub([5, 3, 10])
    v = VectorHasSub([1, 2, 3])
    print(u - v)  # 应该输出 <4, 1, 7>
