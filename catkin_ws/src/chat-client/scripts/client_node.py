#!/usr/bin/env python3
# Software License Agreement (BSD License)
#
# Copyright (c) 2008, Willow Garage, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following
#    disclaimer in the documentation and/or other materials provided
#    with the distribution.
#  * Neither the name of Willow Garage, Inc. nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
# Revision $Id$

## Simple talker demo that published std_msgs/Strings messages
## to the 'chatter' topic

import rospy
import threading
import requests
import json
from std_msgs.msg import String

url = "http://ollama:11434/api/generate"
data = {
    "model": "mistral",
    "prompt": None,
    "context": None
}

def client_input():
    while not rospy.is_shutdown():
        client_input = input("Talk to Pepper: ")
        # pub = rospy.Publisher('client_message', String, queue_size=1)
        # pub.publish(String(client_input))
        data["prompt"] = f"Your name is Pepper, you are a human having a conversation with a friend. Please keep your responses to the following prompt short and brief. Prompt: {client_input}"
        response = requests.post(url, json=data, stream=True)
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
        # Process the streaming data, for example, iterate over lines
            for line in response.iter_lines(decode_unicode=True):
                if line:
                    response_data = json.loads(line)
                    if response_data["done"]:
                        data["context"] = response_data["context"]
                    print(response_data)
                else:
                    print(f"Error: {response.status_code}, {response.text}")

if __name__ == '__main__':
    try:
        client_input_thread = threading.Thread(target=client_input)
        rospy.loginfo("Starting Client Thread:")
        client_input_thread.start()
    except rospy.ROSInterruptException:
        pass

