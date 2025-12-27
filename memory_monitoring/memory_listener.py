# SPDX-FileCopyrightText: 2025 Your Name <your_email@domain.com>
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class MemoryListener(Node):
    def __init__(self):
        super().__init__('memory_listener')
        self.create_subscription(String, 'memory_usage', self.cb, 10)
        self.get_logger().info('Memory Listener Started')

    def cb(self, msg):
        try:
            text = msg.data
            parts = text.split(': ')
            if len(parts) == 2:
                name = parts[0]
                usage_str = parts[1].replace('%', '')
                usage = float(usage_str)

                if usage > 50.0:
                    self.get_logger().warn(
                        f'High Memory Alert! {name} is using {usage}%')
                else:
                    self.get_logger().info(f'Normal: {name} ({usage}%)')
        except Exception as e:
            self.get_logger().error(f'Parse error: {e}')


def main():
    rclpy.init()
    node = MemoryListener()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    rclpy.shutdown()
