# 在之前的项目中写一个模拟器，但添加一个布尔值gender字段和一个浮点strength字段到每一个动物，使用Animal类作为基础类。如果两只同一类型的动物竞争，
# 如果它们是不同性别的动物，那么这种类型只创建一个新的实例；否则，如果两只相同类型和性别的动物竞争，那么只有力量更大的动物才会生存。
import random
from abc import ABC, abstractmethod


class Animal(ABC):
    """动物基类"""

    def __init__(self, gender=None, strength=None):
        # 随机生成性别（True为雄性，False为雌性）
        self.gender = gender if gender is not None else random.choice([True, False])
        # 随机生成力量值（0.0到1.0之间）
        self.strength = strength if strength is not None else round(random.uniform(0.1, 1.0), 2)

    @abstractmethod
    def __repr__(self):
        pass


class Bear(Animal):
    """熊类"""

    def __repr__(self):
        return '♂B' if self.gender else '♀B'


class Fish(Animal):
    """鱼类"""

    def __repr__(self):
        return '♂F' if self.gender else '♀F'


def simulate_ecosystem(river_length, steps, initial_bears, initial_fish):
    """
    模拟生态系统
    :param river_length: 河流长度
    :param steps: 模拟的时间步数
    :param initial_bears: 初始熊的数量
    :param initial_fish: 初始鱼的数量
    :return: 无，直接打印每个时间步的状态
    """
    # 初始化河流（None表示空位置）
    river = [None] * river_length

    # 随机放置初始熊
    for _ in range(initial_bears):
        pos = random.randint(0, river_length - 1)
        while river[pos] is not None:  # 确保位置为空
            pos = random.randint(0, river_length - 1)
        river[pos] = Bear()

    # 随机放置初始鱼
    for _ in range(initial_fish):
        pos = random.randint(0, river_length - 1)
        while river[pos] is not None:
            pos = random.randint(0, river_length - 1)
        river[pos] = Fish()

    print("初始状态:", river_to_string(river))

    # 模拟每个时间步
    for step in range(1, steps + 1):
        river = simulate_step(river)
        print(f"时间步 {step}: {river_to_string(river)}")
        # 计算当前动物数量
        bears = sum(1 for a in river if isinstance(a, Bear))
        fish = sum(1 for a in river if isinstance(a, Fish))
        print(f"  熊: {bears}只, 鱼: {fish}只")


def simulate_step(river):
    """执行一个时间步的模拟"""
    n = len(river)
    # 存储每个位置的移动计划（动物和目标位置）
    plans = []

    # 收集所有动物的移动计划
    for idx, animal in enumerate(river):
        if animal is not None:
            # 随机选择移动方向：-1(左), 0(不动), 1(右)
            move = random.choice([-1, 0, 1])
            target_idx = idx + move
            # 边界检查
            target_idx = max(0, min(n - 1, target_idx))
            plans.append((animal, idx, target_idx))

    # 初始化新状态和冲突解决标记
    new_river = [None] * n
    # 存储移动到同一位置的动物
    conflicts = {}
    # 存储新繁殖的动物
    newborns = []

    # 第一遍：处理无冲突的移动和标记冲突
    for animal, old_idx, new_idx in plans:
        if new_idx not in conflicts:
            conflicts[new_idx] = []
        conflicts[new_idx].append(animal)

    # 第二遍：解决冲突
    for new_idx, animals in conflicts.items():
        if len(animals) == 1:
            # 无冲突：直接移动
            new_river[new_idx] = animals[0]
        else:
            # 有冲突：检查动物类型
            types = {type(a) for a in animals}

            # 熊和鱼混合：熊吃掉鱼
            if Bear in types and Fish in types:
                # 找出最强的熊
                bears = [a for a in animals if isinstance(a, Bear)]
                strongest_bear = max(bears, key=lambda x: x.strength)
                new_river[new_idx] = strongest_bear
            # 同类型动物冲突
            else:
                animal_type = type(animals[0])
                # 按性别分组
                males = [a for a in animals if a.gender]
                females = [a for a in animals if not a.gender]

                # 有不同性别的动物 - 繁殖
                if males and females:
                    # 选择最强的雄性和雌性进行繁殖
                    strongest_male = max(males, key=lambda x: x.strength)
                    strongest_female = max(females, key=lambda x: x.strength)

                    # 创建后代（力量为父母平均值，性别随机）
                    new_strength = round((strongest_male.strength + strongest_female.strength) / 2, 2)
                    new_gender = random.choice([True, False])
                    newborn = animal_type(gender=new_gender, strength=new_strength)
                    newborns.append(newborn)

                    # 当前位置由力量最大的动物占据
                    all_animals = males + females
                    winner = max(all_animals, key=lambda x: x.strength)
                    new_river[new_idx] = winner
                # 只有单一性别 - 强者生存
                else:
                    winner = max(animals, key=lambda x: x.strength)
                    new_river[new_idx] = winner

    # 第三遍：放置新繁殖的动物
    for newborn in newborns:
        # 寻找空位置放置新动物
        empty_positions = [i for i, x in enumerate(new_river) if x is None]
        if empty_positions:
            spawn_pos = random.choice(empty_positions)
            new_river[spawn_pos] = newborn

    return new_river


def river_to_string(river):
    """将河流状态转换为字符串表示"""
    return ''.join(['.' if x is None else x.__repr__() for x in river])


# 运行模拟
if __name__ == "__main__":
    print("=== 生态系统模拟 (带性别和力量属性) ===")
    print("♂B: 雄性熊, ♀B: 雌性熊, ♂F: 雄性鱼, ♀F: 雌性鱼")
    simulate_ecosystem(
        river_length=15,  # 河流长度
        steps=20,  # 时间步数
        initial_bears=3,  # 初始熊数量
        initial_fish=5  # 初始鱼数量
    )
