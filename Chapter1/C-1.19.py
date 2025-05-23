# 演示如何使用Python列表解析语法在不输入所有26个英文字母的情况下产生列表['a', 'b', 'c', ..., 'z']。
from string import ascii_lowercase

alphabet = list(ascii_lowercase)
# print(ascii_lowercase)  # 输出: abcdefghijklmnopqrstuvwxyz
print(alphabet)  # 输出: ['a', 'b', 'c', ..., 'z']
