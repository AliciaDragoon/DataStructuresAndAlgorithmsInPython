# Python允许负整数作为序列的索引值，如一个长度为n的字符串，当索引值-n<=k<0时，所指的元素为s[k]，那么求一个正整数索引值j>=0，使得s[j]指向的也是相同的元素。
def negative_to_positive_index(s, k):
    """
    将负索引转换为等效的正索引

    参数:
    s: 序列（如字符串、列表等）
    k: 负索引（-len(s) <= k < 0）

    返回:
    int: 等效的正索引 j，使得 s[j] == s[k]

    异常:
    ValueError: 如果 k 不是有效的负索引
    """
    if not (-len(s) <= k < 0):
        raise ValueError("k 必须是有效的负索引")
    return len(s) + k


s = "Python"

print(negative_to_positive_index(s, -1))  # 输出: 5 (s[-1] == s[5] == 'n')
print(negative_to_positive_index(s, -3))  # 输出: 3 (s[-3] == s[3] == 'h')
