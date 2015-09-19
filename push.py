import requests
import json
from config import config

PUSHBULLET_API_URL = 'https://api.pushbullet.com/v2/pushes'
PUSHBULLET_API_KEY = config.get('PUSHBULLET_API_KEY')
PUSHBULLET_IDEN_KEY = config.get('PUSHBULLET_IDEN_KEY')


def send_push(stream_data):
    """Send pushbullet notifications - Type: Link"""
    headers = {'content-type': 'application/json'}
    name = stream_data['name']
    status = stream_data['status']
    url = stream_data['url']
    data = {'type': 'link',
            'title': '{0} is now streaming!'.format(name),
            'body': status,
            'url': url,
            }
    # If iden key not set then push to all devices
    if PUSHBULLET_IDEN_KEY:
        data['device_iden'] = PUSHBULLET_IDEN_KEY
    req = requests.post(PUSHBULLET_API_URL,
                        data=json.dumps(data),
                        headers=headers,
                        auth=(PUSHBULLET_API_KEY, '')
                        )
    if req.status_code == requests.codes.ok:
        return True
    return False
