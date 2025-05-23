# 编写一个Python函数，接收一个表示一个句子的字符串s，然后返回该字符串删除了所有标点符号的副本。例如，给定字符串"Let's try, Mike."，
# 这个函数将返回"Lets try Mike"。
import string


def remove_punctuation(s):
    """
    删除字符串中的所有标点符号

    参数:
        s: 输入字符串

    返回:
        删除所有标点符号后的新字符串
    """
    # 创建翻译表，将标点符号映射为None
    translator = str.maketrans('', '', string.punctuation)
    # 使用翻译表删除标点
    return s.translate(translator)


# 示例用法
if __name__ == "__main__":
    test_str = "Let's try, Mike."
    print(remove_punctuation(test_str))  # 输出: Lets try Mike
