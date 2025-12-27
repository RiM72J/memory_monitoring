import rclpy
from rclpy.node import Node
from std_msgs.msg import String 

class MemoryListener(Node):
    def __init__(self):
        super().__init__('memory_listener')
        self.create_subscription(String, 'memory_usage', self.cb, 10)
        self.get_logger().info("Listener started subscription")

    def cb(self, msg):
        self.get_logger().info(f"Received raw data: {msg.data}")

def main():
    rclpy.init()
    node = MemoryListener()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    rclpy.shutdown()
