# 使用1.7节的技术修订CreditCard类的charge和make_payment方法确保调用方可以将一个数字作为参数传递。
from Chapter2.ch02.credit_card import CreditCard


class CreditCardExceptionalHandling(CreditCard):
    def charge(self, price):
        """Charge given price to the card, assuming sufficient credit limit.

        Args:
            price: numeric value to charge (must be positive)

        Returns:
            True if charge was processed; False if charge was denied.

        Raises:
            TypeError: if price is not a number
            ValueError: if price is negative
        """
        if not isinstance(price, (int, float)):
            raise TypeError('Price must be a number')
        if price <= 0:
            raise ValueError('Price must be positive')

        return super().charge(price)  # 调用父类的charge方法

    def make_payment(self, amount):
        """Process customer payment that reduces balance.

        Args:
            amount: numeric value to pay (must be positive)

        Raises:
            TypeError: if amount is not a number
            ValueError: if amount is negative
        """
        if not isinstance(amount, (int, float)):
            raise TypeError('Payment amount must be a number')
        if amount <= 0:
            raise ValueError('Payment amount must be positive')

        super().make_payment(amount)  # 调用父类的make_payment方法


card = CreditCardExceptionalHandling('John', 'Bank', '1234', 1000)

try:
    card.charge('abc')  # 会引发 TypeError
    card.charge(-50)  # 会引发 ValueError
    card.make_payment(0)  # 会引发 ValueError
except (TypeError, ValueError) as e:
    print(f"Error: {e}")
