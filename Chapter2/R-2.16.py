# 2.3.5节中的Range类按照如下公式
# max(0, (stop - start + step -1) // step)
# 去计算范围内元素的数量。即使假设一个正的step大小，也并不能很明显地看出为什么这个公式提供了正确的计算。可以用你自己的方式证明这个公式。

# 公式分析：
# max(0, (stop - start + step - 1) // step)
#
# 基本思路：
# 我们需要计算从start开始，以step为步长，不超过stop的元素数量。
#
# 简单情况：
# 对于start = 0, stop = n, step = 1:
#
# 公式变为: (n - 0 + 1 - 1) // 1 = n // 1 = n
# 这正是我们期望的range(n)的长度
# 一般情况证明：
# 首先考虑stop > start且step > 0的情况：
#
# 我们需要找到最大的整数k，使得start + k*step < stop
# 解不等式：k < (stop - start)/step
# 因为k必须是整数，所以最大k是ceil((stop - start)/step) - 1
# 元素数量是k + 1 = ceil((stop - start)/step)
# 整数除法实现向上取整的技巧：
#
# (a + b - 1) // b等价于ceil(a/b)
# 这里a = stop - start, b = step
# 所以(stop - start + step - 1) // step就是ceil((stop - start)/step)
# 边界情况：
#
# 如果stop <= start，计算结果会是0或负数，max(0, ...)确保返回0
# 如果step为负，公式同样适用（但代码中已经检查step != 0）
# 为什么是stop - start + step - 1而不是stop - start - 1：
# 加上step - 1是为了实现向上取整的效果
# 例如：start=1, stop=10, step=3
# 实际元素：1, 4, 7 (共3个)
# 计算：(10-1+3-1)//3 = 11//3 = 3
# 数学等价性：
# 这个公式等价于计算满足以下条件的最大整数k： start + (k-1)*step < stop <= start + k*step
#
# 因此，这个公式确实能正确计算范围内元素的数量。
