# 实现2.3.3节中Vector类的__mul__方法，使表达式u*v返回一个标量代表向量点运算的结果，即∑（i = 1 到 d）uᵢ · vᵢ。
from ch02.vector import Vector


class VectorDot(Vector):
    def __mul__(self, other):
        """Return the dot product of two vectors."""
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        return sum(self[j] * other[j] for j in range(len(self)))


if __name__ == '__main__':
    u = VectorDot([1, 2, 3])
    v = VectorDot([4, 5, 6])
    print(u * v)  # 应该输出 32 (1*4 + 2*5 + 3*6 = 4 + 10 + 18 = 32)
