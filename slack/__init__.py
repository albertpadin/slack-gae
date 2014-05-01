import json
from google.appengine.ext import deferred
from google.appengine.api import urlfetch

SLACK_TOKEN = 'LiFfS1RL6RxuincoAod8zM5A'
API_BASE_URL = 'https://symph.slack.com/services/hooks/incoming-webhook?token={token}'

def send_to_slack(channel, message, username=None):
    """
    Sample payload:
        {   
            "channel": "#general",
            "username": "webhookbot",
            "text": "This is posted to #general and comes from a bot named webhookbot.",
            "icon_emoji": ":ghost:"
        }
    """
    
    url = API_BASE_URL.format(token=SLACK_TOKEN)

    content = {"channel": channel, "text": message}
    if username:
        content['username'] = username
    urlfetch.fetch(url, payload=json.dumps(content), method=urlfetch.POST)


def post_to_slack(channel, message, username=None):
    deferred.defer(send_to_slack, channel, message, username)
    return

