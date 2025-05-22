# 编写一个函数的伪代码描述，该函数用来逆置n个整数的列表，使这些数以相反的顺序输出，并将该方法与可以实现相同功能的Python函数进行比较。
# FUNCTION reverse_integer_list(original_list):
#     // 输入: original_list (包含n个整数的列表)
#     // 输出: 逆置后的新列表
#
#     n = LENGTH(original_list)          // 获取列表长度
#     reversed_list = NEW_ARRAY(n)       // 创建空数组存储结果
#
#     FOR i FROM 0 TO n-1:
#         reversed_list[i] = original_list[n - 1 - i]  // 首尾交换位置
#
#     RETURN reversed_list
# END FUNCTION
def reverse_list_custom(lst):
    n = len(lst)
    return [lst[n - 1 - i] for i in range(n)]

# Python内置方法1: 切片操作
# reversed_list = original_list[::-1]

# Python内置方法2: reverse()方法（原地修改）
# original_list.reverse()

# Python内置方法3: reversed()函数（新建列表）
# reversed_list = list(reversed(original_list))
