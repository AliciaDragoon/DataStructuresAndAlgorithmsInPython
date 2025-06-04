# 基于拥有抽象方法area()和perimeter()的Polygon类发展继承层次结构。实现拓展自基类的Triangle、Quadrilateral、Pentagon、Hexagon和
# Octagon类，伴随着具有明显意义的area()和perimeter()方法。同时实现IsoscelesTriangle、EquilateralTriangle、Rectangle和Square类，
# 他们有适当的继承关系。最后，写一个简单的程序，允许用户创建各种类型的多边形，输入它们的几何尺寸，输出面积和周长。附加功能：允许用户通过指定顶点坐标
# 输入多边形，并能够测试两个多边形是否相似。
import math
import numpy as np
from abc import ABC, abstractmethod


class Polygon(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def is_similar(self, other):
        """检查两个多边形是否相似（需在子类中实现）"""
        raise NotImplementedError("Similarity check not implemented for this polygon type")


class Triangle(Polygon):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self._validate_triangle()

    def _validate_triangle(self):
        sides = sorted([self.a, self.b, self.c])
        if sides[0] + sides[1] <= sides[2]:
            raise ValueError("Invalid triangle: sides violate triangle inequality")

    def area(self):
        # 使用海伦公式
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def perimeter(self):
        return self.a + self.b + self.c

    def is_similar(self, other):
        if not isinstance(other, Triangle):
            return False

        # 对两边进行排序以便比较比例
        sides1 = sorted([self.a, self.b, self.c])
        sides2 = sorted([other.a, other.b, other.c])

        # 计算比例因子
        ratios = [s1 / s2 for s1, s2 in zip(sides1, sides2)]

        # 检查所有比例是否相等
        return all(math.isclose(r, ratios[0], rel_tol=1e-5) for r in ratios)


class Quadrilateral(Polygon):
    def __init__(self, vertices):
        if len(vertices) != 4:
            raise ValueError("Quadrilateral requires exactly 4 vertices")
        self.vertices = np.array(vertices)
        self.sides = self._calculate_sides()

    def _calculate_sides(self):
        sides = []
        for i in range(4):
            j = (i + 1) % 4
            dx = self.vertices[j][0] - self.vertices[i][0]
            dy = self.vertices[j][1] - self.vertices[i][1]
            sides.append(math.sqrt(dx * dx + dy * dy))
        return sides

    def area(self):
        # 使用鞋带公式
        x = self.vertices[:, 0]
        y = self.vertices[:, 1]
        return 0.5 * abs(np.dot(x, np.roll(y, 1)) - np.dot(y, np.roll(x, 1)))

    def perimeter(self):
        return sum(self.sides)

    def is_similar(self, other):
        if not isinstance(other, Quadrilateral) or len(self.sides) != len(other.sides):
            return False

        # 对角度进行比较（简化版）
        angles1 = self._calculate_angles()
        angles2 = other._calculate_angles()

        # 排序角度并比较
        sorted_angles1 = sorted(angles1)
        sorted_angles2 = sorted(angles2)

        # 检查角度是否相等（允许浮点误差）
        angle_match = all(math.isclose(a1, a2, abs_tol=1e-5)
                          for a1, a2 in zip(sorted_angles1, sorted_angles2))

        # 检查边长比例
        sorted_sides1 = sorted(self.sides)
        sorted_sides2 = sorted(other.sides)
        ratios = [s1 / s2 for s1, s2 in zip(sorted_sides1, sorted_sides2)]

        return angle_match and all(math.isclose(r, ratios[0], rel_tol=1e-5) for r in ratios)

    def _calculate_angles(self):
        angles = []
        n = len(self.vertices)
        for i in range(n):
            a = self.vertices[i]
            b = self.vertices[(i + 1) % n]
            c = self.vertices[(i + 2) % n]

            ba = a - b
            bc = c - b

            dot_product = np.dot(ba, bc)
            mag_ba = np.linalg.norm(ba)
            mag_bc = np.linalg.norm(bc)

            angle = math.acos(dot_product / (mag_ba * mag_bc))
            angles.append(math.degrees(angle))
        return angles


class RegularPolygon(Polygon):
    def __init__(self, n_sides, side_length):
        self.n_sides = n_sides
        self.side_length = side_length

    def area(self):
        return (self.n_sides * self.side_length ** 2) / (4 * math.tan(math.pi / self.n_sides))

    def perimeter(self):
        return self.n_sides * self.side_length

    def is_similar(self, other):
        return isinstance(other, RegularPolygon) and self.n_sides == other.n_sides


# 正多边形子类
class Pentagon(RegularPolygon):
    def __init__(self, side_length):
        super().__init__(5, side_length)


class Hexagon(RegularPolygon):
    def __init__(self, side_length):
        super().__init__(6, side_length)


class Octagon(RegularPolygon):
    def __init__(self, side_length):
        super().__init__(8, side_length)


# 特殊三角形
class IsoscelesTriangle(Triangle):
    def __init__(self, base, leg):
        super().__init__(base, leg, leg)


class EquilateralTriangle(Triangle):
    def __init__(self, side):
        super().__init__(side, side, side)


# 特殊四边形
class Rectangle(Quadrilateral):
    def __init__(self, width, height):
        vertices = [
            [0, 0],
            [width, 0],
            [width, height],
            [0, height]
        ]
        super().__init__(vertices)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def is_similar(self, other):
        if not isinstance(other, Rectangle):
            return False
        ratio1 = self.width / self.height
        ratio2 = other.width / other.height
        return math.isclose(ratio1, ratio2, rel_tol=1e-5)


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)


