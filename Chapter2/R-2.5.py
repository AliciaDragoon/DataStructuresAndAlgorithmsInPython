# 使用1.7节的技术修订CreditCard类的charge和make_payment方法确保调用方可以将一个数字作为参数传递。
from Chapter2.ch02.credit_card import CreditCard


class CreditCardExceptionalHandling(CreditCard):
    def charge(self, price):
        """执行信用卡消费操作（带参数验证）

        参数:
            price: 消费金额（必须为正数）

        返回:
            True 如果消费成功; False 如果超过信用额度

        异常:
            TypeError: 如果消费金额不是数字
            ValueError: 如果消费金额不是正数
        """
        if not isinstance(price, (int, float)):
            raise TypeError('消费金额必须是数字')
        if price <= 0:
            raise ValueError('消费金额必须为正数')

        return super().charge(price)  # 调用父类的charge方法

    def make_payment(self, amount):
        """执行信用卡还款操作（带参数验证）

        参数:
            amount: 还款金额（必须为正数）

        异常:
            TypeError: 如果还款金额不是数字
            ValueError: 如果还款金额不是正数
        """
        if not isinstance(amount, (int, float)):
            raise TypeError('还款金额必须是数字')
        if amount <= 0:
            raise ValueError('还款金额必须为正数')

        super().make_payment(amount)  # 调用父类的make_payment方法


card = CreditCardExceptionalHandling('John', 'Bank', '1234', 1000)

try:
    card.charge('abc')  # 会引发 TypeError
    card.charge(-50)  # 会引发 ValueError
    card.make_payment(0)  # 会引发 ValueError
except (TypeError, ValueError) as e:
    print(f"Error: {e}")
