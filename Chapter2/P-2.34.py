# 写一个Python程序，如输入一个文件，则输出一个柱形图标，以显示文档中每个字母出现的频率。
import sys
import matplotlib.pyplot as plt
from collections import Counter
import string


def main():
    filename = "P-2.34.txt"

    try:
        # 读取文件内容并转换为小写
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read().lower()
    except FileNotFoundError:
        print(f"错误：文件 '{filename}' 不存在")
        sys.exit(1)

    # 仅统计英文字母 (a-z)
    letters = [char for char in text if char in string.ascii_lowercase]
    counter = Counter(letters)  # 使用Counter计算字母频率

    # 准备绘图数据（按字母顺序排序）
    letters_sorted = sorted(counter.keys())
    frequencies = [counter[letter] for letter in letters_sorted]

    # 创建柱状图
    plt.figure(figsize=(12, 6))  # 设置图表大小
    bars = plt.bar(letters_sorted, frequencies, color='skyblue')  # 绘制柱状图

    # 在柱子上方添加频率数值
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2., height,
                 f'{int(height)}',
                 ha='center', va='bottom', fontsize=9)  # 居中显示数值

    # 设置图表标题和坐标轴标签
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置支持中文的字体
    plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题
    plt.title(f'文件 {filename} 中的字母频率分布')
    plt.xlabel('字母')
    plt.ylabel('出现次数')
    plt.grid(axis='y', linestyle='--', alpha=0.7)  # 添加网格线
    plt.tight_layout()  # 自动调整布局

    # 保存图表到文件
    plt.savefig("P-2.34.png")
    print("图表已保存为 'P-2.34.png'")


if __name__ == "__main__":
    main()  # 程序入口
