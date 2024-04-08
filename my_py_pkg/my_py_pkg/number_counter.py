#!/usr/bin/python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import  Int64
from example_interfaces.srv import SetBool
class numbersubscriber(Node):

    def __init__(self):

        super().__init__("number_counter")
        
        self.counter_ = 0 
        self.get_logger().info("numbercounter has been started")
        self.subscriber_ = self.create_subscription(Int64, "number_pub", self.subscriber_counter, 10)
        self.publisher_= self.create_publisher(Int64, "number_count", 10)
        
        
        self.server_ = self.create_service(SetBool, "rese_counter", self.boolset)
        self.get_logger().info(" server has been started")

    def subscriber_counter(self, msg):
        self.counter_ =msg.data+1
        new_msg = Int64()
        
        new_msg.data = self.counter_
        self.publisher_.publish(new_msg)
    
    def boolset(self, request, response):
        if request.data:
            self.counter_= 0
            response.success = True
            response.message = "counter is reset"
        else:
            response.success = False
            response.message = "counter is not reset"
        return response


        
    

def main(args= None):
    rclpy.init(args=args)
    node =numbersubscriber()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ =="__main__":
    main()