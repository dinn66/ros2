#!/usr/bin/python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import  Int64

class numberpublisher(Node):

    def __init__(self):

        super().__init__("number_publisher")
        self.declare_parameter("number_to_publish", 2)
        self.declare_parameter("frequency", 1.0)
        self.publisher_= self.create_publisher(Int64, "number_pub", 10)
        self.counter_ = self.get_parameter("number_to_publish").value
        self.frequency = self.get_parameter("frequency").value
        
        self.timer_ = self.create_timer(1.0 / self.frequency, self.publish_news)
        self.get_logger().info("Robot News Station has started")

    def publish_news(self):
        
        msg = Int64()
        msg.data = self.counter_
        self.publisher_.publish(msg)
    

def main(args= None):
    rclpy.init(args=args)
    node = numberpublisher()
    
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ =="__main__":
    main()