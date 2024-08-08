#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import JointState
from std_msgs.msg import Header

def publish_initial_joint_states():
    pub = rospy.Publisher('/joint_states', JointState, queue_size=10)
    rospy.init_node('initial_joint_state_publisher', anonymous=True)
    rate = rospy.Rate(10)  

    joint_state_msg = JointState()
    joint_state_msg.header = Header()
    joint_state_msg.name = ['joint_1', 'joint_2']
    joint_state_msg.position = [0.018, -0.018]

    
    for _ in range(10):  
        joint_state_msg.header.stamp = rospy.Time.now()
        pub.publish(joint_state_msg)
        rate.sleep()
        rospy.sleep(0.1)

if __name__ == '__main__':
    try:
        publish_initial_joint_states()
    except rospy.ROSInterruptException:
        pass
