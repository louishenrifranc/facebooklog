* Simple script to send plots and logs via Facebook Messenger. 
* Extend the idea of ![navoshta](https://github.com/navoshta/cloudlog) for Messenger.
* Usage for ML/DL: __Get noticed when training tasks is over.__

## Installation
```bash
git clone https://github.com/louishenrifranc/facebooklog.git
cd facebooklog
python setup.py install
```

## Usage
### Create a MessengerLog object
Need a facebook account (email, password)
```python
messenger = MessengerLog(username, password)
```
If you want to send to a thread group, fill the parameter ```thread_id```, with the thread id of the conversation, otherwise logs are sent to the same account as the sender.

### Send pyplot plot
```python
X, y = [], []
for x in xrange(100):
    X.append(x)
    y.append(x * 2)
plt.plot(X, y)
messenger.send_plot(caption='New plot')
```

### Log console outputs
* Replace all calls to ```print()``` by a call to the ```MessengerLog``` object.
* Send all the logs at the end with the command:
```python
messenger.send_log_file()
```

### Send a single message
```python
messenger.send_msg("Min loss: %f" % min_loss)
```
