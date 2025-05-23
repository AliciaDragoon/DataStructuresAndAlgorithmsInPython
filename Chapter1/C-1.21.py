# 编写一个Python程序，反复从标准输入读取一行直到抛出EOFError异常，然后以相反的顺序输出这些行（用户可以通过键按Ctrl+D结束输入）。
def reverse_input_lines():
    """
    读取所有输入行直到EOF，然后逆序输出
    """
    lines = []
    try:
        while True:
            line = input()  # 读取每一行输入
            lines.append(line)
    except EOFError:  # 捕获Ctrl+D/Ctrl+Z（Windows）信号
        pass  # 输入结束

    # 逆序输出所有行
    for line in reversed(lines):
        print(line)


if __name__ == "__main__":
    reverse_input_lines()
