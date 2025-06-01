# 写一个拓展自Progression类的Python类,使Progression中的每个值是前一个数值的平方根（注意：你不能用整数来表示每个值）。构造函数应该接受一个可选参数用于指定开始值，
# 使用65536作为默认值
from ch02.progressions import Progression
import math


class SquareRootProgression(Progression):
    """迭代器生成平方根数列（每个值是前一个值的平方根）。

    构造函数接受一个可选参数指定起始值（默认为65536）。
    起始值必须是非负数，否则会引发ValueError。
    """

    def __init__(self, start=65536):
        """初始化当前值，验证起始值非负。"""
        if start < 0:
            raise ValueError("起始值必须是非负数")
        super().__init__(float(start))  # 确保初始值为浮点数类型

    def _advance(self):
        """将当前值更新为其平方根。"""
        self._current = math.sqrt(self._current)


# 创建默认起始值65536的数列
prog = SquareRootProgression()
prog.print_progression(5)  # 输出：65536.0 256.0 16.0 4.0 2.0

# 创建起始值16的数列
prog = SquareRootProgression(16)
prog.print_progression(4)  # 输出：16.0 4.0 2.0 1.4142135623730951

# 起始值为0的数列
prog = SquareRootProgression(0)
prog.print_progression(3)  # 输出：0.0 0.0 0.0

# 起始值为负数会报错
try:
    prog = SquareRootProgression(-10)
except ValueError as e:
    print(e)  # 输出：起始值必须是非负数
