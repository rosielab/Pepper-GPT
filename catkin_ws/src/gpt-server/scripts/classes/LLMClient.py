import requests
import json
import rospy
from std_msgs.msg import String


class LLMClient:

    def __init__(self, url, prompt_scheme):
        self.url = url
        self.prompt_scheme = prompt_scheme
        self.prompt_prefix = "Your name is Pepper, you are a human having a \
                            conversation with a friend. Please keep your \
                            responses to the following prompt short and brief. \
                            Prompt: "
        self.publisher = rospy.Publisher('model_response', String, queue_size=1)

    def send_prompt(self, prompt):
        """Make a request to the local LLM that contains the given prompt.
        The request response will be streamed to the /model_response topic.

        Args:
            prompt (str): The prompt provided by the text client.
        """
        self.prompt_scheme["prompt"] = self.prompt_prefix + str(prompt)
        response = requests.post(self.url, json=self.prompt_scheme, stream=True)

        if response.status_code == 200:
            for line in response.iter_lines(decode_unicode=True):
                if line:
                    response_data = json.loads(line)
                    self.publisher.publish(String(response_data["response"]))
                    if response_data["done"]:
                        self.prompt_scheme["context"] = response_data["context"]
                else:
                    print(f"Error: {response.status_code}, {response.text}")

