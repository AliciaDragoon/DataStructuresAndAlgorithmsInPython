# 写一个拓展自Progression类的Python类,使Progression中的每个值都是前两个值差的绝对值。其中应包括一个构造函数，以接受一对数字作为第一和第二个值，
# 使用2和200作为默认值。
from ch02.progressions import Progression


class AbsoluteProgression(Progression):
    """生成一个序列，其中每个值都是前两个值的绝对差"""

    def __init__(self, first=2, second=200):
        """
            使用第一和第二值初始化数列。

        参数:
            first: 数列的第一个值 (默认=2)
            second: 数列的第二个值 (默认=200)
        """
        super().__init__(first)  # 使用基类初始化第一个值
        self._next_val = second  # 存储第二个值用于第一次推进
        self._prev = first  # 存储第一个值作为后续计算的前一个值

    def _advance(self):
        """将当前值更新为序列中的下一个值"""
        if self._next_val is not None:
            # 第一次推进：更新到第二个值
            self._prev = self._current  # 保存原始第一个值作为前一个值
            self._current = self._next_val  # 设置当前值为第二个值
            self._next_val = None  # 第一次推进后清除标志
        else:
            # 后续推进：计算前两个值的绝对差
            new_value = abs(self._prev - self._current)
            # 更新状态:
            #   - self._prev 变为当前值（用于下次计算）
            #   - self._current 变为新计算的值
            self._prev, self._current = self._current, new_value


if __name__ == '__main__':
    print("默认起始值的绝对差值数列:")
    AbsoluteProgression().print_progression(10)  # 输出: 2 200 198 2 196 194 2 192 190 2

    print("\n起始值为5和8的绝对差值数列:")
    AbsoluteProgression(5, 8).print_progression(8)  # 输出: 5 8 3 5 2 3 1 2
