# 编写一个Python函数，用来接收一个整数序列，并判断该序列中是否存在一对乘积是奇数的互不相同的数。
def has_odd_product_pair(sequence):
    """
    判断序列中是否存在一对不同的数，其乘积为奇数（奇数 × 奇数 = 奇数，其他组合均为偶数）

    参数:
    sequence: 整数序列（列表、元组等可迭代对象）

    返回:
    bool: 如果存在返回True，否则返回False
    """
    odd_numbers = set()  # 用集合存储不同的奇数
    for num in sequence:
        if num % 2 != 0:  # 如果是奇数
            odd_numbers.add(num)
            if len(odd_numbers) >= 2:  # 存在至少两个不同的奇数
                return True
    return False


print(has_odd_product_pair([1, 2, 3]))  # True (1×3=3)
print(has_odd_product_pair([2, 4, 6]))  # False (无奇数)
print(has_odd_product_pair([3, 3, 5]))  # True (3×5=15)
print(has_odd_product_pair([1]))  # False (只有一个奇数)
print(has_odd_product_pair([]))  # False (空序列)
print(has_odd_product_pair([-1, -3, 4]))  # True (-1×-3=3)
