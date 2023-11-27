#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from classes.LLMClient import LLMClient

url = "http://ollama:11434/api/generate"
data = {
    "model": "mistral",
    "prompt": None,
    "context": None
}
llm_client = LLMClient(url="http://ollama:11434/api/generate", 
                        prompt_scheme=data)
def callback(data):
    rospy.loginfo("Sending prompt to LLM...")
    llm_client.send_prompt(data.data)

def listener():
    rospy.init_node('gpt-server', anonymous=True)
    rospy.Subscriber('client_message', String, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
