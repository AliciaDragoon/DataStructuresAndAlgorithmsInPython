# 编写一个Python程序，输入一个由空格分隔的单词列表，并输出列表中的每个单词出现的次数。在这一点上，你不需要担心效率，因为这个问题会在这本书后面的部分予以解决。
def count_words(words_list):
    """统计单词列表中每个单词的出现次数"""

    words = words_list.split()
    word_counts = {}

    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    print("\n单词出现次数统计：")
    for word, count in word_counts.items():
        print(f"'{word}': {count}次")


if __name__ == "__main__":
    words_list = "apple banana orange apple pear banana apple"
    count_words(words_list)

# 输出：
# 'apple': 3次
# 'banana': 2次
# 'orange': 1次
# 'pear': 1次
