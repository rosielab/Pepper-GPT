#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from classes.LLMClient import LLMClient
from classes.SpeechPublisher import SpeechPublisher

url = "http://ollama:11434/api/generate"
prompt_scheme = {
        "model": "mistral",
        "prompt": None,
        "context": None
    }
llm_client = LLMClient(url="http://ollama:11434/api/generate", prompt_scheme=prompt_scheme)

def client_callback(data):
    """Callback triggered when the client_message topic receives a new message.
    Sends the message to the LLM.
    Args:
        data (String): The message published to the client_message topic.
    """
    rospy.loginfo("Sending prompt to LLM...")
    llm_client.send_prompt(data.data)

def main():
    rospy.init_node('gpt_server', anonymous=True)
    rospy.Subscriber('client_message', String, client_callback)
    speech_publisher = SpeechPublisher()
    rospy.spin()

if __name__ == '__main__':
    main()
