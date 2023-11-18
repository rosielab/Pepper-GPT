#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import JointState

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + ' LOGGING POSITION %s', data.position)

def listener():

    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber('joint_states', JointState, callback)


    rospy.spin()

if __name__ == '__main__':
    listener()