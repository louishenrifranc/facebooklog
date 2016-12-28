import os
import sys

sys.path.insert(0, os.path.abspath('..'))
import matplotlib.pyplot as plt
from messengerlog import MessengerLog

username = ''
password = ''
messenger = MessengerLog(username, password)

# Send a plot
X, y = [], []
for x in xrange(100):
    X.append(x)
    y.append(x * 2)
plt.plot(X, y)
messenger.send_plot(caption='New plot')

# Send a message
messenger.send_msg('Hello world')

# Send from the log file
messenger('H')
messenger('e')
messenger('l')
messenger('l')
messenger('o')
messenger.send_log_file()
