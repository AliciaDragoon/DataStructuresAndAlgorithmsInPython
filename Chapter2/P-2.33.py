# 写一个Python程序，如输入标准的代数多项式，则输出该多项式的一阶导数。
import re


def polynomial_derivative(poly):
    # 移除输入字符串中的所有空格
    poly = poly.replace(' ', '')

    # 空字符串返回"0"
    if not poly:
        return "0"

    # 如果多项式不以符号开头，则在前面添加 '+' 以便统一处理
    if poly[0] not in ['+', '-']:
        poly = '+' + poly

    # 正则表达式匹配每一项：符号([+-])、系数(\d*)、变量部分([xX]?)、指数(?:\^(\d+))?
    pattern = r'([+-])(\d*)([xX]?)(?:\^(\d+))?'
    terms = re.findall(pattern, poly)

    derivative_terms = []
    for sign, coef_str, var, exp_str in terms:
        if not var and not coef_str:
            continue  # 跳过无效项（如单独的符号）

        if var:  # 处理变量项
            # 解析系数：如果系数字符串为空，则系数为1（根据符号调整）
            coef = int(coef_str) if coef_str else 1
            if sign == '-':
                coef = -coef
            # 解析指数：如果指数字符串存在，则使用；否则默认为1
            exp = int(exp_str) if exp_str else 1
        else:  # 处理常数项
            if not coef_str:
                continue  # 系数为空则跳过
            coef = int(sign + coef_str)
            exp = 0

        # 求导：新系数 = 原系数 * 指数，新指数 = 原指数 - 1
        new_coef = coef * exp
        new_exp = exp - 1

        # 跳过导数为0的项
        if new_coef == 0:
            continue

        # 根据新系数和新指数构建项字符串
        if new_exp == 0:  # 常数项
            term = str(new_coef)
        elif new_exp == 1:  # 一次项
            if new_coef == 1:
                term = 'x'
            elif new_coef == -1:
                term = '-x'
            else:
                term = f"{new_coef}x"
        else:  # 高次项
            if new_coef == 1:
                term = f"x^{new_exp}"
            elif new_coef == -1:
                term = f"-x^{new_exp}"
            else:
                term = f"{new_coef}x^{new_exp}"
        derivative_terms.append(term)

    # 组合所有导数项
    if not derivative_terms:
        return "0"

    result = derivative_terms[0]
    for term in derivative_terms[1:]:
        if term.startswith('-'):
            result += term
        else:
            result += '+' + term

    return result


# 测试示例
if __name__ == "__main__":
    print("多项式求导计算器（仅支持标准多项式）")
    print("========================================")
    print("支持的格式示例:")
    print("- 3x^2 + 2x - 5")
    print("- -x^3 + 4x")
    print("- 5")
    print("\n⚠️ 限制说明:")
    print("- 仅支持单变量x的多项式")
    print("- 不支持: 指数函数(e^x), 三角函数(sin/cos), 分数, 负指数等")
    print("- 系数和指数必须为整数")
    print("- 变量必须为x或X")
    print("========================================")
    poly = input("请输入多项式（例如 3x^2 + 2x - 5）: ")
    derivative = polynomial_derivative(poly)
    print("一阶导数为:", derivative)
