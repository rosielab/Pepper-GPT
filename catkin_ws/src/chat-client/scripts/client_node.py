#!/usr/bin/env python3
import rospy
import threading
import requests
import json
from std_msgs.msg import String


def client_input():
    while not rospy.is_shutdown():
        client_input = input("Talk to Pepper: ")
        pub = rospy.Publisher('client_message', String, queue_size=1)
        pub.publish(String(client_input))

if __name__ == '__main__':
    try:
        rospy.init_node('gpt_text_client', anonymous=True)
        client_input_thread = threading.Thread(target=client_input)
        rospy.loginfo("Starting Client Thread:")
        client_input_thread.start()
    except rospy.ROSInterruptException:
        pass