# 主程序
def main():
    polygons = []

    while True:
        print("\n===== 多边形计算器 =====")
        print("1. 创建三角形")
        print("2. 创建等腰三角形")
        print("3. 创建等边三角形")
        print("4. 创建四边形（顶点）")
        print("5. 创建矩形")
        print("6. 创建正方形")
        print("7. 创建五边形")
        print("8. 创建六边形")
        print("9. 创建八边形")
        print("10. 计算所有多边形面积和周长")
        print("11. 检查两个多边形是否相似")
        print("12. 退出")

        choice = input("请选择操作: ")

        if choice == '12':
            break

        elif choice == '1':
            a = float(input("输入第一条边长: "))
            b = float(input("输入第二条边长: "))
            c = float(input("输入第三条边长: "))
            try:
                poly = Triangle(a, b, c)
                polygons.append(poly)
                print("三角形创建成功!")
            except ValueError as e:
                print(f"错误: {e}")

        elif choice == '2':
            base = float(input("输入底边长: "))
            leg = float(input("输入腰长: "))
            try:
                poly = IsoscelesTriangle(base, leg)
                polygons.append(poly)
                print("等腰三角形创建成功!")
            except ValueError as e:
                print(f"错误: {e}")

        elif choice == '3':
            side = float(input("输入边长: "))
            poly = EquilateralTriangle(side)
            polygons.append(poly)
            print("等边三角形创建成功!")

        elif choice == '4':
            print("输入四个顶点坐标 (x y):")
            vertices = []
            for i in range(4):
                coords = input(f"顶点 {i + 1}: ").split()
                if len(coords) != 2:
                    print("错误: 每个顶点需要两个坐标值")
                    break
                vertices.append([float(coords[0]), float(coords[1])])
            else:
                try:
                    poly = Quadrilateral(vertices)
                    polygons.append(poly)
                    print("四边形创建成功!")
                except ValueError as e:
                    print(f"错误: {e}")

        elif choice == '5':
            width = float(input("输入宽度: "))
            height = float(input("输入高度: "))
            poly = Rectangle(width, height)
            polygons.append(poly)
            print("矩形创建成功!")

        elif choice == '6':
            side = float(input("输入边长: "))
            poly = Square(side)
            polygons.append(poly)
            print("正方形创建成功!")

        elif choice == '7':
            side = float(input("输入边长: "))
            poly = Pentagon(side)
            polygons.append(poly)
            print("五边形创建成功!")

        elif choice == '8':
            side = float(input("输入边长: "))
            poly = Hexagon(side)
            polygons.append(poly)
            print("六边形创建成功!")

        elif choice == '9':
            side = float(input("输入边长: "))
            poly = Octagon(side)
            polygons.append(poly)
            print("八边形创建成功!")

        elif choice == '10':
            for i, poly in enumerate(polygons, 1):
                print(f"\n多边形 {i}:")
                print(f"类型: {type(poly).__name__}")
                print(f"面积: {poly.area():.2f}")
                print(f"周长: {poly.perimeter():.2f}")

        elif choice == '11':
            if len(polygons) < 2:
                print("需要至少两个多边形进行比较")
                continue

            print(f"当前有 {len(polygons)} 个多边形")
            idx1 = int(input("输入第一个多边形索引: ")) - 1
            idx2 = int(input("输入第二个多边形索引: ")) - 1

            if 0 <= idx1 < len(polygons) and 0 <= idx2 < len(polygons):
                poly1 = polygons[idx1]
                poly2 = polygons[idx2]

                if poly1.is_similar(poly2):
                    print("这两个多边形是相似的")
                else:
                    print("这两个多边形不相似")
            else:
                print("无效的索引")

        else:
            print("无效选择，请重新输入")


if __name__ == "__main__":
    main()
