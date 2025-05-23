# 一种惩罚学生的常见方法是让他们将一个句子写很多次。编写独立的Python程序，将以下句子"I will never spam my friends again."写100次。
# 程序应该对每个句子进行计数，另外，应该有8次不同的随机输入错误。
import random
import string


def generate_typo(sentence):
    """生成一个有打字错误的句子"""
    if len(sentence) == 0:
        return sentence

    # 随机选择一个字母位置
    pos = random.randint(0, len(sentence) - 1)
    # 保持大小写
    if sentence[pos].islower():
        wrong_char = random.choice(string.ascii_lowercase)
    elif sentence[pos].isupper():
        wrong_char = random.choice(string.ascii_uppercase)
    else:
        return sentence  # 如果不是字母则不修改

    return sentence[:pos] + wrong_char + sentence[pos + 1:]


def punishment_writer():
    sentence = "I will never spam my friends again."

    error_lines = random.sample(range(1, 101), 8)  # 8次不同的随机输入错误

    for i in range(1, 101):
        if i in error_lines:
            print(f"{i:3d}. {generate_typo(sentence)}")
        else:
            print(f"{i:3d}. {sentence}")

if __name__ == "__main__":
    punishment_writer()
