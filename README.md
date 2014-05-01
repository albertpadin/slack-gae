slack-gae
=========

Simple Slack library for sending chat messages to slack from Python on Google App Engine

###Setup

1. Copy the slack folder to your appengine project directory.
2. Activate `deferred: on` in your `app.yaml` file builtins.


app.yaml
```
builtins:
- deferred: on
```


Sending a message
```
import slack
...
slack.post_to_slack(channel='#general', message='Hello World!', username='gaebot')
```