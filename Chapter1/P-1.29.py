# 编写一个Python程序，输出由字母'c'，'a'，'t'，'d'，'o'，'g'组成的所有可能的字符串（每个字母只使用一次）。
from itertools import permutations

# 定义字母列表
letters = ['c', 'a', 't', 'd', 'o', 'g']

# 生成所有可能的排列组合
all_combinations = permutations(letters)

# 遍历并打印每个组合（转换为字符串形式）
for combo in all_combinations:
    print(''.join(combo))
