# 编写一个程序，需要从控制台输入三个整数a、b、c，并确定它们是否可以在一个正确的算术公式（在给定的顺序）下成立，如"a+b=c", "a=b-c"或"a*b=c"。
def check_arithmetic(a, b, c):
    """
    检查三个整数是否满足任意一种基本算术公式

    参数:
        a, b, c: 要检查的三个整数

    返回:
        布尔值，表示是否存在有效的算术公式
    """
    # 检查所有可能的算术关系
    if a + b == c:
        return True
    if a == b - c:
        return True
    if a * b == c:
        return True
    return False


def main():
    try:
        # 从控制台获取三个整数输入
        a = int(input("请输入第一个整数a: "))
        b = int(input("请输入第二个整数b: "))
        c = int(input("请输入第三个整数c: "))

        # 检查算术关系
        if check_arithmetic(a, b, c):
            print(f"{a}, {b}, {c} 满足至少一种算术公式")
        else:
            print(f"{a}, {b}, {c} 不满足任何基本算术公式")

    except ValueError:
        print("错误：请输入有效的整数")


if __name__ == "__main__":
    main()
