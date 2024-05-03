#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def send_ros_message(data):
    rospy.init_node('ros_interface_node')
    pub = rospy.Publisher('/keyboard_events', String, queue_size=10)
    rospy.loginfo(f"Sending character: {data}")
    pub.publish(data)
