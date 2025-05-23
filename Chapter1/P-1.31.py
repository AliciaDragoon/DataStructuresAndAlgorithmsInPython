# 编写一个可以找零钱的Python程序。程序应该将两个数字作为输入，一个是需要支付的钱数，一个是你给找的钱数。当你需要支付和所给的钱数不同时，它应该返回
# 所找的纸币和硬币的数量。纸币和硬币的值可以基于之前或现任政府的货币体系。试设计程序，以便返回尽可能少的纸币和硬币。
def make_change(amount_due, amount_paid):
    """
    计算找零钱的最优组合（使用人民币面额）

    参数:
        amount_due (float): 应付金额
        amount_paid (float): 实付金额

    返回:
        dict: 包含各面额数量的字典
    """
    # 人民币面额（从大到小排列）
    denominations = {
        100: '100元',
        50: '50元',
        20: '20元',
        10: '10元',
        5: '5元',
        1: '1元',
        0.5: '5角',
        0.1: '1角'
    }

    # 计算找零金额
    change = amount_paid - amount_due

    if change < 0:
        raise ValueError("实付金额不足")
    elif change == 0:
        return {"无需找零": 0}

    result = {}
    remaining = round(change, 1)  # 处理浮点数精度问题

    # 遍历所有面额
    for denom in sorted(denominations.keys(), reverse=True):
        if remaining <= 0:
            break

        count = int(remaining // denom)
        if count > 0:
            result[denominations[denom]] = count
            remaining = round(remaining - (count * denom), 1)

    return result


# 用户交互
try:
    due = float(input("请输入应付金额: "))
    paid = float(input("请输入实付金额: "))

    if due <= 0 or paid <= 0:
        print("金额必须大于0")
    else:
        change_result = make_change(due, paid)
        print("\n找零结果:")
        for bill, count in change_result.items():
            print(f"{bill}: {count}张" if "元" in bill else f"{bill}: {count}枚")

except ValueError as e:
    print(f"错误: {e}")
