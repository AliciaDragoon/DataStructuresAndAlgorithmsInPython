# 在2.3.3节中，我们注意到，Vector类支持形如v = u + [5, 3, 10, -2, 1]这样的语法形式，向量和列表的总和返回一个新的向量。
# 然而，语法v = [5, 3, 10, -2, 1] + u却是非法的。解释应该如何修改Vector类的定义使得上述语法能够生成新的向量。
from ch02.vector import Vector


class VectorHasRadd(Vector):
    def __radd__(self, other):
        """Reverse addition operation (commutative case)."""
        return self.__add__(other)  # simply delegate to __add__


if __name__ == '__main__':
    u = VectorHasRadd([4, 5, 6, 7, 8])
    v = [5, 3, 10, -2, 1]
    print(v + u)
    # 输出：<9, 8, 16, 5, 9>
    print(u + v)
    # 输出：<9, 8, 16, 5, 9>
