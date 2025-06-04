# 写一个Python程序，模拟一个支持电子书阅读器的功能系统。你应该为用户在系统中提供“买”新书、查看他们所购买书的名单以及阅读所购买的书籍的方法。系统
# 应该使用实际的书籍（其版权已经过期并可在互联网上获得），为系统用户“购买”和阅读提供可用的书籍。
import os
import requests
from pathlib import Path
from textwrap import fill

# 确保书籍存储目录存在
BOOKS_DIR = Path("ebook_library")
BOOKS_DIR.mkdir(exist_ok=True)

# 公共领域书籍列表（古登堡计划中的书籍）
PUBLIC_DOMAIN_BOOKS = {
    "1": {
        "title": "Pride and Prejudice",
        "author": "Jane Austen",
        "url": "https://www.gutenberg.org/files/1342/1342-0.txt"
    },
    "2": {
        "title": "The Adventures of Sherlock Holmes",
        "author": "Arthur Conan Doyle",
        "url": "https://www.gutenberg.org/files/1661/1661-0.txt"
    },
    "3": {
        "title": "Frankenstein",
        "author": "Mary Shelley",
        "url": "https://www.gutenberg.org/files/84/84-0.txt"
    },
    "4": {
        "title": "A Tale of Two Cities",
        "author": "Charles Dickens",
        "url": "https://www.gutenberg.org/files/98/98-0.txt"
    },
    "5": {
        "title": "The Wonderful Wizard of Oz",
        "author": "L. Frank Baum",
        "url": "https://www.gutenberg.org/files/55/55-0.txt"
    }
}


class EBookReader:
    def __init__(self):
        self.purchased_books = []
        self.load_purchased_books()

    def load_purchased_books(self):
        """从文件加载已购书籍列表"""
        purchased_file = BOOKS_DIR / "purchased.txt"
        if purchased_file.exists():
            with open(purchased_file, 'r') as f:
                self.purchased_books = [line.strip() for line in f.readlines()]

    def save_purchased_books(self):
        """保存已购书籍列表到文件"""
        purchased_file = BOOKS_DIR / "purchased.txt"
        with open(purchased_file, 'w') as f:
            for book_id in self.purchased_books:
                f.write(f"{book_id}\n")

    def download_book(self, book_id):
        """下载电子书并保存到本地"""
        book_info = PUBLIC_DOMAIN_BOOKS.get(book_id)
        if not book_info:
            print("无效的书籍ID")
            return False

        # 检查是否已下载
        book_file = BOOKS_DIR / f"{book_id}.txt"
        if book_file.exists():
            return True

        # 下载书籍内容
        try:
            response = requests.get(book_info["url"])
            response.raise_for_status()

            # 保存书籍内容
            with open(book_file, 'w', encoding='utf-8') as f:
                f.write(response.text)
            return True
        except Exception as e:
            print(f"下载失败: {e}")
            return False

    def purchase_book(self):
        """购买新书功能"""
        print("\n可购买的书籍:")
        for book_id, info in PUBLIC_DOMAIN_BOOKS.items():
            print(f"{book_id}. {info['title']} by {info['author']}")

        choice = input("\n输入要购买的书籍编号 (或输入0返回): ")
        if choice == '0':
            return

        if choice in PUBLIC_DOMAIN_BOOKS:
            if choice in self.purchased_books:
                print("您已经购买过这本书了!")
            else:
                print(f"正在购买: {PUBLIC_DOMAIN_BOOKS[choice]['title']}...")
                if self.download_book(choice):
                    self.purchased_books.append(choice)
                    self.save_purchased_books()
                    print("购买成功!")
                else:
                    print("购买失败，请稍后再试")
        else:
            print("无效的选择")

    def view_purchased_books(self):
        """查看已购书籍列表"""
        if not self.purchased_books:
            print("\n您尚未购买任何书籍")
            return

        print("\n已购书籍列表:")
        for i, book_id in enumerate(self.purchased_books, 1):
            book_info = PUBLIC_DOMAIN_BOOKS[book_id]
            print(f"{i}. {book_info['title']} by {book_info['author']}")

    def read_book(self):
        """阅读已购书籍"""
        self.view_purchased_books()
        if not self.purchased_books:
            return

        try:
            choice = int(input("\n选择要阅读的书籍编号 (0返回): "))
            if choice == 0:
                return
            if 1 <= choice <= len(self.purchased_books):
                book_id = self.purchased_books[choice - 1]
                book_info = PUBLIC_DOMAIN_BOOKS[book_id]
                book_file = BOOKS_DIR / f"{book_id}.txt"

                if not book_file.exists():
                    print("找不到书籍文件，正在重新下载...")
                    if not self.download_book(book_id):
                        print("无法下载书籍")
                        return

                print(f"\n开始阅读: {book_info['title']}")
                self.display_book(book_file)
            else:
                print("无效的选择")
        except ValueError:
            print("请输入有效的数字")

    def display_book(self, file_path):
        """分页显示书籍内容"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            print(f"读取书籍失败: {e}")
            return

        # 清理Gutenberg文本的头部和尾部
        start_marker = "*** START OF THE PROJECT GUTENBERG EBOOK"
        end_marker = "*** END OF THE PROJECT GUTENBERG EBOOK"

        start_index = content.find(start_marker)
        if start_index != -1:
            start_index = content.find('\n', start_index) + 1

        end_index = content.find(end_marker)
        if end_index != -1:
            content = content[start_index:end_index]

        # 分页显示
        lines = content.split('\n')
        page_size = 20
        current_page = 0
        total_pages = (len(lines) + page_size - 1) // page_size

        while True:
            print(f"\n=== 第 {current_page + 1}/{total_pages} 页 ===\n")
            start = current_page * page_size
            end = min((current_page + 1) * page_size, len(lines))

            # 格式化输出（每行适当宽度）
            for line in lines[start:end]:
                if line.strip():
                    print(fill(line, width=80))

            print("\n" + "=" * 50)
            command = input("[N]下一页 [P]上一页 [Q]退出阅读: ").strip().lower()

            if command == 'n' and current_page < total_pages - 1:
                current_page += 1
            elif command == 'p' and current_page > 0:
                current_page -= 1
            elif command == 'q':
                break
            else:
                print("无效命令或已到书籍边界")


def main():
    reader = EBookReader()

    while True:
        print("\n===== 电子书阅读器系统 =====")
        print("1. 购买新书")
        print("2. 查看已购书籍")
        print("3. 阅读书籍")
        print("4. 退出系统")

        choice = input("请选择操作: ")

        if choice == '1':
            reader.purchase_book()
        elif choice == '2':
            reader.view_purchased_books()
        elif choice == '3':
            reader.read_book()
        elif choice == '4':
            print("感谢使用电子书阅读器，再见!")
            break
        else:
            print("无效选择，请重新输入")


if __name__ == "__main__":
    main()
