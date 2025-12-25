# SPDX-FileCopyrightText: 2025 Your Name <your_email@domain.com>
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class MemoryListener(Node):
    def __init__(self):
        super().__init__('memory_listener')
        self.create_subscription(String, 'memory_usage', self.cb, 10)

    def cb(self, msg):
        # とりあえず受信したことをログに出すだけできてるかわからん
        self.get_logger().info(f"Received: {msg.data}")

def main():
    rclpy.init()
    node = MemoryListener()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    rclpy.shutdown()
