# 写一个Python程序来模拟生态系统，其中包含两种类型的动物————熊和鱼。生态系统还包括一条河流，它被建模为一个比较大的列表。列表中的每一个元素都应该
# 是一个Bear对象、一个Fish对象或者None。在每一个时间步长，基于随机过程，每一个动物都试图进入一个相邻的列表位置或停留在原处。如果两只相同类型的动
# 物竞争同一单元格，那么它们留在原处，但它们创造了这种类型动物的新实例，实例放置在列表中的一个随机（即以前为None）位置。如果一头熊和一条鱼竞争，那
# 么鱼就会死亡（即它消失了）。
import random


class Bear:
    """熊类"""

    def __repr__(self):
        return 'B'


class Fish:
    """鱼类"""

    def __repr__(self):
        return 'F'


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

    # 第一遍：处理无冲突的移动和标记冲突
    for animal, old_idx, new_idx in plans:
        if new_idx not in conflicts:
            conflicts[new_idx] = []
        conflicts[new_idx].append((animal, old_idx))

    # 第二遍：解决冲突
    for new_idx, animals in conflicts.items():
        if len(animals) == 1:
            # 无冲突：直接移动
            animal, old_idx = animals[0]
            new_river[new_idx] = animal
        else:
            # 有冲突：检查动物类型
            types = set(type(a) for a, _ in animals)
            if len(types) == 1:
                # 相同类型：动物留在原位置，并繁殖
                animal_type = type(animals[0][0])
                # 所有动物保留在原位置
                for animal, old_idx in animals:
                    if new_river[old_idx] is None:
                        new_river[old_idx] = animal
                # 在随机空位繁殖新动物
                empty_positions = [i for i, x in enumerate(new_river) if x is None]
                if empty_positions:
                    spawn_pos = random.choice(empty_positions)
                    new_river[spawn_pos] = animal_type()
            else:
                # 不同类型：鱼死亡，熊移动
                for animal, old_idx in animals:
                    if isinstance(animal, Bear):
                        new_river[new_idx] = animal  # 熊占据位置
                        break  # 只需一个熊移动

    return new_river


def river_to_string(river):
    """将河流状态转换为字符串表示"""
    return ''.join(['.' if x is None else x.__repr__() for x in river])


# 运行模拟
if __name__ == "__main__":
    simulate_ecosystem(
        river_length=20,  # 河流长度
        steps=10,  # 时间步数
        initial_bears=3,  # 初始熊数量
        initial_fish=5  # 初始鱼数量
    )
