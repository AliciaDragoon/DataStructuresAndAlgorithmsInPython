# 编写一个Python函数is_multiple(n,m)，用来接收两个整数值n和m，如果n是m的倍数，即存在整数i使得n=mi,那么函数返回True，否则返回False。
def is_multiple(n, m):
    """
    检查n是否是m的倍数

    参数:
    n (int): 要检查的数字
    m (int): 可能的因数

    返回:
    bool: 如果n是m的倍数返回True，否则返回False
    """
    if m == 0:
        return False  # 0不能作为除数
    return n % m == 0


print(is_multiple(10, 5))  # 输出: True
print(is_multiple(10, 3))  # 输出: False
print(is_multiple(0, 5))   # 输出: True (0是任何非零数的倍数)
print(is_multiple(5, 0))   # 输出: False (0不能作为除数)
