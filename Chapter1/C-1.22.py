# 编写一个Python程序，用来接收长度为n的两个整数数组a和b并返回数组a和b的点积。也就是返回一个长度为n的数组c，即c[i]=a[i]•b[i], for i = 0, ..., n-1。
def dot_product(a, b):
    """
    计算两个数组的点积（逐元素相乘）

    参数:
        a: 第一个数组（列表）
        b: 第二个数组（列表）

    返回:
        点积结果数组

    异常:
        ValueError: 当输入数组长度不一致时抛出
    """
    if len(a) != len(b):
        raise ValueError("输入数组长度必须相同")

    return [a[i] * b[i] for i in range(len(a))]


# 示例用法
if __name__ == "__main__":
    a = [1, 2, 3]
    b = [4, 5, 6]
    result = dot_product(a, b)
    print(result)  # 输出: [4, 10, 18]
