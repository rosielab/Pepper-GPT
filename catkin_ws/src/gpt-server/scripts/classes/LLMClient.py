import requests
import json


class LLMClient:

    def __init__(self, url, prompt_scheme, publisher):
        self.url = url
        self.prompt_scheme = prompt_scheme
        self.prompt_prefix = "Your name is Pepper, you are a human having a \
                            conversation with a friend. Please keep your \
                            responses to the following prompt short and brief. \
                            Prompt: "
        self.publisher = publisher

    def send_prompt(self, prompt):
        self.prompt_scheme["prompt"] = self.prompt_prefix + str(prompt)
        response = requests.post(self.url, json=self.prompt_scheme, stream=True)

        # maybe pass a thread off to handle_prompt_response that will then deal with the response to the prompt realtime
        # ORRRR NOTE: Just everytime you see punctuation, publish the sentence to the /speech topic the throttling will come ..
        # before the send_prompt is called. so like in the base server node

        # figure out how to live process the below section so that we can divide up the response and send it to the speech
        # might have to be a part of a different function.
        if response.status_code == 200:
            for line in response.iter_lines(decode_unicode=True):
                if line:
                    response_data = json.loads(line)
                    if response_data["done"]:
                        self.prompt_scheme["context"] = response_data["context"]
                    # self.publisher.publish(String(response_data))
                    print(response_data)
                else:
                    print(f"Error: {response.status_code}, {response.text}")

    def handle_prompt_response(self):
        pass
