# 编写一个Python程序，输入一个大于2的正整数，求将该数反复被2整除直到商小于2的次数。
def count_divisions(n):
    """
    计算一个大于2的正整数被2反复整除直到商小于2的次数

    参数:
        n (int): 输入的正整数（必须大于2）

    返回:
        int: 整除次数
    """
    if n <= 2:
        raise ValueError("输入的数字必须大于2")

    count = 0
    while n >= 2:
        n = n // 2
        count += 1
    return count


# 测试示例
num = int(input("请输入一个大于2的正整数: "))
try:
    times = count_divisions(num)
    print(f"数字{num}被2整除直到小于2的次数是: {times}")
except ValueError as e:
    print(e)
