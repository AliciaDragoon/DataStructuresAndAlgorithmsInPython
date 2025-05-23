# 给出一个Python代码的例子，编写一个索引可能越界的元素列表。如果索引越界，程序应该捕获异常结果并打印以下错误消息："Don't try buffer overflow attacks in Python!"。
def access_list_element(lst, index):
    """
    尝试访问列表元素并捕获索引越界异常

    参数:
        lst: 要访问的列表
        index: 要访问的索引

    返回:
        如果索引有效则返回对应元素
        如果索引越界则打印错误消息并返回None
    """
    try:
        return lst[index]
    except IndexError:
        print("Don't try buffer overflow attacks in Python!")
        return None


# 示例用法
if __name__ == "__main__":
    my_list = [10, 20, 30]

    # 正常访问
    print(access_list_element(my_list, 1))  # 输出: 20

    # 越界访问
    print(access_list_element(my_list, 5))  # 输出错误消息并返回None
    # 控制台会显示: Don't try buffer overflow attacks in Python!
    # 然后输出: None
