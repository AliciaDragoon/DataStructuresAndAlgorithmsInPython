# 基于python的解析语法和内置函数sum，写一个单独的命令来计算练习R-1.6中的和。
def sum_of_odd_squares(n):
    """
    计算 1 到 n 的所有奇数的平方和

    参数:
    n (int): 正整数

    返回:
    int: 1² + 3² + 5² + ... + (不超过n的最大奇数)²

    异常:
    ValueError: 如果 n 不是正整数
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n 必须是正整数")

    return sum(i ** 2 for i in range(1, n + 1, 2))  # 步长=2，直接生成奇数


print(sum_of_odd_squares(5))  # 输出: 1² + 3² + 5² = 1 + 9 + 25 = 35
print(sum_of_odd_squares(10))  # 输出: 1 + 9 + 25 + 49 + 81 = 165
print(sum_of_odd_squares(1))  # 输出: 1

try:
    print(sum_of_odd_squares(-3))
except ValueError as e:
    print(e)  # 输出: n 必须是正整数
