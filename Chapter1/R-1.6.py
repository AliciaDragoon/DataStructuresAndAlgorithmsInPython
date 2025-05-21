# 编写一个Python函数，用来接收正整数n，并返回1~n中所有奇数的平方和。
def sum_of_odd_squares(n):
    """
    计算 1 到 n 的所有奇数的平方和（直接遍历奇数）

    参数:
    n (int): 正整数

    返回:
    int: 1² + 3² + 5² + ... + (不超过n的最大奇数)²

    异常:
    ValueError: 如果 n 不是正整数
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n 必须是正整数")

    total = 0
    for i in range(1, n + 1, 2):  # 步长=2，直接遍历奇数
        total += i ** 2
    return total


print(sum_of_odd_squares(3))  # 输出: 1 + 9 + 25 = 35
print(sum_of_odd_squares(10))  # 输出: 1 + 9 + 25 + 49 + 81 = 165
print(sum_of_odd_squares(1))  # 输出: 1

try:
    print(sum_of_odd_squares(-3))
except ValueError as e:
    print(e)  # 输出: n 必须是正整数
