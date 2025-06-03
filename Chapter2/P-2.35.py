# 写一组Python类，可以模拟网络应用程序的其中一方Alice，定期创建一组她想发给Bob的包。互联网进程不断检查是否Alice有想要发送的包，如果有，就发送至
# Bob的计算机，Bob定期检查自己的计算机，以确定是否收到来自Alice的包，如果有，他将阅读并删除包。
import random
import time
from dataclasses import dataclass
from typing import List, Optional
from datetime import datetime


@dataclass
class Packet:
    """表示数据包，包含内容和时间戳"""
    content: str
    timestamp: datetime = datetime.now()


class Alice:
    """
        维护一个发件箱(outbox),
        可以生成随机数据包,
        提供检查是否有数据包待发送的方法
    """

    def __init__(self):
        self.outbox: List[Packet] = []

    def generate_packets(self, num_packets: int = 1) -> None:
        """定期生成要发送给Bob的数据包"""
        for _ in range(num_packets):
            content = f"Message {random.randint(1000, 9999)}"
            self.outbox.append(Packet(content))
            print(f"Alice created packet: {content}")

    def has_packets(self) -> bool:
        """检查是否有待发送的数据包"""
        return len(self.outbox) > 0

    def get_packet(self) -> Optional[Packet]:
        """获取一个待发送的数据包(从队列中移除)"""
        if self.outbox:
            return self.outbox.pop(0)
        return None


class Internet:
    """模拟网络传输过程(添加随机延迟)"""

    @staticmethod
    def transfer_packet(packet: Packet) -> Packet:
        """模拟网络传输过程(可能添加延迟或丢包)"""
        # 模拟网络延迟
        time.sleep(random.uniform(0.1, 0.5))
        return packet


class Bob:
    """
        维护一个收件箱(inbox)
        可以接收数据包
        定期检查并处理收件箱中的消息
    """

    def __init__(self):
        self.inbox: List[Packet] = []

    def receive_packet(self, packet: Packet) -> None:
        """接收来自Alice的数据包"""
        self.inbox.append(packet)
        print(f"Bob received packet: {packet.content}")

    def check_inbox(self) -> None:
        """检查并处理收件箱中的消息"""
        if self.inbox:
            packet = self.inbox.pop(0)
            print(f"Bob read and deleted packet: {packet.content}")
        else:
            print("Bob's inbox is empty")


def simulate_communication(duration: int = 10):
    """模拟Alice和Bob之间的通信"""
    alice = Alice()
    bob = Bob()

    start_time = time.time()

    while time.time() - start_time < duration:
        # Alice随机生成数据包
        if random.random() < 0.3:  # 30%概率生成数据包
            alice.generate_packets(random.randint(1, 3))

        # 网络检查并传输数据包
        if alice.has_packets():
            packet = alice.get_packet()
            if packet:  # 确保有数据包
                transferred_packet = Internet.transfer_packet(packet)
                bob.receive_packet(transferred_packet)

        # Bob定期检查收件箱
        if random.random() < 0.4:  # 40%概率检查收件箱
            bob.check_inbox()

        time.sleep(0.5)  # 模拟时间间隔


if __name__ == "__main__":
    simulate_communication()
