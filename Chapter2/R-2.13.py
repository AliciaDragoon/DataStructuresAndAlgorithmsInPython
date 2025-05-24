# 练习R-2.12要求对2.3.3节中的Vector类实现__mul__方法，以提供对语法v*3的支持。试实现__rmul__方法，提供对语法3*v的支持。
from ch02.vector import Vector


class VectorHasMul(Vector):
    def __mul__(self, scalar):
        """Return the product of the vector and a scalar."""
        if not isinstance(scalar, (int, float)):
            raise TypeError("scalar must be a number")
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] * scalar
        return result

    def __rmul__(self, scalar):
        """Return the product of a scalar and the vector (reverse operation)."""
        return self.__mul__(scalar)  # reuse __mul__ implementation


if __name__ == '__main__':
    v = VectorHasMul([1, 2, 3])
    print(v * 3)  # 应该输出 <3, 6, 9>
    print(3 * v)  # 应该输出 <3, 6, 9> (通过 __rmul__)
