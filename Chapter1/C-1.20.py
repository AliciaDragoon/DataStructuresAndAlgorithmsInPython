# python的random模块包括一个函数shuffle(data)，它可以接收一个元素的列表和一个随机的重新排列元素，以使每个可能的的序列发生概率相等。
# random模块还包括一个更基本的函数randint(a, b)，它可以返回一个从a到b（包括两个端点）的随机整数。只使用randint函数，实现自己的shuffle函数。
from random import randint


def my_shuffle(data):
    """
    使用randint实现Fisher-Yates洗牌算法
    每个元素都有均等的机会出现在任何位置，共n!种可能的排列，每种概率都是1/n!

    参数:
        data: 要打乱的可变序列（通常是列表）
    """
    n = len(data)
    for i in range(n - 1, 0, -1):  # 从最后一个元素开始，向前遍历
        j = randint(0, i)  # 对于当前位置i，随机选择0到i之间的一个索引j
        data[i], data[j] = data[j], data[i]  # 交换i和j位置的元素


data = [1, 2, 3, 4, 5]
my_shuffle(data)
print(data)  # 可能输出: [3, 1, 5, 2, 4]
