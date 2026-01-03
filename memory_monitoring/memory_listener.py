# SPDX-FileCopyrightText: 2025 Ryomu Inukai
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
            if len(parts) == 3:
                status = parts[0]
                name = parts[1]
                usage = parts[2]

                log_msg = f'{status}: {name} ({usage})'

                if status == 'Warn':
                    self.get_logger().warn(log_msg)
                else:
                    self.get_logger().info(log_msg)
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
