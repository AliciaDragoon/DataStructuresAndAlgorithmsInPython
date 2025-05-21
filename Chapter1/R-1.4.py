# 编写一个Python函数，用来接收正整数n，返回1~n的平方和。
def sum_of_squares(n):
    """
        计算1到n的平方和

        参数:
        n (int): 正整数

        返回:
        int: 1² + 2² + ... + n² 的和

        异常:
        ValueError: 如果n不是正整数
        """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n必须是正整数")
    return n * (n + 1) * (2 * n + 1) // 6  # 平方和公式


print(sum_of_squares(3))  # 输出: 14 (1 + 4 + 9)
print(sum_of_squares(5))  # 输出: 55 (1 + 4 + 9 + 16 + 25)
print(sum_of_squares(10))  # 输出: 385

try:
    print(sum_of_squares(0))
except ValueError as e:
    print(e)  # 输出: n必须是正整数
