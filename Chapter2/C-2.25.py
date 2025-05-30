# 练习R-2.12使用__mul__方法支持使用一个数字乘以Verctor类，而练习R-2.14使用__mul__方法支持运用点运算计算两个向量。给出Verctor.__mul__的一个简单实现，
# 使用运行时类型来检查是否支持这两种语法u*v和u*k，u和v表示向量实例，k代表一个数字。
class Vector:
    """Represent a vector in a multidimensional space."""

    def __init__(self, d):
        if isinstance(d, int):
            self._coords = [0] * d
        else:
            try:
                self._coords = [val for val in d]
            except TypeError:
                raise TypeError('invalid parameter type')

    def __len__(self):
        return len(self._coords)

    def __getitem__(self, j):
        return self._coords[j]

    def __setitem__(self, j, val):
        self._coords[j] = val

    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __eq__(self, other):
        return self._coords == other._coords

    def __ne__(self, other):
        return not self == other

    def __str__(self):
        return '<' + str(self._coords)[1:-1] + '>'

    def __neg__(self):
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = -self[j]
        return result

    def __lt__(self, other):
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        return self._coords < other._coords

    def __le__(self, other):
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        return self._coords <= other._coords

    def __mul__(self, other):
        """支持两种乘法运算：
        1. 向量 * 标量 → 返回新向量
        2. 向量 * 向量 → 返回点积标量
        """
        # 标量乘法 (u * k)
        if isinstance(other, (int, float)):
            result = Vector(len(self))
            for j in range(len(self)):
                result[j] = self[j] * other
            return result

        # 点积运算 (u * v)
        elif isinstance(other, Vector):
            if len(self) != len(other):
                raise ValueError('dimensions must agree')
            dot_product = 0
            for j in range(len(self)):
                dot_product += self[j] * other[j]
            return dot_product

        # 不支持的类型
        else:
            raise TypeError('unsupported operand type(s) for *')


# 标量乘法
v = Vector([1, 2, 3])
v2 = v * 2  # 返回新向量 Vector(3): <2, 4, 6>
print(v2)

# 点积运算
u = Vector([1, 2, 3])
w = Vector([4, 5, 6])
dot = u * w  # 返回标量值 32 (1*4 + 2*5 + 3*6)
print(dot)
