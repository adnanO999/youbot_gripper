#!/usr/bin/env python3

from time import sleep
import rospy
from sensor_msgs.msg import JointState
from std_msgs.msg import Header
import numpy as np
import time



def publish_joint_angles(joint_angles_list, rate=100):
    pub = rospy.Publisher('/joint_states', JointState, queue_size=10)
    rospy.init_node('joint_state_publisher', anonymous=True)

    joint_state_msg = JointState()
    joint_state_msg.header = Header()
    joint_state_msg.name = ['joint_1', 'joint_2']

    rate = rospy.Rate(rate)
    
    for joint_angles in joint_angles_list:
        joint_state_msg.position = joint_angles
        for _ in range(10):  
            joint_state_msg.header.stamp = rospy.Time.now()
            pub.publish(joint_state_msg)
            rate.sleep()
        rospy.sleep(0.1)  
        # time.sleep(delay)  

if __name__ == '__main__':
    try:
        while not rospy.is_shutdown():
            distance = input("enter the desired gripper distance: ")
            joint_angles_list = []
            joint_angles_list.append([0.5*float(distance), -0.5*float(distance)])

            publish_joint_angles(joint_angles_list, rate=25)
    except rospy.ROSInterruptException:
        pass