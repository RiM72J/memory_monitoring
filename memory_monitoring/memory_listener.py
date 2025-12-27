import rclpy
from rclpy.node import Node

class MemoryListener(Node):
    def __init__(self):
        super().__init__('memory_listener')
        self.get_logger().info("Listener Node Created (Waiting for logic...)")

def main():
    rclpy.init()
    node = MemoryListener()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    rclpy.shutdown()
