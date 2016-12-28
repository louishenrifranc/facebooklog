from enum import Enum
import fbchat
import time
import os
from matplotlib.pyplot import savefig


class TypeMessage(Enum):
    str = 0
    jpg = 1


class MessengerLog(object):
    def __init__(self, email, password, root_path='log/', thread_id=None, debug=False):
        """
        Create an object to call for sending image and text via messenger

        Parameters
        ----------
        :param email: str
            Email of the facebook sender
        :param password: str
            Password of the sender's facebook sender
        :param root_path: str (default: 'log/'
            Location to save log file
        :param thread_id: int (default: None)
            Thread id of the conversation to send to. By default, messages are send to the same account as the sender
        :param debug: bool (default: False)
            Set true to debug fbchat
        """
        self.email = email
        self.client = fbchat.Client(email, password, debug)
        self.log_file = time.strftime('%Y-%m-%d_%H-%M-%S') + '_log.txt'
        self.root = root_path
        self.thread_id = thread_id
        if not os.path.exists(root_path):
            os.makedirs(root_path)

    def __call__(self, string):
        """
        Action function, when calling the object.
        Save a string in the log file before printing it

        Parameter
        ---------
        :param string: str
            Log info
        """
        print(string)
        with open(os.path.join(self.root, self.log_file), 'a') as f:
            f.write(string + '\n')

    def send_log_file(self):
        """
        Send the log file
        """
        with open(os.path.join(self.root, self.log_file), 'rb') as f:
            data = f.read()
        self.on_send(TypeMessage.str, data)

    def send_msg(self, message):
        """
        Send a message

        Parameter
        ----------
        :param message: str
            A message
        """
        self.on_send(TypeMessage.str, message)

    def send_plot(self, caption=None):
        """
        Send the current plot

        Parameters
        ----------
        :param caption: str
            Legend of the plot
        """
        plot_file = time.strftime('%Y-%m-%d_%H-%M-%S') + '.png'
        plot_path = os.path.join(self.root, plot_file)
        savefig(plot_path)
        self.on_send(TypeMessage.jpg, message=caption, filename=plot_path)

    def on_send(self, type_message, message, filename=None):
        contact = self.client.getUsers(self.email)[0].uid
        if self.thread_id is not None:
            contact = self.thread_id
        if type_message == TypeMessage.str:
            sent = self.client.send(contact, message)
        if type_message == TypeMessage.jpg:
            self.client.sendLocalImage(contact, message, image=filename)

