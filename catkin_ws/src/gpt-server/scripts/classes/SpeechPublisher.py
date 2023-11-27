from std_msgs.msg import String


class SpeechPublisher:

    def __init__(self):
        self.response_subscriber = rospy.Subscriber('model_response', String, self.process_response)
        pass

    def process_response(self, response_msg):
        '''
        Callback that processes the messages from the 
        '''
        pass
    
    