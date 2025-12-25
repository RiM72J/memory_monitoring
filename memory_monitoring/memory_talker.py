import rclpy
from rclpy.node import Node

class MemoryTalker(Node):
    def __init__(self):
        super().__init__('memory_talker')
        self.get_logger().info("Talker Node Created (Empty)")

def main():
    rclpy.init()
    node = MemoryTalker()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    rclpy.shutdown()
