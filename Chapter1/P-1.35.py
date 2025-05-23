# 生日悖论是说，当房间人数n超过23时，那么该房间里有两个人生日相同的可能性是一半以上。这其实不是一个悖论，但许多人觉得不可思议。设计一个Python程序，
# 可以通过一系列随机生成的生日的实验来测试这个悖论，例如可以n=5，10，15，20，...，100测试这个悖论。
import random


def has_duplicate_birthdays(birthdays):
    """检查是否有重复生日"""
    return len(birthdays) != len(set(birthdays))


def generate_birthdays(n):
    """生成n个随机生日（假设一年有365天）"""
    return [random.randint(1, 365) for _ in range(n)]


def run_simulation(n, trials=10000):
    """对给定人数n运行若干次(trials)实验，返回有重复生日的概率"""
    count = 0
    for _ in range(trials):
        birthdays = generate_birthdays(n)
        if has_duplicate_birthdays(birthdays):
            count += 1
    return count / trials


def test_birthday_paradox():
    print("人数\t有相同生日的概率")
    for n in range(5, 105, 5):  # 从5到100，每次增加5人
        probability = run_simulation(n)
        print(f"{n}\t{probability:.2%}")


# 运行程序
test_birthday_paradox()
