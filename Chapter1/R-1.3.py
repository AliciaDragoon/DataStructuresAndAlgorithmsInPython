# 编写一个Python函数minmax(data)，用来在数的序列中找出最小数和最大数，并以一个长度为2的元组返回。注意：不能通过内置函数min和max实现。
def minmax(data):
    """
    找出序列中的最小值和最大值

    参数:
    data: 可迭代的数值序列

    返回:
    tuple: (最小值, 最大值)

    异常:
    ValueError: 如果输入序列为空
    """
    if len(data) == 0:
        raise ValueError("输入序列不能为空")

    min_val = max_val = data[0]  # 将最小值和最大值都初始化为序列的第一个元素

    for num in data[1:]:  # 从第二个元素开始遍历
        if num < min_val:  # 如果当前数字比最小值小，更新最小值
            min_val = num
        elif num > max_val:  # 如果当前数字比最大值大，更新最大值
            max_val = num

    return min_val, max_val


print(minmax([3, 1, 4, 1, 5, 9, 2]))  # 输出: (1, 9)
print(minmax([-5, 10, 8, -3, 12]))  # 输出: (-5, 12)
print(minmax([42]))  # 输出: (42, 42)
