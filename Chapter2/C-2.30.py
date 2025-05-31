# 在2.4.1节的末尾，我们认为一个CreditCard类支持非公有制的方法模型_set_balance(b)，可以被子类使用以影响余额的改变，而不直接访问数据成员_balance。
# (在2.4.1节的末尾，我们认为CreditCard类可以添加一个非公有方法_set_balance，子类可以使用该方法来改变余额，而不直接访问数据成员_balance。)
# 相应地修改CreditCard类和PredatoryCreditCard类，实现这样一个模型。

class CreditCard:
    """A consumer credit card."""

    def __init__(self, customer, bank, acnt, limit):
        """Create a new credit card instance.

        The initial balance is zero.

        customer  the name of the customer (e.g., 'John Bowman')
        bank      the name of the bank (e.g., 'California Savings')
        acnt      the acount identifier (e.g., '5391 0375 9387 5309')
        limit     credit limit (measured in dollars)
        """
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0

    def get_customer(self):
        """Return name of the customer."""
        return self._customer

    def get_bank(self):
        """Return the bank's name."""
        return self._bank

    def get_account(self):
        """Return the card identifying number (typically stored as a string)."""
        return self._account

    def get_limit(self):
        """Return current credit limit."""
        return self._limit

    def get_balance(self):
        """Return current balance."""
        return self._balance

    def charge(self, price):
        """Charge given price to the card, assuming sufficient credit limit.

        Return True if charge was processed; False if charge was denied.
        """
        if price + self._balance > self._limit:  # if charge would exceed limit,
            return False  # cannot accept charge
        else:
            self._balance += price
            return True

    def make_payment(self, amount):
        """Process customer payment that reduces balance."""
        self._balance -= amount

    def _set_balance(self, new_balance):
        """Non-public method to set the balance (for internal use)."""
        # 允许安全地修改余额而不直接暴露内部变量。
        self._balance = new_balance


class PredatoryCreditCard(CreditCard):
    """An extension to CreditCard that compounds interest and fees."""

    def __init__(self, customer, bank, acnt, limit, apr):
        """Create a new predatory credit card instance.

        The initial balance is zero.

        customer  the name of the customer (e.g., 'John Bowman')
        bank      the name of the bank (e.g., 'California Savings')
        acnt      the acount identifier (e.g., '5391 0375 9387 5309')
        limit     credit limit (measured in dollars)
        apr       annual percentage rate (e.g., 0.0825 for 8.25% APR)
        """
        # 通过get_balance()获取当前余额，计算新值后通过_set_balance()更新。子类通过非公有方法_set_balance间接修改余额，避免直接访问父类的私有成员_balance。
        super().__init__(customer, bank, acnt, limit)  # call super constructor
        self._apr = apr

    def charge(self, price):
        """Charge given price to the card, assuming sufficient credit limit.

        Return True if charge was processed.
        Return False and assess $5 fee if charge is denied.
        """
        success = super().charge(price)  # call inherited method
        if not success:
            # 当需要添加罚金时，不再直接访问_balance
            current_balance = self.get_balance()
            self._set_balance(current_balance + 5)
        return success  # caller expects return value

    def process_month(self):
        """Assess monthly interest on outstanding balance."""
        current_balance = self.get_balance()
        # 计算复利时，不再直接修改_balance
        if current_balance > 0:
            # Convert APR to monthly multiplicative factor
            monthly_factor = pow(1 + self._apr, 1 / 12)
            new_balance = current_balance * monthly_factor
            self._set_balance(new_balance)
