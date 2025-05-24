# 2.3节的CreditCard类将一个新账户的余额初始化为0。修改这个类，使构造函数具有第五个参数作为可选参数，它可以初始化一个余额不为0的新账号。
# 而原来的四参数构造函数仍然可以用来生成余额为零的新账户。
from Chapter2.ch02.credit_card import CreditCard


class CreditCardSetBalance(CreditCard):
    """扩展CreditCard类，支持设置初始余额

    Args:
        customer: 客户姓名
        bank: 银行名称
        acnt: 账号
        limit: 信用额度
        balance: (可选)初始余额，默认为0
    """

    def __init__(self, customer, bank, acnt, limit, balance=None):
        super().__init__(customer, bank, acnt, limit)  # 调用父类初始化
        self._balance = balance if balance is not None else 0  # 设置余额


if __name__ == '__main__':
    # 测试默认余额
    card1 = CreditCardSetBalance('张三', '中国银行', '62258888', 5000)
    print(f"默认余额: {card1.get_balance()}")  # 应为0

    # 测试指定余额
    card2 = CreditCardSetBalance('李四', '建设银行', '62259999', 8000, 300)
    print(f"指定初始余额: {card2.get_balance()}")  # 应为300

    # 测试显式None
    card3 = CreditCardSetBalance('王五', '工商银行', '62256666', 10000, None)
    print(f"显式None余额: {card3.get_balance()}")  # 应为0
