# 实现2.3.3节中Vector类的__mul__方法，使得表达式v*3返回一个新的矢量实例，新矢量v的坐标值都是以前的3倍。
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


if __name__ == '__main__':
    v = VectorHasMul([1, 2, 3])
    print(v * 3)  # 应该输出 <3, 6, 9>
