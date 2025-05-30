# 假设你在一个新的电子书阅读器的设计团队。你的读者将需要Python软件哪些主要的类和方法？你应该为这段代码设计一个继承关系图，但你不需要写任何实际的代码。
# 你的软件体系结构至少应该包括顾客购买新书的方式、查看他们购买书的清单以及阅读他们购买的书籍。

# classDiagram
#     Book <|-- EBook
#     Book <|-- AudioBook
#
#     User "1" *-- "*" Book : Purchased
#     User "1" o-- "*" ReadingSession
#
#     class User {
#         -user_id: str
#         -username: str
#         -purchased_books: List[Book]
#         +purchase_book(book: Book)
#         +list_purchased_books() List[Book]
#         +start_reading(book: Book) ReadingSession
#     }
#
#     class Book {
#         <<abstract>>
#         -book_id: str
#         -title: str
#         -author: str
#         -price: float
#         +get_info() dict
#     }
#
#     class EBook {
#         -content: str
#         -format: str
#         +get_content() str
#         +display_page(page: int)
#     }
#
#     class AudioBook {
#         -audio_file: bytes
#         -duration: float
#         +play()
#         +pause()
#     }
#
#     class Library {
#         -available_books: List[Book]
#         +add_book(book: Book)
#         +search_books(query: str) List[Book]
#     }
#
#     class Store {
#         -library: Library
#         +process_purchase(user: User, book: Book)
#         +get_book_details(book_id: str) Book
#     }
#
#     class ReadingSession {
#         -session_id: str
#         -book: Book
#         -current_page: int
#         -progress: float
#         +open_book()
#         +next_page()
#         +previous_page()
#         +jump_to_page(page: int)
#         +close_book()
#     }

# 代码渲染示例：https://mermaid-live.nodejs.cn/edit#pako:eNp9Vclu2zAQ_RWBJzm1AzuxHVkIAnTJLQWKBr20KoSxOJbZSqTKJYjr5t9LUl60JTrQ5HCW94aP9J5kgiKJSVaAUp8Y5BLKhAf2-yDE7-D232QS3Ltp1_jeUCbOG_X4TaEMEjJLSHBhfRJyYWc-Jg6-GJltQSHtuYqT61cEynj-iEoxwZuZPb46aF9b3Dcx1pAyGgdKy46ZQ4lde3XEkK4tKBUHD0zpHw7gz7PXu6OXdwrdEHsSo4ZPYQPTTrpwNJxPaZA6lTW3Zr5Bvi992r6DDdq3t7C2xCDTd3cNdi7zQDM000WvE2D0VshefyTLrOumEKAbBHLUKeMbYQlSlulXcd53gU4ywTVy3a2zEbKErtWXOQTYSu09ylRVwC6tIMfQDXHAuB69CuUkzxYccNZ0w1w_1juNqrFHjQRtT6FP3xUOm4dfgRVY-HrxB7aWIHft0k_AClgX-Kb0gNK3VKcQrOIOavtjUO58D_u6GwD1qIXEFqSihhkf8TYZSpFZUZ4UHrobFfv7Nw6GsbnT8wqkqC1VFTblOArOT8UAtvY9aIFUtW1A12cYTcEZKa1-0pNEWuoWubTp-icsKuR135uMOD7XidqHL_GJCaP6O79MWaVaDGvUe2SFOD4rR_WQMckloyTW0uCYlGhvhlsS34SE6C2WmJDYTiluwBQ6IQl3YRXw70KUx0gpTL4l8QYKZVemoqDx8KCfXJBTlB-F4ZrEs5lPQeI9ebaraXS5ms6ns2Vkp8tVFI3JzpqvV5fLxVV0tVjMp9FsFS1fxuSvrzq9nC-ub1zIYrW8uVpE8zFByqzKPh_-UtzPy3_NPOjx

# 体系结构说明：

# 核心类关系：
# User 聚合多个 Book（购买关系）
# User 组合多个 ReadingSession（阅读会话）
# Store 关联 Library（书籍库存）
# Book 作为抽象基类，被 EBook 和 AudioBook 继承
#
# 关键功能实现：
#
# 购买流程：
# User.purchase_book() 调用 Store.process_purchase()
# Store 从 Library 获取书籍数据
#
# 查看书单：
# User.list_purchased_books() 返回购买列表
#
# 阅读功能：
# User.start_reading() 创建 ReadingSession
# ReadingSession 处理翻页/跳转等操作
# EBook.display_page() 实现内容渲染
#
# 扩展性设计：
# 通过 Book 抽象类支持多种书籍类型
# ReadingSession 独立管理阅读状态
# Library 和 Store 分离库存与交易逻辑
