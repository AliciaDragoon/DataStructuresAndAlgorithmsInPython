# 在1.8节中，我们对于计算所给整数的因子时提供了三种不同的生成器的实现方法。1.8节末尾处的第三种方法是最有效的，但我们注意到，它没有按递增顺序来产生因子。
# 修改生成器，使得其按递增顺序来产生因子，同时保持其性能优势。
def factors(n):
    k = 1
    while k * k < n:
        if n % k == 0:
            yield k
            yield n // k
        k += 1
    if k * k == n:
        yield k


def factors_in_order(n):
    """
    生成n的所有因子，按递增顺序排列

    参数:
        n: 正整数

    生成:
        n的因子，按从小到大顺序
    """
    k = 1
    small_factors = []
    large_factors = []

    while k * k <= n:
        if n % k == 0:
            small_factors.append(k)
            if k != n // k:  # 避免平方根重复添加
                large_factors.append(n // k)
        k += 1

    # 按顺序生成：先小因子，再大因子（反向）
    for factor in small_factors:
        yield factor
    for factor in reversed(large_factors):
        yield factor


# 测试用例
if __name__ == "__main__":
    for num in [36, 17, 100]:
        print(f"Factors of {num}: {list(factors_in_order(num))}")
