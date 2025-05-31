# 请修改2.4.1节的PredatoryCreditCard类，实现这样的功能：给用户分配一个每月最低付款额，作为账号的一部分，如果客户在下一个月周期之前没有连续的支付最低金额，
# 则要评估延迟的费用。
from ch02.credit_card import CreditCard


class PredatoryCreditCard(CreditCard):
    """An extension to CreditCard that compounds interest, fees, and minimum payments."""

    def __init__(self, customer, bank, acnt, limit, apr, min_payment):
        """Create a new predatory credit card instance.

        The initial balance is zero.

        customer    the name of the customer (e.g., 'John Bowman')
        bank        the name of the bank (e.g., 'California Savings')
        acnt        the account identifier (e.g., '5391 0375 9387 5309')
        limit       credit limit (measured in dollars)
        apr         annual percentage rate (e.g., 0.0825 for 8.25% APR)
        min_payment minimum monthly payment required (e.g., 20 for $20)
        """
        super().__init__(customer, bank, acnt, limit)
        self._apr = apr
        self._min_payment = min_payment  # 存储最低付款额
        self._min_payment_met = False  # 标记当月是否完成最低付款

    def charge(self, price):
        """Charge given price to the card, assuming sufficient credit limit.

        Return True if charge was processed.
        Return False and assess $5 fee if charge is denied.
        """
        success = super().charge(price)
        if not success:
            self._balance += 5  # assess penalty
        return success

    def make_payment(self, amount):
        """Process customer payment that reduces balance.
        Updates minimum payment status if payment meets or exceeds minimum.
        """
        super().make_payment(amount)
        # 仅当最低付款尚未完成时才更新状态
        if not self._min_payment_met and amount >= self._min_payment:
            self._min_payment_met = True

    def process_month(self):
        """Assess monthly interest and late fees."""
        # Assess APR first
        if self._balance > 0:
            monthly_factor = pow(1 + self._apr, 1 / 12)
            self._balance *= monthly_factor

        # Check if minimum payment was met
        if not self._min_payment_met and self._balance > 0:  # 延迟费检查逻辑
            self._assess_late_fee()

        # Reset payment status for new month
        self._min_payment_met = False

    def _assess_late_fee(self, late_fee=25):
        """Add late fee to balance for missing minimum payment."""
        # 处理延迟费评估
        self._balance += late_fee


card = PredatoryCreditCard("John", "Bank", "1234", 1000, 0.15, 20)  # 最低付款$20

card.charge(100)
card.make_payment(15)  # 低于最低付款
# ...月末处理时...
card.process_month()  # 将评估$25延迟费 + 利息

card.make_payment(20)  # 满足最低付款
# ...下月末处理...
card.process_month()  # 仅评估利息（无延迟费）
