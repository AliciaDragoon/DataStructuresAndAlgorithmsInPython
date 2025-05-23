# 编写一个Python程序来模拟手持计算器，程序应该可以处理来自Python控制台（表示push按钮）的输入，每个操作执行完毕后将内容输出到屏幕。
# 计算器至少应该能够处理基本的算术运算和复位/清除操作。
def simple_calculator():
    result = 0
    print("手持计算器 (输入 'c' 清除, 'q' 退出)")

    while True:
        num = input("请输入数字: ")
        if num == 'q':
            break
        if num == 'c':
            result = 0
            print("已重置为 0")
            continue

        try:
            num = float(num)
        except:
            print("请输入有效数字！")
            continue

        op = input("请输入操作符 (+, -, *, /): ")
        if op not in ['+', '-', '*', '/']:
            print("无效操作符！")
            continue

        num2 = input("请输入第二个数字: ")
        try:
            num2 = float(num2)
        except:
            print("请输入有效数字！")
            continue

        if op == '+':
            result = num + num2
        elif op == '-':
            result = num - num2
        elif op == '*':
            result = num * num2
        elif op == '/':
            if num2 == 0:
                print("错误：除数不能为0！")
                continue
            result = num / num2

        print(f"结果: {result}")


if __name__ == "__main__":
    simple_calculator()
