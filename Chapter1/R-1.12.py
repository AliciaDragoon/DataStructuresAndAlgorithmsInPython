# Python的random模块包括一个函数choice(data)，可以从一个非空序列返回一个随机元素。Random模块还包含一个更基本的randrange函数，参数类似于内置的range函数，可以在给定范围返回一个随机数。只使用randrange函数，实现自己的choice函数。
import random


def my_choice(data):
    """
    模拟 random.choice 的功能，从非空序列中随机返回一个元素

    参数:
    data: 非空序列（如列表、元组、字符串等）

    返回:
    随机选择的元素

    异常:
    ValueError: 如果输入序列为空
    """
    if not data:
        raise ValueError("输入序列不能为空")
    # 使用 randrange 生成一个随机索引
    random_index = random.randrange(len(data))
    return data[random_index]  # 通过索引直接获取序列元素


# 测试列表
print(my_choice([1, 2, 3, 4, 5]))  # 可能输出: 3

# 测试字符串
print(my_choice("Python"))  # 可能输出: 't'

# 测试元组
print(my_choice(('a', 'b', 'c')))  # 可能输出: 'b'

# 空序列测试
try:
    print(my_choice([]))
except ValueError as e:
    print(e)  # 输出: 输入序列不能为空
