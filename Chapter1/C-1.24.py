# 编写一个Python函数，计算所给字符串中元音字母的个数。
def count_vowels(text):
    """
       计算字符串中元音字母的数量（不区分大小写）

       参数:
           text: 要检查的字符串

       返回:
           元音字母的总数
    """
    vowels = {'a', 'e', 'i', 'o', 'u'}
    count = 0
    for char in text.lower():  # 转换为小写以统一检查
        if char in vowels:
            count += 1
    return count


# 示例用法
if __name__ == "__main__":
    test_string = "Hello World! Python is awesome!"
    print(count_vowels(test_string))  # 输出: 9
