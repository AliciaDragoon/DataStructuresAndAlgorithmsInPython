# 从下面的类的集合中画一个类的继承图：
# ·Goat类拓展了object类，增加了实例变量_tail以及方法milk()和jump()
# ·Pig类拓展了object类，增加了实例变量_nose以及方法eat(food)和wallow()
# ·Horse类拓展了object类，增加了实例变量_height和_color以及方法run()和jump()
# ·Racer类拓展了Horse类，增加了方法race()
# ·Equestrian类拓展了Horse类，增加了实例变量_weight以及方法trot()和is_trained()
#
# 使用Mermaid 渲染类图,语法参考：https://mermaid.nodejs.cn/syntax/classDiagram.html
# 代码渲染示例：https://mermaid-live.nodejs.cn/edit#pako:eNqVk11PgzAUhv_Kcq5mxpYBZYzGOzV6Y2K8NCRLhTPoLO0sJVPn_rt8jA3ELLEXbc_bnqfvado9RCpGoBAJlue3nCWaZaEclU29bjAyo-vv6XR0r5gZqk88GYoPSufYyPW0UZ9ZhHqg3r0XmBvNmWyWmr620jL3jXYYbqg8tctVm64M4-IcTzIu3sZXHWFTZNtW-ANYltPnSdVWUqcjM-O1UnEXuWNCqN0FaFNtD5siT1LTVSIllO5QdSH_Y7y-3O4ZE10qFxLO9953tvvlbGK0Mj0nPF8ZzbjE-IQHCxLNY6BGF2hBhjpjVQg1OgSTYoYh0HIa45oVwoQQyipty-SLUlmbqVWRpEDXTORlVGxjZvD4Ik9bUMaob1QhDVCvJgDdwwdQm5DZ3FkGQeB7vk8CsrDgE6gfzAJ3Yfue69seCdzlwYKv-sz5bOHMl8R2FsR3iO_axAKMuVH68fgjquHwA6qY46I
# classDiagram
#     object <|-- Goat
#     object <|-- Pig
#     object <|-- Horse
#     Horse <|-- Racer
#     Horse <|-- Equestrian
#
#     class object {
#     }
#
#     class Goat {
#         -_tail
#         +milk()
#         +jump()
#     }
#
#     class Pig {
#         -_nose
#         +eat(food)
#         +wallow()
#     }
#
#     class Horse {
#         -_height
#         -_color
#         +run()
#         +jump()
#     }
#
#     class Racer {
#         +race()
#     }
#
#     class Equestrian {
#         -_weight
#         +trot()
#         +is_trained()
#     }
