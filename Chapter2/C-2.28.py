# 2.4.1节的的PredatoryCreditCard类提供了process_month方法，可使模型完成每月一次的循环。请修改该类，实现这样的功能：在本月内，一旦用户完成十次呼叫，
# 就需要对其收取费用。每增加一个额外的呼叫，收取1美元的附加费。
from ch02.credit_card import CreditCard


class PredatoryCreditCard(CreditCard):
    """扩展版信用卡，增加利息、费用和超额呼叫收费"""

    def __init__(self, customer, bank, acnt, limit, apr):
        """创建新的高利贷信用卡实例

        customer  客户姓名（如 'John Bowman'）
        bank      银行名称（如 'California Savings'）
        acnt      账户标识符（如 '5391 0375 9387 5309'）
        limit     信用额度（美元）
        apr       年利率（如 0.0825 表示 8.25% APR）
        """
        super().__init__(customer, bank, acnt, limit)
        self._apr = apr
        self._charge_count = 0  # 本月呼叫次数计数器

    def charge(self, price):
        """处理信用卡消费请求

        如果超过10次呼叫，每次额外收取1美元附加费
        如果消费被拒绝，收取5美元罚款
        """
        # 增加呼叫计数
        self._charge_count += 1

        # 检查是否需要额外收费（第11次及以后的呼叫）
        if self._charge_count > 10:
            # 收取1美元附加费（即使消费被拒绝也要收费）
            # 使用super().charge确保不触发额外计数
            super().charge(1)
            print(f"附加费：第{self._charge_count}次呼叫收取1美元")

        # 处理原始消费请求
        success = super().charge(price)

        if not success:
            # 消费被拒绝时收取5美元罚款
            super().charge(5)  # 使用super()避免额外计数
            print(f"拒绝消费：收取5美元罚款")

        return success

    def process_month(self):
        """处理月末结算"""
        # 1. 计算利息
        if self._balance > 0:
            monthly_factor = pow(1 + self._apr, 1 / 12)
            self._balance *= monthly_factor
            print(f"利息计算：余额更新为${self._balance:.2f}")

        # 2. 重置呼叫计数器
        self._charge_count = 0
        print("月末处理：呼叫计数器已重置")


# 创建信用卡
card = PredatoryCreditCard("John Doe", "Bank of Python", "1234 5678 9012 3456", 1000, 0.15)

# 前10次呼叫免费
for i in range(1, 11):
    card.charge(10)
    print(f"消费${10}，余额: ${card.get_balance()}")

# 第11次呼叫（额外收费）
card.charge(20)  # 输出: "附加费：第11次呼叫收取1美元"
print(f"余额: ${card.get_balance()}")  # 20 + 1 = 21美元新增

# 尝试超额消费（被拒绝并罚款）
card.charge(1000)  # 输出: "附加费..." 和 "拒绝消费：收取5美元罚款"
print(f"余额: ${card.get_balance()}")  # 21 + 1 + 5 = 27美元

# 月末处理
card.process_month()  # 计算利息并重置计数器
