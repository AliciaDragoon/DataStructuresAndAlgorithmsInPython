# 1.5.1节scale函数的实现如下。它能正常工作吗？请给出原因。
def scale(data, factor):
    for var in data:
        var *= factor
# 不能。
# var 是局部变量：在 for var in data 循环中，var 只是获取了列表中元素的值，而不是对列表元素的引用
# 数字不可变：当执行 var *= factor 时：
# 创建了一个新的数字对象
# 但这个新对象只赋值给了局部变量 var，没有修改原列表
# 列表未被修改：循环结束后，原始 data 列表保持不变
