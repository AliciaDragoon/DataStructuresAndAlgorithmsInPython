# 编写一个Python函数is_even(k)，用来接收一个整数k，如果k是偶数返回True，否则返回False。但是函数中不能使用乘法、除法或取余操作。
def is_even(k):
    """
    检查整数k是否为偶数

    参数:
    k (int): 要检查的整数

    返回:
    bool: 如果k是偶数返回True，否则返回False
    """
    return (k & 1) == 0  # 使用位运算&（按位与）操作。


# 任何数与1进行按位与操作，结果为0表示最后一位是0（偶数），结果为1表示最后一位是1（奇数）

print(is_even(4))  # 输出: True
print(is_even(7))  # 输出: False
print(is_even(0))  # 输出: True
print(is_even(-2))  # 输出: True
print(is_even(-3))  # 输出: False
