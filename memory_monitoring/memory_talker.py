import rclpy
from rclpy.node import Node
import psutil 

class MemoryTalker(Node):
    def __init__(self):
        super().__init__('memory_talker')
        self.create_timer(1.0, self.cb) 

    def cb(self):
        procs = []
        for p in psutil.process_iter(['name', 'memory_percent']):
            try:
                procs.append(p.info)
            except:
                pass
        
        sorted_procs = sorted(procs, key=lambda p: p['memory_percent'], reverse=True)
        if sorted_procs:
            top = sorted_procs[0]
            self.get_logger().info(f"Debug: {top['name']} is using {top['memory_percent']}%")

def main():
    rclpy.init()
    node = MemoryTalker()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    rclpy.shutdown()
