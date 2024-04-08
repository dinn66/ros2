#!/usr/bin/python3
import rclpy
from rclpy.node import Node
from my_robot_interfaces.msg import Ledstatearray
from my_robot_interfaces.srv import SetLed

class LedPanelNode(Node):
    def __init__(self):
        super().__init__("ledpanelnode")
        self.declare_parameter("led_states_array", [0,0,0])
        self.led_states_ = self.get_parameter("led_states_array").value
        self.publisher_ = self.create_publisher(Ledstatearray, "ledstates", 10)
        
        self.timer = self.create_timer(4.0, self.publish_ledstates)
        self.server_ = self.create_service(SetLed, "SetLed", self.callback_ledstatus)
        self.get_logger().info("Led panel has been started")


    def publish_ledstates(self):
        msg = Ledstatearray()
        msg.led_states = self.led_states_
        self.publisher_.publish(msg)

    def callback_ledstatus(self, request, response):
        led_number = request.led_number
        state = request.state
        if led_number >len(self.led_states_) or led_number <=0 or state not in [0,1]: 
            response.success = False
        self.led_states_[led_number-1]= state
        response.success = True
        self.publish_ledstates()
        return response
        


def main(args= None):
    rclpy.init(args=args)
    node = LedPanelNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=="__main__":
    main()
    
