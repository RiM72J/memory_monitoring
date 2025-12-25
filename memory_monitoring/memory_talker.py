import rclpy
from rclpy.node import Node
from std_msgs.msg import String 
import psutil

class MemoryTalker(Node):
    def __init__(self):
        super().__init__('memory_talker')
        
        self.pub = self.create_publisher(String, 'memory_usage', 10)
        self.create_timer(3.0, self.cb)

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
            name = top['name']
            usage = top['memory_percent']
            
        
            msg = String()
            msg.data = f"{name}: {usage:.1f}%"
            self.pub.publish(msg)

def main():
    rclpy.init()
    node = MemoryTalker()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    rclpy.shutdown()
