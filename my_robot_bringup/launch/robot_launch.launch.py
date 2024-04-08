
from launch import LaunchDescription
from launch_ros.actions import Node



def generate_launch_description():
    ld = LaunchDescription()
    remap_number_topic = ("number_pub", "my_number")

    number_publisher_node1 = Node(package="my_py_pkg",  executable="robot_news_station" , name= "robot_giskard",  
                                 parameters= [ {"robot_name":"giskard"}])
    
    number_publisher_node2 = Node(package="my_py_pkg",  executable="robot_news_station" , name= "robot_bb8",  
                                 parameters= [ {"robot_name":"bb8"}])
    
    number_publisher_node3 = Node(package="my_py_pkg",  executable="robot_news_station" , name= "robot_daneel",  
                                 parameters= [ {"robot_name":"daneel"}])
    
    number_publisher_node4 = Node(package="my_py_pkg",  executable="robot_news_station" , name= "robot_jander",  
                                 parameters= [ {"robot_name":"jander"}])
    
    number_publisher_node5 = Node(package="my_py_pkg",  executable="robot_news_station" , name= "robot_c3po",  
                                 parameters= [ {"robot_name":"c3po"}])
    
    number_subscriber = Node(package="my_py_pkg", executable="smartphone")

    
    ld.add_action(number_publisher_node1)
    ld.add_action(number_publisher_node2)
    ld.add_action(number_publisher_node3)
    ld.add_action(number_publisher_node4)
    ld.add_action(number_publisher_node5)
    ld.add_action(number_subscriber)




    return ld
