#!/usr/bin/python3
import rclpy
from rclpy.node import Node
from my_robot_interfaces.msg import Ledstatearray
from my_robot_interfaces.srv import SetLed
from functools import partial

class BatteryNode(Node):
    def __init__(self):
        super().__init__("battery_node")
        self.battery_state = "full"
        self.last_state = self.lastbattery()
        self.battery_timer = self.create_timer(0.1, self.check_battery_state)
        self.get_logger().info("Battery node is started")
    
    def lastbattery(self):
        secs, nsecs = self.get_clock().now().seconds_nanoseconds()
        return secs + nsecs / 1000000000.0
    
    
    def check_battery_state(self):
        time_now = self.lastbattery()
        if self.battery_state =="Full":
            if time_now - self.last_state > 4.0:
                self.battery_state = "Empty"
                self.get_logger().info("Battery is empty currently charging")
                self.last_state = time_now
                self.call_set_led_server(3,1)
        else:
            
            if time_now - self.last_state >6.0:
                self.battery_state = "Full"
                self.get_logger().info("Battery is full and discharging now")
                self.last_state = time_now
                self.call_set_led_server(3,0) 
    
    
    def call_set_led_server(self, led_number, state):
        client = self.create_client(SetLed, "SetLed")
        while not client.wait_for_service(1.0):
            self.logger().warn("Service is not started yet")
        request = SetLed.Request()
        request.led_number = led_number
        request.state = state
        future = client.call_async(request)
        
        future.add_done_callback(
            partial(self.battercall_response, led_number= led_number, state = state))
        
    def battercall_response(self, future, led_number, state):
        try:
            response = future.result()
            self.get_logger().info ( str(response.success))
        except Exception as e:
            self.logger().error("service call failed %r"%(e,))
        

def main(args= None):
    rclpy.init(args=args)
    node = BatteryNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=="__main__":
    main()
    
