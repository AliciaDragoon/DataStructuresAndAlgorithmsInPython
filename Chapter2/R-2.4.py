# 编写一个Python类Flower。该类有str、int、float类型三种实例变量，分别代表花的名字、花瓣的数量和价格。该类必须包括一个构造函数，该构造函数给每个变量初始化一个合适的值。
# 该类应该包含设置和检索每种类型值的方法。
class Flower:
    def __init__(self, name: str = "Unknown", petals: int = 0, price: float = 0.0):
        """
        构造函数初始化花的属性
        :param name: 花名 (str)
        :param petals: 花瓣数 (int)
        :param price: 价格 (float)
        """
        self._name = name
        self._petals = petals
        self._price = price

    # 名称属性的getter/setter
    def get_name(self) -> str:
        """返回花名"""
        return self._name

    def set_name(self, name: str):
        """设置花名"""
        if not isinstance(name, str):
            raise TypeError("花名必须是字符串类型")
        self._name = name

    # 花瓣数量的getter/setter
    def get_petals(self) -> int:
        """返回花瓣数量"""
        return self._petals

    def set_petals(self, petals: int):
        """设置花瓣数量"""
        if not isinstance(petals, int):
            raise TypeError("花瓣数量必须是整数")
        if petals < 0:
            raise ValueError("花瓣数量不能为负数")
        self._petals = petals

    # 价格的getter/setter
    def get_price(self) -> float:
        """返回价格"""
        return self._price

    def set_price(self, price: float):
        """设置价格"""
        if not isinstance(price, (float, int)):
            raise TypeError("价格必须是数值类型")
        if price < 0:
            raise ValueError("价格不能为负数")
        self._price = float(price)  # 确保转换为float


rose = Flower("Rose", 12, 3.99)
print(f"{rose.get_name()}: {rose.get_petals()} petals, ${rose.get_price():.2f}")
# 输出：Rose: 12 petals, $3.99
rose.set_price(4.49)  # 更新价格
rose.set_petals(15)  # 更新花瓣数
print(f"{rose.get_name()}: {rose.get_petals()} petals, ${rose.get_price():.2f}")
# 输出：Rose: 15 petals, $4.49
