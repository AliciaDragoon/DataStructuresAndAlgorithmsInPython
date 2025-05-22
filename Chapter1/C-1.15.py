# 编写一个Python函数，用来接收一个数字序列，并判断是否所有数字都互不相同（即它们是不同的）。
def all_unique(numbers):
    """
    检查数字序列中的所有元素是否互不相同

    参数:
        numbers: 可迭代的数字序列

    返回:
        bool: 如果所有元素都互不相同则返回True，否则返回False
    """
    return len(numbers) == len(set(numbers))


print(all_unique([1, 2, 3, 4]))  # True
print(all_unique([1, 2, 2, 3]))  # False
print(all_unique([]))  # True
