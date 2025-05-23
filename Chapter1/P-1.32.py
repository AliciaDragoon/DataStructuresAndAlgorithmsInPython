# 编写一个Python程序来模拟一个简单的计算器，使用控制台作为输入和输出的专用设备。也就是说，计算机的每一次输入做一个单独的行，它可以输入一个数字（如1034或12.34）
# 或操作符（如+或=）。每一次输入后，应该输出计算机显示的结果并将其输出到Python控制台。
result = 0
current_op = None

print("简单计算器 (输入'c'清零，'q'退出)")

while True:
    user_input = input("> ").strip()

    if user_input == 'q':
        break
    elif user_input == 'c':
        result = 0
        current_op = None
        print("显示: 0")
        continue

    try:
        # 尝试作为数字处理
        num = float(user_input)
        if current_op is None:
            result = num
        else:
            if current_op == '+':
                result += num
            elif current_op == '-':
                result -= num
            elif current_op == '*':
                result *= num
            elif current_op == '/':
                result /= num
        print(f"显示: {result}")

    except ValueError:
        # 作为操作符处理
        if user_input in '+-*/':
            current_op = user_input
            print(f"显示: {result}")
        elif user_input == '=':
            print(f"显示: {result}")
        else:
            print(f"未知输入: {user_input}")
