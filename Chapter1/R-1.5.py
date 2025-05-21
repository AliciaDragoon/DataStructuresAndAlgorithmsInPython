# 基于python的解析语法和内置函数sum，写一个单独的命令来计算练习R-1.4中的和。
def sum_of_squares(n):
    """
    使用解析语法和sum函数计算1到n的平方和

    参数:
    n (int): 正整数

    返回:
    int: 1² + 2² + ... + n²的和

    异常:
    ValueError: 如果n不是正整数
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n必须是正整数")

    return sum(i ** 2 for i in range(1, n + 1))


print(sum_of_squares(3))  # 输出: 14 (1 + 4 + 9)
print(sum_of_squares(5))  # 输出: 55 (1 + 4 + 9 + 16 + 25)
print(sum_of_squares(10))  # 输出: 385

try:
    print(sum_of_squares(-2))
except ValueError as e:
    print(e)  # 输出: n必须是正整数
