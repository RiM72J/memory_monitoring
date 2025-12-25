def main():
    rclpy.init()
    node = MemoryTalker()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    rclpy.shutdown()
