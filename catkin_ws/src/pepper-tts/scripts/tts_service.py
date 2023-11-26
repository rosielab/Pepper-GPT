#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import JointState
from std_msgs.msg import String
from naoqi_bridge_msgs.msg import AudioBuffer

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + ' LOGGING DATA %s', data)
    # pub = rospy.Publisher('speech', String, queue_size=1)
    # pub.publish(String("Received joint data"))

def listener():

    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber('audio', AudioBuffer, callback)

    rospy.spin()

if __name__ == '__main__':
    listener()