import rospy
import string
from std_msgs.msg import String


class SpeechPublisher:
    """Class to handle the processing and publishing of the 
    response messages from the LLM.
    """

    def __init__(self):
        self.response_subscriber = rospy.Subscriber('model_response', String, self.process_response)
        self.speech_publisher = rospy.Publisher('speech', String, queue_size=1)
        self.current_sentence = []

    def process_response(self, response_msg):
        """Aggregate LLM response messages into complete sentences. Publish
        the sentences to the /speech topic for Pepper.
        
        Args:
            response_msg (String): The response message from the LLM published to the /model_response topic.
        """
        punctuation = "!.?"
        if response_msg.data in punctuation:
            self.current_sentence.append(response_msg.data)
            completed_sentence = " ".join(self.current_sentence)
            self.speech_publisher.publish(String(completed_sentence))
            self.current_sentence = []
            rospy.loginfo(f"Completed a sentence = {completed_sentence}")
        else:
            self.current_sentence.append(response_msg.data)
            
    