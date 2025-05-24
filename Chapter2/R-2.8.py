# 在代码段2-3的CreditCard类测试中修改第一个for循环的声明，使三张信用卡的其中之一超过其信用额度。哪张信用卡会出现这种情况？
from Chapter2.ch02.credit_card import CreditCard

if __name__ == '__main__':
    wallet = [
        CreditCard('John Bowman', 'California Savings', '5391 0375 9387 5309', 2500),
        CreditCard('John Bowman', 'California Federal', '3485 0399 3395 1954', 3500),
        CreditCard('John Bowman', 'California Finance', '5391 0375 9387 5309', 5000)
    ]

    for val in range(1, 59):  # 增大范围以使某张卡超限
        if not wallet[0].charge(val):
            print(f"Charge denied on wallet[0] for amount {val}")
        if not wallet[1].charge(2 * val):
            print(f"Charge denied on wallet[1] for amount {2 * val}")
        if not wallet[2].charge(3 * val):
            print(f"Charge denied on wallet[2] for amount {3 * val}")
            # 输出：Charge denied on wallet[2] for amount 174

    for c in range(3):
        print('Customer =', wallet[c].get_customer())
        print('Bank =', wallet[c].get_bank())
        print('Account =', wallet[c].get_account())
        print('Limit =', wallet[c].get_limit())
        print('Balance =', wallet[c].get_balance())
        while wallet[c].get_balance() > 100:
            wallet[c].make_payment(100)
            print('New balance =', wallet[c].get_balance())
        print()
